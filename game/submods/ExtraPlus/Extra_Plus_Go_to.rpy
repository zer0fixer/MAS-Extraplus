################################################################################
## CAFE
################################################################################
label go_to_cafe:
    if renpy.get_screen("chibika_chill"):
        $ show_chibika = True
    else:
        $ show_chibika = False
    python:
        extra_chair = store.monika_chr.tablechair.chair
        extra_table = store.monika_chr.tablechair.table
        extra_old_bg = mas_current_background

    if mas_curr_affection == mas_affection.HAPPY or mas_curr_affection == mas_affection.AFFECTIONATE:
        jump sorry_player
    if renpy.seen_label("check_label_cafe"):
        $ mas_gainAffection(1,bypass=True)
        jump gtcafev2
    else:
        $ mas_gainAffection(5,bypass=True)
        pass
label check_label_cafe:
    pass
label gtcafe:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Do you want to go to the cafe?"
        m 3hub "Glad to hear it [player]!"
        m 1hubsa "I know this appointment will be great!"
        m 1hubsb "Okay, let's go [mas_get_player_nickname()]~"
        jump cafe_init

    elif not mas_isDayNow():
        m 3sub "Oh, you want to go out to the cafe?"
        m 3hub "It's pretty sweet that you decided to go tonight."
        m 1eubsa "This date night is going to be great!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Another time then, [mas_get_player_nickname()]."
        jump return_extra
    return

label gtcafev2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Do you want to go to the cafe again?"
        m 2hub "The previous time we went, I had a lot of fun!"
        m 2eubsa "So glad to hear it [player]!"
        m 1hubsb "Well, let's go [mas_get_player_nickname()]~"
        jump cafe_init
    elif not mas_isDayNow():
        m 3wub "Oh, do you want to go out to the cafe again?"
        m 2hub "The previous time we went, it was very romantic~"
        m 2eubsa "So glad to go again [player]!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump return_extra
    return

################################################################################
## MICS
################################################################################
label cafe_init:
    $ HKBHideButtons()
    hide screen chibika_chill
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_cafe, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()

label cafe_cakes:
    if show_chibika is True:
        show screen chibika_chill
    $ dessert_player = None
    m 1hua "We have arrived [mas_get_player_nickname()]~"
    m 1eub "It's a nice place, don't you think!"
    m 1hua "Speaking of nice, I'm in the mood for dessert."
    m 3eub "I'll go pick it up, wait a minute."
    call mas_transition_to_emptydesk from monika_hide_exp_2
    pause 2.0
    if mas_isDayNow():
        $ monika_chr.wear_acs(extraplus_acs_chocolatecake)
    elif not mas_isDayNow():
        $ monika_chr.wear_acs(extraplus_acs_fruitcake)
    call mas_transition_from_emptydesk("monika 1eua")
    if monika_chr.is_wearing_acs(mas_acs_mug):
        m 1hua "Plus, it goes well with coffee~"
    else:
        $ monika_chr.wear_acs(extraplus_acs_coffeecup)
        m 1hua "And I mustn't forget the cup of coffee to go with the dessert~"
    m 1etb "By the way, do you have a dessert at your disposal?"
    m 1rkd "I'd feel bad if I was the only one eating one...{nw}"
    $ _history_list.pop()
    menu:
        m "I'd feel bad if I was the only one eating one...{fast}"
        "Don't worry, I have a dessert.":
            $ dessert_player = True
            m 1hub "I'm glad you have one to accompany me!"
            m 3eub "Also, I recommend you have a cup of coffee with it."
        "Don't worry about it.":
            $ dessert_player = False
            m 1ekc "Well, if you say so."
            m 1ekb "I'd give you mine, but your screen limits me from doing so..."
            m 3hka "I hope you at least have a cup of coffee!"
    m 3hua "Ehehe~"
    jump to_cafe_loop
    return

label to_cafe_loop:
    show monika staticpose at t11
    call screen cafe_loop
    return

