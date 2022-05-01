default persistent._mas_count = 0
default persistent._mas_counttwo = 0
default persistent._mas_countthree = 0

init:
    image tester_idle = im.Scale("mod_assets/other/transparent.png", 30, 30)
    image tester2_idle = im.Scale("mod_assets/other/transparent.png", 180, 120)

init python:
    
    def HKBPHideButtons():
        if mas_HKBPIsVisible():
            config.overlay_screens.remove("extraplus_overlay")
            renpy.hide_screen("extraplus_overlay")

    def HKBPShowButtons():
        if not mas_HKBPIsVisible():
            config.overlay_screens.append("extraplus_overlay")

    def mas_HKBPIsVisible():
        """
        RETURNS: True if teh Hotkey buttons are visible, False otherwise
        """
        return "extraplus_overlay" in config.overlay_screens

init python:

    Zer0fixer = "¿Qué haces aquí?"
    Zer0fixer = "Espero te sirva algo de mi pequeño trabajo."
    Zer0fixer = "Esta es una versión demo, por ello está tan acortada."
    HKBPShowButtons()

screen extraplus_overlay():
    zorder 50
    style_prefix "hkb"

    vbox:
        xpos 0.05

        yanchor 1.0
        ypos 50

        if store.mas_hotkeys.talk_enabled == False:
            text _("")
        elif store.hkb_button.talk_enabled == False:
            text _("")
        else:
            if mas_curr_affection == mas_affection.UPSET or mas_curr_affection == mas_affection.DISTRESSED or mas_curr_affection == mas_affection.BROKEN:
                textbutton _("Extra+")
            else:
                textbutton _("Extra+") action Jump("show_extraplus")

label show_exp:
    $ expression_m = renpy.random.randint(1,5)
    if expression_m == 1:
        show monika 1esa

    elif expression_m == 2:
        show monika 1tuu

    elif expression_m == 3:
        show monika 1nua

    elif expression_m == 4:
        show monika 1eua

    elif expression_m == 5:
        show monika 1rublp
    call screen interaccionesbeta
    return

label show_extraplus:
    $ mas_temp_zoom_level = store.mas_sprites.zoom_level
    call monika_zoom_transition_reset (1.5) from _call_monika_zoom_transition_reset_9
    $ mas_RaiseShield_core()
    $ expression_m = renpy.random.randint(1,5)
    if expression_m == 1:
        show monika 1esa

    elif expression_m == 2:
        show monika 1tuu

    elif expression_m == 3:
        show monika 1nua

    elif expression_m == 4:
        show monika 1eua

    elif expression_m == 5:
        show monika 1rublp
    call screen interaccionesbeta
    return
        
screen interaccionesbeta():
    zorder 50
    style_prefix "hkb"

    vbox:
        xpos 0.05

        yanchor 1.0
        ypos 170

        textbutton _("Cerrar") action Jump("back_mas")

        textbutton _("Cita") action Jump("date_mas")

        textbutton _("Minijuego") action Jump("monika_minigames")

        textbutton _("Adiciones") action Jump("tools_mas")

    #Cabeza
    imagebutton:
        idle "tester2_idle"
        xpos 550
        ypos 10
        action Jump("monika_headpatbeta")
    #Nariz
    imagebutton:
        idle "tester_idle"
        xpos 620
        ypos 235
        action Jump("monika_boopbeta")
    #Mejillas
    imagebutton:
        idle "tester_idle"
        xpos 700
        ypos 256
        action Jump("monika_cheeksbeta")
    imagebutton:
        idle "tester_idle"
        xpos 550
        ypos 256
        action Jump("monika_cheeksbeta")

#Solo labels
label monika_boopbeta:
    $ persistent._mas_count += 1
    hide screen interaccionesbeta
    if persistent._mas_count == 1:
        m 1tsb "Que haces jugando con mi nariz, Beta tester.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        hide screen tear
        m 1hub "Que haces jugando con mi nariz, [player].{fast}"
        m 1hksdrb "No es que moleste, ¡simplemente me tomo por sorpresa!"
        m 1hua "Jeje~"
    else:
        m 1hub "*Boop*"
    jump show_exp
    return

label monika_cheeksbeta:
    $ persistent._mas_counttwo += 1
    hide screen interaccionesbeta
    if persistent._mas_counttwo == 1:
        m 2wubsd "Eh, sentí un pellizco en la mejilla."
        m 2lksdrb "Oh, solamente fue tu cursor. Me tomaste por sorpresa."
        m 2ttb "Pero debo de preguntar, ¿Qué estás tramando [player]?"
        m 1hubla "¿Querías ver como reaccionaria a eso?"
    else:
        m 2fua "Jeje~"
        m 2hua "Sería bueno que usaras tu mano en vez del cursor, pero falta mucho para que eso pase."
    jump show_exp
    return

label monika_headpatbeta:
    $ persistent._mas_countthree += 1
    hide screen interaccionesbeta
    if persistent._mas_countthree == 1:
        m 6subsa "¿¡Me estás dando una palmadita en la cabeza!?"
        m 6eubsb "Es realmente{w=0.3} reconfortante."
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 1eubsb "Gracias [player]~"
    else:
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 7hubsb "Espero que no te canses de hacerlo a diario~"
    jump show_exp
    return

label date_mas:
    hide screen interaccionesbeta
    call screen dialog("Lo siento, aun está en planeación.", ok_action=Return())
    call screen interaccionesbeta
    return

label back_mas:
    hide screen interaccionesbeta
    $ mas_DropShield_core()
    jump ch30_loop
    return
    
label github_submod:
    $ renpy.run(OpenURL('https://github.com/zer0fixer/'))
    call screen interaccionesbeta
    return
    
label aff_log:
    "Tu afecto con [m_name] es de ¡[store._mas_getAffection()]!"
    call screen interaccionesbeta
    return

label monika_minigames:
    hide screen interaccionesbeta
    menu:
        "Shell Game":
            call screen dialog("Estará disponible en la versión final.", ok_action=Return())
            call screen interaccionesbeta
    return

label tools_mas:
    hide screen interaccionesbeta
    menu:
        "Ver el afecto de [m_name]":
            jump aff_log
        "Github":
            jump github_submod
        "Ayuda":
            jump help_mas
        "No importa":
            call screen interaccionesbeta
    return

label help_mas:
    menu:
        "¿Cómo puedo interactuar con [m_name]?":
            "Puede hacerlo cuando esté en las opciones de Extra+, toque la nariz, mejilla o cabeza de su Monika y ella reaccionara."
            "Algo que debe de tener presente sobre este submod."
            "No puede interactuar durante una conversación, tampoco en una opción seleccionada de este submod (Cita, Minijuego, Adiciones)."
            "Ejemplo de ello es estar en esta sección de ayuda, no funcionará si lo intenta solamente avanzara en el juego."
            "Esto se debe a que no se modificó nada del código base y este submod es totalmente independiente al mod."
            "Espero le sirva la explicación de como funciona."

        "¿Por qué esto no está en el botón de Extras de MAS?":
            "Pensando a futuro, Monika After Story suele actualizarse y eso causa que se sobreescriba los archivos."
            "Por pura lógica, no es necesario que esté actualizando este submod, cuando sale una nueva versión de MAS."
            "Además, podría dañar a su Monika por una falla de codificación, esto no está hecho por un dev, está hecho por un fan de DDLC."
            "Este submod solo trata de añadir pocas cosas o ideas para Monika After Story, por ello no se enfoca en una sola cosa."
            "Espero le sirva la explicación."

        "No importa":
            pass
    call screen interaccionesbeta
    return