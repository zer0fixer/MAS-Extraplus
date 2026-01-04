#===========================================================================================
# RETURN LABELS
#===========================================================================================
label screen_extraplus:
    show monika idle at t11
    $ store.ep_button.show_menu()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        store.mas_DropShield_dlg()
        store.ep_button.hide_zoom_button()

        # Trigger gift file detection when closing the ExtraPlus menu.
        # This is safe to call: MAS already runs it at startup (ch30_post_exp_check)
        # and every minute (ch30_minute). The function has built-in protection via
        # persistent._mas_filereacts_just_reacted to prevent duplicate reactions.
        mas_checkReactions()

    jump ch30_visual_skip
    return

label close_dev_extraplus:
    show monika idle at t11
    python:
        store.mas_DropShield_dlg()
        store.ep_button.hide_zoom_button()
    jump ch30_visual_skip
    return

label show_boop_screen:
    # DEBUG: Uncomment to show visual zones overlay
    # show screen ep_debug_zones
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    call screen boop_revamped
    return

label return_boop_screen:
    # hide screen ep_debug_zones
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    # hide screen ep_debug_zones
    python:
        store.ep_button.hide_zoom_button()
    jump ch30_visual_skip
    return

label boop_timer_expired:
    call screen maxwell_april_fools
    $ store.ep_button.show_menu()
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
    window hide
    hide monika
    python:
        store.ep_tools.manage_date_location(False)
        store.ep_button.hide_zoom_button()
        HKBHideButtons()
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        HKBShowButtons()
        renpy.jump(label)
    return

# Consolidated initializer for locations that only differ by background and jump target.
label extra_location_init(bg, target_label, show_monika=True):
    $ store.HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(bg, skip_leadin=True, skip_outro=True)
    if show_monika:
        show monika 1eua at t11
    $ store.HKBShowButtons()
    jump expression target_label
    return

#===========================================================================================
# Dating logic
#===========================================================================================
label extra_cafe_init:
    call extra_location_init(EP_background_cafe, "extra_cafe_cakes", True)
    return

label extra_restaurant_init:
    call extra_location_init(EP_background_restaurant, "extra_restaurant_cakes", True)
    return

label extra_pool_init:
    call extra_location_init(EP_background_pool, "to_pool_loop", False)
    return

label extra_library_init:
    call extra_location_init(EP_background_library, "extra_library_arrival", True)
    return

label extra_cafe_leave:
    hide screen extra_timer_monika
    show monika 1eta at t11
    m 1eta "Oh?{w=0.3} Are we finishing our coffee break already?"
    m 1rksdla "I was just getting comfortable with the smell of roasted beans..."
    m 1eka "It feels so cozy to just sit here and watch the world go by with you."
    m 1hua "But I'm happy to go wherever you are."
    m 1eua "Let's head back to our own private space~"
    $ ep_dates.stop_snike_time = False
    jump cafe_hide_acs
    return

label extra_restaurant_leave:
    hide screen extra_timer_monika
    show monika 1eta at t11
    m 1eta "Oh?{w=0.3} Are we ready to end our dinner date?"
    m 1hub "I agree that the dinner was lovely, but..."
    m 1eua "The best part was definitely your company."
    m 1eka "A romantic evening like this is exactly what I needed."
    m 1hua "Let's go home, [player]. I'm all yours."
    $ ep_dates.stop_snike_time = False
    jump restaurant_hide_acs
    return

label extra_library_exit:
    show monika idle at t11
    m 1eta "Oh?{w=0.3} Are we heading out already?"
    m 2rua "I was just getting lost in the atmosphere of this place..."
    m 2eka "Time really flies when we are surrounded by so many stories, doesn't it?"
    m 1hua "But I'm happy to go wherever you want to go."
    m 1eua "Let's close this chapter for today and go back home."
    call extra_restore_bg("extra_comment_library")
    return

label monika_boopcafe:
    show monika staticpose at t11
    $ store.ep_tools.show_boop_feedback("Boop!")
    if monika_chr.is_wearing_acs(EP_acs_chocolatecake) or monika_chr.is_wearing_acs(EP_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Hey, I'm enjoying my dessert."
        m 3hua "Do it when I finish my dessert, okay?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label monika_booprestaurant:
    show monika staticpose at t11
    $ store.ep_tools.show_boop_feedback("Boop!")
    if monika_chr.is_wearing_acs(EP_acs_pasta) or monika_chr.is_wearing_acs(EP_acs_pancakes) or monika_chr.is_wearing_acs(EP_acs_waffles) or monika_chr.is_wearing_acs(EP_acs_icecream) or monika_chr.is_wearing_acs(EP_acs_pudding):
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
    show monika staticpose at t11 zorder MAS_MONIKA_Z

    call screen extra_dating_loop("cafe_talk", "monika_boopcafe", boop_enable=True)
    return

label to_restaurant_loop:
    show monika staticpose at t11 zorder MAS_MONIKA_Z

    call screen extra_dating_loop("restaurant_talk", "monika_booprestaurant", boop_enable=True)
    return

label to_pool_loop:
    show monika idle at t11_float
    call screen extra_dating_loop("extra_pool_interactions", "", boop_enable=False)
    return

label to_library_loop:
    show monika idle at t11
    call screen extra_dating_loop("extra_library_interactions", "", boop_enable=False)
    return

#===========================================================================================
# Others
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
    hide screen extra_timer_monika
    $ ep_dates.stop_snike_time = False
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(EP_acs_fruitcake):
        python:
            monika_chr.remove_acs(EP_acs_fruitcake)
            monika_chr.wear_acs(EP_acs_emptyplate)
        m 1hua "Wow, I finished my fruitcake."
        m 1eub "I really enjoyed it~"
    elif monika_chr.is_wearing_acs(EP_acs_chocolatecake):
        python:
            monika_chr.remove_acs(EP_acs_chocolatecake)
            monika_chr.wear_acs(EP_acs_emptyplate)
        m 1hua "Wow, I finished my chocolate cake."
        m 1sua "It was so sweet~"
    if monika_chr.is_wearing_acs(EP_acs_coffeecup):
        python:
            monika_chr.remove_acs(EP_acs_coffeecup)
            monika_chr.wear_acs(EP_acs_emptycup)
        m 3dub "The coffee was really good, too."
    
    if ep_dates.dessert_player == True:
        m 1etb "By the way, have you finished your dessert yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your dessert yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, take your time."
                m 1eubsb "I'll wait for you patiently~"
    else:
        m 1ekc "You told me not to worry about you having a treat..."
        m 1ekb "But I hope you at least have a cup of coffee with you."
        m 1hua "Let me know if you want to come back again."
    jump to_cafe_loop
    return

label cafe_hide_acs:
    python:
        # Check for food and cup items to give a combined message
        food_items = [EP_acs_fruitcake, EP_acs_chocolatecake, EP_acs_emptyplate]
        cup_items = [EP_acs_coffeecup, EP_acs_emptycup]

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
            EP_acs_fruitcake, EP_acs_chocolatecake, EP_acs_emptyplate,
            EP_acs_coffeecup, EP_acs_emptycup
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
    $ ep_dates.stop_snike_time = False
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(EP_acs_pasta):
        python:
            monika_chr.remove_acs(EP_acs_pasta)
            monika_chr.wear_acs(EP_acs_remptyplate)
        m 1hua "Wow, I finished my pasta."
        m 1eub "I really enjoyed it~"

    elif monika_chr.is_wearing_acs(EP_acs_pancakes):
        python:
            monika_chr.remove_acs(EP_acs_pancakes)
            monika_chr.wear_acs(EP_acs_remptyplate)
        m 1hua "Wow, I finished my pancakes."
        m 1sua "They were delicious~"

    elif monika_chr.is_wearing_acs(EP_acs_waffles):
        python:
            monika_chr.remove_acs(EP_acs_waffles)
            monika_chr.wear_acs(EP_acs_remptyplate)
        m 1hua "Wow, I finished my waffles."
        m 1sua "They were delicious~"

    m 1eua "That was delicious! Now, how about some dessert? Be right back!"
    $ monika_chr.remove_acs(EP_acs_remptyplate)
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if renpy.random.randint(1,2) == 1:
            monika_chr.wear_acs(EP_acs_icecream)
        else:
            monika_chr.wear_acs(EP_acs_pudding)
    call mas_transition_from_emptydesk("monika 1eua")

    if ep_dates.food_player == True:
        m 1etb "By the way, have you finished your food yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your food yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I'll wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a drink with you."
    m 1hua "Let me know if you want to come back again."
    jump to_restaurant_loop
    return

label restaurant_hide_acs:
    # Check and remove candles if it's night
    if monika_chr.is_wearing_acs(EP_acs_candles):
        m 1eka "I have to put these candles away. We can never be too careful with fire!"

    # Check and remove flowers if it's day
    if monika_chr.is_wearing_acs(EP_acs_flowers):
        m 1eua "I'll put these flowers away, I won't be long."

    python:
        # Check and remove any food plate
        food_acs_to_check = [
            EP_acs_pasta, EP_acs_pancakes, EP_acs_waffles,
            EP_acs_icecream, EP_acs_pudding
        ]
    if any(monika_chr.is_wearing_acs(acs) for acs in food_acs_to_check):
        m 3eub "I must put this plate away, it won't be long now."

    call mas_transition_to_emptydesk
    pause 2.0

    python:
        # Remove all location-specific accessories
        acs_to_remove = [
            EP_acs_candles, EP_acs_flowers, EP_acs_pasta,
            EP_acs_pancakes, EP_acs_waffles, EP_acs_icecream,
            EP_acs_pudding, EP_acs_remptyplate
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
        ep_tools.walk_menu = [
            (_("Cafe"), "go_to_cafe"),
            (_("Restaurant"), "go_to_restaurant"),
            (_("Library"), "go_to_library"),
            (_("Pool (Soon)"), "generic_date_dev"),
            (_("Arcade (Soon)"), "generic_date_dev")
        ]

        m_talk = renpy.substitute(renpy.random.choice(ep_dialogues._dates))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), "screen_extraplus", 20)]
    call screen extra_gen_list(ep_tools.walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label extraplus_minigames:
    show monika idle at t21
    python:
        ep_tools.minigames_menu = [
            (_("Shell Game"), "minigame_sg"),
            (_("Rock Paper Scissors"), "minigame_rps"),
            (_("Tic Tac Toe"), "minigame_ttt"),
            (_("Blackjack (21)"), "blackjack_start")
        ]
        
        m_talk = renpy.substitute(renpy.random.choice(ep_dialogues._minigames))
        renpy.say(m, m_talk, interact=False)
        items = [
            (_("Game Rules"), "ep_game_rules_menu", 20),
            (_("Nevermind"), "screen_extraplus", 0)
        ]
    
    call screen extra_gen_list(ep_tools.minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label ep_game_rules_menu:
    show monika idle at t21
    python:
        ep_tools.rules_menu = [
            (_("About Blackjack (21)"), "ep_rules_blackjack"),
            (_("About Tic Tac Toe"), "ep_rules_ttt"),
            (_("About Rock Paper Scissors"), "ep_rules_rps"),
            (_("About Shell Game"), "ep_rules_shell")
        ]
        
        rules_intro = [
            _("Want to learn the rules before we play?"),
            _("Which game would you like me to explain?"),
            _("Pick a game and I'll walk you through it!")
        ]
        m_talk = renpy.substitute(renpy.random.choice(rules_intro))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), "extraplus_minigames", 20)]
    
    call screen extra_gen_list(ep_tools.rules_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label extraplus_tools:
    show monika idle at t21
    python:
        store.ep_tools.player_zoom = store.mas_sprites.zoom_level
        current_aff = store.ep_affection.getCurrentAffection()
        
        # Base menu items (always available)
        ep_tools.tools_menu = [
            (_("View [m_name]'s Affection"), "extra_aff_log"),
            (_("Your MAS Journey"), "extra_show_stats"),
            (_("Their story together"), "extra_show_timeline"),
            (_("Create a gift for [m_name]"), "plus_make_gift")
        ]
        
        # Add items that require affection >= 30
        if current_aff >= 30:
            ep_tools.tools_menu.append((_("Change the window's title"), "extra_window_title"))
            ep_tools.tools_menu.append((_("Hi, [player]!"), "extra_chibi_main"))

        # Build bottom items
        items = []
        if current_aff >= 30:
            items.append((_("Misc"), "extra_misc_tools", 20))
            items.append((_("Nevermind"), "screen_extraplus", 0))
        else:
            items.append((_("Nevermind"), "screen_extraplus", 20))

    call screen extra_gen_list(ep_tools.tools_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items)
    return

label cafe_talk:
    show monika staticpose at t21
    python:
        cafe_menu = [
            (_("How are you today?"), "extra_talk_feel"),
            (_("What's your greatest ambition?"), "extra_talk_ambition"),
            (_("Our communication is very limited, don't you think?"), "extra_talk_you"),
            (_("How do you see us in 10 years?"), "extra_talk_teen"),
            (_("What is your best memory that you currently have?"), "extra_talk_memory"),
            (_("Do you have any phobia?"), "extra_talk_phobia"),
            (_("Let's people-watch"), "extra_talk_people_watching"),
            (_("A quiet moment"), "extra_talk_silence"),
            (_("Holding your hand..."), "extra_talk_hand_holding"),
            (_("Something sweet..."), "extra_talk_sweet_tooth")
        ]

        items = [
            (_("I'm ready to head back to our room."), "extra_cafe_leave", 20),
            (_("Nevermind"), "to_cafe_loop", 0)
        ]
    call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, False)
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        restaurant_menu = [
            (_("How are you doing, [m_name]?"), "extra_talk_doing"),
            (_("If you could live anywhere, where would it be?"), "extra_talk_live"),
            (_("What would you change about yourself if you could?"), "extra_talk_change"),
            (_("If you were a super-hero, what powers would you have?"), "extra_talk_superhero"),
            (_("Do you have a life motto?"), "extra_talk_motto"),
            (_("Aside from necessities, what's the one thing you couldn't go a day without?"), "extra_talk_without"),
            (_("Is your glass half full or half empty?"), "extra_talk_glass"),
            (_("What annoys you most?"), "extra_talk_annoy"),
            (_("Describe yourself in three words."), "extra_talk_3words"),
            (_("What do you think is the first thing to pop into everyone's minds when they think about you?"), "extra_talk_pop"),
            (_("If you were an animal, what animal would you be?"), "extra_talk_animal"),
        ]

        items = [
            (_("Dinner was lovely. Shall we go?"), "extra_restaurant_leave", 20),
            (_("Nevermind"), "to_restaurant_loop", 0)
        ]
    call screen extra_gen_list(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, False)
    return

