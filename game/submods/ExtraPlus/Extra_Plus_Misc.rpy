################################################################################
## BOOP
################################################################################

#====NOISE
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
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
        call screen boop_event(10, "boop_nop", "boop_yep")
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
    else:
        $ rng_global = renpy.random.randint(1,5)
        if rng_global == 1:
            m 2fubla "Ehehe~"
            m 1hubla "It's very inevitable that you won't stop doing it, [player]."
        elif rng_global == 2:
            m 3ekbsa "Every boop you give me, the more I love you!"
        elif rng_global == 3:
            m 3eubla "You really enjoy touching my nose, [mas_get_player_nickname()]~"
        elif rng_global == 4:
            m 2hublb "Hey, you're tickling me! Ahahaha~"
        elif rng_global == 5:
            m 1hubsb "*Boop*"
    jump show_boop_screen
    return

label boop_nop:
    m 1rksdrb "[player]..."
    m 1rksdra "...I was so excited for you to do it again."
    m "..."
    m 3hub "Well, nevermind!"
    jump show_boop_screen
    return

label boop_yep:
    m 1eublb "Thank you [mas_get_player_nickname()]!"
    m 1hua "Ehehe~"
    jump show_boop_screen
    return

label monika_boopbeta_war:
    if renpy.seen_label("check_boopwar"):
        jump check_boopwarv2
    else:
        pass

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
    call screen boop_event(20, "boopbeta_war_lose", "boopwar_loop")

label boopwar_loop:
    $ boop_war_count += 1
    $ rng_global = renpy.random.randint(1,10)
    if rng_global == 1:
        m 1hublb "*Boop*"
    elif rng_global == 2:
        m 1tub "*Boop*"
    elif rng_global == 3:
        if boop_war_count >= 25:
            jump boopbeta_war_win
            $ boop_war_count = 0
        else:
            m 1fua "*Boop*"
    elif rng_global == 4:
        m 1eua "*Boop*"
    elif rng_global == 5:
        m 1hua "*Boop*"
    elif rng_global == 6:
        if boop_war_count >= 50:
            jump boopbeta_war_win
            $ boop_war_count = 0
        else:
            m 1sub "*Boop*"
    elif rng_global == 7:
        m 1gua "*Boop*"
    elif rng_global == 8:
        m 1kub "*Boop*"
    elif rng_global == 9:
        if boop_war_count >= 100:
            jump boopbeta_war_win
            $ boop_war_count = 0
        else:
            m 1dub "*Boop*"
    elif rng_global == 10:
        m 1wua "*Boop*"

    show monika 1eua
    jump check_boopwarv2
    return

label boopbeta_war_lose:
    $ boop_war_count = 0
    m 1nua "Looks like I've won this boop war, [player]~"
    m "I hope I've been a good opponent."
    m 3hub "But I've also really enjoyed it!"
    m 3dua "Besides, it's good to give your hand a little massage."
    m 1eka "I mean, if you use the mouse too much, "
    extend 1ekb "you can develop carpal tunnel syndrome and I don't want that."
    m 1hksdlb "I'm sorry if I've added a new concern, but my intention is to take care of you."
    m 1eubla "I hope you take my recommendation, [player]~"
    jump show_boop_screen
    return

label boopbeta_war_win:
    $ boop_war_count = 0
    m 1hua "You've won this boop war, [player]!"
    m 1tub "I can tell you like touching my nose, ehehehe~"
    m 1eusdra "I couldn't keep up with you, but maybe next time we'll go further."
    m 1gub "Although, if I were in front of you, I'd play with your cheeks."
    m 1gua "Or I'd tickle you and see how long you could stand it."
    m 1hub "Ahaha~"
    jump show_boop_screen
    return

#====CHEEKS
label monika_cheeksbeta:
    $ persistent.plus_boop[1] += 1
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
    else:
        $ rng_global = renpy.random.randint(1,5)
        if rng_global == 1:
            m 2fua "Ehehe~"
            m 2hua "It would be nice if you used your hand instead of the cursor, but that's far from our reality..."
        elif rng_global == 2:
            m 2hubsa "So gentle."
            m 2tubsb "That word defines you well, when I think of you."
        elif rng_global == 3:
            m 2hubsa "What a warm feeling."
            m 2hublb "It will be hard to forget!"
        elif rng_global == 4:
            m 2nubsa "It would be even more romantic if you gave a kiss on the cheek~"
        elif rng_global == 5:
            m 2eubsb "I'm picturing us right now{nw}"
            extend 2dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} how your hand will feel."
    jump show_boop_screen
    return

label monika_cheeks_long:
    m 2hubsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump show_boop_screen
    return

label cheeks_dis:
    m 1wuw "Ah!"
    m 3lusdrb "I mean..."
    m 3ttu "What are you doing touching my cheek?"
    m 3tsb "We're in a boop war, aren't we?"
    $ rng_global = renpy.random.randint(1,2)
    if rng_global == 1:
        m 1dsb "I'm sorry [player], but I consider this cheating, "
        extend 1hua "that's why I win this war~"
        m 1fub "Next time try not to touch my cheek during the war! Ahahaha~"
    elif rng_global == 2:
        m 1fubsb "Because it's you, this time I will let it go!"
        m 1fubsb "Congratulations, player! You have beat me."
        m 3hksdrb "You've distracted me and I don't think it's worth continuing, ahahaha~"
        m 3hua "I really enjoyed doing this with you though!"
    $ boop_war_count = 0
    jump show_boop_screen
    return

