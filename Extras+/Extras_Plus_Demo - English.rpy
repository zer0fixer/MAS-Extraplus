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

    Zer0fixer = "What are you doing here?"
    Zer0fixer = "I hope you find some of my little work useful."
    Zer0fixer = "This is a demo version, that is why it is so shortened."
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

        textbutton _("Close") action Jump("back_mas")

        textbutton _("Date") action Jump("date_mas")

        textbutton _("Minigame") action Jump("monika_minigames")

        textbutton _("Additions") action Jump("tools_mas")

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
        m 1tsb "What are you doing playing with my nose, Beta tester?{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        hide screen tear
        m 1hub "What are you doing playing with my nose, [player]?{fast}"
        m 1hksdrb "Not that it bothers, it just took me by surprise!"
        m 1hua "Hehe~"
    else:
        m 1hub "*Boop*"
    jump show_exp
    return

label monika_cheeksbeta:
    $ persistent._mas_counttwo += 1
    hide screen interaccionesbeta
    if persistent._mas_counttwo == 1:
        m 2wubsd "Hey, I felt a pinch on my cheek."
        m 2lksdrb "Oh, it was just your cursor. You took me by surprise."
        m 2ttb "But I must ask, what are you [player] up to?"
        m 1hubla "Did you want to see how I would react to that?"
    else:
        m 2fua "Jeje~"
        m 2hua "It would be nice if you could use your hand instead of the cursor, but that's a long way off."
    jump show_exp
    return

label monika_headpatbeta:
    $ persistent._mas_countthree += 1
    hide screen interaccionesbeta
    if persistent._mas_countthree == 1:
        m 6subsa "You're patting me on the head?!"
        m 6eubsb "It is really{w=0.3} comforting."
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 1eubsb "Thank you [player]~"
    else:
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 7hubsb "I hope you don't get tired of doing it every day.~"
    jump show_exp
    return

label date_mas:
    hide screen interaccionesbeta
    call screen dialog("Sorry, it's still in planning.", ok_action=Return())
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
    "Your affection with [m_name] is [store._mas_getAffection()]!"
    call screen interaccionesbeta
    return

label monika_minigames:
    hide screen interaccionesbeta
    menu:
        "Shell Game":
            call screen dialog("It will be available in the final version.", ok_action=Return())
            call screen interaccionesbeta
    return

label tools_mas:
    hide screen interaccionesbeta
    menu:
        "View [m_name]'s Affection":
            jump aff_log
        "Github Repository":
            jump github_submod
        "Help":
            jump help_mas
        "Nevermind":
            call screen interaccionesbeta
    return

label help_mas:
    menu:
        "How can I interact with [m_name]?":
            "You can do this when you are in the Extra+ options, touch your Monika's nose, cheek or head and she will react."
            "Something to keep in mind about this submod."
            "You cannot interact during a conversation, neither in a selected option of this submod (Date, Minigame, Additions)."
            "An example of this is being in this help section, it will not work if you try it will only advance in the game."
            "This is because nothing has been modified in the code base and this submod is totally independent of the mod."
            "I hope you find the explanation of how it works useful."

        "Why is this not on the MAS Extra button?":
            "Thinking ahead, Monika After Story is often updated and this causes files to be overwritten."
            "By pure logic, it is not necessary to be updating this submod, when a new version of MAS is released."
            "Also, you could damage your Monika by a coding glitch, this is not made by a dev, this is made by a DDLC fan."
            "This submod only tries to add few things or ideas for Monika After Story, so it does not focus on one thing."
            "I hope this explanation is helpful."

        "Nevermind":
            pass
    call screen interaccionesbeta
    return