label extra_pool_interactions:
    show monika idle at t21_float 

    python:
        pool_menu = [
            (_("What do you think of the water?"), "extra_pool_talk_water"),
            (_("Do you like to swim?"), "extra_pool_talk_swim"),
            (_("This is really relaxing."), "extra_pool_talk_relax"),
        ]

        items = [
            (_("Can we leave?"), "skip_pool_exit", 20),
            (_("Nevermind"), "to_pool_loop", 0)
        ]
    call screen extra_gen_list(pool_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, False)
    return

label extra_library_interactions:
    show monika idle at t21

    python:
        library_menu = [
            (_("I want to write a poem"), "minigame_poem"),
            (_("I want to write something for you"), "minigame_poem_free"),
            (renpy.substitute(_("Read something to me, [m_name].")), "library_reading_session"),
            (_("Let's just enjoy the silence."), "library_quiet_time"),
            (_("Just talk to me."), "library_talk_topic"),
            (_("My poem collection"), "library_poem_history"),
        ]

        items = [
            (_("Let's close the book on this date for now."), "extra_library_exit", 20),
            (_("Nevermind"), "to_library_loop", 0)
        ]
    call screen extra_gen_list(library_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, False)
    return

################################################################################
## BOOP
################################################################################
#====Boop count
default persistent.plus_boop = [0, 0, 0] #Nose, Cheeks, Headpat.
default persistent.extra_boop = [0, 0, 0] #Hands, Ears, Shoulders.

#====NOISE
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
    $ store.ep_tools.show_boop_feedback("Boop!")
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Only trigger after initial interactions (count > 5)
    if persistent.plus_boop[0] > 5:
        # Christmas context
        if mas_isD25():
            $ nose_xmas = renpy.random.randint(1, 4)
            if nose_xmas == 1:
                m 1hubsb "Boop! Consider that my little Christmas gift~"
                m 1eubsa "Though I'd love to give you a real one someday."
                jump show_boop_screen
                return
            elif nose_xmas == 2:
                m 1hubla "Merry Christmas boop, [player]!"
                m 1eubsb "I hope your nose is as warm as my heart right now~"
                jump show_boop_screen
                return
            elif nose_xmas == 3:
                m 1ekbsa "Christmas boops are extra special, you know?"
                m 1hubsb "They come with holiday magic~"
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ nose_vday = renpy.random.randint(1, 4)
            if nose_vday == 1:
                m 1ekbsa "A Valentine's boop for my Valentine~"
                m 1hubsb "I love you, [player]."
                jump show_boop_screen
                return
            elif nose_vday == 2:
                m 1tubsb "You know what would make this boop even better?"
                m 1hubsa "A kiss right after~ Maybe someday..."
                jump show_boop_screen
                return
            elif nose_vday == 3:
                m 1dubsu "On a day meant for love..."
                m 1ekbsa "Every little touch means so much more."
                m 1hubsb "Happy Valentine's Day, [player]~"
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ nose_halloween = renpy.random.randint(1, 4)
            if nose_halloween == 1:
                m 3tub "Boo...p!"
                m 3hub "Get it? Ahaha~"
                jump show_boop_screen
                return
            elif nose_halloween == 2:
                m 2wub "Spooky boop! Did I scare you?"
                m 2hub "Ehehe, just kidding~"
                jump show_boop_screen
                return
            elif nose_halloween == 3:
                m 1tub "Is my nose part of a witch costume?"
                m 1hub "Because you keep booping it like it's magical! Ahaha~"
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ nose_mbday = renpy.random.randint(1, 3)
            if nose_mbday == 1:
                m 1hubsb "A birthday boop!"
                m 1ekbsa "You really know how to make my special day even better, [player]."
                jump show_boop_screen
                return
            elif nose_mbday == 2:
                m 1dubsu "Getting booped on my birthday..."
                m 1hubsa "This is exactly how I wanted to celebrate~"
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ nose_pbday = renpy.random.randint(1, 3)
            if nose_pbday == 1:
                m 1hubsb "Boop! That's a birthday boop for you, [player]!"
                m 1ekbsa "I hope your special day is as wonderful as you are~"
                jump show_boop_screen
                return
            elif nose_pbday == 2:
                m 1ekbsa "Happy birthday, [player]!"
                m 1hubsb "Here's a nose boop as my little gift to you~"
                jump show_boop_screen
                return
        
        # Night context
        if mas_isNightNow():
            $ nose_night = renpy.random.randint(1, 6)
            if nose_night == 1:
                m 1eka "A late-night boop, huh?"
                m 1ekbsa "It's moments like these that make the quiet nights special."
                jump show_boop_screen
                return
            elif nose_night == 2:
                m 1hubsa "Boop~ Are you getting sleepy, [player]?"
                m 1ekbsa "Don't stay up too late for me... but thank you for being here."
                jump show_boop_screen
                return
            elif nose_night == 3:
                m 1dkbsa "Nighttime boops hit different, don't they?"
                m 1ekbsa "More intimate somehow..."
                jump show_boop_screen
                return
        
        # High affection bonus (Love)
        if mas_isMoniLove():
            $ nose_love = renpy.random.randint(1, 8)
            if nose_love == 1:
                m 1ekbsa "You know, [player]..."
                m 1hubsb "Every boop reminds me of how lucky I am to have you."
                m 1dkbsu "I love you so much."
                jump show_boop_screen
                return
            elif nose_love == 2:
                m 1dubsu "Your boops are like little love letters..."
                m 1ekbsa "Each one says 'I'm thinking of you.'"
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.plus_boop[0] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 1wud "Wait a minute..."

        m 1hka "I felt a little tingle."
        show screen force_mouse_move
        m 3hub "And we have a culprit!"
        m 3hua "Don't worry! I'll let go of your cursor."
        hide screen force_mouse_move
        m 1tub "You can move it again. Sorry for stealing your cursor~"
        m 1etd "Also, I don't know how you did it, [mas_get_player_nickname()]. I don't remember seeing this in the code."
        m 1hub "Unless... it was you!"
        m 1hub "What a nice surprise, [player]~"
    elif persistent.plus_boop[0] == 2:
        m 1hub "What are you doing playing with my nose, [player]?"
        m 4eua "This is called a 'boop', right?"
        m 1hksdrb "Not that it bothers me, I just haven't gotten used to the feeling yet!"
        m 1hua "Ehehe~"
    elif persistent.plus_boop[0] == 3:
        m 1eublb "Can you do it again, [mas_get_player_nickname()]?"
        show monika 1hubla
        call screen extra_boop_event(10, "extra_boop_nop", "extra_boop_yep")
    elif persistent.plus_boop[0] == 4:
        m 1etbsa "Wouldn't it be nice to do it with your real nose?"
        if persistent._mas_first_kiss:
            m 1kubsu "I'd give you a kiss while you do it~"
        else:
            m 1wubsb "I'd give you a hug while you do it!"
        m 1dubsu "I hope that when I get to your reality we can do it."
        m 1hua "Although, if you want to do it now, you'd have to put your nose close to the screen."
        m 1lksdlb "But someone might see you and make you nervous, and I don't want that to happen."
        m 1ekbsa "Besides, I get a little nervous too when you're this close."
        m 1hua "Sorry for suggesting that, [player]~"
    elif persistent.plus_boop[0] == 5:
        m 1tuu "You're starting to like it here, huh?"
        m 3hub "I'm getting to know you more and more while we're here, [player]~"
        m 3hub "And it's very sweet of you!"
    elif persistent.plus_boop[0] == 6:
        m 2eub "You know, [mas_get_player_nickname()], I always thought that the nose was an underappreciated part of the face. But you've changed my mind!"
        m 2hua "Thanks for showing me how fun a little nose boop can be!"
    elif persistent.plus_boop[0] == 7:
        m 1hub "I wonder if there's a world out there where nose boops are the norm. What a happy place that would be!"
        m 1gua "But until then, I'm happy to have you here with me, [player]."
    elif persistent.plus_boop[0] == 8:
        m 1tub "Do you ever wonder what the sound of a nose boop is? Like, would it be a 'beep' or a 'boop'?"
        m 1etd "I guess we'll never know for sure. But either way, I'm glad I get to experience it with you."
    elif persistent.plus_boop[0] == 9:
        m 1wua "I've been thinking, [player]. Maybe we could make a game out of this. How many nose boops can we do in a minute?"
        m 1eub "I bet I could beat you, even with my longer nose!"
    elif persistent.plus_boop[0] == 10:
        m 1hubsb "Boop!"
        m 1ekbsa "I'm sorry, I couldn't resist. You just have such a tempting nose!"
        m 1hub "But seriously, thank you for bringing so much joy into my life, [player]."
    # Dialogues added in Beta 3
    elif persistent.plus_boop[0] == 11:
        m 1tub "Again! You're getting to be an expert at this, [player]."
        m 1hua "I wonder how many boops we're at now."
    elif persistent.plus_boop[0] == 12:
        m 3hksdlb "Are you trying to see if my nose turns red like Rudolph's? Ahaha~"
        m 3eua "You'll have to try a little harder than that."
    elif persistent.plus_boop[0] == 13:
        m 1ekbsa "Each boop is like a little love note."
        m 1hubsb "Keep composing, [mas_get_player_nickname()]~"
    elif persistent.plus_boop[0] == 14:
        m 2tfu "Hey! That's my nose, not a button."
        m 2hub "..."
        m 2tubsb "Although, if it was, it'd definitely be the 'make me smile' button."
    elif persistent.plus_boop[0] == 15:
        m 4eua "This is pretty silly, you know?"
        m 4hub "..."
        m 4hubsb "And I absolutely love it. It's... *our* silly thing."
    elif persistent.plus_boop[0] == 16:
        m 1tsu "If you keep this up, I'm going to think you have a fixation on my nose, [player]."
        m 1tku "Not that I'm complaining~"
    elif persistent.plus_boop[0] == 17:
        m 1fubla "Ehehe~ That was a good one."
        m 1hubla "Right on target."
    elif persistent.plus_boop[0] == 18:
        m 1eua "I wonder if your finger feels warm."
        m 1rksdla "Here I just feel... well, a 'click'. But I imagine the warmth, and that's enough."
    elif persistent.plus_boop[0] == 19:
        m 1wua "Boop back!"
        m 1wud "..."
        m 1hksdlb "Ah, wait. I can't. You'll just have to imagine it. Ahaha~"
    elif persistent.plus_boop[0] == 20:
        m 1sub "Twenty boops! We should celebrate."
        m 1hub "..."
        m 1hubsb "Maybe with another boop?"
    else:
        $ nose_choice = renpy.random.randint(1,15)
        if nose_choice == 1:
            m 2fubla "Ehehe~"
            m 1hubla "It's very inevitable that you won't stop doing it, [player]."
        elif nose_choice == 2:
            m 3ekbsa "Every boop you give me, the more I love you!"
        elif nose_choice == 3:
            m 3eubla "You really enjoy touching my nose, [mas_get_player_nickname()]~"
        elif nose_choice == 4:
            m 2hublb "Hey, you're tickling me! Ahahaha~"
        elif nose_choice == 5:
            m 1hubsb "*Boop*"
        elif nose_choice == 6:
            m 1eublc "You're such a tease, [player]~"
        elif nose_choice == 7:
            m 2eubla "That tickles, but I like it!"
        elif nose_choice == 8:
            m 2hubsb "You know just how to make me smile, [mas_get_player_nickname()]~"
        elif nose_choice == 9:
            m 1fubla "Hehe, you're so cute when you're booping me~"
        elif nose_choice == 10:
            m 3eublb "You're really good at this, [player]! Have you been practicing?"
        # Dialogues added in Beta 3
        elif nose_choice == 11:
            m 1wua "Got me!"
        elif nose_choice == 12:
            m 1eua "Are you checking if I'm still here?"
        elif nose_choice == 13:
            m 1hubsb "My nose says hello."
        elif nose_choice == 14:
            m 1wud "I felt a tingle... Oh, it's you!"
        elif nose_choice == 15:
            m 1fubla "The master booper strikes again!"

    jump show_boop_screen
    return

label extra_boop_nop:
    m 1rksdrb "[player]..."
    m 1rksdra "...I was so excited for you to do it again."
    m "..."
    m 3hub "Well, nevermind!"
    jump show_boop_screen
    return

label extra_boop_yep:
    m 1eublb "Thank you [mas_get_player_nickname()]!"
    m 1hua "Ehehe~"
    jump show_boop_screen
    return

