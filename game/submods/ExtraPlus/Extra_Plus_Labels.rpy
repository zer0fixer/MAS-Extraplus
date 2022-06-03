################################################################################
## R_LABELS
################################################################################
label show_extraplus:
    $ store.mas_sprites.reset_zoom()
    $ mas_RaiseShield_dlg()
    show monika staticpose at t11
    $ Extraplus_show()
    return

label return_extra:
    show monika staticpose at t11
    $ Extraplus_show()
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

label restore_bg:
    python:
        store.monika_chr.tablechair.chair = extra_chair
        store.monika_chr.tablechair.table = extra_table
        HKBHideButtons()
        mas_current_background = extra_old_bg
    if show_chibika is True:
        hide screen chibika_chill
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    $ HKBShowButtons()
    jump comment_cafe
    return

label back_extra:
    if renpy.get_screen("chibika_chill"):
        hide screen chibika_chill
        with dissolve
    $ mas_DropShield_dlg()
    jump ch30_loop
    return

label check_cheat_minigame:
    m 3hksdrb "I think you forgot something, [player]!"
    m 3eksdra "You must restore the variables you have modified."
    m 1hua "We will not play until they are at 0."
    jump return_extra
    return

################################################################################
## GIFTS
################################################################################
label make_gift:
    show monika staticpose at t11
    menu:
        "Create a file":
            jump make_file
        "Groceries":
            jump groceries
        "Objects":
            jump objects
        "Nevermind":
            jump tools_extra
    return

label make_file:
    python:
        import os
        makegift = mas_input("Write the name and extension (.gift, .txt, .chr, etc...)")
        filepath = os.path.join(renpy.config.basedir + '/characters',makegift)
        f = open(filepath,"a")
    "Has been successfully created."
    jump make_gift
    return

label groceries:
    menu:
        "Coffee":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','coffee.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Chocolates":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','chocolates.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Cupcake":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters', 'cupcake.gift')
                f = open(filepath, "a")
            "Has been successfully created."
            jump make_gift

        "Fudge":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','fudge.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Hot Chocolate":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','hotchocolate.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Next":
            jump groceries_next

        "Nevermind":
            jump make_gift
    return

label groceries_next:
    menu:
        "Candy":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','candy.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Candy Canes":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','candycane.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Candy Corn":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','candycorn.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Christmas Cookies":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','christmascookies.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Previous":
            jump groceries

        "Nevermind":
            jump make_gift
    return

label objects:
    menu:
        "Promise Ring":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','promisering.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Roses":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','roses.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Quetzal Plushie":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','quetzalplushie.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Thermos Mug":
            python:
                filepath = os.path.join(renpy.config.basedir + '/characters','justmonikathermos.gift')
                f = open(filepath,"a")
            "Has been successfully created."
            jump make_gift

        "Nevermind":
            jump make_gift
    return

################################################################################
## MENUS
################################################################################
label minigames_extra:
    show monika staticpose at t21
    python:
        monika_talk = renpy.random.choice(minigames_talk)
        renpy.say(m, monika_talk, interact=False)
    call screen minigame_ui() nopredict
    jump return_extra
    return

label tools_extra:
    show monika staticpose at t21
    python:
        tools_menu = []
        tools_menu.append((_("View [m_name]'s Affection"), "affection"))
        tools_menu.append((_("[m_name], can you flip a coin?"), "coin"))
        tools_menu.append((_("[m_name], I want to make a backup"), "backup"))
        tools_menu.append((_("Create a gift for [m_name]"), "gift"))
        tools_menu.append((_("Github Repository"), "github"))
        tools_menu.append((_("Nevermind"),"nevermind"))

        playerchoice = renpy.display_menu(tools_menu, screen="talk_choice")

    if playerchoice == "affection":
        jump aff_log
    elif playerchoice == "coin":
        jump coinflipbeta
    elif playerchoice == "backup":
        jump mas_backup
    elif playerchoice == "gift":
        jump make_gift
    elif playerchoice == "github":
        jump github_submod
    elif playerchoice == "nevermind":
        jump return_extra
    return

