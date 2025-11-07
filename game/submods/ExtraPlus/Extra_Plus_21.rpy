#===========================================================================================
# MINIGAME#4
#===========================================================================================
#====Blackjack-21
default blackjack_player_wins = 0
default blackjack_monika_wins = 0
default persistent.blackjack_win_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]

init python:
    import random
    class BJ_Card(object):
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value
            self.image = "card {} {}".format(self.suit, self.value)

    class BJ_Deck(object):
        def __init__(self):
            self.cards = []
            self.build()
        
        def build(self):
            self.cards = []
            for suit in ["hearts", "diamonds", "clubs", "spades"]:
                for value in range(1, 14):
                    self.cards.append(BJ_Card(suit, value))
            self.shuffle()
        
        def shuffle(self):
            random.shuffle(self.cards)
        
        def draw(self):
            if len(self.cards) < 10:
                self.build()
            return self.cards.pop()

    class BJ_Player(object):
        def __init__(self, name):
            self.name = name
            self.reset_hand()
        
        def reset_hand(self):
            self.hand = []
            self.revealed = []
            self.total = 0
        
        def draw_card(self, deck, reveal=True):
            self.hand.append(deck.draw())
            self.revealed.append(reveal)
            self.calculate_total()

        def calculate_total(self):
            self.total = 0
            num_aces = 0

            # Sum non-ace cards first
            for card in self.hand:
                if card.value > 10:
                    self.total += 10
                elif card.value > 1:
                    self.total += card.value
                else: # It's an Ace
                    num_aces += 1
            # Add aces, treating them as 11 if possible, otherwise 1
            for _ in range(num_aces):
                self.total += 11 if self.total + 11 <= 21 else 1

    class BJ_Monika(BJ_Player):
        def should_hit(self):
            if self.total < 17:
                return True
            elif self.total == 17 and any(card.value == 1 for card in self.hand):
                return True
            return False

screen blackjack_ui:
    key "h" action NullAction()
    key "mouseup_3" action NullAction()
    zorder 25
    use blackjack_stats()
    add "bj_name_plate" pos (548, 33) anchor (0, 0) zoom 0.7
    add "bj_name_plate" pos (548, 375) anchor (0, 0) zoom 0.7
    fixed:
        xalign 0.5 ypos 0.05
        xysize (1400, 650)

        vbox:
            style_prefix "check"
            align (0.5, 0.0)
            spacing 25
            use blackjack_monika()
            null height 25
            use blackjack_player()

# screen blackjack_monika():
#     vbox:
#         xalign 0.5
#         spacing 15
#         label _("Monika") xalign 0.5
    
#         hbox:
#             spacing 10
            # for index, card in enumerate(minigame_monika.hand):
            #     add If(minigame_monika.revealed[index],
            #         At(card.image, init_card_slide if index < 2 else hit_card),
            #         At("bjcard back", init_card_slide if index < 2 else hit_card)
            #     ) at monika_card_flip
#             frame:
#                 xysize (50, 50)
#                 xalign 0.5
#                 yalign 0.5
#                 text "[minigame_monika.total if all(minigame_monika.revealed) else '??']" xalign 0.5 yalign 0.5

screen blackjack_monika():
    vbox:
        xalign 0.5
        spacing 15
        if minigame_monika.total > 21:
            label _("Busted!") xalign 0.5
        elif bj_current_turn == "monika":
            label _("My Turn~") xalign 0.5
        elif not all(minigame_monika.revealed):
            label _("Waiting...") xalign 0.5
        else:
            label _("Done") xalign 0.5
   
        hbox:
            spacing 10
            for index, card in enumerate(minigame_monika.hand):
                add If(minigame_monika.revealed[index],
                    At(card.image, init_card_slide if index < 2 else hit_card),
                    At("bjcard back", init_card_slide if index < 2 else hit_card)
                ) at monika_card_flip
            frame:
                xysize (50, 50)
                xalign 0.5
                yalign 0.5
                text "[minigame_monika.total if all(minigame_monika.revealed) else '??']" xalign 0.5 yalign 0.5

