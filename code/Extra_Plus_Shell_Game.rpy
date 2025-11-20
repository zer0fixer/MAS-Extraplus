#===========================================================================================
# MINIGAME#1
#===========================================================================================
#====Shell Game
default persistent.sg_max_score = 0

image extra_sg_cup:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_cup"
        xalign 0.5 yalign 0.5
image extra_sg_cup_hover:
    contains:
        "extra_cup_hover"
        xalign 0.5 yalign 0.5
image extra_sg_cup_idle:
    contains:
        "extra_cup_idle"
        xalign 0.5 yalign 0.5
image extra_sg_ball:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_ball"
        xalign 0.5 yalign 0.5

init -5 python in ep_sg:
    target_shuffles = 4
    ball_position = 1
    current_turn = 1
    shuffle_cups = 0
    cup_speed = 0.9 
    difficulty = 1 #1-Easy, 2-Normal, 3-Hard, 4-Progressive
    correct_answers = 0
    comment = False
    cup_choice = None
    cup_skin = randomize_cup_skin()
    original_cup = [0, 1, 2]
    cup_coordinates = [695, 925, 1155]
    cup_coordinates_real = [695, 925, 1155]
    #====Comments by moni on standard difficulties
    _compliments = [
        _("Well done, [player]!"),
        _("Impressive, keep it up!"),
        _("You're doing great!"),
        _("Fantastic, [player]!"),
        _("Keep it up!"),
        _("You're making progress!"),
        _("Bravo, [player]!"),
        _("Outstanding, [player]!"),
        _("Way to go, [player]!"),
        _("Keep up the good work, [player]!"),
        _("You're doing fantastic!"),
        _("You're doing amazing!"),
    ]
    _failures = [
        _("Oh, too bad~"),
        _("It's not that, [player]."),
        _("Try again~"),
        _("Don't get distracted, [player]."),
        _("Keep practicing, [player]."),
        _("You'll get it next time!"),
        _("Better luck next try, [player]."),
        _("Don't give up, [player]!"),
        _("That's not quite it, [player]."),
        _("That wasn't the right answer, [player]."),
        _("Sorry, [player], that's not it."),
        _("Not quite, try focusing a bit more!")
    ]

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
                ep_sg.cup_speed = 0.85
                ep_sg.difficulty = 1
                ep_sg.target_shuffles = 4
        "Normal":
            m 3eub "Want to start with a casual game? "
            extend 3hub "Sounds good!"
            python:
                ep_sg.cup_speed = 0.5
                ep_sg.difficulty = 2
                ep_sg.target_shuffles = 6
        "Hard":
            m 3etb "Feeling confident, are we?"
            m 1hub "Ahaha, I like that! Let's do it!"
            python:
                ep_sg.cup_speed = 0.25
                ep_sg.difficulty = 3
                ep_sg.target_shuffles = 8
        "Progressive":
            m 1ttb "A challenge, huh? I like your spirit!"
            m 1hub "Let's start easy and get harder as we go!"
            python:
                ep_sg.cup_speed = 0.7
                ep_sg.difficulty = 4
                ep_sg.target_shuffles = 3

    python:
        store.ep_button.hide_zoom_button()
        # Reset stats for a new game session
        ep_sg.current_turn = 1
        ep_sg.correct_answers = 0

label sg_init_game:
    $ config.allow_skipping = False
    show monika 1eua at t21
    pause 0.2

    show extra_sg_cup zorder 12 as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos -400
        easein_bounce 0.5 ypos 250

    show extra_sg_cup zorder 12 as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show extra_sg_cup zorder 12 as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    pause 1.0

    show extra_sg_ball zorder 12 behind cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 335

    show extra_sg_cup as cup_2:
        linear 0.5 ypos 110

    m 1lub "The ball always starts under the center cup."

    show extra_sg_cup as cup_2:
        linear 0.5 ypos 250

    m 1hub "Watch carefully where it is!"

    hide extra_sg_ball

    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250

    python:
        ep_sg.cup_coordinates_real[0] = 695
        ep_sg.cup_coordinates_real[1] = 925
        ep_sg.cup_coordinates_real[2] = 1155

        ep_sg.original_cup[0] = 0
        ep_sg.original_cup[1] = 1
        ep_sg.original_cup[2] = 2

        ep_sg.ball_position = 1
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

        temp_cup_position = ep_sg.cup_coordinates_real[move_cup_2]
        ep_sg.cup_coordinates_real[move_cup_2] = ep_sg.cup_coordinates_real[move_cup_1]
        ep_sg.cup_coordinates_real[move_cup_1] = temp_cup_position

        if ep_sg.ball_position == move_cup_1:
            ep_sg.ball_position = move_cup_2
        elif ep_sg.ball_position == move_cup_2:
            ep_sg.ball_position = move_cup_1

    $ renpy.pause(ep_sg.cup_speed, hard='True')

    play sound sfx_cup_shuffle

    show extra_sg_cup as cup_1:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[0]

    show extra_sg_cup as cup_2:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[1]

    show extra_sg_cup as cup_3:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[2]

    if ep_sg.shuffle_cups != (ep_sg.target_shuffles - 1):
        $ ep_sg.shuffle_cups += 1
        jump sg_loop_game

    pause 1.0

    show screen shell_game_minigame

    "Select a cup:"

