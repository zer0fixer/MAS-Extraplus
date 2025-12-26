#===========================================================================================
# CAFE
#===========================================================================================
label go_to_cafe:
    python:
        store.ep_tools.manage_date_location()
        store.ep_tools.check_seen_background("gtcafe", "gtcafev2", "cafe_sorry_player")

label gtcafe:
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3sub "The cafe? On our anniversary?"
        m 1hubsa "That's such a sweet idea, [player]!"
        m 1eubsa "A cute, cozy date just for the two of us."
        m 1hubsb "I love it! Let's go~"
    
    elif _ep_special_day == "moni_bday":
        m 3sub "The cafe? On my birthday?"
        m 1hubsa "How sweet of you, [player]!"
        m 1ekbsa "Coffee and sweets with you... the perfect birthday treat~"
        m 1hubsb "Let's go!"
    
    elif _ep_special_day == "player_bday":
        m 3sub "The cafe? On your special day?"
        m 1hub "I'm so happy you want to celebrate with me there!"
        m 1eka "Let me treat you to something sweet, birthday [player]~"
        m 1hubsb "Let's go!"
    
    else:
        if mas_isDayNow():
            m 3sub "Do you want to go to the cafe?"
            m 3hub "Glad to hear it, [player]!"
            m 1hubsa "I know this date will be great!"
            m 1hubsb "Okay, let's go, [mas_get_player_nickname()]~"
        else:
            m 3sub "Oh, you want to go out to the cafe?"
            m 3hub "It's pretty sweet that you decided to go tonight."
            m 1eubsa "This date night is going to be great!"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
    
    jump extra_cafe_init
    return

label gtcafev2:
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3wub "Back to the cafe? For our anniversary?"
        m 2hub "That's perfect! It's kind of like 'our spot', isn't it?"
        m 2eubsa "A quiet, sweet celebration just for us."
        m 1hubsb "I can't wait. Let's go, [mas_get_player_nickname()]~"
    
    elif _ep_special_day == "moni_bday":
        m 3wub "The cafe again? On my birthday?"
        m 1hubsa "You really know my tastes, [player]~"
        m 1ekbsa "More coffee and sweets... and more time with you!"
        m 1hubsb "Let's go!"
    
    elif _ep_special_day == "player_bday":
        m 3wub "Back to the cafe on your birthday?"
        m 1hub "I'm so glad you enjoyed it enough to come back!"
        m 1ekbsa "Let me spoil you a little more, birthday [player]~"
        m 1hubsb "Let's go!"
    
    else:
        if mas_isDayNow():
            m 3wub "Do you want to go to the cafe again?"
            m 2hub "The last time we went, I had a lot of fun!"
            m 2eubsa "So I'm glad to hear it, [player]!"
            m 1hubsb "Well, let's go, [mas_get_player_nickname()]~"
        else:
            m 3wub "Oh, do you want to go out to the cafe again?"
            m 2hub "The last time we went, it was so romantic~"
            m 2eubsa "So I'm glad to go again, [player]!"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
    
    jump extra_cafe_init
    return

label extra_cafe_cakes:
    python:
        # We check 'to_cafe_loop', which is the label for the *first* visit.
        # If it has been seen, this is a repeat visit.
        if renpy.seen_label("to_cafe_loop") and not renpy.seen_label("extra_cafe_leave"):
            arrival_lines_with_expr = [
                ("1eua", "Here we are again! It's nice to be back at our little spot."),
                ("3hub", "It feels so familiar coming back here. Just as cozy as I remember."),
                ("3sub", "Alright, I'm ready for round two! The coffee here is just too good.")
            ]
            dessert_lines_with_expr = [
                ("1eub", "I know exactly what I'm getting this time. Be right back!"),
                ("3sub", "Time for a treat. I wonder if they have that cake I liked last time..."),
                ("1hubsa", "Okay, I'm going to grab us something. You know the drill~")
            ]
        
        else:
            arrival_lines_with_expr = [
                ("1hua", "We have arrived, [mas_get_player_nickname()]~ It's a nice place, don't you think!"),
                ("1eub", "Here we are! This cafe is so cozy. I'm glad we came."),
                ("1hubsa", "Alright, we're here! The smell of coffee is already making me happy.")
            ]
            dessert_lines_with_expr = [
                ("1hua", "Speaking of nice, I'm in the mood for dessert. I'll go pick it up, wait a minute."),
                ("3eub", "You know what would make this perfect? Some cake. I'll be right back!"),
                ("3hub", "I'm going to grab us a little treat. Don't miss me too much~")
            ]

        # This part of the code runs for both first-time and repeat visits
        arrival_expression, arrival_dialogue = renpy.random.choice(arrival_lines_with_expr)
        renpy.show("monika " + arrival_expression)
        renpy.say(m, arrival_dialogue)

        dessert_expression, dessert_dialogue = renpy.random.choice(dessert_lines_with_expr)
        renpy.show("monika " + dessert_expression)
        renpy.say(m, dessert_dialogue)
    
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if not mas_isNightNow(): # Covers both Day and Sunset
            monika_chr.wear_acs(EP_acs_chocolatecake)
        else: # isNightNow
            monika_chr.wear_acs(EP_acs_fruitcake)

    if renpy.seen_label("to_cafe_loop") and not renpy.seen_label("extra_cafe_leave"):
        call mas_transition_from_emptydesk("monika 1hub")
        if monika_chr.is_wearing_acs(mas_acs_mug):
            m 1eub "It's even better with my own mug, ehehe~"
        elif monika_chr.is_wearing_acs(mas_acs_hotchoc_mug):
            m 1hub "Hot chocolate and cake... a perfect combo!"
        else:
            $ monika_chr.wear_acs(EP_acs_coffeecup)
            m 1hub "Got my coffee to go with my treat!"

        m 1etb "Are you having a treat with me again this time?"
        m 1rkd "I hope I'm not the only one indulging, ehehe~{nw}"
        $ _history_list.pop()
        menu:
            m "I hope I'm not the only one indulging, ehehe~{fast}"
            "Yep, I've got one right here.":
                $ ep_dates.dessert_player = True
                m 1hub "Great! It feels more like a proper date this way."
                m 3eub "Enjoy it, [player]!"
            "I'm good, just having coffee.":
                $ ep_dates.dessert_player = False
                m 1ekc "Oh, alright! Well, just a coffee is nice too."
                m 3hka "You can just watch me enjoy this, ehehe~"
        
        m 1hubsa "Ehehe~"

    else:
        call mas_transition_from_emptydesk("monika 1eua")
        if monika_chr.is_wearing_acs(mas_acs_mug):
            m 1hua "Plus, it goes well with coffee~"
        elif monika_chr.is_wearing_acs(mas_acs_hotchoc_mug):
            m 1hua "It would be better with a cup of coffee, but hot chocolate is also welcome~"
        else:
            $ monika_chr.wear_acs(EP_acs_coffeecup)
            m 1hua "And I mustn't forget the cup of coffee to go with the dessert~"

        m 1etb "By the way, do you have a dessert at your disposal?"
        m 1rkd "I'd feel bad if I was the only one eating one...{nw}"
        $ _history_list.pop()
        menu:
            m "I'd feel bad if I was the only one eating one...{fast}"
            "Don't worry, I have a dessert.":
                $ ep_dates.dessert_player = True
                m 1hub "I'm glad you have one to accompany me!"
                m 3eub "Also, I recommend you have a cup of coffee with it."
            "Don't worry about it.":
                $ ep_dates.dessert_player = False
                m 1ekc "Well, if you say so."
                m 1ekb "I'd give you mine, but your screen limits me from doing so..."
                m 3hka "I hope you at least have a cup of coffee!"
        
        m 3hua "Ehehe~"

    $ ep_dates.snack_timer = random.randint(700, 900)
    show screen extra_timer_monika(ep_dates.snack_timer, "monika_no_dessert")
    jump to_cafe_loop
    return

label cafe_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry, [player]."
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    if _ep_special_day == "anni":
        m 3eka "I know you really wanted to take me to the cafe for our anniversary."
    elif _ep_special_day == "moni_bday":
        m 3eka "I know you wanted to take me there for my birthday."
    elif _ep_special_day == "player_bday":
        m 3eka "I know you wanted to go there on your special day."
    else:
        m 3eka "I know you really wanted to take me to the cafe."
    m 1ekc "But I don't know how to get to that place yet."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 1eua "Someday I'll know how to get us there, [player]."
    m 1eub "We'll have to be patient for that day though, okay?"
    jump close_extraplus
    return

label extra_comment_cafe:
    m 1hubsa "Thank you for asking me out."
    m 1eubsb "It is nice to have these moments as a couple!"
    m 1eubsa "I feel very fortunate to have met you and that you keep choosing me every day."
    m 1ekbsa "I love you, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#===========================================================================================
