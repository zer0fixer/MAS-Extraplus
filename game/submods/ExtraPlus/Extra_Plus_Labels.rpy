#===========================================================================================
# RETURN_LABELS
#===========================================================================================

label view_extraplus:
    python:
        store.player_zoom = store.mas_sprites.zoom_level
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
        store.mas_sprites.zoom_level = store.player_zoom
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
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen boop_revamped
    return

label return_boop_screen:
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label hide_images_rps:
    hide e_rock
    hide e_paper
    hide e_scissors
    hide e_rock_1
    hide e_paper_1
    hide e_scissors_1
    $ rps_your_choice = 0
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
# Label
#===========================================================================================

#====Cafe

label go_to_cafe:
    python:
        # check_file_status(cafe_sprite, '/game/submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("cafe_sorry_player", "gtcafev2", "check_label_cafe")

label check_label_cafe:
    pass

label gtcafe:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Do you want to go to the cafe?"
        m 3hub "Glad to hear it [player]!"
        m 1hubsa "I know this appointment will be great!"
        m 1hubsb "Okay, let's go [mas_get_player_nickname()]~"
        jump cafe_init

    elif mas_isNightNow():
        m 3sub "Oh, you want to go out to the cafe?"
        m 3hub "It's pretty sweet that you decided to go tonight."
        m 1eubsa "This date night is going to be great!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Another time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtcafev2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Do you want to go to the cafe again?"
        m 2hub "The previous time we went, I had a lot of fun!"
        m 2eubsa "So glad to hear it [player]!"
        m 1hubsb "Well, let's go [mas_get_player_nickname()]~"
        jump cafe_init
    elif mas_isNightNow():
        m 3wub "Oh, do you want to go out to the cafe again?"
        m 2hub "The previous time we went, it was very romantic~"
        m 2eubsa "So glad to go again [player]!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label cafe_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        cafe_menu = [
            (_("How are you today?"), 'extra_talk_feel'),
            (_("What's your greatest ambition?"), 'extra_talk_ambition'),
            (_("Our communication is very limited, don't you think?"), 'extra_talk_you'),
            (_("How do you see us in 10 years?"), 'extra_talk_teen'),
            (_("What is your best memory that you currently have?"), 'extra_talk_memory'),
            (_("Do you have any phobia?"), 'extra_talk_phobia')
        ]

        items = [
            (_("Can we leave?"), 'cafe_leave', 20),
            (_("Nevermind"), 'to_cafe_loop', 0)
        ]
    call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_cafe_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop("cafe_talk", "monika_boopcafebeta", boop_enable=True)
    return

label cafe_leave:
    hide screen _timer_monika
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    jump cafe_hide_acs

label comment_cafe:
    m 1hubsa "Thank you for asking me out."
    m 1eubsb "It is nice to have these moments as a couple!"
    m 1eubsa "I feel very fortunate to have met you and that you keep choosing me every day."
    m 1ekbsa "I love you, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#====Restaurant====#

label go_to_restaurant:
    python:
        # check_file_status(restaurant_sprite, '/game/submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("restaurant_sorry_player", "gtrestaurantv2", "check_label_restaurant")

label check_label_restaurant:
    pass