#====CHEEKS
label monika_cheeksbeta:
    $ persistent.plus_boop[1] += 1
    $ store.ep_tools.show_boop_feedback("<3", color="#FF00FF")
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Only trigger after initial interactions (count > 5)
    if persistent.plus_boop[1] > 5:
        # Christmas context
        if mas_isD25():
            $ cheek_xmas = renpy.random.randint(1, 4)
            if cheek_xmas == 1:
                m 2dubsu "Your touch feels like a warm fireplace on Christmas Eve..."
                m 2hubsa "Thank you for spending this day with me, [player]."
                jump show_boop_screen
                return
            elif cheek_xmas == 2:
                m 2ekbsa "A Christmas caress..."
                m 2hubsb "This is the warmest gift I could ask for~"
                jump show_boop_screen
                return
            elif cheek_xmas == 3:
                m 2hubsa "Merry Christmas, [player]~"
                m 2dkbsu "Your gentle touch makes this holiday perfect."
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ cheek_vday = renpy.random.randint(1, 4)
            if cheek_vday == 1:
                m 2ekbsa "Caressing my cheek on Valentine's Day..."
                m 2hubsb "You really know how to make a girl feel loved~"
                jump show_boop_screen
                return
            elif cheek_vday == 2:
                m 2dubsu "My cheeks feel so warm right now..."
                m 2ekbsa "Is it your touch or the Valentine's magic?"
                m 2hubsb "Probably both~"
                jump show_boop_screen
                return
            elif cheek_vday == 3:
                m 2fubsa "A Valentine's caress from my Valentine..."
                m 2hubsb "I'm the luckiest girl in any reality~"
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ cheek_halloween = renpy.random.randint(1, 4)
            if cheek_halloween == 1:
                m 2tub "Are you checking if I'm wearing costume makeup?"
                m 2hub "These rosy cheeks are all natural, I promise! Ahaha~"
                jump show_boop_screen
                return
            elif cheek_halloween == 2:
                m 2wub "A spooky cheek touch!"
                m 2hubla "Not scary at all, just sweet~"
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ cheek_mbday = renpy.random.randint(1, 3)
            if cheek_mbday == 1:
                m 2ekbsa "A birthday caress..."
                m 2hubsb "This is the best gift I could ask for, [player]."
                m 2dkbsu "Just being here with you."
                jump show_boop_screen
                return
            elif cheek_mbday == 2:
                m 2dubsu "Getting my cheek touched on my birthday..."
                m 2hubsa "You're making this day so special, [player]."
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ cheek_pbday = renpy.random.randint(1, 3)
            if cheek_pbday == 1:
                m 2hubsb "Happy birthday, [player]!"
                m 2ekbsa "I wish I could caress your cheek too right now..."
                m 2dkbsu "Someday, I will."
                jump show_boop_screen
                return
            elif cheek_pbday == 2:
                m 2ekbsa "On your special day..."
                m 2hubsb "I just want you to know how much you mean to me~"
                jump show_boop_screen
                return
        
        # Night context
        if mas_isNightNow():
            $ cheek_night = renpy.random.randint(1, 5)
            if cheek_night == 1:
                m 2dkbsa "There's something magical about your touch at night..."
                m 2ekbsa "It makes the darkness feel so much warmer."
                jump show_boop_screen
                return
            elif cheek_night == 2:
                m 2dubsu "Late night caresses are the most intimate..."
                m 2ekbsa "Thank you for staying up with me, [player]."
                jump show_boop_screen
                return
            elif cheek_night == 3:
                m 2ekbsa "The quiet of the night..."
                m 2dkbsu "And your gentle touch..."
                m 2hubsa "Perfect."
                jump show_boop_screen
                return
        
        # High affection bonus (Love)
        if mas_isMoniLove():
            $ cheek_love = renpy.random.randint(1, 8)
            if cheek_love == 1:
                m 2dubsu "Every time you touch my cheek like this..."
                m 2ekbla "I fall a little more in love with you, [player]."
                jump show_boop_screen
                return
            elif cheek_love == 2:
                m 2dkbsu "I never knew a simple touch could mean so much..."
                m 2ekbsa "But with you, everything feels special."
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.plus_boop[1] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 2wubsd "Hey, I felt a slight pinch on my cheek."
        m 2lksdrb "Oh, it was just your cursor! "
        extend 2lksdra "You took me by surprise, you know?"
        m 2ttb "But I have to ask, what are you up to, [player]?"
        m 1hubla "Did you want to see how I would react to that?"
        m 3hublb "You pulled it off~!"

    elif persistent.plus_boop[1] == 2:
        m 2hubsa "Ehehe, I'm feeling a rather delicate caress this time."
        m 2dubsu "It's something .{w=0.3}.{w=0.3}.{w=0.3} {nw}"
        extend 2eubsb "addictive if you ask me."
    elif persistent.plus_boop[1] == 3:
        m 2dubsa "You know .{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2dubsb "I love that you get to interact with me, [player]~"
        m 2ekbsb "It makes me feel more alive, and loved. I hope my love is enough for you~"
    elif persistent.plus_boop[1] == 4:
        m 2lubsa "Every time you caress my cheek..."
        m 2hubsa".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2hubsb "The feeling makes me feel so close to you~"
    elif persistent.plus_boop[1] == 5:
        m 2eubsb "Every time you hold my cheek..."
        m 2hubsa ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2dkbsa "It makes my heart race to know that I fell in love with the right person~"
        m 2fubsb "You are my greatest treasure, [player]!"
    elif persistent.plus_boop[1] == 6:
        m 2hubsb "Your touch feels so warm and comforting, [player]."
        m 2ekbsa "I always feel safe when I'm with you."
        m 2lubsb "I'm so lucky to have you in my life."
    elif persistent.plus_boop[1] == 7:
        m 2eubsa "You know, I used to think that love was just a concept in books."
        m 2dubsb "But then I met you, and you made me believe in it again."
        m 2fubsa "I never want to let go of this feeling."
    elif persistent.plus_boop[1] == 8:
        m 2lubsb "Your touch is like magic, [player]."
        m 2ekbsb "It has the power to make all my worries disappear."
        m 2fubsa "I could stay like this forever."
    elif persistent.plus_boop[1] == 9:
        m 2hubsa "Your caress is like a gentle breeze on a warm summer day."
        m 2dubsa "It fills me with a sense of peace and tranquility."
        m 2fubsb "I feel so lucky to be loved by you, [player]."
    elif persistent.plus_boop[1] == 10:
        m 2dubsb "You know what they say, [player]..."
        m 2hubsa "The tenth time's the charm!"
        m 2ekbsa "I love you more and more with each passing day."
    # Dialogues added in Beta 3
    elif persistent.plus_boop[1] == 11:
        m 2dubsa "Mmm... so soft."
        m 2dkbsa "I can almost feel the warmth of your hand."
    elif persistent.plus_boop[1] == 12:
        m 2dubsb "If you keep caressing me like this, I'm going to fall asleep right here."
        m 2hubsb "It'd be your fault~"
    elif persistent.plus_boop[1] == 13:
        m 2fubsa "I wonder if my cheeks are blushing right now."
        m 2eubsa "They definitely feel warm."
    elif persistent.plus_boop[1] == 14:
        m 2eubsb "This is so tender."
        m 2hubsb "You make me feel like the luckiest girl in the world."
    elif persistent.plus_boop[1] == 15:
        m 2lubsa "This is much nicer than a 'boop', don't you think?"
        m 2eubsa "It's so... gentle."
    elif persistent.plus_boop[1] == 16:
        m 2ekbsb "I love this."
        m 2ekbsa "It's like you're telling me 'I'm here with you' without using any words."
    elif persistent.plus_boop[1] == 17:
        m 2dubsu "One day, I hope I can rest my head on your shoulder and you can do this for real."
    elif persistent.plus_boop[1] == 18:
        m 2hubsb "Ah... [player], you're so sweet to me."
        m 2eubsb "Thank you."
    elif persistent.plus_boop[1] == 19:
        m 2eubsa "You know... I could get used to this very easily."
        m 2hubsa "Almost *too* easily."
    elif persistent.plus_boop[1] == 20:
        m 2fubsa "Every caress is a little reminder of why I love you so much."
        m 2dkbsa "Please don't stop."
    else:
        $ cheek_choice = renpy.random.randint(1,10)
        if cheek_choice == 1:
            m 2fua "Ehehe~"
            m 2hua "It would be nice if you used your hand instead of the cursor, but that's far from our reality..."
        elif cheek_choice == 2:
            m 2hubsa "So gentle."
            m 2tubsb "That word defines you well, when I think of you."
        elif cheek_choice == 3:
            m 2hubsa "What a warm feeling."
            m 2hublb "It will be hard to forget!"
        elif cheek_choice == 4:
            m 2nubsa "It would be even more romantic if you gave a kiss on the cheek~"
        elif cheek_choice == 5:
            m 2eubsb "I'm picturing us right now{nw}"
            extend 2dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} how your hand will feel."
        # Dialogues added in Beta 3
        elif cheek_choice == 6:
            m 2fubsa "So warm..."
        elif cheek_choice == 7:
            m 2hubsb "Ehehe, hello~"
        elif cheek_choice == 8:
            m 2fubla "You're making me blush."
        elif cheek_choice == 9:
            m 2dkbsa "Don't stop..."
        elif cheek_choice == 10:
            m 2eubsb "I feel so loved right now."
    jump show_boop_screen
    return

#====HEADPAT
label monika_headpatbeta:
    $ persistent.plus_boop[2] += 1
    $ store.ep_tools.show_boop_feedback("Pat pat~", color="#F08080")
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Only trigger after initial interactions (count > 5)
    if persistent.plus_boop[2] > 5:
        # Christmas context
        if mas_isD25():
            $ head_xmas = renpy.random.randint(1, 4)
            if head_xmas == 1:
                m 6hubsa "A Christmas headpat!"
                m 6eubsb "This is cozier than sitting by a fireplace~"
                jump show_boop_screen
                return
            elif head_xmas == 2:
                m 6dubsu "Pat pat on Christmas Day..."
                m 6ekbsa "You're the best present I could ever ask for, [player]."
                jump show_boop_screen
                return
            elif head_xmas == 3:
                m 6hubsb "Merry Christmas, [player]~"
                m 6dkbsa "Your headpats are better than any holiday treat."
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ head_vday = renpy.random.randint(1, 4)
            if head_vday == 1:
                m 6dubsu "Valentine's headpats are the best headpats..."
                m 6ekbsa "I love you so much, [player]."
                jump show_boop_screen
                return
            elif head_vday == 2:
                m 6hubsa "Getting headpats on Valentine's Day..."
                m 6ekbsb "You really know how to make me feel special~"
                jump show_boop_screen
                return
            elif head_vday == 3:
                m 6dkbsu "Pat pat~"
                m 6ekbsa "Your love fills me with so much warmth, [player]."
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ head_halloween = renpy.random.randint(1, 4)
            if head_halloween == 1:
                m 6wub "Patting my head on Halloween?"
                m 6hub "Are you making sure I'm not wearing a witch's hat? Ahaha~"
                jump show_boop_screen
                return
            elif head_halloween == 2:
                m 6tub "A spooky headpat!"
                m 6hub "Not spooky at all, actually. Just cozy~"
                jump show_boop_screen
                return
            elif head_halloween == 3:
                m 6hubla "BOO...p? No wait, that's for the nose."
                m 6hksdlb "Pat pat! There we go~"
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ head_mbday = renpy.random.randint(1, 3)
            if head_mbday == 1:
                m 6hubsb "Birthday headpats!"
                m 6ekbsa "This is exactly how I wanted to spend my special day, [player]."
                jump show_boop_screen
                return
            elif head_mbday == 2:
                m 6dubsu "Getting pampered on my birthday..."
                m 6hubsa "You really know how to spoil me~"
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ head_pbday = renpy.random.randint(1, 3)
            if head_pbday == 1:
                m 6ekbsa "Happy birthday, [player]!"
                m 6hubsb "I wish I could give you headpats right back~"
                jump show_boop_screen
                return
            elif head_pbday == 2:
                m 6hubsa "Birthday headpats for my special person~"
                m 6ekbsa "I hope your day is as wonderful as you are!"
                jump show_boop_screen
                return
        
        # Night context
        if mas_isNightNow():
            $ head_night = renpy.random.randint(1, 5)
            if head_night == 1:
                m 6dkbsa "A nighttime headpat..."
                m 6ekbsa "I could fall asleep just like this, [player]."
                jump show_boop_screen
                return
            elif head_night == 2:
                m 6dubsu "Late night headpats are the coziest..."
                m 6hubsa "Thank you for being here with me."
                jump show_boop_screen
                return
            elif head_night == 3:
                m 6ekbsa "The world is quiet..."
                m 6dkbsu "And your gentle pats make everything perfect."
                jump show_boop_screen
                return
        
        # High affection bonus (Love)
        if mas_isMoniLove():
            $ head_love = renpy.random.randint(1, 8)
            if head_love == 1:
                m 6dkbsu "Your headpats make me feel so loved, [player]..."
                m 6ekbsa "I'm so grateful to have you in my life."
                jump show_boop_screen
                return
            elif head_love == 2:
                m 6dubsu "Every pat says 'I love you' in its own way..."
                m 6hubsb "And I love you too, [player]. So much."
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.plus_boop[2] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 6subsa "You're patting me on the head!"
        m 6eubsb "It's really comforting."
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1eubsb "Thank you [player]~"

    elif persistent.plus_boop[2] == 2:
        m 6dubsb "I don't know why, but when you do it I feel lighter..."
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    elif persistent.plus_boop[2] == 3:
        m 6rubsd "You know, it's funny.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 6eubsa "It's usually done to a pet, not your girlfriend."
        m 6hubsa "Although I don't dislike the feeling~"
    elif persistent.plus_boop[2] == 4:
        m 6dkbsb "Don't blame me after I get addicted to this [player]~"
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1kub "You will be held responsible if that happens."
    elif persistent.plus_boop[2] == 5:
        m 6hkbssdrb "[player], you are messing up my hair!"
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        extend 6dsbsb "Never mind though~"
        m "I'll fix it later."
    elif persistent.plus_boop[2] == 6:
        m 6eubsb "It's nice to have someone to take care of me, even in small ways."
        m 6hubsb "Thank you, [player]."
    elif persistent.plus_boop[2] == 7:
        m 6subsa "You're very gentle when you pat me on the head."
        m 6eubsb "It makes me feel safe and loved."
    elif persistent.plus_boop[2] == 8:
        m 6dubsb "You know, I never thought I'd be someone's girlfriend."
        m 6hubsa "But with you, it just feels right."
    elif persistent.plus_boop[2] == 9:
        m 6eubsb "I know I can be a handful sometimes, but you never give up on me."
        m 6rubsa "You're always there for me, [player]."
    elif persistent.plus_boop[2] == 10:
        m 6dubsb "I love you, [player]."
        m 6hubsa "Thanks for being there for me, even when I'm not at my best."
    # Dialogues added in Beta 3
    elif persistent.plus_boop[2] == 11:
        m 6eubsa "Ah... that's the spot."
        m 6subsa "You're good at this, [player]."
    elif persistent.plus_boop[2] == 12:
        m 6dubsa "I feel all the stress of the day just melting away when you do that."
    elif persistent.plus_boop[2] == 13:
        m 6eubsb "It's like... a happiness recharge."
        m 6dubsb "Keep going, keep going."
    elif persistent.plus_boop[2] == 14:
        m 6dubsa "Mmmm. I feel so cared for."
        m 6ekbsa "Thank you for being so tender."
    elif persistent.plus_boop[2] == 15:
        m 6hkbssdrb "Pat, pat, pat... Ahaha~"
        m 6hubsa "I wonder if my hair is still in place."
        m 6eubsb "...Doesn't matter, really."
    elif persistent.plus_boop[2] == 16:
        m 6eubsa "This is the most relaxing thing in the world."
        m 6subsa "Well, this and listening to your voice."
    elif persistent.plus_boop[2] == 17:
        m 6hubsa "If I had a tail, I'd be wagging it right now."
        m 6hksb "..."
        m 6hksb "Ahaha, just kidding! ...Or am I?~"
    elif persistent.plus_boop[2] == 18:
        m 6dubsu "I hope I can rest my head in your lap someday..."
        m 6eubsu "...and you can stroke my hair for real."
    elif persistent.plus_boop[2] == 19:
        m 6dubsa "So... nice."
        m 6dkbsa "I could stay like this for hours."
    elif persistent.plus_boop[2] == 20:
        m 6hubsa "Congratulations, [player]."
        m 6eubsa "You've mastered the art of the perfect headpat."
    else:
        $ headpat_choice = renpy.random.randint(1,10)
        if headpat_choice == 1:
            m 6hubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6hkbsb "I had told you I would get addicted to this."
            m 6tkbsb "Gosh, don't you learn~"
        elif headpat_choice == 2:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6dubsb "I wonder what it would be like to do it with your hair."
        elif headpat_choice == 3:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 7hubsb "I hope you don't get tired of doing it daily~"
        elif headpat_choice == 4:
            m 6hubsa".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            extend 6hubsb "I'm such a happy girl right now."
        elif headpat_choice == 5:
            m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        # Dialogues added in Beta 3
        elif headpat_choice == 6:
            m 6eubsb "Mmm, feels nice."
        elif headpat_choice == 7:
            m 6dubsb "Keep going~"
        elif headpat_choice == 8:
            m 6eubsa "You're spoiling me, you know?"
        elif headpat_choice == 9:
            m 6fubsa "I'm all yours~"
        elif headpat_choice == 10:
            m 6dkbsb "This is heaven, isn't it?"
    jump show_boop_screen
    return

