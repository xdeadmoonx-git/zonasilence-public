init:
    $ mods["zona_start"]=u"Зона Безмолвия"
    $ zona_define_assets('zona', zona_sprites_folder='source/images/sprites')


label zona_start:
    $ renpy.block_rollback()
    window hide
    $ renpy.transition(Dissolve(2))
    python:
        store.persistent.zona_default_screens = True
        renpy.game.context().force_checkpoint = True
        zona_screens_save()
        zona_screens_activate()
        zona_say_set = "white"

    $ default_mouse = "zona_mouse"
    jump zone_of_silence

label zona_exit:

    $ renpy.block_rollback()
    python:
        store.persistent.zona_default_screens = True
        zona_screens_default()

    stop music fadeout 4
    stop sound_loop fadeout 4
    stop music_player fadeout 4
    stop ambience fadeout 4
    stop sound_loop fadeout 4
    scene black
    with Fade(1.5, 2, 1.5)

    $ default_mouse = "default"
    $ renpy.show("black")
    $ renpy.call("_start_store")
    $ renpy.start_predict_screen("main_menu")
    $ renpy.display.interface.with_none(overlay=False)
    $ renpy.music.play(config.main_menu_music, if_changed=True)
    $ renpy.stop_predict_screen("main_menu")
    $ renpy.transition(config.end_splash_transition)
    $ renpy.game.context().force_checkpoint = True
    $ renpy.free_memory()
    $ renpy.call("_main_menu")
