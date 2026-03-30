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



import xbmc

import xbmcgui



import os



from resources.libs import check

from resources.libs import db

from resources.libs import extract

from resources.libs import install

from resources.libs import skin

from resources.libs.common import logging

from resources.libs.common import tools

from resources.libs.common.config import CONFIG

from resources.libs.downloader import Downloader





class Wizard:



    def __init__(self):

        tools.ensure_folders(CONFIG.PACKAGES)

        

        self.dialog = xbmcgui.Dialog()

        self.dialogProgress = xbmcgui.DialogProgress()



    def _prompt_for_wipe(self):

        # Should we wipe first?

        if self.dialog.yesno(CONFIG.ADDONTITLE,

                           "[COLOR {0}]Você deseja restaurar seu".format(CONFIG.COLOR2) +'\n' + "Configuração do Kodi para as configurações padrão" + '\n' + "Antes de instalar o backup de compilação?[/COLOR]",

                           nolabel='[B][COLOR red]Não[/COLOR][/B]',

                           yeslabel='[B][COLOR springgreen]Sim[/COLOR][/B]'):

            install.wipe()



    def build(self, name, over=False):

        # if action == 'normal':

            # if CONFIG.KEEPTRAKT == 'true':

                # from resources.libs import traktit

                # traktit.auto_update('all')

                # CONFIG.set_setting('traktnextsave', tools.get_date(days=3, formatted=True))

            # if CONFIG.KEEPDEBRID == 'true':

                # from resources.libs import debridit

                # debridit.auto_update('all')

                # CONFIG.set_setting('debridnextsave', tools.get_date(days=3, formatted=True))

            # if CONFIG.KEEPLOGIN == 'true':

                # from resources.libs import loginit

                # loginit.auto_update('all')

                # CONFIG.set_setting('loginnextsave', tools.get_date(days=3, formatted=True))



        temp_kodiv = int(CONFIG.KODIV)

        buildv = int(float(check.check_build(name, 'kodi')))



        if not temp_kodiv == buildv:

            warning = True

        else:

            warning = False



        if warning:

            yes_pressed = self.dialog.yesno("{0} - [COLOR red]AVISO!![/COLOR]".format(CONFIG.ADDONTITLE), '[COLOR {0}]Existe uma chance de que a pele não apareça corretamente'.format(CONFIG.COLOR2) + '\n' + 'Ao instalar um {0} build em uma instalação Kodi {1}'.format(check.check_build(name, 'kodi'), CONFIG.KODIV) + '\n' + 'Você ainda gostaria de instalar: [COLOR {0}]{1} v{2}[/COLOR]?[/COLOR]'.format(CONFIG.COLOR1, name, check.check_build(name, 'version')), nolabel='[B][COLOR red]Não, Cancelar[/COLOR][/B]', yeslabel='[B][COLOR springgreen]Sim , Instalar[/COLOR][/B]')

        else:

            if over:

                yes_pressed = 1

            else:

                yes_pressed = self.dialog.yesno(CONFIG.ADDONTITLE, '[COLOR {0}]Você gostaria de baixar e instalar: '.format(CONFIG.COLOR2) + '[COLOR {0}]{1} v{2}[/COLOR]?[/COLOR]'.format(CONFIG.COLOR1, name, check.check_build(name,'version')), nolabel='[B][COLOR red]Não, Cancelar[/COLOR][/B]', yeslabel='[B][COLOR springgreen]Sim, Instalar[/COLOR][/B]')

        if yes_pressed:

            CONFIG.clear_setting('build')

            buildzip = check.check_build(name, 'url')

            zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')



            self.dialogProgress.create(CONFIG.ADDONTITLE, '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2} v{3}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, name, check.check_build(name, 'version')) + '\n' + 'Por favor, aguarde')



            lib = os.path.join(CONFIG.MYBUILDS, '{0}.zip'.format(zipname))

            

            try:

                os.remove(lib)

            except:

                pass



            Downloader().download(buildzip, lib)

            xbmc.sleep(500)

            

            if os.path.getsize(lib) == 0:

                try:

                    os.remove(lib)

                except:

                    pass

                    

                return

                

            install.wipe()

                

            skin.look_and_feel_data('save')

            

            title = '[COLOR {0}][B]Instalando:[/B][/COLOR] [COLOR {1}]{2} v{3}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, name, check.check_build(name, 'version'))

            self.dialogProgress.update(0, title + '\n' + 'Por favor, aguardet')

            percent, errors, error = extract.all(lib, CONFIG.HOME, title=title)

            

            skin.skin_to_default('Build Install')



            if int(float(percent)) > 0:

                db.fix_metas()

                CONFIG.set_setting('buildname', name)

                CONFIG.set_setting('buildversion', check.check_build(name, 'version'))

                CONFIG.set_setting('buildtheme', '')

                CONFIG.set_setting('latestversion', check.check_build(name, 'version'))

                CONFIG.set_setting('nextbuildcheck', tools.get_date(days=CONFIG.UPDATECHECK, formatted=True))

                CONFIG.set_setting('installed', 'true')

                CONFIG.set_setting('extract', percent)

                CONFIG.set_setting('errors', errors)

                logging.log('INSTALADO {0}: [ERRORS:{1}]'.format(percent, errors))



                try:

                    os.remove(lib)

                except:

                    pass



                if int(float(errors)) > 0:

                    yes_pressed = self.dialog.yesno(CONFIG.ADDONTITLE,

                                       '[COLOR {0}][COLOR {1}]{2} v{3}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, name, check.check_build(name, 'version')) +'\n' + 'Concluído: [COLOR {0}]{1}{2}[/COLOR] [Errors:[COLOR {3}]{4}[/COLOR]]'.format(CONFIG.COLOR1, percent, '%', CONFIG.COLOR1, errors) + '\n' + 'Você gostaria de ver os erros?[/COLOR]',

                                       nolabel='[B][COLOR red]Não, obrigado[/COLOR][/B]',

                                       yeslabel='[B][COLOR springgreen]Ver erros[/COLOR][/B]')

                    if yes_pressed:

                        from resources.libs.gui import window

                        window.show_text_box("Visualizando Erros de Instalação de Compilação", error)

                self.dialogProgress.close()



                from resources.libs.gui.build_menu import BuildMenu

                themecount = BuildMenu().theme_count(name)



                if themecount > 0:

                    self.theme(name, 'theme')



                db.addon_database(CONFIG.ADDON_ID, 1)

                db.force_check_updates(over=True)



                self.dialog.ok(CONFIG.ADDONTITLE, "[COLOR {0}]Para salvar as alterações, você agora precisa forçar o fechamento do Kodi, pressione OK para forçar o fechamento do Kodi[/COLOR]".format(CONFIG.COLOR2))

                tools.kill_kodi(over=True)

            else:

                from resources.libs.gui import window

                window.show_text_box("Visualizando Erros de Instalação de Compilação", error)

        else:

            logging.log_notify(CONFIG.ADDONTITLE,

                               '[COLOR {0}]Build Install: Cancelado![/COLOR]'.format(CONFIG.COLOR2))



    def gui(self, name, over=False):

        if name == CONFIG.get_setting('buildname'):

            if over:

                yes_pressed = 1

            else:

                yes_pressed = self.dialog.yesno(CONFIG.ADDONTITLE,

                                   '[COLOR {0}]Você gostaria de aplicar o guifix para:'.format(CONFIG.COLOR2) + '\n' + '[COLOR {0}]{1}[/COLOR]?[/COLOR]'.format(CONFIG.COLOR1, name),

                                   nolabel='[B][COLOR red]Não, Cancelar[/COLOR][/B]',

                                   yeslabel='[B][COLOR springgreen]Aplicar Fix[/COLOR][/B]')

        else:

            yes_pressed = self.dialog.yesno("{0} - [COLOR red]AVISO!![/COLOR]".format(CONFIG.ADDONTITLE),

                               "[COLOR {0}][COLOR {1}]{2}[/COLOR] o build da comunidade não está instalado no momento.".format(CONFIG.COLOR2, CONFIG.COLOR1, name) + '\n' + "Você gostaria de aplicar o guiFix mesmo assim?.[/COLOR]",

                               nolabel='[B][COLOR red]Não, Cancelar[/COLOR][/B]',

                               yeslabel='[B][COLOR springgreen]Aplicar Fix[/COLOR][/B]')

        if yes_pressed:

            guizip = check.check_build(name, 'gui')

            zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')



            response = tools.open_url(guizip, check=True)

            if not response:

                logging.log_notify(CONFIG.ADDONTITLE,

                                   '[COLOR {0}]GuiFix: Url Zip Inválido![/COLOR]'.format(CONFIG.COLOR2))

                return



            self.dialogProgress.create(CONFIG.ADDONTITLE, '[COLOR {0}][B]Baixando GuiFix:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, name), '', 'Por favor, aguarde')



            lib = os.path.join(CONFIG.PACKAGES, '{0}_guisettings.zip'.format(zipname))

            

            try:

                os.remove(lib)

            except:

                pass



            Downloader().download(guizip, lib)

            xbmc.sleep(500)

            

            if os.path.getsize(lib) == 0:

                try:

                    os.remove(lib)

                except:

                    pass

                    

                return

            

            title = '[COLOR {0}][B]Instalando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, name)

            self.dialogProgress.update(0, title + '\n' + 'Por favor, aguarde')

            extract.all(lib, CONFIG.USERDATA, title=title)

            self.dialogProgress.close()

            skin.skin_to_default('Build Install')

            skin.look_and_feel_data('save')

            installed = db.grab_addons(lib)

            db.addon_database(installed, 1, True)



            self.dialog.ok(CONFIG.ADDONTITLE, "[COLOR {0}]Para salvar as alterações, você agora precisa forçar o fechamento do Kodi, pressione OK para forçar o fechamento do Kodi[/COLOR]".format(CONFIG.COLOR2))

            tools.kill_kodi(over=True)

        else:

            logging.log_notify(CONFIG.ADDONTITLE,

                               '[COLOR {0}]GuiFix: Cancelado![/COLOR]'.format(CONFIG.COLOR2))



    def theme(self, name, theme, over=False):

        installtheme = False



        if not theme:

            themefile = check.check_build(name, 'theme')



            response = tools.open_url(themefile, check=True)

            if response:

                from resources.libs.gui.build_menu import BuildMenu

                themes = BuildMenu().theme_count(name, False)

                if len(themes) > 0:

                    if self.dialog.yesno(CONFIG.ADDONTITLE, "[COLOR {0}]O Build [COLOR {1}]{2}[/COLOR] vem com [COLOR {3}] {4} [/ COLOR] temas diferentes".format(CONFIG.COLOR2, CONFIG.COLOR1, name, CONFIG.COLOR1, len(themes)) + '\n' + "Você gostaria de instalar um agora?[/COLOR]",

                                    yeslabel="[B][COLOR springgreen]Instalar tema[/COLOR][/B]",

                                    nolabel="[B][COLOR red]Cancelar Temas[/COLOR][/B]"):

                        logging.log("Theme List: {0}".format(str(themes)))

                        ret = self.dialog.select(CONFIG.ADDONTITLE, themes)

                        logging.log("Instalação de tema selecionada: {0}".format(ret))

                        if not ret == -1:

                            theme = themes[ret]

                            installtheme = True

                        else:

                            logging.log_notify(CONFIG.ADDONTITLE,

                                               '[COLOR {0}]Instalação do tema: cancelada![/COLOR]'.format(CONFIG.COLOR2))

                            return

                    else:

                        logging.log_notify(CONFIG.ADDONTITLE,

                                           '[COLOR {0}] Instalação do tema: Cancelado![/COLOR]'.format(CONFIG.COLOR2))

                        return

            else:

                logging.log_notify(CONFIG.ADDONTITLE,

                                   '[COLOR {0}]Instalação do tema: Nenhum encontrado![/COLOR]'.format(CONFIG.COLOR2))

        else:

            installtheme = self.dialog.yesno(CONFIG.ADDONTITLE, '[COLOR {0}]Você gostaria de instalar o tema:'.format(CONFIG.COLOR2) +' \n' + '[COLOR {0}]{1}[/COLOR]'.format(CONFIG.COLOR1, theme) + '\n' + 'for [COLOR {0}]{1} v{2}[/COLOR]?[/COLOR]'.format(CONFIG.COLOR1, name, check.check_build(name,'version')),yeslabel="[B][COLOR springgreen]Instalar Tema[/COLOR][/B]", nolabel="[B][COLOR red]Cancelar Tema[/COLOR][/B]")

                                        

        if installtheme:

            themezip = check.check_theme(name, theme, 'url')

            zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')



            response = tools.open_url(themezip, check=True)

            if not response:

                logging.log_notify(CONFIG.ADDONTITLE,

                                   '[COLOR {0}]Instalação do tema: URL zip inválido![/COLOR]'.format(CONFIG.COLOR2))

                return False



            self.dialogProgress.create(CONFIG.ADDONTITLE, '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, zipname) +' \n' + 'Por favor, aguarde')



            lib = os.path.join(CONFIG.PACKAGES, '{0}.zip'.format(zipname))

            

            try:

                os.remove(lib)

            except:

                pass



            Downloader().download(themezip, lib)

            xbmc.sleep(500)

            

            if os.path.getsize(lib) == 0:

                try:

                    os.remove(lib)

                except:

                    pass

                    

                return

            

            self.dialogProgress.update(0, '\n' + "Instalando {0}".format(name))



            test1 = False

            test2 = False

            

            from resources.libs import skin

            from resources.libs import test

            test1 = test.test_theme(lib) if CONFIG.SKIN not in skin.DEFAULT_SKINS else False

            test2 = test.test_gui(lib) if CONFIG.SKIN not in skin.DEFAULT_SKINS else False



            if test1:

                skin.look_and_feel_data('save')

                swap = skin.skin_to_default('Instalação de tema')



                if not swap:

                    return False



                xbmc.sleep(500)



            title = '[COLOR {0}][B]Instalando Tema:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.COLOR1, theme)

            self.dialogProgress.update(0, title + '\n' + 'Por favor, aguarde')

            percent, errors, error = extract.all(lib, CONFIG.HOME, title=title)

            CONFIG.set_setting('buildtheme', theme)

            logging.log('INSTALADO:{1}]'.format(percent, errors))

            self.dialogProgress.close()



            db.force_check_updates(over=True)

            installed = db.grab_addons(lib)

            db.addon_database(installed, 1, True)



            if test2:

                skin.look_and_feel_data('save')

                skin.skin_to_default("Theme Install")

                gotoskin = CONFIG.get_setting('defaultskin')

                skin.switch_to_skin(gotoskin, "Theme Installer")

                skin.look_and_feel_data('restore')

            elif test1:

                skin.look_and_feel_data('save')

                skin.skin_to_default("Theme Install")

                gotoskin = CONFIG.get_setting('defaultskin')

                skin.switch_to_skin(gotoskin, "Theme Installer")

                skin.look_and_feel_data('restore')

            else:

                xbmc.executebuiltin("ReloadSkin()")

                xbmc.sleep(1000)

                xbmc.executebuiltin("Container.Refresh()")

        else:

            logging.log_notify(CONFIG.ADDONTITLE,

                               '[COLOR {0}]Theme Install: Cancelled![/COLOR]'.format(CONFIG.COLOR2))





def wizard(action, name, url):

    cls = Wizard()



    if action in ['fresh', 'normal']:

        cls.build(action, name)

    elif action == 'gui':

        cls.gui(name)

    elif action == 'theme':

        cls.theme(name, url)