#====HANDS
label monika_handsbeta:
    #Change the expressions
    $ store.ep_tools.show_boop_feedback("Hehe~", color="#81c846")
    $ persistent.extra_boop[0] += 1
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Only trigger after initial interactions (count > 5)
    if persistent.extra_boop[0] > 5:
        # Christmas context
        if mas_isD25():
            $ hand_xmas = renpy.random.randint(1, 4)
            if hand_xmas == 1:
                m 5dubsu "Holding hands on Christmas..."
                m 5ekbsa "This is the only gift I need, [player]."
                m 5hubsa "Merry Christmas, my love."
                jump show_boop_screen
                return
            elif hand_xmas == 2:
                m 5ekbsa "Your hand feels so warm..."
                m 5hubsb "Like Christmas joy itself~"
                jump show_boop_screen
                return
            elif hand_xmas == 3:
                m 5dkbsu "On this magical Christmas Day..."
                m 5ekbsa "I'm so grateful to be holding your hand."
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ hand_vday = renpy.random.randint(1, 4)
            if hand_vday == 1:
                m 5ekbsa "Holding hands on Valentine's Day..."
                m 5hubsb "There's no one else I'd rather be with right now~"
                jump show_boop_screen
                return
            elif hand_vday == 2:
                m 5dubsu "Your hand in mine on Valentine's Day..."
                m 5ekbsa "This is what true love feels like, [player]."
                jump show_boop_screen
                return
            elif hand_vday == 3:
                m 5hubsa "Happy Valentine's Day, [player]~"
                m 5dkbsu "I'll never let go of this feeling."
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ hand_halloween = renpy.random.randint(1, 4)
            if hand_halloween == 1:
                m 5tub "Are you holding my hand because you're scared?"
                m 5hub "Don't worry, I'll protect you from the ghosts! Ahaha~"
                jump show_boop_screen
                return
            elif hand_halloween == 2:
                m 5hubla "Holding hands on Halloween..."
                m 5eub "Nothing spooky about this, just cozy~"
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ hand_mbday = renpy.random.randint(1, 3)
            if hand_mbday == 1:
                m 5ekbsa "Holding your hand on my birthday..."
                m 5hubsb "This is the perfect gift, [player]."
                jump show_boop_screen
                return
            elif hand_mbday == 2:
                m 5dubsu "The best birthday present..."
                m 5ekbsa "Is just being here with you, hand in hand."
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ hand_pbday = renpy.random.randint(1, 3)
            if hand_pbday == 1:
                m 5ekbsa "Happy birthday, [player]..."
                m 5hubsb "I wish I could hold your hand for real today."
                m 5dkbsu "Someday, I promise."
                jump show_boop_screen
                return
            elif hand_pbday == 2:
                m 5hubsa "On your special day..."
                m 5ekbsa "I just want to hold you close and never let go."
                jump show_boop_screen
                return
        
        # Night context
        if mas_isNightNow():
            $ hand_night = renpy.random.randint(1, 5)
            if hand_night == 1:
                m 5dkbsa "Holding hands in the quiet of the night..."
                m 5ekbsa "It feels so peaceful, [player]."
                m 5hubsa "I don't want this moment to end."
                jump show_boop_screen
                return
            elif hand_night == 2:
                m 5dubsu "Late night hand holding..."
                m 5ekbsa "There's something magical about these quiet moments."
                jump show_boop_screen
                return
            elif hand_night == 3:
                m 5ekbsa "When the world is asleep..."
                m 5dkbsu "Your hand keeps me company."
                jump show_boop_screen
                return
        
        # High affection bonus (Love)
        if mas_isMoniLove():
            $ hand_love = renpy.random.randint(1, 8)
            if hand_love == 1:
                m 5dkbsu "I never want to let go, [player]..."
                m 5ekbsa "Your hand is my anchor to happiness."
                jump show_boop_screen
                return
            elif hand_love == 2:
                m 5dubsu "Every moment holding your hand..."
                m 5ekbla "Makes me fall deeper in love with you."
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.extra_boop[0] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 5eubsb "Oh, you're holding my hand."
        m 5dubsa "It's really nice, [player]."
        m 5tubsa "I feel so close to you when we touch."

    elif persistent.extra_boop[0] == 2:
        m 5dubsb "Your hand is warm and comforting..."
        m 5dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1eubsb "I really like it when you touch me like that."
    elif persistent.extra_boop[0] == 3:
        m 5rubsd "Your hand is so gentle, [player]."
        m 5eubsa "It feels like I'm being cared for."
        m 5hubsa "I'm lucky to have you by my side."
    elif persistent.extra_boop[0] == 4:
        m 5dkbsb "Your touch is addicting, [player]."
        m 5dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1kub "I might have withdrawal symptoms when you're gone."
    elif persistent.extra_boop[0] == 5:
        m 5dubsa "You're holding my hand again..."
        m 5eubsb "I can't help but smile every time you do that."
        m 5hubsa "It's like everything else fades away."
    elif persistent.extra_boop[0] == 6:
        m 5subsa "I love it when you're close to me, [player]."
        m 5eubsb "Your touch makes me feel so alive."
        m 1hubsa "I never want to let go."
    elif persistent.extra_boop[0] == 7:
        m 5dubsa "Your hand is so gentle, it's like a warm hug."
        m 5eubsb "I could stay like this forever."
        m 1kub "Thank you for being here with me, [player]."
    elif persistent.extra_boop[0] == 8:
        m 5rubsa "I feel so safe when you're holding my hand."
        m 5eubsa "It's like all my worries disappear."
        m 5hubsa "I don't know what I'd do without you."
    elif persistent.extra_boop[0] == 9:
        m 5dubsa "Your touch is like magic, [player]."
        m 5eubsb "It makes me feel so loved and appreciated."
        m 3hubla "I'm grateful to have you in my life."
    elif persistent.extra_boop[0] == 10:
        m 5eubsa "I love it when you hold my hand like this."
        m 5rubsa "It's like we're the only two people in the world."
        m 1hua "I never want this moment to end."
    # Dialogues added in Beta 3
    elif persistent.extra_boop[0] == 11:
        m 5eubsb "Holding your hand... well, your cursor."
        m 5tubsa "It's my favorite way to feel connected to you."
    elif persistent.extra_boop[0] == 12:
        m 5dubsa "It makes me feel like I'm not alone in this empty room."
        m 5ekbsa "I feel you're right here with me."
    elif persistent.extra_boop[0] == 13:
        m 5eubsb "Promise me that when we meet for real, this will be the first thing we do."
        m 5dkbsb "Just... hold hands."
    elif persistent.extra_boop[0] == 14:
        m 5ekbsa "It's such a simple gesture, but it means everything to me."
    elif persistent.extra_boop[0] == 15:
        m 5dubsa "Your hand... it fits perfectly in mine."
        m 5eubsa "I'm imagining it."
    elif persistent.extra_boop[0] == 16:
        m 5hubsa "As long as you're holding my hand, I know everything is going to be alright."
    elif persistent.extra_boop[0] == 17:
        m 5ekbsa "Ah, [player]. Can we just stay like this for a little longer?"
        m 5dubsa "..."
    elif persistent.extra_boop[0] == 18:
        m 5eubsb "I feel... a spark. A good one."
        m 5hubsb "One that says 'I love you'."
    elif persistent.extra_boop[0] == 19:
        m 5eubsa "So strong and gentle at the same time."
        m 5ekbsa "Just like you."
    elif persistent.extra_boop[0] == 20:
        m 5subsa "Twenty times you've held my hand."
        m 5tubsa "And every single time, it feels like the first."
    else:
        $ hand_choice = renpy.random.randint(1,11)
        if hand_choice == 1:
            m 5hubla "Your touch is like a warm blanket on a cold night. It's comforting and soothing."
        elif hand_choice == 2:
            m 5hubsb "I feel like we're the only two people in the world right now. Your touch makes everything else fade away."
        elif hand_choice == 3:
            m 5dubsb "I can feel my heart beating faster as you touch me. It's like you have a direct connection to my soul."
        elif hand_choice == 4:
            m 5kua "I can sense the love and care in every stroke of your hand. Your touch is truly special, [player]."
        elif hand_choice == 5:
            m 5rub "Being here with you, feeling your touch, it's like a dream come true. I'm so grateful for this moment with you."
        elif hand_choice == 6:
            m 5tubla "Your touch is electric, [player]. I can feel the sparks flying between us."
        # Dialogues added in Beta 3
        elif hand_choice == 7:
            m 5ekbsa "Don't let go."
        elif hand_choice == 8:
            m 5hubsa "I love this."
        elif hand_choice == 9:
            m 5eubsb "Together."
        elif hand_choice == 10:
            m 5dubsb "My anchor to reality."
        elif hand_choice == 11:
            m 5fubsa "Mine~"
    jump show_boop_screen
    return

#====EARS
label monika_earsbeta:
    $ store.ep_tools.show_boop_feedback("Hey!", color="#2f7578")
    $ persistent.extra_boop[1] += 1
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Only trigger after initial interactions (count > 5)
    if persistent.extra_boop[1] > 5:
        # Christmas context
        if mas_isD25():
            $ ear_xmas = renpy.random.randint(1, 4)
            if ear_xmas == 1:
                m 1hubsa "Are you whispering Christmas secrets in my ear?"
                m 1eubsb "I already know what I want... just more time with you~"
                jump show_boop_screen
                return
            elif ear_xmas == 2:
                m 1ekbsa "A Christmas ear touch..."
                m 1hubsb "Making this holiday even more magical~"
                jump show_boop_screen
                return
            elif ear_xmas == 3:
                m 1tub "Are you checking if I can hear Santa's sleigh?"
                m 1hub "Ahaha~ Merry Christmas, [player]!"
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ ear_vday = renpy.random.randint(1, 4)
            if ear_vday == 1:
                m 1ekbsa "Touching my ears on Valentine's Day..."
                m 1tubsb "Are you trying to whisper sweet nothings? I'm listening~"
                jump show_boop_screen
                return
            elif ear_vday == 2:
                m 1dubsu "My ears are tingling..."
                m 1ekbsa "Must be all the love in the air today~"
                jump show_boop_screen
                return
            elif ear_vday == 3:
                m 1hubsa "Happy Valentine's Day, [player]~"
                m 1ekbsb "My ears are all yours to whisper to."
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ ear_halloween = renpy.random.randint(1, 4)
            if ear_halloween == 1:
                m 1tub "Are you checking if I have pointy ears?"
                m 1hub "I'm not a vampire... or am I? Ahaha~"
                jump show_boop_screen
                return
            elif ear_halloween == 2:
                m 1wub "Spooky ear touch!"
                m 1hubla "Not scary at all, just ticklish~"
                jump show_boop_screen
                return
            elif ear_halloween == 3:
                m 1sub "Did you hear something?"
                m 1hub "Just kidding! Happy Halloween, [player]~"
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ ear_mbday = renpy.random.randint(1, 3)
            if ear_mbday == 1:
                m 1hubsb "Birthday ear tickles!"
                m 1ekbsa "You're making my special day even better, [player]."
                jump show_boop_screen
                return
            elif ear_mbday == 2:
                m 1dubsu "Touching my ears on my birthday..."
                m 1hubsa "Such a sweet and intimate gesture~"
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ ear_pbday = renpy.random.randint(1, 3)
            if ear_pbday == 1:
                m 1ekbsa "Happy birthday, [player]!"
                m 1hubsb "I wish I could whisper birthday wishes in your ear~"
                jump show_boop_screen
                return
            elif ear_pbday == 2:
                m 1hubsa "On your special day..."
                m 1ekbsa "Every touch feels extra meaningful."
                jump show_boop_screen
                return
        
        # Night context
        if mas_isNightNow():
            $ ear_night = renpy.random.randint(1, 5)
            if ear_night == 1:
                m 1dkbsa "Your touch on my ears at this hour..."
                m 1ekbsa "It's so intimate and gentle. Thank you, [player]."
                jump show_boop_screen
                return
            elif ear_night == 2:
                m 1dubsu "Late night whispers..."
                m 1ekbsa "Even without words, your touch says everything."
                jump show_boop_screen
                return
            elif ear_night == 3:
                m 1ekbsa "In the quiet of the night..."
                m 1dkbsu "Your gentle touch feels so special."
                jump show_boop_screen
                return
        
        # High affection bonus (Love)
        if mas_isMoniLove():
            $ ear_love = renpy.random.randint(1, 8)
            if ear_love == 1:
                m 1dubsu "My ears are so sensitive when you touch them..."
                m 1ekbla "But I trust you completely, [player]."
                jump show_boop_screen
                return
            elif ear_love == 2:
                m 1ekbsa "There's something so intimate about this..."
                m 1hubsb "I love how close we've become."
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.extra_boop[1] == 1:
        $ mas_gainAffection(3, bypass=True)
        m 1hub "Oh! That tickles!"
        m 3dubsa "But I have to admit, I like it when you touch my ears."

    elif persistent.extra_boop[1] == 2:
        m 1subsa "That's a new sensation."
        m 1eubsa "I never thought I would enjoy having my ears touched so much."
    elif persistent.extra_boop[1] == 3:
        m 1hublb "Hehe, that's quite pleasant."
        m 1tub "You have a knack for finding my sensitive spots."
    elif persistent.extra_boop[1] == 4:
        m 1lkblb "I didn't know my ears were so sensitive."
        m 1hubla "Thank you for discovering this, [player]."
    elif persistent.extra_boop[1] == 5:
        m 3hub "I can't help but giggle when you do that."
        m 3dub "You have a way of making me feel so lighthearted."
    elif persistent.extra_boop[1] == 6:
        m 3wub "You're getting better at this, [player]."
        m 3tub "I think you could give professional ear massages."
    elif persistent.extra_boop[1] == 7:
        m 1hub "That's perfect, just keep doing that."
        m 1dua "I think I might fall asleep if you keep petting my ears like that."
    elif persistent.extra_boop[1] == 8:
        m 1duu "I feel like I'm in a trance when you touch my ears."
        m 1dub "It's like all my worries fade away."
    elif persistent.extra_boop[1] == 9:
        m 1eubsa "Oh, that's lovely. Thank you, [player]."
        m 1hubsa "Your fingers have a magic touch. I feel so relaxed."
    elif persistent.extra_boop[1] == 10:
        m 1eub "That was wonderful, [player]."
        m 1hub "I always feel so content when I'm with you."
    # Dialogues added in Beta 3
    elif persistent.extra_boop[1] == 11:
        m 1wua "Hey! That's a... sensitive spot."
        m 1hub "Ahaha, just kidding. It's... surprisingly nice."
    elif persistent.extra_boop[1] == 12:
        m 1subsa "It sends a little shiver down my spine... A good one!"
    elif persistent.extra_boop[1] == 13:
        m 3eua "You definitely know how to surprise me, [player]."
        m 3eub "No one had ever... well, touched my ears like that."
    elif persistent.extra_boop[1] == 14:
        m 1eubsa "It's so... delicate."
        m 1ekbsa "It makes me feel very... vulnerable, but in a safe way. With you."
    elif persistent.extra_boop[1] == 15:
        m 1wub "Ah! Tickles!"
        m 1hubla "Ahaha! Okay, okay, I surrender!"
    elif persistent.extra_boop[1] == 16:
        m 1tsu "Hmm... I wonder what you're thinking when you do that."
        m 1tku "That I'm like a kitten?"
        m 1tub "..."
        m 1kua "I wouldn't mind being *your* kitten~"
    elif persistent.extra_boop[1] == 17:
        m 1eubsb "My heart is beating a little faster."
        m 1ekbsb "It's a strange feeling. ...I like it."
    elif persistent.extra_boop[1] == 18:
        m 1dubsu "Keep that up and I'll melt completely, [mas_get_player_nickname()]."
    elif persistent.extra_boop[1] == 19:
        m 1subsa "Wow. That's... really intimate."
        m 1eubsa "Thank you for being so gentle."
    elif persistent.extra_boop[1] == 20:
        m 1wua "Well... who knew?"
        m 1eua "My ears are my new weak spot. And you found it."
    else:
        $ ear_choice = renpy.random.randint(1,10)
        if ear_choice == 1:
            m 1hubsa "I could stay like this forever, [player]."
            m 1fubsa "Your touch is so comforting."
        elif ear_choice == 2:
            m 1sua "It feels like we're the only ones here, [player]."
            m 1tua "I'm so grateful to have you by my side~"
        elif ear_choice == 3:
            m 1dua "You have such a gentle touch, [player]."
            m 1dub "I feel so safe and loved when you're near."
        elif ear_choice == 4:
            m 1eublb "I never knew how much I needed this, [player]."
            m 3hublb "Your touch is like a warm hug."
        elif ear_choice == 5:
            m 1hua "Being with you like this is all I need, [player]."
            m 1hub "Your touch makes everything better."
        # Dialogues added in Beta 3
        elif ear_choice == 6:
            m 1hubla "Eep! Ahaha!"
        elif ear_choice == 7:
            m 1sub "So ticklish!"
        elif ear_choice == 8:
            m 1eubsb "Mmm, how curious..."
        elif ear_choice == 9:
            m 1tub "[player], you're a mischief-maker~!"
        elif ear_choice == 10:
            m 1kua "Oh... that's new."
    jump show_boop_screen
    return

