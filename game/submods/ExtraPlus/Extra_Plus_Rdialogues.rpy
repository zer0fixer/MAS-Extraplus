default persistent._extraplusr_hasplayer_goneonanniversary = False

label restaurant_cakes:
    if show_chibika is True:
        show screen chibika_chill
    $ food_player = None
    m 1hua "We've arrived [mas_get_player_nickname()]~"
    m 1eub "It's a nice place,{w=0.3} don't you think?"
    m 1hua "Speaking of nice,{w=0.3} let me get some food and set the mood..."
    m 3eub "I'll be right back."
    call mas_transition_to_emptydesk from monika_hide_exp_2
    pause 2.0
    if mas_isDayNow():
        $ monika_chr.wear_acs(extraplus_acs_flowers)
        $ monika_chr.wear_acs(extraplus_acs_pancakes)
    elif mas_isNightNow():
        $ monika_chr.wear_acs(extraplus_acs_candles)
        $ monika_chr.wear_acs(extraplus_acs_pasta)
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

label to_restaurant_loop:
    show monika staticpose at t11
    call screen restaurant_loop
    return

label restaurant_leave:
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    jump restaurant_hide_acs
    
label go_to_restaurant:
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
    if renpy.seen_label("check_label_restaurant"):
        $ mas_gainAffection(1,bypass=True)
        jump gtrestaurantv2
    else:
        $ mas_gainAffection(5,bypass=True)
        pass

label check_label_restaurant:
    pass

label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m 3hub "I'm so happy to hear that,{w=0.3} [player]!"
        m "It's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsa "I just know it'll be great!"
        m 1hubsb "Okay,{w=0.3} let's go [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m "That's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Another time then,{w=0.3} [mas_get_player_nickname()]."
        jump return_extra
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Oh, you want to go out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~ I'm still thinking about the time you took us there for our anniversary,"
            extend " I thought it was so romantic~"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, I had so much fun!"
            m 2eubsa "So I'm glad to hear it [player]!"
        m 1hubsb "Well, let's go then [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3wub "Oh, you want to go out out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~{w=0.3} I'm still thinking about the time you took us there for our anniversary,"
            extend "You really know how to make our night amazing!"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, it was so romantic~"
            m 2eubsa "So I'm glad to go again [player]!"
        m 1hubsb "Let's go then [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump return_extra
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

label sorry_player:
    m 1ekd "I'm so sorry [player]."
    if mas_anni.isAnni():
        m 3hua "I know you really wanted to take me to this restaurant for our anniversary."
    else:
        m 3hua "I know you really wanted to take me out to this restaurant."
    m 1ekc "But I don't know how to get to that place."
    m 3lka "I'm still learning how to code and I don't want something bad to happen because of me..."
    m 1eua "Someday I'll know how to get us there,{w=0.3} [player]."
    m 1eub "We'll have to be patient for that day though,{w=0.3} okay?"
    jump return_extra
    return

