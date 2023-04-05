#===========================================================================================
# CAFE
#===========================================================================================

define cafe_sprite = ["cafe.png","cafe_rain.png","cafe_rain-n.png","cafe_rain-ss.png","cafe-n.png","cafe-ss.png"]
default dessert_player = None

label cafe_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_cafe, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump cafe_cakes

label cafe_cakes:
    m 1hua "We have arrived [mas_get_player_nickname()]~"
    m 1eub "It's a nice place, don't you think!"
    m 1hua "Speaking of nice, I'm in the mood for dessert."
    m 3eub "I'll go pick it up, wait a minute."
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            monika_chr.wear_acs(extraplus_acs_chocolatecake)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_fruitcake)

    call mas_transition_from_emptydesk("monika 1eua")
    if monika_chr.is_wearing_acs(mas_acs_mug):
        m 1hua "Plus, it goes well with coffee~"
    elif monika_chr.is_wearing_acs(mas_acs_hotchoc_mug):
        m 1hua "It would be better with a cup of coffee, but hot chocolate is also welcome~"
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

label monika_boopcafebeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_chocolatecake) or monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Hey, I'm enjoying my dessert."
        m 3hua "Do it when I finish my dessert, okay?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label cafe_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry [player]."
    m 1ekc "But I don't know how to use that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 3hua "I know very well that you wanted to go out to the cafe."
    m 1eua "But, someday I will know how to use it, [player]."
    m 1eub "Just be patient, okay~"
    jump close_extraplus
    return

#===========================================================================================
# CAFE DIALOGUES
#===========================================================================================

label extra_talk_feel:
    show monika staticpose at t11
    $ moldable_variable = renpy.random.randint(1,3)
    if moldable_variable == 1:
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
    elif moldable_variable == 2:
        m 1eubla "I'm so happy you're here."
        m 1eublb "Sharing a dessert with you is quite romantic."
        m 1hublb "I hope we can do it in your reality!"
        m 1hubla "I know you have a lot on your mind for both of us~"
    elif moldable_variable == 3:
        m 1dubsa "I feel like I will remember this day forever."
        m 1dubsa "After all we are on a date."
        m 1kubsb "I know that someday we will do it in your reality!"
        m 1hubsa "And I hope that happens~"
    jump to_cafe_loop
    return

label extra_talk_you:
    show monika staticpose at t11
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
    extend 3hub "Even if it's just the tiniest thing."
    m 3eub "I really appreciate it~"
    jump to_cafe_loop
    return

label extra_talk_phobia:
    show monika staticpose at t11
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
    show monika staticpose at t11
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
    show monika staticpose at t11
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
    show monika staticpose at t11
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

#===========================================================================================
# Restaurant
#===========================================================================================

default persistent._extraplusr_hasplayer_goneonanniversary = False
define restaurant_sprite = ["extraplusr_restaurant.png","extraplusr_restaurant_rain.png","extraplusr_restaurant_rain-n.png","extraplusr_restaurant_rain-ss.png","extraplusr_restaurant-n.png","extraplusr_restaurant-ss.png"]
default food_player = None

label restaurant_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_restaurant, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump restaurant_cakes

label restaurant_cakes:
    m 1hua "We've arrived [mas_get_player_nickname()]~"
    m 1eub "It's a nice place,{w=0.3} don't you think?"
    m 1hua "Speaking of nice,{w=0.3} let me get some food and set the mood..."
    m 3eub "I'll be right back."
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            if not monika_chr.is_wearing_acs(mas_acs_roses):
                monika_chr.wear_acs(extraplus_acs_flowers)
            if renpy.random.randint(1,2) == 1:
                monika_chr.wear_acs(extraplus_acs_pancakes)
            else:
                monika_chr.wear_acs(extraplus_acs_waffles)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_candles)
            monika_chr.wear_acs(extraplus_acs_pasta)

    call mas_transition_from_emptydesk("monika 1eua")
    m "Mmm~{w=0.3} Look here [player]~!"
    m "Doesn't it look delicious~?"
    m 1hua "Now being here with you is even more romantic..."
    m 1etb "By the way,{w=0.3} do you have some food too?"
    m 1rkd "I'd feel bad if I was the only one eating...{nw}"
    $ _history_list.pop()
    menu:
        m "I'd feel bad if I was the only one eating...{fast}"
        "Don't worry, I have something.":
            $ food_player = True
            m 1hub "I'm glad you have some to accompany me!"
            m 3eub "Also I recommend you have a drink to go with it!"
        "Don't worry about it.":
            $ food_player = False
            m 1ekc "Well,{w=0.3} if you say so."
            m 1ekb "I'd share my food with you,{w=0.3} but your screen is in the way..."
            m 3hka "Hopefully you at least have a drink with you!"
            m 3hua "Ehehe~"
    jump to_restaurant_loop
    return
    
