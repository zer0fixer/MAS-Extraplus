#===========================================================================================
# MINIGAME#4
#===========================================================================================
#====Blackjack-21
default persistent.blackjack_win_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]

init -5 python in ep_bj:
    import store

    player_wins = 0
    monika_wins = 0
    current_turn = "player"
    player_stand = False
    monika_stand = False
    game_quit = False
    comment = _("Playing it safe? I see. Let's see if it pays off.")
    comments_list = [
        _("Playing it safe? I see. My turn, then!"),
        _("You're confident with your hand. Let's see if you're right."),
        _("Alright, you're standing. Let's see how I measure up."),
        _("Okay, locking in your score. Here I go!"),
        _("Standing with that hand? You must be feeling lucky!"),
        _("You think that's enough to beat me? We'll see about that! Ehehe~"),
        _("Stopping there? You're either very brave or very smart. Time to find out which!"),
        _("Putting the pressure on me, huh? I love a good challenge!"),
        _("A strategic choice. You're setting the bar for me."),
        _("Okay, you're holding. That gives me a target to aim for."),
        _("Alright, you're all set. I hope you've got a good score!"),
        _("You've made your move. Let's see what the deck has in store for me!")
    ]

    def getCardImage(suit, value):
        """
        Generates the image of a card dynamically.
        More efficient than preloading all cards.
        """
        card_path = store.ep_folders._join_path(
            store.ep_folders.EP_MG_BLACKJACK, 
            suit, 
            "{}.png".format(value)
        )
        return store.MASFilterSwitch(card_path)

init python in ep_bj:
    import random
    import store

    class BJ_Card(object):
        __slots__ = ['suit', 'value', '_image']
        
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value
            self._image = None

        @property
        def image(self):
            # Lazy loading: Only generate the image when first accessed.
            # This is intentional to avoid loading all 52 card images at once.
            if self._image is None:
                self._image = getCardImage(self.suit, self.value)
            return self._image

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
            
            # Sum all cards, treating Aces as 1 initially
            for card in self.hand:
                if card.value > 10:  # Jack (11), Queen (12), King (13)
                    self.total += 10
                elif card.value == 1:  # Ace
                    self.total += 1
                    num_aces += 1
                else:  # 2-10
                    self.total += card.value
            
            # Try to upgrade ONE ace from 1 to 11 if it doesn't bust
            # (Adding 10 to an ace valued at 1 makes it 11)
            if num_aces > 0 and self.total + 10 <= 21:
                self.total += 10

    class BJ_Monika(BJ_Player):
        def should_hit(self):
            if self.total < 17:
                return True
            elif self.total == 17 and any(card.value == 1 for card in self.hand):
                return True
            return False

screen blackjack_ui:
    key "h" action NullAction()
    key "H" action NullAction()
    key "mouseup_3" action NullAction()
    zorder 25
    use blackjack_stats()
    add "bj_name_plate" pos (548, 33) anchor (0, 0) zoom 0.7
    add "bj_name_plate" pos (548, 375) anchor (0, 0) zoom 0.7
    if store.ep_bj.current_turn == "player":
        timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="bj") repeat True

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

screen blackjack_monika():
    vbox:
        xalign 0.5
        spacing 15
        if minigame_monika.total > 21:
            label _("Busted!") xalign 0.5
        elif minigame_player.total > 21:
            label _("Sorry~") xalign 0.5
        elif store.ep_bj.game_quit:
            label _("End") xalign 0.5
        elif store.ep_bj.current_turn == "monika":
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
                    )
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
        elif store.ep_bj.game_quit:
            label _("End") xalign 0.5
        elif store.ep_bj.current_turn == "player":
            if minigame_player.total >= 17 and minigame_player.total < 21:
                label _("Careful!") xalign 0.5
            else:
                label _("Your Turn") xalign 0.5
        elif store.ep_bj.player_stand:
            label _("Standing") xalign 0.5
        else:
            label _("Done") xalign 0.5
            
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
    text _("[m_name]: [store.ep_bj.monika_wins]") style "monika_text" size 25 pos (80, 380) anchor (0, 0.5) at score_rotate_left
    text _("[player]: [store.ep_bj.player_wins]") style "monika_text" size 25 pos (100, 420) anchor (0, 0.5) at score_rotate_left
    vbox:
        xalign 0.950
        ypos 0.450
        textbutton _("Hit"):
            action If(store.ep_bj.current_turn == "player" and len(minigame_player.hand) < 5, Return("hit"))
        textbutton _("Stand"):
            action If(store.ep_bj.current_turn == "player", Return("stand"))
        textbutton _("Quit"):
            action If(store.ep_bj.current_turn == "player", Return("quit"))

