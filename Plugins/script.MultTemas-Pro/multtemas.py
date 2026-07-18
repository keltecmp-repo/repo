#!/usr/bin/python
# -*- coding: utf-8 -*-
# ============================================================
#  script.MultTemas-Pro  |  Team KelTecMP
#  Instalador + Ativador de Temas Unificado  v1.0.1
#  Combina script.Aeon-Mult.Temas + script.Start-Mult.Temas
# ============================================================

import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import os
import sys
import re
import math
import time
import datetime
import shutil
import zipfile
import pickle
import threading
import urllib.request
import urllib.error
import socket
import platform

# ─── Constantes ─────────────────────────────────────────────
_BASE_URL = 'https://raw.githubusercontent.com/keltecmp-repo/repo/refs/heads/master/SKIN-TOPICS-main'

# Mapa de skin_id -> (pasta no servidor, nome amigavel)
SKIN_MAP = {
    'skin.aeon.nox.silvo_mult': ('silvo',      'Aeon Nox Silvo'),
    'skin.aeon.nox.silvo': ('silvo',      'Aeon Nox Silvo'),
    'skin.confluence':     ('confluence',  'Confluence'),
}

SHOW_TEST_TOPICS = False
NETWORK_TIMEOUT  = 10


def get_skin_config():
    """
    Detecta a skin ativa e retorna (server_url, skin_name).
    Se a skin nao for suportada, retorna (None, skin_id).
    """
    skin_id = xbmc.getSkinDir()
    if skin_id in SKIN_MAP:
        folder, name = SKIN_MAP[skin_id]
        url = '%s/%s/topics_data.txt' % (_BASE_URL, folder)
        return url, name
    return None, skin_id


def contador(msg):
    if platform.system() == 'Linux':
        sistema_operacional = 'Android 9; Mobile; rv:68.0'
    elif platform.system() == 'Windows':
        sistema_operacional = 'Windows NT 6.1; WOW64; rv:54.0'
    elif platform.system() == 'IOS':
        sistema_operacional = 'iPhone; CPU iPhone OS 12_2 like Mac OS X'
    else:
        sistema_operacional = ''
    request_headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        '\x55\x73\x65\x72\x2d\x61\x67\x65\x6e\x74': sistema_operacional,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
        'Referer': "KelTec Media'Play (SCRIPT INSTALADOR AEON-NOX)1.1.0+Mult-Tema",
        'Connection': 'keep-alive'
    }
    try:
        request = urllib.request.Request('https://whos.amung.us/pingjs/?k=08rhq5clrm', headers=request_headers)
        response = urllib.request.urlopen(request).read()
    except Exception:
        pass
    tempo_delay = 0
    xbmc.sleep(tempo_delay * 0)

contador(True)
SHOW_TEST_TOPICS = False
NETWORK_TIMEOUT  = 10

# ─── Paths do Skin ───────────────────────────────────────────
_skin_id_   = xbmc.getSkinDir()
_skin_addon_ = xbmcaddon.Addon(id=_skin_id_)
_skin_root_  = _skin_addon_.getAddonInfo('path')

_skin_topics_dir_     = os.path.join(_skin_root_, 'skin_topics')
_modified_topics_dir_ = os.path.join(_skin_root_, 'skin_topics', 'modified_topics')
_original_topics_dir_ = os.path.join(_skin_root_, 'skin_topics', 'original_topics')
_pickle_file_         = os.path.join(_skin_root_, 'skin_topics', 'data_save')
_update_zip_          = os.path.join(_skin_root_, 'skin_topics', 'update.zip')


# ════════════════════════════════════════════════════════════
#  UTILITARIOS
# ════════════════════════════════════════════════════════════

def log(msg, level=xbmc.LOGINFO):
    xbmc.log('[MultTemas-Pro] ' + str(msg), level)

def reload_skin():
    xbmc.executebuiltin('ReloadSkin()')

def notify(title, msg, icon=xbmcgui.NOTIFICATION_INFO, ms=4000):
    xbmcgui.Dialog().notification(title, msg, icon, ms)

