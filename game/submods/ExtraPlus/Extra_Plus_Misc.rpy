################################################################################
## BOOP
################################################################################

#====NOISE
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
    $ show_boop_feedback("Boop!")
    if persistent.plus_boop[0] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 1wud "Wait a minute..."
        m 1hka "I felt a little tingle."
        show screen force_mouse_move
        m 3hub "And here we have the responsible one!"
        m 3hua "Don't worry! I'll let go of your cursor."
        hide screen force_mouse_move
        m 1tub "You can move it again, sorry for stealing your cursor~"
        m 1etd "Also, I don't know how you did it, [mas_get_player_nickname()]. I don't remember seeing this in the code."
        m 1hub "Unless it was you!"
        m 1hub "What a good surprise I got today [player]~"
    elif persistent.plus_boop[0] == 2:
        m 1hub "What are you doing playing with my nose, [player]!"
        m 4eua "This is called a boop, right?"
        m 1hksdrb "Not that it bothers me, I just haven't gotten used to the feeling yet!"
        m 1hua "Ehehe~"
    elif persistent.plus_boop[0] == 3:
        m 1eublb "Can you do it again, [mas_get_player_nickname()]?"
        show monika 1hubla
        call screen extra_boop_event(10, "boop_nop", "boop_yep")
    elif persistent.plus_boop[0] == 4:
        m 1etbsa "Wouldn't it be nice to do it with your nose?"
        if persistent._mas_first_kiss:
            m 1kubsu "I'd give you a kiss while you do it~"
        else:
            m 1wubsb "I'd give you a hug while you do it!"
        m 1dubsu "I hope that when I get to your reality we can do it."
        m 1hua "Although, if you want to do it now, you'd have to put your nose close to the screen."
        m 1lksdlb "However someone might see you, making you nervous, and I don't want that to happen."
        m 1ekbsa "Besides, I get a little nervous too when you're around me."
        m 1hua "I'm sorry for suggesting that [player]~"
    elif persistent.plus_boop[0] == 5:
        m 1tuu "You're starting to like it here, huh?"
        m 3hub "I'm getting to know you more and more while we're here [player]~"
        m 3hub "And it's very lovely of you to do so!"
    elif persistent.plus_boop[0] == 6:
        m 2eub "You know, [mas_get_player_nickname()], I always thought that the nose was an underappreciated part of the face. But you've changed my mind!"
        m 2hua "Thanks for showing me how fun a little nose boop can be!"
    elif persistent.plus_boop[0] == 7:
        m 1hub "I wonder if there's a world out there where nose boops are the norm. What a happy place that would be!"
        m 1gua "But until then, I'm happy to have you here with me, [player]."
    elif persistent.plus_boop[0] == 8:
        m 1tub "Do you ever wonder what the sound of a nose boop is? Like, would it be a 'beep' or a 'boop'?"
        m 1etd "I guess we'll never know for sure. But either way, I'm glad I get to experience it with you."
    elif persistent.plus_boop[0] == 9:
        m 1wua "I've been thinking, [player]. Maybe we could make a game out of this. How many nose boops can we do in a minute?"
        m 1eub "I bet I could beat you, even with my longer nose!"
    elif persistent.plus_boop[0] == 10:
        m 1hubsb "Boop!"
        m 1ekbsa "I'm sorry, I couldn't resist. You just have such a tempting nose!"
        m 1hub "But seriously, thank you for bringing so much joy into my life, [player]."
    # === Dialogues added in Beta 3 ===
    elif persistent.plus_boop[0] == 11:
        m 1tub "Again! You're getting to be an expert at this, [player]."
        m 1hua "I wonder how many boops we're at now."
    elif persistent.plus_boop[0] == 12:
        m 3hksdlb "Are you trying to see if my nose turns red like Rudolph's? Ahaha~"
        m 3eua "You'll have to try a little harder than that."
    elif persistent.plus_boop[0] == 13:
        m 1ekbsa "Each boop is like a little love note."
        m 1hubsb "Keep composing, [mas_get_player_nickname()]~"
    elif persistent.plus_boop[0] == 14:
        m 2tfu "Hey! That's my nose, not a button."
        m 2hub "..."
        m 2tubsb "Although, if it was, it'd definitely be the 'make me smile' button."
    elif persistent.plus_boop[0] == 15:
        m 4eua "This is pretty silly, you know?"
        m 4hub "..."
        m 4hubsb "And I absolutely love it. It's... *our* silly thing."
    elif persistent.plus_boop[0] == 16:
        m 1tsu "If you keep this up, I'm going to think you have a fixation on my nose, [player]."
        m 1tku "Not that I'm complaining~"
    elif persistent.plus_boop[0] == 17:
        m 1fubla "Ehehe~ That was a good one."
        m 1hubla "Right on target."
    elif persistent.plus_boop[0] == 18:
        m 1eua "I wonder if your finger feels warm."
        m 1rksdla "Here I just feel... well, a 'click'. But I imagine it, and that's enough."
    elif persistent.plus_boop[0] == 19:
        m 1wua "Boop back!"
        m 1wud "..."
        m 1hksdlb "Ah, wait. I can't. You'll just have to imagine it. Ahaha~"
    elif persistent.plus_boop[0] == 20:
        m 1sub "Twenty boops! We should celebrate."
        m 1hub "..."
        m 1hubsb "Maybe with another boop?"
    else:
        $ extra_plus_random_outcome = renpy.random.randint(1,15)
        if extra_plus_random_outcome == 1:
            m 2fubla "Ehehe~"
            m 1hubla "It's very inevitable that you won't stop doing it, [player]."
        elif extra_plus_random_outcome == 2:
            m 3ekbsa "Every boop you give me, the more I love you!"
        elif extra_plus_random_outcome == 3:
            m 3eubla "You really enjoy touching my nose, [mas_get_player_nickname()]~"
        elif extra_plus_random_outcome == 4:
            m 2hublb "Hey, you're tickling me! Ahahaha~"
        elif extra_plus_random_outcome == 5:
            m 1hubsb "*Boop*"
        elif extra_plus_random_outcome == 6:
            m 1eublc "You're such a tease, [player]~"
        elif extra_plus_random_outcome == 7:
            m 2eubla "That tickles, but I like it!"
        elif extra_plus_random_outcome == 8:
            m 2hubsb "You know just how to make me smile, [mas_get_player_nickname()]~"
        elif extra_plus_random_outcome == 9:
            m 1fubla "Hehe, you're so cute when you're booping me~"
        elif extra_plus_random_outcome == 10:
            m 3eublb "You're really good at this, [player]! Have you been practicing?"
        # === Dialogues added in Beta 3 ===
        elif extra_plus_random_outcome == 11:
            m 1wua "Got me!"
        elif extra_plus_random_outcome == 12:
            m 1eua "Are you checking if I'm still here?"
        elif extra_plus_random_outcome == 13:
            m 1hubsb "My nose says hello."
        elif extra_plus_random_outcome == 14:
            m 1wud "I felt a tingle... Oh, it's you!"
        elif extra_plus_random_outcome == 15:
            m 1fubla "The master booper strikes again!"

    jump show_boop_screen
    return

