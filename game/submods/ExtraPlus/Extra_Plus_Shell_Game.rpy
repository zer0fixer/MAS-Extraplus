#===========================================================================================
# MINIGAME#1
#===========================================================================================
#====Shell Game
default persistent.sg_max_score = 0
default sg_target_shuffles = 4
define sg_original_cup = [0, 1, 2]
default sg_ball_position = 1
default sg_current_turn = 1
default sg_shuffle_cups = 0
default sg_cup_speed = 0.9 
define difficulty_sg = 1 #1-Easy, 2-Normal, 3-Hard, 4-Progressive
default sg_correct_answers = 0
default sg_plus_comment = False
default sg_cup_choice = None
define sg_cup_coordinates = [695, 925, 1155]
default sg_cup_coordinates_real = [695, 925, 1155]
define sg_cup_list = ["cup.png", "cup_monika.png", "cup_yuri.png", "cup_natsuki.png", "cup_sayori.png"]
default sg_cup_skin = None

label minigame_sg:
    show monika 1eub at t11
    if renpy.seen_label("minigame_sg"):
        m 1eta "You want to play the shell game again, [player]? "
        if persistent.sg_max_score == 0:
            m 1eka "By the way, I wanted to apologize..."
            m 3lkb "I just realized there was a bug in my code that was preventing your high score from being saved correctly."
            m 1hubsb "I've fixed it now, though! So from this point on, I'll be keeping track of your record."
            m "Good luck setting a new high score!"
        else:
            m 1sua "Great! Let's see if you can beat your record of [persistent.sg_max_score] correct answers in a row!"
    else:
        m 1etb "You want to play the shell game with me, [player]? "
        m 1sua "It's a game of skill and reflexes. I think you'll like it!"
        m 1eua "The rules are simple: I'll hide a ball under one of these cups and shuffle them around."
        m 1hub "You just have to guess which cup the ball is under."
        m 1eub "If you guess right, you score a point!"

    m 1hua "Alright, what difficulty do you want to play on?{nw}"
    menu:
        "Alright, what difficulty do you want to play on?{fast}"
        "Easy":
            m 1eua "Feeling like taking it easy, [player]? "
            extend 1hua "Alright!"
            python:
                sg_cup_speed = 0.85
                difficulty_sg = 1
                sg_target_shuffles = 4
        "Normal":
            m 3eub "Want to start with a casual game? "
            extend 3hub "Sounds good!"
            python:
                sg_cup_speed = 0.5
                difficulty_sg = 2
                sg_target_shuffles = 6
        "Hard":
            m 3etb "Feeling confident, are we?"
            m 1hub "Ahaha, I like that! Let's do it!"
            python:
                sg_cup_speed = 0.25
                difficulty_sg = 3
                sg_target_shuffles = 8
        "Progressive":
            m 1ttb "A challenge, huh? I like your spirit!"
            m 1hub "Let's start easy and get harder as we go!"
            python:
                sg_cup_speed = 0.7
                difficulty_sg = 4
                sg_target_shuffles = 3

    python:
        # Reset stats for a new game session
        sg_current_turn = 1
        sg_correct_answers = 0

