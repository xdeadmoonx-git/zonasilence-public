init:
    $ zona_sprite_set = None

    define config.mouse["zona_mouse"] = [("zona/source/images/gui/mouse/mouse.png", 0, 0)]
    image zona_vbar_history = im.Scale("zona/source/images/gui/bar/vbar_track.png", 15, 810)




#Диалоговое окно
screen zona_say:

    key ['h','H','р','Р'] action HideInterface()
    key ['m','M','ь','Ь'] action ShowMenu("game_menu_selector")
    key "mouseup_3" action ShowMenu("game_menu_selector")


    window:

        background None
        id "window"

        add zona_images + "gui/say/dialogue_box_" + zona_say_set + ".png":
            xpos 174
            ypos 866
            yoffset -23
            xoffset 7
        imagebutton:
            auto zona_images + "gui/say/backward_%s_" + zona_say_set + ".png"
            xpos 38
            ypos 924
            yoffset -25
            xoffset -11
            action ShowMenu("zona_history")
        imagebutton:
            auto zona_images + "gui/say/forward_%s_" + zona_say_set + ".png"
            xpos 1768
            ypos 924
            yoffset -25
            xoffset -15
            action Skip()
        imagebutton:
            auto zona_images + "gui/say/hide_%s_" + zona_say_set + ".png"
            xpos 1567
            ypos 880
            xoffset 16
            yoffset -16
            action HideInterface()
        imagebutton:
            auto zona_images + "gui/say/menu_%s_" + zona_say_set + ".png"
            xpos 1567
            ypos 880
            xoffset 90
            yoffset -16
            action ShowMenu("game_menu_selector")

        text what:
            id "what"
            font zona_fonts + "say_what.ttf"
            xpos 193
            ypos 911
            xoffset 14
            yoffset -19
            xmaximum 1505
            size 30
            line_spacing 1
            color "#FFFFFF"
        if who:
            text who:
                id "who"
                font zona_fonts + "say_who.ttf"
                xpos 193
                ypos 871
                xoffset 13
                yoffset -19
                size 28
                line_spacing 1

screen zona_load:
    tag menu
    key "K_ESCAPE" action Return()


    modal True
    window:
        background "zona_save_load_background"

        add zona_images + "gui/zatemnenie_light.png":
            ypos -20
            xpos -20
        text "Загрузить":
            style "zona_save_screens_style"
            size 75
            text_align 0.5
            xalign 0.1
            yalign 0.060
            xoffset -10
            antialias True
            kerning 2


        textbutton "Сохранить":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            text_size 65
            xalign 0.9
            yalign 0.07
            text_align 0.5
            at zona_settings_button_anim
            action ShowMenu("zona_save")


        textbutton "Загрузить?":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            ypos 950
            xalign 0.5
            action FileLoad(selected_slot)
            at zona_settings_button_anim

        textbutton "Забыть":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            xpos 1610
            ypos 950
            action FileDelete(selected_slot)
            at zona_settings_button_anim

        textbutton "Назад":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            xpos 60
            ypos 950
            action Return()
            at zona_settings_button_anim

        vbox:
            spacing 40
            align (0.1, 0.2)
            xoffset -100
            yoffset 120


            for page in ["zona_FilePage_1", "zona_FilePage_2", "zona_FilePage_3", "zona_FilePage_4", "zona_FilePage_5", "zona_FilePage_6"]:
                textbutton str(page[-1]):
                    text_style "zona_save_screens_style"
                    style "zona_save_screens_style"
                    activate_sound zona_start_sound
                    hover_sound zona_button_menu
                    action FilePage(page)


        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1001, 1013):
                $ display_num = i - 1000
                fixed:
                    add FileScreenshot(str(i)) at zona_settings_button_anim:
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", str(i))
                        activate_sound zona_start_sound
                        hover_sound zona_button_menu
                        xfill False
                        yfill False
                        style "zona_save_load_button"
                        has fixed
                        text ("%s." % display_num + FileTime(str(i), format=' %d.%m.%y, %H:%M', empty=" "+"Пусто") + "\n" +FileSaveName(str(i))) at zona_settings_button_anim:
                            style "zona_save_load_button_text"
                            xpos 15
                            ypos 15