label sg_check_label:

    hide screen shell_game_minigame

    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250
    python:
        ep_sg.cup_coordinates_real[0] = 695
        ep_sg.cup_coordinates_real[1] = 925
        ep_sg.cup_coordinates_real[2] = 1155
        cup_dialogues = ["left", "middle", "right"]
        chosen_cup_dialogue = cup_dialogues[ep_sg.cup_choice]

    m 1eub "You chose the [chosen_cup_dialogue] cup..."

    call sg_reveal_cup(ep_sg.cup_choice, is_chosen=True)

    if ep_sg.comment:
        m 1sub "[renpy.substitute(renpy.random.choice(ep_sg._compliments))]"
    else:
        m 1hub "[renpy.substitute(renpy.random.choice(ep_sg._failures))]"

    if ep_sg.cup_choice != ep_sg.ball_position:
        m 1lub "The correct cup was..."
        call sg_reveal_cup(ep_sg.ball_position, is_chosen=False)
        m 1hua "This!"

    show extra_sg_cup as cup_1:
        linear 0.5 xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        linear 0.5 xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        linear 0.5 xpos ep_sg.cup_coordinates[2] ypos 250

    pause 1.0

    hide extra_sg_ball
    python:
        ep_sg.current_turn += 1
        ep_sg.shuffle_cups = 0
        ep_sg.ball_position = 1
        if ep_sg.difficulty == 4 and ep_sg.current_turn % 6 == 0:
            ep_sg.cup_speed = max(0.15, ep_sg.cup_speed - 0.05)
            ep_sg.target_shuffles += 1
    jump sg_loop_game
    return

label sg_reveal_cup(cup_index, is_chosen):
    if cup_index == 0:
        show extra_sg_cup as cup_1:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_1:
                xpos ep_sg.cup_coordinates[0] ypos 335
    elif cup_index == 1:
        show extra_sg_cup as cup_2:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_2:
                xpos ep_sg.cup_coordinates[1] ypos 335
    elif cup_index == 2:
        show extra_sg_cup as cup_3:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_3:
                xpos ep_sg.cup_coordinates[2] ypos 335

    if is_chosen and cup_index == ep_sg.ball_position:
        $ ep_sg.correct_answers += 1
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label shell_game_result:
    hide screen score_minigame
    python:
        new_high_score = (ep_sg.correct_answers > persistent.sg_max_score)
        enable_esc()
        mas_MUMUDropShield()
        renpy.game.preferences.afm_enable = afm_pref
    hide extra_sg_ball
    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250
        easeout_expo 0.5 ypos -400
    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250
        pause 0.1
        easeout_expo 0.5 ypos -400
    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250
        pause 0.2
        easeout_expo 0.5 ypos -400

    pause 0.8
    hide cup_1
    hide cup_2
    hide cup_3
    hide screen extra_no_click
    show monika at t11

    #The player didn't play any rounds.
    if ep_sg.current_turn == 1 and ep_sg.correct_answers == 0:
        m 1hka "You didn't want to play after all?"
        m 1eua "That's okay, maybe you'll be in the mood next time."
        m 1dub "I'll be here waiting for you, [player]."

    #The player didn't get any correct.
    elif ep_sg.correct_answers == 0:
        m 1eka "[player], are you feeling alright?"
        m 1ekb "We played for [ep_sg.current_turn] rounds and you didn't get any of them right."
        m 1etd "Were you a little distracted, maybe?"
        if ep_sg.difficulty == 4: # Dialogue for Progressive
            m 3eka "That progressive mode can be tricky at first. The speed really ramps up!"
            m 3hua "Don't worry about it, I'm sure you'll get the hang of it."
        else:
            m 1hua "It's okay, everyone has off-days. Let's do something that cheers you up!"

    #Perfect score!
    elif ep_sg.correct_answers == ep_sg.current_turn:
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
            m 1hubsb "You set a new record of [ep_sg.correct_answers]! That's awesome!"
            m 1eua "Even with a few slip-ups, you still managed to beat your best score. That's real progress!"
        else:
            m 1hua "You got [ep_sg.correct_answers] correct. You did a great job!"
            if ep_sg.difficulty == 4: # Dialogue for Progressive
                m 3hua "Keeping up with the progressive speed is tough, but you held on for a long time!"
            else:
                m 3hub "It's just a matter of practice. I know you'll beat your record of [persistent.sg_max_score] soon!"

    m 1hubsa "Well, thank you for playing with me. I had a lot of fun!"
    if ep_sg.current_turn > 50:
        m 3eka "And also, please rest your eyes for a bit. We played for quite a while..."
        m 1dub "I always get concerned about your health, you know~"

    window hide
    python:
        if ep_sg.correct_answers > persistent.sg_max_score:
            persistent.sg_max_score = ep_sg.correct_answers
        ep_sg.current_turn = 0
        ep_sg.correct_answers = 0 # Reset for next session
        ep_sg.target_shuffles = 6
        ep_sg.shuffle_cups = 0
        
    jump close_extraplus
    return