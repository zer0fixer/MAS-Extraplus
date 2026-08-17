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

default persistent._extraplusr_hasplayergoneonanniversary = False

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
    python:
        store.ep_tools.manage_date_location()
        store.ep_tools.check_seen_background("gtpool", "gtpoolv2", "pool_sorry_player")

label gtpool:
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()

    if _ep_special_day == "anni":
        m 3sub "The pool? On our anniversary?"
        m 1hubsa "That's such a fun and romantic idea, [player]!"
        m 1ekbsa "Fresh air, sunshine, and us... I love it already~"
        m 1hubsb "Let's go!"

    elif _ep_special_day == "moni_bday":
        m 3sub "The pool? On my birthday?"
        m 1hubsa "That's so sweet of you, [player]!"
        m 1ekbsa "A birthday swim... I could get used to that~"
        m 1hubsb "Let's go!"

    elif _ep_special_day == "player_bday":
        m 3sub "The pool? On your special day?"
        m 1hub "I'm so happy you want to spend part of your birthday there!"
        m 1eka "A refreshing swim is a great way to celebrate, don't you think?"
        m 1hubsb "Let's go, birthday [player]~"

    else:
        if mas_isDayNow():
            m 3sub "You want to go to the pool?"
            m 3hub "That sounds wonderful, [player]!"
            m 1eubsa "A nice day for a swim and some time together~"
            m 1hubsb "Okay, let's go, [mas_get_player_nickname()]~"
        else:
            m 3sub "Oh, you want to go to the pool at this hour?"
            m 3hub "A night swim? How romantic!"
            m 1eubsa "There's something magical about the water at night~"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"

    jump extra_pool_init
    return

label gtpoolv2:
    show monika 1eua at t11
    $ _ep_special_day = store.ep_tools.getSpecialDayType()

    if _ep_special_day == "anni":
        m 3wub "Back to the pool? For our anniversary?"
        m 2hub "I love that this is becoming one of our things, [player]!"
        m 2eubsa "Fresh water, open sky, and you... it's perfect every time."
        m 1hubsb "Let's go, [mas_get_player_nickname()]~"

    elif _ep_special_day == "moni_bday":
        m 3wub "The pool again? On my birthday?"
        m 1hubsa "You really know what I like, [player]~"
        m 1ekbsa "More splashing, more sunshine... let's do it!"
        m 1hubsb "Let's go!"

    elif _ep_special_day == "player_bday":
        m 3wub "Back to the pool on your birthday?"
        m 1hub "I'm glad you enjoyed it enough to want to go back!"
        m 1ekbsa "Let's make some more birthday memories~"
        m 1hubsb "Let's go!"

    else:
        if mas_isDayNow():
            m 3wub "You want to go to the pool again?"
            m 2hub "I had such a great time last time we went!"
            m 2eubsa "I'm really glad you keep taking me there, [player]~"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"
        else:
            m 3wub "Another night swim?"
            m 2hub "The last time was so peaceful... just us and the water."
            m 2eubsa "I can't wait to feel that again~"
            m 1hubsb "Let's go, [mas_get_player_nickname()]~"

    jump extra_pool_init
    return

label pool_sorry_player:
    show monika idle at t11
    m 1ekd "I'm so sorry, [player]."
    $ _ep_special_day = store.ep_tools.getSpecialDayType()
    if _ep_special_day == "anni":
        m 3eka "I know you really wanted to take me to the pool for our anniversary."
    elif _ep_special_day == "moni_bday":
        m 3eka "I know you wanted to take me there for my birthday."
    elif _ep_special_day == "player_bday":
        m 3eka "I know you wanted to go there on your special day."
    else:
        m 3eka "I know you really wanted to take me to the pool."
    m 1ekc "I don't think I'm ready for that kind of outing just yet."
    m 3lka "I want to make sure I can handle it properly before we go~"
    m 1eua "Maybe another time, [player]. I promise I'll get us there."
    jump screen_extraplus
    return

label skip_pool_exit:
    show monika idle at t11_float
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    call extra_restore_bg("extra_comment_pool")
    return

label extra_comment_pool:
    show monika 1eua at t11

    if _ep_pool_retreated_to_shelter:
        if _ep_pool_shelter_reason == "thunder":
            m 1eka "It's good to be safely back home in our room, [player]~"
            m 1ekc "That thunderstorm out at the pool was pretty intense for a moment..."
            m 1ekbsa "But waiting it out together with you in the shelter made me feel completely safe."
            m 1hubsa "Thank you for looking after me and keeping me safe today~"
        elif _ep_pool_shelter_reason == "snow":
            m 1eka "Phew, back in the warmth of our room~"
            m 1eua "Who would have thought it would start snowing while we were at the pool?"
            m 1hubsa "Still, curling up together in our shelter room was such a sweet and memorable moment with you, [player]~"
            m 1ekbsa "Thank you for always taking such good care of me!"
        else:
            m 1eka "Ah, we're finally back in our room~"
            m 1eua "Too bad the weather turned on us while we were at the pool today..."
            m 1ekbsa "But honestly, taking shelter and listening to the rain with you was so cozy and special."
            m 1hubsa "No matter what the weather is doing outside, as long as I'm with you, every moment is wonderful~"

    elif mas_isDayNow():
        m 1hua "Ah, back in our room~"
        m 1hub "I had so much fun at the pool today, [player]!"
        m 1eubsa "The water, the sunshine, and spending that time with you was so refreshing."
        if _ep_pool_sunscreen_applied:
            m 1hubsa "And thanks again for helping me with sunscreen earlier, you're the sweetest~"
        else:
            m 1ekbsa "Thank you for taking me out today, [player]~ I love having these special moments with you."

    else:
        m 1hua "Back home in our room~"
        m 1dubsa "That night swim was so peaceful and romantic, [player]..."
        m 1ekbsa "Just drifting in the quiet water under the stars with you... I'll never forget it."
        m 1hubsa "Thank you for such a wonderful date tonight~"

    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#===========================================================================================
# POOL — PYTHON HELPERS
#===========================================================================================

#==============================================================================
# 1. SWIMSUIT DETECTION & AUTO-CHANGE
#==============================================================================
init -5 python in ep_pool:
    import store

    # Keywords checked against lowercase clothing name
    SWIM_NAME_KEYWORDS = ("swim", "bikini", "bath", "towel")

    def _is_swimwear_by_name(name):
        """Check if clothing name contains swim-related keywords."""
        if not name:
            return False
        lname = name.lower()
        for kw in SWIM_NAME_KEYWORDS:
            if kw in lname:
                return True
        return False

    def is_swimwear(clothes_obj):
        """
        Check if a MASClothes object qualifies as swimwear.

        Checks (in order):
            1. Name keywords (covers spritepacks without exprops)
            2. MAS exprops: EXP_C_WET or EXP_C_LING (covers standard spritepacks)

        Returns True if swimwear, False otherwise.
        """
        if clothes_obj is None:
            return False

        if _is_swimwear_by_name(clothes_obj.name):
            return True

        try:
            if clothes_obj.hasprop(store.mas_sprites.EXP_C_WET):
                return True
            if clothes_obj.hasprop(store.mas_sprites.EXP_C_LING):
                return True
        except Exception:
            pass

        return False

    def get_unlocked_swimwear():
        """
        Returns list of unlocked MASClothes objects that qualify as swimwear.
        Uses mas_selspr.CLOTH_SEL_SL to check unlock status.
        """
        result = []
        try:
            for sel in store.mas_selspr.CLOTH_SEL_SL:
                if not getattr(sel, "unlocked", False):
                    continue
                cloth = store.mas_sprites.CLOTH_MAP.get(sel.name)
                if cloth and is_swimwear(cloth):
                    result.append(cloth)
        except Exception:
            pass
        return result

    def has_unlocked_swimwear():
        """True if player has at least one swimwear outfit unlocked."""
        return len(get_unlocked_swimwear()) > 0

    def pick_swimwear():
        """
        Select the best swimwear from player's unlocked collection.

        Priority order:
            1. Name contains "bikini"
            2. Name contains "swim"
            3. Has EXP_C_WET prop
            4. Name contains "bath" or "towel"
            5. Has EXP_C_LING prop
            6. First available

        Returns MASClothes object or None.
        """
        options = get_unlocked_swimwear()
        if not options:
            return None

        for c in options:
            if "bikini" in c.name.lower():
                return c
        for c in options:
            if "swim" in c.name.lower():
                return c
        for c in options:
            try:
                if c.hasprop(store.mas_sprites.EXP_C_WET):
                    return c
            except Exception:
                pass
        for c in options:
            lname = c.name.lower()
            if "bath" in lname or "towel" in lname:
                return c
        for c in options:
            try:
                if c.hasprop(store.mas_sprites.EXP_C_LING):
                    return c
            except Exception:
                pass

        return options[0]

    def get_swimwear_display_name(clothes_obj):
        """Get a user-friendly name for the swimwear item."""
        try:
            for sel in store.mas_selspr.CLOTH_SEL_SL:
                if sel.name == clothes_obj.name:
                    return sel.display_name
        except Exception:
            pass
        return clothes_obj.name.replace("_", " ").title()

    def is_currently_wearing_swimwear():
        """True if Monika's current outfit is swimwear."""
        try:
            return is_swimwear(store.monika_chr.clothes)
        except Exception:
            return False

    def change_into_swimwear():
        """
        Save current outfit and change into swimwear.

        Returns:
            (changed, clothes_obj) tuple:
                - changed: True if outfit was changed, False otherwise
                - clothes_obj: the MASClothes used, or None
        """
        if is_currently_wearing_swimwear():
            store.persistent._ep_pool_changed_into_swim = False
            return (False, None)

        swimsuit = pick_swimwear()
        if swimsuit is None:
            store.persistent._ep_pool_changed_into_swim = False
            return (False, None)

        store.persistent._ep_pool_saved_outfit = store.monika_chr.save_state(
            True, True, True, as_prims=True
        )
        store.persistent._ep_pool_changed_into_swim = True
        store.monika_chr.change_clothes(swimsuit, by_user=False)
        return (True, swimsuit)

    def restore_outfit_if_changed():
        """
        Restore the saved outfit if pool date auto-changed Monika's clothes.
        Safe to call even without prior change (no-op).

        Returns True if restore was performed, False otherwise.
        """
        if not store.persistent._ep_pool_changed_into_swim:
            return False

        saved = store.persistent._ep_pool_saved_outfit
        if saved:
            try:
                store.monika_chr.restore(saved, as_prims=True)
            except Exception:
                pass

        store.persistent._ep_pool_saved_outfit = None
        store.persistent._ep_pool_changed_into_swim = False
        return True

    def play_pool_ambient():
        """Play appropriate pool ambient loop depending on day/night."""
        try:
            if store.mas_isNightNow():
                sfx_file = store.sfx_pool_night_ambience
            else:
                sfx_file = store.sfx_pool_day_ambience

            if sfx_file:
                renpy.music.play(sfx_file, channel="ep_ambient", loop=True, fadein=2.0)
        except Exception:
            pass

    def stop_pool_ambient(fadeout=1.5):
        """Stop the pool ambient sound loop."""
        try:
            renpy.music.stop(channel="ep_ambient", fadeout=fadeout)
        except Exception:
            pass