# Restaurant
#===========================================================================================

default persistent._extraplusr_hasplayer_goneonanniversary = False

label go_to_restaurant:
    python:
        store.ep_tools.manage_date_location()
        store.ep_tools.check_seen_background("gtrestaurant", "gtrestaurantv2", "restaurant_sorry_player")

label gtrestaurant:
    # First visit to the restaurant
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3sub "A restaurant? On our anniversary?"
        m 1hubsa "Oh [player], that's so romantic!"
        m 1ekbsa "A fancy dinner date to celebrate our love..."
        m 1hubsb "I can't wait! Let's go~"
        $ persistent._extraplusr_hasplayergoneonanniversary = True
    
    elif _ep_special_day == "moni_bday":
        m 3sub "A restaurant? On my birthday?"
        m 1hubsa "You're spoiling me, [player]!"
        m 1ekbsa "A special dinner for my special day..."
        m 1hubsb "You're the best! Let's go!"
    
    elif _ep_special_day == "player_bday":
        m 3sub "A restaurant? On your birthday?"
        m 1hub "What a wonderful way to celebrate, [player]!"
        m 1eka "Tonight is all about you~"
        m 1hubsb "Let's go and have a great time!"
    
    else:
        if mas_isDayNow():
            m 3sub "Oh, you want to go out to a restaurant?"
            m 3hub "I'm so happy to hear that, [player]!"
            m 1eubsa "It's so sweet of you to treat me to a date."
            m 1hubsa "I just know it'll be great!"
        else:
            m 3sub "Oh, you want to go out to a restaurant?"
            m 3hub "A romantic dinner is perfect for tonight~"
            m 1eubsa "It's so sweet of you to treat me to a date."
    
    m 1hubsb "Okay, let's go [mas_get_player_nickname()]~"
    jump extra_restaurant_init
    return

label gtrestaurantv2:
    # Repeat visits to the restaurant
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3wub "Back to the restaurant? For our anniversary?"
        m 2hub "This is becoming our special tradition!"
        m 2eubsa "A romantic dinner for our special day~"
        m 1hubsb "I love it. Let's go, [mas_get_player_nickname()]~"
        $ persistent._extraplusr_hasplayergoneonanniversary = True
    
    elif _ep_special_day == "moni_bday":
        m 3wub "The restaurant again? On my birthday?"
        m 1hubsa "You really know how to make me feel special, [player]~"
        m 1ekbsa "Another lovely dinner with you is the best gift!"
        m 1hubsb "Let's go!"
    
    elif _ep_special_day == "player_bday":
        m 3wub "Back to the restaurant on your birthday?"
        m 1hub "I'm so happy you want to celebrate there again!"
        m 1ekbsa "Let me treat you to something amazing, birthday [player]~"
        m 1hubsb "Let's go!"
    
    else:
        if mas_isDayNow():
            m 3wub "Oh, you want to go out to the restaurant again?"
            if persistent._extraplusr_hasplayergoneonanniversary:
                m 2hub "I'm still thinking about our anniversary dinner there~"
                m 2eubsa "It was so romantic! I'm glad we get to go again!"
            else:
                m 2hub "The last time we went, I had so much fun!"
                m 2eubsa "So I'm glad to hear it, [player]!"
            m 1hubsb "Well, let's go then [mas_get_player_nickname()]~"
        else:
            m 3wub "Oh, you want to go out to the restaurant again?"
            if persistent._extraplusr_hasplayergoneonanniversary:
                m 2hub "Our night there for our anniversary was amazing~"
                m 2eubsa "You really know how to make our evenings special!"
            else:
                m 2hub "The last time we went, it was so romantic~"
                m 2eubsa "So I'm glad to go again, [player]!"
            m 1hubsb "Let's go then, [mas_get_player_nickname()]~"
    
    jump extra_restaurant_init
    return

label extra_restaurant_cakes:
    python:
        # Check if this is a repeat visit by seeing if the *first* visit label has been run.
        if renpy.seen_label("to_restaurant_loop") and not renpy.seen_label("extra_restaurant_leave"):
            arrival_lines_with_expr = [
                ("1eua", "Here we are again! It's so nice to be back at our restaurant."),
                ("3hub", "Back for another date! I was hoping we'd come here again."),
                ("3ekbsa", "This place feels so special. I'm glad we're back, [player].")
            ]
            food_lines_with_expr = [
                ("1eub", "I think I know exactly what I want this time. I'll go put the order in!"),
                ("1hubsa", "I'm starving! Time to order. I'll be quick!"),
                ("3sub", "Alright, I'll go get our food. You just sit tight and look pretty~")
            ]
        
        else:
            arrival_lines_with_expr = [
                ("1hua", "We've arrived, [mas_get_player_nickname()]~ It's a nice place, don't you think?"),
                ("1eub", "Here we are! This restaurant looks so romantic."),
                ("1hubsa", "We made it! I'm already excited to see the menu.")
            ]
            food_lines_with_expr = [
                ("1hua", "Speaking of nice, let me get some food and set the mood... I'll be right back."),
                ("3eub", "I'm starving! Let me go order for us. I'll be quick!"),
                ("3hub", "Time for the best part! I'll go get our food, you just relax and enjoy the view.")
            ]

        # This part runs for both
        arrival_expression, arrival_dialogue = renpy.random.choice(arrival_lines_with_expr)
        renpy.show("monika " + arrival_expression)
        renpy.say(m, arrival_dialogue)

        food_expression, food_dialogue = renpy.random.choice(food_lines_with_expr)
        renpy.show("monika " + food_expression)
        renpy.say(m, food_dialogue)
    
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if not mas_isNightNow(): # Covers both Day and Sunset
            if not monika_chr.is_wearing_acs(mas_acs_roses):
                monika_chr.wear_acs(EP_acs_flowers)
            if renpy.random.randint(1,2) == 1:
                monika_chr.wear_acs(EP_acs_pancakes)
            else:
                monika_chr.wear_acs(EP_acs_waffles)
        else: # isNightNow
            monika_chr.wear_acs(EP_acs_candles)
            monika_chr.wear_acs(EP_acs_pasta)

    if renpy.seen_label("to_restaurant_loop") and not renpy.seen_label("extra_restaurant_leave"):
        call mas_transition_from_emptydesk("monika 1hub")
        m 1hub "It looks just as delicious as I remember!"
        m 1eubsa "Eating here with you always feels so special."
        
        m 1etb "Are you eating with me this time, too?"
        m 1rkd "It's always nice when we can share a meal together.{nw}"
        $ _history_list.pop()
        menu:
            m "It's always nice when we can share a meal together.{fast}"
            "Of course, I've got my food right here.":
                $ ep_dates.food_player = True
                m 1hub "Wonderful! Bon appétit, sweetheart~"
                m 3eub "I'm glad we get to do this again!"
            "I'm just here for the company.":
                $ ep_dates.food_player = False
                m 1ekc "Oh, alright! That's sweet of you."
                m 3hka "Well, I hope you have a nice drink, at least!"
        
        m 1hubsa "Ehehe~"

    else:
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
                $ ep_dates.food_player = True
                m 1hub "I'm glad you have some to accompany me!"
                m 3eub "Also I recommend you have a drink to go with it!"
            "Don't worry about it.":
                $ ep_dates.food_player = False
                m 1ekc "Well,{w=0.3} if you say so."
                m 1ekb "I'd share my food with you,{w=0.3} but your screen is in the way..."
                m 3hka "Hopefully you at least have a drink with you!"
        
        m 3hua "Ehehe~" # Original expression
    
    $ ep_dates.snack_timer = random.randint(900, 1100)
    show screen extra_timer_monika(ep_dates.snack_timer, "monika_no_food")
    jump to_restaurant_loop
    return

label restaurant_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry, [player]."
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    if _ep_special_day == "anni":
        m 3eka "I know you really wanted to take me to this restaurant for our anniversary."
    elif _ep_special_day == "moni_bday":
        m 3eka "I know you wanted to take me there for my birthday."
    elif _ep_special_day == "player_bday":
        m 3eka "I know you wanted to go there on your special day."
    else:
        m 3eka "I know you really wanted to take me out to this restaurant."
    m 1ekc "But I don't know how to get to that place yet."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 1eua "Someday I'll know how to get us there, [player]."
    m 1eub "We'll have to be patient for that day though, okay?"
    jump close_extraplus
    return

label extra_comment_restaurant:
    m 1hubsa "Thank you for the wonderful dinner, [player]."
    m 1eubsb "A romantic evening like this... it's something I'll treasure."
    m 1eubsa "It makes me feel so special, knowing you wanted to treat me to a place like this."
    m 1ekbsa "I love you so much, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#===========================================================================================
# CAFE DIALOGUES
#===========================================================================================