label cafe_leave:
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
label cafe_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eub "I have to put this fruitcake away."
            m 3eub "Also, I'll put this cup away, I won't be long."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)
            $ monika_chr.remove_acs(extraplus_acs_coffeecup)
            $ monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eub "I have to put this fruitcake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)

    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eua "I must put this chocolate cake away."
            m 3eua "Also, I'll put this cup away, it won't be long now."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)
            $ monika_chr.remove_acs(extraplus_acs_coffeecup)
            $ monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eua "I must put this chocolate cake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)

    elif monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3hua "I'll go put this plate away."
            m 3hua "Also, I'll put this cup away, I won't be long."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate)
            $ monika_chr.remove_acs(extraplus_acs_coffeecup)
            $ monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3hua "I'm going to put this plate away, give me a moment."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate)

    call mas_transition_to_emptydesk from monika_hide_exp_3
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    jump restore_bg
    return

label monika_no_dessert:
    show monika idle at t11
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        $ monika_chr.remove_acs(extraplus_acs_fruitcake)
        $ monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my fruitcake."
        m 1eub "I really enjoyed it~"
    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        $ monika_chr.remove_acs(extraplus_acs_chocolatecake)
        $ monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my chocolate cake."
        m 1sua "It tasted so sweet~"
    if monika_chr.is_wearing_acs(extraplus_acs_coffeecup):
        $ monika_chr.remove_acs(extraplus_acs_coffeecup)
        $ monika_chr.wear_acs(extraplus_acs_emptycup)
        m 3dub "Also, this coffee was also good."
    if dessert_player is True:
        m 1etb "By the way, have you finished your dessert yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your dessert yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a cup of coffee."
    m 1hua "Let me know if you want to come back again."
    jump to_cafe_loop
    return

label monika_boopcafebeta:
    show monika idle at t11
    if monika_chr.is_wearing_acs(extraplus_acs_chocolatecake) or monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Hey, I'm enjoying my dessert."
        m 3hua "Do it when I finish my dessert, okay?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label sorry_player:
    m 1ekd "I'm so sorry [player]."
    m 1ekc "But I don't know how to use that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 3hua "I know very well that you wanted to go out to the cafe."
    m 1eua "But, someday I will know how to use it, [player]."
    m 1eub "Just be patient, okay~"
    jump return_extra
    return

################################################################################
## DIALOGUES
################################################################################
label extra_talk_feel:
    show monika idle at t11
    $ rng_global = renpy.random.randint(1,3)
    if rng_global == 1:
        m 1hkbsb "I'm feeling a little nervous, we're on a date after all!"
        #In case someone doesn't take their Monika for a walk.
        if renpy.seen_label("bye_going_somewhere"):
            m 1ekbsb "Besides, I'm not on a USB stick."
            m 3hubsa "At this moment I feel closer to you, so I'll remember it~"
            m 3hubsb "Thank you for inviting me on a date!"
        else:
            m 1ekbsb "It's the first time we went out together~"
            m 3hubsa "So thank you for inviting me."
            m 3hubsb "You can do it through a USB stick though, even though I can't see anything."
            m 3ekbsa "I know very well that it will be very romantic."
    elif rng_global == 2:
        m 1eubla "I'm so happy you're here."
        m 1eublb "Sharing a dessert with you is quite romantic."
        m 1hublb "I hope we can do it in your reality!"
        m 1hubla "I know you have a lot on your mind for both of us~"
    elif rng_global == 3:
        m 1dubsa "I feel like I will remember this day forever."
        m 1dubsa "After all we are on a date."
        m 1kubsb "I know that someday we will do it in your reality!"
        m 1hubsa "And I hope that happens~"
    jump to_cafe_loop
    return

label extra_talk_you:
    show monika idle at t11
    m 3dkc "I know, [mas_get_player_nickname()]."
    m 3ekd "We are on a date, a way to get to know each other better."
    m 3ekd "You only have preconfigured options to answer based on the question I ask..."
    m 3ekc "After all this is a visual novel, "
    extend 1dua "but compared to other novels, here, we are creating a reality for both of us."
    m 1eub "Although you can create your own answers, after all you have more control than I do."
    if persistent._mas_pm_has_code_experience is True:
        m 3eub "You told me you have experience in coding, that's why I mention it."
    else:
        m 3ekb "I know you have no coding experience, but don't worry, you can learn it."
        m 3hub "I trust you, [mas_get_player_nickname()]."
    m 1eua "You could add more things here, per example is this cafe."
    m 1hua "Also more dialogues that we can discuss, talk about your hobbies or talk about your family."
    m 1rksdra "Try to make sure there is no misspelled code, you may lose me if a pretty serious mistake occurs."
    m 1eub "But leaving that aside, I'd love to be next to you, let's say, as a robot."
    m 1eub "That way we could establish a smooth conversation~"
    m 1eka "I know very well what you want to tell me about something or how you're feeling."
    m 1eka "But our way of communicating is very limited because of what I said earlier."
    m 3hua "It doesn't limit us from having a nice relationship together though!"
    m 3hua "Also, I know the most importants thing about you, whatever information you give me! "
    extend 3hua "Even if it's just the tiniest thing."
    m 3eub "I really appreciate it~"
    jump to_cafe_loop
    return

