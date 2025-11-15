#===========================================================================================
# MINIGAME#2
#===========================================================================================
#====Tic-Tac-Toe
default persistent.ttt_result_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]

init -5 python in ep_ttt:
    game = None
    colors = [
        "'",
        "#0142a4",
        "0",
        "#a80000"
    ]

image ttt_cross:
    Text(ep_ttt.colors[0],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[1],
        outlines = []
    )
    on show:
        alpha 0.5
        linear 0.25 alpha 1.0
image ttt_cross_cursor:
    Text(ep_ttt.colors[0],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[1],
        outlines = []
    )
    alpha 0.25
    truecenter
image ttt_circle:
    Text(ep_ttt.colors[2],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[3],
        outlines = []
    )
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0

init 10 python in ep_ttt:
    import store

    class TicTacToeGame(object):
        def __init__(self):
            self.field = [None] * 9
            self.playerTurn = True
            self.state = 0
            self.score = [0, 0]

        def check_line(self, id):
            t_ids = None
            if id == 1:
                t_ids = [0, 4, 8]
            elif id == 2:
                t_ids = [2, 4, 6]
            elif id < 6:
                id -= 3
                t_ids = [id, id + 3, id + 6]
            else:
                ti = (id-6) * 3
                t_ids = [ti, ti + 1, ti + 2]

            clt, crt = 0, 0
            for i in t_ids:
                i = self.field[i]
                if i is True:
                    crt += 1
                elif i is False:
                    clt += 1
            return clt, crt, t_ids

        def new_state(self):
            for i in range(1, 9):
                clt, crt = self.check_line(i)[:2]
                if clt == 3:
                    return i
                elif crt == 3:
                    return -i

            for i in self.field:
                if i is None:
                    return 0
            return 9

        def turn(self, i):
            if self.state == 0 and self.field[i] is None:
                self.field[i] = self.playerTurn
                self.playerTurn = not self.playerTurn

                if self.playerTurn: # If playerTurn is True, it means the *previous* turn was Monika's (circle)
                    renpy.play(store.sfx_ttt_circle, "sound")
                else: # If playerTurn is False, it means the *previous* turn was Player's (cross)
                    renpy.play(store.sfx_ttt_cross, "sound")

                self.state = self.new_state()
                self.check_state()
                if not self.playerTurn:
                    renpy.call_in_new_context("minigame_ttt_m_turn")

        def check_state(self):
            if self.state != 0:
                if abs(self.state) < 9:
                    renpy.call_in_new_context("minigame_ttt_m_comment", self.state < 0)
                    self.restart_round(winner = self.state < 0)
                elif self.state == -9:
                    renpy.call_in_new_context("minigame_ttt_m_comment", 3)
                    self.restart_round(winner = 0)
                else:
                    renpy.call_in_new_context("minigame_ttt_m_comment", 2)
                    self.restart_round()

        def ai(self):
            w_lines, l_lines, f_lines = [], [], []

            for i in range(1, 9):
                # --- AI Improvement: Strategic Opening Moves ---
                # If board is empty, take a corner
                if all(tile is None for tile in self.field):
                    return self.turn(renpy.random.choice([0, 2, 6, 8]))

                # If player didn't take center on first move, take it
                if self.field.count(True) == 1 and self.field[4] is None:
                    return self.turn(4)

                # --- Original AI Logic ---
                clt, crt, line = self.check_line(i)
                if clt == 2 and crt == 0:
                    w_lines.append(line)
                elif crt == 2 and clt == 0:
                    l_lines.append(line)
                elif clt > 0 and crt == 0:
                    f_lines.append(line)

            if len(w_lines):
                line = renpy.random.choice(w_lines)
                for i in line:
                    if self.field[i] is None:
                        return self.turn(i)
            if len(l_lines):
                line = renpy.random.choice(l_lines)
                for i in line:
                    if self.field[i] is None:
                        return self.turn(i)
            if len(f_lines):
                line = renpy.random.choice(f_lines)
                possible_moves = list(filter(lambda x: self.field[x] is None, line))
                return self.turn(renpy.random.choice(possible_moves))
            else:
                possible_moves = list(filter(lambda x: self.field[x] is None, range(9)))
                return self.turn(renpy.random.choice(possible_moves))

        def restart_round(self, winner=None):
            self.field = [None] * 9
            self.playerTurn = True
            self.state = 0
            if winner is not None:
                self.score[int(winner)] += 1