label blackjack_start:
    show monika 1hub at t11
    if not renpy.seen_label("checkpoint_blackjack") and not renpy.seen_label("blackjack_results"):
        m "Welcome to our Blackjack table, [player]!"
        m 3eub "Ready to test your luck?"
        m 3eub "Remember, the goal is to get as close to 21 as possible without going over."
        m 3tua "Let's see if Lady Luck is on your side today. Have fun!"

label checkpoint_blackjack:
    if renpy.seen_label("blackjack_results"):
        # Previous game was a tie (both had at least one win and tied)
        if persistent.blackjack_win_game[2]:
            m 2sfa "We're tied so far!"
            m 2stb "Let's see who comes out on top this time, [player]."
            m "Are you ready to break the tie?"
        # Player won last session
        elif persistent.blackjack_win_game[0]:
            m 5tub "You're the reigning champion, [player]!"
            m 5tua "Let's see if you can keep your winning streak alive."
            m "I'm going to give it my all this round!"
        # Monika won last session
        elif persistent.blackjack_win_game[1]:
            m 1tub "I'm on a winning streak, but I know you'll try your best to take the crown, [player]!"
            m 1eub "Let's see if you can beat me this time!"
        # Didn't play last time (both were 0-0)
        elif persistent.blackjack_win_game == [False, False, False]:
            m 1wub "We didn't get to play last time."
            m 1hub "Let's start a new game now! I'm excited to see how you do."
        # Default generic greeting
        else:
            m 1eta "Back for more Blackjack, [player]?"
            m "I'm always up for a game with you!"

    scene bg desk_21 onlayer master zorder 0
    window hide
    $ HKBHideButtons()
    $ disable_esc()
    # Disable chibi dragging during minigame
    $ ep_bj.saved_drag_state = persistent.enable_drag_chibika
    $ persistent.enable_drag_chibika = False
    $ minigame_deck = ep_bj.BJ_Deck()
    $ minigame_player = ep_bj.BJ_Player(player)
    $ minigame_monika = ep_bj.BJ_Monika(m_name)

    label bj_game_loop:
        while True:
            $ game_over = False
            $ minigame_player.reset_hand()
            $ minigame_monika.reset_hand()
            $ ep_bj.player_stand = False
            $ ep_bj.monika_stand = False
            $ ep_bj.current_turn = "player"
            $ ep_bj.game_quit = False

            # Reparto inicial
            $ minigame_player.draw_card(minigame_deck)
            $ minigame_monika.draw_card(minigame_deck, reveal=True)
            $ minigame_player.draw_card(minigame_deck)
            $ minigame_monika.draw_card(minigame_deck, reveal=False)
            
            if (minigame_player.total == 21 and len(minigame_player.hand) == 2) or (minigame_monika.total == 21 and len(minigame_monika.hand) == 2):
                jump bj_game_loop

            show screen blackjack_ui
            
            while not game_over:
                if ep_bj.current_turn == "player":
                    $ bj_result = ui.interact()

                    if bj_result == "hit":
                        $ minigame_player.draw_card(minigame_deck)
                        if minigame_player.total >= 21 or len(minigame_player.hand) == 5:
                            $ game_over = True
                        
                        elif minigame_player.total == 21 or len(minigame_player.hand) == 5:
                            $ ep_bj.player_stand = True
                            $ ep_bj.current_turn = "monika"
                            python:
                                ep_bj.comment = renpy.random.choice(ep_bj.comments_list)
                                renpy.say(m, ep_bj.comment)
                        
                    elif bj_result == "stand":
                        $ ep_bj.player_stand = True
                        $ ep_bj.current_turn = "monika"
                        python:
                            ep_bj.comment = renpy.random.choice(ep_bj.comments_list)
                            renpy.say(m, ep_bj.comment)

                    elif bj_result == "quit":
                        jump BJ_quit_game

                else:
                    pause 1
                    if minigame_monika.should_hit() and len(minigame_monika.hand) < 5:
                        $ minigame_monika.draw_card(minigame_deck)
                        if minigame_monika.total >= 21 or len(minigame_monika.hand) == 5:
                            $ game_over = True
                    else:
                        $ ep_bj.monika_stand = True

                $ renpy.restart_interaction()

                if game_over or (ep_bj.player_stand and ep_bj.monika_stand):
                    $ game_over = True
            
            jump blackjack_results

