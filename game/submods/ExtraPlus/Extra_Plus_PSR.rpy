#===========================================================================================
# MINIGAME#3
#===========================================================================================
#====Rock Paper Scissors
default persistent.psr_result_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]
default rps_your_choice = 0
default player_wins = 0
default moni_wins = 0

label minigame_rps:
    $ mas_MUMURaiseShield()
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

    # Very first time playing
    if not renpy.seen_label("minigame_rps"):
        m 1hua "Rock, Paper, Scissors, [player]! Ready to try your luck?"
        m 1eua "It's a simple game of chance, but sometimes those are the most fun."
        m 1eub "Let's see who fate favors today. Good luck!"

    # If the player won the last game
    elif persistent.psr_result_game[0]:
        m 3eub "Ready for a rematch, [player]? I've been thinking about my strategy. Ehehe~"
        m 3hua "I won't make it so easy for you to win this time!"

    # If Monika won the last game
    elif persistent.psr_result_game[1]:
        m 1hub "So, are you ready to challenge the champion again?"
        m 1hua "I hope you're ready! I plan on keeping my winning streak."

    # If the last game was a tie
    elif persistent.psr_result_game[2]:
        m 1eua "Let's play again! We have to break that tie from last time."
        m 1tua "It feels like we're perfectly in sync. Let's see if that's still true!"

    # Default greeting for subsequent plays
    else:
        m 1hua "Ready for another round of Rock, Paper, Scissors, [player]?"
        m 1eua "It's always nice to relax with a simple game."

    hide card_back
    hide e_rock
    hide e_paper
    hide e_scissors
    show screen score_minigame(game="rps")
    show monika idle at t21
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
    show monika idle at t21
    $ rps_your_choice = 0
    jump hide_images_rps
    return

label rps_quit:
    $ mas_MUMUDropShield()
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
    show monika idle at t11
    #Tie
    if moni_wins == player_wins:
        if moni_wins == 0 and player_wins == 0:
            m 1etd "Don't you want to play rock-paper-scissors?"
            m 1eka "I thought he wanted to play with me for a while..."
            m 3hua "But don't worry, I know you have changed your mind and are not in the mood to play."
            m 3hub "So I hope we can play another time!"
            $ persistent.psr_result_game = [False, False, False]
            python:
                moni_wins = 0
                player_wins = 0
        else:
            m 1sua "Wow, it's a tie."
            m 1tua "It's because we are such a couple that our minds are one!"
            m 1hub "Ehehe~"
            m 3hua "But we have to break the tie, [player]."
            m 3hub "We will see who wins next time, good luck!"
            $ persistent.psr_result_game[2] = True

    #Monika wins
    elif moni_wins > player_wins:
        m 3eub "This time I won, [player]~"
        m 3hub "You put up a good fight."
        m 3eub "I've had some luck."
        m 3eubsa "But don't feel bad, what matters most to me is that we both have fun."
        m 1hub "Next time I know you will beat me, I trust you!"
        $ persistent.psr_result_game[1] = True

    #Player wins
    elif moni_wins < player_wins:
        m 1hub "You beat me [player], congratulations."
        m 1hub "I'm proud of you~"
        m 2tub "But I warn you that next time I will try to read your mind."
        m 2hub "I'm likely to win!"
        m 2hua "So be careful when we play again."
        m 2hua "Ehehe~"
        $ persistent.psr_result_game[0] = True
        
    python:
        moni_wins = 0
        player_wins = 0
    jump close_extraplus
    return