label walk_extra:
    show monika staticpose at t21
    python:
        monika_talk = renpy.random.choice(date_talk)
        walk_menu = []
        walk_menu.append((_("Cafe"), "cafe"))
        walk_menu.append((_("Nevermind"), "nevermind"))

        renpy.say(m, monika_talk, interact=False)
        playerchoice = renpy.display_menu(walk_menu, screen="talk_choice")

    if playerchoice == "cafe":
        show monika at t11
        jump go_to_cafe
    elif playerchoice == "nevermind":
        jump return_extra
    return

label cafe_talkdemo:
    show monika staticpose at t21
    python:
        cafe_menu = []
        cafe_menu.append((_("How are you today?"), "t1"))
        cafe_menu.append((_("What's your greatest ambition?"), "t2"))
        cafe_menu.append((_("Our communication is very limited, don't you think?"), "t3"))
        cafe_menu.append((_("Can we leave?"), "t4"))
        cafe_menu.append((_("Next"), "next"))
        cafe_menu.append((_("Nevermind"),"nevermind"))

        playerchoice = renpy.display_menu(cafe_menu, screen="talk_choice")

    if playerchoice == "t1":
        jump extra_talk_feel
    elif playerchoice == "t2":
        jump extra_talk_ambition
    elif playerchoice == "t3":
        jump extra_talk_you
    elif playerchoice == "t4":
        jump cafe_leave
    elif playerchoice == "next":
        jump cafe_talkdemonext
    elif playerchoice == "nevermind":
        jump to_cafe_loop
    return

label cafe_talkdemonext:
    show monika staticpose at t21
    python:
        cafenext_menu = []
        cafenext_menu.append((_("How do you see us in 10 years?"), "t5"))
        cafenext_menu.append((_("What is your best memory that you currently have?"), "t6"))
        cafenext_menu.append((_("Do you have any phobia?"), "t7")) #autophobia
        cafenext_menu.append((_("Previous"), "previous"))
        cafenext_menu.append((_("Nevermind"),"nevermind"))

        playerchoice = renpy.display_menu(cafenext_menu, screen="talk_choice")

    if playerchoice == "t5":
        jump extra_talk_teen
    elif playerchoice == "t6":
        jump extra_talk_memory
    elif playerchoice == "t7":
        jump extra_talk_phobia
    elif playerchoice == "previous":
        jump cafe_talkdemo
    elif playerchoice == "nevermind":
        jump to_cafe_loop
    return

################################################################################
## ADDS
################################################################################
label github_submod:
    show monika staticpose at t11
    $ renpy.run(OpenURL("https://github.com/zer0fixer/MAS-Extraplus"))
    jump return_extra
    return

label aff_log:
    show monika staticpose at t11
    "Your affection with [m_name] is [_mas_getAffection()] {size=+5}{color=#FFFFFF}{font=submods/ExtraPlus/submod_assets/Pictograms.ttf}7{/font}{/color}{/size}"
    window hide
    jump return_extra
    return

label coinflipbeta:
    if renpy.seen_label("check_coinflipbeta"):
        jump view_coinflipbeta
    else:
        pass
label check_coinflipbeta:
    $ rng_global = renpy.random.randint(1,2)
    show monika 1hua at t11
    m "Okay!"
    m 3eub "I'll go get a coin."
    call mas_transition_to_emptydesk from monika_hide_exp_1
    $ renpy.pause(2.0, hard=True)
    call mas_transition_from_emptydesk("monika 1eua")
    m "I found one!"
    show screen no_click
    show monika 3eua
    if mas_isDayNow():
        show coin_flip zorder 12 at rotatecoin:
            xalign 0.5
            yalign 0.5
    elif not mas_isDayNow():
        show coin_flip_n zorder 12 at rotatecoin:
            xalign 0.5
            yalign 0.5
    play sound "submods/ExtraPlus/submod_assets/sfx/coin_flip_sfx.wav"
    pause 1.0
    hide coin_flip
    hide coin_flip_n
    show monika 1eua
    pause 0.5
    hide screen no_click
    if rng_global == 1:
        show coin_heads zorder 12 with Dissolve(0.1):
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads with Dissolve(0.1)
    elif rng_global == 2:
        show coin_tails zorder 12 with Dissolve(0.1):
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails with Dissolve(0.1)
    m 3hua "I hope it helps you~"
    window hide
    jump return_extra
    return

