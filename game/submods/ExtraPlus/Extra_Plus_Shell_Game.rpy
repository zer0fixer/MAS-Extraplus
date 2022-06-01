################################################################################
## MINIGAME#1
################################################################################
#Shell Game
label minigame_sg:
    if correct_answers > 0 or current_turn > 0:
        jump cheat_sg
    show monika 1eub at t11
    m 1hua "Okay, what difficulty do you want?{nw}"
    menu:
        "Okay, what difficulty do you want?{fast}"
        "Easy":
            m 1eua "You want to play something simple, ok."
            $ cup_speed += 0.5
            $ difficulty_sg = 1
        "Normal":
            m 3eub "You want to start casual?, okay"
            $ cup_speed = 0.5
            $ difficulty_sg = 2
        "Hard":
            m 1eub "You want to play hard, ok."
            $ cup_speed -= 0.3
            $ difficulty_sg = 3

label restart_sg:
    if not persistent._mas_pm_cares_about_dokis:
        $ cup_skin = renpy.random.choice(["cup", "cup_monika"])
    show monika 1eua at t21

    pause 0.2

    show cup zorder 12 as cup_1:
        xpos cup_coordinates[0] ypos -400
        easein_bounce 0.5 ypos 250

    show cup zorder 12 as cup_2:
        xpos cup_coordinates[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250
        
    show cup zorder 12 as cup_3:
        xpos cup_coordinates[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    pause 1.0

    show ball zorder 12 behind cup_2:
        xpos cup_coordinates[1] ypos 335

    show cup as cup_2:
        linear 0.5 ypos 110

    m 1lub "There's the ball, don't lose sight of it."

    show cup as cup_2:
        linear 0.5 ypos 250

    m 3hub "Okay, let's see your reflexes!"

    hide ball

    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250

    $ cup_coordinates_real[0] = 695
    $ cup_coordinates_real[1] = 925
    $ cup_coordinates_real[2] = 1155

    $ original_cup[0] = 0
    $ original_cup[1] = 1
    $ original_cup[2] = 2

    $ ball_position = 1
    $ disable_esc()
    $ mas_MUMURaiseShield()

label loop_game:
    show monika 1eua
    show screen no_click
    python:
        move_cup_1 = renpy.random.randint(0,2)
        move_cup_2 = renpy.random.randint(0,2)
        while move_cup_2 == move_cup_1:
            move_cup_2 = renpy.random.randint(0,2)

        temp_cup_position = cup_coordinates_real[move_cup_2]
        cup_coordinates_real[move_cup_2] = cup_coordinates_real[move_cup_1]
        cup_coordinates_real[move_cup_1] = temp_cup_position

        temp_original_cup = original_cup[move_cup_2]
        original_cup[move_cup_2] = original_cup[move_cup_1]
        original_cup[move_cup_1] = temp_original_cup

        if original_cup[move_cup_1] == ball_position:
            ball_position = original_cup[move_cup_2]
            
        elif original_cup[move_cup_2] == ball_position:
            ball_position = original_cup[move_cup_1]

    #Pausa el tiempo necesario para mostra el movimiento de los vasos
    $ renpy.pause(cup_speed, hard='True')

    play sound "submods/ExtraPlus/submod_assets/sfx/cup_shuffle.mp3"

    show cup as cup_1:
        ease cup_speed xpos cup_coordinates_real[0]

    show cup as cup_2:
        ease cup_speed xpos cup_coordinates_real[1]

    show cup as cup_3:
        ease cup_speed xpos cup_coordinates_real[2]

    #Desplasamiento de los vasos.
    if shuffle_cups != 3:
        $ shuffle_cups += 1
        jump loop_game

    pause 1.0

    show screen no_click
    show screen shell_game_minigame

    "Select a cup:"

label check_label:

    $ current_turn += 1

    hide screen no_click
    hide screen shell_game_minigame

    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250

    $ cup_coordinates_real[0] = 695
    $ cup_coordinates_real[1] = 925
    $ cup_coordinates_real[2] = 1155

    #Se muestra los vasos y debe de elegir un vaso
    if your_choice == 0:

        show cup as cup_1:
            linear 0.5 ypos 110

        if your_choice == ball_position:
            show ball zorder 12 behind cup_1:
                xpos cup_coordinates[0] ypos 335

    elif your_choice == 1:

        show cup as cup_2:
            linear 0.5 ypos 110

        if your_choice == ball_position:
            show ball zorder 12 behind cup_2:
                xpos cup_coordinates[1] ypos 335

    elif your_choice == 2:

        show cup as cup_3:
            linear 0.5 ypos 110

        if your_choice == ball_position:
            show ball zorder 12 behind cup_3:
                xpos cup_coordinates[2] ypos 335

    if comment is True:
        m 1sub "[comments_good]"

    elif comment is False:
        m 1hub "[comments_bad]"

    if your_choice != ball_position:

        m 1lub "The correct cup was..."

        #Se comprobara en donde esta la bola
        if ball_position == 0:

            show cup as cup_1:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_1:
                xpos cup_coordinates[0] ypos 335

        elif ball_position == 1:

            show cup as cup_2:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_2:
                xpos cup_coordinates[1] ypos 335

        elif ball_position == 2:

            show cup as cup_3:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_3:
                xpos cup_coordinates[2] ypos 335

        m 1hua "This!"

    show cup as cup_1:
        linear 0.5 xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        linear 0.5 xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        linear 0.5 xpos cup_coordinates[2] ypos 250

    pause 1.0

    hide ball
    $ shuffle_cups = 0
    jump loop_game
    return

################################################################################
## TALKING GAME
################################################################################
label shell_game_result:
    $ enable_esc()
    $ mas_MUINDropShield()
    hide ball
    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250
        easeout_expo 0.5 ypos -400
    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250
        pause 0.1
        easeout_expo 0.5 ypos -400
    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250
        pause 0.2
        easeout_expo 0.5 ypos -400
    pause 0.8
    hide cup_1
    hide cup_2
    hide cup_3
    hide screen no_click
    show monika at t11

    if current_turn == 0:
        m 3ekd "[player], we haven't even started to play."
        m 2gkp "I wanted to play with you for a while."
        m 2etb "But, would you like to continue playing?{nw}"
        menu:
            "But, would you like to continue playing?{fast}"
            "Yes":
                jump restart_sg 
            "No":
                m 1hua "Ok, we'll do it another time."
    
    elif current_turn <= 10 or current_turn >= 10:
        if correct_answers == current_turn:
            m 1hub "Even though we've only played a few turns, you've already made a good impression on me!"
            m "You looked great every turn."
            m 1hua "I guess you don't have time today."
            m 1eua "I hope you go further next time."
            m 1eub "I look forward to it!"
        elif correct_answers < current_turn:
            m 1hua "Don't worry that you failed once."
            m 3hub "You did very well!"
            m "It's just a matter of practice and you'll see how everything will get easier!"
            m 3hua "Next time you'll do better~"
        elif correct_answers == 0:
            m 1eka "I have some concerns about how your result turned out."
            m 1ekb "We've been [current_turn] turns and you haven't gotten any of them right."
            m 1etd "Oh, are you too unmotivated?"
            if difficulty_sg == 1:
                m 1eua "Well, since you are on easy difficulty."
                m 1rkb "I guess you got bored because of how slow the cups were going, you know that's how the [player] difficulty is."
                m "You'd have to try the other difficulties if you want to challenge yourself."
                m 1hua "Oh let's leave all this for another day."
            elif difficulty_sg == 2:
                m 1eua "On normal difficulty."
                m 1rkb "You saw it was no big deal and didn't pay attention to the game."
                m 3hua "You know, you can try the hard difficulty if you want."
                m "Maybe it will motivate you to go further."
                m 3hka "Or you can save it for another day, it's up to you."
            elif difficulty_sg == 3:
                m 1eua "Considering you are on the hard difficulty."
                m 1rkb "You didn't take the time to follow the ball."
                m 1rsb "Although by reflex you should have been able to hit it sometime."
                m "But that wasn't the case."
                m 3hua "You're fine with doing something else, put aside the mini-games and let's do something that motivates you."
                if renpy.seen_label("to_cafe_loop"):
                    m 1eubsa "We can go out on a date again, like to the cafe we went to see."
                    m 1eubsb "Maybe it will lift your spirits a little."
                    m 2eka "But if you want to do absolutely nothing."
                    m 2dka "I hope my presence is enough for you~"
        m 1dubla "And thanks for playing with me [mas_get_player_nickname()]."

    elif current_turn >= 50:
        if correct_answers == current_turn:
            m 2sub "Wow, you always give me a good impression in everything you do [mas_get_player_nickname()]."
            m "Congratulations!"
            m 3hub "You sure have some good reflexes!"
            m 3hua "I won't worry about you failing at a carnival game, ehehe~"
            m 1tubsb "It will be nice to see when you win a teddy bear for me when we have a date there!"
        elif correct_answers < current_turn:
            m 3hua "You did what you could [mas_get_player_nickname()]."
            m 3hub "I'm so happy for you!"
            m "We were already on the [current_turn] shift."
            m 1ekb "So I understand that you couldn't go on any longer and left it at this point."
            m 5hua "But someday you'll make it perfect, just be patient and practice a little."
        elif correct_answers == 0:
            m 1esb "I have a question [player]."
            m 1eka "We've been [current_turn] turns and you haven't hit any."
            m 1etd "Is something wrong?"
            if difficulty_sg == 1:
                m 1eka "Well, since you are on the easy difficulty."
                m 1eta "You wanted to train your reflexes little by little?"
                m 1hua "There's nothing wrong with doing everything in reverse."
                m 3ekb "Although try not to forget that the game is about seeing where the ball is."
            elif difficulty_sg == 2:
                m 1eka "Being on normal difficulty."
                m 1eta "Are you trained to lose every round?"
                m 1hua "I imagine you're going more beech, since we're on [current_turn] turn."
                m 1rtd "Although I wonder where this idea of yours [player] came from."
                m 1gsu "I'd better keep my doubt to myself, I'm going to see how far you can go."
            elif difficulty_sg == 3:
                m 1eka "Considering that you are in the difficult difficulty."
                m 1hua "I feel you have given your best effort to achieve a challenge."
                m 1etb "You wanted to get to more than [current_turn] turns with failures?"
                m 1eub "Well I encourage you to make it!"
                m 1lta "You might be wondering if I worry that you will fail until [current_turn] turn."
                m 1dua "Not really, at this point I feel like you're doing it with intention."
                m 1hksdlb "I'm sorry that I encourage you to fail instead of getting every turn right."
                m "But you're already doing it so I have no choice but to support you."
        m 1eua "I'm glad you like this minigame, though."
        if renpy.seen_label("game_chess"):
            m 3eub "It's not like chess, you need to use strategies."
            m "But it's good to play other games don't you think?"
        m 1eka "I didn't think you would like it because the gameplay is so simple."
        m 4hub "Well I thank you for playing with me [mas_get_player_nickname()]!"
        m "We'll play some other time if that's okay with you."
    
    elif current_turn >= 100:
        if correct_answers == current_turn:
            m 1hua "I must applaud you, [player]."
            m 1hub "You got it right every turn, it shows the concentration you had every turn!"
            m 1hublb "I'm proud of you!"
            m 1ekb "I would love to give you something as a prize but I can't do anything from here, ahaha..."
            m 3hua "Yes you have really trained your reflexes a lot."
            m 1eub "I feel like you're good at rhythm video games."
            m 1eta "Or is it your self-defense system, "
            extend 1sua "If so I'm glad to hear it."
        elif correct_answers < current_turn:
            m 1hua "Not bad [player]."
            m 1hub "You gave your best, considering you made it to the [current_turn] turn!"
            m 1eka "It's normal for you to have a visual fatigue."
            m "So don't lose heart."
            m 3eub "Next time you'll do better, believe me~"
        elif correct_answers == 0:
            m 1hka "I don't know how to feel about that."
            m "We've been [current_turn] turns and you haven't gotten any of them right."
            m 1etb "At this point I feel like it's kind of a challenge to yourself?"
            if difficulty_sg == 1:
                m 1eua "Well as you are on the easy difficulty."
                m 3wud "It is easy to accomplish this, however it is a very time consuming thing to do."
                m 3hub "I'm surprised at how much time you've invested!"
            elif difficulty_sg == 2:
                m 1eua "Being on normal difficulty."
                m 3eub "You had a chance of hitting at least one."
                m 1hub "I'd like to see your face when you did this, ehehe~"
            elif difficulty_sg == 3:
                m 1eua "Considering that you are on hard difficulty."
                m 1sub "I'm amazed at the dedication you put into it."
                m 1hub "You really took it seriously in failing on purpose, ehehe~"
        m 1hubsa "Well, I thank you for taking the time to play with me, I had a lot of fun!"
        m 3eka "And also rest your eyes for a while, we played this mini-game for quite a while."
        m 3hub "You've earned it!"
        m 1dub "I am very concerned about your health, [mas_get_player_nickname()]"
        m 1dua "And don't worry about me, I'll be waiting for you."

    window hide
    $ cup_speed = 0.5
    $ current_turn = 0
    $ correct_answers = 0
    jump return_extra
    return

label cheat_sg:
    show monika 1hua at t11
    if renpy.seen_label("check_cheat_sg"):
        jump check_cheat_minigame
    else:
        jump check_cheat_sg
label check_cheat_sg:
    m 1hub "I'm surprised you modified this minigame, ahaha~"
    m 3esb "After all it is progressive, there is no winner."
    m 3nub "You know you don't have to!"
    m 1eua "The purpose of the mini-games is to have fun for a while."
    m 1etb "Why don't we try again?"
    m 1eud "Or if you want we can play another time."
    m 1hua "Whatever we do will always be unique with you by my side."
    m "Ehehe~"
    jump return_extra
    return