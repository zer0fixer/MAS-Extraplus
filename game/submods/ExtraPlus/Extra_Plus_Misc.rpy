################################################################################
## BOOP
################################################################################

#====NOISE
label monika_boopbeta:
    $ persistent.plus_boop[0] += 1
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
        call screen boop_event(10, "boop_nop", "boop_yep")
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
    else:
        $ moldable_variable = renpy.random.randint(1,10)
        if moldable_variable == 1:
            m 2fubla "Ehehe~"
            m 1hubla "It's very inevitable that you won't stop doing it, [player]."
        elif moldable_variable == 2:
            m 3ekbsa "Every boop you give me, the more I love you!"
        elif moldable_variable == 3:
            m 3eubla "You really enjoy touching my nose, [mas_get_player_nickname()]~"
        elif moldable_variable == 4:
            m 2hublb "Hey, you're tickling me! Ahahaha~"
        elif moldable_variable == 5:
            m 1hubsb "*Boop*"
        elif moldable_variable == 6:
            m 1eublc "You're such a tease, [player]~"
        elif moldable_variable == 7:
            m 2eubla "That tickles, but I like it!"
        elif moldable_variable == 8:
            m 2hubsb "You know just how to make me smile, [mas_get_player_nickname()]~"
        elif moldable_variable == 9:
            m 1fubla "Hehe, you're so cute when you're booping me~"
        elif moldable_variable == 10:
            m 3eublb "You're really good at this, [player]! Have you been practicing?"

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

label monika_boopbeta_war:
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
    call screen boop_event(20, "boopbeta_war_lose", "boopwar_loop")

label boopwar_loop:
    $ boop_war_count += 1
    $ moldable_variable = renpy.random.randint(1,10)
    if moldable_variable == 1:
        m 1hublb "*Boop*"
    elif moldable_variable == 2:
        m 1tub "*Boop*"
    elif moldable_variable == 3:
        if boop_war_count >= 25:
            $ boop_war_count = 0
            jump boopbeta_war_win
        else:
            m 1fua "*Boop*"
    elif moldable_variable == 4:
        m 1eua "*Boop*"
    elif moldable_variable == 5:
        m 1hua "*Boop*"
    elif moldable_variable == 6:
        if boop_war_count >= 50:
            $ boop_war_count = 0
            jump boopbeta_war_win
        else:
            m 1sub "*Boop*"
    elif moldable_variable == 7:
        m 1gua "*Boop*"
    elif moldable_variable == 8:
        m 1kub "*Boop*"
    elif moldable_variable == 9:
        if boop_war_count >= 100:
            $ boop_war_count = 0
            jump boopbeta_war_win
        else:
            m 1dub "*Boop*"
    elif moldable_variable == 10:
        m 1wua "*Boop*"

    show monika 1eua
    jump check_boopwarv2
    return

label boopbeta_war_lose:
    $ boop_war_count = 0
    m 1nua "Looks like I've won this boop war, [player]~"
    m "I hope I've been a good opponent."
    m 3hub "But I've also really enjoyed it!"
    m 3dua "Besides, it's good to give your hand a little massage."
    m 1eka "I mean, if you use the mouse too much, "
    extend 1ekb "you can develop carpal tunnel syndrome and I don't want that."
    m 1hksdlb "I'm sorry if I've added a new concern, but my intention is to take care of you."
    m 1eubla "I hope you take my recommendation, [player]~"
    jump show_boop_screen
    return

label boopbeta_war_win:
    $ boop_war_count = 0
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
    else:
        $ moldable_variable = renpy.random.randint(1,5)
        if moldable_variable == 1:
            m 2fua "Ehehe~"
            m 2hua "It would be nice if you used your hand instead of the cursor, but that's far from our reality..."
        elif moldable_variable == 2:
            m 2hubsa "So gentle."
            m 2tubsb "That word defines you well, when I think of you."
        elif moldable_variable == 3:
            m 2hubsa "What a warm feeling."
            m 2hublb "It will be hard to forget!"
        elif moldable_variable == 4:
            m 2nubsa "It would be even more romantic if you gave a kiss on the cheek~"
        elif moldable_variable == 5:
            m 2eubsb "I'm picturing us right now{nw}"
            extend 2dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3} how your hand will feel."
    jump show_boop_screen
    return