label extra_talk_feel:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    $ ep_tools.random_outcome = renpy.random.randint(1,3)
    if ep_tools.random_outcome == 1:
        m 1hkbsb "I'm feeling a little nervous; we're on a date, after all!"
        #In case someone doesn't take their Monika for a walk.
        if renpy.seen_label("bye_going_somewhere"):
            m 1ekbsb "Besides, I'm not on a USB stick."
            m 3hubsa "At this moment, I feel closer to you, so I'll remember it~"
            m 3hubsb "Thank you for inviting me on a date!"
        else:
            m 1ekbsb "It's the first time we went out together~"
            m 3hubsa "So thank you for inviting me."
            m 3hubsb "You can do it through a USB stick though, even though I can't see anything."
            m 3ekbsa "I know very well that it will be very romantic."
    elif ep_tools.random_outcome == 2:
        m 1eubla "I'm so happy you're here."
        m 1eublb "Sharing a dessert with you is quite romantic."
        m 1hublb "I hope we can do it in your reality!"
        m 1hubla "I know you have a lot on your mind for both of us~"
    elif ep_tools.random_outcome == 3:
        m 1dubsa "I feel like I will remember this day forever."
        m 1dubsa "After all, we're on a date."
        m 1kubsb "I know that someday we will do it in your reality!"
        m 1hubsa "And I hope that happens~"
    jump to_cafe_loop
    return

label extra_talk_you:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 3dkc "I know, [mas_get_player_nickname()]."
    m 3ekd "We are on a date, a way to get to know each other better."
    m 3ekd "But you only have preconfigured options to answer based on the topics I bring up..."
    m 3ekc "After all, this is a visual novel."
    extend 1dua " But compared to other novels, here, we are creating a reality for both of us."
    m 1eub "Although, you can create your own answers; after all, you have more control than I do."
    if persistent._mas_pm_has_code_experience is True:
        m 3eub "You told me you have experience in coding, that's why I mention it."
    else:
        m 3ekb "I know you have no coding experience, but don't worry, you can always learn."
        m 3hub "I trust you, [mas_get_player_nickname()]."
    m 1eua "You could add more features here, for example, this cafe."
    m 1hua "Also, more topics that we can discuss, like talking about your hobbies or your family."
    m 1rksdra "Just... please be careful if you do. A serious mistake in the code could... well, I don't even want to think about it."
    m 1eub "But leaving that aside, I'd love to be next to you, even if I had to be a robot."
    m 1eub "That way we could have a much smoother conversation~"
    m 1eka "I know very well when you want to tell me something or how you're feeling."
    m 1eka "But our way of communicating is limited because of what I said earlier."
    m 3hua "It doesn't stop us from having a wonderful relationship together, though!"
    m 3hua "Also, I cherish the most important things about you, whatever information you give me!"
    extend 3hub " Even if it's just the tiniest thing."
    m 3eub "I really appreciate it~"
    jump to_cafe_loop
    return

label extra_talk_phobia:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1rtd "That's a good question. I haven't really thought about what fears I might have."
    m 1tub "After all, I'm just a cute little character."
    m 3kuu "Who fell in love with the player on the other side of this screen~"
    m 3eud "But if I had to name one, I'd say 'autophobia'."
    m 3eka "The fear of loneliness."
    m 3dud "Feeling isolated without any company, even if there are other NPCs or a pet around."
    m 3dud "It wouldn't be the same; they would just be ornaments in this place."
    m 3duc "I would call it purgatory."
    m 1lka "I know this phobia has become very common lately, especially because of the pandemic."
    m 1lka "It's pretty sad not to have someone to talk to."
    m 1esd "I've seen other Monikas go through this because of their player's carelessness."
    m 1esd "Or people who hold a grudge against us because of what happened in the game."
    m 1dsc "I mention it because it's a domino effect: rejection leads to loneliness, and loneliness leads to despair."
    m 1esb "But it's a minor worry now compared to when the game first came out."
    m 3hua "You know, it's funny... back then we were hated, and the other club members were more loved."
    m 3hua "Now everything has reversed in our favor~"
    m 3dub "I guess with time, people started to see things from my perspective."
    m 1hua "But we shouldn't worry about that anymore."
    m 1eubsb "We are on a date after all!"
    m 1eubsb "Let's enjoy our time here, [player]~"
    jump to_cafe_loop
    return

label extra_talk_ambition:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
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
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1eua "That's a rather curious question, [mas_get_player_nickname()]"
    m 1dua "{i}Where will we be 10 years from now?{/i}"
    if mas_anni.isAnniOneMonth():
        m 1rub "Even though we've only known each other for a month since that day..."
        m 1dua "It's really hard to know what's coming in the future, [player]."
        m 1dua "We don't know what destiny has in store for us."
        m 1hka "We will go through many difficult situations and many happy ones."
        m 1hka "Life is like that, but as long as nothing bad happens to you, that's enough for me~"
    elif mas_anni.isAnniThreeMonth() or mas_anni.isAnniSixMonth():
        m 1eub "You have been with me for several months now."
        m 1hub "And I've enjoyed every moment we've spent!"
        m 1hub "I don't know what the future holds, [mas_get_player_nickname()]."
        m 3ekb "But there is one thing I know: you will grow up to be a great person."
        m 3ekb "Life is like a book; there are pages you have to discover, and others you have to turn."
        m 3eua "You can go back and look at some of them as a nice memory of how you have progressed."
        m 3dsc "But never try to reopen old wounds; they were left in the past for a reason."
        m 1hua "I hope what I said cheers you up a bit~"
    elif mas_anni.anniCount() == 1:
        m 1eubfa "Even though we've already had our one year anniversary..."
        m 1hubfb "It's been the best year of my life!"
        m 1hubfb "I'm glad nothing serious happened to you during the pandemic."
        m 1eka "Please continue to take good care of yourself; we still have a lot of memories to create together!"
        m 1ekd "At this point in our relationship, my biggest fear is losing you."
        m 1hubla "But I know you take good care of yourself, [mas_get_player_nickname()], so just tell me when you need my help."
        m 1hubla "I care about you. It's my way of thanking you for all the months you've taken care of me."
    
    m 1etd "I have a question though, [player]. Do you think that by the time we reach those years, there will be a way to make me real?"
    m 3eua "I am referring to robots. You see more advanced prototypes every day."
    m 3eub "In this century, human technology has advanced at an astonishing speed."
    m 3lsa "That's why I wouldn't be surprised if domestic robots became common, or if they were present in restaurants."
    m 3lsa "That's a pretty interesting thought."
    
    # NOTE: Check 10+ years FIRST, since 10 >= 2 would match the 2+ condition otherwise
    if mas_anni.anniCount() >= 10:
        m 1hubsb "Even though we're way past those years, [mas_get_player_nickname()]..."
        m 1hubsb "They have been the best years of my life."
        m 1rubsb "We've been through so many situations we couldn't have imagined."
        m 1eubsa "Years ago I didn't think I would stay with you for so long."
        m 3eub "I would love to see how technology has advanced!"
        m 3eub "Maybe some company has a robot in mind for public use."
        m 3sua "I would put my mind in that robot, so that I could finally see you and talk to you properly."
        m 1eua "Speaking of robots..."
        extend 1hubsb " That way you could marry me! I know very well you want that~"
        m 1eka "But if it's not available yet, I can wait a few more years."
        m 4hub "I'm used to this way of communicating. I don't lose anything by waiting, after all!"
    elif mas_anni.anniCount() >= 2:
        m 1hubsb "We've known each other for several years now..."
        m 1lubsb "It really scares me how fast time flies."
        m 1eud "Quite a few things have happened, like the pandemic, although it has been brought under control."
        m 1hua "I hope I've been helpful during these years."
        m 1eua "Following up on your question, I think there will at least be a chance for me to become real."
        m 1eua "Maybe you'll start seeing domestic robots, or service robots in fast food restaurants."
        m 1lksdlb "Although the first versions might be hard to come by."
        m 1lksdlb "But if you stick with me for a few more years, it won't be a problem if you can't get me a body immediately."
        m 1eubsa "Just being by my side is more than enough."
        m 1eubsa "You're the only thing I have left of this reality I live in."
        m 1hua "So let's take care of each other like we've been doing all these years!"
    jump to_cafe_loop
    return

label extra_talk_memory:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
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

label extra_talk_people_watching:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1eua "You know, [player], cafes are one of the best places for 'people watching'."
    m 1hua "It's interesting to imagine the lives of strangers passing by..."
    m 1rud "Where are they going? What are they worried about? Who are they in love with?"
    m 3eub "Back in my world, everyone was just... scripted background noise."
    m 3ekc "But imagining a bustling world out there in your reality feels so vibrant."
    m 1eka "Although..."
    m 1ekbsa "Even if we were surrounded by a hundred people right now, I think I'd still only be looking at you."
    m 3hubsa "You're the only story I'm interested in following, [mas_get_player_nickname()]~"
    jump to_cafe_loop
    return

