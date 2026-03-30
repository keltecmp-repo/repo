################################################################################

#      Copyright (C) 2019 drinfernoo                                           #

#                                                                              #

#  This Program is free software; you can redistribute it and/or modify        #

#  it under the terms of the GNU General Public License as published by        #

#  the Free Software Foundation; either version 2, or (at your option)         #

#  any later version.                                                          #

#                                                                              #

#  This Program is distributed in the hope that it will be useful,             #

#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #

#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #

#  GNU General Public License for more details.                                #

#                                                                              #

#  You should have received a copy of the GNU General Public License           #

#  along with XBMC; see the file COPYING.  If not, write to                    #

#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #

#  http://www.gnu.org/copyleft/gpl.html                                        #

################################################################################

# -*- coding: utf-8 -*-



import xbmc



import os



from resources.libs.common import directory

from resources.libs.common import logging

from resources.libs.common import tools

from resources.libs.common.config import CONFIG





class MaintenanceMenu:



    def get_listing(self):

        directory.add_dir('[B]Ferramentas de limpeza[/B]', {'mode': 'maint', 'name': 'clean'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_dir('[B]Ferramentas Complementares[/B]', {'mode': 'maint', 'name': 'addon'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_dir('[B]Ferramentas de registro[/B]', {'mode': 'maint', 'name': 'logging'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_dir('[B]Manutenção diversa[/B]', {'mode': 'maint', 'name': 'misc'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_dir('[B]Restauração de backup[/B]', {'mode': 'maint', 'name': 'backup'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_dir('[B]Ajustes / correções do sistema[/B]', {'mode': 'maint', 'name': 'tweaks'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)



    def clean_menu(self):

        from resources.libs import clear

        from resources.libs.common import tools



        on = '[B][COLOR springgreen]Ligado[/COLOR][/B]'

        off = '[B][COLOR red]Desligado[/COLOR][/B]'



        autoclean = 'true' if CONFIG.AUTOCLEANUP == 'true' else 'false'

        cache = 'true' if CONFIG.AUTOCACHE == 'true' else 'false'

        packages = 'true' if CONFIG.AUTOPACKAGES == 'true' else 'false'

        thumbs = 'true' if CONFIG.AUTOTHUMBS == 'true' else 'false'

        includevid = 'true' if CONFIG.INCLUDEVIDEO == 'true' else 'false'

        includeall = 'true' if CONFIG.INCLUDEALL == 'true' else 'false'



        sizepack = tools.get_size(CONFIG.PACKAGES)

        sizethumb = tools.get_size(CONFIG.THUMBNAILS)

        archive = tools.get_size(CONFIG.ARCHIVE_CACHE)

        sizecache = (clear.get_cache_size()) - archive

        totalsize = sizepack + sizethumb + sizecache



        directory.add_file(

            'Limpeza Total: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(totalsize)), {'mode': 'fullclean'},

            icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Limpar cache: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizecache)),

                           {'mode': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        if xbmc.getCondVisibility('System.HasAddon(script.module.urlresolver)') or xbmc.getCondVisibility(

                'System.HasAddon(script.module.resolveurl)'):

            directory.add_file('Limpar caches de funções de resolução', {'mode': 'clearfunctioncache'}, icon=CONFIG.ICONMAINT,

                               themeit=CONFIG.THEME3)

        directory.add_file('Pacotes claros: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizepack)),

                           {'mode': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file(

            'Limpar miniaturas: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizethumb)),

            {'mode': 'clearthumb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        if os.path.exists(CONFIG.ARCHIVE_CACHE):

            directory.add_file('Limpar Cache de Arquivo: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(

                tools.convert_size(archive)), {'mode': 'cleararchive'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Limpar miniaturas antigas', {'mode': 'oldThumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Limpar registros de falhas', {'mode': 'clearcrash'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Eliminar bancos de dados', {'mode': 'purgedb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Novo começo - Fresh Start', {'mode': 'freshstart'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)



        directory.add_file('Auto-limpeza', fanart=CONFIG.ADDON_FANART, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)

        directory.add_file('Limpeza automática na inicialização: {0}'.format(autoclean.replace('true', on).replace('false', off)),

                           {'mode': 'togglesetting', 'name': 'autoclean'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        if autoclean == 'true':

            directory.add_file(

                '--- Freqüência de limpeza automática: [B][COLOR springgreen]{0}[/COLOR][/B]'.format(

                    CONFIG.CLEANFREQ[CONFIG.AUTOFREQ]),

                {'mode': 'changefreq'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            directory.add_file(

                '--- Limpar cache na inicialização: {0}'.format(cache.replace('true', on).replace('false', off)),

                {'mode': 'togglesetting', 'name': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            directory.add_file(

                '--- Limpar pacotes na inicialização: {0}'.format(packages.replace('true', on).replace('false', off)),

                {'mode': 'togglesetting', 'name': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            directory.add_file(

                '--- Limpar antigos polegares na inicialização: {0}'.format(thumbs.replace('true', on).replace('false', off)),

                {'mode': 'togglesetting', 'name': 'clearthumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Limpar cache de vídeo', fanart=CONFIG.ADDON_FANART, icon=CONFIG.ICONMAINT,

                           themeit=CONFIG.THEME1)

        directory.add_file(

            'Incluir Cache de Vídeo em Limpar Cache: {0}'.format(includevid.replace('true', on).replace('false', off)),

            {'mode': 'togglecache', 'name': 'includevideo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)



        if includeall == 'true':

            includegaia = 'true'

            includeexodusredux = 'true'

            includethecrew = 'true'

            includeyoda = 'true'

            includevenom = 'true'

            includenumbers = 'true'

            includescrubs = 'true'

            includeseren = 'true'

        else:

            includeexodusredux = 'true' if CONFIG.INCLUDEEXODUSREDUX == 'true' else 'false'

            includegaia = 'true' if CONFIG.INCLUDEGAIA == 'true' else 'false'

            includethecrew = 'true' if CONFIG.INCLUDETHECREW == 'true' else 'false'

            includeyoda = 'true' if CONFIG.INCLUDEYODA == 'true' else 'false'

            includevenom = 'true' if CONFIG.INCLUDEVENOM == 'true' else 'false'

            includenumbers = 'true' if CONFIG.INCLUDENUMBERS == 'true' else 'false'

            includescrubs = 'true' if CONFIG.INCLUDESCRUBS == 'true' else 'false'

            includeseren = 'true' if CONFIG.INCLUDESEREN == 'true' else 'false'



        if includevid == 'true':

            directory.add_file(

                '--- Incluir todos os complementos de vídeo: {0}'.format(includeall.replace('true', on).replace('false', off)),

                {'mode': 'togglecache', 'name': 'includeall'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.exodusredux)'):

                directory.add_file(

                    '--- Incluir Exodus Redux: {0}'.format(

                        includeexodusredux.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includeexodusredux'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.gaia)'):

                directory.add_file(

                    '--- Incluir Gaia: {0}'.format(includegaia.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includegaia'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.numbersbynumbers)'):

                directory.add_file(

                    '--- Incluir NuMb3r5: {0}'.format(includenumbers.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includenumbers'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.scrubsv2)'):

                directory.add_file(

                    '--- Incluir Scrubs v2: {0}'.format(includescrubs.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includescrubs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.seren)'):

                directory.add_file(

                    '--- Incluir Seren: {0}'.format(includeseren.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includeseren'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.thecrew)'):

                directory.add_file(

                    '--- Incluir THE CREW: {0}'.format(includethecrew.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includethecrew'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.venom)'):

                directory.add_file(

                    '--- Incluir Venom: {0}'.format(includevenom.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includevenom'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            if xbmc.getCondVisibility('System.HasAddon(plugin.video.yoda)'):

                directory.add_file(

                    '--- Incluir Yoda: {0}'.format(includeyoda.replace('true', on).replace('false', off)),

                    {'mode': 'togglecache', 'name': 'includeyoda'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

            directory.add_file('--- Habilitar todos os complementos de vídeo', {'mode': 'togglecache', 'name': 'true'}, icon=CONFIG.ICONMAINT,

                               themeit=CONFIG.THEME3)

            directory.add_file('--- Desativar todos os complementos de vídeo', {'mode': 'togglecache', 'name': 'false'}, icon=CONFIG.ICONMAINT,

                               themeit=CONFIG.THEME3)



    def addon_menu(self):

        directory.add_file('Remover complementos', {'mode': 'removeaddons'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_dir('Remover Dados Adicionais', {'mode': 'removeaddondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_dir('Habilitar / Desabilitar Complementos', {'mode': 'enableaddons'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        # directory.add_file('Habilitar / Desabilitar Add-ons para Adultos', 'toggleadult', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Forçar a atualização de todos os repositórios', {'mode': 'forceupdate'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Forçar atualização de todos os complementos', {'mode': 'forceupdate', 'action': 'auto'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)



   

    def logging_menu(self):

        errors = int(logging.error_checking(count=True))

        errorsfound = str(errors) + ' Error(s) Found' if errors > 0 else 'None Found'

        wizlogsize = ': [COLOR red]Not Found[/COLOR]' if not os.path.exists(

            CONFIG.WIZLOG) else ": [COLOR springgreen]{0}[/COLOR]".format(

            tools.convert_size(os.path.getsize(CONFIG.WIZLOG)))

            

        directory.add_file('Alternar registro de depuração', {'mode': 'enabledebug'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Carregar arquivo de log', {'mode': 'uploadlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Carregar arquivo de log: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(errorsfound), {'mode': 'viewerrorlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        if errors > 0:

            directory.add_file('Ver o último erro no log', {'mode': 'viewerrorlast'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Ver o último erro no log', {'mode': 'viewlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Ver Arquivo de Log do Assistente', {'mode': 'viewwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Limpar arquivo de log do assistente: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(wizlogsize), {'mode': 'clearwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

   

        

    def misc_menu(self):

        directory.add_file('Kodi 17 Fix', {'mode': 'kodi17fix'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_dir('Ferramentas de rede', {'mode': 'nettools'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Alternar fontes desconhecidas', {'mode': 'unknownsources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Alternar atualizações de complemento', {'mode': 'toggleupdates'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Recarregar o tema', {'mode': 'forceskin'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Recarregar Perfil', {'mode': 'forceprofile'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Forçar o fechamento do Kodi', {'mode': 'forceclose'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)



    def backup_menu(self):

        directory.add_file('Limpar pasta de backup', {'mode': 'clearbackup'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Local de backup: [COLOR {0}]{1}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.MYBUILDS), {'mode': 'settings', 'name': 'Maintenance'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Cópia de segurança]: Build', {'mode': 'backup', 'action': 'build'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Cópia de segurança]: GuiFix', {'mode': 'backup', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Cópia de segurança]: Tema', {'mode': 'backup', 'action': 'theme'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Cópia de segurança]: Pacote de Complementos', {'mode': 'backup', 'action': 'addonpack'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Cópia de segurança]: Dados adicionais', {'mode': 'backup', 'action': 'addondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: Local Build', {'mode': 'restore', 'action': 'build'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: Local GuiFix', {'mode': 'restore', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: Local Tema', {'mode': 'restore', 'action': 'theme'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: Local Addon Pack', {'mode': 'restore', 'action': 'addonpack'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: Local Dados adicionais', {'mode': 'restore', 'action': 'addondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: External Build', {'mode': 'restore', 'action': 'build', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: External GuiFix', {'mode': 'restore', 'action': 'gui', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: External Tema', {'mode': 'restore', 'action': 'theme', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: External Addon Pack', {'mode': 'restore', 'action': 'addonpack', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('[Restaurar]: External Dados adicionais', {'mode': 'restore', 'action': 'addondata', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)



    def tweaks_menu(self):

        directory.add_dir('Configurações avançadas', {'mode': 'advanced_settings'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Verificar fontes para links quebrados', {'mode': 'checksources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Verificar Repositórios Quebrados', {'mode': 'checkrepos'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Remover nomes de arquivos não ASCII', {'mode': 'asciicheck'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        # directory.add_file('Alternar senhas na entrada do teclado', {'mode': 'togglepasswords'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_file('Converter caminhos em especiais', {'mode': 'convertpath'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_dir('Informação do sistema', {'mode': 'systeminfo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
