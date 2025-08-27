#===========================================================================================
# MINIGAME#3
#===========================================================================================

#====Rock Paper Scissors
label minigame_rps:
    python:
        mas_MUMURaiseShield()
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
    show screen score_minigame(game="rps")
    call screen RPS_mg nopredict
    return

label rps_loop:
    $ moldable_variable = renpy.random.randint(1,3)
    show card_back zorder 12:
        xalign 0.7
        yalign 0.1
    if rps_your_choice == 1:
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
        if moldable_variable == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 3hub "A rock against another rock, ahahaha~"
            m 1hua "It is a tie."

        elif moldable_variable == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1dub "The paper wraps the rock."
            m 1tub "So sorry, [player], you have lost!"
            $ moni_wins += 1

        elif moldable_variable == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1hksdrb "The rock breaks the scissors."
            m 1hua "You beat me, [player]!"
            $ player_wins += 1

    elif rps_your_choice == 2:
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
        if moldable_variable == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1lkb "The paper wraps the rock."
            m 1lub "You win, [player]."
            $ player_wins += 1

        elif moldable_variable == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1eub "We both chose paper!"
            m 1tua "We're in a tie and you should stop reading my mind [mas_get_player_nickname()]~"
            m 1hub "Ahahahaha~"

        elif moldable_variable == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 3eub "The scissors cut the paper."
            m 3hua "Sorry [player], you lost."
            $ moni_wins += 1

    elif rps_your_choice == 3:
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
        if moldable_variable == 1:
            show e_rock zorder 12 as e_rock_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1mub "Say goodbye to your scissors, [player]~"
            m "You couldn't beat me! Ahahaha~"
            $ moni_wins += 1

        elif moldable_variable == 2:
            show e_paper zorder 12 as e_paper_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 1hssdrb "The scissors cuts the paper."
            m 1eua "I award you the victory!"
            $ player_wins += 1

        elif moldable_variable == 3:
            show e_scissors zorder 12 as e_scissors_1 with dissolve:
                xalign 0.7
                yalign 0.1
            m 2hkb "Two scissors equals a tie, [player]!"
            m 2hub "Although it's funny that you thought the same thing, ehehehe~"
    show monika 1hua at t21
    $ rps_your_choice = 0
    jump hide_images_rps
    return

label rps_quit:
    $ mas_MUINDropShield()
    hide screen score_minigame
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
    $ rps_your_choice = 0
    jump rps_result
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label rps_result:
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
        m 3hub "You put up a good fight."
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
        
    python:
        moni_wins = 0
        player_wins = 0
    jump close_extraplus
    return