label boop_nop:
    m 1rksdrb "[player]..."
    m 1rksdra "...I was so excited for you to do it again."
    m "..."
    m 3hub "Well, nevermind!"
    jump show_boop_screen
    return

label boop_yep:
    m 1eublb "Thank you [mas_get_player_nickname()]!"
    m 1hua "Ehehe~"
    jump show_boop_screen
    return

label monika_boopbeta_war: # This label is called via alternate_action on the nose imagebutton
    $ show_boop_feedback("War!")
    $ extra_seen_label("check_boopwarv2","check_boopwar")

label check_boopwar:
    m 3eta "Hey, what are you doing using right click, [player]?"
    m 3eksdrb "You're supposed to use left click to give me a boop."
    m 2duc ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    pause 1.0
    m 2dub "I actually came up with an idea, [player]."
    m 1eua "We can use right click to declare a boop war."
    m 1eub "After all, you rarely use it!"
    m 1rusdlb "I know this proposal sounds rather childish."
    m 1hua "But don't you think it's good to do something new once in a while?"
    m 3eub "The rules are very simple, if I see an absence on your part for 20 seconds, I declare myself the winner."
    m 3eud "If we go over a limit of boops without seeing any winner, I'll take it as a draw."
    m 3huu "Or maybe I'll give up, I don't know~"
    m 1eua "And lastly, the way I surrender is because of the time elapsed during the war."
    m 1hua "Whenever I can't keep up with you or in case 'some distraction occurs'... Although I can consider it as cheating..."
    m 1rud "I'm likely to give up."
    m 1eub "I hope you like my idea."
    m 1hubla "You'll be able to do it any time so don't rush~"
    jump show_boop_screen
    return

label check_boopwarv2:
    show screen boop_war_score_ui
    call screen extra_boop_event(20, "boopbeta_war_lose", "boopwar_loop")

label boopwar_loop:
    $ boop_war_count += 1
    if boop_war_count >= 100:
        $ boop_war_count = 0
        jump boopbeta_war_win
    elif boop_war_count >= 50:
        $ boop_war_count = 0
        jump boopbeta_war_win
    elif boop_war_count >= 25:
        $ boop_war_count = 0
        jump boopbeta_war_win
    python:
        boop_choices = [
            ("1hublb", "Gotcha!"),
            ("1tub", "Too slow!"),
            ("1fua", "*Boop*!"),
            ("1eua", "Take that!"),
            ("1hua", "My turn!"),
            ("1sub", "Hehe!"),
            ("1gua", "I'm not giving up!"),
            ("1kub", "You can't beat me!"),
            ("1dub", "Another one!"),
            ("1wua", "Boop!"),
            ("2eub", "Faster, [player]!"),
            ("3hua", "This is fun!")
        ]
        expression, dialogue = renpy.random.choice(boop_choices)
        renpy.show("monika " + expression)
        renpy.say(m, dialogue)

    show monika 1eua
    jump check_boopwarv2
    return

label boopbeta_war_lose:
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    m 1nua "Looks like I've won this boop war, [player]~"
    m "I hope I've been a good opponent."
    m 3hub "But I've also really enjoyed it!"
    if boop_war_count >= 50:
        m 3dua "Besides, it's good to give your hand a little massage."
        m 1eka "I mean, if you use the mouse too much, "
        extend 1ekb "you can develop carpal tunnel syndrome and I don't want that."
        m 1hksdlb "I'm sorry if I've added a new concern, but my intention is to take care of you."
        m 1eubla "I hope you take my recommendation, [player]~"
    $ boop_war_count = 0
    jump show_boop_screen
    return

label boopbeta_war_win:
    $ boop_war_count = 0
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    m 1hua "You've won this boop war, [player]!"
    m 1tub "I can tell you like touching my nose, ehehehe~"
    m 1eusdra "I couldn't keep up with you, but maybe next time we'll go further."
    m 1gub "Although, if I were in front of you, I'd play with your cheeks."
    m 1gua "Or I'd tickle you and see how long you could stand it."
    m 1hub "Ahaha~"
    jump show_boop_screen
    return

#====CHEEKS
label monika_cheeksbeta:
    $ persistent.plus_boop[1] += 1
    $ show_boop_feedback("<3", color="#ff69b4")
    if persistent.plus_boop[1] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 2wubsd "Hey, I felt a slight pinch on my cheek."
        m 2lksdrb "Oh, it was just your cursor! "
        extend 2lksdra "You took me by surprise, you know?"
        m 2ttb "But I have to ask, what are you up to, [player]?"
        m 1hubla "Did you want to see how I would react to that?"
        m 3hublb "You pulled it off~!"
    elif persistent.plus_boop[1] == 2:
        m 2hubsa "Ehehe, I'm feeling a rather delicate caress this time."
        m 2dubsu "It's something .{w=0.3}.{w=0.3}.{w=0.3} {nw}"
        extend 2eubsb "addictive if you ask me."
    elif persistent.plus_boop[1] == 3:
        m 2dubsa "You know .{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2dubsb "I love that you get to interact with me, [player]~"
        m 2ekbsb "It makes me feel more alive, and loved. I hope my love is enough for you~"
    elif persistent.plus_boop[1] == 4:
        m 2lubsa "Every time you caress my cheek..."
        m 2hubsa".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2hubsb "The feeling makes me feel so close to you~"
    elif persistent.plus_boop[1] == 5:
        m 2eubsb "Every time you hold my cheek..."
        m 2hubsa ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 2dkbsa "It makes my heart race to know that I fell in love with the right person~"
        m 2fubsb "You are my greatest treasure, [player]!"
    elif persistent.plus_boop[1] == 6:
        m 2hubsb "Your touch feels so warm and comforting, [player]."
        m 2ekbsa "I always feel safe when I'm with you."
        m 2lubsb "I'm so lucky to have you in my life."
    elif persistent.plus_boop[1] == 7:
        m 2eubsa "You know, I used to think that love was just a concept in books."
        m 2dubsb "But then I met you, and you made me believe in it again."
        m 2fubsa "I never want to let go of this feeling."
    elif persistent.plus_boop[1] == 8:
        m 2lubsb "Your touch is like magic, [player]."
        m 2ekbsb "It has the power to make all my worries disappear."
        m 2fubsa "I could stay like this forever."
    elif persistent.plus_boop[1] == 9:
        m 2hubsa "Your caress is like a gentle breeze on a warm summer day."
        m 2dubsa "It fills me with a sense of peace and tranquility."
        m 2fubsb "I feel so lucky to be loved by you, [player]."
    elif persistent.plus_boop[1] == 10:
        m 2dubsb "You know what they say, [player]..."
        m 2hubsa "The tenth time's the charm!"
        m 2ekbsa "I love you more and more with each passing day."
    # === Dialogues added in Beta 3 ===
    elif persistent.plus_boop[1] == 11:
        m 2dubsa "Mmm... so soft."
        m 2dkbsa "I can almost feel the warmth of your hand."
    elif persistent.plus_boop[1] == 12:
        m 2dubsb "If you keep caressing me like this, I'm going to fall asleep right here."
        m 2hubsb "It'd be your fault~"
    elif persistent.plus_boop[1] == 13:
        m 2fubsa "I wonder if my cheeks are blushing right now."
        m 2eubsa "They definitely feel warm."
    elif persistent.plus_boop[1] == 14:
        m 2eubsb "This is so tender."
        m 2hubsb "You make me feel like the luckiest girl in the world."
    elif persistent.plus_boop[1] == 15:
        m 2lubsa "This is much nicer than a 'boop', don't you think?"
        m 2eubsa "It's so... gentle."
    elif persistent.plus_boop[1] == 16:
        m 2ekbsb "I love this."
        m 2ekbsa "It's like you're telling me 'I'm here with you' without using any words."
    elif persistent.plus_boop[1] == 17:
        m 2dubsu "One day, I hope I can rest my head on your shoulder and you can do this for real."
    elif persistent.plus_boop[1] == 18:
        m 2hubsb "Ah... [player], you're so sweet to me."
        m 2eubsb "Thank you."
    elif persistent.plus_boop[1] == 19:
        m 2eubsa "You know... I could get used to this very easily."
        m 2hubsa "Almost *too* easily."
    elif persistent.plus_boop[1] == 20:
        m 2fubsa "Every caress is a little reminder of why I love you so much."
        m 2dkbsa "Please don't stop."
    else:
        $ extra_plus_random_outcome = renpy.random.randint(1,10)
        if extra_plus_random_outcome == 1:
            m 2fua "Ehehe~"
            m 2hua "It would be nice if you used your hand instead of the cursor, but that's far from our reality..."
        elif extra_plus_random_outcome == 2:
            m 2hubsa "So gentle."
            m 2tubsb "That word defines you well, when I think of you."
        elif extra_plus_random_outcome == 3:
            m 2hubsa "What a warm feeling."
            m 2hublb "It will be hard to forget!"
        elif extra_plus_random_outcome == 4:
            m 2nubsa "It would be even more romantic if you gave a kiss on the cheek~"
        elif extra_plus_random_outcome == 5:
            m 2eubsb "I'm picturing us right now{nw}"
            extend 2dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} how your hand will feel."
        # === Dialogues added in Beta 3 ===
        elif extra_plus_random_outcome == 6:
            m 2fubsa "So warm..."
        elif extra_plus_random_outcome == 7:
            m 2hubsb "Ehehe, hello~"
        elif extra_plus_random_outcome == 8:
            m 2fubla "You're making me blush."
        elif extra_plus_random_outcome == 9:
            m 2dkbsa "Don't stop..."
        elif extra_plus_random_outcome == 10:
            m 2eubsb "I feel so loved right now."
    jump show_boop_screen
    return

