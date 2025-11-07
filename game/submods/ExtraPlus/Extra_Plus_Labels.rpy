#===========================================================================================
# RETURN LABELS
#===========================================================================================
label screen_extraplus:
    show monika idle at t11
    $ Extraplus_show()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label close_dev_extraplus:
    show monika idle at t11
    python:
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose
    $ store.boop_war_active = False
    # Call the screen and wait for it to return a value (the label to jump to)
    call screen boop_revamped
    # _return will contain the label name from the interactable
    $ result = _return
    if result:
        jump expression result
    else:
        jump close_boop_screen
    return

label return_boop_screen:
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    $ disable_button_zoom()
    jump ch30_visual_skip
    return

label boop_timer_expired:
    call screen maxwell_april_fools
    jump show_boop_screen
    return

label hide_images_rps:
    hide extra_rock
    hide extra_paper
    hide extra_scissors
    hide extra_rock_1
    hide extra_paper_1
    hide extra_scissors_1
    call screen RPS_mg
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
# Others
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
    hide screen extra_timer_monika
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        python:
            monika_chr.remove_acs(extraplus_acs_fruitcake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my fruitcake."
        m 1eub "I really enjoyed it~"
    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        python:
            monika_chr.remove_acs(extraplus_acs_chocolatecake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my chocolate cake."
        m 1sua "It tasted so sweet~"
    if monika_chr.is_wearing_acs(extraplus_acs_coffeecup):
        python:
            monika_chr.remove_acs(extraplus_acs_coffeecup)
            monika_chr.wear_acs(extraplus_acs_emptycup)
        m 3dub "Also, this coffee was also good."
    if dessert_player == True:
        m 1etb "By the way, have you finished your dessert yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your dessert yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a cup of coffee."
    m 1hua "Let me know if you want to come back again."
    jump to_cafe_loop
    return

label cafe_hide_acs:
    python:
        # Check for food and cup items to give a combined message
        food_items = [extraplus_acs_fruitcake, extraplus_acs_chocolatecake, extraplus_acs_emptyplate]
        cup_items = [extraplus_acs_coffeecup, extraplus_acs_emptycup]

        food_worn = any(monika_chr.is_wearing_acs(acs) for acs in food_items)
        cup_worn = any(monika_chr.is_wearing_acs(acs) for acs in cup_items)

    if food_worn and cup_worn:
        m 3eub "I have to put this plate and cup away. I won't be long."
    elif food_worn:
        m 3eub "I have to put this plate away. I'll be right back."
    elif cup_worn:
        m 1eua "I'll just put this cup away, give me a moment."

    call mas_transition_to_emptydesk
    pause 2.0

    python:
        # Remove all location-specific accessories
        acs_to_remove = [
            extraplus_acs_fruitcake, extraplus_acs_chocolatecake, extraplus_acs_emptyplate,
            extraplus_acs_coffeecup, extraplus_acs_emptycup
        ]
        for acs in acs_to_remove:
            monika_chr.remove_acs(acs)

    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg("extra_comment_cafe")
    return

#====Restaurant====#

label monika_no_food:
    hide screen extra_timer_monika
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        python:
            monika_chr.remove_acs(extraplus_acs_pasta)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pasta."
        m 1eub "I really enjoyed it~"

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        python:
            monika_chr.remove_acs(extraplus_acs_pancakes)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pancakes."
        m 1sua "They were delicious~"

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        python:
            monika_chr.remove_acs(extraplus_acs_waffles)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my waffles."
        m 1sua "They were delicious~"

    m 1eua "That was delicious! Now, how about some dessert? Be right back!"
    $ monika_chr.remove_acs(extraplus_acs_remptyplate)
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if renpy.random.randint(1,2) == 1:
            monika_chr.wear_acs(extraplus_acs_icecream)
        else:
            monika_chr.wear_acs(extraplus_acs_pudding)
    call mas_transition_from_emptydesk("monika 1eua")

    if food_player == True:
        m 1etb "By the way, have you finished your food yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your food yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a drink with you."
    m 1hua "Let me know if you want to come back again."
    jump to_restaurant_loop
    return

label restaurant_hide_acs:
    # Check and remove candles if it's night
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        m 1eka "I have to put these candles away. We can never be too careful with fire!"

    # Check and remove flowers if it's day
    if monika_chr.is_wearing_acs(extraplus_acs_flowers):
        m 1eua "I'll put these flowers away, I won't be long."

    python:
        # Check and remove any food plate
        food_acs_to_check = [
            extraplus_acs_pasta, extraplus_acs_pancakes, extraplus_acs_waffles,
            extraplus_acs_icecream, extraplus_acs_pudding
        ]
    if any(monika_chr.is_wearing_acs(acs) for acs in food_acs_to_check):
        m 3eub "I must put this plate away, it won't be long now."

    call mas_transition_to_emptydesk
    pause 2.0

    python:
        # Remove all location-specific accessories
        acs_to_remove = [
            extraplus_acs_candles, extraplus_acs_flowers, extraplus_acs_pasta,
            extraplus_acs_pancakes, extraplus_acs_waffles, extraplus_acs_icecream,
            extraplus_acs_pudding, extraplus_acs_remptyplate
        ]
        for acs in acs_to_remove:
            monika_chr.remove_acs(acs)

    call mas_transition_from_emptydesk("monika 1eua")
    
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg("extra_comment_restaurant")
    return

################################################################################
## MENUS
################################################################################

label extraplus_walk:
    show monika idle at t21
    python:
        walk_menu = [
            (_("Cafe"), 'go_to_cafe'),
            (_("Restaurant"), 'go_to_restaurant'),
            (_("Pool"), "go_to_pool"),
            (_("Library"), "generic_date_dev"),
            (_("Arcade"), "generic_date_dev")
        ]
        m_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), 'screen_extraplus', 20)]
    call screen extra_gen_list(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extraplus_minigames:
    show monika idle at t21
    python:
        minigames_menu = [
            (_("Shell Game"), 'minigame_sg'),
            (_("Rock Paper Scissors"), 'minigame_rps'),
            (_("Tic Tac Toe"), 'minigame_ttt'),
            (_("Blackjack (21)"), 'blackjack_start')
        ]
        
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), 'screen_extraplus', 20)]
    
    call screen extra_gen_list(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extraplus_tools:
    show monika idle at t21
    python:
        store.extra_plus_player_zoom = store.mas_sprites.zoom_level
        tools_menu = [
            # (_("PROBAR NOMBRES DE BOTÓN"), 'extra_plus_button_tester_start'),
            (_("View [m_name]'s Affection"), 'extra_aff_log'),
            (_("Your MAS Journey"), 'extra_show_stats'),
            (_("Create a gift for [m_name]"), 'plus_make_gift'),
            (_("Change the window's title"), 'extra_window_title'),
            (_("Hi [player]!"), 'extra_dev_mode'),
            (_("How long have we been together, [m_name]?"), 'extra_relation_monika'),
            (_("[m_name], I want to make a backup"), 'extra_mas_backup'),
            (_("[m_name], can you flip a coin?"), 'extra_coinflip')
        ]
        items = [
            (_("Github Repository"), 'github_submod', 20),
            (_("Nevermind"), 'screen_extraplus', 0)
        ]
    call screen extra_gen_list(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=True)
    return

################################################################################
## GIFTS
################################################################################

label plus_make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            (_("Create a .gift file"), 'plus_make_file'),
            (_("Groceries"), 'plus_groceries'),
            (_("Objects"), 'plus_objects'),
            (_("Ribbons"), 'plus_ribbons')
        ]

        items = [(_("Nevermind"), 'extraplus_tools', 20)]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_make_file:
    show monika idle at t11

    python:
        makegift = mas_input(
            prompt=_("Enter the name of the gift."),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"},
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancel":
            renpy.jump("plus_make_gift")
        else:
            create_gift_file(makegift + ".gift")
            renpy.notify(_("Done! Created '/characters/{}.gift'").format(makegift))
            store.mas_checkReactions()
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    show monika idle at t21
    python:
        groceries_menu = [
            extra_gift(_("Coffee"), 'coffee.gift'),
            extra_gift(_("Chocolates"), 'chocolates.gift'),
            extra_gift(_("Cupcake"), 'cupcake.gift'),
            extra_gift(_("Fudge"), 'fudge.gift'),
            extra_gift(_("Hot Chocolate"), 'hotchocolate.gift'),
            extra_gift(_("Candy"), 'candy.gift'),
            extra_gift(_("Candy Canes"), 'candycane.gift'),
            extra_gift(_("Candy Corn"), 'candycorn.gift'),
            extra_gift(_("Christmas Cookies"), 'christmascookies.gift')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=True)
    return

label plus_objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift(_("Promise Ring"), 'promisering.gift'),
            extra_gift(_("Roses"), 'roses.gift'),
            extra_gift(_("Quetzal Plushie"), 'quetzalplushie.gift'),
            extra_gift(_("Thermos Mug"), 'justmonikathermos.gift')
        ]
        if not mas_seenEvent("mas_reaction_gift_noudeck"):
            objects_menu.append(extra_gift(_("NOU"), 'noudeck.gift'))

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
            