screen zona_save:
    tag menu
    key "K_ESCAPE" action Return()


    modal True

    window:
        background "zona_save_load_background"

        add zona_images + "gui/zatemnenie_light.png":
            ypos -20
            xpos -20
        text "Сохранить":
            style "zona_save_screens_style"
            size 75
            text_align 0.5
            xalign 0.9
            yalign 0.060
            antialias True
            kerning 2
            at zona_settings_button_anim

        textbutton "Загрузить":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            text_size 65
            xalign 0.1
            yalign 0.07
            text_align 0.5
            at zona_settings_button_anim
            action ShowMenu("zona_load")

        textbutton "Сохранить?":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            ypos 950
            xalign 0.5
            action FileSave(selected_slot)
            at zona_settings_button_anim

        textbutton "Забыть":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            xpos 1610
            ypos 950
            action FileDelete(selected_slot)
            at zona_settings_button_anim

        textbutton "Назад":
            text_style "zona_save_screens_style"
            style "zona_save_screens_style"
            activate_sound zona_start_sound hover_sound zona_button_menu
            xpos 60
            ypos 950
            action Return()
            at zona_settings_button_anim

        vbox:
            spacing 40
            align (0.1, 0.2)
            xoffset -100
            yoffset 120

            for page in ["zona_FilePage_1", "zona_FilePage_2", "zona_FilePage_3", "zona_FilePage_4", "zona_FilePage_5", "zona_FilePage_6"]:
                textbutton str(page[-1]):
                    text_style "zona_save_screens_style"
                    style "zona_save_screens_style"
                    activate_sound zona_start_sound
                    hover_sound zona_button_menu
                    action FilePage(page)
        
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1001, 1013):
                $ display_num = i - 1000
                fixed:
                    add FileScreenshot(str(i)) at zona_settings_button_anim:
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", str(i))
                        activate_sound zona_start_sound
                        hover_sound zona_button_menu
                        xfill False
                        yfill False
                        style "zona_save_load_button"
                        has fixed
                        text ("%s." % display_num + FileTime(str(i), format=' %d.%m.%y, %H:%M', empty=" "+"Пусто") + "\n" +FileSaveName(str(i))) at zona_settings_button_anim:
                            style "zona_save_load_button_text"
                            xpos 15
                            ypos 15
#Переопределение истории, чтобы был стиль текста из мода
#Ну и добавление своего скроллбара
screen zona_history:

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 28
    $ history_name_size = 28

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame("images/gui/choice/day/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:

        viewport id "zona_history":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:

                if h.who:

                    text h.who:
                        font zona_fonts + "say_who.otf"
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what style "zona_history_text" text_style "zona_history_text" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax xpos 100

        
        vbar value YScrollValue("zona_history") bottom_bar "zona_vbar_history" top_bar "zona_vbar_history" thumb "zona/source/images/gui/bar/vthumb.png" xoffset 1700

screen zona_nvl:

    $ zona_nvl_size = 30

    add zona_images + "gui/nvl_box.png"

    vbox:
        spacing 10

        for who, what, who_id, what_id, window_id in dialogue:

            window:
                id window_id

                has hbox
                xpos 150
                ypos 75
                spacing 10

                if who:
                    text who id who_id size zona_nvl_size font zona_fonts + "say_who.ttf"

                text what id what_id xmaximum 1620 size zona_nvl_size font zona_fonts + "say_what.ttf" color "FFFFFF"

    imagebutton auto zona_images + "gui/say/forward_%s_" + zona_say_set + ".png" xpos 1652 ypos 866 xoffset 70 yoffset 30 action Skip()
    imagebutton auto zona_images + "gui/say/backward_%s_" + zona_say_set + ".png" xpos 54 ypos 866 xoffset 30 yoffset 30 action ShowMenu("zona_history")
