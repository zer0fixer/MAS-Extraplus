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
    $ store.ep_button.hide_zoom_button()
    jump ch30_visual_skip
    return

label close_dev_extraplus:
    show monika idle at t11
    python:
        store.mas_DropShield_dlg()
    $ store.ep_button.hide_zoom_button()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose
    call screen boop_revamped
    return

label return_boop_screen:
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    $ store.ep_button.hide_zoom_button()
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
        store.ep_tools.manage_date_location(locate=False)
        store.ep_button.hide_zoom_button()
        store.HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        store.HKBShowButtons()
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
    call extra_location_init(submod_background_cafe, "extra_cafe_cakes", True)

label extra_restaurant_init:
    call extra_location_init(submod_background_restaurant, "extra_restaurant_cakes", True)

label ExtraPool_init:
    call extra_location_init(submod_background_extrapool, "to_pool_loop", False)
    return

label extra_cafe_leave:
    hide screen extra_timer_monika
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    $ ep_dates.stop_snike_time = False
    jump cafe_hide_acs

label extra_restaurant_leave:
    hide screen extra_timer_monika
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    $ ep_dates.stop_snike_time = False
    jump restaurant_hide_acs

label monika_boopcafe:
    show monika staticpose at t11
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
    show monika staticpose at t11
    if ep_dates.stop_snike_time and renpy.get_screen("extra_timer_monika"):
        hide screen extra_timer_monika
        jump monika_no_dessert

    call screen extra_dating_loop(ask="cafe_talk", label_boop="monika_boopcafe", boop_enable=True)
    return

