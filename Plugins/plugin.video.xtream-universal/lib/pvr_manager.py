# -*- coding: utf-8 -*-
"""
Módulo de integração com PVR (pvr.iptvsimple) para Xtream Universal.
Gerencia sincronização de canais, EPG e favoritos PVR.
Baseado nas melhores práticas do XStream Player.
"""
import json
import os
import time
import xml.etree.ElementTree as ET
import urllib.parse
import unicodedata
import re

import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs


ADDON_ID = 'plugin.video.xtream-universal'
LOG_TAG = '[Xtream Universal PVR]'

# ─────────────────────────────────────────────────────────────
# Utilitários de log
# ─────────────────────────────────────────────────────────────

def _log(msg):
    xbmc.log(f'{LOG_TAG} {msg}', xbmc.LOGINFO)


def _notify(title, msg, icon=xbmcgui.NOTIFICATION_INFO, time_ms=4000):
    xbmcgui.Dialog().notification(title, msg, icon, time_ms)


# ─────────────────────────────────────────────────────────────
# Caminhos
# ─────────────────────────────────────────────────────────────

def _get_profile():
    addon = xbmcaddon.Addon(ADDON_ID)
    profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    if not os.path.exists(profile):
        os.makedirs(profile)
    return profile


def pvr_m3u_path():
    return os.path.join(_get_profile(), 'pvr_live.m3u8')


def pvr_epg_path():
    return os.path.join(_get_profile(), 'pvr_epg.xml')


def pvr_favs_m3u_path():
    return os.path.join(_get_profile(), 'pvr_favorites.m3u8')


def pvr_favs_json_path():
    return os.path.join(_get_profile(), 'pvr_favorites.json')


# ─────────────────────────────────────────────────────────────
# Verificação de pvr.iptvsimple
# ─────────────────────────────────────────────────────────────

def is_pvr_installed():
    """Verifica se o pvr.iptvsimple está instalado."""
    try:
        resp = json.loads(xbmc.executeJSONRPC(json.dumps({
            'jsonrpc': '2.0', 'id': 1,
            'method': 'Addons.GetAddonDetails',
            'params': {'addonid': 'pvr.iptvsimple', 'properties': ['enabled', 'installed']}
        })))
        addon_info = resp.get('result', {}).get('addon', {})
        return addon_info.get('installed', False)
    except Exception:
        return False


def prompt_install_pvr():
    """Solicita instalação do pvr.iptvsimple."""
    if xbmcgui.Dialog().yesno(
        'PVR IPTV Simple Client',
        'O addon pvr.iptvsimple não está instalado.\n\nDeseja abrir a loja de addons para instalá-lo?'
    ):
        xbmc.executebuiltin('InstallAddon(pvr.iptvsimple)')


# ─────────────────────────────────────────────────────────────
# Bootstrap inicial do PVR
# ─────────────────────────────────────────────────────────────

