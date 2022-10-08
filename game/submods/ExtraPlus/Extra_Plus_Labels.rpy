#===========================================================================================
# RETURN_LABELS
#===========================================================================================

label view_extraplus:
    python:
        player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        extra_button_zoom()
        Extraplus_show()
    return

label screen_extraplus:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        Extraplus_show()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        store.mas_sprites.zoom_level = player_zoom
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    # call monika_zoom_transition_reset(1.5)
    call screen boop_revamped
    return

label return_boop_screen:
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label hide_images_psr:
    hide e_rock
    hide e_paper
    hide e_scissors
    hide e_rock_1
    hide e_paper_1
    hide e_scissors_1
    $ your_choice = 0
    call screen PSR_mg
    return

label extra_restore_bg(label="ch30_visual_skip"):
    python:
        mas_extra_location(locate=False)
        disable_button_zoom()
        HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        HKBShowButtons()
        renpy.jump(label)
    return

#===========================================================================================
# LABELS
#===========================================================================================

label extra_change_title:
    show monika idle at t11
    python:
        player_input = mas_input(_("What title do you want to put on this window?"),
                            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.0123456789",
                            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"})
        if not player_input:
            renpy.jump("extra_change_title")
        else:
            if player_input == "cancel":
                renpy.jump("extra_window_title")
            else:
                persistent.save_window_title = player_input
                config.window_title = persistent.save_window_title 
                renpy.notify("The change is done.")
                renpy.jump("close_extraplus")
    return

label extra_restore_title:
    show monika idle at t11
    python:
        persistent.save_window_title = backup_window_title
        config.window_title = persistent.save_window_title 
        renpy.notify("It has been successfully restored.")
        renpy.jump("close_extraplus")
    return

label check_cheat_minigame:
    m 3hksdrb "I think you forgot something, [player]!"
    m 3eksdra "You must restore the variables you have modified."
    m 1hua "We will not play until they are at 0."
    jump screen_extraplus
    return

################################################################################
## MENUS
################################################################################

label walk_extra:
    show monika idle at t21
    python:
        store.disable_zoom_button = True
        monika_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, monika_talk, interact=False)
    call screen list_scrolling(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

label minigames_extra:
    show monika idle at t21
    python:
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
    call screen list_generator(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

label tools_extra:
    show monika idle at t21
    $ store.disable_zoom_button = True
    call screen list_scrolling(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

################################################################################
## GIFTS
################################################################################

label make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            ("Customized gift", 'make_file'),
            ("Groceries", 'groceries'),
            ("Objects", 'objects'),
            ("Ribbons", 'ribbons')
        ]
    call screen list_scrolling(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"tools_extra",close=True) nopredict
    return

label make_file:
    show monika idle at t11
    python:
        import os
        makegift = mas_input(_("Enter the name of the gift."),
                            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
                            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"})
        if not makegift:
            renpy.jump("make_file")
        else:
            if makegift == "cancel":
                renpy.jump("make_gift")
            else:
                filepath = os.path.join(renpy.config.basedir + '/characters', makegift + '.gift')
                f = open(filepath,"a")
                renpy.notify("Has been successfully created.")
                renpy.jump("make_gift")
    return

label groceries:
    show monika idle at t21
    python:
        groceries_menu = [
            extra_gift("Coffee", 'coffee.gift', gift_append),
            extra_gift("Chocolates", 'chocolates.gift', gift_append),
            extra_gift("Cupcake", 'cupcake.gift', gift_append),
            extra_gift("Fudge", 'fudge.gift', gift_append),
            extra_gift("Hot Chocolate", 'hotchocolate.gift', gift_append),
            extra_gift("Candy", 'candy.gift', gift_append),
            extra_gift("Candy Canes", 'candycane.gift', gift_append),
            extra_gift("Candy Corn", 'candycorn.gift', gift_append),
            extra_gift("Christmas Cookies", 'christmascookies.gift', gift_append)
        ]
        
    call screen list_generator(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return

label objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift("Promise Ring", 'promisering.gift', gift_append),
            extra_gift("Roses", 'roses.gift', gift_append),
            extra_gift("Quetzal Plushie", 'quetzalplushie.gift', gift_append),
            extra_gift("Thermos Mug", 'justmonikathermos.gift', gift_append),
        ]

    call screen list_generator(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return
            
label ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [
            extra_gift("Black Ribbon", 'blackribbon.gift', gift_append),
            extra_gift("Blue Ribbon", 'blueribbon.gift', gift_append),
            extra_gift("Dark Purple Ribbon", 'darkpurpleribbon.gift', gift_append),
            extra_gift("Emerald Ribbon", 'emeraldribbon.gift', gift_append),
            extra_gift("Gray Ribbon", 'grayribbon.gift', gift_append),
            extra_gift("Green Ribbon", 'greenribbon.gift', gift_append),
            extra_gift("Light Purple Ribbon", 'lightpurpleribbon.gift', gift_append),
            extra_gift("Peach Ribbon", 'peachribbon.gift', gift_append),
            extra_gift("Pink Ribbon", 'pinkribbon.gift', gift_append),
            extra_gift("Platinum Ribbon", 'platinumribbon.gift', gift_append),
            extra_gift("Red Ribbon", 'redribbon.gift', gift_append),
            extra_gift("Ruby Ribbon", 'rubyribbon.gift', gift_append),
            extra_gift("Sapphire Ribbon", 'sapphireribbon.gift', gift_append),
            extra_gift("Silver Ribbon", 'silverribbon.gift', gift_append),
            extra_gift("Teal Ribbon", 'tealribbon.gift', gift_append),
            extra_gift("Yellow Ribbon", 'yellowribbon.gift', gift_append)
        ]
        
    call screen list_generator(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return