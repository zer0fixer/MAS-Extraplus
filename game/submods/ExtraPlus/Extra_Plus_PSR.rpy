#===========================================================================================
# MINIGAME#3
#===========================================================================================
#====Rock Paper Scissors
default persistent.psr_result_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]
default -5 persistent.rps_player_history = []

init python in ep_rps:
    import store
    
    class RPSChoice:
        """
        Represents a single choice in the Rock, Paper, Scissors game.
        """
        def __init__(self, name, value, image, beats):
            """
            Initializes a new RPSChoice.

            Args:
                name (str): The display name of the choice (e.g., "Rock").
                value (int): The numerical identifier for the choice (1: Rock, 2: Paper, 3: Scissors).
                image (str): The name of the image displayable for this choice.
                beats (int): The numerical value of the choice that this one beats.
            """
            self.name = name
            self.value = value
            self.image = image
            self.beats = beats

    your_choice = 0
    player_wins = 0
    moni_wins = 0
    choices = [RPSChoice("Rock", 1, "extra_rock", 3), RPSChoice("Paper", 2, "extra_paper", 1), RPSChoice("Scissors", 3, "extra_scissors", 2)]


    def get_monika_choice():
        """
        Determines Monika's choice based on the player's history.
        """
        history = store.persistent.rps_player_history
        
        # If there's not much history, or with a 30% chance, play randomly.
        if len(history) < 3 or renpy.random.randint(1, 100) <= 30:
            return renpy.random.randint(1, 3)

        # --- AI Logic ---
        
        # 1. Frequency Analysis: What is the player's most common move?
        # We count how many times the player has chosen each option.
        rock_count = history.count(1)
        paper_count = history.count(2)
        scissors_count = history.count(3)

        # Find the most frequent move.
        player_most_frequent_move = 0
        max_count = -1
        if rock_count > max_count:
            max_count = rock_count
            player_most_frequent_move = 1
        if paper_count > max_count: # Use 'if' instead of 'elif' to handle ties, defaulting to the last one checked.
            max_count = paper_count
            player_most_frequent_move = 2
        if scissors_count > max_count:
            max_count = scissors_count
            player_most_frequent_move = 3

        # Monika chooses the counter to the player's most frequent move.
        # choices[0] = Rock (1), beats Scissors (3)
        # choices[1] = Paper (2), beats Rock (1)
        # choices[2] = Scissors (3), beats Paper (2)
        # The 'beats' value is the 'value' of the move it wins against.
        # To counter, Monika should choose the move that has the player's most frequent move as its 'beats' value.
        counter_move = [c.value for c in choices if c.beats == player_most_frequent_move][0]


        # 2. Anti-Repetition Pattern: If the player repeated their last move, they are less likely to repeat it a third time.
        # For example, if they played Rock, Rock, they are now more likely to play Paper or Scissors.
        # Monika can play Scissors, which beats Paper and ties with Scissors, making it a safe bet.
        if len(history) >= 2 and history[-1] == history[-2]:
            last_move = history[-1]
            # The move that beats the player's last move.
            move_that_beats_player = [c.value for c in choices if c.beats == last_move][0]
            # Monika chooses the move that beats 'move_that_beats_player'.
            # This is a strategy to cover the player's two most likely options.
            smart_bet = [c.value for c in choices if c.beats == move_that_beats_player][0]
            # There's a 50% chance she'll use this strategy instead of the frequency analysis.
            if renpy.random.randint(1, 2) == 1:
                return smart_bet
        
        # Fallback to the counter move if the anti-repetition logic wasn't used
        return counter_move

label minigame_rps:
    $ mas_MUMURaiseShield()
    show extra_card_back zorder 12:
        xalign 0.7
        yalign 0.1
        yoffset -900
        easein 0.5 yoffset 0
    show extra_rock zorder 12:
        xalign 0.5
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.1
    show extra_paper zorder 12:
        xalign 0.7
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.2
    show extra_scissors zorder 12:
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

    hide extra_card_back
    hide extra_rock
    hide extra_paper
    hide extra_scissors
    show screen score_minigame(game="rps")
    show monika idle at t21
    call screen RPS_mg nopredict
    return