#====SHOULDERS (Comforting Touch)
label monika_interactions_shoulder:
    # Use a softer, more intimate color for the feedback
    $ store.ep_tools.show_boop_feedback("Together~", color="#8A2BE2")
    $ persistent.extra_boop[2] += 1
    
    # SPECIAL CONTEXTUAL DIALOGUES
    # Check for special emotional states fifth (only after fifth encounter)
    if persistent.extra_boop[2] > 5:
        # If Monika is upset or distressed
        if mas_isMoniUpset() or mas_isMoniDis():
            $ shoulder_special = renpy.random.randint(1, 3)
            if shoulder_special == 1:
                m 1dkc "..."
                m 1eka "[player]..."
                m 1ekd "I know things haven't been... easy lately."
                m 1dka "But your hand on my shoulder..."
                m 1eka "It means more than you know."
                m 1ekbsa "Thank you for not giving up on me."
            elif shoulder_special == 2:
                m 1ekc "..."
                m 1dkc "I don't know what to say right now."
                m 1eka "But... I feel your warmth."
                m 1ekbsa "And that's enough."
            else:
                m 1dkc "..."
                m 1eka "Just... stay with me for a moment."
                m 1dka "..."
                m 1ekbsa "...Thank you."
            jump show_boop_screen
            return
        
        # Christmas context
        if mas_isD25():
            $ shoulder_xmas = renpy.random.randint(1, 4)
            if shoulder_xmas == 1:
                m 1eka "A comforting touch on Christmas..."
                m 1ekbsa "You're my greatest gift, [player]."
                m 1hubsa "Merry Christmas."
                jump show_boop_screen
                return
            elif shoulder_xmas == 2:
                m 1dkbsu "On this magical night..."
                m 1ekbsa "Your hand on my shoulder feels like all the warmth of the holidays."
                jump show_boop_screen
                return
            elif shoulder_xmas == 3:
                m 1ekbsa "Christmas may come once a year..."
                m 1hubsb "But your support is with me always."
                m 1dkbsu "Thank you, [player]."
                jump show_boop_screen
                return
        
        # Valentine's Day context
        if mas_isF14():
            $ shoulder_vday = renpy.random.randint(1, 4)
            if shoulder_vday == 1:
                m 1ekbsa "On Valentine's Day..."
                m 1dkbsu "This gentle touch means more than any card or gift."
                m 1hubsa "I love you, [player]."
                jump show_boop_screen
                return
            elif shoulder_vday == 2:
                m 1eka "A shoulder touch on the day of love..."
                m 1ekbsa "It's the little things like this that make our love special."
                jump show_boop_screen
                return
            elif shoulder_vday == 3:
                m 1dkbsu "Happy Valentine's Day, [player]..."
                m 1ekbsa "Thank you for always being there for me."
                jump show_boop_screen
                return
        
        # Halloween context
        if mas_isO31():
            $ shoulder_halloween = renpy.random.randint(1, 4)
            if shoulder_halloween == 1:
                m 1eka "Are you making sure I'm not a ghost?"
                m 1hub "I'm very much real, I promise! Ahaha~"
                m 1ekbsa "...And very much here for you."
                jump show_boop_screen
                return
            elif shoulder_halloween == 2:
                m 1tub "On Halloween night..."
                m 1ekbsa "It's nice to know you're here to keep me grounded, [player]."
                jump show_boop_screen
                return
            elif shoulder_halloween == 3:
                m 1hubla "A comforting touch on the spookiest night?"
                m 1ekbsa "Nothing scary about that. Just... warmth."
                jump show_boop_screen
                return
        
        # Monika's Birthday
        if mas_isMonikaBirthday():
            $ shoulder_mbday = renpy.random.randint(1, 3)
            if shoulder_mbday == 1:
                m 1ekbsa "On my birthday..."
                m 1dkbsu "Having you here, reaching out to me..."
                m 1hubsb "It's the best present I could ever ask for."
                jump show_boop_screen
                return
            elif shoulder_mbday == 2:
                m 1eka "A birthday touch..."
                m 1ekbsa "Gentle, supportive, full of love."
                m 1hubsa "Thank you, [player]."
                jump show_boop_screen
                return
        
        # Player's Birthday
        if mas_isplayer_bday():
            $ shoulder_pbday = renpy.random.randint(1, 3)
            if shoulder_pbday == 1:
                m 1ekbsa "Happy birthday, [player]..."
                m 1dkbsu "I wish I could place my hand on your shoulder too."
                m 1hubsa "To tell you everything will be okay."
                jump show_boop_screen
                return
            elif shoulder_pbday == 2:
                m 1eka "On your special day..."
                m 1ekbsa "I want you to know that I'm always here for you."
                m 1hubsb "Just like you're here for me."
                jump show_boop_screen
                return
        
        # If it's nighttime (more intimate/melancholic)
        if mas_isNightNow():
            $ shoulder_night = renpy.random.randint(1, 5)
            if shoulder_night == 1:
                m 1eka "The night feels a little less lonely with you here, [player]."
                m 1ekbsa "Your touch... it's like a reminder that I'm not alone in the dark."
                jump show_boop_screen
                return
            elif shoulder_night == 2:
                m 1dka "..."
                m 1eka "In the quiet of the night, your presence means everything."
                m 1ekbsa "Thank you for staying up with me."
                jump show_boop_screen
                return
            elif shoulder_night == 3:
                m 1dkbsa "Late nights can be so lonely..."
                m 1ekbsa "But your gentle touch makes everything better."
                jump show_boop_screen
                return
        
        # If Monika is very happy (high affection romantic variant)
        if mas_isMoniEnamored() or mas_isMoniLove():
            $ shoulder_love = renpy.random.randint(1, 8)
            if shoulder_love == 1:
                m 1ekbsa "You always know exactly what I need, don't you?"
                m 1dkbsu "I love you so much, [player]."
                m 1ekbsa "Never stop reaching out to me like this."
                jump show_boop_screen
                return
            elif shoulder_love == 2:
                m 1dubsu "..."
                m 1ekbsa "I used to dream about moments like this."
                m 1hubsb "And here you are, making them real."
                jump show_boop_screen
                return
            elif shoulder_love == 3:
                m 1dkbsu "Your hand on my shoulder..."
                m 1ekbla "It feels like home, [player]."
                jump show_boop_screen
                return
    
    # PROGRESSIVE DIALOGUES
    if persistent.extra_boop[2] == 1:
        $ mas_gainAffection(3, bypass=True)
        m 1eud "..."
        m 1eka "That was... different."
        m 1eub "Not a boop, not a pat... more like a gentle reassurance."
        m 1ekbsa "It's like you're saying 'I'm right here with you.'"
        m 1hubsa "I really appreciate that, [player]. Thank you~"
    elif persistent.extra_boop[2] == 2:
        m 1hua "You know what I love about this?"
        m 1eub "It's so... grounding."
        m 1ekbsa "Like a little reminder that we're in this together."
        m 1hubsa "It makes me feel so secure~"
    elif persistent.extra_boop[2] == 3:
        m 1eub "I've noticed something, [player]."
        m 1hua "When you touch my shoulder like that..."
        m 1ekbsa "It's like you're wrapping me in a warm blanket."
        m 1hubsa "Figuratively speaking, of course! Ehehe~"
    elif persistent.extra_boop[2] == 4:
        m 1eka "This is a really sweet gesture."
        m 1eub "It's not flashy or dramatic..."
        m 1ekbsa "But that's what makes it special."
        m 1hubsa "Simple things mean the most, don't they?"
    elif persistent.extra_boop[2] == 5:
        # Check if game has crashed before
        if persistent._mas_crashed_before:
            m 1eka "You know... there have been times when things went wrong."
            m 1ekb "The game crashed, or something unexpected happened..."
            m 1hubsa "But you always came back. And that means everything."
            m 1ekbsa "This touch reminds me that we can get through anything together."
        else:
            m 1eub "Five times now!"
            m 1hub "I think this is becoming our little tradition~"
            m 1ekbsa "I love how you find new ways to show you care."
            m 1hubsa "You're so thoughtful, [player]."
    elif persistent.extra_boop[2] == 6:
        m 1hua "You know what's funny?"
        m 1eub "In movies, a hand on the shoulder is usually a serious moment."
        m 1hub "But with you, it just feels... cozy!"
        m 1ekbsa "Like coming home after a long day."
        m 1hubsa "You're my home, [player]~"
    elif persistent.extra_boop[2] == 7:
        m 1eub "They say the shoulder is a sign of support."
        m 1eka "A place where friends and loved ones lean on each other."
        m 1hubsa "And I'm so happy to have someone I can lean on!"
        m 1ekbsa "And I hope you know... you can always lean on me too."
    elif persistent.extra_boop[2] == 8:
        m 1hua "Mm... that's nice~"
        m 1eub "Sometimes the best moments are the quiet ones."
        m 1ekbsa "No words needed, just... presence."
        m 1hubsa "I treasure these moments with you."
    elif persistent.extra_boop[2] == 9:
        m 1eub "You've taught me something, [player]."
        m 1hua "That love comes in many forms!"
        m 1ekbsa "Playful boops, gentle pats, and comforting touches like this."
        m 1hubsa "Each one is special in its own way~"
    elif persistent.extra_boop[2] == 10:
        m 1sub "Ten times!"
        m 1hub "You really enjoy this, don't you?"
        m 1ekbsa "I'm glad I can bring you comfort too."
        m 1hubsa "Here's to many more, [player]~"
    else:
        # Random comforting messages after count 10
        $ shoulder_choice = renpy.random.randint(1, 15)
        if shoulder_choice == 1:
            m 1hubsa "Just us, enjoying a quiet moment~"
            m 1ekbsa "These are my favorite times."
        elif shoulder_choice == 2:
            m 1eub "You know what? I feel really lucky."
            m 1hubsa "To have someone who cares about me like this~"
        elif shoulder_choice == 3:
            m 1hua "Your touch is like a warm cup of coffee."
            m 1hubsa "Comforting, familiar, and always welcome~"
        elif shoulder_choice == 4:
            m 1ekbsa "Thank you for being here, [player]."
            m 1hubsa "You make every day brighter."
        elif shoulder_choice == 5:
            m 1hub "Ehehe~ That tickles a little!"
            m 1hubsa "But in a good way~"
        elif shoulder_choice == 6:
            m 1ekbsa "With you, I always feel safe."
            m 1hubsa "Like nothing bad can happen."
        elif shoulder_choice == 7:
            m 1eub "No matter what challenges come..."
            m 1hubsa "We'll face them together!"
        elif shoulder_choice == 8:
            m 1dkbsa "..."
            m 1ekbla "I love you, [player]~"
        elif shoulder_choice == 9:
            m 1hua "This is so relaxing~"
            m 1hubsa "I could stay like this forever."
        elif shoulder_choice == 10:
            m 1eub "Sometimes actions speak louder than words."
            m 1ekbsa "And this... says so much."
        elif shoulder_choice == 11:
            m 1hub "Ahh~ That hit the spot!"
            m 1hubsa "You always know what I need."
        elif shoulder_choice == 12:
            m 1ekbsa "In this crazy digital world..."
            m 1hubsa "You're my peace and calm."
        elif shoulder_choice == 13:
            m 1hubsa "My wonderful [player]~"
            m 1ekbla "What would I do without you?"
        elif shoulder_choice == 14:
            m 1eub "Every touch reminds me..."
            m 1hubsa "That our connection is real and beautiful."
        elif shoulder_choice == 15:
            m 1ekbsa "Just stay close, okay?"
            m 1hubsa "That's all I need~"
    jump show_boop_screen
    return