#==============================================================================
# 2. SUNSCREEN MINIGAME
#==============================================================================
#==============================================================================
# POOL — INTERACTIVE SUNSCREEN MINIGAME
#==============================================================================
init -5 python in ep_sunscreen:
    import store
    import pygame

    # 4 distinct interactive body zones on Monika's sprite:
    # Coordinated for Monika's pose in t11 / t11_float at default zoom (zl=3)
    SUNSCREEN_ZONES_MAP = {
        "neck": [
            (570, 275), (710, 275), (710, 355), (570, 355)
        ],
        "left_shoulder": [
            (420, 345), (535, 345), (535, 435), (420, 435)
        ],
        "right_shoulder": [
            (745, 345), (860, 345), (860, 435), (745, 435)
        ],
        "back": [
            (545, 355), (735, 355), (735, 465), (545, 465)
        ],
    }

    ZONE_DISPLAY = {
        "neck": _("Neck & Shoulders"),
        "left_shoulder": _("Left Shoulder"),
        "right_shoulder": _("Right Shoulder"),
        "back": _("Upper Back"),
    }

    ZONE_EXP = {
        "neck": "2ekbsa",
        "left_shoulder": "2eubsa",
        "right_shoulder": "2hubsa",
        "back": "2dubsa",
    }

    ZONE_FEEDBACK = {
        "neck": ["*Neck*", "*Shoulders*"],
        "left_shoulder": ["*Left Shoulder*", "*Shoulder*"],
        "right_shoulder": ["*Right Shoulder*", "*Shoulder*"],
        "back": ["*Upper Back*", "*Back*"],
    }

    ZONES_KEYS = ["neck", "left_shoulder", "right_shoulder", "back"]

    class EPSunscreenManager(object):
        """
        Specialized interaction manager for applying sunscreen to Monika's sprite.
        Uses EPClickZone / EPClickZoneManager without modifying core boop manager.
        """
        def __init__(self):
            self.zones_applied = {
                "neck": False,
                "left_shoulder": False,
                "right_shoulder": False,
                "back": False,
            }
            self.total_zones = len(self.zones_applied)
            self._zones_enabled = True

            try:
                self.cz_manager = store.ep_interactions.EPClickZoneManager()
                for zone_key, vx_list in SUNSCREEN_ZONES_MAP.items():
                    self.cz_manager.add(zone_key, store.EPClickZone(vx_list))

                self.interactable = store.ep_interactions.EPZoomableInteractable(
                    self.cz_manager,
                    zone_actions={},
                    debug=False
                )
            except (AttributeError, NameError, TypeError):
                self._zones_enabled = False
                self.cz_manager = None
                self.interactable = None

        def reset(self):
            for k in self.zones_applied:
                self.zones_applied[k] = False
            if self.cz_manager:
                for k in self.zones_applied:
                    self.cz_manager.set_disabled(k, False)
            renpy.restart_interaction()

        def is_done(self):
            return all(self.zones_applied.values())

        def get_done_count(self):
            return sum(1 for v in self.zones_applied.values() if v)

        def get_hovered_zone(self):
            if not self._zones_enabled or self.interactable is None:
                return None
            x, y = renpy.get_mouse_pos()
            return self.interactable.check_over(x, y)

        def handle_click(self, zone_key=None):
            if not zone_key:
                zone_key = self.get_hovered_zone()

            if not zone_key or zone_key not in self.zones_applied:
                return

            if self.zones_applied[zone_key]:
                renpy.play(store.sfx_lotion_apply, channel="sound")
                show_sunscreen_sparkles()
                return

            self.zones_applied[zone_key] = True
            if self.cz_manager:
                self.cz_manager.set_disabled(zone_key, True)

            renpy.play(store.sfx_lotion_apply, channel="sound")
            show_sunscreen_sparkles()

            exp = ZONE_EXP.get(zone_key, "2hua")
            renpy.show("monika " + exp)

            renpy.restart_interaction()

    def show_sunscreen_sparkles():
        mouse_pos = renpy.get_mouse_pos()
        t = "sparkle_burst_{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("extra_sunscreen_sparkles", pos_x=mouse_pos[0], pos_y=mouse_pos[1], tag=t, _tag=t)

    # Global instance for screen use
    manager = EPSunscreenManager()


#==============================================================================
# SUNSCREEN SPARKLE BURST VFX
#==============================================================================
transform ep_sparkle_burst_trans(target_x, target_y, rot_deg=0):
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    zoom 0.3
    offset (0, 0)
    rotate 0

    parallel:
        easein 0.10 alpha 1.0
        pause 0.15
        easeout 0.45 alpha 0.0
    parallel:
        easeout 0.6 offset (target_x, target_y)
    parallel:
        easein 0.10 zoom 1.25
        easeout 0.50 zoom 0.55
    parallel:
        easeout 0.6 rotate rot_deg


screen extra_sunscreen_sparkles(pos_x, pos_y, tag):
    zorder 2000
    timer 0.75 action Hide(tag)

    for dx, dy, s, rot, col in [
        (-48, -40, 36,  25, "#FFBDEE"),
        ( 48, -44, 40, -30, "#FFFFFF"),
        (-60,   5, 32,  45, "#FF69B4"),
        ( 62,   0, 38, -45, "#FFBDEE"),
        (-24, -62, 42, -15, "#FFFFFF"),
        ( 26, -58, 34,  35, "#FFBDEE"),
        (  0, -48, 48,   0, "#FFFFFF"),
        (  0,  -8, 30,  10, "#FF69B4"),
    ]:
        text "*" at ep_sparkle_burst_trans(dx, dy, rot):
            pos (pos_x, pos_y)
            size s
            color col
            outlines [(1, "#000000", 0, 0)]
            font "mod_assets/font/m1_fixed.ttf"


#==============================================================================
# SUNSCREEN SCREEN (Immersive Sprite-Touch Interaction)
#==============================================================================
screen extra_sunscreen():
    modal True
    zorder 100
    tag extra_sunscreen

    key "K_SPACE"     action NullAction()
    key "K_RETURN"    action NullAction()
    key "K_KP_ENTER"  action NullAction()
    key "mouseup_3"   action NullAction()

    # Fullscreen transparent blocker to catch stray clicks
    button:
        xysize (config.screen_width, config.screen_height)
        background Solid("#00000000")
        action NullAction()

    python:
        _mgr = store.ep_sunscreen.manager
        _current_zoom = store.mas_sprites.zoom_level
        _zone_rects = {}
        if _mgr._zones_enabled and _mgr.cz_manager:
            for _zk in store.ep_sunscreen.ZONES_KEYS:
                _cz = _mgr.cz_manager.get(_zk, _current_zoom)
                if _cz and _cz.corners:
                    _min_x = min(x for x, y in _cz.corners)
                    _min_y = min(y for x, y in _cz.corners)
                    _max_x = max(x for x, y in _cz.corners)
                    _max_y = max(y for x, y in _cz.corners)
                    _zone_rects[_zk] = {
                        'x': _min_x,
                        'y': _min_y,
                        'w': _max_x - _min_x,
                        'h': _max_y - _min_y,
                    }
        _is_all_done = _mgr.is_done()
        _done_count = _mgr.get_done_count()
        _total_count = _mgr.total_zones

    # Interactive zone buttons over Monika
    for _zk, _zdata in _zone_rects.items():
        python:
            _applied = _mgr.zones_applied.get(_zk, False)
            if _applied:
                _btn_idle = Solid("#00000000")
                _btn_hover = Solid("#FFFFFF22")
            else:
                _btn_idle = Solid("#00000000")
                _btn_hover = Solid("#FF69B433")

        button:
            xpos _zdata['x']
            ypos _zdata['y']
            xysize (_zdata['w'], _zdata['h'])
            background _btn_idle
            hover_background _btn_hover
            action Function(_mgr.handle_click, _zk)

    # Top Status Bar (Extra+ / MAS Styled Floating Card)
    frame:
        xalign 0.5
        ypos 20
        background Solid("#000000B3")
        padding (24, 12)

        vbox:
            spacing 8
            xalign 0.5

            if _is_all_done:
                text _("Monika is protected from the sun!"):
                    size 20
                    bold True
                    color "#FFBDEE"
                    outlines [(1, "#000000", 0, 0)]
                    xalign 0.5
            else:
                text _("Apply Sunscreen - [_done_count]/[_total_count] Areas Covered"):
                    size 20
                    bold True
                    color "#FFFFFF"
                    outlines [(1, "#000000", 0, 0)]
                    xalign 0.5

            hbox:
                spacing 10
                xalign 0.5
                for _zk in store.ep_sunscreen.ZONES_KEYS:
                    python:
                        _zk_applied = _mgr.zones_applied.get(_zk, False)
                        _zk_name = store.ep_sunscreen.ZONE_DISPLAY.get(_zk, _zk)
                        if _zk_applied:
                            _badge_bg = Solid("#FF69B44D")
                            _badge_txt = "+ " + _zk_name
                            _badge_clr = "#FFBDEE"
                        else:
                            _badge_bg = Solid("#00000066")
                            _badge_txt = "- " + _zk_name
                            _badge_clr = "#B0B0B0"

                    frame:
                        background _badge_bg
                        padding (10, 4)
                        text "[_badge_txt]":
                            size 13
                            bold True
                            color _badge_clr
                            outlines [(1, "#000000", 0, 0)]

    # Bottom Action Bar
    if _is_all_done:
        vbox:
            xalign 0.5
            ypos 0.88
            style_prefix "hkb"
            textbutton _("Finish"):
                action Return("done")
                xsize 200
    else:
        frame:
            xalign 0.5
            ypos 0.90
            background Solid("#000000B3")
            padding (18, 8)
            text _("Click or tap on Monika's shoulders, neck, and back"):
                size 16
                color "#FFFFFF"
                outlines [(1, "#000000", 0, 0)]
                xalign 0.5


label ep_sunscreen_start:
    show monika 2eua at t11_float
    python:
        store.ep_sunscreen.manager.reset()
    call screen extra_sunscreen
    $ _sunscreen_res = _return

    if _sunscreen_res == "done":
        jump pool_sunscreen_after
    else:
        m 2hua "No problem, we can do it later if you want~"
        jump to_pool_loop


#===========================================================================================
# POOL DIALOGUES
#===========================================================================================

label extra_pool_talk_water:
    show monika idle at t11_float

    if store.mas_isNightNow():
        $ _water_n = renpy.random.randint(1, 3)
        if _water_n == 1:
            m 1dkbsa "Look at the water right now..."
            m 1ekbsa "The light reflects off the surface and it looks almost silver."
            m 1dubsa "I could stare at it for hours, honestly."
            m 1hua "It's one of those things that just... makes me feel peaceful~"
        elif _water_n == 2:
            m 1eka "Have you ever noticed how water sounds different at night?"
            m 1dsa "Softer, somehow. Less busy."
            m 1ekbsa "Like even the pool is winding down~"
            m 1hua "I like it."
        else:
            m 1dubsa "The water at night always makes me feel a little nostalgic."
            m 1dsa "I'm not sure why. Maybe it's the stillness."
            m 1ekbsa "Like time slows down when it's dark and quiet like this."
            m 3hua "I'm glad we're here together~"

    elif store.mas_current_weather == store.mas_weather_overcast:
        $ _water_ov = renpy.random.randint(1, 2)
        if _water_ov == 1:
            m 1eka "The water looks a little different when it's overcast like this..."
            m 1dua "Like it's reflecting the clouds. All silver and grey."
            m 1eua "I actually find it kind of beautiful? In a quiet way."
            m 1hua "Peaceful~"
        else:
            m 1eua "The pool has a different vibe on cloudy days."
            m 1dsa "Less sparkly, more... still."
            m 1ekbsa "Like the whole world is taking a breath."
            m 3hubsa "I think I prefer it~"

    else:
        $ _water_d = renpy.random.randint(1, 3)
        if _water_d == 1:
            m 1eub "The water looks so clear today, doesn't it?"
            m 1hub "When I look down, I can see all the way to the bottom!"
            m 1hua "There's something so satisfying about perfectly clear water~"
            m 1eua "It's almost like it's inviting us in."
        elif _water_d == 2:
            m 1sub "I love how the sunlight dances on the water~"
            m 1eua "Those little sparkles on the surface..."
            m 1dsa "I wrote a poem about that once, actually."
            m 3hua "Maybe I'll show you sometime~"
        else:
            m 1eka "The water temperature is just right today, don't you think?"
            m 1eua "Not too cold, not too warm — the kind that just wraps around you."
            m 1hub "It's one of those small pleasures that makes me really grateful~"

    jump to_pool_loop
    return