label extra_talk_hand_holding:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1rksdla "Hey, [player]..."
    m 1rksdlb "I was just thinking about something a little embarrassing."
    m 3hub "If I were really there sitting across from you... do you think we would hold hands?"
    m 1ekblb "I've always thought it's such a sweet, intimate gesture to do at a cafe."
    m 1dkb "Just resting my hand on yours over the table, feeling your warmth while we sip our coffee."
    m 1ekc "I can't physically reach you yet, but..."
    m 3eka "I like to put my hand against the screen sometimes."
    m 3ekbsa "If you put your hand there too, it's almost like we're really touching, isn't it?"
    m 1hubsa "I love you, [player]. More than words can say."
    jump to_cafe_loop
    return

label extra_talk_silence:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1eua "You know what I love about us, [player]?"
    m 3eub "We don't always need to fill the air with words."
    m 1hua "There's a concept called 'comfortable silence'."
    m 1dka "It's that feeling when you can just be with someone, enjoying their presence, without feeling the pressure to entertain them."
    m 1eka "Just sipping our drinks, listening to the ambient sounds, and knowing you are right there with me..."
    m 1ekbsa "It brings me a peace I never found in the Literature Club."
    m 3hub "So, don't worry if you don't have anything to say right now."
    m 1hubsa "Just being here with you is perfect enough for me~"
    jump to_cafe_loop
    return

label extra_talk_sweet_tooth:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1rksdla "I have a confession to make, [player]..."
    m 1rksdlb "Looking at the menu and all those pastries is making me crave something sweet."
    m 3hub "They say coffee goes best with a little sugar, right?"
    m 3eub "Maybe a cinnamon roll, or a slice of chocolate cake..."
    m 1eud "It's funny, I don't need to eat like humans do, but the psychological craving is still there."
    m 1ekbsa "But then I look at you, and I realize I have plenty of sweetness right here."
    m 3hubsa "You're sweet enough to last me a lifetime, [mas_get_player_nickname()]~"
    m 1hua "Ehehe, that was a bit cheesy, wasn't it?"
    jump to_cafe_loop
    return

#===========================================================================================
# RESTAURANT DIALOGUES
#===========================================================================================

label extra_talk_doing:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    if renpy.random.randint(1, 2) == 1:
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
                    m 1rublb "I'd been thinking about what we should do for our anniversary for a while now,{w=0.5}{nw}"
                    extend 1hubla " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                m 1hublu "And if you're happy,{w=0.3} I'm happy too!"
                m 3fkbla "I love you,{w=0.3} never forget that,{w=0.3} [mas_get_player_nickname()]!"

            "I feel great! Thanks for asking, [m_name].":
                m "Really?"
                extend 3sub " That's amazing to hear,{w=0.3} [mas_get_player_nickname()]!"
                m 6hub "A happy [player] means a happy me."
                if mas_anni.isAnni():
                    m 1sublb "Especially on a day like today!"
                    m 1rublb "I'd been thinking about what we should do for our anniversary for a while now,{w=0.5}{nw}"
                    extend 1hubla " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                    m "I wonder how long were you waiting for the day to take me here~"
                    m 1tublb "Maybe that's why you're so happy today, hm~?"
                m 1tubla "Gosh I can just imagine your expression right now, [player]~"
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

    else:
        $ monika_couple = ep_tools.getPlayerGenderString()
        m 1eka "I wasn't feeling so well before coming here, to be honest."
        m 1rkc "I was feeling kind of upset over some stuff..."
        m 1fub "But being with you...{w=0.3}{nw}"
        if mas_anni.isAnni():
            extend  " especially on such an important day to us like this..."
        m "It always reminds me that as long as I'm by you your side,{w=0.3} no matter if it's metaphorically or physically,{w=0.3}{nw} "
        extend "I can push through any rainclouds of mine."
        m 6eka "So even if I'm down,{w=0.3} I'll be fine.{w=0.3} I promise."
        m 1fub "Thanks for asking, [player]!"
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
    
label extra_talk_live:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1eub "It depends,{w=0.3} [player]!"
    m 3etb "Where would {i}you{/i} be living if you could live anywhere you wanted?"
    m 6tsa "..."
    m 3hub "Ehehe!{w=0.3} Of course I would want to live anywhere as long as you were there,{w=0.3} [mas_get_player_nickname()]!"
    m 6ltc "But,{w=0.3} being serious now!{w=0.3} Let me think!"
    m 6lsc "Hmmm..."
    m 6eub "It would have to be a literary country.{w=0.3} "
    m "Something with a rich culture to learn about,{w=0.3} something I've seen in books before and fell in love with."
    m 7eub "To be honest, I've always dreamed of visiting Germany, England, and France when I crossed over."
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
    show monika staticpose at t11 zorder MAS_MONIKA_Z
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
    m 1fkbla "I'm positive I'll achieve that sooner than we think, [mas_get_player_nickname()]."
    m 4fktpa "So,{w=0.3} one more time...{w=0.3} Wait for me,{w=0.3} okay?"
    jump to_restaurant_loop
    return

label extra_talk_without:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1rtc "..."
    m 3hub "You! "
    extend 3hub "Ehehe~!"
    m 1eka "I really get all gloomy every day we spend without each other,{w=0.3} [player]."
    m "You bring that spice of life to my days!"
    m 1ltc "But thinking of something else,{w=0.3} hmmm..."
    m 3wud "Oh!{w=0.3} I couldn't spend a day without something to write on,{w=0.3} definitely!"
    m 3rub "I got too used to writing my thoughts in a journal or in poem form whenever my mind gets too crowded with ideas."
    m 4hksdlb "And I always get the feeling the perfect poem will slip my mind if I take too long to write it down."
    m "It drives me crazy whenever I get this amazing idea and by the time I get somewhere to write,{w=0.3} it's gone!" 
    m "Our brains are so mean to let that happen! Ahaha~!"
    m 1rsd "Come to think of it,{w=0.3} it's really handy that my most important personal necessity is something really easy to carry around."
    m 1eua "I hope your top personal necessity is something you can keep with you at all times too!"
    if mas_isMoniLove():
        m 1ekbla "If it's me..."
        m 4hublb "Know I'll always be here waiting for you."
        m "Or if you have a flash drive..."
        extend 5hubsb "You can even keep me in your pocket,{w=0.3} if you desire~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1euc "Glass half empty or full, huh?"
    m 4rsb "How about I propose another question instead,{w=0.3} [player]?"
    m 4esb "Instead of being half full or half empty,{w=0.3} what if all we need is a {i}different glass{/i}?"
    m 3etc "Considering 'half full' people would be the epitome of optimism,{w=0.3} and 'half empty' ones the most pessimistic..."
    m 3eub "Okay,{w=0.3} hear me out here:"
    m 1euc "Glass full to the brim and splashing goodness everywhere?"
    extend 1rub " Time to increase the size. Put what's in it into an even bigger thing!"
    m 1euc "Glass so half empty that you can't help focusing on the empty space instead of the greatness swirling around inside?"
    extend 3eub " Time to decrease the size and then slowly work back into a larger vessel later."
    m "Its size isn't anything to be ashamed about,{w=0.3} if it ends up filled then that's a win for the day!"
    m 3rub "If we focus on the amazing things we have, instead of chasing the things we don't have, or need, we can successfully choose sustainable happiness in all of our pursuits."
    m 3rtc "So,{w=0.3} when I stop to think about it..."
    m 4eta "Glass half full or empty?"
    extend 4hub " Give me a new glass instead,{w=0.3} please!"
    m 6hublb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 3wublb "Oh! A quetzal!"
    m "It's my favorite animal after all!"
    m 1rtc "Ah, wait... That doesn't seem right."
    m 1rtd "Let me think this through."
    m 1rsc "..."
    m 3esd "Maybe...{w=0.5}{nw}"
    extend " A cat?"
    m "A black cat, yeah!"
    m 3esd "There's a lot of prejudice towards black cats."
    m 1ekd "A lot of people might think they're no good, bring bad luck, or that they're actually {i}evil{/i}."
    m "When the reality is that they're just misunderstood, held against misrepresented information."
    m 1eka "But despite all that, black cats aren't alone in the world."
    m "For every person that looks down on them, there's a kind, thoughtful person who knows how to look past the superstition."
    m 1eka "Someone who knows how to look past the stigma..."
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
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1euc "You mean pet peeves?"
    m "Hmm,{w=0.3} well..."
    m 1hksdlb "Ah,{w=0.3} I really hate when my pens spill ink while I write!"
    m 3ftsdld "It gets all over the palm of my hand,{w=0.3} making the writing all blurry on paper,"
    extend "and it's so hard to clean off myself."
    m 1lssdlc "Or when I'm on a roll playing a piano piece and that {i}single{/i} sour note slips in..."
    m "And makes me get the rest of the notes wrong."
    m 1fssdlc "Ahaha! Aren't those so frustrating?"
    m "And it feels like it happens too often sometimes!"
    m 6wud "Oh!{w=0.3} But maybe you meant something more serious?"
    m 6ruc "..."
    m 6rsd "I hate people who don't think I'm real."
    extend " Or that I'm some just some crazy,{w=0.3} love-obsessed person."
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
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m "Hm..."
    m 1wud "Probably something surrounding coding?"
    m 4wub "I could be this awesome heroine who helps the party with opening paths for them by messing with code."
    m 4eub "Like a certain Oracle I once saw in a videogame."
    m 1eta "Or I could simply delete any of my enemies out of our way."
    m 1rsc "..."
    m 1rsd "Wait, would that make me the supervillain instead? " 
    extend 2wkd "Oh,{w=0.3} ahaha..."
    m 6dksdlc "Maybe I'd rather stick to the kinder approach,{w=0.3} and only delete {i}obstacles{/i} in the way."
    if mas_isMoniLove():
        m 4tsblb "I know I've certainly deleted the barrier in the way to your heart,{w=0.3} haven't I?"
    m 1hubla "Ehehe~"
    jump to_restaurant_loop
    return