label view_coinflipbeta:
    show monika 1hua at t11
    $ rng_global = renpy.random.randint(1,2)
    show screen no_click
    pause 1.0
    show monika 3eua at t11
    if mas_isDayNow():
        show coin_flip zorder 12 at rotatecoin:
            xalign 0.5
            yalign 0.5
    elif not mas_isDayNow():
        show coin_flip_n zorder 12 at rotatecoin:
            xalign 0.5
            yalign 0.5
    play sound "submods/ExtraPlus/submod_assets/sfx/coin_flip_sfx.wav"
    pause 1.0
    hide coin_flip
    hide coin_flip_n
    show monika 1eua
    pause 0.5
    hide screen no_click
    if rng_global == 1:
        show coin_heads zorder 12 with Dissolve(0.1):
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads with Dissolve(0.1)
    elif rng_global == 2:
        show coin_tails zorder 12 with Dissolve(0.1):
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails with Dissolve(0.1)
    m 3hua "I hope it helps you~"
    window hide
    jump return_extra
    return

label mas_backup:
    show monika 1hua at t11
    m 1hub "I'm glad you want to make a backup!"
    m 3eub "I'll open the route for you."
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    pause 0.5
    window hide
    python:
        import os
        #Monika will open the mod data folder
        try:
            os.startfile("C:\\Users\\" + currentuser + "\\AppData\\Roaming\\RenPy\\Monika After Story")
        except:
            renpy.jump("mas_backup_fail")
    jump return_extra
    return

label mas_backup_fail:
    m 1lkb "Sorry, I could not open the folder."
    m 1eka "Please try again later."
    jump return_extra
    return
label comment_cafe:
    m 1hubsa "Thank you for asking me out."
    m 1eubsb "It is nice to have these moments as a couple!"
    m 1eubsa "I feel very fortunate to have met you and that you keep choosing me every day."
    m 1ekbsa "I love you, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_loop
    return

################################################################################
## TOPICS
################################################################################
#BOOP
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
    if persistent.plus_boop[0] == 1:
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
    jump return_extra
    return

label boop_nop:
    m 1rksdrb "[player]..."
    m 1rksdra "...I was so excited for you to do it again."
    m "..."
    m 3hub "Well, nevermind!"
    jump return_extra
    return

label boop_yep:
    m 1eublb "Thank you [mas_get_player_nickname()]!"
    m 1hua "Ehehe~"
    jump return_extra
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
    jump return_extra
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
    jump return_extra
    return

label boopbeta_war_win:
    $ boop_war_count = 0
    m 1hua "You've won this boop war, [player]!"
    m 1tub "I can tell you like touching my nose, ehehehe~"
    m 1eusdra "I couldn't keep up with you, but maybe next time we'll go further."
    m 1gub "Although, if I were in front of you, I'd play with your cheeks."
    m 1gua "Or I'd tickle you and see how long you could stand it."
    m 1hub "Ahaha~"
    jump return_extra
    return

#CHEEKS
label monika_cheeksbeta:
    $ persistent.plus_boop[1] += 1
    if persistent.plus_boop[1] == 1:
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
    jump return_extra
    return

label monika_cheeks_long:
    m 2hubsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump return_extra
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
    jump return_extra
    return

#HEADPAT
label monika_headpatbeta:
    $ persistent.plus_boop[2] += 1
    if persistent.plus_boop[2] == 1:
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
    jump return_extra
    return

label monika_headpat_long:
    m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump return_extra
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
    jump return_extra
    return