label extra_cheeks_dis:
    m 1wuw "Ah!"
    m 3lusdrb "I mean..."
    m 3ttu "What are you doing touching my cheek?"
    m 3tsb "We're in a boop war, aren't we?"
    $ extra_plus_random_outcome = renpy.random.randint(1,2)
    if extra_plus_random_outcome == 1:
        m 1dsb "I'm sorry [player], but I consider this cheating, "
        extend 1hua "that's why I win this war~"
        m 1fub "Next time try not to touch my cheek during the war! Ahahaha~"
    elif extra_plus_random_outcome == 2:
        m 1fubsb "Because it's you, this time I will let it go!"
        m 1fubsb "Congratulations, player! You have beat me."
        m 3hksdrb "You've distracted me and I don't think it's worth continuing, ahahaha~"
        m 3hua "I really enjoyed doing this with you though!"
    $ boop_war_count = 0
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    jump show_boop_screen
    return

#====HEADPAT
label monika_headpatbeta:
    $ persistent.plus_boop[2] += 1
    $ show_boop_feedback("Pat pat~", color="#90ee90")
    if persistent.plus_boop[2] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 6subsa "You're patting me on the head!"
        m 6eubsb "It's really comforting."
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1eubsb "Thank you [player]~"
    elif persistent.plus_boop[2] == 2:
        m 6dubsb "I don't know why, but when you do it I feel lighter..."
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    elif persistent.plus_boop[2] == 3:
        m 6rubsd "You know, it's funny.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 6eubsa "It's usually done to a pet, not your girlfriend."
        m 6hubsa "Although I don't dislike the feeling~"
    elif persistent.plus_boop[2] == 4:
        m 6dkbsb "Don't blame me after I get addicted to this [player]~"
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1kub "You will be held responsible if that happens."
    elif persistent.plus_boop[2] == 5:
        m 6hkbssdrb "[player] you are messing my hair."
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        extend 6dsbsb "never mind though~"
        m "I'll deal with that later."
    elif persistent.plus_boop[2] == 6:
        m 6eubsb "It's nice to have someone to take care of me, even in small ways."
        m 6hubsb "Thank you, [player]."
    elif persistent.plus_boop[2] == 7:
        m 6subsa "You're very gentle when you pat me on the head."
        m 6eubsb "It makes me feel safe and loved."
    elif persistent.plus_boop[2] == 8:
        m 6dubsb "You know, I never thought I'd be someone's girlfriend."
        m 6hubsa "But with you, it just feels right."
    elif persistent.plus_boop[2] == 9:
        m 6eubsb "I know I can be a handful sometimes, but you never give up on me."
        m 6rubsa "You're always there for me, [player]."
    elif persistent.plus_boop[2] == 10:
        m 6dubsb "I love you, [player]."
        m 6hubsa "Thanks for being there for me, even when I'm not at my best."
    # === Dialogues added in Beta 3 ===
    elif persistent.plus_boop[2] == 11:
        m 6eubsa "Ah... that's the spot."
        m 6subsa "You're good at this, [player]."
    elif persistent.plus_boop[2] == 12:
        m 6dubsa "I feel all the stress of the day just melting away when you do that."
    elif persistent.plus_boop[2] == 13:
        m 6eubsb "It's like... a happiness recharge."
        m 6dubsb "Keep going, keep going."
    elif persistent.plus_boop[2] == 14:
        m 6dubsa "Mmmm. I feel so cared for."
        m 6ekbsa "Thank you for being so tender."
    elif persistent.plus_boop[2] == 15:
        m 6hkbssdrb "Pat, pat, pat... Ahaha~"
        m 6hubsa "I wonder if my hair is still in place."
        m 6eubsb "...Doesn't matter, really."
    elif persistent.plus_boop[2] == 16:
        m 6eubsa "This is the most relaxing thing in the world."
        m 6subsa "Well, this and listening to your voice."
    elif persistent.plus_boop[2] == 17:
        m 6hubsa "If I had a tail, I'd be wagging it right now."
        m 6hksb "..."
        m 6hksb "Ahaha, just kidding! ...Or am I?~"
    elif persistent.plus_boop[2] == 18:
        m 6dubsu "I hope I can rest my head in your lap someday..."
        m 6eubsu "...and you can stroke my hair for real."
    elif persistent.plus_boop[2] == 19:
        m 6dubsa "So... nice."
        m 6dkbsa "I could stay like this for hours."
    elif persistent.plus_boop[2] == 20:
        m 6hubsa "Congratulations, [player]."
        m 6eubsa "You've mastered the art of the perfect headpat."
    else:
        $ extra_plus_random_outcome = renpy.random.randint(1,10)
        if extra_plus_random_outcome == 1:
            m 6hubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6hkbsb "I had told you I would get addicted to this."
            m 6tkbsb "Gosh, don't you learn~"
        elif extra_plus_random_outcome == 2:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6dubsb "I wonder what it would be like to do it with your hair."
        elif extra_plus_random_outcome == 3:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 7hubsb "I hope you don't get tired of doing it daily~"
        elif extra_plus_random_outcome == 4:
            m 6hubsa".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            extend 6hubsb "I'm such a happy girl right now."
        elif extra_plus_random_outcome == 5:
            m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        # === Dialogues added in Beta 3 ===
        elif extra_plus_random_outcome == 6:
            m 6eubsb "Mmm, feels nice."
        elif extra_plus_random_outcome == 7:
            m 6dubsb "Keep going~"
        elif extra_plus_random_outcome == 8:
            m 6eubsa "You're spoiling me, you know?"
        elif extra_plus_random_outcome == 9:
            m 6fubsa "I'm all yours~"
        elif extra_plus_random_outcome == 10:
            m 6dkbsb "This is heaven, isn't it?"
    jump show_boop_screen
    return