label plus_ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [
            extra_gift(_("Black Ribbon"), 'blackribbon.gift'),
            extra_gift(_("Blue Ribbon"), 'blueribbon.gift'),
            extra_gift(_("Dark Purple Ribbon"), 'darkpurpleribbon.gift'),
            extra_gift(_("Emerald Ribbon"), 'emeraldribbon.gift'),
            extra_gift(_("Gray Ribbon"), 'grayribbon.gift'),
            extra_gift(_("Green Ribbon"), 'greenribbon.gift'),
            extra_gift(_("Light Purple Ribbon"), 'lightpurpleribbon.gift'),
            extra_gift(_("Peach Ribbon"), 'peachribbon.gift'),
            extra_gift(_("Pink Ribbon"), 'pinkribbon.gift'),
            extra_gift(_("Platinum Ribbon"), 'platinumribbon.gift'),
            extra_gift(_("Red Ribbon"), 'redribbon.gift'),
            extra_gift(_("Ruby Ribbon"), 'rubyribbon.gift'),
            extra_gift(_("Sapphire Ribbon"), 'sapphireribbon.gift'),
            extra_gift(_("Silver Ribbon"), 'silverribbon.gift'),
            extra_gift(_("Teal Ribbon"), 'tealribbon.gift'),
            extra_gift(_("Yellow Ribbon"), 'yellowribbon.gift')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return