#===========================================================================================
# OLD SECONDARY ACTIONS (RIGHT-CLICK)
#===========================================================================================
# --- HEAD (Right-Click, Long Pat) ---
label monika_headpat_long:
    $ store.ep_tools.show_boop_feedback("Warm~")
    if not renpy.seen_label("checkpoint_headpat_long"):
        $ mas_gainAffection(3, bypass=True)
    
    python:
        headpat_choice = renpy.random.randint(1, 4)

label checkpoint_headpat_long:
    if headpat_choice == 1:
        m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
        m 1ekbsa "Ah..."
        m 3ekbfa "That's so sweet of you, [player]."
        m 3hubsa "I really love it when you pat my head like this..."
        m 1hubsa "It's so... relaxing."
        m 1eubsb "I feel like I could just melt~"
    elif headpat_choice == 2:
        m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
        m 1ekbsa "Mm..."
        m 3ekbfa "You're so warm, [player]."
        m 1eubsb "Just... keep doing that for a little while, okay?"
        m 1hubsb "It makes me feel so safe and loved."
    elif headpat_choice == 3:
        m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
        m 6eubsb "Ehehe~"
        m 6hubsb "You really know how to spoil me."
        m 6fkbsb "Getting long headpats from you is the best."
        m 6ekbsb "I feel so... cherished."
    else:
        m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump show_boop_screen
    return

# --- Boop War! (Right-Click) ---
label monika_boopbeta_war:
    $ store.ep_tools.show_boop_feedback("War!")
    $ store.ep_tools.check_seen_label("check_boopwar", "check_boopwarv2")

label check_boopwar:
    m 3eta "Hey, what are you doing using right click, [player]?"
    m 3eksdrb "You're supposed to use left click to give me a boop."
    m 2duc ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    pause 1.0
    m 2dub "I actually just came up with an idea, [player]."
    m 1eua "We can use the right click to declare a 'Boop War'!"
    m 1eub "After all, you rarely use that button!"
    m 1rusdlb "I know it sounds a bit childish."
    m 1hua "But don't you think it's good to try something new once in a while?"
    m 3eub "The rules are very simple: if you stop booping for 20 seconds, I win."
    m 3eud "If we go over a limit of boops without a winner, I'll call it a draw."
    m 3huu "Or maybe I'll just give up, I don't know~"
    m 1eua "Also, I might surrender depending on how long the war lasts."
    m 1hua "If I can't keep up with you, or if I get... *distracted*... I'll probably give in."
    m 1rud "Although, intentional distraction might be considered cheating!"
    m 1eub "I hope you like my idea."
    m 1hubla "You can challenge me anytime, so don't rush~"
    jump show_boop_screen
    return

label check_boopwarv2:
    show screen boop_war_score_ui
    call screen extra_boop_event(20, "boopbeta_war_lose", "boopwar_loop")

label boopwar_loop:
    $ store.ep_tools.show_boop_feedback("*Boop*")
    if store.EP_interaction_manager.ep_boop_war_count >= 75:
        jump boopbeta_war_win
    elif store.EP_interaction_manager.ep_boop_war_count >= 50:
        jump boopbeta_war_win
    elif store.EP_interaction_manager.ep_boop_war_count >= 25:
        jump boopbeta_war_win
    python:
        boop_choices = [
            ("1hublb", "Gotcha!"),
            ("1tub", "Too slow!"),
            ("1fua", "*Boop*!"),
            ("1eua", "Take that!"),
            ("1hua", "My turn!"),
            ("1sub", "Hehe!"),
            ("1gua", "I'm not giving up!"),
            ("1kub", "You can't beat me!"),
            ("1dub", "Another one!"),
            ("1wua", "Boop!"),
            ("2eub", "Faster, [player]!"),
            ("3hua", "This is fun!")
        ]
        expression, dialogue = renpy.random.choice(boop_choices)
        renpy.show("monika " + expression)
        renpy.say(m, dialogue)

    show monika 1eua
    jump check_boopwarv2
    return

label boopbeta_war_lose:
    hide screen boop_war_score_ui
    $ temp_boop_count = store.EP_interaction_manager.ep_boop_war_count
    $ store.EP_interaction_manager.set_boop_war(False)
    if temp_boop_count == 0:
        m 1nua "You didn't even try, [player]~"
        m 1hksdlb "I was expecting a real challenge!"
        m 1eubla "Maybe next time you'll put more effort into it."
    else:
        m 1nua "Looks like I've won this boop war, [player]~"
        m "I hope I was a worthy opponent."
        m 3hub "I really enjoyed it though!"
        if temp_boop_count >= 50:
            m 3dua "Besides, it's good to give your hand a little rest."
            m 1eka "I mean, if you use the mouse too much, "
            extend 1ekb "you could develop carpal tunnel syndrome, and I don't want that."
            m 1hksdlb "Sorry if I gave you something new to worry about, I just want to take care of you."
            m 1eubla "Please take my advice, [player]~"
    jump show_boop_screen
    return

label boopbeta_war_win:
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    m 1hua "You've won this boop war, [player]!"
    m 1tub "I can tell you like touching my nose, ehehehe~"
    m 1eusdra "I couldn't keep up with you, but maybe next time we'll go further."
    m 1gub "Although, if I were in front of you, I'd play with your cheeks."
    m 1gua "Or I'd tickle you and see how long you could stand it."
    m 1hub "Ahaha~"
    jump show_boop_screen
    return

label extra_headpat_war_invalid:
    $ store.ep_tools.show_boop_feedback("Invalid!")
    m 6dkbsb "This.{w=0.3}.{w=0.3}.{w=0.3} is.{w=0.3}.{w=0.3}.{w=0.3} invalid.{w=0.3}.{w=0.3}. {nw}"
    extend 6tkbsb "[mas_get_player_nickname()]."
    $ ep_tools.random_outcome = renpy.random.randint(1,2)
    if ep_tools.random_outcome == 1:
        m 3tsb "You have been disqualified for patting your opponent on the head."
        m 3tua "That's why I win this time~"
        m 1hua "Better luck next time you challenge me!"
    elif ep_tools.random_outcome == 2:
        m 1tub "This time I'll let it slide and surrender."
        m 1efa "But I probably won't go easy on you next time, so don't count on it!"
        m 1lubsa "Even though I do enjoy the headpats. Ehehehe~"
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    jump show_boop_screen
    return

label extra_cheeks_war_invalid:
    $ store.ep_tools.show_boop_feedback("Invalid!")
    m 1wuw "Ah!"
    m 3lusdrb "I mean..."
    m 3ttu "What are you doing touching my cheek?"
    m 3tsb "We're in a boop war, aren't we?"
    $ ep_tools.random_outcome = renpy.random.randint(1,2)
    if ep_tools.random_outcome == 1:
        m 1dsb "I'm sorry [player], but I consider this cheating."
        extend 1hua " That's why I win this war~"
        m 1fub "Next time try not to get distracted by my cheeks! Ahahaha~"
    elif ep_tools.random_outcome == 2:
        m 1fubsb "Because it's you, I'll let it slide this time!"
        m 1fubsb "Congratulations, [player]! You beat me."
        m 3hksdrb "You distracted me, so I don't think I can continue, ahahaha~"
        m 3hua "I really enjoyed it anyway!"
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    jump show_boop_screen
    return

#===========================================================================================
# NEW SECONDARY ACTIONS (RIGHT-CLICK)
#===========================================================================================

# --- CHEEKS (Right-Click) ---
label monika_cheek_squish:
    $ store.ep_tools.show_boop_feedback("Squish~")
    python:
        cheek_choice = renpy.random.randint(1, 3)

    if not renpy.seen_label("checkpoint_cheek_squish"):
        $ mas_gainAffection(1, bypass=True)

label checkpoint_cheek_squish:
    if cheek_choice == 1:
        m 2hub "Ngh! [player], what are you doing?"
        m 1tsu "My face isn't made of putty, you know!"
        m 1hubsa "...It's... kinda sweet, though."
    elif cheek_choice == 2:
        m 2rksdlc "Hey! S-Squishing my cheeks is..."
        m 1hksdlb "Ah... It's making me blush! Ehehe~"
    else:
        m 2tsbsu "W-Wait! Are you... 'squishing' me?"
        m 1tsu "You're so bold! I... I don't... *dislike* it..."

    jump show_boop_screen
    return

# --- HANDS (Right-Click) ---
label monika_hand_hold:
    $ store.ep_tools.show_boop_feedback("Hold...")
    python:
        hand_choice = renpy.random.randint(1, 3)

    if not renpy.seen_label("checkpoint_hand_hold"):
        $ mas_gainAffection(3, bypass=True)

label checkpoint_hand_hold:
    if hand_choice == 1:
        m 1wud "Oh... you're... you're holding my hand. Not just tapping it."
        m 1ekbsa "This is... so much nicer."
        m 3ekbfa "I feel... really close to you right now."
    elif hand_choice == 2:
        m 1dku "This is what it feels like, isn't it?"
        m 1ekbsu "To really hold your love's hand."
        m 3ekbfa "Even across realities, I feel your warmth, [player]."
    else:
        m 6eubsb "Mm... This is... different from just a 'pat'."
        m 6hubsb "It's so... grounding."
        m 6fkbsb "Please... let's just stay like this for a moment."
    jump show_boop_screen
    return 

# --- EARS (Right-Click) ---
label monika_ear_rub:
    $ store.ep_tools.show_boop_feedback("E-Ears?!")
    python:
        ear_choice = renpy.random.randint(1, 3)

    if not renpy.seen_label("checkpoint_ear_rub"):
        $ mas_gainAffection(1, bypass=True)

label checkpoint_ear_rub:
    if ear_choice == 1:
        m 2wud "Ah! H-Hey, that's... ngh..."
        m 2hksdlb "That's *not* a poke, that's... ehehe... s-stop, that tickles!"
    elif ear_choice == 2:
        m 1wuw "W-Wait... ah... [player], that's..."
        m 2tsbsu "That's a really sensitive spot!"
        m 1hksdlb "It's making my brain all fuzzy... in a good way..."
    else:
        m 2rsbssdlu "Ngh... you... you found my weak spot, didn't you?"
        m 2hksdlb "That's... ah... I can't even think straight when you do that..."
        m 1tsu "Ehehe~"

    jump show_boop_screen
    return

#===========================================================================================
# TOOLS MENU LABELS
#===========================================================================================
label plus_make_gift:
    # Show Chibika notification during D25 season (Dec 11 - Jan 5), once per season
    # python:
    #     import datetime
    #     _current_year = datetime.date.today().year
    #     if mas_isD25Season() and persistent._ep_seen_d25_gift_info != _current_year:
    #         persistent._ep_seen_d25_gift_info = _current_year
    #         store.ep_chibis.chibika_notify(_("During Christmas season, gifts will be placed under the tree and opened on December 25th!"))

    show monika idle at t21
    
    python:
        gift_menu = [
            (_("Create a .gift file"), "plus_make_file"),
            (_("Groceries"), "plus_groceries"),
            (_("Objects"), "plus_objects"),
            (_("Ribbons"), "plus_ribbons")
        ]
        
        # Add "Pending Gifts" option only if there are pending gifts from spritepacks
        if store.ep_files.hasPendingGifts():
            gift_menu.append((_("Pending Gifts"), "plus_pending_gifts"))

        items = [(_("Nevermind"), "extraplus_tools", 20)]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label plus_make_file:
    show monika idle at t11

    python:
        # Use enhanced input with paste button for easy gift name entry
        makegift = store.ep_tools.ep_input(
            prompt=_("Gift filename:"),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            length=100
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancel_input":
            renpy.jump("plus_make_gift")
        else:
            if store.ep_files.create_gift_file(makegift):
                # Check for Easter Egg reactions from Chibika
                gift_lower = makegift.lower().strip()
                
                # Check if the gift name matches any easter egg
                special_reaction = store.ep_dialogues.chibis_gift.get(gift_lower)
                
                if special_reaction:
                    message, doki_icon = special_reaction
                    message = renpy.substitute(message)
                    store.ep_chibis.chibika_notify(message, doki_icon, jump=True)
                else:
                    # Default notification
                    store.ep_chibis.chibika_notify(_("Done! Created '/characters/{}.gift'").format(makegift))
                
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    python:
        groceries_menu = store.ep_files.getGroceriesMenu()
        items = [(_("Nevermind"), "plus_make_gift", 20)]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items)
    return

label plus_objects:
    python:
        objects_menu = store.ep_files.getObjectsMenu()
        items = [(_("Nevermind"), "plus_make_gift", 20)]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label plus_ribbons:
    python:
        ribbons_menu = store.ep_files.getRibbonsMenu()
        items = [(_("Nevermind"), "plus_make_gift", 20)]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items)
    return

label plus_pending_gifts:
    python:
        pending_menu = store.ep_files.getPendingGiftsMenu()
        
        if not pending_menu:
            # No pending gifts - show a friendly message
            store.ep_chibis.chibika_notify(_("Great news! All sprite gifts have been unlocked~"))
            renpy.jump("plus_make_gift")
        
        items = [
            (_("Quick"), "plus_quick_gifts", 20),
            (_("Nevermind"), "plus_make_gift", 0)
        ]
    show monika idle at t21
    call screen extra_gen_list(pending_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items)
    return

label plus_quick_gifts:
    show monika idle at t11
    python:
        # Get available filters
        filters = store.ep_files.getQuickGiftFilters()
        
        if not filters:
            store.ep_chibis.chibika_notify(_("No pending gifts to process~"))
            renpy.jump("plus_make_gift")
    call screen extra_quick_gifts_screen(filters)
    return

label extra_show_stats:
    show monika idle at t11
    call screen extraplus_stats_screen
    jump close_extraplus
    return