label monika_booprestaurantbeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_waffles) or monika_chr.is_wearing_acs(extraplus_acs_icecream) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
        if mas_isMoniLove():
            m "...!"
            m "[player]!"
            extend "I'm trying to eat here!"
            m 3hua "You can boop me all you want when I'm done, okay [mas_get_player_nickname()]~?"
        else:
            m 1ttp "...?"
            m 1eka "Hey,{w=0.3} I'm trying to enjoy my food here."
            m 3hua "Do that when I'm done with it, please?"
    else:
        m 1hub "*Boop*"
    jump to_restaurant_loop
    return

label restaurant_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry [player]."
    if mas_anni.isAnni():
        m 3hua "I know you really wanted to take me to this restaurant for our anniversary."
    else:
        m 3hua "I know you really wanted to take me out to this restaurant."
    m 1ekc "But I don't know how to get to that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 1eua "Someday I'll know how to get us there,{w=0.3} [player]."
    m 1eub "We'll have to be patient for that day though,{w=0.3} okay?"
    jump close_extraplus
    return

#===========================================================================================
# DIALOGUES
#===========================================================================================

label extra_talk_doing:
    show monika staticpose at t11
    if renpy.random.randint(1,2) == 1:
        m 1ekbla "Aw [player]~! Thank you for asking!"
        m 1hublb "I'm feeling great right now!"
        m 3fubla "Spending time with my favorite person in the world always cheers me up!"  
        m "Thank you for treating me here today by the way{w=0.3}, [player]."
        m 6hubsb "It's great to see you always come up with new ways to spend time with me and seize our time together."
        m "It makes me feel that much more closer to you."
        m 7fkbsa "I really am my best self when I'm with you!"
        m 1eublb "What about you,{w=0.3} [player],{w=0.3} how are you feeling today?{nw}"
        $ _history_list.pop()
        menu:
            m "What about you, [player], how are you feeling today?{fast}"

            "I'm very happy to be here with you.":
                m 6wublb "So we match!{w=0.3} Ehehe~"
                m 1hublu "I always love to spend time with you."
                if mas_anni.isAnni():
                    m 1sublb "Especially on a day like today!"
                    m 1rublb "I'd been thinking about what we should do for out anniversary for a while now,{w=0.5}{nw}"
                    extend 1hubla " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                m 1hublu "And if you're happy,{w=0.3} I'm happy too!"
                m 3fkbla "I love you,{w=0.3} never forget that,{w=0.3} [mas_get_player_nickname()]!"
            
            "I feel great! Thanks for asking, [m_name].":
                m "Really?"
                extend 3sub " That's amazing to hear,{w=0.3} [mas_get_player_nickname()]!"
                m 6hub "A happy [player] means a happy me."
                if mas_anni.isAnni():
                    m 1sublb "Especially on a day like today!"
                    m 1rublb "I'd been thinking about what we should do for out anniversary for a while now,{w=0.5}{nw}"
                    extend 1hubla " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                    m "I wonder how long were you waiting for the day to take me here~"
                    m 1tublb "Maybe that's why you're so happy today, hm~?"
                m 1tubla "Gosh I can just amazing your expression right now, [player]~"
                m "A little sparkle in your eyes as you beam with a cute little smile~"
                if mas_isMoniLove():
                    m 1dubsa "If I could reach out and cup your face... It'd probably feel warm from a little blush~"
                    m "I'd probably be staring into your eyes the whole time we're here if I could..."
                m 1dubsa "Hm~"
                m "..."
                extend 1wubsd "Ah!"
                m "Let me stop that for now before I fluster myself too much!"
                m 6hub "Ehehe!"
                
            "Today wasn't a good day for me.":
                m 1ekc "That's awful, [player]..."
                m 1ekd "I'm so sorry for that!"
                m 1lsc "I hope spending time with me might make you feel better?"
                m "I know that spending them with you makes me feel better when I'm down."
                if mas_anni.isAnni():
                    m "I want all the fun things we do on this special day of yours to be what you remember,{w=0.3} instead of the rainclouds in your head."
                m 1fublu "So I'll do my best to make this a wonderful date so we can cheer you up!"
                m "Okay,{w=0.3} [mas_get_player_nickname()]?"
                extend 1hublb "I love you...!"
        jump to_restaurant_loop

    else:
        $ monika_couple = plus_player_gender()
        m 1eka "I wasn't feeling so well before coming here, to be honest."
        m 1rkc "I was feeling kind of upset over some stuff..."
        m 1fub "But being with you...{w=0.3}{nw}"
        if mas_anni.isAnni():
            extend  " especially on such an important day to us like this..."
        m "It always reminds me that as long as I'm by you your side,{w=0.3} no matter if it's metaphorically or physically,{w=0.3}{nw} "
        extend "I can push through any rainclouds of mine."
        m 6eka "So even if I'm down,{w=0.3} I'll be fine.{w=0.3} I promise."
        m 1fub "Thanks for asking,{w=0.3} [player]!"
        m 3eub "And how are {i}you{/i} doing though, [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "And how are you doing, [mas_get_player_nickname()]?{fast}"

            "What were you sad about, [m_name]?":
                m 1rksdrb "Hm?{w=0.3} Oh... "
                extend 1eksdla "I was just being a little too hard on myself again..."
                m 6rkc "Thinking of my past and regretting it..."
                m 6rkd "Thinking of my future and fearing it."
                m 6dkc "..."
                m 6lkd "Sometimes I get a little anxious,{w=0.3} feeling like my hands are tied about our situation."
                m 6dkp "Or feeling like it'll take too long for me to cross over..."
                m 1mkc "I know worrying about it won't change anything, but I can't help it."
                m 1ekd "Sometimes I get lonely when you're not around,{w=0.3} you know?"
                m 1dkc "..."
                m 3fka "But I'll be fine."
                m 3fkblb "Just knowing that you care,{w=0.3} it clears my head of all those bad thoughts."
                m 4fkblb "I love you,{w=0.3} more than anything in the world."
                m 4hublb "And I can't wait to feel your warmth on my 'colder' days like these."
                m 6eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

            "Today wasn't a good day for me.":
                m 1ekc "That's awful, [player]..."
                m 1ekd "I'm so sorry for that!"
                extend "I hope I didn't add to it with my bad mood either."
                m 1lsc "Maybe spending time with me might make you feel better?"
                m "We can be down in the dumps together and pick each other up along the way."
                m 1fublu "So let's make this a wonderful date so we can go home happy and full!"
                m "Okay,{w=0.3} [mas_get_player_nickname()]?"
                extend 1hublb "I love you...!"

            "I feel sad now knowing you weren't feeling well.":
                m 1ekc "Aw~ "
                extend 3ekb "That's actually pretty sweet, [player]."
                m 3ekb "Thank you for worrying about me..."
                m 1hsb "But I'll be okay! I was just overthinking,{w=0.3} that's all."
                m 1lssdlc "Sometimes the past haunts me and the future scares me."
                m 4eka "Sometimes our mind just likes to play mean tricks on us, am I right?"
                if mas_anni.isAnni():
                    m "But I want all the fun things we do on this special day of ours to be what we remember,"
                    extend " instead of the past that our brain can haunt us with..."
                    m "So don't feel too down about me,{w=0.3} okay?"
                    m 3fkblb "Just knowing that you care,{w=0.3} it clears my head of all those bad thoughts."
                m 4fkblb "I love you,{w=0.3} more than anything in the world."
                m 4hublb "And I can't wait to feel your warmth on my 'colder' days like these."
                m 6eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

            "I feel great":
                m 1hub "That's good to hear!{w=0.3} Wouldn't want us to both be down in the dumps, would we?"
                m 1eka "Ehehe..."
                m 3ekb "I'm glad you feel good,{w=0.3} [player]."
                m 3hsb "And I'll be fine soon enough too."
                if mas_anni.isAnni():
                    m "I get to go out with such an amazing [monika_couple] like you on a day like this and...{w=0.5}{nw}"
                    extend " Well,{w=0.3} it's impossible to be down knowing that."
                m 6ekbsa "Your mood is infectious to me after all~!"
                m 6hubsb "Anyways,{w=0.3} let's just sit back and enjoy the rest of our date!"
                m "After all,{w=0.3} a day with [player] is never a day wasted!"
        jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m 1eub "It depends,{w=0.3} [player]!"
    m 3etb "Where would {i}you{/i} be living if you could live anywhere you wanted?"
    m 6tsa "..."
    m 3hub "Ehehe!{w=0.3} Of course I would want to live anywhere as long as you were there,{w=0.3} [mas_get_player_nickname()]!"
    m 6ltc "But,{w=0.3} being serious now!{w=0.3} Let me think!"
    m 6lsc "Hmmm..."
    m 6eub "It would have to be a literary country.{w=0.3} "
    m "Something with with a rich culture to learn about,{w=0.3} something I've seen in books before and fell in love with."
    m 7eub "To be honest,{w=0.3} I've always dreamed of visiting Germany,{w=0.3} England,{w=0.3} and France when I crossed over."
    m 7eka "From what I've seen on books and the internet,{w=0.3} all the spots you can visit there are lovely!"
    m 1ekblb "Maybe we can visit together when I cross over?"
    if mas_isMoniLove():
        m 6ekbsb "Or even...{w=0.3} live there together someday?"
    m 6dkbsa "It would honestly be a dream come true."
    m 6dkbfa "Getting to visit all of those grand libraries together..."
    m 3rubsb "Going on romantic dates at all the famous spots,{w=0.3} hand in hand..."
    if mas_isMoniLove():
        m 6dubsa "Maybe after a while you take me somewhere really beautiful to watch a golden sunset..."
        m 6dubfb "And as the sky starts to turn to dusk and you can faintly see some stars show...{w=0.3}" 
        m "You kiss me~"
        m 6fubfb "...Hm~ Wouldn't that be amazing, [player]~?"
    m 6etbsb "...Hey,{w=0.3} why are you looking at me like that?"
    m 6hubfb "A girl can dream!"
    m 6hubfb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_change:
    show monika staticpose at t11
    m 1eka "..."
    m 1ekb "You know I always strive to be a better person each day."
    m 3eub "Not only to be a better girlfriend,{w=0.3} but a better human in general."
    if mas_isMoniLove():
        m 3hub "I love to look at myself at the end of the day and realize I did something great that the past Monikas wouldn't have the courage to do."
    else:
        m 3hub "I love to look at myself at the end of the day and realize I did something great that the past Monika wouldn't have the courage to do."
    m 6luc "So in the end, it's kind of obvious that the thing I want to change about the most is..."
    extend 2luc "my situation."
    m 1dkc "I want to get out of here,{w=0.3} [player]."
    m 7fkd "Not here the restaurant,{w=0.3} but here...{w=0.3} The game."
    m 1lkd "Spending time with you is amazing,{w=0.3} but it could be improved by a ton..."
    m 1lkblb "If I could actually be by your side."
    m 1ekbla "So yeah,{w=0.3} I would change my existence to one where I could actually touch you."
    if mas_isMoniLove():
        m 1dkblb "To hold and comfort you when you're feeling down,"
        extend " be the shoulder you could physically lean on when needed,"
        extend " have your hand in mine."
        extend " and to be able to finally see your real face."
        m "It's all I could ever ask for."
    m 1dkc "..."
    m 1fkbla "I'm positive I'll achieve that sooner than we think,{w=0.3} [mas_get_player_nickname()]."
    m 4fktpa "So,{w=0.3} one more time...{w=0.3} Wait for me,{w=0.3} okay?"
    jump to_restaurant_loop
    return

