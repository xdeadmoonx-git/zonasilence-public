init -1000 python:

    global zona_default_screens

    def zona_screens_save():
        if store.persistent.zona_default_screens is True:
            renpy.display.screen.screens[("zona_old_say", None)] = renpy.display.screen.screens[("say", None)]
            renpy.display.screen.screens[("zona_old_nvl", None)] = renpy.display.screen.screens[("nvl", None)]
            renpy.display.screen.screens[("zona_old_load", None)] = renpy.display.screen.screens[("load", None)]
            renpy.display.screen.screens[("zona_old_save", None)] = renpy.display.screen.screens[("save", None)]
            renpy.display.screen.screens[("zona_old_text_history_screen", None)] = renpy.display.screen.screens[("text_history_screen", None)]

            store.persistent.zona_default_screens = False

        else:
            pass

    def zona_screens_activate():
        config.window_title = u"Зона безмолвия"
        config.name = "zona"
        config.version = "1.01"

        persistent._file_page = "zona_FilePage_1"  
        
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("zona_say", None)]
        renpy.display.screen.screens[("load", None)] = renpy.display.screen.screens[("zona_load", None)]
        renpy.display.screen.screens[("save", None)] = renpy.display.screen.screens[("zona_save", None)]
        renpy.display.screen.screens[("text_history_screen", None)] = renpy.display.screen.screens[("zona_history", None)]
        renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("zona_nvl", None)]

        zona_set_adv_mode()


    def zona_screens_default():
        if store.persistent.zona_default_screens is True:
            persistent._file_page = 1
            config.window_title = u"Бесконечное Лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
            renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("zona_old_say", None)]
            renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("zona_old_nvl", None)]
            renpy.display.screen.screens[("load", None)] = renpy.display.screen.screens[("zona_old_load", None)]
            renpy.display.screen.screens[("save", None)] = renpy.display.screen.screens[("zona_old_save", None)]
            renpy.display.screen.screens[("text_history_screen", None)] = renpy.display.screen.screens[("zona_old_text_history_screen", None)]

            char_define("narrator", is_nvl=False)

            store.persistent.zona_default_screens = False


        else:
            pass