label blackjack_results:
    $ ep_bj.current_turn = "monika"
    $ minigame_monika.revealed = [True] * len(minigame_monika.hand)
    $ player_total = minigame_player.total
    $ monika_total = minigame_monika.total
    
    # Natural blackjack (21 with 2 cards) - highest priority
    if player_total == 21 and len(minigame_player.hand) == 2 and not (monika_total == 21 and len(minigame_monika.hand) == 2):
        m "Blackjack! Wow, you've got a real talent for this, [player]!"
        $ ep_bj.player_wins += 1
    
    elif monika_total == 21 and len(minigame_monika.hand) == 2 and not (player_total == 21 and len(minigame_player.hand) == 2):
        m "Blackjack!"
        m "Looks like I got lucky this time. Ehehe~"
        $ ep_bj.monika_wins += 1
    
    # Both have natural blackjack
    elif player_total == 21 and len(minigame_player.hand) == 2 and monika_total == 21 and len(minigame_monika.hand) == 2:
        m "We both got natural Blackjacks!"
        m "That's a push, [player]. Amazing!"
    
    # If the player busts, they lose IMMEDIATELY (regardless of whether Monika also busts)
    elif player_total > 21:
        m "Oh, you went over."
        m "That's a tough break. Don't worry, it happens!"
        $ ep_bj.monika_wins += 1
    
    # If Monika busts but the player doesn't, the player wins
    elif monika_total > 21:
        m "Ah, I went over 21."
        m "Looks like this round is yours. Well played!"
        $ ep_bj.player_wins += 1
    
    # Tie (same score without busting)
    elif player_total == monika_total:
        m "It's a push!"
        m "We have the exact same score. We really are in sync, aren't we?"
    
    # Normal comparison (both ≤ 21)
    else:
        if player_total > monika_total:
            m "You win this round!"
            m "Nice job staying cool under pressure."
            $ ep_bj.player_wins += 1
        else:
            m "Looks like my hand was just a little bit better."
            m "I win this one!"
            $ ep_bj.monika_wins += 1
    
    window hide
    pause 1
    jump bj_game_loop

label BJ_quit_game:
    $ game_over = True
    $ ep_bj.game_quit = True
    $ ep_bj.current_turn = "monika"
    if ep_bj.player_wins > ep_bj.monika_wins:
        m "You finished ahead! I'm impressed, you're a natural at this."
        m "Thanks for playing with me, I had a lot of fun."
        m "Let's do this again soon!"
        $ persistent.blackjack_win_game[0] = True
    elif ep_bj.player_wins < ep_bj.monika_wins:
        m "I ended up with more wins, but you put up a great fight!"
        m "I'm sure you'll beat me next time."
        m "Thanks for playing with me, [player]!"
        $ persistent.blackjack_win_game[1] = True
    elif ep_bj.player_wins == ep_bj.monika_wins and ep_bj.player_wins > 0:
        m "Wow, a perfect tie. It seems we're evenly matched!"
        m "That was a lot of fun."
        m "We'll have to play again sometime to find the true winner~"
        $ persistent.blackjack_win_game[2] = True
    else:
        m "Oh, are you leaving already?"
        m "But I understand if you're not in the mood right now."
        m "We can always play another time!"
        $ persistent.blackjack_win_game = [False, False, False]

    $ enable_esc()
    $ HKBShowButtons()
    # Restore chibi dragging state
    $ persistent.enable_drag_chibika = ep_bj.saved_drag_state
    window hide
    hide screen blackjack_ui
    $ ep_bj.monika_wins = 0
    $ ep_bj.player_wins = 0
    call spaceroom(scene_change=True)
    jump close_extraplus
    return