label rps_loop:
    $ store.persistent.rps_player_history.append(ep_rps.your_choice)
    $ monika_choice_val = ep_rps.get_monika_choice()
    $ renpy.restart_interaction()
    $ player_choice = ep_rps.choices[ep_rps.your_choice - 1]
    $ monika_choice = ep_rps.choices[monika_choice_val - 1]

    # Show player's and Monika's choices
    show extra_card_back as monika_card_back zorder 12:
        xalign 0.7
        yalign 0.1

    # Show all choices at their default positions
    show extra_rock zorder 12:
        xalign 0.5 yalign 0.7
    show extra_paper zorder 12:
        xalign 0.7 yalign 0.7
    show extra_scissors zorder 12:
        xalign 0.9 yalign 0.7

    # Adjust yoffset for player's choice
    if player_choice.value == 1: # Rock
        show extra_rock:
            yoffset -20
    elif player_choice.value == 2: # Paper
        show extra_paper:
            yoffset -20
    elif player_choice.value == 3: # Scissors
        show extra_scissors:
            yoffset -20

    m 1eub "Rock,{w=0.3} Paper,{w=0.3} Scissors{w=0.3}!{nw}"
    hide monika_card_back with dissolve

    # Show Monika's choice
    show expression monika_choice.image as monika_choice_display zorder 12 with dissolve:
        xalign 0.7
        yalign 0.1

    # Determine winner and show dialogue
    if monika_choice.value == player_choice.value:
        # Tie
        if player_choice.value == 1: # Rock
            m 3hub "A rock against another rock, ahahaha~"
            m 1hua "It is a tie."
        elif player_choice.value == 2: # Paper
            m 1eub "We both chose paper!"
            m 1tua "We're in a tie and you should stop reading my mind [mas_get_player_nickname()]~"
            m 1hub "Ahahahaha~"
        elif player_choice.value == 3: # Scissors
            m 2hkb "Two scissors equals a tie, [player]!"
            m 2hub "Although it's funny that you thought the same thing, ehehehe~"

    elif player_choice.beats == monika_choice.value:
        # Player wins
        $ ep_rps.player_wins += 1
        if player_choice.value == 1: # Rock vs Scissors
            m 1hksdrb "The rock breaks the scissors."
            m 1hua "You beat me, [player]!"
        elif player_choice.value == 2: # Paper vs Rock
            m 1lkb "The paper wraps the rock."
            m 1lub "You win, [player]."
        elif player_choice.value == 3: # Scissors vs Paper
            m 1hssdrb "The scissors cuts the paper."
            m 1eua "I award you the victory!"

    else:
        # Monika wins
        $ ep_rps.moni_wins += 1
        if monika_choice.value == 1: # Rock vs Scissors (Player)
            m 1mub "Say goodbye to your scissors, [player]~"
            m "You couldn't beat me! Ahahaha~"
        elif monika_choice.value == 2: # Paper vs Rock (Player)
            m 1dub "The paper wraps the rock."
            m 1tub "So sorry, [player], you have lost!"
        elif monika_choice.value == 3: # Scissors vs Paper (Player)
            m 3eub "The scissors cut the paper."
            m 3hua "Sorry [player], you lost."

    hide monika_choice_display
    show monika idle at t21
    $ ep_rps.your_choice = 0
    jump hide_images_rps
    return

label rps_quit:
    $ mas_MUMUDropShield()
    hide screen score_minigame
    
    show extra_card_back zorder 12:
        xalign 0.7 yalign 0.1
    show extra_rock zorder 12:
        xalign 0.5 yalign 0.7
    show extra_paper zorder 12:
        xalign 0.7 yalign 0.7
    show extra_scissors zorder 12:
        xalign 0.9 yalign 0.7
    
    show extra_card_back:
        easeout 0.6 yoffset -1300
    show extra_rock:
        easeout 0.6 yoffset 1300
    pause 0.1
    
    show extra_paper:
        easeout 0.6 yoffset 1300
    pause 0.2
    
    show extra_scissors:
        easeout 0.6 yoffset 1300
    pause 0.3
    
    hide extra_card_back
    hide extra_rock
    hide extra_paper
    hide extra_scissors
    
    $ ep_rps.your_choice = 0
    jump rps_result
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label rps_result:
    show monika idle at t11
    #Tie
    if ep_rps.moni_wins == ep_rps.player_wins:
        if ep_rps.moni_wins == 0 and ep_rps.player_wins == 0:
            m 1etd "Don't you want to play rock-paper-scissors?"
            m 1eka "I thought he wanted to play with me for a while..."
            m 3hua "But don't worry, I know you have changed your mind and are not in the mood to play."
            m 3hub "So I hope we can play another time!"
            python:
                ep_rps.moni_wins = 0
                ep_rps.player_wins = 0
        else:
            m 1sua "Wow, it's a tie."
            m 1tua "It's because we are such a couple that our minds are one!"
            m 1hub "Ehehe~"
            m 3hua "But we have to break the tie, [player]."
            m 3hub "We will see who wins next time, good luck!"
            $ persistent.psr_result_game[2] = True

    #Monika wins
    elif ep_rps.moni_wins > ep_rps.player_wins:
        m 3eub "This time I won, [player]~"
        m 3hub "You put up a good fight."
        m 3eub "I've had some luck."
        m 3eubsa "But don't feel bad, what matters most to me is that we both have fun."
        m 1hub "Next time I know you will beat me, I trust you!"
        $ persistent.psr_result_game[1] = True

    #Player wins
    elif ep_rps.moni_wins < ep_rps.player_wins:
        m 1hub "You beat me [player], congratulations."
        m 1hub "I'm proud of you~"
        m 2tub "But I warn you that next time I will try to read your mind."
        m 2hub "I'm likely to win!"
        m 2hua "So be careful when we play again."
        m 2hua "Ehehe~"
        $ persistent.psr_result_game[0] = True
        
    python:
        ep_rps.moni_wins = 0
        ep_rps.player_wins = 0
        ep_tools.seen_notification_games = False
    jump close_extraplus
    return