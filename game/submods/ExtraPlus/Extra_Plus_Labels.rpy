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
    # $ store.boop_war_active = False
    # Call the screen and wait for it to return a value (the label to jump to)
    call screen boop_revamped
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
# Dating logic
#===========================================================================================
label extra_cafe_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_cafe, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump extra_cafe_cakes

label extra_restaurant_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_restaurant, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump extra_restaurant_cakes

label ExtraPool_init:
    python:
        HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_extrapool, skip_leadin=True, skip_outro=True)
    $ HKBShowButtons()
    jump to_pool_loop
    return

label extra_cafe_leave:
    hide screen extra_timer_monika
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    $ stop_snike_time = False
    jump cafe_hide_acs

label extra_restaurant_leave:
    hide screen extra_timer_monika
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    $ stop_snike_time = False
    jump restaurant_hide_acs

label monika_boopcafe:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_chocolatecake) or monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Hey, I'm enjoying my dessert."
        m 3hua "Do it when I finish my dessert, okay?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label monika_booprestaurant:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_waffles) or monika_chr.is_wearing_acs(extraplus_acs_icecream) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
        if mas_isMoniLove():
            m "...!"
            m "[player]!"
            extend "I'm trying to eat here!"
            m 3hua "You can boop me all you want when I'm done, okay [mas_get_player_nickname()]~?"
        else:
            m 1ttp "...?"
            m 1eka "Hey,{w=0.3} I'm trying to enjoy my food here."
            m 3hua "Do that when I'm done with it, please?"
    else:
        m 1hub "*Boop*"
    jump to_restaurant_loop
    return

#===========================================================================================
# Loops
#===========================================================================================
label to_cafe_loop:
    show monika staticpose at t11
    if stop_snike_time and renpy.get_screen("extra_timer_monika"):
        hide screen extra_timer_monika
        jump monika_no_dessert

    call screen extra_dating_loop(ask="cafe_talk", label_boop="monika_boopcafe", boop_enable=True)
    return

label to_restaurant_loop:
    show monika staticpose at t11
    if stop_snike_time and renpy.get_screen("extra_timer_monika"):
        hide screen extra_timer_monika
        jump monika_no_food

    # NOTE: Boop during dates is disabled for now.
    call screen extra_dating_loop("restaurant_talk", "monika_booprestaurant", boop_enable=False)
    return

label to_pool_loop:
    # show monika staticpose at t11
    show monika idle at t11_float

    call screen extra_dating_loop("ExtraPool_interactions", "", boop_enable=False)
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
    if EP_dessert_player == True:
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

    if EP_food_player == True:
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
            # (_("Botones"), 'extra_plus_button_tester_start'),
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

label cafe_talk:
    show monika staticpose at t21
    python:
        cafe_menu = [
            (_("How are you today?"), 'extra_talk_feel'),
            (_("What's your greatest ambition?"), 'extra_talk_ambition'),
            (_("Our communication is very limited, don't you think?"), 'extra_talk_you'),
            (_("How do you see us in 10 years?"), 'extra_talk_teen'),
            (_("What is your best memory that you currently have?"), 'extra_talk_memory'),
            (_("Do you have any phobia?"), 'extra_talk_phobia')
        ]

        items = [
            (_("Can we leave?"), 'extra_cafe_leave', 20),
            (_("Nevermind"), 'to_cafe_loop', 0)
        ]
    call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=False)
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        restaurant_menu = [
            (_("How are you doing, [m_name]?"), 'extra_talk_doing'),
            (_("If you could live anywhere, where would it be?"), 'extra_talk_live'),
            (_("What would you change about yourself if you could?"), 'extra_talk_change'),
            (_("If you were a super-hero, what powers would you have?"), 'extra_talk_superhero'),
            (_("Do you have a life motto?"), 'extra_talk_motto'),
            (_("Aside from necessities, what's the one thing you couldn't go a day without?"), 'extra_talk_without'),
            (_("Is your glass half full or half empty?"), 'extra_talk_glass'),
            (_("What annoys you most?"), 'extra_talk_annoy'),
            (_("Describe yourself in three words."), 'extra_talk_3words'),
            (_("What do you think is the first thing to pop into everyone's minds when they think about you?"), 'extra_talk_pop'),
            (_("If you were an animal, what animal would you be?"), 'extra_talk_animal'),
        ]

        items = [
            (_("Can we leave?"), 'extra_restaurant_leave', 20),
            (_("Nevermind"), 'to_restaurant_loop', 0)
        ]
    call screen extra_gen_list(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=False)
    return

label ExtraPool_interactions:
    show monika idle at t21_float

    python:
        pool_menu = [
            (_("What do you think of the water?"), 'extra_pool_talk_water'),
            (_("Do you like to swim?"), 'extra_pool_talk_swim'),
            (_("This is really relaxing."), 'extra_pool_talk_relax'),
        ]

        items = [
            (_("Can we leave?"), 'skip_pool_exit', 20),
            (_("Nevermind"), 'to_pool_loop', 0)
        ]
    call screen extra_gen_list(pool_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=False)
    return