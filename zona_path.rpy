init -1199 python:
    from os import path
    import store

    zona_mod_folder = 'zona/'
    zona_main_path = zona_mod_folder + 'source/'
    zona_images = zona_main_path + 'images/'
    zona_fonts = zona_main_path + 'fonts/'
    zona_videos = zona_main_path + 'videos/'
    zona_prefix = 'zona_'

    def zona_define_assets(zona_mod_folder, zona_sprites_folder):
        for file in renpy.list_files():

            if zona_mod_folder not in file:
                continue

            filename = path.splitext(path.basename(str(file)))[0]
            lower_file = file.lower()

            # БГ
            if '/bg/' in lower_file and lower_file.endswith(('.png', '.jpg')):
                renpy.image(
                    'bg ' + zona_prefix + filename,
                    im.Composite((1920,1080), (0,0), file)   
                )

            # Арты
            elif '/cg/' in lower_file and lower_file.endswith(('.png', '.jpg')):
                renpy.image(
                    'cg ' + zona_prefix + filename,
                    im.Composite((1920,1080), (0,0), file)   
                )

            # Спрайты
            elif zona_sprites_folder in file and lower_file.endswith('.png'):
                parts = file.replace('\\', '/').split('/')
                try:
                    idx = parts.index('sprites') + 1
                    char_name = parts[idx]
                    next_part = parts[idx+1]
                    distance = next_part if next_part in ('close', 'normal', 'far') else 'normal'
                    image_name = filename
                    #image_name = f"{char_name}_{filename}"

                    renpy.image(
                        #f"{char_name} {img_name} {distance}",
                        "{char} {img} {dist}".format(
                            char = char_name,
                            img  = image_name,
                            dist = distance
                        ),
                        ConditionSwitch(
                            "zona_sprite_set == 'sunset'",
                            im.MatrixColor(file, im.matrix.tint(0.94, 0.82, 1.0)),
                            "zona_sprite_set == 'night'",
                            im.MatrixColor(file, im.matrix.tint(0.63, 0.78, 0.82)),
                            True, file
                        )
                    )

                except:
                    pass

            # Всё остальное
            elif lower_file.endswith(('.png', '.jpg')):
                renpy.image(zona_prefix + filename, file)

            # Видео
            elif lower_file.endswith(('.webm', '.flv', '.vob')):
                renpy.image(
                    'videos ' + zona_prefix + filename,
                    Movie(
                        fps=60,
                        size=(1920,1080),
                        loop=False,
                        play=file
                    )
                )

            # Аудио
            elif file.endswith(('.wav', '.mp2', '.mp3', '.ogg', '.opus')):
                globals()[zona_prefix + filename] = file



    def zona_define_es_assets(zona_es_folder):
        for file in renpy.list_files():
            if zona_es_folder in file:
                file_name = path.splitext(path.basename(file))[0]
                if file.endswith((".png", ".jpg")):
                    renpy.image(
                        "bg " + poligon_prefix + file_name,
                        im.Composite((1920,1080), (0,0), file)
                    )