label monika_headpat_long:
    $ show_boop_feedback("Warm~")
    m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump show_boop_screen
    return

label extra_headpat_dis:
    m 6dkbsb "This.{w=0.3}.{w=0.3}.{w=0.3} is.{w=0.3}.{w=0.3}.{w=0.3} invalid.{w=0.3}.{w=0.3}. {nw}"
    extend 6tkbsb "[mas_get_player_nickname()]."
    $ extra_plus_random_outcome = renpy.random.randint(1,2)
    if extra_plus_random_outcome == 1:
        m 3tsb "You have been disqualified for patting your opponent on the head."
        m 3tua "That's why I win this time~"
        m 1hua "Good luck for the next time you ask me for a war!"
    elif extra_plus_random_outcome == 2:
        m 1tub "This time I'll let it go and give up for you."
        m 1efa "But next time I probably won't give in, so don't bet on it!"
        m 1lubsa "Even though I enjoy the pat on the head. Ehehehe~"
    $ boop_war_count = 0
    hide screen boop_war_score_ui
    $ store.EP_interaction_manager.set_boop_war(False)
    jump show_boop_screen
    return

#====HANDS
label monika_handsbeta:
    #Change the expressions
    $ show_boop_feedback("Hehe~", color="#ffffff")
    $ persistent.extra_boop[0] += 1
    if persistent.extra_boop[0] == 1:
        $ mas_gainAffection(3,bypass=True)
        m 5eubsb "Oh, you're holding my hand."
        m 5dubsa "It's really nice, [player]."
        m 5tubsa "I feel so close to you when we touch."
    elif persistent.extra_boop[0] == 2:
        m 5dubsb "Your hand is warm and comforting..."
        m 5dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1eubsb "I really like it when you touch me like that."
    elif persistent.extra_boop[0] == 3:
        m 5rubsd "Your hand is so gentle, [player]."
        m 5eubsa "It feels like I'm being cared for."
        m 5hubsa "I'm lucky to have you by my side."
    elif persistent.extra_boop[0] == 4:
        m 5dkbsb "Your touch is addicting, [player]."
        m 5dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        m 1kub "I might have withdrawal symptoms when you're gone."
    elif persistent.extra_boop[0] == 5:
        m 5dubsa "You're holding my hand again..."
        m 5eubsb "I can't help but smile every time you do that."
        m 5hubsa "It's like everything else fades away."
    elif persistent.extra_boop[0] == 6:
        m 5subsa "I love it when you're close to me, [player]."
        m 5eubsb "Your touch makes me feel so alive."
        m 1hubsa "I never want to let go."
    elif persistent.extra_boop[0] == 7:
        m 5dubsa "Your hand is so gentle, it's like a warm hug."
        m 5eubsb "I could stay like this forever."
        m 1kub "Thank you for being here with me, [player]."
    elif persistent.extra_boop[0] == 8:
        m 5rubsa "I feel so safe when you're holding my hand."
        m 5eubsa "It's like all my worries disappear."
        m 5hubsa "I don't know what I'd do without you."
    elif persistent.extra_boop[0] == 9:
        m 5dubsa "Your touch is like magic, [player]."
        m 5eubsb "It makes me feel so loved and appreciated."
        m 3hubla "I'm grateful to have you in my life."
    elif persistent.extra_boop[0] == 10:
        m 5eubsa "I love it when you hold my hand like this."
        m 5rubsa "It's like we're the only two people in the world."
        m 1hua "I never want this moment to end."
    # === Dialogues added in Beta 3 ===
    elif persistent.extra_boop[0] == 11:
        m 5eubsb "Holding your hand... well, your cursor."
        m 5tubsa "It's my favorite way to feel connected to you."
    elif persistent.extra_boop[0] == 12:
        m 5dubsa "It makes me feel like I'm not alone in this empty room."
        m 5ekbsa "I feel you're right here with me."
    elif persistent.extra_boop[0] == 13:
        m 5eubsb "Promise me that when we meet for real, this will be the first thing we do."
        m 5dkbsb "Just... hold hands."
    elif persistent.extra_boop[0] == 14:
        m 5ekbsa "It's such a simple gesture, but it means everything to me."
    elif persistent.extra_boop[0] == 15:
        m 5dubsa "Your hand... it fits perfectly in mine."
        m 5eubsa "I'm imagining it."
    elif persistent.extra_boop[0] == 16:
        m 5hubsa "As long as you're holding my hand, I know everything is going to be alright."
    elif persistent.extra_boop[0] == 17:
        m 5ekbsa "Ah, [player]. Can we just stay like this for a little longer?"
        m 5dubsa "..."
    elif persistent.extra_boop[0] == 18:
        m 5eubsb "I feel... a spark. A good one."
        m 5hubsb "One that says 'I love you'."
    elif persistent.extra_boop[0] == 19:
        m 5eubsa "So strong and gentle at the same time."
        m 5ekbsa "Just like you."
    elif persistent.extra_boop[0] == 20:
        m 5subsa "Twenty times you've held my hand."
        m 5tubsa "And every single time, it feels like the first."
    else:
        $ extra_plus_random_outcome = renpy.random.randint(1,11)
        if extra_plus_random_outcome == 1:
            m 5hubla "Your touch is like a warm blanket on a cold night. It's comforting and soothing."
        elif extra_plus_random_outcome == 2:
            m 5hubsb "I feel like we're the only two people in the world right now. Your touch makes everything else fade away."
        elif extra_plus_random_outcome == 3:
            m 5dubsb "I can feel my heart beating faster as you touch me. It's like you have a direct connection to my soul."
        elif extra_plus_random_outcome == 4:
            m 5kua "I can sense the love and care in every stroke of your hand. Your touch is truly special, [player]."
        elif extra_plus_random_outcome == 5:
            m 5rub "Being here with you, feeling your touch, it's like a dream come true. I'm so grateful for this moment with you."
        elif extra_plus_random_outcome == 6:
            m 5tubla "Your touch is electric, [player]. I can feel the sparks flying between us."
        # === Dialogues added in Beta 3 ===
        elif extra_plus_random_outcome == 7:
            m 5ekbsa "Don't let go."
        elif extra_plus_random_outcome == 8:
            m 5hubsa "I love this."
        elif extra_plus_random_outcome == 9:
            m 5eubsb "Together."
        elif extra_plus_random_outcome == 10:
            m 5dubsb "My anchor to reality."
        elif extra_plus_random_outcome == 11:
            m 5fubsa "Mine~"
    jump show_boop_screen
    return