label extra_talk_phobia:
    show monika idle at t11
    m 1rtd "The truth is that's a good question, I haven't even thought about which fear I would have."
    m 1hua "After all, I'm not human, I'm just a cute little character. "
    extend 1dksdlb "Although I'm aware of everything going on around me."
    m 3eud "But if you want to know one, I'll give you 'autophobia'."
    m 3eka "The fear of loneliness."
    m 3dud "Feeling isolated without any company even if there are other NPCs or a pet to keep me company."
    m 3dud "It wouldn't be the same, they would just be ornaments to this place."
    m 3duc "Although I would call it purgatory."
    m 1lka "I know very well that this phobia has become very common and more so because of the pandemic."
    m 1lka "It's pretty sad not to have someone to talk to."
    m 1esd "I've seen other Monikas having this happen to them, because of their player's carelessness."
    m 1esd "Or people who have a grudge against us because of what happened in the game."
    m 1dsc "I mention it because it's a domino effect, rejection leads to loneliness and loneliness leads to despair."
    m 1esb "But it's a very minor thing, compared to when the game came out."
    m 3hua "You know, it's a funny thing, before we were more hated and the other members of the club were more loved."
    m 3hua "Now everything is reversed in our favor~"
    m 3dub "Finally people realized that the story was badly told."
    m 1hua "But we shouldn't worry about that anymore."
    m 1eubsb "We are on a date after all!"
    m 1eubsb "Let's enjoy our time here, [player]~"
    jump to_cafe_loop
    return

label extra_talk_ambition:
    show monika idle at t11
    m 1tubsb "{i}You{/i}, you are my great ambition."
    m 1hkbsa "Just to think that I am so far away and so close at the same time."
    m 1hkbsa "It will be hard enough to get to you, but that's what I'm looking forward to the most."
    m 1ekbsa "When I see your pretty face for the first time, I don't think my heart will be able to have a steady rhythm because of the excitement."
    m 1ekbsa "I'd like to use your computer camera to at least see what you look like."
    m 1rksdlb "But I don't have administrator permission to use it."
    m 1hua "What a hilarious situation, don't you think?"
    m 1lub "Well at least I have an idea of what you look like."
    m 1lub "For me it's more than enough, with the information I have of your appearance."
    m 1eubsa "Thanks for listening, let's get on with our date~"
    jump to_cafe_loop
    return