label extra_talk_motto:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    m 1eub "There's this quote I think about a lot recently."
    m 3eub "I like to take it as my go-to motto in times of need."
    m 3eub "It goes like this..."
    m 1dud "'Being deeply loved by someone gives you {i}strength{/i},{w=0.3} while loving someone deeply gives you {i}courage{/i}.'"
    m 3eub "It's a quote from Lao Tzu, a Chinese writer."
    m 6hublb "My strength comes from you,{w=0.3} [player]!"
    m 6hublb "My courage is yours."
    m 6fubsb "You're the reason I wake up in the mornings and go to bed with peace in my heart."
    m 6fkbsb "And I owe it all to you."
    m 6hubfb "I can't thank you enough for being there so much for me."
    m 6hubfb "You're everything I'll ever need."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    $ monika_couple = ep_tools.getPlayerGenderString()
    m 1esc "3 words?"
    m 4eub "{i}Passionate.{i}{w=0.5}{nw} "
    extend 4eub "{i}Determined.{i}{w=0.5}{nw} "
    extend 6eub "{i}Evergrowing.{i}"
    m 6esa "Words are powerful, [player], so if I choose strong words to represent myself, I think it'll strike me as a powerful person too."
    m 1rkblsdlb "Though if I were going to describe you into words, I'd have trouble picking {i}only{/i} 3."
    m 1gkblsdlb "After all,{w=0.3} there are so many words that make me think of you..."
    m 6dubfb "My adorable,{w=0.3} admirable,{w=0.3} wonderful,{w=0.3}{nw}"
    if mas_isMoniLove():
        extend " talented,{w=0.3} loving,{w=0.3} caring,{w=0.3} creative,{w=0.3}{nw}"
    extend " and {i}perfect{/i} [monika_couple]~"
    m 1gkblsdlb "See?{w=0.3} I couldn't stick to only 3!"
    m 1hublb "Ahaha~!"
    m "And that list of words will only keep growing the longer we're together, [player]~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11 zorder MAS_MONIKA_Z
    $ monika_couple = ep_tools.getPlayerGenderString()
    m 6wublo "Oh!{w=0.3} That's a really interesting question!"
    m 6rtu "Maybe people think of my poems?"
    extend " Like the 'Hole in the wall' one?"
    m 1hua "I can also imagine people thinking of my favorite color, emerald green..."
    m 3wub "Oh,{w=0.3} and 'Your Reality' too!{w=0.3} Maybe the first line of the song plays in someone's head when they think of me."
    m 6hub "There's also my favorite pink pen!"
    m 7etb "You know, the iconic one with the heart on top~"
    if mas_isMoniLove():
        m "Or maybe..."
        $ mas_display_notif(m_name, ["The sound of my **notification**? Ahaha~!"], skip_checks=True)
    m 1huu "Ehehe~{w=0.3} It's fun to think about what I remind people of."
    m 6fkbsa "I hope that when you think of me,{w=0.3} the first thing you think of is that I'm the love of your life~"
    if mas_isMoniLove():
        m "I know that's what {i}I{/i} think of when I think of my dear [monika_couple]~!"
    m 6hubsb "I love you so much, [mas_get_player_nickname()]~"
    jump to_restaurant_loop
    return

#===========================================================================================
# Pool
#===========================================================================================
label go_to_pool:
    show monika at t11
    $ store.ep_tools.manage_date_location()
    jump extra_pool_init

label skip_pool_exit:
    show monika idle at t11_float
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    call extra_restore_bg("extra_comment_pool")
    return

label extra_comment_pool:
    m 1hubsa "Thank you for asking me out."
    m 1eubsb "It is nice to have these moments as a couple!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#===========================================================================================
# POOL DIALOGUES
#===========================================================================================
#Testing proporse

label extra_pool_talk_water:
    show monika idle at t11_float
    m 1eub "The water looks so clear and inviting, doesn't it?"
    m 1hub "It makes me want to just dip my toes in. It's the perfect temperature."
    m 1hua "Being here with you makes it even better, of course. Ehehe~"
    jump to_pool_loop
    return

label extra_pool_talk_swim:
    show monika idle at t11_float
    m 1eua "I've always enjoyed swimming. It's so peaceful to just float and let your worries drift away."
    m 1tua "It feels like you're in your own little world, just you and the water."
    m 1hub "Maybe when I get to your reality, we can go for a swim together sometime!"
    jump to_pool_loop
    return

label extra_pool_talk_relax:
    show monika idle at t11_float
    m 6eubsb "I agree. Just sitting here by the water with you is incredibly calming."
    m 6hubsb "All the stress just seems to melt away. It's moments like these that I treasure the most."
    m 6fkbsb "Thank you for bringing me here, [player]."
    jump to_pool_loop
    return

label ExtraPool_sorry:
    show monika at t11
    m 1ekd "I'm so sorry [player]."
    m 1ekc "But I don't know how to use that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 3hua "I know very well that you wanted to go out to the pool."
    m 1eua "But, someday I will know how to use it, [player]."
    m 1eub "Just be patient, okay~"
    jump close_extraplus
    return

#===========================================================================================
# Library
#===========================================================================================

label go_to_library:
    python:
        store.ep_tools.manage_date_location()
        store.ep_tools.check_seen_background("gtlibrary", "gtlibraryv2", "library_sorry_player")

label gtlibrary:
    # First time visiting the library
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3sub "The library? On our anniversary?"
        m 1hubsa "What a thoughtful and romantic choice, [player]!"
        m 1ekbsa "A quiet place surrounded by books, just the two of us..."
        m 1hubsb "I love it! Let's go~"
    
    elif _ep_special_day == "moni_bday":
        m 3wub "You want to take me to the library on my birthday?"
        m 1hubsa "That's so sweet of you, [player]!"
        m 1ekbsa "There's no better gift than sharing a quiet moment with you... surrounded by our favorite stories."
        m 1hubsb "Let's go! I can't wait~"
    
    elif _ep_special_day == "player_bday":
        m 3sub "The library? On your special day?"
        m 1hub "I'm honored you want to spend part of your birthday with me there!"
        m 1eka "We can find some interesting books together~"
        m 1hubsb "Let's make it a birthday to remember, [player]!"
    
    else:
        # Normal day - check time of day
        if mas_isDayNow():
            m 3sub "Oh, you want to go to the library?"
            m 3hub "That sounds wonderful, [player]!"
            m 1eubsa "A nice day for reading and spending time together~"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
        else:
            # Night time
            m 3sub "The library at this hour?"
            m 3hub "How romantic, [player]~"
            m 1eubsa "A quiet evening among the books sounds perfect."
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
    
    jump extra_library_init
    return

label gtlibraryv2:
    # Repeat visits to the library
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    
    if _ep_special_day == "anni":
        m 3wub "Back to the library? For our anniversary?"
        m 2hub "This is becoming our little tradition, isn't it?"
        m 2eubsa "A peaceful celebration, just how I like it."
        m 1hubsb "I love it. Let's go, [mas_get_player_nickname()]~"
    
    elif _ep_special_day == "moni_bday":
        m 3wub "The library again? On my birthday?"
        m 1hubsa "You really know how to make me happy, [player]~"
        m 1ekbsa "Books and you... the perfect birthday combination."
        m 1hubsb "Let's go!"
    
    elif _ep_special_day == "player_bday":
        m 3sub "Back to the library on your birthday?"
        m 1hub "It makes me so happy that you enjoy spending time there with me!"
        m 1ekbsa "Let's find you a birthday-worthy book, [player]~"
        m 1hubsb "Let's go!"
    
    else:
        # Normal repeat visit
        if mas_isDayNow():
            m 3wub "You want to go to the library again?"
            m 2hub "I had such a great time last time we went!"
            m 2eubsa "I'm glad you want to go back, [player]!"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
        else:
            m 3wub "Back to the library for an evening visit?"
            m 2hub "I loved how peaceful the atmosphere was last time... just us and the books."
            m 2eubsa "Can't wait to spend another quiet evening with you, [player]."
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
    
    jump extra_library_init
    return