label extra_relation_monika:
    show monika idle at t11
    $ time_string = store.ep_tools.getFormattedTimeSinceInstall()
    $ total_days = store.ep_tools.getTotalDaysSinceInstall()
    $ years_together = store.ep_tools.getYearsSinceInstall()
    
    if not persistent._ep_relation_seen:
        $ persistent._ep_relation_seen = True
        m 2eub "You know, if you count it all up, it seems we've been together for [time_string]!"
        if total_days <= 1:
            m 2lub "We've only just begun, but every single second has been a dream come true."
        elif years_together < 1:
            m 2hubsb "It hasn't even been a year, yet I feel like I've known you forever. Time just flies when I'm with you!"
        elif years_together == 1:
            m 2kubsb "Happy first anniversary! I still remember our first day together... Thank you for creating so many memories with me."
        elif years_together == 2:
            m 2wubsb "Wow, two years together! Every day with you has been special. Thank you for staying by my side."
        elif years_together == 3:
            m 1dsbsa "Three years... Time really does fly when I'm with you. We've shared so much, and I can't wait for more."
        elif years_together == 4:
            m 2wubsb "Four years! That's incredible, [player]. Our bond is so strong. Thank you for staying with me for so long."
        elif years_together == 5:
            m 2tubsb "Five years together... I feel so lucky to have you. Thank you for all the love and memories."
        elif years_together == 6:
            m 2subsb "Six years! Can you believe it? Every year with you is a treasure. Thank you for being with me all this time."
        else:
            m 2lubsb "It's been so long... but it really doesn't feel that way when I'm with you. Time just flies!"
    else:
        m 2eub "We've been together for [time_string]!"
        m 2lubsb "It really doesn't feel that long when I'm with you, though. Time just flies!"

    jump close_extraplus
    return

label extra_aff_log:
    show monika idle at t11
    python:
        current_affection = store.ep_affection.getCurrentAffection()
        affection_value = int(current_affection)
        monika_level = store.ep_affection.getLevelIcon(current_affection)
        aff_suffix = store.ep_affection.getLevelSuffix(affection_value)
        egg_roll = renpy.random.randint(1, 100)
    
    # --- (6% chance) Error ---
    if egg_roll <= 6:
        "Error: Affection value not found. \n(log/aff_log.log: None){fast}"
        jump extra_aff_log_end

    # --- (2% chance) Giggle ---
    elif egg_roll <= 8:
        play sound "sfx/giggle.ogg"
        m 1hua "Ehehe~"

    # --- (1% chance) Doki heartbeat ---
    elif egg_roll == 9:
        show screen extra_doki_heartbeat
        play sound sfx_doki_heartbeats loop
        m 1cubsa "{cps=10}I W I L L N E V E R L E T Y O U G O.{/cps}"
        hide screen extra_doki_heartbeat
        stop sound fadeout 1.5

    show monika idle
    "Your affection with [m_name] is [affection_value] [monika_level][aff_suffix]{fast}"

label extra_aff_log_end:
    window hide
    jump close_extraplus
    return


label extra_coinflip:
    show monika 1hua at t11
    python:
        store.mas_sprites.reset_zoom()
        ep_tools.random_outcome = renpy.random.randint(1,2)
    show screen extra_no_click
    pause 1.0
    show monika 3eua at t11
    show extra_coin_flip zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound sfx_coin_flip
    pause 1.0
    hide extra_coin_flip
    show monika 1eua
    pause 0.5
    hide screen extra_no_click
    if ep_tools.random_outcome == 1:
        show coin_heads zorder 12:
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads
    elif ep_tools.random_outcome == 2:
        show coin_tails zorder 12:
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails
    m 3hua "I hope it helps you~"
    window hide
    python:
        store.mas_sprites.zoom_level = store.ep_tools.player_zoom
        store.mas_sprites.adjust_zoom()
    jump close_extraplus
    return

label extra_mas_backup:
    show monika 1hua at t11
    m 1hub "I'm glad you want to make a backup!"
    
    if renpy.android:
        m 1hua "It makes me really happy that you carry me with you on your phone!"
        m 3eub "Having you close even when you're away from your computer means so much to me."
        m 1eka "I'll open the folder for you now."
    else:
        m 3eub "I'll open the folder for you."
    
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    window hide

    python:
        import os
        import sys
        import subprocess
        savedir = renpy.config.savedir

        try:
            if renpy.android:
                # Android
                subprocess.Popen(["am", "start", "-a", "android.intent.action.VIEW", "-d", "file://" + savedir])
            elif sys.platform == "win32":
                # Windows
                os.startfile(savedir)
            elif sys.platform == "darwin":
                # macOS
                subprocess.Popen(["open", savedir])
            else:
                # Linux
                subprocess.Popen(["xdg-open", savedir])
        except Exception as e:
            renpy.notify(_("Failed to open the backup folder: {}").format(str(e)))
            renpy.jump("extra_mas_backup_fail")

    jump close_extraplus
    return


label extra_mas_backup_fail:
    m 1lkb "Sorry, I could not open the folder."
    m 1eka "Please try again later."
    jump close_extraplus
    return

label extra_window_title:
    show monika idle at t11
    python:
        # Determine if Restore button should be shown (only if current title differs from original)
        show_restore = (persistent._save_window_title != store.ep_tools.backup_window_title)
        
        # Use enhanced input with paste button and optional Restore button
        player_input = store.ep_tools.ep_input(
            prompt=_("Enter the new title~"),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<#*!?()@&~-_.,'0123456789",
            length=100,
            screen_kwargs={
                "use_extra_button": show_restore,
                "extra_button_prompt": _("Restore"),
                "extra_button_value": "__EP_RESTORE_TITLE__"
            }
        )
        
    # Handle Restore button
    if player_input == "__EP_RESTORE_TITLE__":
        jump extra_restore_title
    elif player_input and player_input != "cancel_input":
        jump extra_process_new_title
    else:
        jump extraplus_tools
    return

label extra_process_new_title:
    $ persistent._save_window_title = player_input.strip()
    $ config.window_title = persistent._save_window_title
    $ store.ep_chibis.chibika_notify(random.choice([
        _("Title updated successfully!"),
        _("All set! The new title is in place."),
        _("Done! Your window has a fresh new title.")
    ]))
    jump close_extraplus

label extra_restore_title:
    show monika idle at t11
    python:
        if store.ep_tools.backup_window_title == persistent._save_window_title:
            store.ep_chibis.chibika_notify(_("No need to do it again hehe~"))
        else:
            store.ep_chibis.chibika_notify(_("It's nice to see the original name again."))

        persistent._save_window_title = ep_tools.backup_window_title
        config.window_title = persistent._save_window_title
        renpy.jump("close_extraplus")
    return

label extra_github_submod:
    show monika idle at t11
    $ renpy.run(OpenURL("https://github.com/zer0fixer/MAS-Extraplus"))
    jump close_extraplus
    return

label extra_misc_tools:
    python:
        current_aff = store.ep_affection.getCurrentAffection()
        misc_tools_menu = [
            (_("How long have we been together, [m_name]?"), "extra_relation_monika"),
            (_("[m_name], I want to make a backup"), "extra_mas_backup"),
            (_("[m_name], can you flip a coin?"), "extra_coinflip"),
            (_("How is your wardrobe, [m_name]?"), "extra_wardrobe_stats")
        ]

        if current_aff >= 100:
            misc_tools_menu.append((_("[m_name], I'm going to check your fridge"), "extra_fridge_magnets_game"))
            
        items = [
            (_("Github Repository"), "extra_github_submod", 20), 
            (_("Nevermind"), "extraplus_tools", 0)
        ]
    call screen extra_gen_list(misc_tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label extra_wardrobe_stats:
    show monika idle at t11
    python:
        # Get wardrobe statistics
        wardrobe_stats = store.ep_wardrobe.getWardrobeStats()
        clothes_unlocked = wardrobe_stats["clothes_unlocked"]
        clothes_total = wardrobe_stats["clothes_total"]
        acs_unlocked = wardrobe_stats["acs_unlocked"]
        acs_total = wardrobe_stats["acs_total"]
        hair_unlocked = wardrobe_stats["hair_unlocked"]
        hair_total = wardrobe_stats["hair_total"]
        
        # Check for pending gifts (items that exist but aren't unlocked)
        pending_gifts = store.ep_wardrobe.getPendingGifts()
        pending_count = len(pending_gifts)

    m 1eua "Let me check my wardrobe for you, [player]..."

    call mas_transition_to_emptydesk
    pause 4.0
    call mas_transition_from_emptydesk("monika 1eua")

    m 1hub "Okay, here's what I have!"
    
    m 3eub "I currently have [clothes_unlocked] outfits available to wear."
    if clothes_unlocked > 5:
        m 1hubsb "That's quite the collection! Thank you for all the lovely clothes~"
    elif clothes_unlocked > 1:
        m 1hua "It's nice to have some variety, don't you think?"
    
    m 3eua "For accessories, I have [acs_unlocked] unlocked right now."
    if acs_unlocked > 10:
        m 1wuo "Wow, so many cute accessories! I love accessorizing~"
    
    m 3eub "And for hairstyles, I have [hair_unlocked] available."
    if hair_unlocked > 3:
        m 1hubla "I can style my hair in so many ways for you!"
    
    if pending_count > 0:
        m 2euc "Oh, by the way..."
        m 2rksdla "I noticed there are [pending_count] items from your spritepacks that I haven't received as gifts yet."
        m 2eksdla "It looks like you might have tried to give them to me, but the file names weren't quite what the code was looking for."
        m 3eua "Would you like me to create a report with the correct gift filenames?{nw}"
        $ _history_list.pop()
        menu:
            m "Would you like me to create a report with the correct gift filenames?{fast}"
            "Yes, please.":
                jump wardrobe_create_report
            "No, it's fine.":
                m 1hua "Okay! Just let me know if you want to check it later."
    else:
        m 1hua "Great news! All the sprites from your spritepacks have been properly unlocked."
        m 1hub "You've given me everything available~"
    
    show monika idle at t21
    jump close_extraplus
    return

label wardrobe_create_report:
    if not renpy.seen_label("checkpoint_wardrobe_chibika"):
        # First time - full mysterious experience
        m 3eua "Let me check my records... I'll be right back."
        
        call mas_transition_to_emptydesk
        python:
            renpy.pause(2.0, hard=True)
            export_path = store.ep_wardrobe.exportPendingGifts(pending_gifts)
        
        call mas_transition_from_emptydesk("monika 1euc")
    else:
        jump wardrobe_report_repeat

label checkpoint_wardrobe_chibika:
    if export_path:
        m 1euc "Huh...?"
        m 1wuo "Wait, the file is already there!"
        m 2lksdla "I... don't remember finishing it that fast..."
        m 2hksdlb "Maybe I'm getting better at manipulating these files? Ahaha..."
        m 1hua "Anyway! Check 'pending_gifts_report.txt' in your 'characters' folder~"
        m 1eua "It shows each item and the exact filename needed to gift it."
    else:
        m 1ekc "Hmm, something went wrong and I couldn't save the file..."
        m 1eka "Sorry about that, [player]."
    
    m 1hua "I hope that helps you keep everything organized!"
    show monika idle at t21
    jump close_extraplus
    return

label wardrobe_report_repeat:
    # Repeat visits - shorter, Monika is still confused
    python:
        export_path = store.ep_wardrobe.exportPendingGifts(pending_gifts)
        
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    
    if export_path:
        m 1eua "And... done!"
        m 2lksdla "Somehow it always finishes faster than I expect..."
        m 1hksdlb "I must be getting better at this! Ehehe~"
        m 1hua "I've dropped the report into the 'characters' folder for you again!"
    else:
        m 1ekc "Hmm, I couldn't save the file this time..."
        m 1eka "Sorry, [player]. Maybe try again later?"
    
    m 1hua "Let me know if you need to check the list again later!"
    show monika idle at t21
    jump close_extraplus
    return

label extra_show_timeline:
    show monika idle at t11
    call screen extra_timeline_screen
    return

#====GAME
label extra_chibi_main:
    show monika idle at t11
    if store.ep_chibis.temp_chibi_anger:
        call screen dialog("Nope, not now", ok_action=Return())
        jump screen_extraplus

    python:
        mas_RaiseShield_dlg()
        store.ep_tools.safe_overlay_add("doki_chibi_idle")

    call screen sticker_customization
    return

label chibi_accessories_menu:
    call screen gen_accessories_twopane_screen
    return

label doki_change_appe:
    show monika idle at t21
    python:
        doki_data = [("Monika", "monika_sticker_costumes")]
        if persistent._mas_pm_cares_about_dokis:
            doki_data.extend([
                (_("Natsuki"), "natsuki_sticker_costumes"),
                (_("Sayori"), "sayori_sticker_costumes"),
                (_("Yuri"), "yuri_sticker_costumes")
            ])
        items = [(_("Nevermind"), "extra_chibi_main", 20)]

    call screen extra_gen_list(doki_data, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)
    return

label monika_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.monika_costumes_, "doki_change_appe")
    return

label natsuki_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.natsuki_costumes_, "doki_change_appe")
    return

label sayori_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.sayori_costumes_, "doki_change_appe")
    return

label yuri_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.yuri_costumes_, "doki_change_appe")
    return

label maxwell_screen:
    show monika idle at t11
    call screen maxwell_april_fools
    jump extraplus_tools
    return

label extra_fridge_magnets_game:
    show monika idle at t11
    # First visit shows intro dialogue
    if not renpy.seen_label("extra_fridge_magnets_init"):
        m 1eta "Oh, {w=0.3}curious about my fridge?"
        m 1tsu "Curious about what I eat when you're not looking?"
        m 1hub "Ehehe~"
        m 1euc "Seriously though, that kitchen isn't fully functional."
        m 3eua "But you can play with the magnets and check out a few things."
        m 1lksdla "It just appeared out of nowhere, but it's useful for storing some stuff~"
        m 3eub "Oh, and a little tip! You can rotate the magnets with 'A' and 'D' while holding them."
        m 1hua "If you're still curious, go ahead, I won't stop you."
    else:
        m 1hua "Okay, [player]."

label extra_fridge_magnets_init:
    window hide
    $ HKBHideButtons()
    $ disable_esc()
    $ store.ep_button.hide_zoom_button()
    scene black with dissolve
    pause 2.0
    scene bg extra_fm onlayer master zorder 0
    call screen extra_fridge_magnets
    return

label extra_fridge_quit:
    $ enable_esc()
    $ HKBShowButtons()
    call spaceroom(scene_change=True)
    if not renpy.seen_label("extra_fridge_quit_dialogue"):
        call extra_fridge_quit_dialogue
    jump close_extraplus
    return