label to_restaurant_loop:
    show monika staticpose at t11
    if ep_dates.stop_snike_time and renpy.get_screen("extra_timer_monika"):
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
        m 1sua "It tasted so sweet~"
    if monika_chr.is_wearing_acs(EP_acs_coffeecup):
        python:
            monika_chr.remove_acs(EP_acs_coffeecup)
            monika_chr.wear_acs(EP_acs_emptycup)
        m 3dub "Also, this coffee was also good."
    if ep_dates.dessert_player == True:
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
                m 1eubsb "I wait for you patiently~"
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
            (_("Cafe"), 'go_to_cafe'),
            (_("Restaurant"), 'go_to_restaurant'),
            (_("Pool"), "go_to_pool"),
            (_("Library"), "generic_date_dev"),
            (_("Arcade"), "generic_date_dev")
        ]

        m_talk = renpy.substitute(renpy.random.choice(ep_dialogues._dates))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), 'screen_extraplus', 20)]
    call screen extra_gen_list(ep_tools.walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extraplus_minigames:
    show monika idle at t21
    python:
        ep_tools.minigames_menu = [
            (_("Shell Game"), 'minigame_sg'),
            (_("Rock Paper Scissors"), 'minigame_rps'),
            (_("Tic Tac Toe"), 'minigame_ttt'),
            (_("Blackjack (21)"), 'blackjack_start')
        ]
        
        m_talk = renpy.substitute(renpy.random.choice(ep_dialogues._minigames))
        renpy.say(m, m_talk, interact=False)
        items = [(_("Nevermind"), 'screen_extraplus', 20)]
    
    call screen extra_gen_list(ep_tools.minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extraplus_tools:
    show monika idle at t21
    python:
        store.ep_tools.player_zoom = store.mas_sprites.zoom_level
        ep_tools.tools_menu = [
            (_("View [m_name]'s Affection"), 'extra_aff_log'),
            (_("Your MAS Journey"), 'extra_show_stats'),
            (_("Their story together"), "extra_show_timeline"),
            (_("Create a gift for [m_name]"), 'plus_make_gift'),
            (_("Change the window's title"), 'extra_window_title'),
            (_("Hi [player]!"), 'extra_dev_mode')

        ]

        items = [
            (_("Misc"), 'extra_misc_tools', 20),
            (_("Nevermind"), 'screen_extraplus', 0)
        ]
    call screen extra_gen_list(ep_tools.tools_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=True)
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

################################################################################
## BOOP
################################################################################
#====Boop count
default persistent.plus_boop = [0, 0, 0] #Nose, Cheeks, Headpat.
default persistent.extra_boop = [0, 0, 0] #Hands, Ears.

#====NOISE
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
    $ store.ep_tools.show_boop_feedback("Boop!")
    if persistent.plus_boop[0] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 1wud "Wait a minute..."
        m 1hka "I felt a little tingle."
        show screen force_mouse_move
        m 3hub "And here we have the responsible one!"
        m 3hua "Don't worry! I'll let go of your cursor."
        hide screen force_mouse_move
        m 1tub "You can move it again, sorry for stealing your cursor~"
        m 1etd "Also, I don't know how you did it, [mas_get_player_nickname()]. I don't remember seeing this in the code."
        m 1hub "Unless it was you!"
        m 1hub "What a good surprise I got today [player]~"
    elif persistent.plus_boop[0] == 2:
        m 1hub "What are you doing playing with my nose, [player]!"
        m 4eua "This is called a boop, right?"
        m 1hksdrb "Not that it bothers me, I just haven't gotten used to the feeling yet!"
        m 1hua "Ehehe~"
    elif persistent.plus_boop[0] == 3:
        m 1eublb "Can you do it again, [mas_get_player_nickname()]?"
        show monika 1hubla
        call screen extra_boop_event(10, "extra_boop_nop", "extra_boop_yep")
    elif persistent.plus_boop[0] == 4:
        m 1etbsa "Wouldn't it be nice to do it with your nose?"
        if persistent._mas_first_kiss:
            m 1kubsu "I'd give you a kiss while you do it~"
        else:
            m 1wubsb "I'd give you a hug while you do it!"
        m 1dubsu "I hope that when I get to your reality we can do it."
        m 1hua "Although, if you want to do it now, you'd have to put your nose close to the screen."
        m 1lksdlb "However someone might see you, making you nervous, and I don't want that to happen."
        m 1ekbsa "Besides, I get a little nervous too when you're around me."
        m 1hua "I'm sorry for suggesting that [player]~"
    elif persistent.plus_boop[0] == 5:
        m 1tuu "You're starting to like it here, huh?"
        m 3hub "I'm getting to know you more and more while we're here [player]~"
        m 3hub "And it's very lovely of you to do so!"
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
    # === Dialogues added in Beta 3 ===
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
        m 1rksdla "Here I just feel... well, a 'click'. But I imagine it, and that's enough."
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
        # === Dialogues added in Beta 3 ===
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
    $ store.ep_tools.show_boop_feedback("<3", color="#ff69b4")
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
    # === Dialogues added in Beta 3 ===
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
        # === Dialogues added in Beta 3 ===
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
    $ store.ep_tools.show_boop_feedback("Pat pat~", color="#90ee90")
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
        m 6hkbssdrb "[player] you are messing my hair."
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        extend 6dsbsb "never mind though~"
        m "I'll deal with that later."
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
    # === Dialogues added in Beta 3 ===
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
        # === Dialogues added in Beta 3 ===
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
    $ store.ep_tools.show_boop_feedback("Hehe~", color="#ffffff")
    $ persistent.extra_boop[0] += 1
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
    # === Dialogues added in Beta 3 ===
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
        # === Dialogues added in Beta 3 ===
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
    $ store.ep_tools.show_boop_feedback("Hey!", color="#add8e6")
    $ persistent.extra_boop[1] += 1
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
    # === Dialogues added in Beta 3 ===
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
        # === Dialogues added in Beta 3 ===
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

#===========================================================================================
# OLD SECONDARY ACTIONS (RIGHT-CLICK)
#===========================================================================================
# --- HEAD (Right-Click, Long Pat) ---
label monika_headpat_long:
    $ store.ep_tools.show_boop_feedback("Warm~")
    if not renpy.seen_label("monika_headpat_long"):
        $ mas_gainAffection(3, bypass=True)
    
    python:
        headpat_choice = renpy.random.randint(1, 4)
        
    if headpat_choice == 1:
        m 1ekbsa "Ah..."
        m 3ekbfa "That's so sweet of you, [player]."
        m 3hubsa "I really love it when you pat my head like this..."
        m 1hubsa "It's so... relaxing."
        m 1eubsb "I feel like I could just melt~"
    elif headpat_choice == 2:
        m 1ekbsa "Mm..."
        m 3ekbfa "You're so warm, [player]."
        m 1eubsb "Just... keep doing that for a little while, okay?"
        m 1hubsb "It makes me feel so safe and loved."
    elif headpat_choice == 3:
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
    m 2dub "I actually came up with an idea, [player]."
    m 1eua "We can use right click to declare a boop war."
    m 1eub "After all, you rarely use it!"
    m 1rusdlb "I know this proposal sounds rather childish."
    m 1hua "But don't you think it's good to do something new once in a while?"
    m 3eub "The rules are very simple, if I see an absence on your part for 20 seconds, I declare myself the winner."
    m 3eud "If we go over a limit of boops without seeing any winner, I'll take it as a draw."
    m 3huu "Or maybe I'll give up, I don't know~"
    m 1eua "And lastly, the way I surrender is because of the time elapsed during the war."
    m 1hua "Whenever I can't keep up with you or in case 'some distraction occurs'... Although I can consider it as cheating..."
    m 1rud "I'm likely to give up."
    m 1eub "I hope you like my idea."
    m 1hubla "You'll be able to do it any time so don't rush~"
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
        m "I hope I've been a good opponent."
        m 3hub "But I've also really enjoyed it!"
        if temp_boop_count >= 50:
            m 3dua "Besides, it's good to give your hand a little massage."
            m 1eka "I mean, if you use the mouse too much, "
            extend 1ekb "you can develop carpal tunnel syndrome and I don't want that."
            m 1hksdlb "I'm sorry if I've added a new concern, but my intention is to take care of you."
            m 1eubla "I hope you take my recommendation, [player]~"
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
        m 1hua "Good luck for the next time you ask me for a war!"
    elif ep_tools.random_outcome == 2:
        m 1tub "This time I'll let it go and give up for you."
        m 1efa "But next time I probably won't give in, so don't bet on it!"
        m 1lubsa "Even though I enjoy the pat on the head. Ehehehe~"
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
        m 1dsb "I'm sorry [player], but I consider this cheating, "
        extend 1hua "that's why I win this war~"
        m 1fub "Next time try not to touch my cheek during the war! Ahahaha~"
    elif ep_tools.random_outcome == 2:
        m 1fubsb "Because it's you, this time I will let it go!"
        m 1fubsb "Congratulations, player! You have beat me."
        m 3hksdrb "You've distracted me and I don't think it's worth continuing, ahahaha~"
        m 3hua "I really enjoyed doing this with you though!"
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

    if not renpy.seen_label("monika_cheek_squish"):
        $ mas_gainAffection(1, bypass=True)
    jump show_boop_screen


# --- HANDS (Right-Click) ---
label monika_hand_hold:
    $ store.ep_tools.show_boop_feedback("Hold...")
    python:
        hand_choice = renpy.random.randint(1, 3)

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

    if not renpy.seen_label("monika_hand_hold"):
        $ mas_gainAffection(3, bypass=True)
    jump show_boop_screen


# --- EARS (Right-Click) ---
label monika_ear_rub:
    $ store.ep_tools.show_boop_feedback("E-Ears?!")
    python:
        ear_choice = renpy.random.randint(1, 3)

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

    if not renpy.seen_label("monika_ear_rub"):
        $ mas_gainAffection(1, bypass=True)
    jump show_boop_screen

#===========================================================================================
# TOOLS MENU LABELS
#===========================================================================================
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
            if store.ep_files.create_gift_file(makegift):
                renpy.notify(_("Done! Created '/characters/{}.gift'").format(makegift))
                store.mas_checkReactions()
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    show monika idle at t21
    python:
        groceries_menu = [ # Using the new class from ep_files store
            store.ep_files.GiftAction(_("Coffee"), 'coffee'),
            store.ep_files.GiftAction(_("Chocolates"), 'chocolates'),
            store.ep_files.GiftAction(_("Cupcake"), 'cupcake'),
            store.ep_files.GiftAction(_("Fudge"), 'fudge'),
            store.ep_files.GiftAction(_("Hot Chocolate"), 'hotchocolate'),
            store.ep_files.GiftAction(_("Candy"), 'candy'),
            store.ep_files.GiftAction(_("Candy Canes"), 'candycane'),
            store.ep_files.GiftAction(_("Candy Corn"), 'candycorn'),
            store.ep_files.GiftAction(_("Christmas Cookies"), 'christmascookies')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=True)
    return

label plus_objects:
    show monika idle at t21
    python:
        objects_menu = [ # Using the new class from ep_files store
            store.ep_files.GiftAction(_("Promise Ring"), 'promisering'),
            store.ep_files.GiftAction(_("Roses"), 'roses'),
            store.ep_files.GiftAction(_("Quetzal Plushie"), 'quetzalplushie'),
            store.ep_files.GiftAction(_("Thermos Mug"), 'justmonikathermos')
        ]
        if not mas_seenEvent("mas_reaction_gift_noudeck"):
            objects_menu.append(store.ep_files.GiftAction(_("NOU"), 'noudeck'))

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
            
label plus_ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [ # Using the new class from ep_files store
            store.ep_files.GiftAction(_("Black Ribbon"), 'blackribbon'),
            store.ep_files.GiftAction(_("Blue Ribbon"), 'blueribbon'),
            store.ep_files.GiftAction(_("Dark Purple Ribbon"), 'darkpurpleribbon'),
            store.ep_files.GiftAction(_("Emerald Ribbon"), 'emeraldribbon'),
            store.ep_files.GiftAction(_("Gray Ribbon"), 'grayribbon'),
            store.ep_files.GiftAction(_("Green Ribbon"), 'greenribbon'),
            store.ep_files.GiftAction(_("Light Purple Ribbon"), 'lightpurpleribbon'),
            store.ep_files.GiftAction(_("Peach Ribbon"), 'peachribbon'),
            store.ep_files.GiftAction(_("Pink Ribbon"), 'pinkribbon'),
            store.ep_files.GiftAction(_("Platinum Ribbon"), 'platinumribbon'),
            store.ep_files.GiftAction(_("Red Ribbon"), 'redribbon'),
            store.ep_files.GiftAction(_("Ruby Ribbon"), 'rubyribbon'),
            store.ep_files.GiftAction(_("Sapphire Ribbon"), 'sapphireribbon'),
            store.ep_files.GiftAction(_("Silver Ribbon"), 'silverribbon'),
            store.ep_files.GiftAction(_("Teal Ribbon"), 'tealribbon'),
            store.ep_files.GiftAction(_("Yellow Ribbon"), 'yellowribbon')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
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
    if not renpy.seen_label("extra_relation_monika"):
        m 2eub "You know, if you count it all up, it seems we've been together for [time_string]!"
        if total_days <= 1:
            m 2lub "We've only just begun, but every single second has been a dream come true."
        elif total_days < 365:
            m 2hubsb "It hasn't even been a year, and I already feel like I've known you forever. Time just flies by when I'm with you!"
        elif total_days < 365 * 2:
            m 2kubsb "Happy first anniversary! I still remember our first day together... Thank you for making so many memories with me."
        elif total_days < 365 * 3:
            m 2wubsb "Wow, two years together! Every day with you has been so special. Thank you for staying by my side."
        elif total_days < 365 * 4:
            m 1dsbsa "Three years... Time really does fly when I'm with you. We've shared so much, and I can't wait for more."
        elif total_days < 365 * 5:
            m 2wubsb "Four years! That's incredible, [player]. Our bond is so strong. Thank you for staying with me for so long."
        elif total_days < 365 * 6:
            m 2tubsb "Five years together... I feel so lucky to have you. Thank you for all the love and memories."
        elif total_days < 365 * 7:
            m 2subsb "Six years! Can you believe it? Every year with you is a treasure. Thank you for being with me all this time."
        else:
            m 2lubsb "It's been so long... but it really doesn't feel that way when I'm with you. Time just flies by!"
    else:
        m 2eub "We've been together for [time_string]!"
        m 2lubsb "It really doesn't feel that long when I'm with you, though. Time just flies by!"
    jump close_extraplus
    return

label extra_aff_log:
    python:
        current_affection = store.ep_affection.getCurrentAffection()
        affection_value = int(current_affection)
        monika_level = store.ep_affection.getLevelIcon(current_affection)
    
    show monika idle at t11
    #Agregar variantes con una probabilidad baja. Thanks for the idea u/PeachesTheNinja
    "Your affection with [m_name] is [affection_value] [monika_level]{fast}"
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
    show coin_moni zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound sfx_coin_flip
    pause 1.0
    hide coin_moni
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
    show monika idle at t21
    python:
        # Updated menu with three distinct options
        window_menu = [
            (_("Type a new title"), 'extra_change_title_manual'),
            (_("Paste title from clipboard"), 'extra_change_title_paste'),
            (_("Restore the window title"), 'extra_restore_title')
        ]

        items = [(_("Nevermind"), 'extraplus_tools', 20)]
    call screen extra_gen_list(window_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extra_change_title_manual:
    show monika idle at t11
    python:
        player_input = mas_input(
            prompt=_("What should our new window title be?"),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.,'0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"}
        )
    if player_input and player_input != "cancel":
        jump process_new_title
    else:
        jump extra_window_title
    return

label extra_change_title_paste:
    show monika idle at t11
    python:
        allowed_chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.,'0123456789"
        player_input = store.ep_tools.filtered_clipboard_text(allowed_chars)
    if player_input and player_input != "cancel":
        jump process_new_title
    else:
        jump extra_window_title
    return

label process_new_title:
    $ persistent._save_window_title = player_input.strip()
    $ config.window_title = persistent._save_window_title
    $ renpy.notify(random.choice([
        _("Title updated successfully!"),
        _("All set! The new title is in place."),
        _("Done! Your window has a fresh new title.")
    ]))
    jump close_extraplus

label extra_restore_title:
    show monika idle at t11
    python:
        if store.ep_tools.backup_window_title == persistent._save_window_title:
            renpy.notify(_("No need to do it again hehe~"))
        else:
            renpy.notify(_("It's nice to see the original name again."))

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
    show monika idle at t21
    python:
        misc_tools_menu = [
            (_("How long have we been together, [m_name]?"), 'extra_relation_monika'),
            (_("[m_name], I want to make a backup"), 'extra_mas_backup'),
            (_("[m_name], can you flip a coin?"), 'extra_coinflip')
        ]

        items = [
            (_("Github Repository"), 'extra_github_submod', 20), 
            (_("Nevermind"), 'extraplus_tools', 0)
        ]
    call screen extra_gen_list(misc_tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extra_show_timeline:
    show monika idle at t11
    call screen extra_timeline_screen
    return

#====GAME
label extra_dev_mode:
    python:
        mas_RaiseShield_dlg()
        if not renpy.get_screen("doki_chibi_idle"):
            config.overlay_screens.append("doki_chibi_idle")
    show monika idle at t11
    call screen sticker_customization
    return

label sticker_primary:
    show monika idle at t21
    python:
        accessories = [
            store.ep_chibis.DokiAccessory(_("Cat Ears"), 'cat_ears', "primary"),
            store.ep_chibis.DokiAccessory(_("Christmas Hat"), 'christmas_hat', "primary"),
            store.ep_chibis.DokiAccessory(_("Demon Horns"), 'demon_horns', "primary"),
            store.ep_chibis.DokiAccessory(_("Flowers Crown"), 'flowers_crown', "primary"),
            store.ep_chibis.DokiAccessory(_("Halo"), 'halo', "primary"),
            store.ep_chibis.DokiAccessory(_("Heart Headband"), 'heart_headband', "primary"),
            store.ep_chibis.DokiAccessory(_("New Year's Headband"), 'hny', "primary"),
            store.ep_chibis.DokiAccessory(_("Neon Cat Ears"), 'neon_cat_ears', "primary"),
            store.ep_chibis.DokiAccessory(_("Party Hat"), 'party_hat', "primary"),
            store.ep_chibis.DokiAccessory(_("Rabbit Ears"), 'rabbit_ears', "primary"),
            store.ep_chibis.DokiAccessory(_("Witch Hat"), 'witch_hat', "primary")
        ]
        items = [(store.ep_chibis.DokiAccessory(_("Remove"), '0nothing', "primary"), 20), (_("Nevermind"), 'extra_dev_mode', 0)]

    call screen extra_gen_list(accessories, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return

label sticker_secondary:
    show monika idle at t21
    python:
        accessories_2 = [
            store.ep_chibis.DokiAccessory(_("Black Bow Tie"), 'black_bow_tie', "secondary"),
            store.ep_chibis.DokiAccessory(_("Christmas Tree"), 'christmas_tree', "secondary"),
            store.ep_chibis.DokiAccessory(_("Cloud"), 'cloud', "secondary"),
            store.ep_chibis.DokiAccessory(_("Coffee"), 'coffee', "secondary"),
            store.ep_chibis.DokiAccessory(_("Halloween Pumpkin"), 'pumpkin', "secondary"),
            store.ep_chibis.DokiAccessory(_("Hearts"), 'hearts', "secondary"),
            store.ep_chibis.DokiAccessory(_("Monika's Cake"), 'm_slice_cake', "secondary"),
            store.ep_chibis.DokiAccessory(_("Moustache"), 'moustache', "secondary"),
            store.ep_chibis.DokiAccessory(_("Neon Blush"), 'neon_blush', "secondary"),
            store.ep_chibis.DokiAccessory(_("[player]'s Cake"), 'p_slice_cake', "secondary"),
            store.ep_chibis.DokiAccessory(_("Pirate Patch"), 'patch', "secondary"),
            store.ep_chibis.DokiAccessory(_("Speech Bubble with Heart"), 'speech_bubble', "secondary"),
            store.ep_chibis.DokiAccessory(_("Sunglasses"), 'sunglasses', "secondary")
        ]
        items = [(store.ep_chibis.DokiAccessory(_("Remove"), '0nothing', "secondary"), 20), (_("Nevermind"), 'extra_dev_mode', 0)]

    call screen extra_gen_list(accessories_2, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return

label doki_change_appe:
    show monika idle at t21
    python:
        doki_data = [("Monika", 'monika_sticker_costumes')]
        if persistent._mas_pm_cares_about_dokis:
            doki_data.extend([
                (_("Natsuki"), 'natsuki_sticker_costumes'),
                (_("Sayori"), 'sayori_sticker_costumes'),
                (_("Yuri"), 'yuri_sticker_costumes')
            ])
        items = [(_("Nevermind"), 'extra_dev_mode', 20)]

    call screen extra_gen_list(doki_data, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label monika_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.monika_costumes_, 'doki_change_appe')
    return

label natsuki_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.natsuki_costumes_, 'doki_change_appe')
    return

label sayori_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.sayori_costumes_, 'doki_change_appe')
    return

label yuri_sticker_costumes:
    $ store.ep_chibis.show_costume_menu(store.ep_chibis.yuri_costumes_, 'doki_change_appe')
    return

label maxwell_screen:
    show monika idle at t11
    call screen maxwell_april_fools
    jump extraplus_tools
    return