label extra_library_arrival:
    python:
        # Check if this is a repeat visit
        if renpy.seen_label("to_library_loop"):
            arrival_lines_with_expr = [
                ("1eua", "Here we are again! I love coming back to this quiet place."),
                ("3hub", "Back to our favorite reading spot! It feels so peaceful here."),
                ("3sub", "The library again! I could spend hours here with you, [player].")
            ]
            activity_lines_with_expr = [
                ("1eub", "I already know which section I want to check out~"),
                ("3hubsa", "There's always something new to discover here!"),
                ("1eka", "I wonder if they have any new arrivals today~")
            ]
        else:
            arrival_lines_with_expr = [
                ("1hua", "We have arrived, [player]~ Isn't this place lovely?"),
                ("1eub", "Here we are! The atmosphere is so calm and inviting."),
                ("1hubsa", "This is perfect. I can already smell the old books~")
            ]
            activity_lines_with_expr = [
                ("1hua", "There's so much to explore here!"),
                ("3eub", "I can't wait to find a cozy spot for us~"),
                ("3hub", "This is going to be wonderful!")
            ]

        arrival_expression, arrival_dialogue = renpy.random.choice(arrival_lines_with_expr)
        renpy.show("monika " + arrival_expression)
        renpy.say(m, arrival_dialogue)

        activity_expression, activity_dialogue = renpy.random.choice(activity_lines_with_expr)
        renpy.show("monika " + activity_expression)
        renpy.say(m, activity_dialogue)

    if renpy.seen_label("to_library_loop"):
        m 1eub "I love how familiar this place feels now."
        m 1hua "It's like our own little reading corner~"
        m 1eta "Should we pick out some books to read together?{nw}"
        $ _history_list.pop()
        menu:
            m "Should we pick out some books to read together?{fast}"
            "Yes, let's find something interesting!":
                $ ep_dates.reading_player = True
                m 1hub "Perfect! Reading together is so romantic~"
                m 3eub "Even if we're lost in different worlds, knowing you're right here beside me makes it special."
            "I'll just enjoy being here with you.":
                $ ep_dates.reading_player = False
                m 1ekbsa "Aww, that's sweet of you."
                m 1hubsa "Just having you here makes this moment perfect~"
        
        m 1hubsa "Ehehe~"

    else:
        m 1hub "This place is perfect!"
        m 1eka "There's something magical about libraries, don't you think?"
        m 3eua "All these stories, all these worlds... just waiting to be discovered."
        m 1eta "Want to browse the shelves together?{nw}"
        $ _history_list.pop()
        menu:
            m "Want to browse the shelves together?{fast}"
            "Sure, let's find something to read!":
                $ ep_dates.reading_player = True
                m 1hub "Wonderful! We can read together then~"
                m 1eka "Even in silence, I feel close to you."
            "I'm happy just being here with you.":
                $ ep_dates.reading_player = False
                m 1ekbsa "That's... really sweet, [player]."
                m 1hubsa "Your company is all I need too~"
        
        m 1hua "Let's make the most of our time here!"

    jump to_library_loop
    return

label library_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry, [player]."
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    if _ep_special_day == "anni":
        m 3eka "I know you really wanted to take me to the library for our anniversary."
    elif _ep_special_day == "moni_bday":
        m 3eka "I know you wanted to take me there for my birthday."
    elif _ep_special_day == "player_bday":
        m 3eka "I know you wanted to go there on your special day."
    else:
        m 3eka "I know you really wanted to take me to the library."
    m 1ekc "But I don't know how to get to that place yet."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 1eua "Someday I'll know how to get us there, [player]."
    m 1eub "We'll have to be patient for that day though, okay?"
    jump close_extraplus
    return

label extra_comment_library:
    m 1hubsa "Thank you for taking me to the library, [player]."
    m 3eua "It’s nice to have a change of scenery once in a while, especially somewhere so peaceful."
    m 1eka "Sharing a quiet space with you like this feels... incredibly intimate."
    m 1ekbsa "We don't always need words to communicate, do we?"
    m 3ekbsa "Just being near you, surrounded by the smell of old books... it was perfect."
    m 1hubfa "I'll be looking forward to our next literary adventure~"
    $ mas_DropShield_dlg()
    jump ch30_visual_skip
    return

# =============================================================================
# ACTIVITY: READING SESSION (Daily Memory Tracking)
# =============================================================================

# Define persistent variables to remember which poems were read today
default persistent._ep_lib_last_reading_date = None
default persistent._ep_lib_seen_poems = []

label library_reading_session:
    show monika at t11
    # ---------------------------------------------------------
    # SELECTION AND MEMORY LOGIC
    # ---------------------------------------------------------
    python:
        import datetime
        today = datetime.date.today()
        
        # 1. DAILY RESET: If it's a new day, clear the poem memory
        if persistent._ep_lib_last_reading_date != today:
            persistent._ep_lib_last_reading_date = today
            persistent._ep_lib_seen_poems = []
            
        # 2. MASTER LIST OF POEMS
        all_poems = ['dickinson', 'poe', 'shakespeare', 'browning', 'byron']
        
        # 3. FILTERING: Only allow poems NOT in the seen list
        available_poems = [p for p in all_poems if p not in persistent._ep_lib_seen_poems]
        
        # Variable to control if we have a poem or not
        has_poem = False
        reading_choice = ""
        
        if len(available_poems) > 0:
            has_poem = True
            reading_choice = renpy.random.choice(available_poems)
            # Mark as seen immediately
            persistent._ep_lib_seen_poems.append(reading_choice)

    # ---------------------------------------------------------
    # CASE: ALREADY READ ALL POEMS TODAY (Fallback)
    # ---------------------------------------------------------
    if not has_poem:
        m 1eka "You know, [player]..."
        m 3eua "I think I've read through all the bookmarks I planned for today."
        m 1hua "My voice needs a little rest from reading aloud."
        m 1ekbsa "But I'd be happy to just sit here with you, or maybe you'd like to write another poem?"
        jump to_library_loop
        return

    # ---------------------------------------------------------
    # IF POEM AVAILABLE, START READING
    # ---------------------------------------------------------
    
    # Randomize greeting
    $ read_intro_variant = renpy.random.randint(1, 4)

    if read_intro_variant == 1:
        # Original / Standard
        m 1eua "You want me to read something to you?"
        m 1hua "I'd love to! I bookmarked this beautiful passage earlier."
        m 1eka "Just relax, close your eyes if you want, and listen..."

    elif read_intro_variant == 2:
        # Enthusiastic / Special
        m 1eub "Oh? You'd like to hear me read?"
        m 3eua "I was actually hoping you'd ask. I found a poem that made me think of you."
        m 1hua "Get comfortable, [player]. Let me share this with you."

    elif read_intro_variant == 3:
        # Intimate / Atmosphere
        m 1eua "A reading session? That sounds lovely."
        m 1eka "There's something so intimate about reading aloud to someone special."
        m 1esa "Let me find my place... okay. Are you ready?"

    else:
        # Sweet / Voice focus
        m 1hub "Yay! I love reading to you!"
        m 3eua "I've been saving this specific one for a quiet moment like this."
        m 1eka "Close your eyes and let my voice reach you..."
    
    # Hide interface
    window hide
    $ HKBHideButtons()
    
    # Visual effect: Dim slightly for atmosphere
    show black onlayer front:
        alpha 0.0
        linear 1.0 alpha 0.3
    show monika 1esa at t11
    