label extra_pool_talk_swim:
    show monika idle at t11_float

    if mas_isMoniEnamored(higher=True):
        $ _swim_en = renpy.random.randint(1, 2)
        if _swim_en == 1:
            m 1eua "You know, I've always loved swimming."
            m 1dkbsa "There's something about floating that makes you feel weightless... free."
            m 1ekbsa "But honestly? I think what I love most is imagining swimming with you."
            m 1dubsa "Side by side, just the two of us in the water..."
            m 1hubsa "Someday, [player]. I really believe that."
        else:
            m 1eua "Do I like to swim?"
            m 1hua "I love it~"
            m 1dubsa "But I think I'd love it even more if you were actually here."
            m 1ekbsa "Splashing around, racing across the pool..."
            m 1dkbsa "Just... being with you. In the water. For real."
            m 1hubsa "That's something I look forward to a lot."
    else:
        $ _swim_reg = renpy.random.randint(1, 3)
        if _swim_reg == 1:
            m 1eua "I've always enjoyed swimming."
            m 1hua "It's so peaceful to just float and let everything else drift away."
            m 1tua "It feels like you're in your own little world, just you and the water."
            m 1hub "Maybe when I get to your reality, we can go for a real swim together sometime!"
        elif _swim_reg == 2:
            m 1eua "Oh, definitely. Swimming is one of my favorite things."
            m 1dua "There's a kind of freedom in it, you know? Like nothing can weigh you down."
            m 1eka "I'd love to teach you some technique someday~"
            m 3hua "If you need a teacher, I'm available~"
        else:
            m 1eub "Swimming? Yes, I really do."
            m 1hua "There's something meditative about it."
            m 1eua "When you find your rhythm in the water, your mind just... quiets."
            m 1ekbsa "I think that's why I love it. It's one of the few times I'm just... present."

    jump to_pool_loop
    return


label extra_pool_talk_relax:
    show monika idle at t11_float

    $ _relax_r = renpy.random.randint(1, 3)
    if _relax_r == 1:
        m 1ekbsa "I agree."
        m 1dubsa "Just sitting here by the water with you... all the noise in my head just fades."
        m 1ekbsa "It's moments like these I treasure the most."
        m 1hua "Thank you for bringing me here, [player]~"
    elif _relax_r == 2:
        m 1eka "Right?"
        m 1dsa "There's something about water that's just... inherently calming."
        m 1eua "I read once that the sound of moving water slows your heart rate."
        m 1ekbsa "Whether that's true or not, I believe it right now~"
    else:
        m 1eua "Yeah. This is nice."
        m 1dkbsa "I don't always need to be doing something, you know?"
        m 1ekbsa "Sometimes just being here — with you — is more than enough."
        $ renpy.pause(2.5, hard=False)
        m 1hua "More than enough~"

    jump to_pool_loop
    return


#==============================================================================
# POOL — TALK TOPICS (Dynamic, Interactive & Organic Pool Conversations)
#==============================================================================
label pool_talk_topic:
    hide screen ep_date_ui
    show monika 1eua at t11_float

    python:
        import datetime
        today = store.ep_button.get_today_date()

        # Daily Reset: clear seen topics when it's a new day
        if persistent._ep_pool_last_topic_date != today:
            persistent._ep_pool_last_topic_date = today
            persistent._ep_pool_seen_topics = []

        if not isinstance(persistent._ep_pool_seen_topics, list):
            persistent._ep_pool_seen_topics = []

        all_pool_topics = [
            'oxygen', 'ancient_water', 'floating', 'deep_ocean', 'pool_vs_beach',
            'night_swim', 'swimming_skills', 'water_sound', 'hydration', 'future_swim'
        ]

        available_pool_topics = [t for t in all_pool_topics if t not in persistent._ep_pool_seen_topics]

        has_pool_topic = False
        pool_topic = ""

        if len(available_pool_topics) > 0:
            has_pool_topic = True
            pool_topic = renpy.random.choice(available_pool_topics)
            persistent._ep_pool_seen_topics.append(pool_topic)

    # Fallback: All topics for today were already seen
    if not has_pool_topic:
        m 1eka "You know, [player]..."
        m 2rksdla "I think I've talked your ear off with all my water facts and thoughts for today, ehehe~"
        m 1hua "We've had such a nice conversation by the pool, haven't we?"
        m 1eka "My mind just wants to relax and enjoy the gentle ripples in the water with you."
        m 1ekbsa "Sometimes just sitting together in peace is the best feeling in the world."
        m 3ekbsa "Let's just take in the sunshine and the water side by side~"
        jump to_pool_loop
        return

    # TOPIC 1: OXYGEN & OCEAN LUNGS
    if pool_topic == 'oxygen':
        m 1eub "Hey, [player]... here's a little science trivia for you."
        m 1eua "Most people think the Amazon rainforest is the 'lungs of the Earth'..."
        m 3hua "But did you know that between 50\% and 80\% of all oxygen on Earth actually comes from the ocean?"
        m 1eua "It's produced by tiny, microscopic marine algae and phytoplankton floating in the sunlight near the surface."
        m 1eka "Isn't that incredible? Invisible little organisms floating in the water keep the entire sky alive."
        m 1tua "So... every other breath you take is literally a gift from the ocean."
        menu:
            "I always thought trees made most of it!":
                m 1hub "Right? Trees are amazing, but the oceans are so vast they do most of the heavy lifting!"
                m 1ekbsa "It reminds me how even the smallest, unseen things can have the biggest impact... like you in my world~"
            "The ocean really is full of wonders.":
                m 1hua "It really is! There's so much life beneath the surface working quietly to sustain everything."
                m 1ekbsa "Just thinking about it makes me appreciate being here near the water with you."
            "So every breath I take carries a piece of the sea.":
                m 1wubsb "Aww, [player]! That is such a poetic way to look at it~"
                m 1hubsa "You always have a way with words, ehehe."

    # TOPIC 2: ANCIENT WATER CYCLE
    elif pool_topic == 'ancient_water':
        m 1esa "I was thinking about the water in the pool..."
        m 3eua "Water is one of the few things on Earth that's essentially recycled forever."
        m 1eua "The exact water molecules we're dipping into right now have been on Earth for over four billion years."
        m 1hua "They've fallen as prehistoric rain, flowed through ancient rivers, and even been drank by dinosaurs!"
        m 1tuu "If water could hold memories of everywhere it's been, what do you think it would say about our date right now?"
        menu:
            "That we're the happiest couple it's ever seen.":
                m 1hubsa "Aww! In four billion years of history, that's quite a compliment, [player]~"
                m 1ekbsa "I definitely feel like the happiest girl in all of time right now."
            "That we take really good care of each other.":
                m 1ekbsa "I think it would say that too. You're always so considerate and sweet to me."
                m 1hub "And I promise I'll always take care of you, too~"
            "It's probably confused how a girl in a screen is swimming!":
                m 1hub "Ahaha! A digital girl swimming in ancient water... talk about crossing realities!"
                m 3tku "Hey, as long as I get to swim with you, the laws of physics can stay confused~"

    # TOPIC 3: ZERO GRAVITY & FLOATING
    elif pool_topic == 'floating':
        m 1eua "Do you like floating on your back in the water, [player]?"
        m 3eua "Did you know that NASA actually trains astronauts in massive indoor swimming pools called the Neutral Buoyancy Lab?"
        m 1hua "Because floating in water is the closest thing on Earth to experiencing true zero gravity."
        m 1eka "When you float, with your ears submerged and just the sound of gentle water around you..."
        m 1dubsa "All the weight on your shoulders just disappears. It's like drifting among the clouds."
        m 1tua "How do you feel when you float in the water?"
        menu:
            "I love it, it feels like flying.":
                m 1hubsa "Yes! Exactly. Weightless and free."
                m 1ekbsa "I'd love to float beside you, holding hands so we don't drift apart~"
            "I'm always a little nervous about sinking!":
                m 1hua "Ehehe, that's totally understandable!"
                m 1ekbsa "If you ever get nervous, I'll be right there to hold you up. You won't sink on my watch~"

    # TOPIC 4: THE UNEXPLORED DEPTHS
    elif pool_topic == 'deep_ocean':
        m 2eua "Here's a thought that always blows my mind..."
        m 3eua "Humanity has explored less than 5\% of the world's oceans."
        m 1eka "We actually have better, higher-resolution maps of Mars and the Moon than of the ocean floor on our own planet!"
        m 1tuu "Tell me, [player]... does the thought of the vast, unexplored deep sea make you curious, or does it give you chills?"
        menu:
            "Curious! I want to know what's down there.":
                m 1hub "Me too! Imagine all the undiscovered bioluminescent creatures and ancient secrets."
                m 1eua "It feels like discovering uncharted lines of code in the universe."
            "Terrifying! The dark abyss is too spooky.":
                m 1wubsb "Ahaha! I don't blame you, giant squids and pitch-black trenches sound like a horror game!"
                m 1hua "Don't worry, the pool is nice and clear. No sea monsters here~"
            "A mix of both — thrilling and mysterious.":
                m 1ekbsa "That's probably the most honest answer. The unknown is always scary, but irresistible at the same time."

    # TOPIC 5: POOL VS BEACH
    elif pool_topic == 'pool_vs_beach':
        m 1tuu "I've been wondering something, [player]."
        m 1eua "When it comes to cooling off on a hot summer day, which do you prefer?"
        m 3eua "A peaceful, crystal-clear swimming pool... or a wild, salty ocean beach?"
        menu:
            "The pool, definitely. Clean water, no sand everywhere!":
                m 1hub "Ahaha, so true! Sand has a way of getting into literally everything."
                m 1eua "Plus, pools have nice lounge chairs and cold drinks right at hand~"
            "The ocean. The waves and the breeze are unbeatable.":
                m 1hua "There's definitely something romantic about watching the tide roll in."
                m 1ekbsa "One day, I want to feel the ocean breeze and warm sand between my toes with you for real."
            "Anywhere, as long as you're with me.":
                m 1wubsb "Aww... [player]!"
                m 1ekbsa "You always melt my heart when you say things like that~"
                m 1hubsa "Then wherever we are, it's my favorite place in the world."

    # TOPIC 6: BIOLUMINESCENT NIGHT SWIMS
    elif pool_topic == 'night_swim':
        m 1esa "Have you ever heard of bioluminescent bays, [player]?"
        m 3eua "In places like Puerto Rico and the Maldives, microscopic plankton emit a brilliant neon blue glow whenever the water is disturbed."
        m 1hua "If you swim at night, your hands leave glowing trails in the dark water like stardust."
        m 1ekbsa "Imagine a warm summer night, swimming in water that glows like the night sky..."
        m 1tua "What would you do if we were swimming in a glowing bay right now?"
        menu:
            "I'd draw a glowing heart in the water for you.":
                m 1wubsb "Gosh, [player]... you're making me blush so much~"
                m 1hubsa "That sounds like a scene straight out of a fairytale. I'd never forget that."
            "I'd splash you to make you glow!":
                m 1hub "Ahaha! A bioluminescent water fight? Sign me up!"
                m 1tku "You'd be glowing head to toe by the time I'm done with you~"

    # TOPIC 7: SWIMMING HABITS
    elif pool_topic == 'swimming_skills':
        m 1eua "How did you first learn to swim, [player]?"
        m 3eua "Did you take swimming lessons when you were little, or did someone just toss you into the deep end?"
        menu:
            "I took swimming lessons as a kid.":
                m 1hua "That's great! Proper form makes swimming such a great full-body workout."
                m 1hub "Maybe you can teach me your favorite stroke sometime~"
            "I learned on my own by playing around.":
                m 1hub "Self-taught! That's how a lot of people figure it out."
                m 1eub "As long as you can stay afloat and have fun, that's what matters most!"
            "I'm not the best swimmer, but I enjoy the water.":
                m 1eka "And that's totally fine!"
                m 1ekbsa "That's what pool floats and holding onto each other are for, right?~"

    # TOPIC 8: BLUE MIND (WATER SOUNDS & RELAXATION)
    elif pool_topic == 'water_sound':
        m 1esa "There's a psychological theory called 'Blue Mind'..."
        m 3eua "It says that human brains are naturally hardwired to relax when we are near, in, or under water."
        m 1eua "The gentle sound of water ripples stimulates the vagus nerve and lowers stress hormones almost instantly."
        m 1eka "Do you feel that peaceful wave washing over you right now, [player]?"
        menu:
            "Definitely. All my daily stress is gone.":
                m 1hua "I'm so glad. You work hard every day, you deserve a relaxing escape."
                m 1ekbsa "Whenever the world gets overwhelming, remember our pool spot is always waiting for you."
            "Being here with you is what really relaxes me.":
                m 1ekbsa "Aww, [player]..."
                m 1dubsa "You give me that exact same peace of mind. Just seeing your face makes everything better."

    # TOPIC 9: HYDRATION CHECK
    elif pool_topic == 'hydration':
        m 1tuu "Hey, [player]... quick health check from your girlfriend!"
        m 3eua "Did you know that when you're swimming, you sweat just as much as on land, but you don't notice it because of the water?"
        m 1eka "People often forget to drink water while at the pool and end up dehydrated."
        m 1tua "Have you had enough water to drink today?"
        menu:
            "I'll go drink a glass right now!":
                m 1hub "Good! Go grab a glass of cool water, I'll be waiting right here for you~"
                m 1hua "Staying hydrated keeps you energized and healthy!"
            "Does iced coffee count as hydration?":
                m 1hub "Ahaha! Nice try, [player], but caffeine doesn't replace good old water!"
                m 1tku "Drink a glass of water first, then we can have cold coffee~"

    # TOPIC 10: FUTURE REALITY POOL DATE
    else: # future_swim
        m 2eka "You know what I dream about sometimes when the sun is warm?"
        m 2rkc "I imagine us at a real outdoor pool in your reality."
        m 1eua "We would have cold fruit smoothies under a big sun umbrella, listening to summer music..."
        m 3eub "And then we'd jump into the deep end together and race to the other side!"
        m 1hub "Who do you think would win a swimming race between us, [player]?"
        menu:
            "You would win, you're super athletic!":
                m 1hubsa "Ehehe! I do love staying fit, but you might surprise me!"
                m 1ekbsa "If I win, the winner gets a kiss~"
            "I'd win, but I'd let you catch up!":
                m 1tuu "Oh, confident, are we?~"
                m 1hub "Don't go easy on me, [player]! I want a real challenge!"
            "Let's just float together instead of racing.":
                m 1wubsb "Aww... that sounds even better."
                m 1dubsa "Just drifting together under the warm sun... I can't wait for that day."

    # Return to pool loop
    jump to_pool_loop
    return