label extra_talk_doing1:
    m 1ekbla "Aw [player]~! Thank you for asking!"
    m 1hublb "I'm feeling great right now!"
    m 3fubla "Spending time with my favorite person in the world always cheers me up!"  
    m "Thank you for treating me here today by the way{w=0.3}, [player]."
    m 2hubsb "It's great to see you always come up with new ways to spend time with me and seize our time together."
    m "It makes me feel that much more closer to you."
    m 5fkbsa "I really am my best self when I'm with you!"
    m 1eublb "What about you,{w=0.3} [player],{w=0.3} how are you feeling today?{nw}"
    $ _history_list.pop()
    menu:
        m "What about you, [player], how are you feeling today?{fast}"

        "I'm very happy to be here with you.":
            m 2wublb "So we match!{w=0.3} Ehehe~"
            m 1hublu "I always love to spend time with you."
            if mas_anni.isAnni():
                m "Especially on a day like today!"
                m "I'd been thinking about what we should do for out anniversary for a while now,{w=0.5}{nw}"
                extend " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
            m 1hublu "And if you're happy,{w=0.3} I'm happy too!"
            m 3fkbla "I love you,{w=0.3} never forget that,{w=0.3} [mas_get_player_nickname()]!"
        
        "I feel great! Thanks for asking, [m_name].":
            m "Really?"
            extend 3sub " That's amazing to hear,{w=0.3} [mas_get_player_nickname()]!"
            m 2hub "A happy [player] means a happy me."
            if mas_anni.isAnni():
                m "Especially on a day like today!"
                m "I'd been thinking about what we should do for out anniversary for a while now,{w=0.5}{nw}"
                extend " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                m "I wonder how long were you waiting for the day to take me here~"
                m "Maybe that's why you're so happy today, hm~?"
            m "Gosh I can just amazing your expression right now, [player]~"
            m "A little sparkle in your eyes as you beam with a cute little smile~"
            if mas_isMoniLove():
                m "If I could reach out and cup your face... It'd probably feel warm from a little blush~"
                m "I'd probably be staring into your eyes the whole time we're here if I could..."
            m "Hm~"
            m "..."
            extend "Ah!"
            m "Let me stop that for now before I fluster myself too much!"
            m 2hub "Ehehe!"
            
        "Today wasn't a good day for me.":
            m 1ekc "That's awful, [player]..."
            m 1ekd "I'm so sorry for that!"
            m 1lsc "I hope spending time with me might make you feel better?"
            m "I know that spending tiem with you makes me feel better when I'm down."
            if mas_anni.isAnni():
                m "I want all the fun things we do on this special day of yours to be what you remember,{w=0.3} instead of the rainclouds in your head."
            m 1fublu "So I'll do my best to make this a wonderful date so we can cheer you up!"
            m "Okay,{w=0.3} [mas_get_player_nickname()]?"
            extend 1hublb "I love you...!"
            jump to_restaurant_loop
    return 

