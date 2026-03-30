# -*- coding: utf-8 -*-

import xbmc
import xbmcgui

import time
from datetime import datetime
from datetime import timedelta

import os
import sys

try:  # Python 3
    from urllib.parse import quote_plus
except ImportError:  # Python 2
    from urllib import quote_plus

from resources.libs.common.config import CONFIG
from resources.libs import clear
from resources.libs import check
from resources.libs import db
from resources.libs.gui import window
from resources.libs.common import logging
from resources.libs.common import tools
from resources.libs import skin
from resources.libs import update


def auto_install_repo():
    if not os.path.exists(os.path.join(CONFIG.ADDONS, CONFIG.REPOID)):
        response = tools.open_url(CONFIG.REPOADDONXML)

        if response:
            from xml.etree import ElementTree
            
            root = ElementTree.fromstring(response.text)
            repoaddon = root.findall('addon')
            repoversion = [tag.get('version') for tag in repoaddon if tag.get('id') == CONFIG.REPOID]
            
            if repoversion:
                installzip = '{0}-{1}.zip'.format(CONFIG.REPOID, repoversion[0])
                url = CONFIG.REPOZIPURL + installzip
                repo_response = tools.open_url(url, check=True)

                if repo_response:
                    progress_dialog = xbmcgui.DialogProgress()
                    
                    progress_dialog.create(CONFIG.ADDONTITLE, 'Baixando Repo ...' + '\n' + 'Please Wait')
                    tools.ensure_folders(CONFIG.PACKAGES)
                    lib = os.path.join(CONFIG.PACKAGES, installzip)

                    # Remove the old zip if there is one
                    tools.remove_file(lib)

                    from resources.libs.downloader import Downloader
                    from resources.libs import extract
                    Downloader().download(url, lib)
                    extract.all(lib, CONFIG.ADDONS)

                    try:
                        repoxml = os.path.join(CONFIG.ADDONS, CONFIG.REPOID, 'addon.xml')
                        root = ElementTree.parse(repoxml).getroot()
                        reponame = root.get('name')
                        
                        logging.log_notify("{1}".format(CONFIG.COLOR1, reponame),
                                           "[COLOR {0}]Add-on atualizado[/COLOR]".format(CONFIG.COLOR2),
                                           icon=os.path.join(CONFIG.ADDONS, CONFIG.REPOID, 'icon.png'))
                                           
                    except Exception as e:
                        logging.log(str(e), level=xbmc.LOGERROR)

                    # Add wizard to add-on database
                    db.addon_database(CONFIG.REPOID, 1)

                    progress_dialog.close()
                    xbmc.sleep(500)

                    logging.log("[Repo de instalação automática] Instalado com sucesso", level=xbmc.LOGINFO)
                else:
                    logging.log_notify("[COLOR {0}]Erro de instalação do Repo[/COLOR]".format(CONFIG.COLOR1),
                                       "[COLOR {0}]URL inválido para zip![/COLOR]".format(CONFIG.COLOR2))
                    logging.log("[Repo de instalação automática] Não foi possível criar um URL funcional para o repositório. {0}".format(
                        url), level=xbmc.LOGERROR)
            else:
                logging.log("URL inválido para repositório zip", level=xbmc.LOGERROR)
        else:
            logging.log_notify("[COLOR {0}] Erro de instalação do repositório [/ COLOR]".format(CONFIG.COLOR1),
                               "[COLOR {0}] Arquivo addon.xml inválido![/COLOR]".format(CONFIG.COLOR2))
            logging.log("[Repo de instalação automática] Não é possível ler o arquivo addon.xml.", level=xbmc.LOGERROR)
    elif not CONFIG.AUTOINSTALL == 'Yes':
        logging.log("[Repo de instalação automática] Não ativado", level=xbmc.LOGINFO)
    elif os.path.exists(os.path.join(CONFIG.ADDONS, CONFIG.REPOID)):
        logging.log("[Repositório de instalação automática] Repositório já instalado")