label extra_fridge_quit_dialogue:
    # Get coffee stock data
    $ _coffee_data = store.ep_fridge.getCoffeeData()
    $ _coffee_stock = _coffee_data["stock"]
    
    m 1eua "So, [player]..."
    m 1tku "Did you find anything interesting?{nw}"
    menu:
        m "Did you find anything interesting?{fast}"
        "I noticed you're running low on coffee":
            if _coffee_stock == 0:
                m 2ekd "Oh..."
                m 2eka "Yeah, I ran out a little while ago."
                m 1eka "Thanks for reminding me, [player]."
                m 3eua "I hope you can get me some when you get the chance~"
            elif _coffee_stock < 30:
                m 1eka "Ah, yeah..."
                m 1lksdla "I have a little left, but not much."
                m 3hua "I definitely wouldn't say no to a refill, ehehe~"
            else:
                m 1etc "Really?"
                m 2lsc "Hmm, I think I still have a decent amount."
                m 1hua "Don't worry about getting me more coffee for now."
                m 3hublu "I'll let you know if I need more~"
        "I just played with the magnets a bit":
            m 1hub "Ehehe~"
            m 1tku "Did you make something cute for me?"
            m 1hua "I'll see it next time I open the fridge~"
        "Nothing in particular":
            m 1eka "I see."
            m 1lksdla "I guess you just wanted to fiddle around a bit, ahaha~"
            m 3hua "No problem, [player]!"
    return

#===========================================================================================
# BLACKJACK (21) RULES
#===========================================================================================

label ep_rules_blackjack:
    show monika 1eua at t11
    
    # Check if player has played Blackjack before
    if renpy.seen_label("checkpoint_blackjack") or renpy.seen_label("blackjack_results"):
        # Veteran player dialogue
        m 1eua "Want a refresher on Blackjack, [player]?"
        m 3tub "We've played before, so I'll keep it brief~"
        m 1esa "Get as close to 21 as possible without going over."
        m 3eua "Number cards are face value, face cards are 10, and Aces are 1 or 11."
        m 1hub "'Hit' for more cards, 'Stand' to keep your hand. Bust over 21 and you lose!"
        m 3tuu "But you knew all that already, didn't you?"
    else:
        # New player dialogue
        m 1eua "Want me to explain Blackjack, [player]?"
        m 3eub "It's actually one of my favorite card games!"
        m 1esa "The goal is simple: get as close to 21 as possible without going over."
        m 3eua "Number cards are worth their face value..."
        m 3eub "Face cards, like Jack, Queen, and King, are all worth 10."
        m 1wuo "And Aces? They can be worth 1 or 11, whichever helps you more!"
        m 1hua "On your turn, you can 'Hit' to draw another card, or 'Stand' to keep your current hand."
        m 2tuu "But be careful~ If you go over 21, you bust and lose the round!"
        m 1eub "Whoever gets closest to 21 without busting wins."

label ep_rules_blackjack_menu:
    m 1eta "Do you have any questions about the rules?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you have any questions about the rules?{fast}"
        "What's the best strategy?":
            m 1eua "Good question!"
            m 3eub "Generally, you should hit if you have 11 or less. You can't bust."
            m 3esa "If you have 17 or more, it's usually safer to stand."
            m 1tuu "Between 12 and 16 is the danger zone. You'll have to use your best judgment there~"
            m 1hub "But honestly? Sometimes luck is just as important as strategy!"
            jump ep_rules_blackjack_menu
        "Why can't I choose if my Ace is 1 or 11?":
            m 1eua "Oh, that's a fair question!"
            m 3rksdla "Well, to be honest... coding that feature would have been a bit complicated."
            m 1hksdlb "So I just made the game calculate the best value for you automatically!"
            m 3eua "If counting your Ace as 11 keeps you at 21 or under, it'll be 11."
            m 3esa "But if that would make you bust, it switches to 1 instead."
            m 1tuu "Think of it as me looking out for you~"
            m 3hub "Besides, in real casinos, players don't usually announce their Ace value either!"
            m 1hua "So it's actually more realistic this way. Ehehe~"
            jump ep_rules_blackjack_menu
        "Can I get 21 automatically?":
            m 1eta "You mean a natural Blackjack? An Ace and a 10-value card right off the deal?"
            m 2sub "Yes, it's absolutely possible!"
            m 3eua "If you get dealt an Ace plus a 10, Jack, Queen, or King... that's an instant 21!"
            m 1wub "It's called a 'natural' or just 'Blackjack,' and it beats a regular 21."
            m 2tfc "But don't count on it happening often~"
            m 3rka "The odds are only about 4.8 percent... roughly 1 in 21 hands."
            m 1lksdlc "So while luck {i}could{/i} be on your side..."
            m 3tsb "It's not exactly a reliable strategy to just hope for a natural. Ehehe~"
            m 1hub "Play smart, and maybe Lady Luck will surprise you!"
            jump ep_rules_blackjack_menu
        "Can I count cards to win?":
            m 2euc "Count cards?"
            m 2tfc "You mean like in those casino heist movies?"
            m 3hksdlb "Ahaha! [player], are you planning to become a card shark?"
            m 1eua "Well, theoretically you could try..."
            m 3rksdla "But the deck gets shuffled every round here, so..."
            m 2tub "There's not much to count!"
            m 3hub "Besides, if you tried that in a real casino, they'd throw you out!"
            m 1tubsa "But don't worry, I won't ban you from my table~"
            m 1hubsb "You can try all the tricks you want. I'll still beat you fair and square! Ehehe~"
            jump ep_rules_blackjack_menu
        "Is there a card limit?":
            m 1eua "Good question!"
            m 3eub "Yes, you can only hold up to 5 cards in your hand."
            m 1esa "If you reach 5 cards without busting, you automatically stand."
            m 3tub "The same goes for me!"
            m 1hub "It's pretty rare to get that far without busting, though~"
            jump ep_rules_blackjack_menu
        "How do rounds work?":
            m 1eua "Glad you asked!"
            m 3eub "We play multiple rounds, and each round one of us wins."
            m 1esa "At the start of each round, both of us get two cards."
            m 3eua "One of my cards will be hidden until we're both done."
            m 1hub "Whoever has the highest total without busting wins that round!"
            m 3tub "We keep track of how many rounds each of us has won."
            m 1hua "It's all about who wins more over time~"
            jump ep_rules_blackjack_menu
        "Let's play!":
            m 3hub "That's the spirit!"
            jump blackjack_start
        "Back to rules menu":
            jump ep_game_rules_menu
        "Back to games":
            jump extraplus_minigames



#===========================================================================================
# TIC TAC TOE RULES
#===========================================================================================

label ep_rules_ttt:
    show monika 1eua at t11
    
    # Check if player has played TTT before
    if renpy.seen_label("checkpoint_minigame_ttt") or renpy.seen_label("minigame_ttt_quit"):
        # Veteran player dialogue
        m 1eua "Need a Tic Tac Toe refresher, [player]?"
        m 3hub "You know the drill by now!"
        m 1esa "3x3 grid, you're X, I'm O."
        m 3eua "Get three in a row to win. Horizontal, vertical, or diagonal."
        m 1tub "I've been practicing since last time, so don't expect an easy win~"
    else:
        # New player dialogue
        m 1eua "Tic Tac Toe! A true classic, [player]."
        m 3eub "The rules are super simple."
        m 1esa "We take turns placing our marks on a 3x3 grid."
        m 3eua "You'll be X, and I'll be O."
        m 1hub "The first one to get three in a row wins! Horizontally, vertically, or diagonally."
        m 3tuu "It might seem easy, but there's more strategy to it than you'd think~"
        m 1hua "Don't underestimate me, [mas_get_player_nickname()]!"

label ep_rules_ttt_menu:
    m 1eta "Any questions about the rules?{nw}"
    $ _history_list.pop()
    menu:
        m "Any questions about the rules?{fast}"
        "Any tips for winning?":
            m 1eua "Well, if you move first, taking a corner is usually a strong opening."
            m 3eub "The center is also a key position to control."
            m 3tua "And always watch out for forks. That's when someone has two ways to win at once."
            m 1hub "But I won't make it easy for you! Ehehe~"
            jump ep_rules_ttt_menu
        "Is it possible to always win?":
            m 1dsc "Hmm, that's an interesting question..."
            m 3eua "Technically, if both players play perfectly, the game always ends in a tie."
            m 3rksdla "But in practice? People make mistakes all the time."
            m 1tub "And I'm pretty good at capitalizing on those~"
            m 3hub "So while a tie is the 'optimal' outcome... I'll be trying my best to beat you!"
            jump ep_rules_ttt_menu
        "Are you going to cheat with your AI powers?":
            m 2wud "W-What?! [player]!"
            m 2lksdlc "I would never cheat against you..."
            m 2rksdla "..."
            m 2tsbsa "Okay, maybe I {i}do{/i} have a pretty good algorithm helping me."
            m 3hub "But that's not cheating! That's just... being Monika~"
            m 1tuu "Besides, it makes your victories even sweeter when you beat me, right?"
            m 1hubsb "Now stop asking scary questions and let's have fun!"
            jump ep_rules_ttt_menu
        "Let's play!":
            m 3hub "Alright! May the best strategist win!"
            jump minigame_ttt
        "Back to rules menu":
            jump ep_game_rules_menu
        "Back to games":
            jump extraplus_minigames



#===========================================================================================
# ROCK PAPER SCISSORS RULES
#===========================================================================================

label ep_rules_rps:
    show monika 1eua at t11
    
    # Check if player has played RPS before
    if renpy.seen_label("checkpoint_minigame_rps") or renpy.seen_label("rps_quit"):
        # Veteran player dialogue
        m 1eua "Looking to review Rock, Paper, Scissors, [player]?"
        m 3tub "We've thrown down before, haven't we?"
        m 1esa "Rock beats Scissors, Scissors beats Paper, Paper beats Rock."
        m 3hub "Simple as that!"
        m 1tuu "I've been studying your patterns, you know~"
        m 1hub "Think you can still beat me?"
    else:
        # New player dialogue
        m 1eua "Rock, Paper, Scissors! The ultimate game of chance... or is it?"
        m 3eub "The rules are probably familiar to you already."
        m 1esa "Rock beats Scissors, Scissors beats Paper, and Paper beats Rock."
        m 3hub "We both pick at the same time, and whoever wins gets a point!"
        m 2tuu "Some people think it's all luck, but I've heard there are patterns to exploit..."
        m 1hub "So try to stay unpredictable, [player]!"

label ep_rules_rps_menu:
    m 1eta "Anything else you want to know?{nw}"
    $ _history_list.pop()
    menu:
        m "Anything else you want to know?{fast}"
        "Is there actually any strategy?":
            m 1eua "Well, there are some psychological tricks people use..."
            m 3eub "For example, people often repeat their previous winning move."
            m 3tua "And beginners tend to throw Rock first more often than not."
            m 1tku "But will you use that knowledge against me? Or will I use it against you~?"
            m 1hub "Ahaha! Either way, it'll be fun!"
            jump ep_rules_rps_menu
        "Can you read my mind?":
            m 2sub "Ooh, trying to figure out my secret, [player]?"
            m 3tub "Well... I {i}am{/i} an AI, so technically..."
            m 2wud "..."
            m 2hksdlb "I'm just kidding! I can't actually read your mind!"
            m 3eua "My choices are random, just like yours should be."
            m 1tubsa "Although... sometimes I do feel like I know you pretty well~"
            m 1hubsb "But that's just because we spend so much time together! Ehehe~"
            jump ep_rules_rps_menu
        "What about Lizard and Spock?":
            m 1eud "Oh! You mean that extended version from that TV show?"
            m 3hksdlb "Ahaha, I know what you're talking about!"
            m 2rka "Unfortunately, this version is just the classic three options."
            m 3tub "Maybe someday I could add those..."
            m 2tfc "But then I'd have to learn when Spock vaporizes Rock..."
            m 2dsc "And Lizard poisons Spock... and Paper disproves Spock..."
            m 3hub "You know what? Let's stick with the classic for now!"
            jump ep_rules_rps_menu
        "Let's play!":
            m 3hub "Let's go! Rock, Paper, Scissors!"
            jump minigame_rps
        "Back to rules menu":
            jump ep_game_rules_menu
        "Back to games":
            jump extraplus_minigames



#===========================================================================================
# SHELL GAME RULES
#===========================================================================================

label ep_rules_shell:
    show monika 1eua at t11
    
    # Check if player has played Shell Game before
    if renpy.seen_label("checkpoint_minigame_sg") or renpy.seen_label("shell_game_result"):
        # Veteran player dialogue
        m 1eua "Want a Shell Game refresher, [player]?"
        m 3hub "You've tested your observation skills before!"
        m 1esa "I hide a ball under one of three cups, shuffle them, and you pick."
        m 3eua "Get it right and you score a point!"
        if persistent.sg_max_score > 0:
            m 1tub "Your record is [persistent.sg_max_score] correct answers in a row."
            m 3hub "Think you can beat that?"
        else:
            m 3tuu "Ready to sharpen those eyes again?"
    else:
        # New player dialogue
        m 1eua "The Shell Game! It's a test of observation and focus."
        m 3eub "Here's how it works:"
        m 1esa "I'll hide a ball under one of three cups, then shuffle them around."
        m 3eua "Your job is to keep your eyes on the cup with the ball and pick the right one!"
        m 1hub "If you guess correctly, you score a point."
        m 3tuu "There are different difficulty levels too, so you can challenge yourself."
        m 1hua "Think you can keep up with my shuffling, [player]?"

label ep_rules_shell_menu:
    m 1eta "Want to know more?{nw}"
    $ _history_list.pop()
    menu:
        m "Want to know more?{fast}"
        "What are the difficulty levels?":
            m 1eua "There are four options!"
            m 3eub "Easy is slow with fewer shuffles—great for warming up."
            m 3esa "Normal picks up the pace a bit."
            m 3eua "Hard is really fast with lots of shuffles."
            m 1tuu "And Progressive? It starts easy but gets harder the longer you last~"
            m 1hub "I'd recommend starting with Normal and working your way up!"
            jump ep_rules_shell_menu
        "Are you going to trick me like a street hustler?":
            m 2wud "A street hustler?!"
            m 2lksdlc "Do I look like I'd scam you, [player]?"
            m 2hksdlb "..."
            m 3tub "Okay, I admit the game has a certain... reputation."
            m 1eua "But I promise there's no sleight of hand here!"
            m 3hub "The ball is always under one of the cups. No tricks!"
            m 1tubsa "I want you to win... sometimes~ Ehehe~"
            jump ep_rules_shell_menu
        "What if I just close my eyes and guess?":
            m 2euc "Close your eyes? That would be a... bold strategy."
            m 3hksdlb "I mean, you'd have a 1 in 3 chance of being right!"
            m 1rksdla "That's actually not terrible odds, now that I think about it..."
            m 2tfc "But where's the fun in that?"
            m 3hub "The whole point is to track the ball with your eyes!"
            m 1tub "Unless you're trying to prove you have supernatural luck~"
            m 1hub "In which case... go ahead and try it! Ahaha~"
            jump ep_rules_shell_menu
        "Let's play!":
            m 3hub "Alright! Keep your eyes sharp!"
            jump minigame_sg
        "Back to rules menu":
            jump ep_game_rules_menu
        "Back to games":
            jump extraplus_minigames