def bootstrap_pvr():
    """
    Cria arquivos M3U e EPG stub iniciais e configura o pvr.iptvsimple
    para apontar para eles (instância 1 = todos os canais).
    """
    profile = _get_profile()
    m3u_path = pvr_m3u_path()
    epg_path = pvr_epg_path()

    # Cria stubs se não existirem
    if not os.path.exists(m3u_path):
        with open(m3u_path, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')
    if not os.path.exists(epg_path):
        with open(epg_path, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?><tv></tv>\n')

    # Configura o pvr.iptvsimple (instância 1) para usar nossos arquivos
    _configure_pvr_instance(m3u_path, epg_path, instance=1)
    _configure_pvr_osd()
    _install_pvr_keymap()
    _log('Bootstrap PVR concluído')


def _configure_pvr_instance(m3u_path, epg_path, instance=1, instance_name=''):
    """Configura uma instância do pvr.iptvsimple para usar os caminhos especificados."""
    try:
        pvr_profile = xbmcvfs.translatePath('special://profile/addon_data/pvr.iptvsimple')
        if not os.path.exists(pvr_profile):
            os.makedirs(pvr_profile)
        settings_path = os.path.join(pvr_profile, f'instance-settings-{instance}.xml')

        addon = xbmcaddon.Addon(ADDON_ID)
        use_addon_settings = addon.getSetting('pvr_addon_control') == 'true'

        if use_addon_settings:
            # Controla completamente as configurações do PVR
            root = ET.Element('settings', {'version': '2'})
            defs = [
                ('m3uPathType', '0'),
                ('m3uPath', m3u_path),
                ('m3uUrl', ''),
                ('epgPathType', '0'),
                ('epgPath', epg_path),
                ('epgUrl', ''),
                ('m3uRefreshMode', '1'),
                ('logoPathType', '0'),
                ('logoPath', ''),
                ('logoBaseUrl', ''),
            ]
            if instance_name:
                defs.insert(0, ('kodi_addon_instance_name', instance_name))
                defs.insert(1, ('kodi_addon_instance_enabled', 'true'))

            # Configurações de catchup
            catchup_enabled = addon.getSetting('pvr_catchup_enabled') == 'true'
            catchup_days = addon.getSetting('pvr_catchup_days') or '7'
            try:
                epg_hours = int(addon.getSetting('pvr_epg_refresh') or '12')
            except ValueError:
                epg_hours = 12
            defs.extend([
                ('catchupEnabled', 'true' if catchup_enabled else 'false'),
                ('catchupDays', catchup_days),
                ('catchupPlayEpgAsLive', 'false'),
                ('catchupOnlyOnFinishedProgrammes', 'false'),
                ('catchupWatchEpgBeginBufferMins', '5'),
                ('catchupWatchEpgEndBufferMins', '15'),
                ('epgRefreshInterval', str(epg_hours * 3600)),
            ])
            for key, val in defs:
                el = ET.SubElement(root, 'setting', {'id': key})
                el.text = val
            ET.ElementTree(root).write(settings_path, encoding='utf-8', xml_declaration=True)
        else:
            # Apenas atualiza os caminhos, preserva o restante
            updates = {'m3uPath': m3u_path, 'epgPath': epg_path}
            if os.path.exists(settings_path):
                tree = ET.parse(settings_path)
                root = tree.getroot()
                changed = False
                for key, val in updates.items():
                    el = root.find(f".//setting[@id='{key}']")
                    if el is not None:
                        if (el.text or '') != val:
                            el.text = val
                            changed = True
                    else:
                        new_el = ET.SubElement(root, 'setting', {'id': key})
                        new_el.text = val
                        changed = True
                if changed:
                    tree.write(settings_path, encoding='utf-8', xml_declaration=True)
            else:
                root = ET.Element('settings', {'version': '2'})
                base_defs = [
                    ('m3uPathType', '0'), ('m3uPath', m3u_path),
                    ('epgPathType', '0'), ('epgPath', epg_path),
                ]
                if instance_name:
                    base_defs.insert(0, ('kodi_addon_instance_name', instance_name))
                for key, val in base_defs:
                    el = ET.SubElement(root, 'setting', {'id': key})
                    el.text = val
                ET.ElementTree(root).write(settings_path, encoding='utf-8', xml_declaration=True)

        _log(f'Instância {instance} do PVR configurada: {settings_path}')
        return True
    except Exception as e:
        _log(f'Erro ao configurar instância {instance} do PVR: {e}')
        return False


def _configure_pvr_osd():
    """Configura o OSD do PVR do Kodi para navegação com setas."""
    addon = xbmcaddon.Addon(ADDON_ID)
    if addon.getSetting('pvr_osd_navigation') != 'true':
        return
    try:
        settings = {
            'pvrplayback.confirmchannelswitch': 'false',
            'pvrplayback.channelentrytimeout': '0',
        }
        for setting, value in settings.items():
            xbmc.executeJSONRPC(json.dumps({
                'jsonrpc': '2.0', 'method': 'Settings.SetSettingValue',
                'params': {'setting': setting, 'value': value}, 'id': 1
            }))
        _log('Configurações OSD do PVR aplicadas')
    except Exception as e:
        _log(f'Erro ao configurar OSD do PVR: {e}')


def _install_pvr_keymap():
    """Instala keymap para navegação PVR com setas esq/dir."""
    addon = xbmcaddon.Addon(ADDON_ID)
    if addon.getSetting('pvr_osd_navigation') != 'true':
        return
    try:
        keymaps_dir = xbmcvfs.translatePath('special://profile/keymaps/')
        keymap_path = os.path.join(keymaps_dir, 'xtream_universal_pvr.xml')
        if os.path.exists(keymap_path):
            return  # Já instalado
        if not os.path.exists(keymaps_dir):
            os.makedirs(keymaps_dir)
        keymap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<keymap>
  <FullscreenLiveTV>
    <keyboard>
      <left>ActivateWindow(PVROSDChannels)</left>
      <right>ActivateWindow(PVROSDGuide)</right>
    </keyboard>
  </FullscreenLiveTV>
  <FullscreenRadio>
    <keyboard>
      <left>ActivateWindow(PVROSDChannels)</left>
      <right>ActivateWindow(PVROSDGuide)</right>
    </keyboard>
  </FullscreenRadio>
</keymap>
'''
        with open(keymap_path, 'w', encoding='utf-8') as f:
            f.write(keymap_xml)
        _log('Keymap PVR instalado')
    except Exception as e:
        _log(f'Erro ao instalar keymap PVR: {e}')


# ─────────────────────────────────────────────────────────────
# Exportação M3U para PVR
# ─────────────────────────────────────────────────────────────

def _m3u_safe(val):
    """Sanitiza valor para uso em M3U."""
    if not val:
        return ''
    val = str(val).replace('"', '').replace('\n', ' ').replace('\r', ' ')
    allowed = set(" -_.():&/+'|`=?@#%")
    val = ''.join(
        c for c in val
        if unicodedata.category(c)[0] in 'LNZP' or c in allowed
    )
    return val.strip()


def build_m3u_content(channels):
    """Constrói conteúdo M3U a partir de lista de canais."""
    lines = ['#EXTM3U']
    reconnect_opts = 'reconnect=1&reconnect_streamed=1&reconnect_at_eof=1&reconnect_delay_max=5'

    for ch in channels:
        url = ch.get('url', '')
        if not url:
            continue
        name = _m3u_safe(ch.get('name', 'Unknown'))
        tvg_id = _m3u_safe(ch.get('tvg_id', '') or name)
        logo = _m3u_safe(ch.get('logo', '') or ch.get('stream_icon', ''))
        group = _m3u_safe(ch.get('group', 'Geral'))
        catchup = _m3u_safe(ch.get('catchup', ''))
        catchup_source = _m3u_safe(ch.get('catchup_source', ''))
        catchup_days = _m3u_safe(ch.get('catchup_days', ''))

        attrs = [f'tvg-id="{tvg_id}"', f'tvg-name="{name}"']
        if logo:
            attrs.append(f'tvg-logo="{logo}"')
        if group:
            attrs.append(f'group-title="{group}"')
        if catchup:
            attrs.append(f'catchup="{catchup}"')
            if catchup_source:
                attrs.append(f'catchup-source="{catchup_source}"')
            if catchup_days:
                attrs.append(f'catchup-days="{catchup_days}"')

        lines.append(f"#EXTINF:-1 {' '.join(attrs)},{name}")
        # Adiciona parâmetros de reconexão
        if '|' in url:
            url = url + '&' + reconnect_opts
        else:
            url = url + '|' + reconnect_opts
        lines.append(url)

    return '\n'.join(lines)


def export_pvr_m3u(channels):
    """
    Exporta a lista de canais para o arquivo M3U do PVR.
    channels: lista de dicts com name, url, tvg_id, logo, group, etc.
    """
    if not channels:
        _log('Nenhum canal para exportar')
        return False
    m3u_path = pvr_m3u_path()
    m3u_data = build_m3u_content(channels)
    try:
        with open(m3u_path, 'w', encoding='utf-8') as f:
            f.write(m3u_data)
        _log(f'M3U PVR exportado: {len(channels)} canais → {m3u_path}')
        return True
    except Exception as e:
        _log(f'Erro ao exportar M3U PVR: {e}')
        return False


# ─────────────────────────────────────────────────────────────
# Exportação EPG para PVR
# ─────────────────────────────────────────────────────────────

def export_pvr_epg_from_url(epg_url, username='', password=''):
    """
    Baixa e exporta o EPG XMLTV para o arquivo EPG do PVR.
    Suporta URL direta XMLTV ou auto-detecção via Xtream Codes.
    """
    import requests

    epg_path = pvr_epg_path()

    # Auto-detecção de URL EPG via Xtream Codes
    if not epg_url:
        _log('EPG: Nenhuma URL configurada')
        # Escreve stub vazio
        _write_epg_stub(epg_path)
        return False

    _log(f'EPG: Baixando de {epg_url.split("?")[0]}...')
    try:
        resp = requests.get(
            epg_url,
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=30,
            stream=True
        )
        resp.raise_for_status()

        chunks = []
        total = 0
        MAX_BYTES = 200 * 1024 * 1024  # 200 MB
        for chunk in resp.iter_content(chunk_size=65536):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                resp.close()
                _log('EPG: Arquivo muito grande, abortando download')
                _write_epg_stub(epg_path)
                return False
            chunks.append(chunk)
        resp.close()

        payload = b''.join(chunks)

        # Valida e escreve
        try:
            root = ET.fromstring(payload)
        except ET.ParseError as e:
            _log(f'EPG: XML inválido: {e}')
            _write_epg_stub(epg_path)
            return False

        # Exporta apenas uma janela razoável (1 dia atrás + 2 dias à frente)
        _export_epg_window(root, epg_path)
        _log(f'EPG exportado com sucesso para {epg_path}')
        return True

    except Exception as e:
        _log(f'EPG: Erro ao baixar: {e}')
        _write_epg_stub(epg_path)
        return False


def _export_epg_window(root, dest_path):
    """Exporta EPG filtrado para uma janela de tempo razoável."""
    try:
        now = time.time()
        start_cutoff = now - (1 * 86400)    # 1 dia atrás
        stop_cutoff = now + (3 * 86400)     # 3 dias à frente

        new_root = ET.Element('tv')
        exported_channels = set()

        for prog in root.findall('programme'):
            start_str = prog.get('start', '')
            stop_str = prog.get('stop', '')
            channel = prog.get('channel', '')

            start_ts = _parse_xmltv_time(start_str)
            stop_ts = _parse_xmltv_time(stop_str)

            if stop_ts < start_cutoff or start_ts > stop_cutoff:
                continue

            if channel not in exported_channels:
                # Adiciona elemento channel se ainda não foi adicionado
                for ch_el in root.findall('channel'):
                    if ch_el.get('id') == channel:
                        new_root.append(ch_el)
                        break
                else:
                    ch_el = ET.SubElement(new_root, 'channel', {'id': channel})
                    disp = ET.SubElement(ch_el, 'display-name')
                    disp.text = channel
                exported_channels.add(channel)

            new_root.append(prog)

        tmp_path = dest_path + '.tmp'
        ET.ElementTree(new_root).write(tmp_path, encoding='utf-8', xml_declaration=True)
        os.replace(tmp_path, dest_path)
        _log(f'EPG janela exportada: {len(exported_channels)} canais')
    except Exception as e:
        _log(f'Erro ao exportar janela EPG: {e}')
        _write_epg_stub(dest_path)


def _write_epg_stub(path):
    """Escreve EPG stub vazio."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?><tv></tv>')
    except Exception:
        pass


def _parse_xmltv_time(ts):
    """Converte timestamp XMLTV para Unix timestamp."""
    import calendar
    if not ts:
        return 0
    ts = ts.strip()
    offset_sec = 0
    if ' ' in ts:
        parts = ts.split(' ', 1)
        ts = parts[0]
        tz = parts[1].strip()
        if tz and (tz[0] == '+' or tz[0] == '-'):
            try:
                sign = 1 if tz[0] == '+' else -1
                tz = tz[1:]
                offset_sec = sign * (int(tz[:2]) * 3600 + int(tz[2:4]) * 60)
            except (ValueError, IndexError):
                offset_sec = 0
    try:
        t = time.strptime(ts, '%Y%m%d%H%M%S')
        return calendar.timegm(t) - offset_sec
    except ValueError:
        return 0


# ─────────────────────────────────────────────────────────────
# Sincronização PVR Principal
# ─────────────────────────────────────────────────────────────

def sync_pvr(channels, epg_url=''):
    """
    Sincronizacao completa do PVR:
    1. Exporta M3U
    2. Exporta EPG (se URL configurada)
    3. Configura pvr.iptvsimple (instancia 1)
    4. Solicita recarregamento suave via UpdateLocalAddons
    Retorna True se bem-sucedido.
    NOTA: Nao para/desabilita o PVR para evitar crash no Kodi.
    """
    _log('Iniciando sincronizacao PVR...')

    if not is_pvr_installed():
        _log('pvr.iptvsimple nao encontrado')
        prompt_install_pvr()
        return False

    # Exporta M3U
    _log(f'Exportando M3U: {len(channels)} canais')
    ok_m3u = export_pvr_m3u(channels)
    if not ok_m3u:
        _log('Falha ao exportar M3U')

    # Exporta EPG (apenas se URL configurada e arquivo antigo ou ausente)
    epg_path = pvr_epg_path()
    skip_epg = False
    if os.path.exists(epg_path):
        try:
            age_hours = (time.time() - os.path.getmtime(epg_path)) / 3600
            if age_hours < 4:
                with open(epg_path, 'r', encoding='utf-8') as f:
                    content = f.read(500)
                if '<programme' in content or '<channel' in content:
                    skip_epg = True
                    _log(f'EPG existente valido ({age_hours:.1f}h), pulando exportacao')
        except Exception:
            pass

    if not skip_epg and epg_url:
        _log('Exportando EPG...')
        export_pvr_epg_from_url(epg_url)
    elif not epg_url:
        _log('Sem URL de EPG, usando arquivo existente ou stub')
        if not os.path.exists(epg_path):
            _write_epg_stub(epg_path)

    # Configura pvr.iptvsimple (instancia 1 = todos os canais)
    _log('Configurando pvr.iptvsimple (instancia 1)...')
    ok_cfg = _configure_pvr_instance(pvr_m3u_path(), pvr_epg_path(), instance=1)

    # Sincroniza favoritos PVR (instancia 2) se habilitado
    addon = xbmcaddon.Addon(ADDON_ID)
    if addon.getSetting('pvr_favorites_enabled') == 'true':
        _log('Sincronizando Favoritos PVR (instancia 2)...')
        sync_pvr_favorites()

    # Recarrega addons locais de forma suave (nao fecha/reabre o PVR)
    try:
        xbmc.executebuiltin('UpdateLocalAddons')
        xbmc.sleep(500)
        _log('UpdateLocalAddons solicitado')
    except Exception as e:
        _log(f'Aviso ao recarregar addons: {e}')

    return ok_m3u and ok_cfg


def open_pvr_channels():
    """Abre a tela de canais do PVR do Kodi."""
    xbmc.executebuiltin('ActivateWindow(TVChannels)')


def open_pvr_guide():
    """Abre o guia EPG do PVR do Kodi."""
    xbmc.executebuiltin('ActivateWindow(TVGuide)')


# ─────────────────────────────────────────────────────────────
# Favoritos PVR (instância 2)
# ─────────────────────────────────────────────────────────────

def pvr_favs_load():
    """Carrega favoritos PVR do disco."""
    path = pvr_favs_json_path()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Migração: formato antigo era lista flat
        if isinstance(data, list):
            return {'Favoritos': data}
        return data
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def pvr_favs_save(groups):
    """Salva favoritos PVR no disco."""
    path = pvr_favs_json_path()
    tmp = path + '.tmp'
    try:
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(groups, f, ensure_ascii=False)
            try:
                f.flush()
                os.fsync(f.fileno())
            except OSError:
                pass
        os.replace(tmp, path)
    except Exception as e:
        _log(f'Erro ao salvar favoritos PVR: {e}')


def pvr_fav_add(channel, group='Favoritos'):
    """Adiciona canal aos favoritos PVR."""
    groups = pvr_favs_load()
    if group not in groups:
        groups[group] = []
    sid = str(channel.get('stream_id', '') or channel.get('id', ''))
    if not any(str(i.get('stream_id', '')) == sid for i in groups[group]):
        groups[group].append(channel)
        pvr_favs_save(groups)
        sync_pvr_favorites()
        return True
    return False


def pvr_fav_remove(stream_id, group='Favoritos'):
    """Remove canal dos favoritos PVR."""
    groups = pvr_favs_load()
    sid = str(stream_id)
    changed = False
    for g in groups:
        before = len(groups[g])
        groups[g] = [i for i in groups[g] if str(i.get('stream_id', '')) != sid]
        if len(groups[g]) != before:
            changed = True
    if changed:
        pvr_favs_save(groups)
        sync_pvr_favorites()
    return changed


def pvr_fav_is_fav(stream_id):
    """Verifica se canal está nos favoritos PVR."""
    groups = pvr_favs_load()
    sid = str(stream_id)
    for items in groups.values():
        if any(str(i.get('stream_id', '')) == sid for i in items):
            return True
    return False


def export_pvr_favs_m3u(base_url, username, password):
    """Exporta favoritos PVR como M3U para a instância 2 do pvr.iptvsimple."""
    groups = pvr_favs_load()
    lines = ['#EXTM3U']
    for gname, items in groups.items():
        for ch in items:
            name = ch.get('name', 'Unknown')
            icon = ch.get('stream_icon', '') or ch.get('icon', '')
            sid = str(ch.get('stream_id', ''))
            epg_id = ch.get('epg_channel_id') or sid
            if not (base_url and username and password and sid):
                continue
            url = f'{base_url.rstrip("/")}/live/{username}/{password}/{sid}.ts'
            lines.append(f'#EXTINF:-1 tvg-id="{epg_id}" tvg-logo="{icon}" group-title="★ Favoritos PVR - {gname}",{name}')
            lines.append(url)

    m3u_path = pvr_favs_m3u_path()
    try:
        with open(m3u_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        _log(f'M3U de Favoritos PVR exportado: {m3u_path}')
        return m3u_path
    except Exception as e:
        _log(f'Erro ao exportar M3U de Favoritos PVR: {e}')
        return None


def sync_pvr_favorites():
    """
    Sincroniza a instância 2 do pvr.iptvsimple com os favoritos PVR.
    """
    addon = xbmcaddon.Addon(ADDON_ID)
    if addon.getSetting('pvr_favorites_enabled') != 'true':
        # Remove instância se existir
        try:
            pvr_profile = xbmcvfs.translatePath('special://profile/addon_data/pvr.iptvsimple')
            settings_path = os.path.join(pvr_profile, 'instance-settings-2.xml')
            if os.path.exists(settings_path):
                os.remove(settings_path)
                _log('Instância 2 do PVR removida (favoritos desabilitados)')
        except Exception as e:
            _log(f'Erro ao remover instância 2: {e}')
        return

    base_url = addon.getSetting('base_url') or ''
    username = addon.getSetting('username') or ''
    password = addon.getSetting('password') or ''

    # Stub M3U se sem credenciais
    if not (base_url and username and password):
        m3u_path = pvr_favs_m3u_path()
        if not os.path.exists(m3u_path):
            with open(m3u_path, 'w', encoding='utf-8') as f:
                f.write('#EXTM3U\n')
    else:
        export_pvr_favs_m3u(base_url, username, password)

    # Configura instância 2
    _configure_pvr_instance(
        pvr_favs_m3u_path(),
        pvr_epg_path(),
        instance=2,
        instance_name='Xtream Universal - Favoritos PVR'
    )
    _log('Favoritos PVR sincronizados')


# ─────────────────────────────────────────────────────────────
# Addon Launcher (abrir outros addons pelo menu)
# ─────────────────────────────────────────────────────────────

def get_addon_groups(addon):
    """Retorna lista de grupos de addons configurados."""
    groups = []
    for i in range(1, 6):
        if addon.getSetting(f'ag_{i}_enabled') == 'true':
            name = addon.getSetting(f'ag_{i}_name') or f'Grupo {i}'
            addons_json = addon.getSetting(f'ag_{i}_addons') or '[]'
            try:
                addons_list = json.loads(addons_json)
            except Exception:
                addons_list = []
            groups.append({'num': i, 'name': name, 'addons': addons_list})
    return groups


def save_addon_group_addons(addon, group_num, addons_list):
    """Salva lista de addons de um grupo."""
    try:
        addon.setSetting(f'ag_{group_num}_addons', json.dumps(addons_list))
        return True
    except Exception as e:
        _log(f'Erro ao salvar grupo {group_num}: {e}')
        return False


def get_installed_video_addons():
    """Retorna lista de addons de vídeo instalados (exceto o próprio)."""
    try:
        resp = json.loads(xbmc.executeJSONRPC(json.dumps({
            'jsonrpc': '2.0', 'id': 1,
            'method': 'Addons.GetAddons',
            'params': {
                'type': 'xbmc.python.pluginsource',
                'enabled': True,
                'properties': ['name', 'thumbnail', 'description']
            }
        })))
        addons = resp.get('result', {}).get('addons', [])
        result = []
        for a in addons:
            aid = a.get('addonid', '')
            if aid == ADDON_ID or aid.startswith('script.') or aid.startswith('service.'):
                continue
            result.append({
                'id': aid,
                'name': a.get('name', aid),
                'icon': a.get('thumbnail', ''),
            })
        result.sort(key=lambda x: x['name'].lower())
        return result
    except Exception as e:
        _log(f'Erro ao listar addons: {e}')
        return []


def open_addon(addon_id):
    """Abre um addon pelo seu ID."""
    if not addon_id or not re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*$', str(addon_id)):
        _log(f'ID de addon inválido: {addon_id}')
        return
    xbmc.executebuiltin(f'Container.Update(plugin://{addon_id})')