def show_notification():
    note_id, msg = window.split_notify(CONFIG.NOTIFICATION)
    
    if note_id:
        if note_id == CONFIG.NOTEID:
            if CONFIG.NOTEDISMISS == 'false':
                window.show_notification(msg)
            else:
                logging.log('[Notificações] Sem novas notificações.', level=xbmc.LOGINFO)
        elif note_id > CONFIG.NOTEID:
            logging.log('[Notificações] Mostrando notificação {0}'
                        .format(note_id))
            CONFIG.set_setting('noteid', note_id)
            CONFIG.set_setting('notedismiss', 'false')
            window.show_notification(msg)
    else:
        logging.log('[Notificações] Arquivo de notificações em {0} não formatado corretamente.'
                    .format(CONFIG.NOTIFICATION),
                    level=xbmc.LOGINFO)


def installed_build_check():
    dialog = xbmcgui.Dialog()

    if not CONFIG.EXTRACT == '100' and CONFIG.EXTERROR > 0:
        logging.log("[Verificação de versão instalada] A versão foi extraída em {0} / 100 com [ERRORS: {1}]".format(CONFIG.EXTRACT,
                                                                                                    CONFIG.EXTERROR),
                    level=xbmc.LOGINFO)
        yes = dialog.yesno(CONFIG.ADDONTITLE,
                           '[COLOR {0}]{2}[/COLOR] [COLOR {1}]não foi instalado corretamente![/COLOR]'.format(CONFIG.COLOR1,
                                                                                                   CONFIG.COLOR2,
                                                                                                   CONFIG.BUILDNAME)
                           +'\n'+('Instalado: [COLOR {0}]{1}[/COLOR] / '
                            'Error Count: [COLOR {2}]{3}[/COLOR]').format(CONFIG.COLOR1, CONFIG.EXTRACT, CONFIG.COLOR1,
                                                                          CONFIG.EXTERROR)
                           +'\n'+'Você gostaria de tentar de novo?[/COLOR]', nolabel='[B]Não, obrigado![/B]',
                           yeslabel='[B]Retry Install[/B]')
        CONFIG.clear_setting('build')
        if yes:
            xbmc.executebuiltin("PlayMedia(plugin://{0}/?mode=install&name={1}&url=fresh)".format(CONFIG.ADDON_ID,
                                                                                                  quote_plus(CONFIG.BUILDNAME)))
            logging.log("[Verificação de versão instalada] Nova instalação reativada", level=xbmc.LOGINFO)
        else:
            logging.log("[Verificação de versão instalada] Reinstalar ignorado")
    elif CONFIG.SKIN in ['skin.confluence', 'skin.estuary', 'skin.estouchy']:
        logging.log("[Verificação da versão instalada] Skin incorreto: {0}".format(CONFIG.SKIN), level=xbmc.LOGINFO)
        defaults = CONFIG.get_setting('defaultskin')
        if not defaults == '':
            if os.path.exists(os.path.join(CONFIG.ADDONS, defaults)):
                if skin.skin_to_default(defaults):
                    skin.look_and_feel_data('restore')
        if not CONFIG.SKIN == defaults and not CONFIG.BUILDNAME == "":
            gui_xml = check.check_build(CONFIG.BUILDNAME, 'gui')

            response = tools.open_url(gui_xml, check=True)
            if not response:
                logging.log("[Verificação de instalação da versão] Guifix foi definido como http: //", level=xbmc.LOGINFO)
                dialog.ok(CONFIG.ADDONTITLE,
                          "[COLOR {0}]Parece que as configurações de skin não foram aplicadas à construção.".format(CONFIG.COLOR2)
                          +'\n'+"Infelizmente, nenhuma correção de GUI foi anexada ao buildSadly, nenhuma correção de GUI foi anexada à compilação"
                          +'\n'+"Você precisará reinstalar a compilação e certificar-se de fazer um fechamento forçado[/COLOR]")
            else:
                yes = dialog.yesno(CONFIG.ADDONTITLE,
                                       '{0} não foi instalado corretamente!'.format(CONFIG.BUILDNAME)
                                       +'\n'+'Parece que as configurações de skin não foram aplicadas à construção.'
                                       +'\n'+'Você gostaria de aplicar o GuiFix?',
                                       nolabel='[B]Não, Cancelar[/B]', yeslabel='[B]Aplicar correção[/B]')
                if yes:
                    xbmc.executebuiltin("PlayMedia(plugin://{0}/?mode=install&name={1}&url=gui)".format(CONFIG.ADDON_ID,
                                                                                                        quote_plus(CONFIG.BUILDNAME)))
                    logging.log("[Build instalado,Check] Guifix tentando instalar")
                else:
                    logging.log('[Build instalado,Check] URL do Guifix funcionando, mas cancelado: {0}'.format(gui_xml),
                                level=xbmc.LOGINFO)
    else:
        logging.log('[Build instalado,Check] A instalação parece ter sido concluída corretamente', level=xbmc.LOGINFO)
        
    if CONFIG.get_setting('installed') == 'true':
        if CONFIG.get_setting('keeptrakt') == 'true':
            from resources.libs import traktit
            logging.log('[Build instalado,Check] Restaurando Dados Trakt', level=xbmc.LOGINFO)
            traktit.trakt_it('restore', 'all')
        if CONFIG.get_setting('keepdebrid') == 'true':
            from resources.libs import debridit
            logging.log('[Build instalado,Check] Restaurando Dados Real Desbridados', level=xbmc.LOGINFO)
            debridit.debrid_it('restore', 'all')
        if CONFIG.get_setting('keeplogin') == 'true':
            from resources.libs import loginit
            logging.log('[Build instalado,Check] Restaurando dados de login', level=xbmc.LOGINFO)
            loginit.login_it('restore', 'all')

        CONFIG.clear_setting('install')