def convert_size(size):
    if size == 0:
        return '0 B'
    units = (' B', ' KB', ' MB', ' GB', ' TB')
    i = min(int(math.floor(math.log(max(size, 1), 1024))), len(units) - 1)
    return '%.2f%s' % (size / math.pow(1024, i), units[i])


# ════════════════════════════════════════════════════════════
#  REDE
# ════════════════════════════════════════════════════════════

def _make_request(url):
    ua_map = {
        'Linux':   'Android 9; Mobile; rv:68.0',
        'Windows': 'Windows NT 6.1; WOW64; rv:54.0',
        'Darwin':  'Macintosh; Intel Mac OS X 10_15_7',
    }
    ua = ua_map.get(platform.system(), 'Kodi/20 (compatible)')
    return urllib.request.Request(url, headers={
        'User-Agent':      ua,
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.5',
        'Accept':          'text/html,application/xhtml+xml,*/*;q=0.8',
        'Connection':      'keep-alive',
    })


def fetch_async(url, callback, timeout=NETWORK_TIMEOUT):
    """
    Busca URL em thread separada.
    Chama callback(texto) no sucesso ou callback(False) no erro.
    """
    def _run():
        try:
            resp = urllib.request.urlopen(_make_request(url), timeout=timeout)
            data = resp.read().decode('utf-8')
            resp.close()
            callback(data)
        except Exception as e:
            log('fetch_async error: ' + str(e), xbmc.LOGWARNING)
            callback(False)
    threading.Thread(target=_run, daemon=True).start()


def fetch_with_progress(url, label='Carregando...'):
    """
    Busca URL mostrando DialogProgress animado.
    Retorna o texto ou False.
    NUNCA bloqueia o Kodi — usa thread + polling.
    """
    dp = xbmcgui.DialogProgress()
    dp.create('MultTemas-Pro', label)
    dp.update(5)

    result = [None]
    done   = threading.Event()

    def on_done(data):
        result[0] = data
        done.set()

    fetch_async(url, on_done)

    pct      = 5
    deadline = time.time() + NETWORK_TIMEOUT + 3
    while not done.is_set():
        if dp.iscanceled() or time.time() > deadline:
            done.set()
            break
        xbmc.sleep(100)
        pct = min(pct + 2, 90)
        dp.update(pct)

    dp.update(100)
    dp.close()
    return result[0]


def download_file(url, dest_path):
    """Download de arquivo binario com barra de progresso. Retorna True/False."""
    dp = xbmcgui.DialogProgress()
    dp.create('MultTemas-Pro', 'Baixando tema...')
    dp.update(0)
    try:
        resp  = urllib.request.urlopen(_make_request(url), timeout=60)
        total = int(resp.info().get('Content-Length') or 0)
        done  = 0
        start = time.time()
        CHUNK = 1024 * 32

        with open(dest_path, 'wb') as fw:
            while True:
                chunk = resp.read(CHUNK)
                if not chunk:
                    break
                fw.write(chunk)
                done += len(chunk)

                if dp.iscanceled():
                    resp.close()
                    dp.close()
                    return False

                if total > 0:
                    pct   = int(min(done * 100 / total, 100))
                    speed = done / max(time.time() - start, 0.001)
                    rem   = (total - done) / max(speed, 1)
                    dp.update(pct,
                        'Baixado: %s de %s (%d%%)\nVelocidade: %s/s\nRestante: %s' % (
                            convert_size(done), convert_size(total), pct,
                            convert_size(speed),
                            str(datetime.timedelta(seconds=int(rem)))))
                else:
                    dp.update(50, 'Baixado: %s' % convert_size(done))

        dp.update(100)
        resp.close()
        dp.close()
        return True

    except Exception as e:
        dp.close()
        xbmcgui.Dialog().ok('ERRO DE DOWNLOAD', str(e))
        log('download_file: ' + str(e), xbmc.LOGERROR)
        return False