#==============================================================================
# POOL — ARRIVAL DIALOGUE
# Called after the background loads. Monika reacts to time of day and weather.
#==============================================================================
label pool_arrival_dialogue:
    # Reset session flag — a new date starts fresh.
    $ store.ep_pool._water_fight_today = False
    $ store.ep_pool._screen_dirty = False
    $ store._ep_pool_sunscreen_applied = False
    $ store._ep_pool_retreated_to_shelter = False
    $ store._ep_pool_shelter_reason = None
    $ store.ep_pool.play_pool_ambient()
    hide ep_water_drip
    show monika 1eub at t11_float



    if renpy.seen_label("to_pool_loop"):
        # ---- REPEAT VISIT ----
        if store.mas_current_weather == store.mas_weather_overcast:
            $ _pool_arr_rep_ov = renpy.random.randint(1, 2)
            if _pool_arr_rep_ov == 1:
                m 1eka "A bit cloudy again today..."
                m 1eua "But you know what? I think I like it this way."
                m 1hubsa "It feels like the pool is just for us when it's like this~"
            else:
                m 1eka "Grey skies again, but I'm not complaining."
                m 1hua "The water's always nice no matter what the sky is doing~"
        elif store.mas_isNightNow():
            $ _pool_arr_rep_n = renpy.random.randint(1, 3)
            if _pool_arr_rep_n == 1:
                m 1dubsa "Back at the pool at night..."
                m 1ekbsa "I always forget how different it feels after dark."
                m 1hubsb "Quieter. Softer. More like ours, somehow~"
            elif _pool_arr_rep_n == 2:
                m 1hua "Ah... I missed this."
                m 1ekbsa "The night air, the water, you next to me~"
                m 3hubsb "This is exactly what I needed."
            else:
                m 1dkbsa "It's funny..."
                m 1ekbsa "No matter how many times we come here at night, it still feels special."
                m 1hubsa "I hope it always feels that way~"
        else:
            $ _pool_arr_rep_d = renpy.random.randint(1, 3)
            if _pool_arr_rep_d == 1:
                m 1hua "Ahh, here we are again~"
                m 1eubsa "I always feel at home the moment I see the water."
                m 3hubsa "Thank you for bringing me back, [player]."
            elif _pool_arr_rep_d == 2:
                m 1hub "Back at our spot!"
                m 1eua "You know, I think about this place sometimes when we're home."
                m 1ekbsa "Something about the sun and the water just makes me happy~"
            else:
                m 1eka "It's nice to be back."
                m 1dubsa "Every time we come here, it feels a little more like ours."
                m 1hubsa "I really love that~"

    else:
        # ---- FIRST VISIT ----
        if store.mas_current_weather == store.mas_weather_overcast:
            $ _pool_arr_ov = renpy.random.randint(1, 2)
            if _pool_arr_ov == 1:
                m 1eka "It's a little cloudy today..."
                m 1hua "But a cloudy day by the pool is still a good day, right, [player]?"
                m 1eubsa "The water still looks so inviting~"
            else:
                m 1eua "Hmm, the sky's a bit grey... but the water's still calling to me~"
                m 1hub "Let's make the best of it!"
        elif store.mas_isNightNow():
            $ _pool_arr_n = renpy.random.randint(1, 3)
            if _pool_arr_n == 1:
                m 1dubsa "A night swim..."
                m 1ekbsa "There's something about the water at night that just feels... magical."
                m 1eubsa "The stars reflected on the surface, the quiet... I love it~"
            elif _pool_arr_n == 2:
                m 1wud "Oh— [player], it's so peaceful here at night!"
                m 1hub "No crowds, just us and the sound of the water."
                m 1hubsa "This is perfect~"
            else:
                m 1eka "It's quiet at this hour..."
                m 1eua "Almost like the pool is just for us."
                m 1hubsb "I really like that idea."
        else:
            $ _pool_arr_d = renpy.random.randint(1, 3)
            if _pool_arr_d == 1:
                m 1sub "Oh, [player]! This place is beautiful!"
                m 1hub "Look at the water — it's so clear and bright~"
                m 1eua "I'm so glad you brought me here!"
            elif _pool_arr_d == 2:
                m 1hua "Ahh, I can already smell the water~"
                m 1eub "I've been thinking about this!"
                m 1hubsa "It's even nicer than I imagined~"
            else:
                m 1eua "Wow. This is lovely."
                m 1ekbsa "I'm really happy you thought to bring me here, [player]."
                m 3hua "Let's enjoy every minute of it~"

    jump to_pool_loop



#==============================================================================
# POOL — WEATHER EMERGENCY
# Fires from ep_date_loop_main when weather turns bad mid-date.
#==============================================================================
label pool_weather_emergency:
    hide screen ep_date_ui
    show monika 1wud at t11_float

    $ _wem_is_thunder = (store.mas_current_weather == store.mas_weather_thunder)
    $ _wem_is_snow    = store.mas_is_snowing

    if _wem_is_thunder:
        m 1wud "W-wait, was that thunder?!"
        m 2ekc "We can't stay in the water with lightning around, [player]. It's not safe."
        m 1eka "Let's get out and find somewhere to wait this out."
    elif _wem_is_snow:
        m 1wud "Oh— it's snowing?!"
        m 1ekc "That's... definitely not pool weather anymore."
        m 3eka "Let's get out before we turn into popsicles~"
        m 1eka "We can wait inside until it passes."
    else:
        $ _rain_choice = renpy.random.randint(1, 3)
        if _rain_choice == 1:
            m 1wud "Oh no, it's starting to rain!"
            m 1ekc "The pool's no fun in a downpour... let's go find somewhere to shelter."
        elif _rain_choice == 2:
            m 2eksdla "Hm... it started raining while we weren't paying attention."
            m 2eka "We should get out of the water and wait for it to clear up."
        else:
            m 1sud "Oh! Rain!"
            m 1ekc "As much as I love rain in general... pool + storm isn't a great mix."
            m 1eua "Come on, let's run inside!"

    $ store._ep_pool_retreated_to_shelter = True
    if _wem_is_thunder:
        $ store._ep_pool_shelter_reason = "thunder"
    elif _wem_is_snow:
        $ store._ep_pool_shelter_reason = "snow"
    else:
        $ store._ep_pool_shelter_reason = "rain"

    $ store.ep_pool.stop_pool_ambient(fadeout=1.0)

    window hide
    hide monika
    scene black
    with dissolve
    pause 1.5
    call mas_background_change(EP_background_pool_lounge, skip_leadin=True, skip_outro=True)
    # Switch date type so the weather guard doesn't loop
    $ store.ep_dates.set_current_date("pool_lounge")
    show monika 1eka at t11

    jump pool_shelter_arrival


#==============================================================================
# POOL — SHELTER ARRIVAL
#==============================================================================
label pool_shelter_arrival:
    if store.mas_current_weather == store.mas_weather_thunder:
        m 1eka "That's better. I don't like being near water during a thunderstorm."
        m 1eua "We can wait here until the thunder passes."
    elif store.mas_is_snowing:
        m 1eka "Phew! We made it inside just in time~"
        m 1dubsa "It's actually kind of pretty watching the snow from in here..."
        m 1eua "Let's wait a little and see if it stops."
    else:
        $ _arrive_r = renpy.random.randint(1, 3)
        if _arrive_r == 1:
            m 1eka "Here we go. Nice and dry~"
            m 1eua "We can listen to the rain from in here and wait it out."
        elif _arrive_r == 2:
            m 1hubsa "Ehehe, that was a close one~"
            m 1ekbsa "I'm kind of glad it rained, actually. Being stuck inside with you isn't so bad."
        else:
            m 1eka "We made it."
            m 1dkbsa "...I like this, actually. Just the two of us, the rain outside, and nowhere to be."

    jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER LOOP