#====HEADPAT
label monika_headpatbeta:
    $ persistent.plus_boop[2] += 1
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
    else:
        $ rng_global = renpy.random.randint(1,5)
        if rng_global == 1:
            m 6hubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6hkbsb "I had told you I would get addicted to this."
            m 6tkbsb "Gosh, don't you learn~"
        elif rng_global == 2:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6dubsb "I wonder what it would be like to do it with your hair."
        elif rng_global == 3:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 7hubsb "I hope you don't get tired of doing it daily~"
        elif rng_global == 4:
            m 6hubsa".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            extend 6hubsb "I'm such a happy girl right now."
        elif rng_global == 5:
            m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    jump show_boop_screen
    return

label monika_headpat_long:
    m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump show_boop_screen
    return

label headpat_dis:
    m 6dkbsb "This.{w=0.3}.{w=0.3}.{w=0.3} is.{w=0.3}.{w=0.3}.{w=0.3} invalid.{w=0.3}.{w=0.3}. {nw}"
    extend 6tkbsb "[mas_get_player_nickname()]."
    $ rng_global = renpy.random.randint(1,2)
    if rng_global == 1:
        m 3tsb "You have been disqualified for patting your opponent on the head."
        m 3tua "That's why I win this time~"
        m 1hua "Good luck for the next time you ask me for a war!"
    elif rng_global == 2:
        m 1tub "This time I'll let it go and give up for you."
        m 1efa "But next time I probably won't give in, so don't bet on it!"
        m 1lubsa "Even though I enjoy the pat on the head. Ehehehe~"
    $ boop_war_count = 0
    jump show_boop_screen
    return

#===========================================================================================
# EXTRAS
#===========================================================================================
define coin_sprites = ["sprite_coin.png","sprite_coin-n.png","coin_heads.png","coin_tails.png"]

label aff_log:
    show monika idle at t11
    $ get_affection = int(_mas_getAffection())
    if os.path.isfile(renpy.config.basedir + '/game/submods/ExtraPlus/submod_assets/Pictograms.ttf'):
        "Your affection with [m_name] is [get_affection] {size=+5}{color=#FFFFFF}{font=submods/ExtraPlus/submod_assets/Pictograms.ttf}7{/font}{/color}{/size}"
    else:
        "Your affection with [m_name] is [get_affection]"
    window hide
    jump close_extraplus
    return

label coinflipbeta:
    $ validate_files(coin_sprites, type=True)
    if renpy.seen_label("check_coinflipbeta"):
        jump view_coinflipbeta
    else:
        pass

label check_coinflipbeta:
    show monika 1hua at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
        rng_global = renpy.random.randint(1,2)
    m "Okay!"
    m 3eub "I'll go get a coin."
    call mas_transition_to_emptydesk
    $ renpy.pause(2.0, hard=True)
    call mas_transition_from_emptydesk("monika 1eua")
    m "I found one!"
    show screen extra_no_click
    show monika 3eua
    show coin_moni zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound "submods/ExtraPlus/submod_assets/sfx/coin_flip_sfx.ogg"
    pause 1.0
    hide coin_moni
    show monika 1eua
    pause 0.5
    hide screen extra_no_click
    if rng_global == 1:
        show coin_heads zorder 12:
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads
    elif rng_global == 2:
        show coin_tails zorder 12:
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails
    m 3hua "I hope it helps you~"
    window hide
    python:
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
    jump close_extraplus
    return

label view_coinflipbeta:
    show monika 1hua at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
        rng_global = renpy.random.randint(1,2)
    show screen extra_no_click
    pause 1.5
    show monika 3eua at t11
    show coin_moni zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound "submods/ExtraPlus/submod_assets/sfx/coin_flip_sfx.ogg"
    pause 1.0
    hide coin_moni
    show monika 1eua
    pause 0.5
    hide screen extra_no_click
    if rng_global == 1:
        show coin_heads zorder 12:
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads
    elif rng_global == 2:
        show coin_tails zorder 12:
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails
    m 3hua "I hope it helps you~"
    window hide
    python:
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
    jump close_extraplus
    return

label mas_backup:
    show monika 1hua at t11
    m 1hub "I'm glad you want to make a backup!"
    m 3eub "I'll open the route for you."
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    window hide
    python:
        import os, sys, subprocess
        #Monika will open the mod data folder
        try:
            if sys.platform == "win32":
                os.startfile(renpy.config.savedir)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, renpy.config.savedir])
        except:
            renpy.jump("mas_backup_fail")
    jump close_extraplus
    return

label mas_backup_fail:
    m 1lkb "Sorry, I could not open the folder."
    m 1eka "Please try again later."
    jump close_extraplus
    return

label extra_window_title:
    show monika idle at t21
    python:
        window_menu = [
            ("Change the window's title", 'extra_change_title'),
            ("Restore the window title", 'extra_restore_title')
        ]
        
    call screen list_scrolling(window_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"tools_extra",close=True) nopredict
    return
    
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
    
label github_submod:
    show monika idle at t11
    $ renpy.run(OpenURL("https://github.com/zer0fixer/MAS-Extraplus"))
    jump close_extraplus
    return