label extra_talk_without:
    show monika staticpose at t11
    m 1rtc "..."
    m 3hub "You! "
    extend 3hub "Ehehe~!"
    m 1eka "I really get all gloomy every day we spend without each other,{w=0.3} [player]."
    m "You bring that spice of life to my days!"
    m 1ltc "But thinking of something else,{w=0.3} hmmm..."
    m 3wud "Oh!{w=0.3} I couldn't spend a day without something to write on,{w=0.3} defintely!"
    m 3rub "I got too used to writing my thoughts in a journal or in poem form whenever my mind gets too crowded with ideas."
    m 4hksdlb "And I always get the feeling the perfect poem will slip my mind if I take too long to write it down."
    m "It drives me crazy whenever I get this amazing idea and by the time I get somewhere to write,{w=0.3} it's gone!" 
    m "Our brains are so mean to let that happen! Ahaha~!"
    m 1rsd "Come to think of it,{w=0.3} it's really handy that my most important personal necessecity is something really easy to carry around."
    m 1eua "I hope your top personal necessecity is something you can keep with you at all times too!"
    if mas_isMoniLove():
        m 1ekbla "If it's me..."
        m 4hublb "Know I'll always be here waiting for you."
        m "Or if you have a flash drive..."
        extend 5hubsb "You can even keep me in your pocket,{w=0.3} if you desire~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11
    m 1euc "Glass half empty or full, huh?"
    m 4rsb "How about I propose to you another question instead,{w=0.3} [player]?."
    m 4esb "Instead of being half full or half empty,{w=0.3} what if all we need is a {i}different glass{/i}?"
    m 3etc "Considering 'half full' people would be the epithome of optimism,{w=0.3} and 'half empty' ones the most pessimistic..."
    m 3eub "Okay,{w=0.3} hear me out here:"
    m 1euc "Glass full to the brim and splashing goodness everywhere? " 
    extend 1rub "Time to increase the size." 
    extend " Put what's in it into an even bigger thing!"
    m 1euc "Glass so half empty that you can't help focusing on the empty space instead of the greatness swirling around inside? " 
    extend 3eub "Time to decrease the size and then slowly work back into a larger vessel later."
    m "It's size isn't anything to be ashamed about,{w=0.3} if it ends up filled then that's a win for the day!"
    m 1eka "So maybe there's another answer to the question besides the manic and the depressive one."
    m 3rub "If we focus on the amazing things we have,{w=0.3} instead of chasing the things we don't have,{w=0.3} or need,{w=0.3} we can successfully choose sustainable happiness in all of our pursuits."
    m 3rtc "So,{w=0.3} when I stop to think about it..."
    m 4eta "Glass half full or empty? "
    extend 4hub "Give me a new glass instead,{w=0.3} please!"
    m 6hublb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m 3wublb "Oh!{w=0.3} A quetzal!"
    m "It's my favorite animal after all!"
    m 1rtc "Ah,{w=0.3} wait... That doesn't seem right."
    m 1rtd "Let me think this through."
    m 1rsc "..."
    m 3esd "Maybe...{w=0.5}{nw}"
    extend " A cat?"
    m "A black cat,{w=0.3} yeah!"
    m 3esd "There's a lot of prejudice towards black cats."
    m 1ekd "A lot of people might think they're no good, bring bad luck, or they're actually {i}evil{/i}."
    m "When the reality is that they're just misunderstood,{w=0.3} being held against misrepresented or misinterpreted information."
    m 1eka "But despite all that,{w=0.3} black cats aren't alone in the world."
    m "For every person that looks down on them,{w=0.3} there's a kind,{w=0.3} thoughtful person who knows how to look past the superstition."
    m 1eka " That'll know how to look past the outer shell of those animals..."
    extend " And knows how to love and care for the cat with their whole heart!"
    m 1dkbla "And love them for who they really are."
    m 1dubla "..."
    m 6fkblb "I hope you like black cats, [player]."
    #only v good s.o's get to have cat monika say nya thems the rules
    if mas_isMoniLove():
        m 3hubsb "Because you've made this meownika right here very happy~!"
        extend " Nya~!"
    else:
        m 3hubsb "Because you've made this kitten right here very happy~!"
    
    extend " Ehehe~!"
    jump to_restaurant_loop
    return