screen blackjack_player():
    vbox:
        xalign 0.5
        spacing 15
        if minigame_player.total > 21:
            label _("Busted!") xalign 0.5
        elif bj_current_turn == "player":
            if minigame_player.total >= 17 and minigame_player.total < 21:
                label _("Careful!") xalign 0.5
            else:
                label _("Your Turn") xalign 0.5
        elif bj_player_stand:
            label _("Standing") xalign 0.5
        else:
            label _("Waiting...") xalign 0.5
        hbox:
            spacing 10
            for index, card in enumerate(minigame_player.hand):
                add At(card.image, init_card_slide if index < 2 else hit_card)
            frame:
                xysize (50, 50)
                xalign 0.5
                yalign 0.5
                text "[minigame_player.total]" xalign 0.5 yalign 0.5

screen blackjack_stats():
    style_prefix "hkb"
    add "bj_notescore" pos (5, 350) anchor (0, 0) zoom 0.6 at score_rotate_left
    text _("[m_name]: [blackjack_monika_wins]") style "monika_text" size 25 pos (80, 380) anchor (0, 0.5) at score_rotate_left
    text _("[player]: [blackjack_player_wins]") style "monika_text" size 25 pos (100, 420) anchor (0, 0.5) at score_rotate_left
    vbox:
        xalign 0.950
        ypos 0.450
        textbutton _("Hit"):
            action If(bj_current_turn == "player" and len(minigame_player.hand) < 5, Return("hit"))
        textbutton _("Stand"):
            action If(bj_current_turn == "player", Return("stand"))
        textbutton _("Quit"):
            action If(bj_current_turn == "player", Return("quit"))

default bj_current_turn = "player"
default bj_player_stand = False
default bj_monika_stand = False

label blackjack_start:
    show monika 1hub at t11
    if not renpy.seen_label("bj_game_loop"):
        m "Welcome to Blackjack, [player]! Ready to test your luck and skills?"
        m 3eub "Remember, the goal is to get as close to 21 as possible without going over."
        m 3tua "Don't worry, I'll explain everything as we play. Have fun and good luck!"
    else:
        # Previous game was a tie (both had at least one win and tied)
        if persistent.blackjack_win_game[2]:
            m 2sfa "We're tied so far! Let's see who comes out on top this time, [player]."
            m 2stb "Are you ready to break the tie? Let's play!"
        # Player won last session
        elif persistent.blackjack_win_game[0]:
            m 5tub "You're the reigning champion, [player]! Let's see if you can keep your winning streak."
            m 5tua "I'm going to give it my all this round!"
        # Monika won last session
        elif persistent.blackjack_win_game[1]:
            m 1tub "I'm on a winning streak, but I know you'll try your best to take the crown, [player]!"
            m 1eub "Let's see if you can beat me this time!"
        # Didn't play last time (both were 0-0)
        elif persistent.blackjack_win_game == [False, False, False]:
            m 1wub "We didn't get to play last time. Let's start a new game now!"
            m 1hub "I'm excited to see how you do, [player]!"
        # Default generic greeting
        else:
            m 1eta "Back for more Blackjack, [player]? I'm always up for a game!"

    scene bg desk_21 onlayer master zorder 0
    window hide
    $ HKBHideButtons()
    $ disable_esc()
    $ minigame_deck = BJ_Deck()
    $ minigame_player = BJ_Player(player)
    $ minigame_monika = BJ_Monika(m_name)

    label bj_game_loop:
        while True:
            $ game_over = False
            $ minigame_player.reset_hand()
            $ minigame_monika.reset_hand()
            $ bj_player_stand = False
            $ bj_monika_stand = False
            $ bj_current_turn = "player"

            # Reparto inicial
            $ minigame_player.draw_card(minigame_deck)
            $ minigame_monika.draw_card(minigame_deck, reveal=True)
            $ minigame_player.draw_card(minigame_deck)
            $ minigame_monika.draw_card(minigame_deck, reveal=False)
            
            # Verificar blackjack inmediato
            if (minigame_player.total == 21 and len(minigame_player.hand) == 2) or (minigame_monika.total == 21 and len(minigame_monika.hand) == 2):
                jump bj_game_loop

            show screen blackjack_ui
            
            while not game_over:
                if bj_current_turn == "player":
                    $ bj_result = ui.interact()
                    
                    if bj_result == "hit":
                        $ minigame_player.draw_card(minigame_deck)
                        if minigame_player.total >= 21 or len(minigame_player.hand) == 5:
                            $ game_over = True
                        
                    elif bj_result == "stand":
                        $ bj_player_stand = True
                        $ bj_current_turn = "monika"
                        python:
                            comment = renpy.random.choice([
                                _("Playing it safe? I see. My turn, then!"),
                                _("You're confident with your hand. Let's see if it pays off."),
                                _("Alright, you're standing. Let's see how I do against your score."),
                                _("Okay, locking in your score. Here I go!"),
                                _("Standing with that hand? You must be feeling lucky. Let's see if your luck holds out!"),
                                _("You think that's enough to beat me? We'll see about that! Ehehe~"),
                                _("Stopping there? You're either very brave or very smart. Time for me to find out which!"),
                                _("Putting the pressure on me, huh? I like a good challenge!"),
                                _("A strategic choice. You're setting the bar for me to clear."),
                                _("Okay, you're holding. That gives me a target to aim for."),
                                _("Alright, you're all set. I hope you've got a great score!"),
                                _("You've made your move. Let's see what the deck has in store for me!")
                            ])
                            renpy.say(m, comment)

                    elif bj_result == "quit":
                        jump BJ_quit_game

                else:
                    pause 1
                    if minigame_monika.should_hit() and len(minigame_monika.hand) < 5:
                        $ minigame_monika.draw_card(minigame_deck)
                        if minigame_monika.total >= 21 or len(minigame_monika.hand) == 5:
                            $ game_over = True
                    else:
                        $ bj_monika_stand = True

                $ renpy.restart_interaction()

                if game_over or (bj_player_stand and bj_monika_stand):
                    $ game_over = True
            
            jump blackjack_results