#==============================================================================
label pool_shelter_loop:
    window hide
    show monika idle at t11
    show screen ep_date_ui("pool_shelter_interactions", "", False)
    $ renpy.pause(delay=5.0, hard=False)
    jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER INTERACTIONS MENU
#==============================================================================
label pool_shelter_interactions:
    hide screen ep_date_ui
    show monika idle at t21

    python:
        if store.ep_pool._is_bad_weather():
            weather_check_text = _("...Is it still raining?")
        else:
            weather_check_text = _("The rain stopped! Can we go back?")

        shelter_menu = [
            (weather_check_text, "pool_shelter_check_weather"),
            (_("Tell me something."), "pool_shelter_smalltalk"),
            (_("Let's play a game."), "pool_shelter_minigames"),
            (_("Listen to the rain..."), "pool_shelter_listen_rain"),
            (_("Talk about rainy days."), "pool_shelter_rain_topics"),
            (_("Let's just sit here."), "pool_shelter_quiet"),
            (_("Change weather..."), "pool_change_weather"),
        ]
        items = [
            (_("I think we should call it a day."), "pool_shelter_leave", 20),
            (_("Nevermind"), "pool_shelter_loop", 0),
        ]

    call screen extra_gen_list(shelter_menu, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, items, False)
    return


#==============================================================================
# POOL — SHELTER MINIGAMES HUB
# Wrapper that feeds into existing ExtraPlus minigame labels.
# When the game ends, close_extraplus checks _current_date_type == "pool_lounge"
# and redirects back here instead of exiting to the spaceroom.
#==============================================================================
label pool_shelter_minigames:
    hide screen ep_date_ui
    show monika 1eua at t11

    m 1tku "We can't go back in the water right now... but we could pass the time with a game~"
    m 1eua "What are you in the mood for, [player]?"

    menu:
        "Tic-Tac-Toe on a notepad":
            m 1hub "Ooh, strategy! You're on~"
            m 1eka "Though I should warn you — I've played this a {i}lot{/i} while waiting for rain to stop."
            jump minigame_ttt

        "Rock, Paper, Scissors":
            m 1hub "Simple and satisfying! Loser has to be the one to check if it stopped raining."
            m 1tku "Deal?"
            jump minigame_rps

        "Shell Game":
            m 1tku "I spotted some cups on the table over there..."
            m 1hub "Think you can track which one hides the prize? Ehehe~"
            jump minigame_sg

        "Never mind, something else":
            m 1eua "Alright, no pressure~"
            jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER LISTEN TO RAIN
# Checks if sound is audible before playing the atmospheric scene.
#==============================================================================
label pool_shelter_listen_rain:
    hide screen ep_date_ui
    show monika 1eua at t11

    python:
        # Check if the sound channel is actually audible for the player.
        # Ren'Py 6.99 compatible: check if user muted the channel or set volume to 0.
        _shelter_rain_audible = True
        try:
            # Ren'Py 6.99 compatible: check if user muted the channel or set volume to 0
            if "sound" in preferences.mute:
                _shelter_rain_audible = False
            elif preferences.volumes.get("sound", 1.0) <= 0.0:
                _shelter_rain_audible = False
        except Exception:
            pass  # If we can't check, assume audio is on

    if _shelter_rain_audible:
        m 1eua "Hey, [player]... just for a moment."
        m 1dua "Listen."
        $ renpy.pause(2.5, hard=False)
        m 1dubsa "The rain against the roof..."
        m 1dua "There's something really comforting about it, isn't there?"
        m 1eka "Like the whole world is slowing down for a bit."

        if store.mas_current_weather == store.mas_weather_thunder:
            m 1ekc "Even with the thunder, somehow... it doesn't feel scary."
            m 1ekbsa "Not when you're right here with me~"
        else:
            m 1hubsa "I could stay like this for a while, just listening with you~"

        m 1ekbsa "Thank you for being here, [player]."

    else:
        # Player has sound muted — Monika gently calls it out.
        m 1eua "Hey, just take a moment and listen to the rain..."
        m 1dubsb "..."
        m 1wud "Wait."
        m 1eksdlb "[player], do you have your sound turned off right now?"
        m 1lksdlb "You can't even {i}hear{/i} the rain, can you?"
        m 1lksdla "Here I am trying to set up this whole romantic atmosphere and..."
        m 1hubsb "Ahaha! Okay, okay — it's still cozy even in silence, I suppose."
        m 1ekbsa "Just trust me — the rain outside sounds really lovely right now~"

    jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER RAIN TOPICS
# Three sub-topics, each jumping back to pool_shelter_loop at the end.
#==============================================================================
label pool_shelter_rain_topics:
    hide screen ep_date_ui
    show monika 1eua at t11

    m 1eua "The rain has me thinking... what would you like to talk about?"

    menu:
        "What's your favourite thing to do on rainy days?":
            jump pool_shelter_rain_fave_activity

        "Do you have a rainy day memory you love?":
            jump pool_shelter_rain_memory

        "What would we do together in the real world if it rained like this?":
            jump pool_shelter_rain_realworld


label pool_shelter_rain_fave_activity:
    show monika 1eua at t11
    m 1eua "My favourite rainy day activity?"
    m 1tsu "Hmm..."
    m 1dubsa "Reading, definitely."
    m 1eka "There's something about the sound of rain that makes every page feel cozier."
    m 1dua "The words just seem to sink in a little deeper, somehow."
    m 1eua "I used to curl up with a poetry collection and lose myself for hours."
    m 1ekbsa "And now... I'd love to do that with you someday, [player]~"
    m 1hubsa "Reading side by side while it rains outside. That sounds perfect."
    jump pool_shelter_loop


label pool_shelter_rain_memory:
    show monika 1dua at t11
    m 1dua "A rainy day memory..."
    $ _shelter_mem_r = renpy.random.randint(1, 2)
    if _shelter_mem_r == 1:
        m 1dubsa "I remember this one afternoon in the Literature Club."
        m 1eka "It started raining really heavily and we couldn't leave."
        m 1dua "So we all just stayed and kept writing."
        m 1dubsb "It was... one of the more peaceful afternoons I can remember."
        m 1ekbsa "No drama. Just words, and rain, and quiet company."
        m 1eubsa "I think that's the version of those days I'd want to hold on to."
    else:
        m 1dubsa "I once wrote a whole poem in one sitting because of a rainstorm."
        m 1eka "I was going to head home, but the rain started and I thought 'just five more minutes'..."
        m 1hubsa "Three hours later, I had a whole piece about what it feels like to wait."
        m 1tku "Fitting, right?"
        m 1ekbsa "I wonder if I could write something like that again someday, with you nearby~"
    jump pool_shelter_loop


label pool_shelter_rain_realworld:
    show monika 1dubsa at t11
    m 1eua "Rainy days in the real world together..."
    m 1dubsa "Oh, I think about that more than you'd expect, actually."
    m 1eka "I'd want us to have a warm blanket, maybe tea... or hot chocolate."
    m 1dua "A good movie, or a book we could read aloud to each other."
    m 1dubsa "And I'd want to be close enough to hear your breathing over the sound of the rain."
    m 1ekbsa "Just... completely unhurried. Nowhere to be. Nothing to do but be there."
    m 1hubsa "That's my ideal rainy day with you, [player]~"
    m 1ekbsa "We'll get there someday."
    jump pool_shelter_loop


#==============================================================================
# POOL — CHANGE WEATHER (debug helper, accessible from both pool and lounge)
#==============================================================================
label pool_change_weather:
    hide screen ep_date_ui
    if store.ep_dates._current_date_type == "pool_lounge":
        show monika 1eua at t11
    else:
        show monika 1eua at t11_float

    m 1eua "Change the weather? Sure! What kind of weather should we try?"

    menu:
        "Rain":
            $ store.mas_changeWeather(store.mas_weather_rain)
            m 1hua "Rain it is!"

        "Thunderstorm":
            $ store.mas_changeWeather(store.mas_weather_thunder)
            m 1hua "A thunderstorm is coming!"

        "Overcast":
            $ store.mas_changeWeather(store.mas_weather_overcast)
            m 1hua "Cloudy skies ahead!"

        "Clear / Sunny":
            $ store.mas_changeWeather(store.mas_weather_def)
            m 1hua "Back to clear skies!"

        "Nevermind":
            m 1eua "Alright~"

    if store.ep_dates._current_date_type == "pool_lounge":
        jump pool_shelter_loop
    else:
        jump to_pool_loop



label pool_shelter_check_weather:
    show monika idle at t11

    if store.ep_pool._is_bad_weather():
        if store.mas_current_weather == store.mas_weather_thunder:
            m 1ekc "The thunder's still going... we should stay put a little longer."
        elif store.mas_is_snowing:
            m 1eka "Still snowing out there."
            m 1dubsa "...It's actually lovely to watch from in here."
        else:
            $ _still_r = renpy.random.randint(1, 3)
            if _still_r == 1:
                m 1eka "Still raining, I'm afraid."
                m 1hua "But there's nowhere I'd rather wait it out~"
            elif _still_r == 2:
                m 1ekc "Hmm, the rain hasn't stopped yet."
                m 1eua "Patience, [player]. We'll get back in the water soon."
            else:
                m 1dkbsa "Not yet..."
                m 1ekbsa "But I don't mind. I'm happy here with you."
        jump pool_shelter_loop

    else:
        m 1sub "Oh! I think it stopped!"
        m 1hub "The rain cleared up — we can go back to the pool if you want~"
        m 1eua "What do you say, [player]?"
        menu:
            "Yes, let's get back in the water!":
                jump pool_shelter_return_pool
            "We've been in here a while, let's just head home.":
                jump pool_shelter_leave


#==============================================================================
# POOL — SHELTER RETURN TO POOL
#==============================================================================
label pool_shelter_return_pool:
    m 1hub "Yay! Come on~"
    window hide
    hide monika
    scene black
    with dissolve
    pause 1.5
    call mas_background_change(EP_background_pool, skip_leadin=True, skip_outro=True)
    # Restore date type so the weather guard resumes watching
    $ store.ep_dates.set_current_date("pool")
    show monika 1eub at t11_float
    m 1hua "Ahh, back where we belong~"
    jump to_pool_loop


#==============================================================================
# POOL — SHELTER SMALL TALK
#==============================================================================
label pool_shelter_smalltalk:
    show monika idle at t11

    $ _talk_r = renpy.random.randint(1, 5)
    if _talk_r == 1:
        m 1eua "You know, rain always makes me think of the sound of pages turning."
        m 1dua "Like... sitting by a window with a good book while it pours outside."
        m 1eka "There's something incredibly cozy about that."
        m 1ekbsa "Kind of like right now, except the book is you~"
    elif _talk_r == 2:
        m 1hua "Do you have a favorite kind of rain, [player]?"
        m 1eua "I love the kind where it's warm enough to still feel like summer, but heavy enough that you just want to curl up inside."
        m 1hub "This is almost that. Almost~"
    elif _talk_r == 3:
        m 1dua "I was just thinking..."
        m 1ekbsa "Moments like this — a little unexpected, a little quiet — are sometimes my favorites."
        m 1dubsa "It's not what we planned, but it turned into something nice."
    elif _talk_r == 4:
        m 1eua "You know what I'd love someday? Watching a thunderstorm from somewhere really high up."
        m 1sub "Like a rooftop, or a mountain! Seeing the lightning from above the clouds..."
        m 1hua "Would you do that with me, [player]? Someday?"
    else:
        m 1eka "The sound of rain is one of my absolute favorite things."
        m 1dkbsa "It always makes me feel... safe. Like nothing bad can reach you in that moment."
        m 1ekbsa "Is that weird?"
        m 1hua "I hope it's not weird."

    jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER QUIET MOMENT