label cheeks_dis:
    m 1wuw "Ah!"
    m 3lusdrb "I mean..."
    m 3ttu "What are you doing touching my cheek?"
    m 3tsb "We're in a boop war, aren't we?"
    $ moldable_variable = renpy.random.randint(1,2)
    if moldable_variable == 1:
        m 1dsb "I'm sorry [player], but I consider this cheating, "
        extend 1hua "that's why I win this war~"
        m 1fub "Next time try not to touch my cheek during the war! Ahahaha~"
    elif moldable_variable == 2:
        m 1fubsb "Because it's you, this time I will let it go!"
        m 1fubsb "Congratulations, player! You have beat me."
        m 3hksdrb "You've distracted me and I don't think it's worth continuing, ahahaha~"
        m 3hua "I really enjoyed doing this with you though!"
    $ boop_war_count = 0
    jump show_boop_screen
    return

#====HEADPAT
label monika_headpatbeta:
    $ persistent.plus_boop[2] += 1
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
    else:
        $ moldable_variable = renpy.random.randint(1,5)
        if moldable_variable == 1:
            m 6hubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6hkbsb "I had told you I would get addicted to this."
            m 6tkbsb "Gosh, don't you learn~"
        elif moldable_variable == 2:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 6dubsb "I wonder what it would be like to do it with your hair."
        elif moldable_variable == 3:
            m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            m 7hubsb "I hope you don't get tired of doing it daily~"
        elif moldable_variable == 4:
            m 6hubsa".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            extend 6hubsb "I'm such a happy girl right now."
        elif moldable_variable == 5:
            m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    jump show_boop_screen
    return

label monika_headpat_long:
    m 6dkbsa ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}{nw}"
    jump show_boop_screen
    return

label headpat_dis:
    m 6dkbsb "This.{w=0.3}.{w=0.3}.{w=0.3} is.{w=0.3}.{w=0.3}.{w=0.3} invalid.{w=0.3}.{w=0.3}. {nw}"
    extend 6tkbsb "[mas_get_player_nickname()]."
    $ moldable_variable = renpy.random.randint(1,2)
    if moldable_variable == 1:
        m 3tsb "You have been disqualified for patting your opponent on the head."
        m 3tua "That's why I win this time~"
        m 1hua "Good luck for the next time you ask me for a war!"
    elif moldable_variable == 2:
        m 1tub "This time I'll let it go and give up for you."
        m 1efa "But next time I probably won't give in, so don't bet on it!"
        m 1lubsa "Even though I enjoy the pat on the head. Ehehehe~"
    $ boop_war_count = 0
    jump show_boop_screen
    return

#====HANDS
label monika_handsbeta:
    #Change de expressions
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
    else:
        $ moldable_variable = renpy.random.randint(1,5)
        if moldable_variable == 1:
            m 5hubla "Your touch is like a warm blanket on a cold night. It's comforting and soothing."
        elif moldable_variable == 2:
            m 5hubsb "I feel like we're the only two people in the world right now. Your touch makes everything else fade away."
        elif moldable_variable == 3:
            m 5dubsb "I can feel my heart beating faster as you touch me. It's like you have a direct connection to my soul."
        elif moldable_variable == 4:
            m 5kua "I can sense the love and care in every stroke of your hand. Your touch is truly special, [player]."
        elif moldable_variable == 5:
            m 5rub "Being here with you, feeling your touch, it's like a dream come true. I'm so grateful for this moment with you."
        elif moldable_variable == 6:
            m 5tubla "Your touch is electric, [player]. I can feel the sparks flying between us."
    jump show_boop_screen
    return

#====EARS
label monika_earsbeta:
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
    else:
        $ moldable_variable = renpy.random.randint(1,5)
        if moldable_variable == 1:
            m 1hubsa "I could stay like this forever, [player]."
            m 1fubsa "Your touch is so comforting."
        elif moldable_variable == 2:
            m 1sua "It feels like we're the only ones here, [player]."
            m 1tua "I'm so grateful to have you by my side~"
        elif moldable_variable == 3:
            m 1dua "You have such a gentle touch, [player]."
            m 1dub "I feel so safe and loved when you're near."
        elif moldable_variable == 4:
            m 1eublb "I never knew how much I needed this, [player]."
            m 3hublb "Your touch is like a warm hug."
        elif moldable_variable == 5:
            m 1hua "Being with you like this is all I need, [player]."
            m 1hub "Your touch makes everything better."
    jump show_boop_screen
    return
    