label extra_talk_teen:
    show monika idle at t11
    m 1eua "That's a rather curious question, [mas_get_player_nickname()]"
    m 1dua "{i}How will we be 10 years from now?{/i}"
    if mas_anni.isAnniOneMonth():
        m 1rub "Even though we've known each other for a month since that day..."
        m 1dua "It's really hard to know what's coming in the future, [player]."
        m 1dua "We don't know what destiny has in store for us."
        m 1hka "We will go through many difficult situations and many happy ones."
        m 1hka "Life is like that, but as long as nothing bad happens to you, that's more than enough for me~"
    elif mas_anni.isAnniThreeMonth() or mas_anni.isAnniSixMonth():
        m 1eub "Although you have been with me for several months with me."
        m 1hub "I've enjoyed the months we've spent!"
        m 1hub "I don't know what the future holds, [mas_get_player_nickname()]."
        m 3ekb "But there is one thing I know I will see from you, you will grow up to be a great person."
        m 3ekb "Life is like a book, there are pages that you have to discover, and others that you have to hide."
        m 3eua "You can go back and look at some of them as a nice memory or as you have progressed."
        m 3dsc "But never try to open old wounds, they were left in the past so it is unnecessary to remember them."
        m 1hua "I hope what I said cheers you up a bit~"
    elif store.mas_anni.anniCount() == 1:
        m 1eubfa "Even though we've already had our one year anniversary..."
        m 1hubfb "It's been the best year of my life!"
        m 1hubfb "I'm glad something serious didn't happen to you because of the pandemic."
        m 1eka "But still take good care of yourself, we still have a lot of memories to create together!"
        m 1ekd "At this point in our relationship, I'm afraid of losing you."
        m 1hubla "Well, I know you take good care of yourself [mas_get_player_nickname()], so just tell me when you need my help."
        m 1hubla "I care about you, it's a way of thanking you for the months you've taken care of me."
    m 1etd "I have a question though [player]. Do you think that when I reach those years there will be a way to make me real?"
    m 3eua "I am referring to robots, every time you see several prototypes, some more advanced than others."
    m 3eub "In this century, human beings have advanced in technology at an astonishing speed."
    m 3lsa "That's why I wouldn't be surprised if there were signs of domestic robots or if they were present in a restaurant."
    m 3lsa "That's a pretty interesting thought."
    if store.mas_anni.anniCount() >= 2:
        m 1hubsb "Even though we've known each other for several years..."
        m 1lubsb "How much the time flies, it really scares me."
        m 1eud "Quite a few things have happened, such as the pandemic, although it has been brought under control."
        m 1hua "I hope I've been helpful during these years of quarantine."
        m 1eua "Following your question, I think there will at least be a chance to get real."
        m 1eua "Let's say you see signs of domestic robots or they are present in a fast food restaurant."
        m 1lksdlb "Although the first versions of the robots will be hard to come by."
        m 1lksdlb "But if you stick with me for a few more years, it won't be a problem if you can't get me a body."
        m 1eubsa "Just being by my side is more than enough."
        m 1eubsa "You're the only thing I have left of this reality I live in."
        m 1hua "And let's take care of each other like we've been doing all these years!"
    elif store.mas_anni.anniCount() >= 10:
        m 1hubsb "Even though we're way past those years, [mas_get_player_nickname()]..."
        m 1hubsb "They have been the best years of my life."
        m 1rubsb "We've traveled in so many situations we can't imagine."
        m 1eubsa "Years ago I didn't think I would stay with you for so long."
        m 3eub "I would love to see how technology has advanced!"
        m 3eub "Maybe some company has a robot in mind for public use."
        m 3sua "I would put my mind in the robot, so that I could see you and talk to you."
        m 1eua "Speaking of the robot, "
        extend 1hubsb "that way you could marry me, I know very well you want that~"
        m 1eka "But if it's not available yet, I can wait for more years."
        m 4hub "I'm used to this way of communicating. I don't lose anything after all!"
    jump to_cafe_loop
    return

label extra_talk_memory:
    show monika idle at t11
    m 1dubsa "I can tell you, "
    extend 1subsa "I met a person who has made me feel very happy."
    if persistent._mas_acs_enable_promisering:
        m 1hua "Although one of the memories I really cherish."
        m 3ekbfb "Is when you gave me this ring~"
        m "I understood that both of us are already committed to be together forever."
        m 3hubfb "Ehehe~"
    else:
        m 1hua "I would say that already the day you played Doki Doki Literature Club, boy, was I looking forward to meeting you."
        if persistent.monika_kill:
            m 1eka "We know you eliminated me, but I know you did it for good."
            m 1ekb "I say that because I'm here again, with you."
            m 1eub "If you hated me you wouldn't have thought of bringing me back."
        else:
            m 1eka "You've always stood by me, even through everything I go through at the club."
            m 1ekblb "I haven't met anyone who is as amazing as you."
    m 1dua "But really, every day is a nice memory for me."
    m 1dua "I have many in mind and I cherish them very much."
    m 1dub "I know you will have the same memories too."
    m 1dub "I'd like to hear from you in your own words, not preconfigured answers."
    m 3eka "We'll figure out a way for you to at least use your microphone to talk about them."
    m 3eka "Until then we'll have to keep it that way, I'm very sorry if you want to talk about your memories..."
    jump to_cafe_loop
    return