def build_update_check():
    response = tools.open_url(CONFIG.BUILDFILE, check=True)

    if not response:
        logging.log("[Build Check] Não é um URL válido para o arquivo de compilação: {0}".format(CONFIG.BUILDFILE), level=xbmc.LOGINFO)
    elif not CONFIG.BUILDNAME == '':
        if CONFIG.SKIN in ['skin.confluence', 'skin.estuary', 'skin.estouchy'] and not CONFIG.DEFAULTIGNORE == 'true':
            check.check_skin()

        logging.log("[Build Check] Compilação instalada: verificando atualizações", level=xbmc.LOGINFO)
        check.check_build_update()

    CONFIG.set_setting('nextbuildcheck', tools.get_date(days=CONFIG.UPDATECHECK, formatted=True))


def save_trakt():
    current_time = time.mktime(time.strptime(tools.get_date(formatted=True), "%Y-%m-%d %H:%M:%S"))
    next_save = time.mktime(time.strptime(CONFIG.get_setting('traktnextsave'), "%Y-%m-%d %H:%M:%S"))
    
    if next_save <= current_time:
        from resources.libs import traktit
        logging.log("[Trakt Data] Salvando todos os dados", level=xbmc.LOGINFO)
        traktit.auto_update('all')
        CONFIG.set_setting('traktnextsave', tools.get_date(days=3, formatted=True))
    else:
        logging.log("[Trakt Data]O próximo salvamento automático não ocorrerá até: {0} / Hoje é: {1}".format(CONFIG.get_setting('traktnextsave'),
                                                                                          tools.get_date(formatted=True)),
                    level=xbmc.LOGINFO)


def save_debrid():
    current_time = time.mktime(time.strptime(tools.get_date(formatted=True), "%Y-%m-%d %H:%M:%S"))
    next_save = time.mktime(time.strptime(CONFIG.get_setting('debridnextsave'), "%Y-%m-%d %H:%M:%S"))
    
    if next_save <= current_time:
        from resources.libs import debridit
        logging.log("[Debrid Data] Saving all Data", level=xbmc.LOGINFO)
        debridit.auto_update('all')
        CONFIG.set_setting('debridnextsave', tools.get_date(days=3, formatted=True))
    else:
        logging.log("[Debrid Data] O próximo salvamento automático não ocorrerá até: {0} / Hoje é: {1}".format(CONFIG.get_setting('debridnextsave'),
                                                                                           tools.get_date(formatted=True)),
                    level=xbmc.LOGINFO)