#===========================================================================================
# EXTRAS
#===========================================================================================
define coin_sprites = ["sprite_coin.png","sprite_coin-n.png","coin_heads.png","coin_tails.png"]

label aff_log:
    show monika idle at t11
    if os.path.isfile(renpy.config.basedir + '/game/submods/ExtraPlus/submod_assets/Pictograms.ttf'):
        "Your affection with [m_name] is [extra_current_affection] {size=+5}{color=#FFFFFF}{font=[Pictograms_font]}7{/font}{/color}{/size}"
    else:
        "Your affection with [m_name] is [extra_current_affection]"
    window hide
    jump close_extraplus
    return

label coinflip:
    python:
        check_file_status(coin_sprites, '/game/submods/ExtraPlus/submod_assets/sprites')

    show monika 1hua at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
        moldable_variable = renpy.random.randint(1,2)
    show screen extra_no_click
    pause 1.0
    show monika 3eua at t11
    show coin_moni zorder 12 at rotatecoin:
        xalign 0.5
        yalign 0.5
    play sound "submods/ExtraPlus/submod_assets/sfx/coin_flip_sfx.ogg"
    pause 1.0
    hide coin_moni
    show monika 1eua
    pause 0.5
    hide screen extra_no_click
    if moldable_variable == 1:
        show coin_heads zorder 12:
            xalign 0.9
            yalign 0.5
        m 1sub "The coin came up heads!"
        hide coin_heads
    elif moldable_variable == 2:
        show coin_tails zorder 12:
            xalign 0.9
            yalign 0.5
        m 1wub "The coin came up tails!"
        hide coin_tails
    m 3hua "I hope it helps you~"
    window hide
    python:
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
    jump close_extraplus
    return

label mas_backup:
    show monika 1hua at t11
    m 1hub "I'm glad you want to make a backup!"
    m 3eub "I'll open the route for you."
    m 1dsa "Wait a moment.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    window hide
    python:
        import os, sys, subprocess
        #Monika will open the mod data folder
        try:
            if sys.platform == "win32":
                os.startfile(renpy.config.savedir)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, renpy.config.savedir])
        except:
            renpy.jump("mas_backup_fail")
    jump close_extraplus
    return

label mas_backup_fail:
    m 1lkb "Sorry, I could not open the folder."
    m 1eka "Please try again later."
    jump close_extraplus
    return

label extra_window_title:
    show monika idle at t21
    python:
        window_menu = [
            ("Change the window's title", 'extra_change_title'),
            ("Restore the window title", 'extra_restore_title')
        ]

        items = [
            ("Nevermind", 'plus_tools', 20)
        ]
    call screen extra_gen_list(window_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
    
label extra_change_title:
    show monika idle at t11
    python:
        player_input = mas_input(
            prompt =("What title do you want to put on this window?"),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?()~-_.0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"})

        if not player_input:
            renpy.jump("extra_change_title")

        elif player_input == "cancel":
            renpy.jump("extra_window_title")

        else:
            persistent.save_window_title = player_input
            config.window_title = persistent.save_window_title 
            renpy.notify("The change is done.")
            renpy.jump("close_extraplus")
    return

label extra_restore_title:
    show monika idle at t11
    python:
        persistent.save_window_title = backup_window_title
        config.window_title = persistent.save_window_title 
        renpy.notify("It has been successfully restored.")
        renpy.jump("close_extraplus")
    return

label github_submod:
    show monika idle at t11
    $ renpy.run(OpenURL("https://github.com/zer0fixer/MAS-Extraplus"))
    jump close_extraplus
    return

#====GAME
label extra_dev_mode:
    if not os.path.exists(renpy.config.basedir + "/game/submods/ExtraPlus/submod_assets/sprites/"):
        jump close_extraplus

    $ mas_RaiseShield_dlg()
    call screen sticker_customization
    return