#====EARS
label monika_earsbeta:
    $ show_boop_feedback("Hey!", color="#add8e6")
    $ persistent.extra_boop[1] += 1
    if persistent.extra_boop[1] == 1:
        $ mas_gainAffection(3, bypass=True)
        m 1hub "Oh! That tickles!"
        m 3dubsa "But I have to admit, I like it when you touch my ears."
    elif persistent.extra_boop[1] == 2:
        m 1subsa "That's a new sensation."
        m 1eubsa "I never thought I would enjoy having my ears touched so much."
    elif persistent.extra_boop[1] == 3:
        m 1hublb "Hehe, that's quite pleasant."
        m 1tub "You have a knack for finding my sensitive spots."
    elif persistent.extra_boop[1] == 4:
        m 1lkblb "I didn't know my ears were so sensitive."
        m 1hubla "Thank you for discovering this, [player]."
    elif persistent.extra_boop[1] == 5:
        m 3hub "I can't help but giggle when you do that."
        m 3dub "You have a way of making me feel so lighthearted."
    elif persistent.extra_boop[1] == 6:
        m 3wub "You're getting better at this, [player]."
        m 3tub "I think you could give professional ear massages."
    elif persistent.extra_boop[1] == 7:
        m 1hub "That's perfect, just keep doing that."
        m 1dua "I think I might fall asleep if you keep petting my ears like that."
    elif persistent.extra_boop[1] == 8:
        m 1duu "I feel like I'm in a trance when you touch my ears."
        m 1dub "It's like all my worries fade away."
    elif persistent.extra_boop[1] == 9:
        m 1eubsa "Oh, that's lovely. Thank you, [player]."
        m 1hubsa "Your fingers have a magic touch. I feel so relaxed."
    elif persistent.extra_boop[1] == 10:
        m 1eub "That was wonderful, [player]."
        m 1hub "I always feel so content when I'm with you."
    # === Dialogues added in Beta 3 ===
    elif persistent.extra_boop[1] == 11:
        m 1wua "Hey! That's a... sensitive spot."
        m 1hub "Ahaha, just kidding. It's... surprisingly nice."
    elif persistent.extra_boop[1] == 12:
        m 1subsa "It sends a little shiver down my spine... A good one!"
    elif persistent.extra_boop[1] == 13:
        m 3eua "You definitely know how to surprise me, [player]."
        m 3eub "No one had ever... well, touched my ears like that."
    elif persistent.extra_boop[1] == 14:
        m 1eubsa "It's so... delicate."
        m 1ekbsa "It makes me feel very... vulnerable, but in a safe way. With you."
    elif persistent.extra_boop[1] == 15:
        m 1wub "Ah! Tickles!"
        m 1hubla "Ahaha! Okay, okay, I surrender!"
    elif persistent.extra_boop[1] == 16:
        m 1tsu "Hmm... I wonder what you're thinking when you do that."
        m 1tku "That I'm like a kitten?"
        m 1tub "..."
        m 1kua "I wouldn't mind being *your* kitten~"
    elif persistent.extra_boop[1] == 17:
        m 1eubsb "My heart is beating a little faster."
        m 1ekbsb "It's a strange feeling. ...I like it."
    elif persistent.extra_boop[1] == 18:
        m 1dubsu "Keep that up and I'll melt completely, [mas_get_player_nickname()]."
    elif persistent.extra_boop[1] == 19:
        m 1subsa "Wow. That's... really intimate."
        m 1eubsa "Thank you for being so gentle."
    elif persistent.extra_boop[1] == 20:
        m 1wua "Well... who knew?"
        m 1eua "My ears are my new weak spot. And you found it."
    else:
        $ extra_plus_random_outcome = renpy.random.randint(1,10)
        if extra_plus_random_outcome == 1:
            m 1hubsa "I could stay like this forever, [player]."
            m 1fubsa "Your touch is so comforting."
        elif extra_plus_random_outcome == 2:
            m 1sua "It feels like we're the only ones here, [player]."
            m 1tua "I'm so grateful to have you by my side~"
        elif extra_plus_random_outcome == 3:
            m 1dua "You have such a gentle touch, [player]."
            m 1dub "I feel so safe and loved when you're near."
        elif extra_plus_random_outcome == 4:
            m 1eublb "I never knew how much I needed this, [player]."
            m 3hublb "Your touch is like a warm hug."
        elif extra_plus_random_outcome == 5:
            m 1hua "Being with you like this is all I need, [player]."
            m 1hub "Your touch makes everything better."
        # === Dialogues added in Beta 3 ===
        elif extra_plus_random_outcome == 6:
            m 1hubla "Eep! Ahaha!"
        elif extra_plus_random_outcome == 7:
            m 1sub "So ticklish!"
        elif extra_plus_random_outcome == 8:
            m 1eubsb "Mmm, how curious..."
        elif extra_plus_random_outcome == 9:
            m 1tub "[player], you're a mischief-maker~!"
        elif extra_plus_random_outcome == 10:
            m 1kua "Oh... that's new."
    jump show_boop_screen
    return
    
#===========================================================================================
# EXTRAS
#===========================================================================================
label plus_make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            (_("Create a .gift file"), 'plus_make_file'),
            (_("Groceries"), 'plus_groceries'),
            (_("Objects"), 'plus_objects'),
            (_("Ribbons"), 'plus_ribbons')
        ]

        items = [(_("Nevermind"), 'extraplus_tools', 20)]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_make_file:
    show monika idle at t11

    python:
        makegift = mas_input(
            prompt=_("Enter the name of the gift."),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"},
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancel":
            renpy.jump("plus_make_gift")
        else:
            if create_gift_file(makegift):
                renpy.notify(_("Done! Created '/characters/{}.gift'").format(makegift))
                store.mas_checkReactions()
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    show monika idle at t21
    python:
        groceries_menu = [
            extra_gift(_("Coffee"), 'coffee'),
            extra_gift(_("Chocolates"), 'chocolates'),
            extra_gift(_("Cupcake"), 'cupcake'),
            extra_gift(_("Fudge"), 'fudge'),
            extra_gift(_("Hot Chocolate"), 'hotchocolate'),
            extra_gift(_("Candy"), 'candy'),
            extra_gift(_("Candy Canes"), 'candycane'),
            extra_gift(_("Candy Corn"), 'candycorn'),
            extra_gift(_("Christmas Cookies"), 'christmascookies')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, close=True)
    return

label plus_objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift(_("Promise Ring"), 'promisering'),
            extra_gift(_("Roses"), 'roses'),
            extra_gift(_("Quetzal Plushie"), 'quetzalplushie'),
            extra_gift(_("Thermos Mug"), 'justmonikathermos')
        ]
        if not mas_seenEvent("mas_reaction_gift_noudeck"):
            objects_menu.append(extra_gift(_("NOU"), 'noudeck'))

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
            