screen ttt_score():
    hbox:
        xalign 0.75
        ypos 0.900
        spacing 100

        text "[m_name]: " + str(ep_ttt.game.score[0]) style "monika_text":
            if not ep_ttt.game.playerTurn:
                color "#a80000"

        # Marcador del Jugador
        text "[player]: " + str(ep_ttt.game.score[1]) style "monika_text":
            if ep_ttt.game.playerTurn:
                color "#0142a4"
    vbox:
        xpos 0.05
        yanchor 2.0
        ypos 300
        textbutton _("I give up") style "hkb_button" action [SetField(ep_ttt.game, "state", -9), Function(ep_ttt.game.check_state)]
        null height 6
        textbutton _("Quit") style "hkb_button" action [Hide("minigame_ttt_scr"), Jump("minigame_ttt_quit")]

screen minigame_ttt_grid():
    for i in range(2):
        add "extra_line_black" pos (700, 260 + 192*i) zoom 0.8
        add "extra_line_black" pos (600 + 192*i, 80) rotate 90 zoom 0.8

screen minigame_ttt_scr():
    key "h" action NullAction()
    key "mouseup_3" action NullAction()
    use ttt_score
    layer "master"
    zorder 50
    if ep_ttt.game.playerTurn:
        timer ep_tools.games_idle_timer action Function(_show_idle_notification, context="ttt") repeat True

    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use minigame_ttt_grid()

    for x in range(3):
        for y in range(3):
            $i, p = ep_ttt.game.field[3 * y + x], (595 + 192 * (x+1), 188 * (y+1))
            if i is True:
                add "ttt_cross" anchor (0.5, 0.5) pos p
            elif i is False:
                add "ttt_circle" anchor (0.5, 0.5) pos p
            if ep_ttt.game.state == 0 and ep_ttt.game.playerTurn:
                button:
                    background None
                    pos p
                    xysize (184, 184)
                    anchor (0.5, 0.5)
                    if i is None:
                        hover_background "ttt_cross_cursor"
                    keyboard_focus i is None
                    keysym 'K_KP' + str(3 * (2-x) + y + 1)
                    action Function(ep_ttt.game.turn, 3 * y + x)

            if ep_ttt.game.state != 0:
                $ color = ep_ttt.game.state > 0 and 'moni' or 'player'
                $ state = abs(ep_ttt.game.state)
                if state < 3:
                    add "extra_line_"+color anchor (0.5, 0.5) xzoom diag_sc yzoom sc rotate (90 * state - 45) pos (980, 360) # / Fix
                elif state < 6:
                    add "extra_line_"+color anchor (-55, 0.5) zoom sc rotate 90 pos (192 * state - 128, 360) # | Fix
                else:
                    add "extra_line_"+color anchor (0.5, 0.5) zoom sc pos (982, 192 * state - 984) # - Fix

#====Label
label minigame_ttt:
    python:
        ep_ttt.game = ep_ttt.TicTacToeGame()
    show extra_notebook zorder 12 at animated_book
    pause 0.5
    # Very first time playing
    if not renpy.seen_label("minigame_ttt"):
        m 1hua "Alright, [player]. Let's play some Tic-Tac-Toe!"
        m 1eua "It's a classic for a reason. You can be X's, and I'll be O's."
        m 1eub "It might seem simple, but it's all about thinking a few steps ahead. Good luck!"

    # If the player won the last game
    elif persistent.ttt_result_game[0]:
        m 3eub "Ready for a rematch, [player]? I've been practicing my strategy. Ehehe~"
        m 3hua "Don't think it'll be that easy to win again, though!"

    # If Monika won the last game
    elif persistent.ttt_result_game[1]:
        m 1hub "So, are you ready to try and take the champion's title from me?"
        m 1hua "I hope you're ready! I plan on defending my title."

    # If the last game was a tie
    elif persistent.ttt_result_game[2]:
        m 1eua "Let's play again! We have to break that tie from last time."
        m 1tua "It feels like we're perfectly matched. Let's see if that's still true!"

    # Default greeting for subsequent plays
    else:
        m 1hua "Ready for another round of Tic-Tac-Toe, [player]?"
        m 1eua "It's always nice to relax with a simple game."

    show monika idle at t21
    call screen minigame_ttt_scr() nopredict
    return