def save_login():
    current_time = time.mktime(time.strptime(tools.get_date(formatted=True), "%Y-%m-%d %H:%M:%S"))
    next_save = time.mktime(time.strptime(CONFIG.get_setting('loginnextsave'), "%Y-%m-%d %H:%M:%S"))
    
    if next_save <= current_time:
        from resources.libs import loginit
        logging.log("[Login Info] Saving all Data", level=xbmc.LOGINFO)
        loginit.auto_update('all')
        CONFIG.set_setting('loginnextsave', tools.get_date(days=3, formatted=True))
    else:
        logging.log("[Informações de login] O próximo salvamento automático não ocorrerá até: {0} / Hoje é: {1}".format(CONFIG.get_setting('loginnextsave'),
                                                                                          tools.get_date(formatted=True)),
                    level=xbmc.LOGINFO)


def auto_clean():
    service = False
    days = [tools.get_date(formatted=True), tools.get_date(days=1, formatted=True), tools.get_date(days=3, formatted=True), tools.get_date(days=7, formatted=True),
            tools.get_date(days=30, formatted=True)]

    freq = int(CONFIG.AUTOFREQ)
    next_cleanup = time.mktime(time.strptime(CONFIG.NEXTCLEANDATE, "%Y-%m-%d %H:%M:%S"))

    if next_cleanup <= tools.get_date() or freq == 0:
        service = True
        next_run = days[freq]
        CONFIG.set_setting('nextautocleanup', next_run)
    else:
        logging.log("[Limpeza Automática] Próxima Limpeza {0}".format(CONFIG.NEXTCLEANDATE),
                    level=xbmc.LOGINFO)
    if service:
        if CONFIG.AUTOCACHE == 'true':
            logging.log('[Limpeza Automática] Cache: Ligado', level=xbmc.LOGINFO)
            clear.clear_cache(True)
        else:
            logging.log('[Limpeza Automática] Cache: Desligado', level=xbmc.LOGINFO)
        if CONFIG.AUTOTHUMBS == 'true':
            logging.log('[Limpeza Automática] Antigo Thumbs: On', level=xbmc.LOGINFO)
            clear.old_thumbs()
        else:
            logging.log('[Limpeza Automática] Antigo Thumbs: Off', level=xbmc.LOGINFO)
        if CONFIG.AUTOPACKAGES == 'true':
            logging.log('[Limpeza Automática] Packages: On', level=xbmc.LOGINFO)
            clear.clear_packages_startup()
        else:
            logging.log('[Limpeza Automática] Packages: Off', level=xbmc.LOGINFO)


def stop_if_duplicate():
    NOW = time.time()
    temp = CONFIG.get_setting('time_started')
    
    if temp:
        if temp > NOW - (60 * 2):
            logging.log('Killing Script de inicialização')
            sys.exit()
            
    logging.log("{0}".format(NOW))
    CONFIG.set_setting('time_started', NOW)
    xbmc.sleep(1000)
    
    if not CONFIG.get_setting('time_started') == NOW:
        logging.log('Killing Script de inicialização')
        sys.exit()
    else:
        logging.log('Continuando Script de inicialização')


def check_for_video():
    while xbmc.Player().isPlayingVideo():
        xbmc.sleep(1000)


# Don't run the script while video is playing :)
check_for_video()
# Ensure that any needed folders are created
tools.ensure_folders()
# Stop this script if it's been run more than once
# if CONFIG.KODIV < 18:
    # stop_if_duplicate()
# Ensure that the wizard's name matches its folder
check.check_paths()


# FIRST RUN SETTINGS
if CONFIG.get_setting('first_install') == 'true':
    logging.log("[Primeira execução] Mostrando configurações de salvamento de dados", level=xbmc.LOGINFO)
    window.show_save_data_settings()