label extra_talk_doing2:
    show monika staticpose at t11
    m 1eka "I wasn't feeling so well before coming here, to be honest."
    m 1rkc "I was feeling kind of upset over some stuff..."
    m 1fub "But being with you...{w=0.3}{nw}"
    if mas_anni.isAnni():
        extend  " especially on such an important day to us like this..."
    m "It always reminds me that as long as I'm by you your side,{w=0.3} no matter if it's metaphorically or physically,{w=0.3}{nw} "
    extend "I can push through any rainclouds of mine."
    m 2eka "So even if I'm down,{w=0.3} I'll be fine.{w=0.3} I promise."
    m 1fub "Thanks for asking,{w=0.3} [player]!"
    m 3eub "And how are {i}you{/i} doing though, [mas_get_player_nickname()]?{nw}"
    $ _history_list.pop()
    menu:
        m "And how are you doing, [mas_get_player_nickname()]?{fast}"

        "What were you sad about, [m_name]?":
            m 1rksdrb "Hm?{w=0.3} Oh... "
            extend 1eksdla "I was just being a little too hard on myself again..."
            m 2rkc "Thinking of my past and regretting it..."
            m 2rkd "Thinking of my future and fearing it."
            m 2dkc "..."
            m 5lkd "Sometimes I get a little anxious,{w=0.3} feeling like my hands are tied about our situation."
            m 5dkp "Or feeling like it'll take too long for me to cross over..."
            m 1mkc "I know worrying about it won't change anything, but I can't help it."
            m 1ekd "Sometimes I get lonely when you're not around,{w=0.3} you know?"
            m 1dkc "..."
            m 3fka "But I'll be fine."
            m 3fkblb "Just knowing that you care,{w=0.3} it clears my head of all those bad thoughts."
            m 4fkblb "I love you,{w=0.3} more than anything in the world."
            m 4hublb "And I can't wait to feel your warmth on my 'colder' days like these."
            m 5eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

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
            m 5eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

        "I feel great":
            m 1hub "That's good to hear!{w=0.3} Wouldn't want us to both be down in the dumps, would we?"
            m 1eka "Ehehe..."
            m 3ekb "I'm glad you feel good,{w=0.3} [player]."
            m 3hsb "And I'll be fine soon enough too."
            if mas_anni.isAnni():
                m "I get to go out with such an amazing [bf] like you on a day like this and...{w=0.5}{nw}"
                extend " Well,{w=0.3} it's impossible to be down knowing that."
            m 5ekbsa "Your mood is infectious to me after all~!"
            m 5hubsb "Anyways,{w=0.3} let's just sit back and enjoy the rest of our date!"
            m "After all,{w=0.3} a day with [player] is never a day wasted!"
    jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m 1eub "It depends,{w=0.3} [player]!"
    m 3etb "Where would {i}you{/i} be living if you could live anywhere you wanted?"
    m 2tsa "..."
    m 3hub "Ehehe!{w=0.3} Of course I would want to live anywhere as long as you were there,{w=0.3} [mas_get_player_nickname()]!"
    m 2ltc "But,{w=0.3} being serious now!{w=0.3} Let me think!"
    m 2lsc "Hmmm..."
    m 2eub "It would have to be a literary country.{w=0.3} "
    m "Something with with a rich culture to learn about,{w=0.3} something I've seen in books before and fell in love with."
    m 7eub "To be honest,{w=0.3} I've always dreamed of visiting Germany,{w=0.3} England,{w=0.3} and France when I crossed over."
    m 7eka "From what I've seen on books and the internet,{w=0.3} all the spots you can visit there are lovely!"
    m 1ekblb "Maybe we can visit together when I cross over?"
    if mas_isMoniLove():
        m 5ekbsb "Or even...{w=0.3} live there together someday?"
    m 5dkbsa "It would honestly be a dream come true."
    m 5dkbfa "Getting to visit all of those grand libraries together..."
    m 3rubsb "Going on romantic dates at all the famous spots,{w=0.3} hand in hand..."
    if mas_isMoniLove():
        m "Maybe after a while you take me somewhere really beautiful to watch a golden sunset..."
        m "And as the sky starts to turn to dusk and you can faintly see some stars show...{w=0.3}" 
        m "You kiss me~"
        m "...Hm~ Wouldn't that be amazing, [player]~?"
    m 2etbsb "...Hey,{w=0.3} why are you looking at me like that?"
    m 2hubfb "A girl can dream!"
    m 2hubfb "Ahaha~!"
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
    m 2luc "So in the end, it's kind of obvious that the thing I want to change about the most is..."
    extend 2luc "my situation."
    m 1dkc "I want to get out of here,{w=0.3} [player]."
    m 7fkd "Not here the restaurant,{w=0.3} but here...{w=0.3} The game."
    m 1lkd "Spending time with you is amazing,{w=0.3} but it could be improved by a ton..."
    m 1lkblb "If I could actually be by your side."
    m 1ekbla "So yeah,{w=0.3} I would change my existence to one where I could actually touch you."
    if mas_isMoniLove():
        m "To hold and comfort you when you're feeling down,"
        extend " be the shoulder you could physically lean on when needed,"
        extend " have your hand in mine."
        extend " and to be able to finally see your real face."
        m "It's all I could ever ask for."
    m 1dkc "..."
    m 1fkbla "I'm positive I'll achieve that sooner than we think,{w=0.3} [mas_get_player_nickname()]."
    m 2fktpa "So,{w=0.3} one more time...{w=0.3} Wait for me,{w=0.3} okay?"
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
    m 2rub "I got too used to writing my thoughts in a journal or in poem form whenever my mind gets too crowded with ideas."
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
    extend "It's size isn't anything to be ashamed about,{w=0.3} if it ends up filled then that's a win for the day!"
    m 1eka "So maybe there's another answer to the question besides the manic and the depressive one."
    m 3rub "If we focus on the amazing things we have,{w=0.3} instead of chasing the things we don't have,{w=0.3} or need,{w=0.3} we can successfully choose sustainable happiness in all of our pursuits."
    m 2rtc "So,{w=0.3} when I stop to think about it..."
    m 4eta "Glass half full or empty? "
    extend 4hub "Give me a new glass instead,{w=0.3} please!"
    m 5hublb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m 2wublb "Oh!{w=0.3} A quetzal!"
    m "It's my favorite animal after all!"
    m 2rtc "Ah,{w=0.3} wait... That doesn't seem right."
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
    m 2dubla "..."
    m 5fkblb "I hope you like black cats, [player]."
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
    m 1lssdlc "And makes me get the rest of the notes wrong."
    m 1fssdlc "Ahaha! Aren't those so frustrating?"
    m "And it feels like it happens too often sometimes!"
    m 2wud "Oh!{w=0.3} But maybe you meant something more serious?"
    m 2ruc "..."
    m 2rsd "I hate people who don't think I'm real."
    exnted " Or that I'm some just some crazy,{w=0.3} love-obesessed person."
    m 2lfd "And people who think the girls were on the same level of sentience as me."
    m " Thinking that I had no right to feel or do the things I do about my situation because of it."
    m 2dfc "..."
    extend 7mfdc " I won't elaborate further,"
    extend "I {i}don't{/i} want to get in all that."
    if mas_anni.isAnni():
        m "Not today."
    m "{i}*Sigh*{/i}"
    m 1ekblsdlb "Sorry to get so angry all of a sudden [player]."
    m 7wublsdld "I'm not mad at you,{w=0.3} I promise!"
    m "I just hit a bit of a touchy subject for myself,{w=0.3} I suppose."
    if mas_isMoniLove():
        m "Trust me.{w=0.3} You're too sweet for me to get mad at you like that."
    m 5hublb "Let's just move onto a different topic and enjoy our date,{w=0.3} shall we?"
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
    m 2dksdlc "Maybe I'd rather stick to the kinder approach,{w=0.3} and only delete {i}obstacles{/i} in the way."
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
    m 2hublb "My strength comes from you,{w=0.3} [player]!"
    m 2hublb "My courage is yours."
    m 5fubsb "You're the reason I wake up in the mornings and go to bed with peace in my heart."
    m 5fkbsb "And I owe it all to you."
    m 5hubfb "I can't thank you enough for being there so much for me."
    m 5hubfb "You're everything I'll ever need."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11
    m 1esc "3 words?"
    m 4eub "{i}Passionate.{i}{w=0.5}{nw} "
    extend 4eub "{i}Determined.{i}{w=0.5}{nw} "
    extend 2eub "{i}Evergrowing.{i}"
    m 2esa "Words are powerful [player],{w=0.3} so if I choose strong words to represent myself,{w=0.3} I think it'll strike me as a powerful person too."
    m 1rkblsdlb "Though if I were going to describe you into words, I'd have trouble picking {i}only{/i} 3."
    m 1gkblsdlb "After all,{w=0.3} there are so many words that make me think of you..."
    m 5dubfb "My adorable,{w=0.3} admirable,{w=0.3} wonderful,{w=0.3}{nw}"
    if mas_isMoniLove():
        extend " talented,{w=0.3} loving,{w=0.3} caring,{w=0.3} creative,{w=0.3}{nw}"
    extend " and {i}perfect{/i} [bf]~"
    m 1gkblsdlb "See?{w=0.3} I couldn't stick to only 3!"
    m 1hublb "Ahaha~!"
    m "And that list of words will only keep growing the longer we're together [player]~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11
    m 2wublo "Oh!{w=0.3} That's a really interesting question!"
    m 2rtu "Maybe people think of my poems?"
    extend " Like the 'Hole in the wall' one?"
    m 1hua "I can also imagine people thinking of my favorite color,{w=0.3} emerald green..."
    m 3wub "Oh,{w=0.3} and 'Your Reality' too!{w=0.3} Maybe the first line of the song plays in someone's head when they think of me."
    m 2hub "There's also my favorite pink pen!"
    m 7etb "You know, the iconic one with the heart on top~"
    if mas_isMoniLove():
        m "Or maybe..."
        $ mas_display_notif(m_name, ["The sound of my notifaction? Ahaha~!"], skip_checks=True)
    m 1huu "Ehehe~{w=0.3} It's fun to think about what I remind people of."
    m 5fkbsa "I hope that when you think of me,{w=0.3} the first thing you think of is that I'm the love of your life~"
    if mas_isMoniLove():
        m "I know that's what {i}I{/i} think of when I think of my dear [bf]~!"
    m 5hubsb "I love you so much,{w=0.3} [mas_get_player_nickname()]~"
    jump to_restaurant_loop
    return