label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m 3hub "I'm so happy to hear that,{w=0.3} [player]!"
        m "It's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsa "I just know it'll be great!"
        m 1hubsb "Okay,{w=0.3} let's go [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m "That's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Another time then,{w=0.3} [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Oh, you want to go out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~ I'm still thinking about the time you took us there for our anniversary,"
            extend " I thought it was so romantic~"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, I had so much fun!"
            m 2eubsa "So I'm glad to hear it [player]!"
        m 1hubsb "Well, let's go then [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3wub "Oh, you want to go out out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~{w=0.3} I'm still thinking about the time you took us there for our anniversary,"
            extend "You really know how to make our night amazing!"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, it was so romantic~"
            m 2eubsa "So I'm glad to go again [player]!"
        m 1hubsb "Let's go then [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
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
            (_("Can we leave?"), 'restaurant_leave', 20),
            ("Nevermind", 'to_restaurant_loop', 0)
        ]
    call screen extra_gen_list(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_restaurant_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop("restaurant_talk", "monika_booprestaurantbeta", boop_enable=True)
    return

label restaurant_leave:
    hide screen _timer_monika
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    jump restaurant_hide_acs

#====Pool

# label go_to_pool:
#     python:
#         # check_file_status(cafe_sprite, '/game/submods/ExtraPlus/submod_assets/backgrounds')
#         mas_extra_location(locate=True)
#         extra_seen_background("pool_sorry_player", "gtpoolv2", "check_label_pool")

# label check_label_pool:
#     pass

# label gtpool:
#     show monika 1eua at t11
#     if mas_isDayNow():
#         jump cafe_init

#     elif mas_isNightNow():
#         jump cafe_init
#     else:
#         m 1eub "Another time then, [mas_get_player_nickname()]."
#         jump screen_extraplus
#     return

# label gtpoolv2:
#     show monika 1eua at t11
#     if mas_isDayNow():
#         m 3wub "Do you want to go to the cafe again?"
#         m 2hub "The previous time we went, I had a lot of fun!"
#         m 2eubsa "So glad to hear it [player]!"
#         m 1hubsb "Well, let's go [mas_get_player_nickname()]~"
#         jump cafe_init
#     elif mas_isNightNow():
#         m 3wub "Oh, do you want to go out to the cafe again?"
#         m 2hub "The previous time we went, it was very romantic~"
#         m 2eubsa "So glad to go again [player]!"
#         m 1hubsb "Let's go [mas_get_player_nickname()]~"
#         jump cafe_init
#     else:
#         m 1eub "Next time then, [mas_get_player_nickname()]."
#         jump screen_extraplus
#     return

# label pool_talk:
#     show monika staticpose at t21
#     python:
#         store.disable_zoom_button = True
#         cafe_menu = [
#             ("How are you today?", 'extra_talk_feel'),
#             ("What's your greatest ambition?", 'extra_talk_ambition'),
#             ("Our communication is very limited, don't you think?", 'extra_talk_you'),
#             ("How do you see us in 10 years?", 'extra_talk_teen'),
#             ("What is your best memory that you currently have?", 'extra_talk_memory'),
#             ("Do you have any phobia?", 'extra_talk_phobia')
#         ]

#         items = [
#             ("Can we leave?", 'cafe_leave', 20),
#             ("Nevermind", 'to_cafe_loop', 0)
#         ]
#     call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
#     return

# label to_cafe_loop:
#     show monika staticpose at t11
#     $ store.disable_zoom_button = False
#     call screen dating_loop(extraplus_acs_emptyplate, extraplus_acs_emptycup, "cafe_talk", "monika_no_dessert", "monika_boopcafebeta", boop_enable=True)
#     return

# label cafe_leave:
#     show monika 1hua at t11
#     m 1eta "Oh, you want us to go back?"
#     m 1eub "Sounds good to me!"
#     m 3hua "But before we go..."
#     jump cafe_hide_acs

# label comment_cafe:
#     m 1hubsa "Thank you for asking me out."
#     m 1eubsb "It is nice to have these moments as a couple!"
#     m 1eubsa "I feel very fortunate to have met you and that you keep choosing me every day."
#     m 1ekbsa "I love you, [mas_get_player_nickname()]!"
#     $ mas_DropShield_dlg()
#     $ mas_ILY()
#     jump ch30_visual_skip
#     return

#===========================================================================================
# Others
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
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
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eub "I have to put this fruitcake away."
            m 3eub "Also, I'll put this cup away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_fruitcake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eub "I have to put this fruitcake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)

    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eua "I must put this chocolate cake away."
            m 3eua "Also, I'll put this cup away, it won't be long now."
            python:
                monika_chr.remove_acs(extraplus_acs_chocolatecake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eua "I must put this chocolate cake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)

    elif monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3hua "I'll go put this plate away."
            m 3hua "Also, I'll put this cup away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_emptyplate)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3hua "I'm going to put this plate away, give me a moment."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg("comment_cafe")
    return

#====Restaurant====#

label monika_no_food:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        python:
            monika_chr.remove_acs(extraplus_acs_pasta)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pasta."
        m 1eub "I really enjoyed it~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_icecream)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        python:
            monika_chr.remove_acs(extraplus_acs_pancakes)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pancakes."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        python:
            monika_chr.remove_acs(extraplus_acs_waffles)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my waffles."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
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
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_icecream):
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            m 3eub "Also, I'll put this plate away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_candles)
                monika_chr.remove_acs(extraplus_acs_pasta)
                monika_chr.remove_acs(extraplus_acs_icecream)

        else:
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            $ monika_chr.remove_acs(extraplus_acs_candles)

    elif monika_chr.is_wearing_acs(extraplus_acs_flowers):
        m 3eua "I'll put these flowers away, I won't be long."
        python:
            monika_chr.remove_acs(extraplus_acs_flowers)

    elif not monika_chr.is_wearing_acs(extraplus_acs_flowers):
        if monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_pudding) or monika_chr.is_wearing_acs(extraplus_acs_waffles):
            m 3eua "I must put this plate away."
            python:
                monika_chr.remove_acs(extraplus_acs_waffles)
                monika_chr.remove_acs(extraplus_acs_pancakes)
                monika_chr.remove_acs(extraplus_acs_pudding)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg
    return


