################################################################################
## MINIGAME#3
################################################################################
#Rock Paper Scissors
label minigame_psr:
    if moni_wins > 0 or player_wins > 0:
        jump cheat_psr
    show monika 1hua at t21
    show card_back zorder 12:
        xalign 0.7
        yalign 0.1
        yoffset -900
        easein 0.5 yoffset 0
    show e_rock zorder 12:
        xalign 0.5
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.1
    show e_paper zorder 12:
        xalign 0.7
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.2
    show e_scissors zorder 12:
        xalign 0.9
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.3
    hide card_back
    hide e_rock
    hide e_paper
    hide e_scissors
    call screen PSR_mg
    return

label psr_loop:
    $ rng_global = renpy.random.randint(1,3)
    show card_back zorder 12:
        xalign 0.7
        yalign 0.1
    if your_choice == 1:
        show e_rock zorder 12:
            yoffset -20
            xalign 0.5
            yalign 0.7
        show e_paper zorder 12:
            xalign 0.7
            yalign 0.7
        show e_scissors zorder 12:
            xalign 0.9
            yalign 0.7
        m 1eub "Rock,{w=0.3} Paper,{w=0.3} Scissors{w=0.3}!{nw}"
        hide card_back with dissolve
        if rng_global == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 3hub "A rock against another rock, ahahaha~"
            m 1hua "It is a tie."

        elif rng_global == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1dub "The paper wraps the rock."
            m 1tub "So sorry, [player], you have lost!"
            $ moni_wins += 1

        elif rng_global == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1hksdrb "The rock breaks the scissors."
            m 1hua "You beat me, [player]!"
            $ player_wins += 1

    elif your_choice == 2:
        show e_rock zorder 12:
            xalign 0.5
            yalign 0.7
        show e_paper zorder 12:
            yoffset -20
            xalign 0.7
            yalign 0.7
        show e_scissors zorder 12:
            xalign 0.9
            yalign 0.7
        m 1eub "Rock,{w=0.3} Paper,{w=0.3} Scissors{w=0.3}!{nw}"
        hide card_back with dissolve
        if rng_global == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1lkb "The paper wraps the rock."
            m 1lub "You win, [player]."
            $ player_wins += 1

        elif rng_global == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1hua "We both chose paper!"
            m 1tua "We're in a tie and you should stop reading my mind [mas_get_player_nickname()]~"
            m 1tua "Ahahahaha~"

        elif rng_global == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 3eub "The scissors cut the paper."
            m 3hua "Sorry [player], you lost."
            $ moni_wins += 1

    elif your_choice == 3:
        show e_rock zorder 12:
            xalign 0.5
            yalign 0.7
        show e_paper zorder 12:
            xalign 0.7
            yalign 0.7
        show e_scissors zorder 12:
            yoffset -20
            xalign 0.9
            yalign 0.7
        m 1eub "Rock,{w=0.3} Paper,{w=0.3} Scissors{w=0.3}!{nw}"
        hide card_back with dissolve
        if rng_global == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1mub "Say goodbye to your scissors, [player]~"
            m "You couldn't beat me! Ahahaha~"
            $ moni_wins += 1

        elif rng_global == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1hssdrb "The scissors cuts the paper."
            m 1eua "I award you the victory!"
            $ player_wins += 1

        elif rng_global == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 2hkb "Two scissors equals a tie, [player]!"
            m 2hub "Although it's funny that you thought the same thing, ehehehe~"
    show monika 1hua at t21
    $ your_choice = 0
    jump hide_images_psr
    return

label psr_quit:
    show card_back zorder 12 as v1:
        xalign 0.7
        yalign 0.1
    show e_rock zorder 12 as r1:
        xalign 0.5
        yalign 0.7
    show e_paper zorder 12 as r2:
        xalign 0.7
        yalign 0.7
    show e_scissors zorder 12 as r3:
        xalign 0.9
        yalign 0.7

    show card_back zorder 12:
        xalign 0.7
        yalign 0.1
        easeout 0.6 yoffset -1300
    show e_rock zorder 12:
        xalign 0.5
        yalign 0.7
        easeout 0.6 yoffset 1300
    hide e_rock as r1
    hide card_back as v1
    pause 0.1

    show e_paper zorder 12:
        xalign 0.7
        yalign 0.7
        easeout 0.6 yoffset 1300
    hide e_paper as r2
    pause 0.2

    show e_scissors zorder 12:
        xalign 0.9
        yalign 0.7
        easeout 0.6 yoffset 1300
    hide e_scissors as r3
    pause 0.3

    hide card_back
    hide e_rock
    hide e_paper
    hide e_scissors
    $ your_choice = 0
    jump psr_result
    return

################################################################################
## TALKING GAME
################################################################################
label psr_result:
    show monika 1hua at t11
    #Tie
    if moni_wins == player_wins:
        if moni_wins == 0 and player_wins == 0:
            m 1etd "Don't you want to play rock-paper-scissors?"
            m 1eka "I thought he wanted to play with me for a while..."
            m 3hua "But don't worry, I know you have changed your mind and are not in the mood to play."
            m 3hub "So I hope we can play another time!"
        else:
            m 1sua "Wow, it's a tie."
            m 1tua "It's because we are such a couple that our minds are one!"
            m 1hub "Ehehe~"
            m 3hua "But we have to break the tie, [player]."
            m 3hub "We will see who wins next time, good luck!"
    #Monika wins
    elif moni_wins > player_wins:
        m 3eub "This time I won, [player]~"
        m 3eub "I've had some luck."
        m 3eubsa "But don't feel bad, what matters most to me is that we both have fun."
        m 1hub "Next time I know you will beat me, I trust you!"
    #Player wins
    elif moni_wins < player_wins:
        m 1hub "You beat me [player], congratulations."
        m 1hub "I'm proud of you~"
        m 2tub "But I warn you that next time I will try to read your mind."
        m 2hub "I'm likely to win!"
        m 2hua "So be careful when we play again."
        m 2hua "Ehehe~"
    jump return_extra
    return

label cheat_psr:
    show monika 1hua at t11
    if renpy.seen_label("check_cheat_psr"):
        jump check_cheat_minigame
    else:
        jump check_cheat_psr
label check_cheat_psr:
    m 1hkb "Uhhh, to be honest, I don't know how to respond to what you have done."
    if moni_wins == player_wins:
        m 3eua "Even if we are tied."
    elif moni_wins > player_wins:
        m 3lkb "It feels bad that I'm beating you..."
    elif moni_wins < player_wins:
        m 1hsb "You are ahead without even starting the game."
    m 1hua "I don't think it's worth it for you to do so..."
    m 1dua "And I don't see the need to talk about whether modifying the minigame is wrong or not."
    m 2fub "After all, I have a feeling that you did it more out of curiosity than to get an easy victory."
    m 1etd "I guess you must be thinking, 'Are you angry [m_name]?'"
    m 3hub "Of course not!"
    m 3dub "Imagine getting angry about something so simple, like cheating in a mini-game."
    m 1eua "Well I hope you don't do it in other video games."
    m 1lud "Eventually you will feel empty..."
    m 1lkb "And I don't want that to happen to you, "
    extend 1hubsb "so just have fun fair and square!"
    jump return_extra
    return