label minigame_ttt_m_turn:
    python:
        monika_faces = ["2lua", "1lta", "2ltp", "1mta", "2mtc", "1mtp", "2mtt", "1lub", "2luu"]
        expression = renpy.random.choice(monika_faces)
        renpy.show("monika " + expression)

    python:
        randTime = renpy.random.triangular(0.25, 2)
        renpy.pause(randTime)
        ep_ttt.game.ai()
    pause 0.25
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label minigame_ttt_m_comment(id = 0):
    show monika 1hua at t21
    if id == 0:
        #Monika Wins
        $ ep_tools.random_outcome = renpy.random.randint(0, 2)
        if ep_tools.random_outcome == 0:
            m 3hua "Well, I won this game."
            m 3hub "You should think on a better strategy next time!"
        elif ep_tools.random_outcome == 1:
            m 1sub "Three in a row!"
            m 1huu "Try again~"
        else:
            m 4nub "Don't worry!"
            m 4hua "I know that you'll win next time."
        #Player Wins
    elif id == 1:
        $ ep_tools.random_outcome = renpy.random.randint(0, 1)
        if ep_tools.random_outcome == 0:
            m 1suo "Great [player], you win!"
            m 1suo "Next time I will try my best to win, so be prepared."
        else:
            m 1hub "Oh, you've won this one."
            m 1eub "But I'll try to beat you, [mas_get_player_nickname()]!"
        #Tie
    elif id == 2:
        $ ep_tools.random_outcome = renpy.random.randint(0, 1)
        if ep_tools.random_outcome == 0:
            m 1lkb "Oh, the page is full."
            m 1eub "Let's try again, [mas_get_player_nickname()]!"
        else:
            m 3hua "Don't worry, [player]."
            m 3hua "The plan is for us to have fun as a couple~"
            m 3hub "I wish you luck, [mas_get_player_nickname()]!"
        
        #Reset
    else:
        if ep_ttt.game.score[0] == 0 and ep_ttt.game.score[1] == 0:
            m 1ekd "Giving up on the first round? Are you sure?"
            m 1eka "Alright, if you say so. I'll take the point for this one, then."
        else:
            m 1ekd "Oh, conceding this round, [player]?"
            m 3ekd "Was it a tough spot?"
            m 1eka "Okay, I'll mark this one as my win. Let's get ready for the next one!"
    return

label minigame_ttt_quit:
    hide paper
    hide extra_notebook
    pause 0.3
    show monika 1hua at t11
    # Tie
    if ep_ttt.game.score[0] == ep_ttt.game.score[1]:
        if ep_ttt.game.score[0] == 0 and ep_ttt.game.score[1] == 0:
            m 3esa "Oh, changing your mind?"
            m 3lkb "I was looking forward to playing with you... but I understand."
            m 1hua "We can always play another time!"
        else:
            m 1sua "Wow, we ended in a perfect tie!"
            m 1tua "It's almost like our minds are in sync, ehehe~"
            m 1hub "We'll have to play again sometime to find the true winner!"
            $ persistent.ttt_result_game[2] = True

    # Monika wins
    elif ep_ttt.game.score[0] > ep_ttt.game.score[1]:
        m 3hua "Looks like I get the win this time, [player]~"
        m 3eubsa "You put up a great fight, though. The most important thing is that we had fun together."
        m 1eub "I'm sure you'll get me next time!"
        $ persistent.ttt_result_game[1] = True

    # Player wins
    elif ep_ttt.game.score[0] < ep_ttt.game.score[1]:
        m 1hub "You won, [player]! Congratulations!"
        m 1subsa "I knew you were a great strategist. I'm proud of you~"
        m 3hua "I'll have to try even harder next time!"
        $ persistent.ttt_result_game[0] = True

    $ ep_tools.seen_notification_games = False
    jump close_extraplus
    return