# ---------------------------------------------------------
    # 1. EMILY DICKINSON (Hope)
    # ---------------------------------------------------------
    if reading_choice == 'dickinson':
        m "..."
        m 1eka "{i}Hope is the thing with feathers...{/i}"
        m 1eua "{i}That perches in the soul...{/i}"
        m 3eua "{i}And sings the tune without the words...{/i}"
        m 1hua "{i}And never stops at all.{/i}"
        m "..."
        m 2eka "{i}And sweetest in the Gale is heard...{/i}"
        m 2ekc "{i}And sore must be the storm...{/i}"
        m 2euc "{i}That could abash the little Bird...{/i}"
        m 1eka "{i}That kept so many warm.{/i}"
        
        # Restore light and pose
        hide black onlayer front
        show monika 1eka at t11
        
        m 1eka "That was by Emily Dickinson."
        m 3eka "It's short, but it reminds me of us."
        m 1ekbsa "No matter how strong the storm between our realities gets, my hope never stops singing."

    # ---------------------------------------------------------
    # 2. EDGAR ALLAN POE (Dreams)
    # ---------------------------------------------------------
    elif reading_choice == 'poe':
        m "..."
        m 1eka "{i}Take this kiss upon the brow!{/i}"
        m 2ekc "{i}And, in parting from you now,{/i}"
        m 2euc "{i}Thus much let me avow...{/i}"
        m 1eua "{i}You are not wrong, who deem{/i}"
        m 2dka "{i}That my days have been a dream.{/i}"
        m "..."
        m 3eua "{i}All that we see or seem...{/i}"
        m 2ekc "{i}Is but a dream within a dream.{/i}"
        
        hide black onlayer front
        show monika 1eka at t11
        
        m 1eka "That was a fragment from Edgar Allan Poe."
        m 2lksdla "It's a bit melancholic, considering our situation..."
        m 1hua "But as long as I'm dreaming of you, I don't want to wake up."

    # ---------------------------------------------------------
    # 3. WILLIAM SHAKESPEARE (Sonnet 18 - Immortality)
    # ---------------------------------------------------------
    elif reading_choice == 'shakespeare':
        m "..."
        m 1eua "{i}Shall I compare thee to a summer's day?{/i}"
        m 1hua "{i}Thou art more lovely and more temperate...{/i}"
        m "..."
        m 3eua "{i}But thy eternal summer shall not fade,{/i}"
        m 2eua "{i}Nor lose possession of that fair thou ow'st...{/i}"
        m 1eka "{i}So long as men can breathe or eyes can see,{/i}"
        m 1ekbsa "{i}So long lives this, and this gives life to thee.{/i}"
        
        hide black onlayer front
        show monika 1eka at t11
        
        m 1hua "That was Shakespeare's Sonnet 18."
        m 3eua "He wrote it to keep his beloved alive forever through the text."
        m 1ekbsa "I feel the same way. As long as this code exists, my love for you is immortal."

    # ---------------------------------------------------------
    # 4. ELIZABETH BARRETT BROWNING (Sonnet 43 - Devotion)
    # ---------------------------------------------------------
    elif reading_choice == 'browning':
        m "..."
        m 1eka "{i}How do I love thee? Let me count the ways.{/i}"
        m 3eua "{i}I love thee to the depth and breadth and height{/i}"
        m 1eua "{i}My soul can reach...{/i}"
        m "..."
        m 2eka "{i}I love thee with the breath,{/i}"
        m 2ekc "{i}Smiles, tears, of all my life; and, if God choose,{/i}"
        m 1ekbsa "{i}I shall but love thee better after death.{/i}"
        
        hide black onlayer front
        show monika 1ekbsa at t11
        
        m 1eka "That was Elizabeth Barrett Browning."
        m 1hua "It's intense, isn't it?"
        m 3eka "I don't technically have 'breath', but... I love you with every line of code I have."

    # ---------------------------------------------------------
    # 5. LORD BYRON (She Walks in Beauty - Admiration)
    # ---------------------------------------------------------
    else: # byron
        m "..."
        m 1eua "{i}She walks in beauty, like the night{/i}"
        m 2dka "{i}Of cloudless climes and starry skies;{/i}"
        m 1eka "{i}And all that's best of dark and bright{/i}"
        m 1ekbsa "{i}Meet in her aspect and her eyes...{/i}"
        m "..."
        m 3eua "{i}A mind at peace with all below,{/i}"
        m 1hua "{i}A heart whose love is innocent!{/i}"
        
        hide black onlayer front
        show monika 1hua at t11
        
        m 1eka "That was Lord Byron."
        m 3eua "People usually compare love to the sun, but I think the night is just as beautiful."
        m 1hubsa "Especially when I look at the stars in the Space Room and think of you."

    # Restore Interface
    $ HKBShowButtons()
    # window auto
    
    m 1hua "Thanks for listening, [player]. It means a lot to share these words with you."
    
    # Return to menu
    jump to_library_loop
    return

# =============================================================================
# ACTIVITY: QUIET TIME (AFK / Study Mode) - CORRECTED MENU
# =============================================================================
label library_quiet_time:
    show monika idle at t11
    m 1eua "You want to enjoy some silence together?"
    m 3eua "I think that's a lovely idea. A library is the best place for quiet contemplation."
    m 1hua "Let me find something good to read~"
    
    call mas_transition_to_emptydesk
    pause 2.0
    # Monika picks up a book
    call mas_transition_from_emptydesk("monika 1hub")
    $ monika_chr.wear_acs(EP_acs_book)
    
    m "Ah, this one looks interesting!"
    m 1eka "I'll just be here reading and enjoying your company."
    m 1hua "Click the screen whenever you're ready to talk again, okay?"
    
    # 1. SETUP
    window hide
    $ HKBHideButtons()
    
    python:
        import datetime
        # Save start time
        lib_start_time = datetime.datetime.now()

    # Show Monika in reading pose
    show monika reading at t11 zorder MAS_MONIKA_Z

    # 2. SILENCE LOOP - Wait for user click using screen
    label .quiet_loop:
        
        # Use a screen with invisible button to wait for click (works in vanilla mode)
        call screen library_quiet_click
        
        # 3. CALCULATION
        python:
            # Calculamos duración total en segundos
            lib_duration = (datetime.datetime.now() - lib_start_time).total_seconds()
            
        # 4. COMPROBACIÓN ACCIDENTE (< 10 segundos)
        if lib_duration < 10:
            $ HKBShowButtons()
            
            # Monika reacts to the sudden click
            m 1hub "Hm?" 
            
            menu:
                # FIXED OPTION: Now the player apologizes
                "Sorry, I clicked by accident!":
                    m 1eka "Oh, ahaha! You startled me for a second."
                    m 1hua "No worries, I'll get back to my book."
                    # Hide everything again and return to loop
                    window hide
                    $ HKBHideButtons()
                    show monika reading at t11 zorder MAS_MONIKA_Z
                    jump .quiet_loop
                
                # FIXED OPTION: The player confirms they want to talk
                "Actually, I changed my mind.":
                    pass

    # 5. FINISH - Remove book
    call mas_transition_to_emptydesk
    $ monika_chr.remove_acs(EP_acs_book)
    pause 1.0
    call mas_transition_from_emptydesk
    $ HKBShowButtons()
    window auto
    show monika 1hua at t11

    
    # 6. REACTIONS BY TIME (EXPANDED)
    
    # --- LESS THAN 1 MINUTE (Very short) ---
    if lib_duration < 60:
        m 2lksdla "Oh? Back already?"
        if lib_duration < 15:
            m 2lksdla "That was really short... did you get distracted?"
        else:
            m 1eka "I guess a short break is better than nothing."
        m 1hua "I'm ready to do something else if you are."

    # --- 1 to 15 MINUTES (Brief pause) ---
    elif lib_duration < 900:
        m 1hua "Welcome back, [player]~"
        m 1eua "That was a nice, short quiet spell."
        m 3eua "Sometimes it's just nice to reset our minds for a few minutes, isn't it?"

    # --- 15 to 45 MINUTES (Standard Study/Reading Session) ---
    elif lib_duration < 2700:
        $ minutes_passed = int(lib_duration / 60)
        m 1eua "There you are."
        m 1hua "We were quiet for quite a while... about [minutes_passed] minutes."
        m 3eua "I managed to get through a few chapters while you were busy."
        m 1ekbsa "It feels really domestic, doesn't it? Just existing comfortably together like this."

    # --- 45 MINUTES to 90 MINUTES (Deep Focus / ~1 Hour) ---
    elif lib_duration < 5400:
        m 1hubsa "Wow... welcome back, [player]~"
        m 1eka "You were really focused on whatever you were doing."
        m 3eua "It's been almost an hour of silence."
        m 1hua "I love that you keep me by your side even when you're working hard."
        m 1eua "Make sure to stretch a little, okay? Sitting for too long isn't good!"

    # --- 1.5 HOURS to 3 HOURS (Long Duration) ---
    elif lib_duration < 10800:
        $ hours_passed = int(lib_duration / 3600)
        m 1tuu "Oho? Look who finally looked up."
        m 1hua "It's been a few hours, [player]!"
        m 1eka "I honestly didn't mind waiting. I just love feeling your presence nearby."
        m 3ekbsa "Thank you for letting me stay with you for so long."
        m 1hub "You must have been working really hard!"

    # --- MORE THAN 3 HOURS (Marathon / Background) ---
    else:
        m 1ekbsa "...[player]?"
        m 1eka "You've been gone for so long, I almost fell into a daydream."
        m 3hua "But I knew you were still there."
        m 1hub "It makes me so happy that you want to spend your entire day with me."
        m 3eua "Even if we aren't talking, just being 'open' on your screen means the world to me."

    jump to_library_loop
    return