# ════════════════════════════════════════════════════════════
#  ZIP
# ════════════════════════════════════════════════════════════

def extract_zip(zip_path, dest_path):
    if not os.path.exists(zip_path):
        return False
    try:
        zf = zipfile.ZipFile(zip_path, 'r')
    except zipfile.BadZipFile as e:
        xbmcgui.Dialog().ok('ERRO NO ZIP', str(e))
        return False

    dp = xbmcgui.DialogProgress()
    dp.create('MultTemas-Pro', 'Extraindo arquivos...')
    dp.update(0)
    items = zf.infolist()
    total = float(len(items))
    count = 0
    try:
        for item in items:
            try:
                zf.extract(item, path=dest_path)
            except Exception:
                pass
            count += 1
            dp.update(int(count / total * 100))
            if dp.iscanceled():
                zf.close(); dp.close()
                return False
        zf.close(); dp.close()
        return True
    except Exception as e:
        zf.close(); dp.close()
        xbmcgui.Dialog().ok('ERRO NA EXTRACAO', str(e))
        return False


# ════════════════════════════════════════════════════════════
#  GERENCIAMENTO DE TOPICS
# ════════════════════════════════════════════════════════════

def save_pickle(path, value):
    with open(path, 'wb') as f:
        pickle.dump(value, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def list_local_topics():
    if not os.path.exists(_modified_topics_dir_):
        return []
    return sorted([
        d for d in os.listdir(_modified_topics_dir_)
        if os.path.isdir(os.path.join(_modified_topics_dir_, d))
    ])

def scan_topic_files(topic_root):
    dirs_arr, files_arr = [], []
    plen = len(topic_root) + 1
    for root, dirs, files in os.walk(topic_root, topdown=True, followlinks=True):
        for d in dirs:
            dirs_arr.append(os.path.join(root[plen:], d))
        for f in files:
            files_arr.append(os.path.join(root[plen:], f))
    return {'dirs': dirs_arr, 'files': files_arr}

def backup_original_files(dirs, files):
    for d in dirs:
        dst = os.path.join(_original_topics_dir_, d)
        if not os.path.exists(dst):
            os.makedirs(dst)
    for f in files:
        src = os.path.join(_skin_root_, f)
        dst = os.path.join(_original_topics_dir_, f)
        if os.path.exists(src) and not os.path.exists(dst):
            try: shutil.copy(src, dst)
            except Exception: pass

def restore_original_files(files):
    for f in files:
        src = os.path.join(_original_topics_dir_, f)
        dst = os.path.join(_skin_root_, f)
        if os.path.exists(dst):
            try: os.remove(dst)
            except Exception: pass
        if os.path.exists(src):
            try: shutil.copy(src, dst)
            except Exception: pass

def clear_backup():
    for root, dirs, files in os.walk(_original_topics_dir_, topdown=False):
        for f in files:
            try: os.unlink(os.path.join(root, f))
            except Exception: pass
        for d in dirs:
            try: os.rmdir(os.path.join(root, d))
            except Exception: pass

def apply_topic_files(files, topic_root):
    for f in files:
        src = os.path.join(topic_root, f)
        dst = os.path.join(_skin_root_, f)
        ddir = os.path.dirname(dst)
        if not os.path.exists(ddir):
            os.makedirs(ddir)
        if os.path.exists(dst):
            try: os.remove(dst)
            except Exception: pass
        if os.path.exists(src):
            try: shutil.copy(src, dst)
            except Exception: pass

def delete_path(path):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
    elif os.path.isfile(path):
        try: os.remove(path)
        except Exception: pass


# ════════════════════════════════════════════════════════════
#  ACAO: ATIVAR TEMA LOCAL
# ════════════════════════════════════════════════════════════

def action_activate_local_topic(auto_select=None):
    """
    Mostra temas locais e permite ativar ou resetar.
    Se auto_select (nome do tema) for informado, pula o dialog
    e aplica diretamente — usado apos download automatico.
    """
    topics = list_local_topics()

    if not topics:
        resp = xbmcgui.Dialog().yesno(
            'MultTemas-Pro',
            'Nenhum tema instalado.\nDeseja baixar novos temas do servidor?')
        if resp:
            action_download_topic()
        return

    # Aplicacao automatica apos download
    if auto_select and auto_select in topics:
        _apply_topic(auto_select, topics)
        return

    reset_label = '[COLOR red][ RESTAURAR TEMA ORIGINAL ][/COLOR]'
    listitems   = []

    for idx, item in enumerate([reset_label] + topics):
        li = xbmcgui.ListItem(label=item, path=item)
        if idx == 0:
            img = os.path.join(_skin_topics_dir_, 'reset.png')
            if os.path.exists(img):
                li.setArt({'thumb': img})
        else:
            base = os.path.join(_modified_topics_dir_, item)
            for ext in ('info.jpg', 'info.png'):
                img = os.path.join(base, ext)
                if os.path.exists(img):
                    li.setArt({'thumb': img})
                    break
        listitems.append(li)

    choice = xbmcgui.Dialog().select(
        '[COLOR blue]SKIN TOPICS LOADER[/COLOR]',
        listitems, useDetails=True)

    if choice < 0:
        return

    if choice == 0:
        if os.path.exists(_pickle_file_):
            saved = load_pickle(_pickle_file_)
            restore_original_files(saved)
            clear_backup()
            delete_path(_pickle_file_)
            reload_skin()
        else:
            notify('MultTemas-Pro', 'Nenhum backup encontrado.')
        return

    _apply_topic(topics[choice - 1], topics)


def _apply_topic(topic_name, topics=None):
    """Aplica um tema pelo nome."""
    if topics is None:
        topics = list_local_topics()
    topic_path = os.path.join(_modified_topics_dir_, topic_name)
    data = scan_topic_files(topic_path)

    backup_original_files(data['dirs'], data['files'])

    if os.path.exists(_pickle_file_):
        prev = load_pickle(_pickle_file_)
        restore_original_files(prev)

    save_pickle(_pickle_file_, data['files'])
    apply_topic_files(data['files'], topic_path)
    reload_skin()


# ════════════════════════════════════════════════════════════
#  ACAO: BAIXAR NOVO TEMA
#  - Abre a lista INSTANTANEAMENTE (sem xbmcvfs.exists por tema)
#  - Apos download/extracao, abre popup para ativar o tema
# ════════════════════════════════════════════════════════════

def parse_server_data(raw):
    raw = raw.replace("'", '"').strip()
    names, urls = [], []
    for name, url in re.compile(r'name="(.*?)".*?url="(.*?)"', re.DOTALL).findall(raw):
        if name and url:
            if not name.startswith('*') or SHOW_TEST_TOPICS:
                names.append(name)
                urls.append(url)
    return names, urls


def action_download_topic():
    # 0. Verifica se a skin ativa e suportada
    server_url, skin_name = get_skin_config()
    if not server_url:
        xbmcgui.Dialog().ok(
            'MultTemas-Pro',
            'Skin nao suportada: [COLOR yellow]%s[/COLOR]\n\n'
            'Skins suportadas:\n- Aeon Nox Silvo\n- Confluence' % skin_name)
        return

    # 1. Busca indice de temas com progresso animado (nao bloqueia)
    raw = fetch_with_progress(
        server_url,
        'Carregando temas para %s...' % skin_name)

    if not raw:
        xbmcgui.Dialog().ok(
            'ERRO DE CONEXAO',
            'Nao foi possivel carregar a lista de temas.\n'
            'Verifique sua conexao com a internet.')
        return

    names, urls = parse_server_data(raw)
    if not names:
        xbmcgui.Dialog().ok('MultTemas-Pro', 'Nenhum tema disponivel no servidor.')
        return

    # 2. Monta lista SEM fazer requests HTTP por tema
    #    (thumbnails locais apenas — sem xbmcvfs.exists para URLs remotas)
    listitems = []
    for name, url in zip(names, urls):
        li = xbmcgui.ListItem(label=name, path=url)
        # Tenta thumbnail local se ja existir do download anterior
        base_local = os.path.join(_modified_topics_dir_, name)
        for ext in ('info.jpg', 'info.png'):
            img = os.path.join(base_local, ext)
            if os.path.exists(img):
                li.setArt({'thumb': img})
                break
        listitems.append(li)

    # 3. Abre dialog de selecao — instantaneo
    choice = xbmcgui.Dialog().select(
        '[COLOR blue]SKIN TOPICS DOWNLOADER - %s[/COLOR]' % skin_name,
        listitems, useDetails=True)

    if choice < 0:
        return

    selected_url  = urls[choice]
    selected_name = names[choice]

    # 4. Download
    if not download_file(selected_url, _update_zip_):
        return

    xbmc.sleep(100)

    if not os.path.exists(_update_zip_):
        xbmcgui.Dialog().ok('MultTemas-Pro', 'Arquivo ZIP nao encontrado apos download.')
        return

    # 5. Extracao
    delete_path(_modified_topics_dir_)
    xbmc.sleep(50)

    ok = extract_zip(_update_zip_, _skin_topics_dir_)
    delete_path(_update_zip_)

    if not ok:
        return

    # 6. Popup automatico para ativar o tema recem baixado
    topics_now = list_local_topics()

    # Descobre qual tema foi baixado (primeiro da lista ou pelo nome)
    best_match = None
    for t in topics_now:
        if selected_name.lower() in t.lower() or t.lower() in selected_name.lower():
            best_match = t
            break
    if not best_match and topics_now:
        best_match = topics_now[0]

    confirm = xbmcgui.Dialog().yesno(
        'MultTemas-Pro',
        'Download concluido!\n\nDeseja ativar o tema agora?',
        yeslabel='Ativar Agora',
        nolabel='Depois')

    if confirm:
        if best_match:
            _apply_topic(best_match, topics_now)
        else:
            action_activate_local_topic()
    else:
        notify('MultTemas-Pro', 'Tema baixado. Use "Ativar Tema Local" para aplicar.', ms=5000)


# ════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ════════════════════════════════════════════════════════════

def main_menu():
    _, skin_name = get_skin_config()
    skin_label   = skin_name if skin_name else xbmc.getSkinDir()

    options = [
        ('[COLOR lime]Ativar Tema Local[/COLOR]',
         'Escolha e aplique um tema ja instalado'),
        ('[COLOR dodgerblue]Baixar Novo Tema[/COLOR]',
         'Conecta ao servidor e baixa novos temas para %s' % skin_label),
        ('[COLOR red]Restaurar Tema Original[/COLOR]',
         'Remove o tema ativo e volta ao skin padrao'),
    ]

    listitems = []
    for label, desc in options:
        li = xbmcgui.ListItem(label=label)
        li.setLabel2(desc)
        listitems.append(li)

    choice = xbmcgui.Dialog().select(
        'MultTemas-Pro  |  %s' % skin_label,
        listitems, useDetails=True)

    if choice == 0:
        action_activate_local_topic()
    elif choice == 1:
        action_download_topic()
    elif choice == 2:
        if os.path.exists(_pickle_file_):
            if xbmcgui.Dialog().yesno(
                    'MultTemas-Pro',
                    'Restaurar o tema original?\nO tema atual sera desativado.'):
                saved = load_pickle(_pickle_file_)
                restore_original_files(saved)
                clear_backup()
                delete_path(_pickle_file_)
                reload_skin()
        else:
            notify('MultTemas-Pro', 'Nenhum tema ativo para restaurar.')


# ════════════════════════════════════════════════════════════
#  ENTRADA
# ════════════════════════════════════════════════════════════

if __name__ == '__main__':
    for d in (_skin_topics_dir_, _modified_topics_dir_, _original_topics_dir_):
        if not os.path.exists(d):
            try: os.makedirs(d)
            except Exception: pass

    main_menu()
