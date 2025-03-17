#===========================================================================================
# MINIGAME#2
#===========================================================================================
# define ttt_sprite = ["line.png","line_moni.png","line_player.png","notebook.png"]

#====Tic-Tac-Toe
init 10 python:
    def ttt_prep(self, restart = False, *args, **kwargs):
        self.field = [None] * 9
        self.playerTurn = True
        self.state = 0

        if not restart:
            self.score = [0, 0]

            def ttt_check_line(id):
                t_ids = None
                if id == 0:
                    tiles = range(9)
                elif id == 1:
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
                    i = ttt.field[i]
                    if i is True:
                        crt += 1
                    elif i is False:
                        clt += 1
                return clt, crt, t_ids

            def ttt_new_state():
                for i in range(1, 9):
                    clt, crt = ttt_check_line(i)[:2]
                    if clt == 3:
                        return i
                    elif crt == 3:
                        return -i

                for i in ttt.field:
                    if i is None:
                        return 0
                return 9

            def ttt_turn(i):
                if ttt.state == 0 and ttt.field[i] is None:
                    ttt.field[i] = ttt.playerTurn
                    ttt.playerTurn = not ttt.playerTurn

                    fig = "circle"
                    if ttt.playerTurn:
                        fig = "cross"
                    renpy.play("submods/ExtraPlus/submod_assets/sfx/ttt_"+ fig + ".ogg", "sound")

                    ttt.state = ttt_new_state()
                    ttt_check_state()
                    if not ttt.playerTurn:
                        renpy.call_in_new_context("minigame_ttt_m_turn")

            def ttt_check_state():
                if ttt.state != 0:
                    if abs(ttt.state) < 9:
                        renpy.call_in_new_context("minigame_ttt_m_comment", ttt.state < 0)
                        ttt(restart = True, winner = ttt.state < 0)
                    elif ttt.state == -9:
                        renpy.call_in_new_context("minigame_ttt_m_comment", 3)
                        ttt(restart = True, winner = 0)
                    else:
                        renpy.call_in_new_context("minigame_ttt_m_comment", 2)
                        ttt(restart = True)

            def ttt_ai():
                w_lines, l_lines, f_lines = [], [], []

                for i in range(1, 9):
                    clt, crt, line = ttt_check_line(i)
                    if clt == 2 and crt == 0:
                        w_lines.append(line)
                    elif crt == 2 and clt == 0:
                        l_lines.append(line)
                    elif clt > 0 and crt == 0:
                        f_lines.append(line)

                if len(w_lines):
                    line = renpy.random.choice(w_lines)
                    for i in line:
                        if ttt.field[i] is None:
                            return ttt_turn(i)
                if len(l_lines):
                    line = renpy.random.choice(l_lines)
                    for i in line:
                        if ttt.field[i] is None:
                            return ttt_turn(i)
                if len(f_lines):
                    line = renpy.random.choice(f_lines)
                    line = filter(lambda x: ttt.field[x] is None, line)
                    return ttt_turn(renpy.random.choice(line))
                else:
                    line = filter(lambda x: ttt.field[x] is None, range(9))
                    return ttt_turn(renpy.random.choice(line))

            self.new_state, self.check_state = ttt_new_state, ttt_check_state
            self.check_line, self.turn, self.ai = ttt_check_line, ttt_turn, ttt_ai

        elif not kwargs.get("winner") is None:
            w = kwargs['winner']
            self.score[w] += 1



screen ttt_score():
    vbox:
        xpos 0.6
        ypos 0.900

        text "[m_name]: " + str(ttt.score[0])  style "monika_text":
            if not ttt.playerTurn:
                color "#a80000"
    vbox:
        xpos 0.9
        ypos 0.900

        text "[player]: " + str(ttt.score[1])  style "monika_text":
            if ttt.playerTurn:
                color "#0142a4"
    vbox:
        xpos 0.05
        yanchor 2.0
        ypos 300

        # spacing 5
        # xpos 280
        # yanchor 2.0
        # ypos 1.0

        textbutton _("I give up") style "hkb_button" action [Function(ttt.set_state, -9), Function(ttt.check_state)]
        null height 6
        textbutton _("Quit") style "hkb_button" action [Hide("minigame_ttt_scr"), Jump("minigame_ttt_quit")]

screen minigame_ttt_grid():
    for i in range(2):
        add "line_black" pos (700, 260 + 192*i) zoom 0.8
        add "line_black" pos (600 + 192*i, 80) rotate 90 zoom 0.8