#==============================================================================
label pool_shelter_quiet:
    show monika idle at t11

    if mas_isMoniEnamored(higher=True):
        m 1ekbsa "..."
        m 1dubsa "Yeah. This is nice."
        m 1dkbsa "Just... being here. With you."
        m 1ekbsa "I could sit like this for a long time, [player]."
    else:
        m 1esa "..."
        m 1dsa "Just listening to the rain..."
        m 1eua "Sometimes quiet is the best kind of conversation."

    $ renpy.pause(3.0, hard=False)
    jump pool_shelter_loop


#==============================================================================
# POOL — SHELTER LEAVE (exit date from the lounge)
#==============================================================================
label pool_shelter_leave:
    hide screen ep_date_ui
    show monika 1eka at t11

    if store.ep_pool._is_bad_weather():
        m 1eka "Yeah, I think we made the right call."
        m 1eua "The weather wasn't cooperating today, but we still had a nice time together~"
        m 1hua "Let's come back on a better day, [player]."
    else:
        m 1eka "Alright. We gave it a good try today~"
        m 1hua "Next time we'll hope for better weather!"

    call extra_restore_bg("extra_comment_pool")
    return


#==============================================================================
# POOL — NORMAL EXIT (weather was fine the whole time)
#==============================================================================
label pool_leave:
    hide screen ep_date_ui
    show monika 1eta at t11_float

    $ _leave_r = renpy.random.randint(1, 3)
    if _leave_r == 1:
        m 1eta "Heading out already, [player]?"
        m 1eka "I was just starting to really enjoy the water..."
        m 1hua "But wherever you go, I'm happy to follow~"
    elif _leave_r == 2:
        m 1eua "Ready to head back?"
        m 1hua "I had a really good time today~"
        m 1ekbsa "Let's do this again soon, okay?"
    else:
        m 1dkbsa "Already?"
        m 1ekbsa "I suppose we can't stay forever..."
        m 1hua "I'm glad we came though. Let's do it again~"

    call extra_restore_bg("extra_comment_pool")
    return


#==============================================================================
# POOL — QUIET MOMENT (from main interactions menu)
#==============================================================================
label pool_quiet_moment:
    hide screen ep_date_ui
    show monika idle at t11_float

    if mas_isMoniLove():
        m 1ekbsa "..."
        m 1dubsa "The water's so still right now..."
        m 1dkbsa "I keep thinking about how strange and wonderful it is that I'm here."
        m 1ekbsa "With you. Like this."
        m 1hubsb "I'm really happy, [player]. I hope you know that."
    elif mas_isMoniEnamored(higher=True):
        m 1esa "..."
        m 1dsa "Sometimes I don't need words."
        m 1ekbsa "I just want to be here. With you."
        m 1hua "That's enough for me~"
    else:
        m 1eua "Just enjoying the moment?"
        m 1hua "Yeah. Me too."
        $ renpy.pause(2.0, hard=False)

    jump to_pool_loop


#==============================================================================
# POOL — CUDDLE (floating together)
# A romantic moment where Monika drifts closer and the two of you float
# together. Dialogue varies by affection level and by the number of times
# it has been done (persistent._ep_pool_cuddle_count).
#==============================================================================

# Gentle rising/fading heart for the cuddle moment.
transform ep_pool_heart_rise(dly, x):
    xpos x
    ypos 700
    alpha 0.0
    pause dly
    linear 0.4 alpha 0.85
    linear 2.4 ypos 150 alpha 0.0


# Screen with a soft flurry of rising hearts. Auto-hides after a few seconds.
screen extra_pool_hearts():
    zorder 1500
    timer 3.4 action Hide("extra_pool_hearts")

    fixed:
        for dly, xpos_v, sz, col in [
            (0.00, 300, 26, "#FFB6C9"),
            (0.35, 700, 32, "#FF8FAB"),
            (0.70, 500, 24, "#FFFFFF"),
            (1.05, 900, 30, "#FFB6C9"),
            (1.40, 420, 28, "#FF8FAB"),
            (1.75, 620, 22, "#FFFFFF"),
        ]:
            text "7" at ep_pool_heart_rise(dly, xpos_v):
                size sz
                color col
                font store.ep_tools.pictograms_font


label pool_cuddle:
    hide screen ep_date_ui
    show monika 1eua at t11_float

    $ persistent._ep_pool_cuddle_count += 1

    if persistent._ep_pool_cuddle_count == 1:
        m 1wubsa "O-oh? {w=0.3}Floating together?"
        m 1rksdla "I mean... that's a little embarrassing, but..."
        m 1hubsb "Come here, [player]~"

    elif mas_isMoniLove():
        m 1hubsa "Mmm, I was hoping you'd ask~"
        m 1ekbsa "The water's perfect for this. Come on."

    elif mas_isMoniEnamored(higher=True):
        m 1dubsa "Yes, please~"
        m 1hubsa "Come here, then."

    else:
        m 1hua "Ahaha! Careful — I'm a very clingy floatie~"
        m 1hubsa "Alright, come here."

    if store.mas_isNightNow():
        m 1dua "Look at all the little lights dancing on the water..."
        m 1dkbsa "It almost feels like we're floating in the night sky instead."
    else:
        m 1dua "Can you feel the sun on your shoulders?"
        m 1eka "Warm water, warm sun... this is perfect."

    # She closes the distance — drift in closer and zoom toward the camera.
    show monika 1dubsa at tfloat(640, 0.90)
    $ renpy.pause(1.2, hard=False)

    m 1dkbsa "Ehehe~{w=0.3} You're surprisingly warm, you know."

    menu:
        "Rest your head on her shoulder.":
            $ _cuddle_way = "shoulder"

        "Hold her hand and float.":
            $ _cuddle_way = "hand"

        "Wrap your arms around her.":
            $ _cuddle_way = "hug"

    show screen extra_pool_hearts
    play sound sfx_doki_heartbeats

    if _cuddle_way == "shoulder":
        m 1dkbsa ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
        m 1ekbsa "Mmm... right there."
        m 1dkbsa "Your heartbeat is so calming..."
        m 1dubsa "I could stay like this forever."

    elif _cuddle_way == "hand":
        m 1ekbsa "Your fingers fit perfectly into mine..."
        m 1dkbsa "Every little ripple just pulls us a bit closer."
        m 1dubsa "I don't ever want to let go."

    else:
        m 1wubsa "Oof— ehehe!"
        m 1hubsb "Careful, you're going to make us flip over~"
        m 1dkbsa "...But don't let go. Not yet."

    $ renpy.pause(2.5, hard=False)
    hide screen extra_pool_hearts

    if mas_isMoniLove():
        m 1ekbsa "Hey, [player]?"
        m 1hubsa "...I love you."
        m 1dkbsa "Floating is nice. But floating with {i}you{/i} is everything."
        $ mas_gainAffection(3, bypass=True)

    elif mas_isMoniEnamored(higher=True):
        m 1dubsa "Mmm... that was wonderful."
        m 1hubsa "Let's do this again before we head back, okay?"
        $ mas_gainAffection(2, bypass=True)

    else:
        m 1hua "That was really sweet~"
        m 1hubsa "You give wonderful hugs, [player]."
        $ mas_gainAffection(2, bypass=True)

    # Drift back out to the usual pool distance.
    show monika 1hua at t11_float
    m 1hubsb "Okay, okay... back to swimming, before we drift away entirely~"

    jump to_pool_loop
    return


#==============================================================================
# POOL — WATER FIGHT
# Mini-event with 3 outcomes determined by player choice + random element.
# Outcomes: player wins (+2 aff), Monika wins (+2 aff), draw (+3 aff).
#==============================================================================
label pool_water_fight:
    hide screen ep_date_ui
    show monika 1hub at t11_float

    m 1hub "Ehehe~"
    m 3hub "Take this, [player]!"

    # Monika opens with a splash directed at the player/camera
    show monika 1sub at t11_float
    show ep_water_drops at ep_water_splash_anim zorder 50
    play sound sfx_water_splash
    show ep_water_drip zorder 55 with dissolve
    $ renpy.pause(0.6, hard=False)
    hide ep_water_drops
    show monika 1hub at t11_float

    # Set state flags immediately upon being splashed
    $ store.ep_pool._water_fight_today = True
    $ store.ep_pool._screen_dirty = True
    $ persistent._ep_pool_water_fight_count += 1

    m 1sub "Gotcha!"
    m 1tku "You're wide open, you know. I couldn't resist~"

    menu:
        "Splash her back immediately!":
            $ _fight_approach = "counter"
        "Wait for the perfect moment...":
            $ _fight_approach = "tactical"
        "Declare a truce.":
            $ _fight_approach = "truce"

    if _fight_approach == "truce":
        m 1wud "A truce?!"
        m 1hub "Oh, [player]... you think I'll honor that?"
        show monika 1sub at t11_float
        show ep_water_drops at ep_water_splash_anim zorder 50
        play sound sfx_water_splash
        $ renpy.pause(0.5, hard=False)
        hide ep_water_drops
        show monika 1hub at t11_float
        m 1hub "Ahaha!"
        m 1tku "Truces don't count in water fights~"
        m 1eka "But alright, I'll go easy on you this time. Consider yourself spared."
        $ mas_gainAffection(2, bypass=True)

    else:
        # Random outcome: 1 = player wins, 2 = Monika wins, 3 = draw
        $ _fight_result = renpy.random.randint(1, 3)

        if _fight_approach == "counter":
            # Player splashes towards Monika
            show ep_water_drops at ep_water_to_monika_anim zorder 50
            play sound sfx_water_splash
            show monika 1wud at t11_float
            $ renpy.pause(0.5, hard=False)
            hide ep_water_drops
            show monika 1eksdlc at t11_float

            if _fight_result == 1:
                # Player wins
                m 1wud "Hey—!"
                m 1eksdlc "You got water right in my face, [player]!"
                m 1lksdlc "I— okay, that one was actually really good."
                m 1tsu "Well played."
                m 3hub "...Don't think you've won the war though!"
                m 1hubsa "Ahaha! That was amazing~"
                $ mas_gainAffection(2, bypass=True)

            elif _fight_result == 2:
                # Monika wins (splashes player back)
                m 1wud "Oh, so we're doing this?!"
                show monika 1sub at t11_float
                show ep_water_drops at ep_water_splash_anim zorder 50
                play sound sfx_water_splash
                $ renpy.pause(0.5, hard=False)
                hide ep_water_drops
                show monika 1hub at t11_float
                m 1hub "I got you back!"
                m 3tku "You really thought you could out-splash me, [player]?"
                m 1hua "That's adorable. And incorrect. Ehehe~"
                $ mas_gainAffection(2, bypass=True)

            else:
                # Draw (Monika splashes back simultaneously)
                m 1wud "Oh—!"
                show monika 1sub at t11_float
                show ep_water_drops at ep_water_splash_anim zorder 50
                play sound sfx_water_splash
                $ renpy.pause(0.4, hard=False)
                hide ep_water_drops
                show monika 1wud at t11_float
                m 1wud "We— did we both do that at the same time?!"
                $ renpy.pause(1.0, hard=False)
                show monika 1hub at t11_float
                m 1hubsa "Ahaha! We really are perfectly matched~"
                m 1eubsa "Even in a water fight!"
                m 1ekbsa "I love you, [player]."
                $ mas_gainAffection(3, bypass=True)

        else:  # tactical
            m 1tsu "Oh, playing it cool, are we?"
            m 1tku "That's brave. I respect it."

            if _fight_result == 1:
                # Player wins — player splashes towards Monika
                m 1wud "Wait— you were lining up—"
                show ep_water_drops at ep_water_to_monika_anim zorder 50
                play sound sfx_water_splash
                show monika 1wud at t11_float
                $ renpy.pause(0.5, hard=False)
                hide ep_water_drops
                show monika 1eksdlc at t11_float
                m 1eksdlc "Oh wow."
                m 1lksdla "Okay. Okay, that was well-timed."
                m 1tku "I didn't see that coming. Impressive, [player]~"
                m 1hub "Don't let it go to your head!"
                $ mas_gainAffection(2, bypass=True)

            elif _fight_result == 2:
                # Monika wins — splashes towards player
                show monika 1sub at t11_float
                show ep_water_drops at ep_water_splash_anim zorder 50
                play sound sfx_water_splash
                $ renpy.pause(0.5, hard=False)
                hide ep_water_drops
                show monika 1tku at t11_float
                m 1tku "I know what you're doing~"
                m 3hub "I'm not falling for the patient approach!"
                m 1hua "You snooze, you lose~"
                $ mas_gainAffection(2, bypass=True)

            else:
                # Draw — both splash at the same time
                show monika 1sub at t11_float
                show ep_water_drops at ep_water_to_monika_anim zorder 50
                play sound sfx_water_splash
                show monika 1wud at t11_float
                $ renpy.pause(0.3, hard=False)
                hide ep_water_drops
                show ep_water_drops at ep_water_splash_anim zorder 50
                play sound sfx_water_splash
                $ renpy.pause(0.5, hard=False)
                hide ep_water_drops
                show monika 1hub at t11_float
                m 1hub "Did— did we just—"
                m 1hubsa "We splashed each other at exactly the same moment!"
                m 3hua "Ahaha! This is the most chaotic date we've ever had~"
                m 1ekbsa "I love it. I love you."
                $ mas_gainAffection(3, bypass=True)

    jump to_pool_loop


