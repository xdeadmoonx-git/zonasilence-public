init:

    transform zona_heartbeat(m):
        truecenter
        subpixel True

        block:
            linear 0.33 zoom 1.00 + 0.06 * m xalign 0.5  + 0.012 * m blur 3

            linear 0.37 zoom 1.00 xalign 0.5 blur 0

            pause 0.40

            linear 0.29 zoom 1.00 + 0.04 * m xalign 0.5  - 0.012 * m blur 2

            linear 0.33 zoom 1.00 xalign 0.5 blur 0

            pause 0.70

            repeat

    transform zona_settings_button_anim:
        on hover:
            easein 0.1 yoffset -2 zoom 1.1
        on idle:
            easein 0.1 yoffset 2 zoom 1.0
            
    transform zona_headshake(zooming, zoom1, zoom2, zoom3, rotate1, rotate2, xxoffset, yyoffset, blur1, blur2, blur3, blur4, blur5, blur6):
        subpixel True
        zoom zooming xalign 0.5 yalign 0.5
        parallel:
            ease 0.2 blur blur1
            ease 4 blur blur2
            ease 1.5 blur blur3
            ease 0.2 blur blur4
            ease 3 blur blur5
            ease 4 blur blur6
            repeat
        parallel:
            ease 1.8 zoom zoom1
            ease 2.2 zoom zoom2
            ease 1.6 zoom zoom3
            repeat
        parallel:
            ease 1.5 rotate rotate1
            ease 2.0 rotate rotate2
            ease 1.5 rotate 0
            repeat
        parallel:
            ease 1.3 xoffset -xxoffset - 4 yoffset -yyoffset - 1
            ease 1.5 xoffset xxoffset + 8 yoffset yyoffset + 4
            ease 1.4 xoffset -xxoffset - 1 yoffset yyoffset + 6
            ease 1.6 xoffset 0 yoffset 0
            repeat