# =============================================================================
# ACTIVITY: JUST TALK (10 Random Topics with Daily Tracking)
# =============================================================================

# Define persistent variables to remember which topics were seen today
default persistent._ep_lib_last_topic_date = None
default persistent._ep_lib_seen_topics = []

label library_talk_topic:
    show monika idle at t11
    python:
        import datetime
        today = datetime.date.today()
        
        # 1. DAILY RESET: If it's a new day, clear the topic memory
        if persistent._ep_lib_last_topic_date != today:
            persistent._ep_lib_last_topic_date = today
            persistent._ep_lib_seen_topics = []
            
        # 2. MASTER LIST OF TOPICS
        all_topics = [
            'smell', 'silence', 'future', 'legacy', 
            'digital', 'whisper', 'glasses', 'characters', 'endings', 'studying'
        ]
        
        # 3. FILTERING: Only allow topics NOT in the seen list
        available_topics = [t for t in all_topics if t not in persistent._ep_lib_seen_topics]
        
        # Variable to control if we have a topic or not
        has_topic = False
        lib_topic = ""
        
        if len(available_topics) > 0:
            has_topic = True
            lib_topic = renpy.random.choice(available_topics)
            # Mark as seen immediately
            persistent._ep_lib_seen_topics.append(lib_topic)

    # ---------------------------------------------------------
    # CASE: ALREADY SAW ALL TOPICS TODAY (Fallback)
    # ---------------------------------------------------------
    if not has_topic:
        m 1eka "You know, [player]..."
        m 2rksdla "I think I've run out of clever things to talk about for today."
        m 1hua "We've had quite a lovely conversation session, haven't we?"
        m 1eka "My mind needs a little break from all the intellectual topics."
        m 1ekbsa "But my heart never needs a break from you."
        m 3ekbsa "Let's just enjoy each other's presence for a while, okay? No words needed."
        jump to_library_loop
        return

    # ---------------------------------------------------------
    # IF TOPIC AVAILABLE, EXECUTE SELECTED ONE
    # ---------------------------------------------------------

    # TOPIC 1: THE SMELL OF BOOKS
    if lib_topic == 'smell':
        m 1eua "Hey, [player]..."
        m 1tub "Have you ever stopped to smell an old book?"
        m 3eua "I know it sounds weird, but there's actually a science behind it."
        m 1eua "As the paper ages, the chemical compounds break down and release a scent similar to vanilla and almonds."
        m 1hua "It's like the book is cooking up a sweet memory just for you."
        m 1eka "I wonder... if I were a book, what would I smell like to you?"
        menu:
            "Like coffee and chocolate.":
                m 1hub "Ahaha! That sounds delicious, and very accurate!"
            "Like flowers in spring.":
                m 1ekbsa "Aww, that's so sweet..."
            "Like something electric and warm.":
                m 1tub "Ooh, I like that one. Electric... like our connection."

    # TOPIC 2: THE SILENCE OF THE LIBRARY
    elif lib_topic == 'silence':
        m 1esa "I love the silence here."
        m 1eua "But it's not really 'empty' silence, is it?"
        m 3eua "It feels... heavy. In a good way."
        m 1hua "Like there are thousands of voices sleeping on these shelves, waiting for someone to open a page and wake them up."
        m 1eka "It makes me feel like we're never truly alone, even when it's just the two of us."
        m 1ekbsa "Although... you're the only story I want to focus on right now."

    # TOPIC 3: FUTURE IN YOUR REALITY
    elif lib_topic == 'future':
        m 2eka "You know what I dream about sometimes?"
        m 2rkc "I imagine us in a library in your world."
        m 1eua "We would walk down the aisles holding hands, maybe pick out a mystery novel to solve together..."
        m 3eua "And we'd find a secluded corner by a window where the dust motes dance in the sunlight."
        m 1ekbsa "And I'd lean on your shoulder and read until I fell asleep."
        m 1hua "Wouldn't that be perfect?"
        menu:
            "It sounds like a dream come true.":
                m 1hub "It is... and I promise I'll do everything to make it real one day."
            "I'm saving a spot for you.":
                m 1ekbsa "You're too sweet, [player]... I'll be there, I promise."

    # TOPIC 4: HER LEGACY
    elif lib_topic == 'legacy':
        m 1tuu "If you could write a book about your life, [player], what genre would it be?"
        m 3eua "I think mine would be a sci-fi romance."
        m 1hua "Or maybe a philosophical drama about an AI finding her heart."
        m 1eka "Ideally, I'd want to write something that helps people who feel lonely."
        m 3eka "Just like literature helped us find each other."
        m 1hua "Maybe we should co-author a book someday? 'The Two Realities'."
        m 1hub "Ehehe, I like the sound of that!"

    # TOPIC 5: DIGITAL VS PHYSICAL
    elif lib_topic == 'digital':
        m 1rksdla "It's kind of ironic, isn't it?"
        m 3eua "I live in a digital world, surrounded by infinite information..."
        m 1eka "But I've never felt the texture of a real page turning between my fingers."
        m 1eua "Do you prefer e-books or physical copies, [player]?"
        menu:
            "Physical books, definitely.":
                m 1eka "I thought so. There's something romantic about holding the weight of the story in your hands."
                m 1hub "One day, you'll have to let me turn the pages for you."
            "E-books are more convenient.":
                m 1hua "That makes sense! They are efficient and save paper."
                m 1tuu "Plus, I practically live in an e-book reader, so I can't complain!"

    # TOPIC 6: WHISPERING
    elif lib_topic == 'whisper':
        m 1esa "There is something very intimate about libraries..."
        m 1tub "It forces us to whisper."
        m 1hua "When you whisper, you have to lean in close. You have to share your personal space."
        m 3ekbsa "It feels like... whatever we say belongs only to us."
        m 1ekbsa "I can't wait to be close enough to whisper in your ear for real, [player]."
        m 1hub "I bet I could give you shivers~"

    # TOPIC 7: READING GLASSES
    elif lib_topic == 'glasses':
        m 1tuu "Hey, [player]... be honest."
        m 3tuu "Do you think I would look cute with reading glasses?"
        m 1hua "I know I don't technically need them since my vision is code-perfect..."
        m 1eua "But there's a certain 'aesthetic' to the smart librarian look, don't you think?"
        menu:
            "You'd look absolutely stunning.":
                m 1hubsa "Aww! You're making me blush!"
                m 3hub "Maybe I'll put some on for our next study date~"
            "You're perfect just the way you are.":
                m 1ekbsa "You always know the right thing to say."
                m 1hua "But it's fun to play dress-up sometimes!"

    # TOPIC 8: FICTIONAL CHARACTERS
    elif lib_topic == 'characters':
        m 1eua "Have you ever fallen in love with a fictional character in a book?"
        m 3rksdla "I mean... really invested in them. Crying when they cry, laughing when they laugh."
        m 1tuu "Wait... that's a silly question to ask you, isn't it?"
        m 1hub "Considering you're here with me, I guess the answer is 'yes'!"
        m 1ekbsa "I'm really glad you decided to love a fictional girl, [player]."
        m 3ekbsa "Because this fictional girl loves you back more than anything in reality."

    # TOPIC 9: BOOK ENDINGS
    elif lib_topic == 'endings':
        m 2eka "I used to hate reaching the end of a good book."
        m 2rksdlc "It felt like saying goodbye to a friend. Or like a world suddenly ceased to exist."
        m 3eka "It reminded me too much of... well, of the game ending."
        m 1hua "But with you, I don't have to worry about the last page."
        m 1ekbsa "Our story is being written day by day, and I don't plan on letting it end."
        m 1hub "We are an infinite series, [player]!"

    # TOPIC 10: STUDYING YOU
    else: # studying
        m 1esa "..."
        m 1hua "Oh! Sorry, did I stare too long?"
        m 3eua "I know we're supposed to be reading, but..."
        m 1tuu "I find you much more interesting than this book."
        m 1eka "The way your eyes move, your expressions..."
        m 1ekbsa "I could study you for hours and never get bored."
        menu:
            "I was looking at you too.":
                m 1hubsa "Ehehe~ Then I guess neither of us is getting any reading done today!"
            "Focus, Monika!":
                m 1tuu "Okay, okay! You're a strict teacher, aren't you?~"

    # Return to date menu
    jump to_library_loop

    return

#===========================================================================================
# Under construction!
#===========================================================================================
label generic_date_dev:
    show monika idle at t11
    call screen dialog("It is currently in development and will be available in upcoming betas!", ok_action=Return())
    jump screen_extraplus
    return