screen minigame_ttt_scr():
    use ttt_score()
    layer "master"
    zorder 50

    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use minigame_ttt_grid()

    for x in range(3):
        for y in range(3):
            $i, p = ttt.field[3 * y + x], (595 + 192 * (x+1), 188 * (y+1))
            if i is True:
                add "ttt_cross" anchor (0.5, 0.5) pos p
            elif i is False:
                add "ttt_circle" anchor (0.5, 0.5) pos p
            if ttt.state == 0 and ttt.playerTurn:
                button:
                    background None
                    pos p
                    xysize (184, 184)
                    anchor (0.5, 0.5)
                    if i is None:
                        hover_background "ttt_cross_cursor"
                    keyboard_focus i is None
                    keysym 'K_KP' + str(3 * (2-x) + y + 1)
                    action Function(ttt.turn, 3 * y + x)

            if ttt.state != 0:
                $ color = ttt.state > 0 and 'moni' or 'player'
                $ state = abs(ttt.state)
                if state < 3:
                    add "line_"+color anchor (0.5, 0.5) xzoom diag_sc yzoom sc rotate (90 * state - 45) pos (980, 360) # / Fix
                elif state < 6:
                    add "line_"+color anchor (-55, 0.5) zoom sc rotate 90 pos (192 * state - 128, 360) # | Fix
                else:
                    add "line_"+color anchor (0.5, 0.5) zoom sc pos (982, 192 * state - 984) # - Fix



#====Label
label minigame_ttt:
    # $ check_file_status(ttt_sprite, '/game/submods/ExtraPlus/submod_assets/sprites')
    # if not os.path.isfile(renpy.config.basedir + '/game/submods/ExtraPlus/submod_assets/Pictograms.ttf'):
    #     show monika idle at t11
    #     call screen dialog("A font is needed here, you know?",ok_action=Jump("close_extraplus"))

    show monika 1hua at t21
    show notebook zorder 12 at animated_book
    pause 0.5
    call screen minigame_ttt_scr() nopredict
    return
    
label minigame_ttt_m_turn:
    show monika 1lua at t21
    python:
        randTime = renpy.random.triangular(0.25, 2)
        renpy.pause(randTime)
        ttt.ai()
    show monika 1lua at t21
    pause 0.25
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label minigame_ttt_m_comment(id = 0):
    show monika 1hua at t21
    if id == 0:
        # if persistent.win_minigame["monika"]["ttt"] == True:
        #     ""
        #Monika Wins
        $ moldable_variable = renpy.random.randint(0, 2)
        if moldable_variable == 0:
            m 3hua "Well, I won this game."
            m 3hub "You should think on a better strategy next time!"
        elif moldable_variable == 1:
            m 1sub "Three in a row!"
            m 1huu "Try again~"
        else:
            m 4nub "Don't worry!"
            m 4hua "I know that you'll win next time."
        # $ persistent.win_minigame["monika"]["ttt"] = True
        #Player Wins
    elif id == 1:
        $ moldable_variable = renpy.random.randint(0, 1)
        if moldable_variable == 0:
            m 1suo "Great [player], you win!"
            m 1suo "Next time I will try my best to win, so be prepared."
        else:
            m 1hub "Oh, you've won this one."
            m 1eub "But I'll try to beat you, [mas_get_player_nickname()]!"
        # $ persistent.win_minigame["player"]["ttt"] = True
        #Tie
    elif id == 2:
        $ moldable_variable = renpy.random.randint(0, 1)
        if moldable_variable == 0:
            m 1lkb "Oh, the page is full."
            m 1eub "Let's try again, [mas_get_player_nickname()]!"
        else:
            m 3hua "Don't worry, [player]."
            m 3hua "The plan is for us to have fun as a couple~"
            m 3hub "I wish you luck, [mas_get_player_nickname()]!"
        # $ persistent.win_minigame["monika"]["ttt"] = False
        # $ persistent.win_minigame["player"]["ttt"] = False
        
        #Reset
    else:
        $ moldable_variable = renpy.random.randint(0, 1)
        if moldable_variable == 0:
            m 1ekd "Are you giving up on this round?"
            m 1eka "Well, I'm going to restart the game, but I'll take a point!"
        else:
            m 1ekd "What's wrong, [player]?"
            m 3ekd "Were you distracted?"
            m 1eka "Okay, I'm going to restart the game, but I will be the winner of this round!"
    return

label minigame_ttt_quit:
    hide paper
    hide notebook
    pause 0.3
    show monika 1hua at t11
    if ttt.score[0] == ttt.score[1]:
        if ttt.score[0] == 0 and ttt.score[1] == 0:
            m 3esa "Oh! You stopped playing?"
            m 3lkb "I thought you wanted to play with me for a while..."
            m 3lkb "But don't worry, I understand if you don't feel like playing."
            m 1hua "I just hope we can play some other time."
        else:
            m 1suo "Wow, it's a tie!"
            m 2huu "There must be a winner, though."
            m 2hub "Next time, we'll see who wins!"
            m 1hub "Ehehe~"
    elif ttt.score[0] > ttt.score[1]:
        m 3hua "I won this time, [player]~"
        m 3eubsa "But don't feel bad, what matters most to me is that we both have fun."
        m 1eub "Maybe you'll beat me next time!"
    elif ttt.score[0] < ttt.score[1]:
        m 1hub "You have won [player], congratulations."
        m 1hub "I am proud of you~"
        m 3hua "I'll do my best next time too!"
    jump close_extraplus
    return