label sg_init_game:
    $ config.allow_skipping = False
    show monika 1eua at t21
    pause 0.2

    show cup zorder 12 as cup_1:
        xpos sg_cup_coordinates[0] ypos -400
        easein_bounce 0.5 ypos 250

    show cup zorder 12 as cup_2:
        xpos sg_cup_coordinates[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show cup zorder 12 as cup_3:
        xpos sg_cup_coordinates[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    pause 1.0

    show ball zorder 12 behind cup_2:
        xpos sg_cup_coordinates[1] ypos 335

    show cup as cup_2:
        linear 0.5 ypos 110

    m 1lub "The ball always starts under the center cup."

    show cup as cup_2:
        linear 0.5 ypos 250

    m 1hub "Watch carefully where it is!"

    hide ball

    show cup as cup_1:
        xpos sg_cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos sg_cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos sg_cup_coordinates[2] ypos 250

    python:
        sg_cup_coordinates_real[0] = 695
        sg_cup_coordinates_real[1] = 925
        sg_cup_coordinates_real[2] = 1155

        sg_original_cup[0] = 0
        sg_original_cup[1] = 1
        sg_original_cup[2] = 2

        sg_ball_position = 1
        disable_esc()
        mas_MUMURaiseShield()
        afm_pref = renpy.game.preferences.afm_enable
        renpy.game.preferences.afm_enable = False
    show screen score_minigame(game="sg")

label sg_loop_game:
    show monika 1eua
    show screen extra_no_click
    python:
        move_cup_1, move_cup_2 = renpy.random.sample(range(3), 2)

        temp_cup_position = sg_cup_coordinates_real[move_cup_2]
        sg_cup_coordinates_real[move_cup_2] = sg_cup_coordinates_real[move_cup_1]
        sg_cup_coordinates_real[move_cup_1] = temp_cup_position

        if sg_ball_position == move_cup_1:
            sg_ball_position = move_cup_2
        elif sg_ball_position == move_cup_2:
            sg_ball_position = move_cup_1

    $ renpy.pause(sg_cup_speed, hard='True')

    play sound "Submods/ExtraPlus/submod_assets/sfx/cup_shuffle.mp3"

    show cup as cup_1:
        ease sg_cup_speed xpos sg_cup_coordinates_real[0]

    show cup as cup_2:
        ease sg_cup_speed xpos sg_cup_coordinates_real[1]

    show cup as cup_3:
        ease sg_cup_speed xpos sg_cup_coordinates_real[2]

    if sg_shuffle_cups != (sg_target_shuffles - 1):
        $ sg_shuffle_cups += 1
        jump sg_loop_game

    pause 1.0

    show screen shell_game_minigame

    "Select a cup:"

label sg_check_label:

    hide screen shell_game_minigame

    show cup as cup_1:
        xpos sg_cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos sg_cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos sg_cup_coordinates[2] ypos 250
    python:
        sg_cup_coordinates_real[0] = 695
        sg_cup_coordinates_real[1] = 925
        sg_cup_coordinates_real[2] = 1155

    if sg_cup_choice == 0:
        m 1eub "You chose the left cup..."
        show cup as cup_1:
            linear 0.5 ypos 110
        if sg_cup_choice == sg_ball_position:
            show ball zorder 12 behind cup_1:
                xpos sg_cup_coordinates[0] ypos 335
            $ sg_correct_answers += 1

    elif sg_cup_choice == 1:
        m 1eub "You chose the middle cup..."
        show cup as cup_2:
            linear 0.5 ypos 110
        if sg_cup_choice == sg_ball_position:
            show ball zorder 12 behind cup_2:
                xpos sg_cup_coordinates[1] ypos 335
            $ sg_correct_answers += 1

    elif sg_cup_choice == 2:
        m 1eub "You chose the right cup..."
        show cup as cup_3:
            linear 0.5 ypos 110
        if sg_cup_choice == sg_ball_position:
            show ball zorder 12 behind cup_3:
                xpos sg_cup_coordinates[2] ypos 335
            $ sg_correct_answers += 1

    if sg_plus_comment is True:
        m 1sub "[renpy.substitute(renpy.random.choice(_plus_complies))]"

    elif sg_plus_comment is False:
        m 1hub "[renpy.substitute(renpy.random.choice(_plus_not_met))]"

    if sg_cup_choice != sg_ball_position:

        m 1lub "The correct cup was..."

        if sg_ball_position == 0:
            show cup as cup_1:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_1:
                xpos sg_cup_coordinates[0] ypos 335

        elif sg_ball_position == 1:
            show cup as cup_2:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_2:
                xpos sg_cup_coordinates[1] ypos 335

        elif sg_ball_position == 2:
            show cup as cup_3:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_3:
                xpos sg_cup_coordinates[2] ypos 335

        m 1hua "This!"

    show cup as cup_1:
        linear 0.5 xpos sg_cup_coordinates[0] ypos 250

    show cup as cup_2:
        linear 0.5 xpos sg_cup_coordinates[1] ypos 250

    show cup as cup_3:
        linear 0.5 xpos sg_cup_coordinates[2] ypos 250

    pause 1.0

    hide ball
    python:
        store.sg_current_turn += 1
        store.sg_shuffle_cups = 0
        store.sg_ball_position = 1
        if difficulty_sg == 4 and sg_current_turn % 6 == 0:
            store.sg_cup_speed = max(0.15, sg_cup_speed - 0.05)
            store.sg_target_shuffles += 1
    jump sg_loop_game
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label shell_game_result:
    hide screen score_minigame
    python:
        new_high_score = (sg_correct_answers > persistent.sg_max_score)
        enable_esc()
        mas_MUMUDropShield()
        renpy.game.preferences.afm_enable = afm_pref
    hide ball
    show cup as cup_1:
        xpos sg_cup_coordinates[0] ypos 250
        easeout_expo 0.5 ypos -400
    show cup as cup_2:
        xpos sg_cup_coordinates[1] ypos 250
        pause 0.1
        easeout_expo 0.5 ypos -400
    show cup as cup_3:
        xpos sg_cup_coordinates[2] ypos 250
        pause 0.2
        easeout_expo 0.5 ypos -400

    pause 0.8
    hide cup_1
    hide cup_2
    hide cup_3
    hide screen extra_no_click
    show monika at t11

    #The player didn't play any rounds.
    if sg_current_turn == 1 and sg_correct_answers == 0:
        m 1hka "You didn't want to play after all?"
        m 1eua "That's okay, maybe you'll be in the mood next time."
        m 1dub "I'll be here waiting for you, [player]."

    #The player didn't get any correct.
    elif sg_correct_answers == 0:
        m 1eka "[player], are you feeling alright?"
        m 1ekb "We played for [sg_current_turn] rounds and you didn't get any of them right."
        m 1etd "Were you a little distracted, maybe?"
        if difficulty_sg == 4: # Dialogue for Progressive
            m 3eka "That progressive mode can be tricky at first. The speed really ramps up!"
            m 3hua "Don't worry about it, I'm sure you'll get the hang of it."
        else:
            m 1hua "It's okay, everyone has off-days. Let's do something that cheers you up!"

    #Perfect score!
    elif sg_correct_answers == sg_current_turn:
        m 2sub "Wow, a perfect score! You got every single one right!"
        if new_high_score:
            m 1hubsa "And it's a new high score! Congratulations, [player]! I'm so proud of you."
        else:
            m 1hubsb "You matched your high score perfectly. Your focus is amazing!"
        m 3eub "You have some really sharp eyes, ehehe~"

    #Mixed result (some correct, some failed).
    else:
        m 1eua "That was a good run, [player]!"
        if new_high_score:
            m 1hubsb "You set a new record of [sg_correct_answers]! That's awesome!"
            m 1eua "Even with a few slip-ups, you still managed to beat your best score. That's real progress!"
        else:
            m 1hua "You got [sg_correct_answers] correct. You did a great job!"
            if difficulty_sg == 4: # Dialogue for Progressive
                m 3hua "Keeping up with the progressive speed is tough, but you held on for a long time!"
            else:
                m 3hub "It's just a matter of practice. I know you'll beat your record of [persistent.sg_max_score] soon!"

    m 1hubsa "Well, thank you for playing with me. I had a lot of fun!"
    if sg_current_turn > 15:
        m 3eka "And also, please rest your eyes for a bit. We played for quite a while..."
        m 1dub "I always get concerned about your health, you know~"

    window hide
    python:
        if sg_correct_answers > persistent.sg_max_score:
            persistent.sg_max_score = sg_correct_answers
        sg_current_turn = 0
        sg_correct_answers = 0 # Reset for next session
        sg_target_shuffles = 6
        sg_shuffle_cups = 0
    jump close_extraplus
    return