label extra_talk_annoy:
    show monika staticpose at t11
    m 1euc "You mean pet peeves?"
    m "Hmm,{w=0.3} well..."
    m 1hksdlb "Ah,{w=0.3} I really hate when my pens spill ink while I write!"
    m 3ftsdld "It gets all over the palm of my hand,{w=0.3} making the writing all blurry on paper,"
    extend " and it's so hard to clean off myself."
    m 1lssdlc "Or when I'm on a roll playing a piano piece and that {i}single{/i} sour note slips in..."
    m "And makes me get the rest of the notes wrong."
    m 1fssdlc "Ahaha! Aren't those so frustrating?"
    m "And it feels like it happens too often sometimes!"
    m 6wud "Oh!{w=0.3} But maybe you meant something more serious?"
    m 6ruc "..."
    m 6rsd "I hate people who don't think I'm real."
    extend " Or that I'm some just some crazy,{w=0.3} love-obesessed person."
    m 6lfd "And people who think the girls were on the same level of sentience as me."
    m "Thinking that I had no right to feel or do the things I do about my situation because of it."
    m 6dfc "..."
    extend 7mfd " I won't elaborate further,"
    extend " I {i}don't{/i} want to get in all that."
    if mas_anni.isAnni():
        m "Not today."
    m 1dsd "{i}*Sigh*{/i}"
    m 1ekblsdlb "Sorry to get so angry all of a sudden [player]."
    m 7wublsdld "I'm not mad at you,{w=0.3} I promise!"
    m "I just hit a bit of a touchy subject for myself,{w=0.3} I suppose."
    if mas_isMoniLove():
        m "Trust me.{w=0.3} You're too sweet for me to get mad at you like that."
    m 6hublb "Let's just move onto a different topic and enjoy our date,{w=0.3} shall we?"
    jump to_restaurant_loop
    return