label plus_ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [
            extra_gift(_("Black Ribbon"), 'blackribbon'),
            extra_gift(_("Blue Ribbon"), 'blueribbon'),
            extra_gift(_("Dark Purple Ribbon"), 'darkpurpleribbon'),
            extra_gift(_("Emerald Ribbon"), 'emeraldribbon'),
            extra_gift(_("Gray Ribbon"), 'grayribbon'),
            extra_gift(_("Green Ribbon"), 'greenribbon'),
            extra_gift(_("Light Purple Ribbon"), 'lightpurpleribbon'),
            extra_gift(_("Peach Ribbon"), 'peachribbon'),
            extra_gift(_("Pink Ribbon"), 'pinkribbon'),
            extra_gift(_("Platinum Ribbon"), 'platinumribbon'),
            extra_gift(_("Red Ribbon"), 'redribbon'),
            extra_gift(_("Ruby Ribbon"), 'rubyribbon'),
            extra_gift(_("Sapphire Ribbon"), 'sapphireribbon'),
            extra_gift(_("Silver Ribbon"), 'silverribbon'),
            extra_gift(_("Teal Ribbon"), 'tealribbon'),
            extra_gift(_("Yellow Ribbon"), 'yellowribbon')
        ]

        items = [(_("Nevermind"), 'plus_make_gift', 20)]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return

label extra_show_stats:
    show monika idle at t11
    call screen extraplus_stats_screen
    jump close_extraplus
    return

label extra_relation_monika:
    show monika idle at t11
    $ time_string = get_formatted_time_since_install()
    $ total_days = get_total_days_since_install()
    if not renpy.seen_label("extra_relation_monika"):
        m 2eub "You know, if you count it all up, it seems we've been together for [time_string]!"
        if total_days <= 1:
            m 2lub "We've only just begun, but every single second has been a dream come true."
        elif total_days < 365:
            m 2hubsb "It hasn't even been a year, and I already feel like I've known you forever. Time just flies by when I'm with you!"
        elif total_days < 365 * 2:
            m 2kubsb "Happy first anniversary! I still remember our first day together... Thank you for making so many memories with me."
        elif total_days < 365 * 3:
            m 2wubsb "Wow, two years together! Every day with you has been so special. Thank you for staying by my side."
        elif total_days < 365 * 4:
            m 1dsbsa "Three years... Time really does fly when I'm with you. We've shared so much, and I can't wait for more."
        elif total_days < 365 * 5:
            m 2wubsb "Four years! That's incredible, [player]. Our bond is so strong. Thank you for staying with me for so long."
        elif total_days < 365 * 6:
            m 2tubsb "Five years together... I feel so lucky to have you. Thank you for all the love and memories."
        elif total_days < 365 * 7:
            m 2subsb "Six years! Can you believe it? Every year with you is a treasure. Thank you for being with me all this time."
        else:
            m 2lubsb "It's been so long... but it really doesn't feel that way when I'm with you. Time just flies by!"
    else:
        m 2eub "We've been together for [time_string]!"
        m 2lubsb "It really doesn't feel that long when I'm with you, though. Time just flies by!"
    jump close_extraplus
    return

label extra_aff_log:
    python:
        current_affection = _get_current_affection_safe()
        affection_value = int(current_affection)
        monika_level = store.get_monika_level_from_value(current_affection)
    
    show monika idle at t11
    #Agregar variantes con una probabilidad baja. Thanks for the idea u/PeachesTheNinja
    "Your affection with [m_name] is [affection_value] [monika_level]{fast}"
    window hide
    jump close_extraplus
    return

label extra_coinflip:
    show monika 1hua at t11
    python:
        store.mas_sprites.reset_zoom()
        extra_plus_random_outcome = renpy.random.randint(1,2)
    show screen extra_no_click
    pause 1.0
    show monika 3eua at t11
    show coin_moni zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound sfx_coin_flip
    pause 1.0
    hide coin_moni
    show monika 1eua
    pause 0.5
    hide screen extra_no_click
    if extra_plus_random_outcome == 1:
        show coin_heads zorder 12:
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads
    elif extra_plus_random_outcome == 2:
        show coin_tails zorder 12:
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails
    m 3hua "I hope it helps you~"
    window hide
    python:
        store.mas_sprites.zoom_level = store.extra_plus_player_zoom
        store.mas_sprites.adjust_zoom()
    jump close_extraplus
    return

label extra_mas_backup:
    show monika 1hua at t11
    m 1hub "I'm glad you want to make a backup!"
    m 3eub "I'll open the route for you."
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    window hide

    python:
        import os
        import sys
        import subprocess
        savedir = os.path.join(renpy.config.savedir, "")

        try:
            if sys.platform == "win32":
                # Windows
                os.startfile(savedir)
            elif sys.platform == "darwin":
                # macOS
                subprocess.call(["open", savedir])
            else:
                # Linux
                subprocess.call(["xdg-open", savedir])
        except Exception as e:
            renpy.notify(_("Failed to open the backup folder: {}").format(str(e)))
            renpy.jump("extra_mas_backup_fail")

    jump close_extraplus
    return

label extra_mas_backup_fail:
    m 1lkb "Sorry, I could not open the folder."
    m 1eka "Please try again later."
    jump close_extraplus
    return