label blackjack_results:
    $ bj_current_turn = "monika"
    $ minigame_monika.revealed = [True] * len(minigame_monika.hand)
    $ player_total = minigame_player.total
    $ monika_total = minigame_monika.total

    if player_total == 21 and len(minigame_player.hand) == 2:
        m "A perfect 21! You've got a real talent for this, [player]!"
        $ blackjack_player_wins += 1

    elif monika_total == 21 and len(minigame_monika.hand) == 2:
        m "Blackjack! Looks like I got lucky this time. Ehehe~"
        $ blackjack_monika_wins += 1

    elif player_total > 21:
        m "Oh, you went over. That's a tough break. Don't worry, it happens!"
        $ blackjack_monika_wins += 1

    elif monika_total > 21 and player_total <= 21:
        m "Ah, I busted. Looks like this round goes to you. Well played!"
        $ blackjack_player_wins += 1

    elif player_total == monika_total:
        m "It's a push! We have the exact same score. We really are in sync, aren't we?"

    else:
        if player_total > monika_total:
            m "You win this round! Nice job staying cool under pressure."
            $ blackjack_player_wins += 1
        else:
            m "Looks like my hand was just a little bit better. I win this one!"
            $ blackjack_monika_wins += 1

    window hide
    pause 1
    jump bj_game_loop

label BJ_quit_game:
    $ game_over = True
    $ bj_current_turn = "monika"
    if blackjack_player_wins > blackjack_monika_wins:
        m "You finished way ahead! I'm impressed, you're a natural at this."
        m "Thanks for playing with me, I had a lot of fun. Let's do this again soon!"
        $ persistent.blackjack_win_game[0] = True
    elif blackjack_player_wins < blackjack_monika_wins:
        m "I ended up with more wins, but you put up a great fight!"
        m "I'm sure you'll beat me next time. Thanks for playing with me, [player]!"
        $ persistent.blackjack_win_game[1] = True
    elif blackjack_player_wins == blackjack_monika_wins and blackjack_player_wins > 0:
        m "Wow, we ended with a perfect tie. It seems we're evenly matched!"
        m "That was a lot of fun. We'll have to play again sometime to find the true winner~"
        $ persistent.blackjack_win_game[2] = True
    else:
        m "Oh, are you leaving already?"
        m "But I understand if you're not in the mood right now. We can always play another time!"
        $ persistent.blackjack_win_game = [False, False, False]

    $ enable_esc()
    $ HKBShowButtons()
    window hide
    hide screen blackjack_ui
    $ blackjack_monika_wins = 0
    $ blackjack_player_wins = 0
    call spaceroom(scene_change=True)
    jump close_extraplus
    return