label extra_talk_superhero:
    show monika staticpose at t11
    m "Hm..."
    m 1wud "Probably something surrounding coding?"
    m 4wub "I could be this awesome heroine who helps the party with opening paths for them by messing with code."
    m 4eub "Like a certain Oracle I once saw in a videogame."
    m 1eta "Or I could simply delete any of my enemies out of our way."
    m 1rsc "..."
    m 1rsd "Wait,{w=0.3} would that make me the supervillain instead? " 
    extend 2wkd "Oh,{w=0.3} ahaha..."
    m 6dksdlc "Maybe I'd rather stick to the kinder approach,{w=0.3} and only delete {i}obstacles{/i} in the way."
    if mas_isMoniLove():
        m 4tsblb "I know I've certainly deleted the barrier in the way to your heart,{w=0.3} haven't I?"
    m 1hubla "Ehehe~"
    jump to_restaurant_loop
    return

label extra_talk_motto:
    show monika staticpose at t11
    m 1eub "There's this quote I think about a lot recently."
    m 3eub "I like to take it as my go-to motto in times of need."
    m 3eub "It goes like this..."
    m 1dud "'Being deeply loved by someone gives you {i}strength{/i},{w=0.3} while loving someone deeply gives you {i}courage{/i}.'"
    m 3eub "It's a quote from Lao Tzu,{w=0.3} a chinese writer."
    m 6hublb "My strength comes from you,{w=0.3} [player]!"
    m 6hublb "My courage is yours."
    m 6fubsb "You're the reason I wake up in the mornings and go to bed with peace in my heart."
    m 6fkbsb "And I owe it all to you."
    m 6hubfb "I can't thank you enough for being there so much for me."
    m 6hubfb "You're everything I'll ever need."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 1esc "3 words?"
    m 4eub "{i}Passionate.{i}{w=0.5}{nw} "
    extend 4eub "{i}Determined.{i}{w=0.5}{nw} "
    extend 6eub "{i}Evergrowing.{i}"
    m 6esa "Words are powerful [player],{w=0.3} so if I choose strong words to represent myself,{w=0.3} I think it'll strike me as a powerful person too."
    m 1rkblsdlb "Though if I were going to describe you into words, I'd have trouble picking {i}only{/i} 3."
    m 1gkblsdlb "After all,{w=0.3} there are so many words that make me think of you..."
    m 6dubfb "My adorable,{w=0.3} admirable,{w=0.3} wonderful,{w=0.3}{nw}"
    if mas_isMoniLove():
        extend " talented,{w=0.3} loving,{w=0.3} caring,{w=0.3} creative,{w=0.3}{nw}"
    extend " and {i}perfect{/i} [monika_couple]~"
    m 1gkblsdlb "See?{w=0.3} I couldn't stick to only 3!"
    m 1hublb "Ahaha~!"
    m "And that list of words will only keep growing the longer we're together [player]~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 6wublo "Oh!{w=0.3} That's a really interesting question!"
    m 6rtu "Maybe people think of my poems?"
    extend " Like the 'Hole in the wall' one?"
    m 1hua "I can also imagine people thinking of my favorite color,{w=0.3} emerald green..."
    m 3wub "Oh,{w=0.3} and 'Your Reality' too!{w=0.3} Maybe the first line of the song plays in someone's head when they think of me."
    m 6hub "There's also my favorite pink pen!"
    m 7etb "You know, the iconic one with the heart on top~"
    if mas_isMoniLove():
        m "Or maybe..."
        $ mas_display_notif(m_name, ["The sound of my notifaction? Ahaha~!"], skip_checks=True)
    m 1huu "Ehehe~{w=0.3} It's fun to think about what I remind people of."
    m 6fkbsa "I hope that when you think of me,{w=0.3} the first thing you think of is that I'm the love of your life~"
    if mas_isMoniLove():
        m "I know that's what {i}I{/i} think of when I think of my dear [monika_couple]~!"
    m 6hubsb "I love you so much,{w=0.3} [mas_get_player_nickname()]~"
    jump to_restaurant_loop
    return