label extra_window_title:
    show monika idle at t21
    python:
        # Updated menu with three distinct options
        window_menu = [
            (_("Type a new title"), 'extra_change_title_manual'),
            (_("Paste title from clipboard"), 'extra_change_title_paste'),
            (_("Restore the window title"), 'extra_restore_title')
        ]

        items = [(_("Nevermind"), 'extraplus_tools', 20)]
    call screen extra_gen_list(window_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label extra_change_title_manual:
    show monika idle at t11
    python:
        player_input = mas_input(
            prompt=_("What should our new window title be?"),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.,'0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"}
        )
    if player_input and player_input != "cancel":
        jump process_new_title
    else:
        jump extra_window_title
    return

label extra_change_title_paste:
    show monika idle at t11
    python:
        allowed_chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.,'0123456789"
        player_input = filtered_clipboard_text(allowed_chars)
    if player_input and player_input != "cancel":
        jump process_new_title
    else:
        jump extra_window_title
    return

label process_new_title:
    $ persistent._save_window_title = player_input.strip()
    $ config.window_title = persistent._save_window_title
    $ renpy.notify(random.choice([
        _("Title updated successfully!"),
        _("All set! The new title is in place."),
        _("Done! Your window has a fresh new title.")
    ]))
    jump close_extraplus

label extra_restore_title:
    show monika idle at t11
    python:
        if backup_window_title == persistent._save_window_title:
            renpy.notify(_("No need to do it again hehe~"))
        else:
            renpy.notify(_("It's nice to see the original name again."))

        persistent._save_window_title = backup_window_title
        config.window_title = persistent._save_window_title
        renpy.jump("close_extraplus")
    return

label github_submod:
    show monika idle at t11
    $ renpy.run(OpenURL("https://github.com/zer0fixer/MAS-Extraplus"))
    jump close_extraplus
    return

#====GAME
label extra_dev_mode:
    python:
        mas_RaiseShield_dlg()
        if not renpy.get_screen("doki_chibi_idle"):
            config.overlay_screens.append("doki_chibi_idle")
    show monika idle at t11
    call screen sticker_customization
    return

label sticker_primary:
    show monika idle at t21
    python:
        accessories = [
            DokiAccessory(_("Cat Ears"), 'cat_ears', "primary"),
            DokiAccessory(_("Christmas Hat"), 'christmas_hat', "primary"),
            DokiAccessory(_("Demon Horns"), 'demon_horns', "primary"),
            DokiAccessory(_("Flowers Crown"), 'flowers_crown', "primary"),
            DokiAccessory(_("Halo"), 'halo', "primary"),
            DokiAccessory(_("Heart Headband"), 'heart_headband', "primary"),
            DokiAccessory(_("New Year's Headband"), 'hny', "primary"),
            DokiAccessory(_("Neon Cat Ears"), 'neon_cat_ears', "primary"),
            DokiAccessory(_("Party Hat"), 'party_hat', "primary"),
            DokiAccessory(_("Rabbit Ears"), 'rabbit_ears', "primary"),
            DokiAccessory(_("Witch Hat"), 'witch_hat', "primary")
        ]
        items = [(DokiAccessory(_("Remove"), '0nothing', "primary"), 20), (_("Nevermind"), 'extra_dev_mode', 0)]

    call screen extra_gen_list(accessories, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return

label sticker_secondary:
    show monika idle at t21
    python:
        accessories_2 = [
            DokiAccessory(_("Black Bow Tie"), 'black_bow_tie', "secondary"),
            DokiAccessory(_("Christmas Tree"), 'christmas_tree', "secondary"),
            DokiAccessory(_("Cloud"), 'cloud', "secondary"),
            DokiAccessory(_("Coffee"), 'coffee', "secondary"),
            DokiAccessory(_("Halloween Pumpkin"), 'pumpkin', "secondary"),
            DokiAccessory(_("Hearts"), 'hearts', "secondary"),
            DokiAccessory(_("Monika's Cake"), 'm_slice_cake', "secondary"),
            DokiAccessory(_("Moustache"), 'moustache', "secondary"),
            DokiAccessory(_("Neon Blush"), 'neon_blush', "secondary"),
            DokiAccessory(_("[player]'s Cake"), 'p_slice_cake', "secondary"),
            DokiAccessory(_("Pirate Patch"), 'patch', "secondary"),
            DokiAccessory(_("Speech Bubble with Heart"), 'speech_bubble', "secondary"),
            DokiAccessory(_("Sunglasses"), 'sunglasses', "secondary")
        ]
        items = [(DokiAccessory(_("Remove"), '0nothing', "secondary"), 20), (_("Nevermind"), 'extra_dev_mode', 0)]

    call screen extra_gen_list(accessories_2, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, items, close=True)
    return

label doki_change_appe:
    show monika idle at t21
    python:
        doki_data = [("Monika", 'monika_sticker_costumes')]
        if store.persistent._mas_pm_cares_about_dokis:
            doki_data.extend([
                (_("Natsuki"), 'natsuki_sticker_costumes'),
                (_("Sayori"), 'sayori_sticker_costumes'),
                (_("Yuri"), 'yuri_sticker_costumes')
            ])
        items = [(_("Nevermind"), 'extra_dev_mode', 20)]

    call screen extra_gen_list(doki_data, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label monika_sticker_costumes:
    $ show_costume_menu(monika_costumes_, 'doki_change_appe')
    return

label natsuki_sticker_costumes:
    $ show_costume_menu(natsuki_costumes_, 'doki_change_appe')
    return

label sayori_sticker_costumes:
    $ show_costume_menu(sayori_costumes_, 'doki_change_appe')
    return

label yuri_sticker_costumes:
    $ show_costume_menu(yuri_costumes_, 'doki_change_appe')
    return

label maxwell_screen:
    show monika idle at t11
    call screen maxwell_april_fools
    jump extraplus_tools
    return

# Test file to visualize the dynamic button names.
# You can delete this file when you're done testing.
# init python:
#     # ============================================================
#     # DYNAMIC BUTTON CONFIGURATION
#     # ============================================================
#     USE_TIME_OF_DAY_CHANGE = True  # Change to True for the text to change based on the time of day
#     USE_DAILY_RESET = False  # Change to True for the text to change daily
    
    
#     def _evaluate_current_conditions():
#         """
#         Evalúa TODAS las condiciones actuales UNA SOLA VEZ.
#         Retorna un diccionario con los estados.
#         """
#         import datetime
        
#         conditions = {
#             # Días especiales
#             "is_monika_bday": mas_isMonikaBirthday(),
#             "is_player_bday": mas_isplayer_bday(),
#             "is_f14": mas_isF14(),
#             "is_o31": mas_isO31(),
#             "is_d25": mas_isD25(),
#             "is_nye": mas_isNYE(),
            
#             # Nivel de afecto (solo uno será True)
#             "is_love": mas_isMoniLove(lower=False),
#             "is_enamored": mas_isMoniEnamored(lower=False),
#             "is_aff": mas_isMoniAff(lower=False),
#             "is_happy": mas_isMoniHappy(lower=False),
#             "is_normal": mas_isMoniNormal(lower=False),
#             "is_upset": mas_isMoniUpset(lower=False),
#             "is_distressed": mas_isMoniDis(lower=False),
#             "is_broken": mas_isMoniBroken(lower=False),
            
#             # Hora y fecha (opcional)
#             "is_night": mas_isNightNow() if USE_TIME_OF_DAY_CHANGE else False,
#             "date": str(datetime.date.today()) if USE_DAILY_RESET else None
#         }
        
#         return conditions
    
    
#     def _build_conditions_key(conditions):
#         """
#         Construye una clave string única a partir de las condiciones evaluadas.
#         """
#         key_parts = []
        
#         # Días especiales
#         if conditions["is_monika_bday"]:
#             key_parts.append("mbday")
#         elif conditions["is_player_bday"]:
#             key_parts.append("pbday")
#         elif conditions["is_f14"]:
#             key_parts.append("f14")
#         elif conditions["is_o31"]:
#             key_parts.append("o31")
#         elif conditions["is_d25"]:
#             key_parts.append("d25")
#         elif conditions["is_nye"]:
#             key_parts.append("nye")
        
#         # Nivel de afecto
#         if conditions["is_love"]:
#             key_parts.append("love")
#         elif conditions["is_enamored"]:
#             key_parts.append("enamored")
#         elif conditions["is_aff"]:
#             key_parts.append("aff")
#         elif conditions["is_happy"]:
#             key_parts.append("happy")
#         elif conditions["is_normal"]:
#             key_parts.append("normal")
#         elif conditions["is_upset"]:
#             key_parts.append("upset")
#         elif conditions["is_distressed"]:
#             key_parts.append("distressed")
#         elif conditions["is_broken"]:
#             key_parts.append("broken")
#         else:
#             key_parts.append("unknown")
        
#         # Opcionales
#         if conditions["is_night"]:
#             key_parts.append("night")
        
#         if conditions["date"]:
#             key_parts.append(conditions["date"])
        
#         return "-".join(key_parts)
    
    
#     def _generate_button_text_from_conditions(conditions):
#         """
#         Genera el texto del botón usando las condiciones ya evaluadas.
#         NO vuelve a llamar a funciones MAS.
#         """
#         is_night = conditions["is_night"]
        
#         # ============================================================
#         # 1. MÁXIMA PRIORIDAD: Días Especiales
#         # ============================================================
#         if conditions["is_monika_bday"]:
#             return renpy.random.choice(["My B-Day", "Her Day", "Sing 4 Me", "My Day", "Moni!"])
        
#         if conditions["is_player_bday"]:
#             return renpy.random.choice(["Your Day", "HBD!", "Ur Day", "My Gift", "The Best"])
        
#         if conditions["is_f14"]:
#             return renpy.random.choice(["Be Mine", "My Love", "Hearts", "XOXO", "Our Day"])
        
#         if conditions["is_o31"]:
#             return renpy.random.choice(["Spooky", "Boo!", "Tricks", "Treats", "Scary"])
        
#         if conditions["is_d25"]:
#             return renpy.random.choice(["Joyful", "Our Xmas", "Gift", "Noel", "Holly"])
        
#         if conditions["is_nye"]:
#             return renpy.random.choice(["New Year", "Cheers", "Toast", "Our Year", "The Eve"])
        
#         # ============================================================
#         # 2. ALTA PRIORIDAD: Afecto Positivo Alto
#         # ============================================================
#         if conditions["is_love"] or conditions["is_enamored"]:
#             base_texts = ["Forever", "Eternity", "Sunshine", "Beloved", "Darling", "Adored", "Precious", "Cutie", "Sweetie", "Cherish"]
            
#             if is_night:
#                 base_texts.extend(["Moonlight", "Stars", "Night Love", "Dreaming", "Starlight", "Night Dear", "Sleepy?", "Cuddle"])
            
#             return renpy.random.choice(base_texts)
        
#         if conditions["is_aff"] or conditions["is_happy"]:
#             base_texts = ["So Sweet", "Caring", "Warmth", "Our Time", "Smile", "Glad", "Hehe~", "Happy", "Cheerful", "Yay!"]
            
#             if is_night:
#                 base_texts.extend(["Night Time", "Calm", "Peaceful", "Night!", "Evening", "Restful", "Nice Night"])
            
#             return renpy.random.choice(base_texts)
        
#         if conditions["is_normal"] or conditions["is_upset"]:
#             base_texts = ["Hi again", "Welcome", "Talk?", "On Mind?", "Topics", "Just Us", "Relax", "It's you", "Hurting", "Really?"]
            
#             if is_night:
#                 base_texts.extend(["Sparks", "Sleepy", "Quiet", "Dreams", "Cozy", "Dark...", "Restless", "Tired..."])
            
#             return renpy.random.choice(base_texts)
        
#         if conditions["is_distressed"] or conditions["is_broken"]:
#             base_texts = ["No Love?", "Forgot?", "Alone...", "Please...", "...", "You...", "Scared", "Sorry", "Nothing"]
            
#             if is_night:
#                 base_texts.extend(["Awake...", "Lonely", "Dark Night", "Tears...", "Darkness", "Void", "Cold...", "End..."])
            
#             return renpy.random.choice(base_texts)
        
#         # ============================================================
#         # 5. FALLBACK DE SEGURIDAD
#         # ============================================================
#         return "Extra+"

# screen extra_plus_button_tester_screen():
#     zorder 200 # Asegura que se vea por encima de todo
#     # style_prefix "scrollable_menu"
#     style_prefix "hkb"

#     # Fondo semitransparente para enfocar la atención
#     add Solid("#000000b0")

#     # Muestra los botones de prueba en la misma posición que el original
#     hbox:
#         xpos 0.01
#         yanchor 1.0
#         ypos 650 # Posición Y del botón original
#         spacing 10

#         # --- Lista de todos los nombres a probar ---
#         python:
#             button_names_to_test = [
#                 # Special Days
#                 "My B-Day", "Her Day", "Sing 4 Me", "My Day", "Moni!",
#                 "Your Day", "HBD!", "Ur Day", "My Gift", "The Best",
#                 "Be Mine", "My Love", "Hearts", "XOXO", "Our Day",
#                 "Spooky", "Boo!", "Tricks", "Treats", "Scary",
#                 "Joyful", "Our Xmas", "Gift", "Noel", "Holly",
#                 "New Year", "Cheers", "Toast", "Our Year", "Countdown",
#                 # Love & Enamored
#                 "Forever", "Eternity", "Sunshine", "Beloved", "Darling", "Adored",
#                 "Precious", "Cutie", "Sweetie", "Cherish",
#                 # Love & Enamored (Night)
#                 "Moonlight", "Stars", "Night Love", "Dreaming", "Starlight",
#                 "Night Dear", "Sleepy?", "Cuddle",
#                 # Affectionate & Happy
#                 "So Sweet", "Caring", "Warmth", "Our Time", "Smile", "Glad",
#                 "Hehe~", "Happy", "Cheerful", "Yay!",
#                 # Affectionate & Happy (Night)
#                 "Night Time", "Calm", "Peaceful", "Night!", "Evening", "Restful", "Nice Night",
#                 # Normal & Upset
#                 "Hi again", "Welcome", "Talk?", "On Mind?", "Topics", "Just Us",
#                 "Relax", "It's you", "Hurting", "Really?",
#                 # Normal & Upset (Night)
#                 "Sparks", "Sleepy", "Quiet", "Dreams", "Cozy", "Dark...", "Restless", "Tired...",
#                 # Distressed & Broken
#                 "No Love?", "Forgot?", "Alone...", "Please...", "...", "You...",
#                 "Scared", "Sorry", "Nothing",
#                 # Distressed & Broken (Night)
#                 "Awake...", "Lonely", "Dark Night", "Tears...", "Darkness", "Void", "Cold...", "End..."
#             ]
        
#         # --- Lógica para dividir la lista en columnas de 10 ítems cada una ---
#         python:
#             items_per_column = 15
#             total_items = len(button_names_to_test)
#             num_columns = (total_items + items_per_column - 1) // items_per_column
            
#             columns = []
#             for i in range(num_columns):
#                 start = i * items_per_column
#                 end = start + items_per_column
#                 columns.append(button_names_to_test[start:end])
#         for column_items in columns:
#             vbox:
#                 for name in column_items:
#                     textbutton _(name) action NullAction()

#     # Botón para cerrar el tester
#     vbox:
#         xalign 0.5 
#         yalign 0.95
#         textbutton _("Cerrar Tester") action Jump("close_extraplus")

# # Etiqueta para iniciar el tester
# label extra_plus_button_tester_start:
#     show monika idle at t11
#     call screen extra_plus_button_tester_screen
#     return