################################################################################
## MENUS
################################################################################

label plus_walk:
    show monika idle at t21
    python:
        walk_menu = [
            (_("Cafe"), 'go_to_cafe'),
            (_("Restaurant"), 'go_to_restaurant'),
            (_("Pool"), "screen_extraplus")
        ]
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("Nevermind", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_minigames:
    show monika idle at t21
    python:
        global ttt
        minigames_menu = [
            minigames("Shell Game", 'minigame_sg', None),
            minigames("Rock Paper Scissors", 'minigame_rps', None)
        ]
        ttt = minigames("Tic Tac Toe", 'minigame_ttt', ttt_prep)
        minigames_menu.append(ttt)
        
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("Nevermind", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_tools:
    show monika idle at t21
    python:
        tools_menu = [
            (_("View [m_name]'s Affection"), 'aff_log'),
            (_("Create a gift for [m_name]"), 'plus_make_gift'),
            (_("Change the window's title"), 'extra_window_title'),
            (_("[m_name], I want to make a backup"), 'mas_backup'),
            (_("[m_name], can you flip a coin?"), 'coinflip'),
            (_("Hi [player]!"), 'extra_dev_mode')
            
        ]
        store.disable_zoom_button = True
        items = [
            (_("Github Repository"), 'github_submod', 20),
            ("Nevermind", 'screen_extraplus', 0)
        ]
    call screen extra_gen_list(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

################################################################################
## GIFTS
################################################################################

label plus_make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            (_("Customized gift"), 'plus_make_file'),
            (_("Groceries"), 'plus_groceries'),
            (_("Objects"), 'plus_objects'),
            (_("Ribbons"), 'plus_ribbons')
        ]

        items = [
            ("Nevermind", 'plus_tools', 20)
        ]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_make_file:
    show monika idle at t11

    python:
        import os
        makegift = mas_input(
            prompt=(_("Enter the name of the gift.")),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"},
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancel":
            renpy.jump("plus_make_gift")
        else:
            if os.name == 'nt':
            # 如果是 PC 系统（Windows、Linux 或 macOS），使用 renpy.config.basedir
              filepath = os.path.join(renpy.config.basedir, 'characters', makegift + ".gift")
            else:
            # 如果是其他系统（例如 Android），使用指定路径
              filepath = os.path.join("/storage/emulated/0/MAS/characters/", makegift + ".gift")
            #filepath = os.path.join(renpy.config.basedir, 'characters', makegift + ".gift")
            with open(filepath, "a"):
                pass  # just create an empty file
            renpy.notify(_("Has been successfully created."))
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

        items = [
            ("Nevermind", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
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

        items = [
            ("Nevermind", 'plus_make_gift', 20)
        ]
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

        items = [
            ("Nevermind", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return