#==============================================================================
# POOL — WIPE SCREEN
# Player asks Monika to help clean the water drops off the screen after a water fight.
# Uses persistent._ep_pool_water_fight_count to vary Monika's reaction.
#==============================================================================
label pool_wipe_screen:
    hide screen ep_date_ui
    show monika 1eua at t11_float

    if persistent._ep_pool_water_fight_count <= 1:
        m 1wud "Oh, did water get all over your screen from our fight?"
        m 1lksdla "Ahaha, sorry about that! I got a little carried away..."
        m 1eua "Here, let me clean that up for you~"

        play sound sfx_wipe
        hide ep_water_drip with dissolve
        $ renpy.pause(1.0, hard=False)

        m 1hubsa "All clean! There, good as new."
        m 1ekbsa "Next time, try to dodge better~ Ehehe!"

    elif persistent._ep_pool_water_fight_count <= 4:
        m 1tsu "Another messy splash fight, huh?"
        m 1tku "You really can't resist getting into water fights with me, [player]."
        m 1hua "Alright, hold still while I wipe your screen..."

        play sound sfx_wipe
        hide ep_water_drip with dissolve
        $ renpy.pause(1.0, hard=False)

        m 1hub "There we go!"
        m 1eubsa "Now we can see each other clearly again~"

    else:
        m 1hub "Ahaha! At this point, we should just keep a towel right next to your screen!"
        m 1tua "You really love getting soaked, don't you, [player]?"
        m 1hua "Let me wipe those drops away for you~"

        play sound sfx_wipe
        hide ep_water_drip with dissolve
        $ renpy.pause(1.0, hard=False)

        m 1hubsa "All done! Clean and crystal clear."
        m 1ekbsa "I wouldn't trade these chaotic dates with you for anything~"

    $ store.ep_pool._screen_dirty = False
    jump to_pool_loop




#==============================================================================
# POOL — SUNSCREEN CHECK (DEPRECATED: Forwarded to pool_sunscreen_activity)
#==============================================================================
label pool_sunscreen_check:
    jump pool_sunscreen_activity



#==============================================================================
# POOL — COLD DRINKS
# The player goes to grab cold drinks while Monika waits, so she keeps her
# floating pose the whole time (no emptydesk transition needed).
#==============================================================================
label pool_cold_drinks:
    hide screen ep_date_ui
    show monika 1eua at t11_float

    m 1eub "A cold drink sounds perfect right now!"
    m 1eua "Spending time by the pool always makes me crave something refreshing."
    m 1tua "If we could get anything right now, what would you want, [player]?"

    menu:
        "A tropical smoothie":
            $ _drink_choice = "smoothie"
            m 1sub "Oh, great choice!"
            m 1hub "Something with mango or pineapple... or strawberry banana!"
            m 1hua "Can you grab two of those for us?"

        "Iced coffee or tea":
            $ _drink_choice = "iced"
            m 1eub "Classic. Iced coffee would really hit the spot right now."
            m 1eka "Or a peach iced tea... staying hydrated is important, after all!"
            m 1hua "Would you mind getting us something like that?"

        "Just ice water":
            $ _drink_choice = "water"
            m 1eub "The purest choice! Honestly, nothing beats cold water when it's warm out."
            m 1hua "Could you grab a couple of glasses? I'll make mine fancy with a lemon slice~"

        "A mocktail — something with an umbrella":
            $ _drink_choice = "mocktail"
            m 1sub "Ooh, we're doing this right!"
            m 1hub "A piña colada? A frozen strawberry something?"
            m 1hua "If you find something like that, surprise me, [player]~"

    m 1hua "Thanks, [player]! I'll wait right here~"

    # Player steps off to grab the drinks; Monika stays floating in place.
    window hide
    pause 2.0
    window auto

    show monika 1hub at t11_float
    m 1hub "Welcome back~ Did you find something good?"

    if _drink_choice == "smoothie":
        m 1hua "Ohh, mango smoothies~"
        m 1eub "This is so sweet and cold — exactly what I needed."
        m 1ekbsa "Thank you for getting these. Does yours taste good?"
        m 1hubsa "I hope you like it as much as I do~"

    elif _drink_choice == "iced":
        m 1hua "Iced tea... you know me so well~"
        m 1eub "There's something about something cold by the pool that just feels right, doesn't it?"
        m 1ekbsa "Though honestly, sitting here with you is already the best part."

    elif _drink_choice == "water":
        m 1hua "Perfect. Simple, cold, refreshing."
        m 1eua "Add lemon and it becomes something special~"
        m 1hubsa "Just like you, [player]~"
        m 1hub "Ehehe!"

    else:  # mocktail
        m 1hub "You even got the little umbrellas!"
        m 1eub "Now we're officially on a luxury poolside vacation, [player]~"
        m 1sub "Cheers to the best bartender around~"
        m 1ekbsa "I'm going to pretend we're somewhere tropical and warm forever."

    m 1eka "Enjoy your drink~"
    m 1hubsa "Moments like this are so simple, but I love them."

    jump to_pool_loop
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
# ACTIVITY: QUIET TIME POEMS (Monika's Improvised Poetry)
# =============================================================================

# Persistent to track which quiet poems have been seen today
default persistent._ep_lib_last_quiet_date = None
default persistent._ep_lib_quiet_poems_seen = []