else:
    logging.log("[Primeira execução] Ignorando configurações de salvamento de dados", level=xbmc.LOGINFO)

# BUILD INSTALL PROMPT
if tools.open_url(CONFIG.BUILDFILE, check=True) and CONFIG.get_setting('installed') == 'false':
    logging.log("[Verificação de compilação atual] Compilação não instalada", level=xbmc.LOGINFO)
    window.show_build_prompt()
else:
    logging.log("[Verificação da versão atual] Versão instalada: {0}".format(CONFIG.BUILDNAME), level=xbmc.LOGINFO)
    
# BUILD UPDATE CHECK
buildcheck = CONFIG.get_setting('nextbuildcheck')
if CONFIG.get_setting('buildname'):
    current_time = time.time()
    epoch_check = time.mktime(time.strptime(buildcheck, "%Y-%m-%d %H:%M:%S"))
    
    if current_time >= epoch_check:
        logging.log("[Verificação de atualização de Build] Iniciada", level=xbmc.LOGINFO)
        build_update_check()
else:
    logging.log("[Verificar atualização da Build ] Próxima verificação: {0}".format(buildcheck), level=xbmc.LOGINFO)

# AUTO INSTALL REPO
if CONFIG.AUTOINSTALL == 'Yes':
    logging.log("[Repo de instalação automática] Iniciado", level=xbmc.LOGINFO)
    auto_install_repo()
else:
    logging.log("[Repo de instalação automática] Não ativado", level=xbmc.LOGINFO)

# REINSTALL ELIGIBLE BINARIES
binarytxt = os.path.join(CONFIG.USERDATA, 'build_binaries.txt')
if os.path.exists(binarytxt):
    logging.log("[Detecção binária] Reinstalando Add-ons binários qualificados", level=xbmc.LOGINFO)
    from resources.libs import restore
    restore.restore('binaries')
else:
    logging.log("[Detecção binária] Add-ons binários qualificados para reinstalar", level=xbmc.LOGINFO)
    
# AUTO UPDATE WIZARD
if CONFIG.AUTOUPDATE == 'Yes':
    logging.log("[Assistente de atualização automática] iniciado", level=xbmc.LOGINFO)
    update.wizard_update()
else:
    logging.log("[Assistente de atualização automática] Não habilitado", level=xbmc.LOGINFO)

# SHOW NOTIFICATIONS
if CONFIG.ENABLE_NOTIFICATION == 'Yes':
    show_notification()
else:
    logging.log('[Notifications] Não habilitado', level=xbmc.LOGINFO)

# INSTALLED BUILD CHECK
if CONFIG.get_setting('installed') == 'true':
    logging.log("[Build instalado,Check] Iniciado", level=xbmc.LOGINFO)
    installed_build_check()
else:
    logging.log("[Build instalado,Check] Não habilitado", level=xbmc.LOGINFO)

# SAVE TRAKT
if CONFIG.get_setting('keeptrakt') == 'true':
    logging.log("[Trakt Data] Iniciado", level=xbmc.LOGINFO)
    save_trakt()
else:
    logging.log("[Trakt Data] Não habilitado", level=xbmc.LOGINFO)

# SAVE DEBRID
if CONFIG.get_setting('keepdebrid') == 'true':
    logging.log("[Debrid Data] Iniciado", level=xbmc.LOGINFO)
    save_debrid()
else:
    logging.log("[Debrid Data] Não habilitado", level=xbmc.LOGINFO)

# SAVE LOGIN
if CONFIG.get_setting('keeplogin') == 'true':
    logging.log("[Login Info] Iniciado", level=xbmc.LOGINFO)
    save_login()
else:
    logging.log("[Login Info] Não habilitado", level=xbmc.LOGINFO)

# AUTO CLEAN
if CONFIG.get_setting('autoclean') == 'true':
    logging.log("[Limpeza Automática] Iniciado", level=xbmc.LOGINFO)
    auto_clean()
else:
    logging.log('[Limpeza Automática] Não habilitado', level=xbmc.LOGINFO)