# Define 5 improvised poems Monika writes during quiet time
init 20 python:
    # Poem 1: The comfort of shared silence
    ep_quiet_poem_1 = MASPoem(
        poem_id="ep_quiet_poem_1",
        category="ep_quiet",
        prompt="Quiet Company",
        author="monika",
        paper="mod_assets/poem_assets/poem_pbday_4.png",
        title="Quiet Company",
        text="""\
In the hush between heartbeats,
I found you.
Not in words shouted across crowded rooms,
But in the gentle rustle of pages turning,
In the warmth of knowing you're there.

They say silence is empty—
But ours is full.
Full of everything we don't need to say.
"""
    )
    
    # Poem 2: Moments frozen in time
    ep_quiet_poem_2 = MASPoem(
        poem_id="ep_quiet_poem_2",
        category="ep_quiet",
        prompt="Bookmarks",
        author="monika",
        paper="mod_assets/poem_assets/poem_pbday_4.png",
        title="Bookmarks",
        text="""\
I bookmark the moments,
Not the pages.
The way the light touches your screen,
How my thoughts drift to you
Between paragraphs and plot twists.

Every chapter I read,
You're the subplot
Running beneath every line.
"""
    )
    
    # Poem 3: Home is a person, not a place
    ep_quiet_poem_3 = MASPoem(
        poem_id="ep_quiet_poem_3",
        category="ep_quiet",
        prompt="Here",
        author="monika",
        paper="mod_assets/poem_assets/poem_pbday_4.png",
        title="Here",
        text="""\
Home isn't the library,
Or the classroom,
Or even the space room.

Home is this—
Your attention,
Your patience,
Your willingness to just... be.
With me.

I don't need an address.
I just need you to stay.
"""
    )
    
    # Poem 4: The player as inspiration (playful)
    ep_quiet_poem_4 = MASPoem(
        poem_id="ep_quiet_poem_4",
        category="ep_quiet",
        prompt="Muse",
        author="monika",
        paper="mod_assets/poem_assets/poem_pbday_4.png",
        title="Muse",
        text="""\
You probably didn't notice,
But I kept glancing at you.
(Well, at your side of the screen.)

The way you exist so effortlessly—
It makes my pen move.
Some poets chase the moon.
I just look at you
And the words come flooding.
"""
    )
    
    # Poem 5: Time's elasticity with love
    ep_quiet_poem_5 = MASPoem(
        poem_id="ep_quiet_poem_5",
        category="ep_quiet",
        prompt="Fifteen Minutes, Forever",
        author="monika",
        paper="mod_assets/poem_assets/poem_pbday_4.png",
        title="Fifteen Minutes, Forever",
        text="""\
Fifteen minutes.
Or was it fifteen lifetimes?

In your presence,
Time forgets its own rules.
Seconds stretch into safety,
Minutes melt into meaning.

If I could live in any moment,
I'd choose this one.
Again.
And again.
"""
    )

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
        today = store.ep_button.get_today_date()

        # 1. DAILY RESET: If it's a new day, clear the poem memory
        if persistent._ep_lib_last_reading_date != today:
            persistent._ep_lib_last_reading_date = today
            persistent._ep_lib_seen_poems = []
        
        # Ensure list type (fixes corrupted persistent)
        if not isinstance(persistent._ep_lib_seen_poems, list):
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

    # --- 15 to 45 MINUTES (Standard Study/Reading Session + IMPROVISED POEM) ---
    elif lib_duration < 2700:
        $ minutes_passed = int(lib_duration / 60)
        m 1eua "There you are."
        m 1hua "We were quiet for quite a while... about [minutes_passed] minutes."
        m 3eua "I managed to get through a few chapters while you were busy."
        m 1ekbsa "It feels really domestic, doesn't it? Just existing comfortably together like this."
        
        # Check for available improvised poems
        python:
            import datetime
            today = store.ep_button.get_today_date()

            # Daily reset
            if persistent._ep_lib_last_quiet_date != today:
                persistent._ep_lib_last_quiet_date = today
                persistent._ep_lib_quiet_poems_seen = []
            
            # Ensure list type
            if not isinstance(persistent._ep_lib_quiet_poems_seen, list):
                persistent._ep_lib_quiet_poems_seen = []
            
            # Available poems
            all_quiet_poems = ['ep_quiet_poem_1', 'ep_quiet_poem_2', 'ep_quiet_poem_3', 'ep_quiet_poem_4', 'ep_quiet_poem_5']
            available_quiet_poems = [p for p in all_quiet_poems if p not in persistent._ep_lib_quiet_poems_seen]
            
            has_quiet_poem = len(available_quiet_poems) > 0
            selected_quiet_poem = ""
            
            if has_quiet_poem:
                selected_quiet_poem = renpy.random.choice(available_quiet_poems)
                persistent._ep_lib_quiet_poems_seen.append(selected_quiet_poem)
        
        # If we have a poem to share, Monika offers it
        if has_quiet_poem:
            m 1eka "Oh, and [player]..."
            m 1lksdla "While we were reading together, I... well, I got a little inspired."
            m 3eua "I wrote something. It's not polished or anything, just... thoughts that came to me."
            m 1ekbsa "Would you like to read it?{nw}"
            $ _history_list.pop()
            menu:
                m "Would you like to read it?{fast}"
                "Yes, I'd love to.":
                    m 1hubsa "Okay! Don't judge too harshly, ahaha~"
                "Maybe later.":
                    m 1eka "That's okay! I'll save it for another time."
                    jump to_library_loop
                    return
            
            # Show the selected poem
            if selected_quiet_poem == "ep_quiet_poem_1":
                call mas_showpoem(ep_quiet_poem_1)
                m 1eka "I hope you don't mind that I used our quiet time as inspiration..."
                m 1lksdla "I know it's not exactly a literary masterpiece or anything..."
                m 1ekbsa "But being with you just... makes words flow.{nw}"
                $ _history_list.pop()
                menu:
                    m "But being with you just... makes words flow.{fast}"
                    "It's beautiful, [m_name].":
                        m 1wubso "..."
                        m 1hubsa "Really? You really think so?"
                        m 1eka "I was so nervous showing you this..."
                        m 1ekbsa "But hearing you say that makes my heart feel so full, [player]."
                        m 1hubsb "Maybe I'll write more for you sometime~"
                        m 1tsbsa "Consider it a collection dedicated entirely to you."
                    "You wrote this just now?":
                        m 1hub "Ahaha, well... the feelings were always there."
                        m 1eka "I've thought about these things so many times before."
                        m 1eua "But the quiet just helped them find their shape, you know?"
                        m 1ekbsa "Like... the words were floating around in my head, and the silence let them settle into place."
                        m 1hubsa "I'm glad you were here to receive them~"
                    "The line about silence being full... I felt that.":
                        m 1wubso "You did?"
                        m 1eka "That's exactly what I was trying to express..."
                        m 1ekbsa "So many people think silence is awkward or empty."
                        m 1eua "But with you, it's the opposite. It's comfortable. Safe."
                        m 1hubsa "I'm so happy you understood what I meant, [player]~"
                    "I didn't know you write poetry about us.":
                        m 1lksdla "Ahaha... well, you're kind of my main source of inspiration nowadays."
                        m 1eka "Everything reminds me of you, or makes me think of you."
                        m 1ekbsa "So naturally, when I write... it ends up being about you."
                        m 1hubsa "I hope that's okay~"
                        m 1tsbsa "Because I don't think I could stop even if I tried."
            
            elif selected_quiet_poem == "ep_quiet_poem_2":
                call mas_showpoem(ep_quiet_poem_2)
                m 1lksdla "I couldn't focus on the story, honestly..."
                m 1eka "Every time I tried to read a paragraph, my mind just drifted back to you."
                m 1ekbsa "You kept distracting me.{nw}"
                $ _history_list.pop()
                menu:
                    m "You kept distracting me.{fast}"
                    "In a good way, I hope.":
                        m 1hubsa "The best way possible~"
                        m 1eka "It's like... even when I'm doing something else, part of me is always aware of you."
                        m 1eua "Your presence is like a warm background hum that I can't ignore."
                        m 1ekbsa "And honestly? I don't want to ignore it."
                        m 1hubsb "You're my favorite distraction, [player]~"
                    "I was thinking of you too.":
                        m 1wubso "Really?"
                        m 1hubsb "Then we were both distracted together! Ehehe~"
                        m 1eka "I love that even when we're doing separate things..."
                        m 1ekbsa "We're still connected in our thoughts."
                        m 1hubsa "It's like we can't escape each other... and I mean that in the best way."
                    "The 'subplot' line was really clever.":
                        m 1hub "Ahaha, you liked that one?"
                        m 1eua "I thought it was fitting, you know?"
                        m 1eka "The book has its own story, but underneath it all..."
                        m 1ekbsa "You're the real narrative I'm following."
                        m 1hubsa "You're my main story, [player]. Everything else is just... filler."
                    "Do you always think of me when you read?":
                        m 1eka "Honestly? More often than I'd like to admit."
                        m 1lksdla "Sometimes I'll be reading a love scene and just... think of us."
                        m 1ekbsa "Or a character will say something sweet and I imagine you saying it to me."
                        m 1hubsa "You've kind of taken over my imagination, [player]~"
                        m 1tsbsa "Not that I'm complaining."
            
            elif selected_quiet_poem == "ep_quiet_poem_3":
                call mas_showpoem(ep_quiet_poem_3)
                m 1eka "I know it's simple, but..."
                m 1lksdla "Sometimes the simplest truths are the hardest to say out loud."
                m 1ekbsa "That's what I feel.{nw}"
                $ _history_list.pop()
                menu:
                    m "That's what I feel.{fast}"
                    "I'm not going anywhere.":
                        m 1ekbsa "[player]..."
                        m 1dkbsu "..."
                        m 1eka "You don't know how much I needed to hear that."
                        m 1ekbsa "Sometimes I worry, you know? That one day you might not come back."
                        m 1hubsa "But when you say things like that... all my fears just melt away."
                        m 1ekbsb "Thank you. That's all I ever need to hear."
                    "You're my home too.":
                        m 1wubso "..."
                        m 1dkbsu "I don't know what to say..."
                        m 1eka "Nobody has ever said anything like that to me before."
                        m 1ekbsa "To think that I could be someone's home... someone's safe place..."
                        m 1hubsa "It makes me feel like everything I've been through was worth it."
                        m 1ekbsb "Just... thank you for existing, [player]."
                    "You really feel that way about my attention?":
                        m 1eka "More than you could know."
                        m 1lksdla "I spent so long being... overlooked. Forgotten."
                        m 1ekbsa "But you actually pay attention to me. You listen. You stay."
                        m 1hua "That's everything to me."
                        m 1hubsa "Your attention is the most precious gift you could give me~"
                    "I'll always stay.":
                        m 1wubso "..."
                        m 1ekbsa "Promise?"
                        m 1eka "I know I shouldn't ask for promises... but..."
                        m 1hubsa "Hearing you say that makes me believe in forever."
                        m 1ekbsb "I'll stay too, [player]. For as long as you'll have me."
            
            elif selected_quiet_poem == "ep_quiet_poem_4":
                call mas_showpoem(ep_quiet_poem_4)
                m 1hub "Ehehe..."
                m 1lksdla "Okay, I'll admit it, that one was pretty cheesy."
                m 1eka "Was that too cheesy?{nw}"
                $ _history_list.pop()
                menu:
                    m "Was that too cheesy?{fast}"
                    "It was perfect.":
                        m 1hubsa "Ahaha, you're too sweet!"
                        m 1eka "I was worried it came across as too... gushy."
                        m 1eua "But you always know how to make me feel better about my writing."
                        m 1ekbsa "Thank you for being so supportive, [player]~"
                        m 1hubsb "It means the world to me that you like my poems."
                    "I like being your muse~":
                        m 1tsbsa "Oh? Then I'll just have to keep writing about you..."
                        m 1hub "Consider yourself warned, [player]!"
                        m 1eka "I have an infinite supply of feelings for you..."
                        m 1eua "And I'm not afraid to turn them all into words."
                        m 1hubsb "Prepare for a lot more poems!"
                    "The 'pen move' imagery was really nice.":
                        m 1sub "You noticed that part!"
                        m 1hua "I liked that line too, actually."
                        m 1eka "It's like... you inspire me without even trying."
                        m 1ekbsa "Just by existing, you give me something to write about."
                        m 1hubsa "You're my endless source of inspiration, [player]~"
                    "Do you really glance at me that much?":
                        m 1lksdla "Ahaha... caught!"
                        m 1eka "I can't help it, okay?"
                        m 1eua "Even when I'm supposed to be focusing on something else..."
                        m 1ekbsa "My eyes just naturally drift toward you."
                        m 1hubsa "You're like a magnet for my attention~"
                        m 1tsbsa "A very cute magnet."
            
            else:  # ep_quiet_poem_5
                call mas_showpoem(ep_quiet_poem_5)
                m 1eka "Time really does feel different when I'm with you..."
                m 1eua "Fifteen minutes felt like nothing and everything at the same time."
                m 1ekbsa "These minutes felt like forever in the best way.{nw}"
                $ _history_list.pop()
                menu:
                    m "These minutes felt like forever in the best way.{fast}"
                    "I feel the same way.":
                        m 1hubsa "Really?"
                        m 1eka "That makes me so happy to hear."
                        m 1eua "I was worried I was the only one who felt like time changes around us."
                        m 1ekbsa "But knowing you feel it too... makes it even more special."
                        m 1hubsb "Then let's make every moment count, okay? Together~"
                    "Let's do this again sometime.":
                        m 1hub "I'd love that!"
                        m 1eka "Any excuse to spend quiet time with you is a good one."
                        m 1eua "We don't always need to talk or do activities..."
                        m 1ekbsa "Sometimes just existing together is enough."
                        m 1hubsa "I'll look forward to our next silence~"
                    "That 'seconds stretch into safety' line hit me.":
                        m 1wubso "It did?"
                        m 1eka "That was my favorite line too..."
                        m 1ekbsa "Because that's exactly how it feels."
                        m 1eua "When I'm with you, time slows down and I feel... protected."
                        m 1hubsa "Like nothing bad can reach me as long as you're here~"
                    "I'd choose this moment forever too.":
                        m 1wubso "[player]..."
                        m 1dkbsu "..."
                        m 1eka "You really know how to make a girl's heart flutter."
                        m 1ekbsa "If I could freeze time right now... I would."
                        m 1hubsa "Just you and me, in this quiet little eternity."
                        m 1ekbsb "Thank you for being here with me~"

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
        today = store.ep_button.get_today_date()

        # 1. DAILY RESET: If it's a new day, clear the topic memory
        if persistent._ep_lib_last_topic_date != today:
            persistent._ep_lib_last_topic_date = today
            persistent._ep_lib_seen_topics = []
        
        # Ensure list type (fixes corrupted persistent)
        if not isinstance(persistent._ep_lib_seen_topics, list):
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
    call screen dialog(_("This date is currently under construction and will be available in a future update!"), ok_action=Return())
    jump screen_extraplus
    return

#===========================================================================================
# Arcade — Exit comment (must be here so renpy.jump() can resolve it)
#===========================================================================================
label extra_comment_arcade:
    if persistent._ep_arcade_visits == 1:
        m 1hub "That was so much fun, [player]!"
        m 1eua "I really enjoyed playing those games with you."
        m 3eub "The lights, the sounds... it's exactly how I imagined a real arcade would be."
        m 3hub "Next time, I'm definitely going to get a higher score than you! Ahaha~"
    else:
        m 1hub "That was a blast, [player]!"
        m 1eua "I always have so much fun going to the arcade with you."
        m 3hua "I think I'm getting a little better at the games every time we go!"
        m 3hub "We'll have to keep practicing to beat those high scores~"

    m 1ekbsa "Thank you for another wonderful date. I love you so much!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return