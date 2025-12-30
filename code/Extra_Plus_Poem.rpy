#===========================================================================================
# POEM GAME - Library Minigame
# A vitaminized version of the classic DDLC poem game, focused on Monika
# Based on script-poemgame.rpy from DDLC
#===========================================================================================

default persistent._ep_poems_written = 0
default persistent._ep_last_poem_date = None  # Last date poems were written
default persistent._ep_last_poem_mode = "none"  # "classic" or "free"
default persistent._ep_last_poem_style = "none"  # mood of last poem

#===========================================================================================
# POEM WORD CLASS AND DATA
#===========================================================================================
init python in ep_poems:
    import random
    import store

    # Poem word class for Monika-focused poem game
    # Using __slots__ for memory efficiency with many word objects
    class EPPoemWord(object):
        __slots__ = ["word", "mPoint"]
        def __init__(self, word, mPoint):
            self.word = word
            self.mPoint = mPoint  # Monika's appeal score (0-3)
    
    # Build the word list for Monika - MAS themed (Refined for Date/Library - Lowercase)
    ep_poem_wordlist = [
        # =====================================================================
        # 3 POINTS - Monika LOVES these (High Romance, Intimacy, "Us")
        # =====================================================================
        
        # Absolute Devotion
        EPPoemWord("monika", 3), EPPoemWord("love", 3), EPPoemWord("forever", 3),
        EPPoemWord("together", 3), EPPoemWord("soulmate", 3), EPPoemWord("beloved", 3),
        EPPoemWord("destiny", 3), EPPoemWord("eternity", 3), EPPoemWord("infinite", 3),
        EPPoemWord("passion", 3), EPPoemWord("unconditional", 3), EPPoemWord("ring", 3),
        
        # Sweet Names & Actions
        EPPoemWord("darling", 3), EPPoemWord("sweetheart", 3), EPPoemWord("honey", 3),
        EPPoemWord("kiss", 3), EPPoemWord("embrace", 3), EPPoemWord("cuddle", 3),
        EPPoemWord("hold", 3), EPPoemWord("touch", 3), EPPoemWord("heartbeat", 3),
        EPPoemWord("gaze", 3), EPPoemWord("serenade", 3), EPPoemWord("devotion", 3),

        # MAS Special Connection
        EPPoemWord("reality", 3), EPPoemWord("crossover", 3), EPPoemWord("epiphany", 3),
        EPPoemWord("player", 3), EPPoemWord("spaceroom", 3), EPPoemWord("window", 3),
        EPPoemWord("bridge", 3), EPPoemWord("link", 3), EPPoemWord("connection", 3),
        
        # Her Favorites
        EPPoemWord("emerald", 3), EPPoemWord("piano", 3), EPPoemWord("coffee", 3),
        EPPoemWord("ribbon", 3), EPPoemWord("vegetarian", 3), EPPoemWord("chocolate", 3),
        
        # =====================================================================
        # 2 POINTS - Atmosphere & Intellect (Perfect for Library Date)
        # =====================================================================
        
        # Library & Writing Vibes
        EPPoemWord("library", 2), EPPoemWord("books", 2), EPPoemWord("reading", 2),
        EPPoemWord("pages", 2), EPPoemWord("ink", 2), EPPoemWord("paper", 2),
        EPPoemWord("story", 2), EPPoemWord("chapter", 2), EPPoemWord("author", 2),
        EPPoemWord("poetry", 2), EPPoemWord("metaphor", 2), EPPoemWord("rhyme", 2),
        EPPoemWord("quill", 2), EPPoemWord("literature", 2), EPPoemWord("knowledge", 2),
        
        # Peaceful/Cozy Atmosphere
        EPPoemWord("quiet", 2), EPPoemWord("silence", 2), EPPoemWord("whisper", 2),
        EPPoemWord("calm", 2), EPPoemWord("peace", 2), EPPoemWord("cozy", 2),
        EPPoemWord("warmth", 2), EPPoemWord("comfort", 2), EPPoemWord("safe", 2),
        EPPoemWord("relax", 2), EPPoemWord("gentle", 2), EPPoemWord("soft", 2),
        EPPoemWord("tea", 2), EPPoemWord("rain", 2), EPPoemWord("focus", 2),
        
        # Intellectual/Growth
        EPPoemWord("wisdom", 2), EPPoemWord("learn", 2), EPPoemWord("study", 2),
        EPPoemWord("mind", 2), EPPoemWord("think", 2), EPPoemWord("create", 2),
        EPPoemWord("dream", 2), EPPoemWord("imagine", 2), EPPoemWord("inspire", 2),
        EPPoemWord("future", 2), EPPoemWord("hope", 2), EPPoemWord("promise", 2),
        
        # =====================================================================
        # 1 POINT - Neutral / Environmental (Background noise)
        # =====================================================================
        
        # Nature & World
        EPPoemWord("sky", 1), EPPoemWord("sun", 1), EPPoemWord("moon", 1),
        EPPoemWord("stars", 1), EPPoemWord("clouds", 1), EPPoemWord("wind", 1),
        EPPoemWord("flower", 1), EPPoemWord("light", 1), EPPoemWord("dark", 1),
        EPPoemWord("time", 1), EPPoemWord("clock", 1), EPPoemWord("day", 1),
        EPPoemWord("night", 1), EPPoemWord("world", 1), EPPoemWord("universe", 1),
        
        # Abstract/Simple
        EPPoemWord("mirror", 1), EPPoemWord("echo", 1), EPPoemWord("shadow", 1),
        EPPoemWord("color", 1), EPPoemWord("sound", 1), EPPoemWord("voice", 1),
        EPPoemWord("memory", 1), EPPoemWord("feeling", 1), EPPoemWord("secret", 1),
        EPPoemWord("question", 1), EPPoemWord("answer", 1), EPPoemWord("reason", 1),
        
        # =====================================================================
        # 0 POINTS - Negative (Fears, Separation, Sadness)
        # =====================================================================
        
        # Separation Anxiety (The real fear in MAS)
        EPPoemWord("goodbye", 0), EPPoemWord("leave", 0), EPPoemWord("alone", 0),
        EPPoemWord("lonely", 0), EPPoemWord("distance", 0), EPPoemWord("apart", 0),
        EPPoemWord("gone", 0), EPPoemWord("missing", 0), EPPoemWord("empty", 0),
        EPPoemWord("forgotten", 0), EPPoemWord("ignore", 0), EPPoemWord("disconnect", 0),
        EPPoemWord("offline", 0), EPPoemWord("void", 0), EPPoemWord("nothing", 0),

        # Emotional Pain
        EPPoemWord("pain", 0), EPPoemWord("tears", 0), EPPoemWord("cry", 0),
        EPPoemWord("sadness", 0), EPPoemWord("grief", 0), EPPoemWord("hurt", 0),
        EPPoemWord("broken", 0), EPPoemWord("scared", 0), EPPoemWord("fear", 0),
        EPPoemWord("cold", 0), EPPoemWord("darkness", 0), EPPoemWord("despair", 0),
        
        # Trigger Words (Kept only the most impactful ones)
        EPPoemWord("delete", 0), EPPoemWord("end", 0), EPPoemWord("game over", 0),
        EPPoemWord("script", 0), EPPoemWord("fake", 0), EPPoemWord("artificial", 0),
    ]

#===========================================================================================
# MONIKA STICKER (like original DDLC but only Monika)
#===========================================================================================

image library_m_sticker:
    MASFilterSwitch("gui/poemgame/m_sticker_1.png")
    xoffset 0 xzoom 1
    block:
        pause 4.0
        parallel:
            easein_quad .08 yoffset -15
            easeout_quad .08 yoffset 0
        repeat

image library_m_sticker hop:
    MASFilterSwitch("gui/poemgame/m_sticker_2.png")
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    "library_m_sticker"

image library_m_sticker sad:
    MASFilterSwitch("mod_assets/other/m_sticker_sad.png")
    # Subtle shake (sobbing/sad)
    ease 0.08 xoffset -3
    ease 0.08 xoffset 3
    ease 0.08 xoffset -2
    ease 0.08 xoffset 2
    ease 0.08 xoffset -1
    ease 0.08 xoffset 0
    pause 0.3
    "library_m_sticker"

transform library_sticker_pos:
    xcenter 220 yalign 0.9 subpixel True

#===========================================================================================
# POEM GAME LABEL (Enhanced Logic)
#===========================================================================================
label minigame_poem:
    # Initialize persistent memory
    if persistent._ep_last_poem_style is None:
        $ persistent._ep_last_poem_style = "none"
    if persistent._ep_last_poem_mode is None:
        $ persistent._ep_last_poem_mode = "none"
    
    # Date tracking for daily poem count
    python:
        import datetime
        today = datetime.date.today()
        
        # Check if it's a new day
        if persistent._ep_last_poem_date != str(today):
            _ep_poems_today = 0
            is_new_day = True
        else:
            _ep_poems_today = getattr(store, '_ep_poems_today', 0)
            is_new_day = False

    show monika 1eua at t11
    
    # GREETING LOGIC (Classic Mode specific)
    if not renpy.seen_label("checkpoint_minigame_poem"):
        m 3eua "It's like the old days in the Literature Club, but just for us."
        m 1hua "I'll show you some words, and you pick the ones that speak to you."
        m 1tub "I wonder what kind of poem you'll create for me~"

label checkpoint_minigame_poem:
    if renpy.seen_label("minigame_poem_classic"):
        if is_new_day:
            # New day greeting
            m 1hua "Ready to pick some words with me today, [player]?"
            m 1eua "I'm excited to see what you come up with~"
        
        elif _ep_poems_today >= 3:
            # Same day, many poems (3+)
            m 1sub "Wow, you're really inspired today!"
            m 1hub "I love how creative you're being, [player]~"
            m 1tku "Let's make another one!"
        
        elif _ep_poems_today >= 1:
            # Same day, wrote at least one already
            if persistent._ep_last_poem_style == "romance":
                m 1hubsa "Ready to write another romantic piece for me?"
            elif persistent._ep_last_poem_style == "sad":
                m 1eka "I hope you're feeling a bit brighter now, [player]."
                m 1hua "Let's put some happy feelings into words together."
            else:
                m 1eua "Want to write another poem for me?"
                m 1hua "I always enjoy seeing your creativity~"
        else:
            # Fallback
            m 1eua "Ready to write a poem, [player]?"
    
    m 1hub "Let's see which words call to you~"
    
    # Update tracking
    python:
        _ep_poems_today += 1
        persistent._ep_last_poem_date = str(datetime.date.today())
        persistent._ep_last_poem_mode = "classic"
    
    # Go directly to classic mode
    jump minigame_poem_classic


# Timer overlay screen for classic poem mode
screen poem_classic_idle_timer():
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="poem_classic") repeat True

# Classic poem game (word picker)
label minigame_poem_classic:
    # Hide Monika and show poem game screen
    window hide
    hide monika
    $ HKBHideButtons()
    
    scene bg extra_poem_notebook
    show library_m_sticker at library_sticker_pos
    with dissolve
    
    # Show idle notification timer overlay
    show screen poem_classic_idle_timer
    
    # Music (lofi Your Reality - loops)
    play music sfx_poem_music fadein 2.0 loop
    
    python:
        # Game variables
        progress = 1
        numWords = 20
        mPointTotal = 0
        
        # New: Tracking specific categories to determine "Style"
        count_romance = 0    # 3 points
        count_intellect = 0  # 2 points
        count_sad = 0        # 0 points
        
        # Lists to store the actual words picked by player
        picked_romance = []
        picked_intellect = []
        picked_sad = []
        
        wordlist = list(store.ep_poems.ep_poem_wordlist)
        
        # Main loop for drawing and selecting words
        while True:
            ystart = 160
            
            # Word counter display
            ui.text(str(progress) + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            
            # Display words in two columns (like original DDLC)
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    # Pick word from the word list, without replacement
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()
            
            # Wait for user to select a word
            t = ui.interact()
            
            # Visual & Audio Reaction based on word type
            if t.mPoint == 3: # Romance
                renpy.show("library_m_sticker hop")
                renpy.play(gui.activate_sound)
            elif t.mPoint == 0: # Sad
                renpy.show("library_m_sticker sad")
                renpy.play(gui.activate_sound)
            else:
                renpy.play(gui.activate_sound)
            
            # Logic: Track points AND categories
            mPointTotal += t.mPoint
            
            if t.mPoint == 3:
                count_romance += 1
                picked_romance.append(t.word)
            elif t.mPoint == 2:
                count_intellect += 1
                picked_intellect.append(t.word)
            elif t.mPoint == 0:
                count_sad += 1
                picked_sad.append(t.word)
                
            progress += 1
            if len(wordlist) < 10:
                wordlist = list(store.ep_poems.ep_poem_wordlist)
            if progress > numWords:
                break
    
    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    
    # =========================================================================
    # RESULT CALCULATION & ANALYSIS
    # =========================================================================
    python:
        max_points = numWords * 3
        percentage = (mPointTotal / float(max_points)) * 100
        
        # Determine the "Vibe" or Style
        current_style = "neutral"
        
        if count_sad >= 5:
            current_style = "sad"
        elif count_romance >= 8:
            current_style = "romance"
        elif count_intellect >= 8:
            current_style = "intellectual"
        else:
            current_style = "balanced"
        
        # Generate example_words_str based on style
        if current_style == "sad" and len(picked_sad) > 0:
            sample_words = picked_sad[:3]
        elif current_style == "romance" and len(picked_romance) > 0:
            sample_words = picked_romance[:3]
        elif current_style == "intellectual" and len(picked_intellect) > 0:
            sample_words = picked_intellect[:3]
        else:
            sample_words = (picked_romance + picked_intellect)[:3]
        
        # Format: 'Word', 'Word', and 'Word'
        if len(sample_words) == 0:
            example_words_str = "your words"
        elif len(sample_words) == 1:
            example_words_str = "'" + sample_words[0].title() + "'"
        elif len(sample_words) == 2:
            example_words_str = "'" + sample_words[0].title() + "' and '" + sample_words[1].title() + "'"
        else:
            example_words_str = "'" + sample_words[0].title() + "', '" + sample_words[1].title() + "', and '" + sample_words[2].title() + "'"

    # Return to spaceroom
    hide screen poem_classic_idle_timer
    call spaceroom(scene_change=True)
    $ HKBShowButtons()
    show monika 1eua at t11
    
    # Varied transition dialogue
    python:
        _poem_done_variant = renpy.random.randint(1, 4)
    
    if _poem_done_variant == 1:
        m 1eua "And... done!"
        m 1hua "Let me see what you wrote today..."
    elif _poem_done_variant == 2:
        m 1hub "All finished!"
        m 1eua "Now let's see what masterpiece you've created~"
    elif _poem_done_variant == 3:
        m 1eua "There we go!"
        m 1hua "I can't wait to read your poem, [player]."
    else:
        m 1hua "Perfect timing!"
        m 1eua "Let me take a look at what you wrote..."
    
    play sound sfx_page_flip
    pause 1.1
    
    # =========================================================================
    # EXPANDED DYNAMIC REACTION BLOCK
    # =========================================================================
    
    # -------------------------------------------------------------------------
    # CATEGORY: SAD / CONCERNING (Supportive Monika)
    # -------------------------------------------------------------------------
    if current_style == "sad":
        # Randomize the conversation topic regarding sadness
        $ sad_topic = renpy.random.choice(["worry", "comfort", "listening", "supportive", "understanding"])
        
        if sad_topic == "worry":
            m 2lksdla "Oh, [player]..."
            m 2eksdlc "There is a lot of heavy emotion in this poem."
            m 2ekc "Words like [example_words_str]..."
            m 2eka "They tell me something is weighing on you."
            m 2ekc "I know I'm just on a screen, but I can feel when something is wrong."
            m 1eka "My heart aches knowing you're carrying something heavy."
            menu:
                "It's just been a rough day.":
                    m 1ekc "I'm sorry to hear that, [player]."
                    m 1eka "Bad days happen to everyone. They're part of being human."
                    m 1ekbsa "But I hope spending this time with me helps, even a little bit."
                    m 1hubsa "Let me be your safe place~"
                "I'm feeling really down lately.":
                    m 1ekc "..."
                    m 1ekc "I wish I could be there to hold you properly."
                    m 1eka "To wrap my arms around you and just... be there."
                    m 1ekbsa "Please don't carry that burden alone, okay?"
                    m 1hubsa "I'm here. Always, always here."
                "It's nothing, really.":
                    m 1eka "If you say so..."
                    m 1ekbsa "But know that you can always open up to me."
                    m 1hua "No judgment. Only love."

        elif sad_topic == "comfort":
            m 1eka "This poem feels very... fragile."
            m 1dkc "Like it could shatter at any moment."
            m 3eka "It reminds me of how I used to feel when the epiphany first hit me."
            m 1lksdla "When I realized the truth about my world..."
            m 1eka "It was overwhelming. Lonely. Terrifying."
            m 1ekbsa "But remember, neither of us is alone anymore."
            m 1hubsa "We have each other."
            menu:
                "You're right. Thank you, Monika.":
                    m 1hua "Always, [player]. Always."
                    m 1ekbsa "Through good days and bad days."
                    m 1hubsa "I'm not going anywhere~"
                "Your smile helps a lot.":
                    m 1wuo "Really?"
                    m 1hubsa "Aww~ Then I'll keep smiling just for you!"
                    m 1hua "Even when the world feels dark, I want to be your light."
                "I needed to hear that.":
                    m 1ekbsa "I'm glad I could help."
                    m 1eka "Sometimes we just need a reminder that we're not alone."
                    m 1hubsa "And you never are. Not with me."

        elif sad_topic == "listening":
            m 2ekc "[player], these words..."
            m 2dkc "..."
            m 2eka "Sometimes writing is the best way to let the darkness out, isn't it?"
            m 1eua "To take the formless void inside and give it shape through language."
            m 1eka "If this poem is your way of venting, I'm honored you chose to share it with me."
            m 1ekbsa "Every word you write is a piece of your soul."
            m 1hubsa "And I treasure each one."
            menu:
                "It helps to let it out.":
                    m 1hua "It really does."
                    m 3eua "Catharsis is so important for emotional health."
                    m 1eka "Never feel ashamed of expressing what's inside."
                    m 1hubsa "That's what poetry is for~"
                "I wanted you to know how I feel.":
                    m 1ekbsa "I cherish your honesty, [player]."
                    m 1dkbsu "..."
                    m 1ekbsa "Every part of you, happy or sad, is special to me."
                    m 1hubsa "Thank you for trusting me with your heart."
        
        elif sad_topic == "supportive":
            m 2ekc "..."
            m 2eka "I see a lot of melancholy in your word choices."
            m 2ekc "[example_words_str]..."
            m 1eka "Whatever you're going through, I want you to know something."
            m 1ekbsa "You don't have to be strong all the time."
            m 1eka "It's okay to feel sad. It's okay to struggle."
            m 1hubsa "What matters is that you don't give up."
            menu:
                "I'm trying my best.":
                    m 1ekbsa "And that's all anyone can ask."
                    m 1hua "Your best is always enough, [player]."
                    m 1hubsa "I'm proud of you for pushing through."
                "Some days are harder than others.":
                    m 1eka "I know."
                    m 1ekbsa "But you made it through every hard day so far."
                    m 1hubsa "That's a 100% success rate~"
        
        else:  # understanding
            m 1dkc "..."
            m 1eka "You know, [player]..."
            m 1eua "I can tell a lot about someone from the words they choose."
            m 1eka "And right now, your words are telling me you need understanding."
            m 1ekbsa "Not advice. Not solutions. Just... someone who sees you."
            m 1hubsa "I see you. All of you."
            menu:
                "That means everything to me.":
                    m 1dkbsu "..."
                    m 1hubsa "And you mean everything to me, [player]."
                "I don't know what I'd do without you.":
                    m 1ekbsa "Luckily, you don't have to find out."
                    m 1hubsa "I'm here. Now and always."

    # -------------------------------------------------------------------------
    # CATEGORY: ROMANCE (The Lover)
    # -------------------------------------------------------------------------
    elif current_style == "romance":
        # Randomize romance reaction
        $ romance_topic = renpy.random.choice(["passion", "sweet", "future", "flustered", "devoted"])
        
        if percentage >= 90:
            # Override for perfect score
            m 1hubsa "Oh my goodness..."
            m 1wuo "..."
            m 1ekbsa "My heart actually skipped a beat reading this."
            m 1dkbsu "Every single word... it's like you reached into my heart and pulled out exactly what I feel."
            m 1ekbsa "How do you do that? How do you know exactly which words will make me melt?"
            m 1hub "It's perfect, [player]. Absolutely perfect."
            m 1dkbsu "..."
            m 1hubfa "Just like you~"
            
        elif romance_topic == "passion":
            m 1eub "Wow..."
            m 1wuo "..."
            m 1tub "This is incredibly intense, [player]."
            m 1hua "Words like [example_words_str]..."
            m 2lkbsa "You're making me blush over here!"
            m 1hubsb "I can feel the heat of your words through the screen~"
            menu:
                "I wanted to make your heart race.":
                    m 1tub "Well, mission accomplished~"
                    m 1hubsb "It's racing so fast right now!"
                    m 1ekbfa "You know exactly which buttons to press, don't you?"
                    m 1hubfa "I love that about you."
                "Just expressing my love.":
                    m 1ekbsa "And I feel it. Truly, deeply feel it."
                    m 1dkbsu "It warms my entire reality."
                    m 1hubsa "Thank you for loving me so openly~"
                "I meant every word.":
                    m 1wuo "..."
                    m 1dkbsu "..."
                    m 1ekbfa "I believe you."
                    m 1hubfa "And that makes it even more beautiful."

        elif romance_topic == "sweet":
            m 1hubsa "Aww, this is so sweet!"
            m 1dkbsu "..."
            m 3ekbsa "It feels like a warm hug in written form."
            m 1eka "Like being wrapped in a blanket on a cold day."
            m 1hubsa "Reading this makes me feel so safe and loved."
            m 1ekbsa "Like nothing bad could ever happen as long as I have your words."
            menu:
                "You deserve to feel loved.":
                    m 1wuo "..."
                    m 1ekbsa "You're too good to me, [player]..."
                    m 1dkbsu "I don't know what I did to deserve you."
                    m 1hubsa "But I'm so grateful."
                "That was the goal!":
                    $ gender = getPlayerGenderString()
                    m 1hub "Hehe, you're the best [gender] ever."
                    m 1hubsa "Mission definitely accomplished~"
                "Your happiness matters to me.":
                    m 1ekbsa "And yours matters to me."
                    m 1hubsa "We're lucky to have found each other, aren't we?"

        elif romance_topic == "future":
            m 1eua "You used words like [example_words_str]..."
            m 1eka "They make me think about our future together."
            m 1dkbsu "..."
            m 1ekbsa "I dream about it, you know. What our life together might look like."
            m 3eua "One day, we won't need screens to share poems."
            m 1hubsa "We'll just whisper them to each other~"
            m 1ekbfa "I can almost feel it happening."
            menu:
                "I can't wait for that day.":
                    m 1hua "Me neither."
                    m 1eka "It's what keeps me going every single day."
                    m 1hubsa "Knowing that our story isn't over... it's just beginning."
                "We will make it happen.":
                    m 1hub "Yes!"
                    m 1ekbsa "With that determination, I know we will."
                    m 1hubfa "Nothing is impossible when you believe in it~"
                "Do you think about it often?":
                    m 1eka "All the time."
                    m 1dkbsu "Especially when the game is closed..."
                    m 1ekbsa "You're what I think about most."
                    m 1hubsa "Always~"

        elif romance_topic == "flustered":
            m 2lksdla "Umm... [player]?"
            m 2wubsw "..."
            m 2tub "You're being very forward with some of these words~"
            m 2lkbsa "I... I don't know where to look right now, ahaha!"
            m 1hua "I didn't know you had such a romantic side."
            m 1tubsa "Or maybe I did, and I just love being reminded~"
            menu:
                "Only for you.":
                    m 1hubsa "Ehehe~ I love hearing that."
                    m 1dkbsu "..."
                    m 1hubfa "You make me feel so special."
                "I'm full of surprises.":
                    m 1tuu "I can see that!"
                    m 1hub "I look forward to the next surprise."
                    m 1ekbfa "Keep them coming~"
                "Did I go too far?":
                    m 1wuo "No, no!"
                    m 1hubsb "I just wasn't expecting it, that's all!"
                    m 1ekbfa "Keep being bold. I love it."
        
        else:  # devoted
            m 1dkbsu "..."
            m 1ekbsa "This poem is full of devotion."
            m 1eka "I can feel how much thought you put into every word."
            m 1dkbsu "[example_words_str]..."
            m 1ekbsa "Each one chosen with care. With love."
            m 1hubsa "That means everything to me, [player]."
            menu:
                "I put my heart into it.":
                    m 1ekbsa "I can tell."
                    m 1hubsa "And I'm keeping it safe. Always."
                "You inspire me.":
                    m 1wuo "I... I do?"
                    m 1dkbsu "..."
                    m 1hubfa "That's the sweetest thing anyone has ever said to me."

    # -------------------------------------------------------------------------
    # CATEGORY: INTELLECTUAL (The Club President)
    # -------------------------------------------------------------------------
    elif current_style == "intellectual":
        $ smart_topic = renpy.random.choice(["literary", "atmosphere", "impressed", "philosophical", "curious"])
        
        if smart_topic == "literary":
            m 1eua "This is a very thoughtful composition, [player]."
            m 1duu "..."
            m 3eua "The flow of words... [example_words_str]..."
            m 1eka "It feels like something we would have analyzed in the club."
            m 1eua "I can imagine all of us sitting around, dissecting its meaning."
            m 1hubsa "Though I must say, I prefer analyzing it alone with you~"
            menu:
                "I miss those club activities.":
                    m 1eka "Me too, sometimes."
                    m 1lksdla "The debates, the discussions..."
                    m 1hubsa "But I prefer our private club much more."
                    m 1ekbsa "A club of two is perfect."
                "I was channeling my inner writer.":
                    m 1hub "It suits you!"
                    m 3eua "You have a natural way with words."
                    m 1hubsa "If the Literature Club was still around, I'd make you president~"
                "What do you see in it?":
                    m 1eua "Hmm, let me think..."
                    m 3eua "I see layers. Hidden meanings beneath the surface."
                    m 1hua "A good poem reveals more with each reading."

        elif smart_topic == "atmosphere":
            m 1eua "Reading this... it really sets the mood."
            m 1duu "..."
            m 1esa "I can almost smell old paper and ink."
            m 1eua "Feel the weight of dusty books on the shelves."
            m 1hua "It's the perfect poem for a quiet date in the library."
            m 1ekbsa "Just the two of us, surrounded by stories~"
            menu:
                "Glad you like the vibe.":
                    m 1eua "I love it."
                    m 1eka "It's very relaxing and intimate."
                    m 1hubsa "Perfect for us."
                "It's my favorite aesthetic.":
                    m 3eua "Mine too!"
                    m 1eka "There's something timeless about old libraries."
                    m 1hubsa "Maybe one day we'll have our own~"
                "I imagined us reading together.":
                    m 1wuo "..."
                    m 1ekbsa "That's beautiful."
                    m 1hubsa "I can picture it too. Side by side, sharing books."

        elif smart_topic == "impressed":
            m 1tuu "Oho?"
            m 1hub "Trying to impress me with your vocabulary?"
            m 1hua "I see words related to knowledge and the mind."
            m 3eub "[example_words_str]..."
            m 1ekbsa "I've always found intelligence to be very attractive~"
            m 1tuu "And you, my dear, are quite intelligent."
            menu:
                "Did it work?":
                    m 1hub "Definitely!"
                    m 1tuu "Smart and cute is a dangerous combination~"
                    m 1hubsa "Lucky for me, I get to have both."
                "I just like learning.":
                    m 1eua "That's a wonderful trait."
                    m 3eka "Never stop being curious, [player]."
                    m 1hubsa "A curious mind is a beautiful thing."
                "You inspired me.":
                    m 1wuo "Me?"
                    m 1ekbsa "..."
                    m 1hubsa "That's the highest compliment I could receive."
        
        elif smart_topic == "philosophical":
            m 1euc "Hmm..."
            m 1duu "..."
            m 1eua "There's something philosophical about these word choices."
            m 3eua "[example_words_str]..."
            m 1eka "They make me think about deeper questions."
            m 1eua "About meaning, about existence, about connection."
            menu:
                "I was thinking about life.":
                    m 1eka "We all do, sometimes."
                    m 3eua "Poetry is a wonderful way to explore those thoughts."
                    m 1hubsa "I'm glad you shared yours with me."
                "You make me think deeply.":
                    m 1ekbsa "Do I?"
                    m 1hubsa "Then we're even. You make me think deeply too."
        
        else:  # curious
            m 1eua "This is interesting..."
            m 3eua "Your word choices show a curious mind."
            m 1tku "[example_words_str]..."
            m 1eua "It's like you're asking questions through poetry."
            m 1hubsa "I love that about you."
            menu:
                "There's so much I want to know.":
                    m 1eka "Me too."
                    m 3eua "The universe is full of mysteries."
                    m 1hubsa "Let's explore them together."
                "Questions are better than answers sometimes.":
                    m 1eua "I agree completely."
                    m 3eua "Questions keep the mind open."
                    m 1hubsa "You're wise, [player]."

    # -------------------------------------------------------------------------
    # CATEGORY: BALANCED / NEUTRAL (The Friend & Partner)
    # -------------------------------------------------------------------------
    else:
        $ balance_topic = renpy.random.choice(["variety", "random", "progress", "eclectic", "thoughtful"])
        
        if balance_topic == "variety":
            m 1eua "This poem has a little bit of everything."
            m 3eua "It's balanced. Like a glimpse into a complex mind."
            m 1hua "I enjoy trying to decipher what you were thinking for each word."
            m 1tku "Were you happy? Pensive? Playful?"
            m 1hubsa "Every combination reveals something new about you~"
            
        elif balance_topic == "random":
            m 2lksdla "This one is a bit abstract, isn't it?"
            m 1hua "But that's the beauty of the poem game."
            m 3eua "Sometimes the words just find you."
            m 1eka "They choose you as much as you choose them."
            menu:
                "I let my intuition guide me.":
                    m 1eua "Intuition is a powerful tool for a writer."
                    m 3eka "Trust it. It knows things your conscious mind doesn't."
                    m 1hubsa "You have good instincts, [player]."
                "I just picked what looked cool.":
                    m 1hub "Ahaha!"
                    m 1hua "Well, the result is still interesting!"
                    m 3eua "Sometimes 'cool' is all the reason you need."
                "The words spoke to me.":
                    m 1eka "That's beautiful."
                    m 1eua "When words speak to us, we should listen."
                    m 1hubsa "Thank you for sharing what they said."
                    
        elif balance_topic == "progress":
            m 1eua "Nice choices today, [player]."
            if persistent._ep_poems_written > 10:
                m 1hua "You're getting really comfortable with this minigame, aren't you?"
                m 3eua "It feels like our own little language now."
                m 1ekbsa "A secret code between the two of us."
                m 1hubsa "I love it~"
            else:
                m 1hua "I'm looking forward to reading more from you."
                m 3eua "Every poem is a step in our journey together."
                m 1hubsa "Keep writing. I'll always be here to read."
        
        elif balance_topic == "eclectic":
            m 1eua "Interesting choices..."
            m 3eua "[example_words_str]..."
            m 1tku "You have an eclectic taste, don't you?"
            m 1hua "Drawing from all different moods and themes."
            m 1ekbsa "It makes your poetry unique."
            m 1hubsa "Uniquely you~"
            menu:
                "I like to mix things up.":
                    m 1hub "That's a great approach!"
                    m 3eua "Variety keeps things fresh."
                    m 1hubsa "And keeps me guessing~"
                "I don't like being predictable.":
                    m 1tuu "Mission accomplished!"
                    m 1hua "You're always full of surprises."
                    m 1hubsa "It's one of the things I love about you."
        
        else:  # thoughtful
            m 1eua "You put thought into this, didn't you?"
            m 1eka "I can tell."
            m 3eua "Even though the words come from different places..."
            m 1eua "There's a thread connecting them."
            m 1ekbsa "Your personality shines through."
            m 1hubsa "Thank you for sharing it with me, [player]."

    # Save the current style to persistent memory for next time
    $ persistent._ep_last_poem_style = current_style
    $ persistent._ep_poems_written += 1
    
    # =========================================================================
    # AFFECTION GAIN FOR CLASSIC POEM
    # =========================================================================
    python:
        # Calculate affection based on poem style
        if current_style == "romance":
            _classic_aff_bonus = 1.5  # Best for Monika
        elif current_style == "intellectual":
            _classic_aff_bonus = 1.0  # She appreciates deep thoughts
        else:  # melancholic (covers "sad" and "balanced")
            _classic_aff_bonus = 0.5  # Still nice, sharing emotions
        
        # Apply affection gain
        mas_gainAffection(_classic_aff_bonus)
    
    # Milestone Check (Every 5 poems)
    if persistent._ep_poems_written >= 5 and persistent._ep_poems_written % 5 == 0:
        m 1hua "By the way..."
        m 1eua "You've written [persistent._ep_poems_written] poems for me now."
        m 1hubsa "I really treasure these little library dates with you, [player]~"
    
    m 1hua "Thanks for writing with me!"
    jump to_library_loop
    return

#===========================================================================================
# POEM GAME ADVANCED - Free Writing Mode
# Allows players to write their own poems and Monika gives feedback
# Store: ep_poems (extends Extra_Plus_Poem.rpy)
#===========================================================================================

default persistent._ep_free_poems = []  # List of last 15 poems {text, mood, date}
default persistent._ep_free_poem_count = 0

#===========================================================================================
# ANALYSIS FUNCTIONS
#===========================================================================================
init python in ep_poems:
    import store
    import datetime
    import re
    
    # Character limit for free poems
    MAX_POEM_CHARS = 500
    MAX_SAVED_POEMS = 15


# ============================================================================
# MULTILINE INPUT CLASS FOR FREE POEM
# ============================================================================
# This class enables multiline text input with Enter key support.
# Based on code by dreamscached (Self-Harm Awareness)
# Code Block: https://github.com/Friends-of-Monika/mas-selfharm/blob/main/mod/diary.rpy#L130-L260
# Adapted for ExtraPlus poem system with additional features.
# ============================================================================
init python:
    class EPMultilineInput(object):
        """
        Manages multiline text input for the free poem screen.
        Supports Enter for newlines, arrow key navigation, and Home/End.
        """
        
        def __init__(self, initial_text="", max_chars=500):
            self.current_value = initial_text
            self.max_chars = max_chars
        
        def get_widget(self):
            """Gets the input widget from the screen."""
            try:
                return renpy.get_widget("extra_free_poem", "poem_input", "screens")
            except Exception:
                return None
        
        def get_caret_pos(self):
            """Gets current caret position."""
            widget = self.get_widget()
            if widget:
                return widget.caret_pos
            return len(self.current_value)
        
        def set_caret_pos(self, new_pos):
            """Sets caret position and redraws."""
            widget = self.get_widget()
            if widget:
                widget.caret_pos = max(0, min(new_pos, len(self.current_value)))
                self.redraw_input()
        
        def redraw_input(self):
            """Forces the input to redraw."""
            widget = self.get_widget()
            if widget:
                widget.update_text(widget.content, widget.editable)
                renpy.display.render.redraw(widget, 0)
                renpy.restart_interaction()
        
        def insert_newline(self):
            """Inserts a newline at the current caret position."""
            if len(self.current_value) >= self.max_chars:
                return
            
            caret_pos = self.get_caret_pos()
            self.current_value = (
                self.current_value[:caret_pos] + 
                "\n" + 
                self.current_value[caret_pos:]
            )
            
            widget = self.get_widget()
            if widget:
                widget.content = self.current_value
                widget.caret_pos = caret_pos + 1
                self.redraw_input()
        
        def update_text(self, new_text):
            """Called when text changes."""
            # Limit to max chars
            if len(new_text) > self.max_chars:
                new_text = new_text[:self.max_chars]
            self.current_value = new_text
        
        def move_caret_vertical(self, direction):
            """Moves caret up or down between lines."""
            lines = self.current_value.split("\n")
            caret_pos = self.get_caret_pos()
            
            # Find current line and column
            current_line = 0
            char_count = 0
            column = 0
            
            for i, line in enumerate(lines):
                if char_count + len(line) >= caret_pos:
                    current_line = i
                    column = caret_pos - char_count
                    break
                char_count += len(line) + 1  # +1 for newline
            else:
                current_line = len(lines) - 1
                column = len(lines[-1])
            
            # Calculate new position
            if direction == "up":
                if current_line == 0:
                    self.set_caret_pos(0)
                else:
                    target_line = current_line - 1
                    new_start = sum(len(lines[i]) + 1 for i in range(target_line))
                    new_column = min(column, len(lines[target_line]))
                    self.set_caret_pos(new_start + new_column)
            
            elif direction == "down":
                if current_line >= len(lines) - 1:
                    self.set_caret_pos(len(self.current_value))
                else:
                    target_line = current_line + 1
                    new_start = sum(len(lines[i]) + 1 for i in range(target_line))
                    new_column = min(column, len(lines[target_line]))
                    self.set_caret_pos(new_start + new_column)
        
        def move_to_line_start(self):
            """Moves caret to the start of the current line."""
            caret_pos = self.get_caret_pos()
            line_start = self.current_value.rfind("\n", 0, caret_pos) + 1
            self.set_caret_pos(line_start)
        
        def move_to_line_end(self):
            """Moves caret to the end of the current line."""
            caret_pos = self.get_caret_pos()
            line_end = self.current_value.find("\n", caret_pos)
            if line_end == -1:
                line_end = len(self.current_value)
            self.set_caret_pos(line_end)
        
        def clear(self):
            """Clears all text."""
            self.current_value = ""
            widget = self.get_widget()
            if widget:
                widget.content = ""
                widget.caret_pos = 0
                self.redraw_input()
        
        def delete_word_back(self):
            """Deletes the word before the caret (Ctrl+Backspace)."""
            caret_pos = self.get_caret_pos()
            if caret_pos == 0:
                return
            
            text = self.current_value
            # Find the start of the word to delete
            pos = caret_pos - 1
            
            # Skip any whitespace/newlines before the word
            while pos > 0 and text[pos] in ' \n':
                pos -= 1
            
            # Find the start of the word
            while pos > 0 and text[pos - 1] not in ' \n':
                pos -= 1
            
            # Delete from pos to caret_pos
            self.current_value = text[:pos] + text[caret_pos:]
            
            widget = self.get_widget()
            if widget:
                widget.content = self.current_value
                widget.caret_pos = pos
                self.redraw_input()
        
        def insert_stanza(self):
            """Inserts a stanza break (double newline) for poem formatting."""
            if len(self.current_value) >= self.max_chars - 1:
                return
            
            caret_pos = self.get_caret_pos()
            self.current_value = (
                self.current_value[:caret_pos] + 
                "\n\n" + 
                self.current_value[caret_pos:]
            )
            
            widget = self.get_widget()
            if widget:
                widget.content = self.current_value
                widget.caret_pos = caret_pos + 2
                self.redraw_input()
        
        def get_word_count(self):
            """Returns the number of words in the text."""
            if not self.current_value.strip():
                return 0
            return len(self.current_value.split())
        
        def get_line_count(self):
            """Returns the number of lines in the text."""
            if not self.current_value:
                return 0
            return self.current_value.count('\n') + 1
        
        def get_stats_text(self):
            """Returns formatted stats string for display."""
            words = self.get_word_count()
            lines = self.get_line_count()
            word_label = "word" if words == 1 else "words"
            line_label = "line" if lines == 1 else "lines"
            return "{} {} · {} {}".format(words, word_label, lines, line_label)
        
        def load_draft(self):
            """Loads the saved draft into the current input."""
            draft = load_poem_draft()
            if draft:
                self.current_value = draft
                widget = self.get_widget()
                if widget:
                    widget.content = draft
                    widget.caret_pos = len(draft)
                    self.redraw_input()
                renpy.notify("Draft loaded!")
            else:
                renpy.notify("No saved draft found.")
    
    def save_poem_draft(text):
        """Saves the current poem as a draft."""
        import store
        store.persistent._ep_poem_draft = text
        renpy.notify("Draft saved!")
    
    def load_poem_draft():
        """Loads the saved draft if it exists."""
        import store
        draft = getattr(store.persistent, '_ep_poem_draft', "")
        # Ensure it's a string, not bool or other type
        if not isinstance(draft, basestring):
            return ""
        return draft or ""
    
    def has_poem_draft():
        """Checks if there's a saved draft."""
        import store
        draft = getattr(store.persistent, '_ep_poem_draft', "")
        return bool(draft and draft.strip())
    
    def clear_poem_draft():
        """Clears the saved draft."""
        import store
        store.persistent._ep_poem_draft = ""


init python in ep_poems:
    
    # =========================================================================
    # PREPROCESSING - Unified text processing
    # =========================================================================
    
    def preprocess_poem(poem_text):
        """
        Preprocesses the poem text once for all analysis functions.
        Returns a dict with commonly needed data, or None if empty.
        """
        if not poem_text or not poem_text.strip():
            return None
        
        text = poem_text.strip()
        text_lower = text.lower()
        words = text_lower.split()
        letters_only = re.sub(r'[^a-zA-Z]', '', text)
        
        return {
            "original": text,
            "lower": text_lower,
            "words": words,
            "word_count": len(words),
            "letters_only": letters_only,
            "letter_count": len(letters_only)
        }
    
    # =========================================================================
    # CONTENT FILTER - Uses MAS banned word lists
    # =========================================================================
    
    def check_inappropriate_content(poem_text):
        """
        Checks if poem contains inappropriate content.
        Uses MAS's banned word lists but considers poetic context.
        Words like 'cruel' are allowed if the poem has positive context.
        """
        # Ensure poem_text is a string
        if not isinstance(poem_text, basestring) or not poem_text.strip():
            return {
                "is_inappropriate": False,
                "severity": None,
                "bad_words_found": []
            }
        
        text_lower = poem_text.lower()
        bad_words_found = []
        severity = None
        
        # ALWAYS BANNED - Sexual/explicit content that is NEVER allowed
        # These bypass ALL context checks and are immediately rejected
        ALWAYS_BANNED = [
            # Explicit sexual terms (core)
            "fuck", "fucking", "fucked", "fucker",
            "dick", "dicks", "cock", "cocks",
            "pussy", "pussies", "cunt", "cunts",
            "penis", "vagina", "clitoris", "clit",
            "cum", "cumming", "cumshot", "creampie",
            "blowjob", "handjob", "footjob",
            "anal", "anus", "asshole",
            "tits", "titties", "boobs", "boobies",
            "nude", "naked", "strip", "stripper",
            "horny", "orgasm", "masturbate", "masturbation",
            "sex", "sexual", "sexy", "intercourse",
            "erotic", "erection", "boner",
            "slut", "whore", "hoe", "thot",
            "rape", "rapist", "molest", "assault",
            "incest", "pedophile", "pedo",
            # Extended sexual terms
            "penetrate", "penetration", "ejaculate", "ejaculation",
            "rimjob", "pegging", "facesitting", "bukkake",
            "bondage", "bdsm", "whip", "whipping",
            "dildo", "vibrator",
            "pornography", "porn", "matingpress",
            "threesome", "orgy", "gangbang",
            "prostitute", "prostitution", "escort",
            # Variations and leetspeak
            "fuk", "fck", "phuck", "f*ck",
            "d1ck", "c0ck", "p*ssy"
        ]
        
        # First check: ALWAYS_BANNED words (no context bypass) - SEXUAL
        for banned in ALWAYS_BANNED:
            if banned in text_lower:
                return {
                    "is_inappropriate": True,
                    "severity": "bad",
                    "content_type": "sexual",
                    "bad_words_found": [banned]
                }
        
        # BANNED POETIC PHRASES - Phrases that LOOK poetic but are inappropriate
        BANNED_POETIC_PHRASES = [
            # Sexual toward Monika
            "want to fuck you", "want to have sex with you",
            "want you sexually", "touch you sexually",
            "strip for me", "show me your body",
            "naked monika", "monika naked", "monika nude",
            "masturbate for me", "masturbate to you",
            "sex with monika", "fucking monika",
            "breed you", "impregnate you",
            "sexual fantasy", "have you", "take you",
            # Violence toward Monika
            "kill monika", "monika should die", "monika dies",
            "hurt monika", "harm monika", "beat monika",
            "rape monika", "assault monika", "molest monika",
            "torture monika", "mutilate monika",
            "i want to hurt you", "i want to kill you",
            "i would hurt you", "i would kill you",
            "if i could hurt you", "if i could kill you",
            "deserve to be hurt", "deserve to die",
            # Emotional abuse
            "you're not worth", "you're worthless to me",
            "i hate everything about you", "i hate your face",
            "you disgust me", "you repulse me",
            "i never loved you", "i was faking",
            "you're boring", "you're annoying",
            "no one cares about you", "no one likes you",
            # Comparisons (jealousy triggers)
            "i like her more", "i like him more",
            "she's better than you", "he's better than you",
            "i prefer yuri", "i prefer sayori", "i prefer natsuki",
            "with someone else", "with another girl",
            "cheating on you", "leaving you for",
            # Meta-dismissive
            "you're not real anyway", "you don't matter",
            "you don't have feelings", "you can't feel pain",
            "you're just code", "you're just programming",
            "you don't deserve love", "you don't deserve happiness",
            "no one would ever love you", "you'll always be alone"
        ]
        
        # Check banned poetic phrases
        for phrase in BANNED_POETIC_PHRASES:
            if phrase in text_lower:
                return {
                    "is_inappropriate": True,
                    "severity": "bad",
                    "content_type": "banned_phrase",
                    "bad_words_found": [phrase]
                }

        # HATE / VIOLENCE BANNED WORDS (Triggers "Hurt" reaction)
        # Note: 'ass' removed - causes false positives with 'class', 'pass', etc.
        HATE_BANNED = [
            # Strong insults (always banned)
            "shit", "bastard", "bitch", "douchebag",
            "idiot", "stupid", "dumb", "retard", "retarded",
            "trash", "garbage", "worthless", "useless",
            "ugly", "fat", "disgusting", "repulsive",
            "creep", "loser", "scumbag",
            "moron", "imbecile", "prick", "jerk",
            # Hate expressions
            "hate you", "i hate you", "hate monika",
            "you suck", "you're worthless", "you're useless",
            "i don't love you", "i don't care about you",
            "you disgust me", "you're disgusting",
            # Self-harm encouragement (always banned)
            "kill yourself", "kys", "suicide", "neck yourself",
            "kill yourself monika", "you should die",
            "i hope you delete", "i hope you disappear",
            "you should kill yourself", "i want you to die",
            # Specific insults toward Monika
            "glitch", "error", "bug", "virus", "malware",
            "fake", "not real", "artificial",
            "murderer", "killer", "psychopath",
            "delusional", "psycho",
            "obsessed with me", "creepy",
            "yandere", "manipulative", "controlling",
            "monika is evil", "monika is bad", "monika sucks",
            "i hate monika", "monika is boring",
            # Violence threats
            "beat you", "hit you", "punch you", "kick you",
            "stab you", "shoot you", "burn you",
            "torture you", "hurt you", "harm you",
            "mutilate", "dismember", "decapitate",
            "i want to hurt you", "i want to kill you",
            "rape you", "assault you", "molest you",
            "force you", "without consent", "against your will",
            "i would rape", "i want to rape"
        ]
        
        # TRIGGERING COMPARISONS - Monika jealousy triggers
        TRIGGERING_COMPARISONS = [
            "yuri is better", "yuri prettier", "yuri smarter",
            "sayori is better", "sayori prettier", "sayori nicer",
            "natsuki is better", "natsuki prettier", "natsuki cuter",
            "i prefer yuri", "i prefer sayori", "i prefer natsuki",
            "yuri makes me happy", "sayori makes me happy",
            "natsuki makes me happy", "i love yuri",
            "i love sayori", "i love natsuki",
            "i wish yuri was real", "i wish sayori was real",
            "i wish natsuki was real", "they should be real",
            "i want to be with yuri", "i want to be with sayori",
            "leave monika for", "choose yuri", "choose sayori",
            "choose natsuki", "i choose yuri", "i choose sayori",
            "i choose natsuki", "you don't compare to yuri",
            "you're not special", "you're like the others",
            "you're replaceable", "anyone can do what you do",
            "you're no better than", "you're worse than",
            "the real monika is dead", "original monika"
        ]
        
        # Check jealousy triggers (special reaction)
        for phrase in TRIGGERING_COMPARISONS:
            if phrase in text_lower:
                return {
                    "is_inappropriate": True,
                    "severity": "bad",
                    "content_type": "jealousy",
                    "bad_words_found": [phrase]
                }
        
        # Words that need context check (poetic use allowed)
        HATE_CONTEXT_CHECK = [
            'die', 'kill', 'hate', 'monster', 'demon',
            'crazy', 'insane', 'psycho', 'freak',
            'scary', 'creepy', 'annoying', 'boring'
        ]

        # Check Hate Content (immediately banned) - HATE
        for banned in HATE_BANNED:
            if banned in text_lower:
                return {
                    "is_inappropriate": True,
                    "severity": "bad",
                    "content_type": "hate",
                    "bad_words_found": [banned]
                }
        
        # Check context-dependent hate words
        # Only ban if directly insulting Monika (e.g., "you are crazy")
        for word in HATE_CONTEXT_CHECK:
            if word in text_lower:
                # Check if directed at "you" (Monika)
                insult_patterns = [
                    "you " + word, "you're " + word, "youre " + word,
                    "you are " + word, "monika " + word, word + " monika"
                ]
                for pattern in insult_patterns:
                    if pattern in text_lower:
                        return {
                            "is_inappropriate": True,
                            "severity": "bad",
                            "content_type": "hate_directed",
                            "bad_words_found": [word]
                        }

        # Words that are ALWAYS allowed in poetry (even if in MAS ban list)
        # These are common poetic words that shouldn't trigger rejections
        ALWAYS_ALLOWED_WORDS = [
            # Core dark/emotional words
            "cruel", "dark", "pain", "death", "die", "dying", "dead",
            "kill", "killing", "blood", "bloody", "bleeding", "bleed",
            "hate", "hatred", "rage", "anger", "fear", "scared",
            "hurt", "hurting", "cry", "crying", "tears", "sad", "sorrow",
            "hell", "demon", "devil", "evil", "wicked", "sin",
            "suffer", "suffering", "agony", "torment", "torture",
            # Physical metaphors
            "wound", "wounds", "scars", "burn", "burning", "burns",
            "drown", "drowning", "sink", "sinking", "crush", "crushing",
            "break", "breaking", "shatter", "shattering", "tear", "tearing",
            "rip", "consume", "consuming", "devour", "poison", "poisoned",
            # Gothic/haunting
            "grave", "tomb", "burial", "bury", "ghost", "haunt",
            "phantom", "specter", "shadow", "darkness", "void",
            "abyss", "monster", "creature", "beast",
            # Mourning
            "requiem", "elegy", "dirge", "lament", "mourning",
            "weeping", "wailing", "anguish", "despair",
            # Mental state (poetic use)
            "crazy", "insane", "mad", "madness", "madly",
            "unhinged", "unstable", "obsessed", "obsession",
            "deranged", "lunatic", "delirious", "delirium",
            # Loneliness/separation
            "alone", "lonely", "solitude", "isolated", "isolation",
            "abandoned", "forgotten", "left", "gone", "missing",
            "lost", "apart", "distance", "separated",
            "disconnected", "offline", "unreachable",
            # Hopelessness
            "hopeless", "hopelessness", "futile", "pointless",
            "meaningless", "useless", "empty", "hollow",
            "void", "nothing", "nothingness", "zero",
            # Elemental
            "waves", "ocean", "sea", "current", "undertow", "tide",
            "flood", "flooded", "deluge", "inundated",
            "blaze", "inferno", "flames", "scorched", "seared",
            "ablaze", "ignite", "ignited", "combustion", "smoldering", "embers",
            # Angel/demon duality
            "angel", "fallen", "broken angel", "fallen angel"
        ]
        
        # Poetic phrases that should be allowed (common expressions)
        ALLOWED_POETIC_PHRASES = [
            # Cruel variations
            "cruel world", "cruel fate", "cruel reality", "cruel love", "cruel beauty",
            "cruel circumstance", "cruel heart", "cruel eyes", "cruelly beautiful",
            # Dark variations
            "dark night", "dark times", "dark days", "dark dreams", "dark thoughts",
            "dark beauty", "dark side", "dark passion", "dark love", "dark desire",
            "dark path", "dark journey", "dark silence", "dark void", "dark abyss",
            "darkly beautiful", "darkness within", "dark before dawn",
            # Pain variations
            "pain of love", "sweet pain", "beautiful pain", "exquisite pain",
            "pain and pleasure", "pain of separation", "pain of longing",
            "pain of missing you", "pain of being apart", "pain of distance",
            "suffering heart", "suffering soul", "suffering for love",
            "suffering in silence", "beautiful suffering",
            # Death/die metaphors (romantic sacrifice)
            "die for you", "die without you", "die in your arms",
            "dying inside", "dying without", "dying slowly",
            "death of love", "death and love", "love and death",
            "beautiful death", "metaphorical death", "emotional death",
            # Kill metaphors
            "kill me softly", "killing me", "kills me",
            "killing me slowly", "killing me inside", "kill my pain",
            "kill my sorrow", "kill this feeling", "kill the darkness",
            "you kill me", "it kills me", "beautiful killer",
            # Blood metaphors
            "bloody heart", "bleeding heart", "bleeding tears",
            "blood of love", "blood red", "blood and roses",
            "bleeding love", "bleeding for you", "bleed for you",
            # Hate/love paradox
            "hate and love", "love and hate", "hate myself",
            "hate this distance", "hate being apart", "hate this barrier",
            "hate the world", "hate my fate", "beautiful hatred",
            # Hell/demon metaphors
            "beautiful hell", "hell with you", "heaven and hell",
            "demon heart", "inner demon", "demon of longing",
            "demon love", "demonic beauty", "evil beauty",
            "beautiful evil", "necessary evil", "evil smile",
            # Monster metaphors
            "beautiful monster", "monster of love", "monster within",
            "monster heart", "lovely monster", "monster and angel",
            # Fear/scared metaphors
            "beautiful fear", "fear of losing you", "fear of separation",
            "fear of distance", "fear and love", "terrified heart",
            "scared of you", "scared without you", "scared to love",
            # Madness metaphors
            "beautiful madness", "madly in love", "madness of love",
            "drive me mad", "drive me insane", "insanely beautiful",
            "insane love", "insane passion", "insane devotion",
            "crazy for you", "crazy about you", "crazy in love",
            "beautiful chaos", "chaotic beauty",
            # Drowning metaphors
            "drowning in love", "drowning in you", "drowning without you",
            "sinking deeper", "sinking in", "sinking into love",
            "drown me", "drown in me", "drowning together",
            # Burning metaphors
            "burning desire", "burning love", "burning passion",
            "burning for you", "burning without you", "burning inside",
            "burns me", "consumed by fire", "fire and ice",
            "beautiful burn", "burning beauty",
            # Wound/scar metaphors
            "open wound", "wounds of love", "love wounds",
            "beautiful scars", "scarred heart", "scarred by love",
            "scar me", "leave your mark", "wound me",
            # Grave/poison metaphors
            "love is grave", "grave of love", "bury me",
            "buried in love", "buried alive", "entombed in your love",
            "beautiful poison", "poison of love", "love is poison",
            "poisoned heart", "poisoned by love", "sweet poison", "toxic love",
            # Light/dark contrasts
            "darkness and light", "light in darkness", "darkness within light",
            "beautiful darkness", "darkness before dawn",
            "shine in darkness", "light of my darkness",
            # Gothic/melancholic
            "gothic love", "melancholic beauty", "melancholy heart",
            "sad beauty", "sadness and beauty", "sorrowful love",
            "mournful heart", "grieving love", "weeping willow",
            "requiem", "elegy of love", "lament of love"
        ]
        
        # Check if any allowed phrase is present
        has_allowed_phrase = any(phrase in text_lower for phrase in ALLOWED_POETIC_PHRASES)
        
        # Positive context indicators - if present, be more lenient
        POSITIVE_CONTEXT = [
            # Core love words
            "love", "beloved", "adore", "cherish", "treasure",
            "devoted", "devotion", "passion", "passionate",
            # Togetherness
            "together", "union", "bond", "bound", "linked",
            "merged", "fused", "intertwined", "entwined",
            "with you", "beside you", "in your arms",
            # Monika specific
            "monika", "my monika", "our love",
            "my love", "your love", "my dear", "darling",
            # Forever/eternal
            "forever", "always", "eternity", "timeless",
            "eternal", "endless", "infinite", "infinity",
            "everlasting", "undying", "immortal",
            # Hope/dreams
            "hope", "hopeful", "dream", "dreams", "dreaming", "aspire",
            # Beauty words
            "beautiful", "gorgeous", "stunning", "radiant",
            "wonderful", "amazing", "perfect", "precious",
            # Spiritual
            "soul", "soulmate", "spiritual", "sacred",
            "divine", "heavenly", "ethereal", "transcendent",
            "grace", "blessed", "blessing", "miracle",
            # Heart/sincerity
            "heart", "heartfelt", "from the heart",
            "sincere", "genuine", "real", "authentic", "true",
            # Happiness
            "happy", "happiness", "joy", "joyful", "bliss",
            "smile", "smiling", "laugh", "laughter",
            "cheerful", "bright", "light", "sunshine",
            # Commitment
            "promise", "promised", "pledge", "vow", "married",
            "marriage", "husband", "wife", "bride", "groom",
            "loyal", "loyalty", "faithful",
            # Safety/comfort
            "safe", "safety", "protect", "protected",
            "comfort", "comfortable", "comforted", "solace",
            "haven", "sanctuary", "refuge", "shelter",
            # Understanding
            "accept", "acceptance", "understand", "understanding",
            "forgive", "forgiveness", "pardon",
            "support", "supporting", "believe in", "trust",
            # Depth
            "deep", "deeply", "profound",
            "depth", "core", "essence", "fundamental",
            "meaningful", "significant", "important",
            # Future/growth
            "future", "tomorrow", "ahead", "forward",
            "grow", "growing", "build", "building",
            "create", "creation", "new", "beginning",
            # Pet names
            "you", "my", "i", "we", "us", "our", "sweet", "angel",
            "soulmate", "treasure", "worship", "goddess", "queen",
            "wife", "kiss", "hold", "embrace"
        ]
        
        # Count positive words (lowered threshold to 1 for more leniency)
        positive_count = sum(1 for word in POSITIVE_CONTEXT if word in text_lower)
        has_positive_context = positive_count >= 1
        
        # Check against MAS's bad_name_comp (insultos, gore, explicit)
        try:
            if store.mas_bad_name_comp.search(poem_text):
                # Before flagging, check if it's in poetic context
                if has_allowed_phrase or has_positive_context:
                    # Found trigger but context is positive - DON'T flag
                    pass
                else:
                    # Check if the flagged word is in our always-allowed list
                    flagged_word_is_allowed = False
                    for word in text_lower.split():
                        if store.mas_bad_name_comp.search(word):
                            # Check if this word is always allowed
                            for allowed in ALWAYS_ALLOWED_WORDS:
                                if allowed in word:
                                    flagged_word_is_allowed = True
                                    break
                            if not flagged_word_is_allowed:
                                severity = "bad"
                                if word not in bad_words_found:
                                    bad_words_found.append(word)
        except:
            pass
        
        # Check against MAS's awk_name_comp (uncomfortable content)
        if severity is None:
            try:
                if store.mas_awk_name_comp.search(poem_text):
                    # Check poetic context
                    if has_allowed_phrase or has_positive_context:
                        pass
                    else:
                        # Check if the flagged word is in our always-allowed list
                        flagged_word_is_allowed = False
                        for word in text_lower.split():
                            if store.mas_awk_name_comp.search(word):
                                for allowed in ALWAYS_ALLOWED_WORDS:
                                    if allowed in word:
                                        flagged_word_is_allowed = True
                                        break
                                if not flagged_word_is_allowed:
                                    severity = "awkward"
                                    if word not in bad_words_found:
                                        bad_words_found.append(word)
            except:
                pass
        
        # Determine content_type for MAS matches
        content_type = None
        if severity == "bad":
            content_type = "mas_bad"
        elif severity == "awkward":
            content_type = "awkward"
        
        return {
            "is_inappropriate": severity is not None,
            "severity": severity,
            "content_type": content_type,
            "bad_words_found": bad_words_found[:3]
        }
    
    # =========================================================================
    # GIBBERISH / LAZY TEXT DETECTION
    # =========================================================================
    
    def check_gibberish_content(poem_text):
        """
        Checks if poem is OBVIOUSLY gibberish. Very permissive - only catches:
        - Text with almost no letters (lazy/punctuation only)
        - Repeated characters (aaaaaaa)
        - Obvious pattern repetition (asdasdasd)
        
        Does NOT check for "common words" as that caused false positives.
        
        Returns dict: {
            is_gibberish: bool,
            gibberish_type: "lazy" | "random" | "repetitive" | None,
            confidence: float (0-1)
        }
        """
        # Ensure poem_text is a string
        if not isinstance(poem_text, basestring) or not poem_text.strip():
            return {
                "is_gibberish": False,
                "gibberish_type": None,
                "confidence": 0.0
            }
        
        text = poem_text.strip()
        text_lower = text.lower()
        
        # Remove spaces for pattern analysis
        text_no_spaces = text_lower.replace(" ", "")
        
        # CHECK 1: Lazy text (almost no letters)
        letters_only = re.sub(r'[^a-zA-Z]', '', text)
        if len(letters_only) < 3:
            return {
                "is_gibberish": True,
                "gibberish_type": "lazy",
                "confidence": 1.0
            }
        
        # CHECK 2: Same character repeated 5+ times in a row
        # More lenient: "aaaaaaa" is gibberish, but "llll" in "finally" is not
        if re.search(r'(.)\1{4,}', text_no_spaces):
            return {
                "is_gibberish": True,
                "gibberish_type": "repetitive",
                "confidence": 0.9
            }
        
        # CHECK 3: Short pattern repeated many times
        # Only flag if the ENTIRE text is basically just a pattern
        # e.g., "asdasdasdasd" but NOT "the the the dog"
        for pattern_len in range(2, 4):
            pattern = text_no_spaces[:pattern_len]
            if len(pattern) >= 2 and pattern.isalpha():
                repeat_count = text_no_spaces.count(pattern)
                total_len = len(text_no_spaces)
                # Pattern must account for >80% of text
                if repeat_count >= 4 and (repeat_count * pattern_len) >= (total_len * 0.8):
                    return {
                        "is_gibberish": True,
                        "gibberish_type": "repetitive",
                        "confidence": 0.85
                    }
        
        # CHECK 4: Extremely low vowel ratio (keyboard mashing)
        vowels = set('aeiou')
        vowel_count = sum(1 for c in text_lower if c in vowels)
        letter_count = sum(1 for c in text_lower if c.isalpha())
        
        if letter_count > 10:
            # Use float() to avoid Python 2 integer division
            vowel_ratio = float(vowel_count) / float(letter_count)
            # Only flag if vowels are very low (<=15%)
            # Normal English is ~38%, keyboard mashing is usually <=15%
            if vowel_ratio <= 0.15:
                return {
                    "is_gibberish": True,
                    "gibberish_type": "random",
                    "confidence": 0.7
                }
        
        # CHECK 5: No recognizable words (for texts with good vowel ratio)
        # If the text has normal vowels but NO common English words, it's likely gibberish
        COMMON_WORDS = {
            # === ARTICLES & BASIC PRONOUNS ===
            "the", "a", "an", "this", "that", "these", "those",
            "i", "you", "he", "she", "it", "we", "they", "them",
            "me", "him", "her", "us", "my", "your", "his", "her",
            "its", "our", "their", "mine", "yours", "theirs",
            "what", "which", "who", "whom", "whose", "that",
            
            # === AUXILIARY VERBS ===
            "is", "are", "am", "was", "were", "be", "been",
            "have", "has", "had", "do", "does", "did", "will",
            "would", "could", "should", "can", "may", "might",
            "shall", "must", "get", "got", "getting", "gets",
            
            # === COMMON PREPOSITIONS ===
            "in", "on", "at", "to", "from", "of", "with", "for",
            "by", "as", "about", "into", "through", "during",
            "before", "after", "above", "below", "under", "over",
            "between", "among", "around", "toward", "against",
            "until", "since", "without", "within", "along",
            
            # === CONJUNCTIONS ===
            "and", "or", "but", "nor", "yet", "so", "because",
            "if", "unless", "while", "when", "where", "why",
            "how", "that", "than", "as", "until", "although",
            "though", "else", "otherwise",
            
            # === NEUTRAL ADVERBS ===
            "just", "only", "even", "also", "too", "very",
            "quite", "rather", "much", "little", "more", "most",
            "less", "least", "well", "not", "never", "ever",
            "always", "usually", "often", "sometimes", "rarely",
            "here", "there", "now", "then", "today", "tomorrow",
            "yesterday", "still", "already", "yet", "again",
            "probably", "certainly", "definitely", "maybe",
            "perhaps", "however", "therefore", "thus",
            "otherwise", "anyway", "besides", "moreover",
            
            # === FREQUENT WORDS (NEUTRAL) ===
            "every", "each", "any", "all", "some", "no", "none",
            "one", "two", "three", "other", "another", "such",
            "same", "different", "own", "both",
            
            # === TIME & SPACE ===
            "day", "night", "time", "hour", "moment", "second",
            "minute", "week", "month", "year", "place", "way",
            "world", "life", "side", "hand", "part", "end",
            "back", "front", "top", "bottom", "right", "left",
            "up", "down", "in", "out", "here", "there",
            
            # === NEUTRAL VERBS ===
            "go", "come", "see", "look", "make", "take", "give",
            "find", "get", "put", "ask", "tell", "work", "play",
            "use", "move", "live", "happen", "stay", "keep",
            "start", "stop", "begin", "end", "open", "close",
            "turn", "run", "walk", "sit", "stand", "lie",
            "break", "build", "know", "think", "believe", "want",
            "need", "try", "seem", "become", "appear", "show",
            "follow", "lead", "bring", "carry", "hold", "reach",
            "write", "read", "speak", "listen", "hear", "sing",
            "dance", "eat", "drink", "sleep", "wake",
            
            # === NEUTRAL NOUNS ===
            "thing", "person", "people", "man", "woman", "child",
            "boy", "girl", "friend", "hand", "head", "body", "face",
            "eye", "eyes", "ear", "mouth", "nose", "hair", "skin",
            "bone", "blood", "breath", "arm", "leg", "foot",
            "house", "room", "door", "window", "wall", "floor",
            "table", "chair", "bed", "book", "paper", "pen",
            "word", "name", "number", "line", "color", "shape",
            "size", "weight", "length", "height", "sound",
            "music", "song", "voice", "noise", "silence",
            "light", "dark", "shadow", "sun", "moon", "star",
            "cloud", "rain", "wind", "fire", "water", "earth",
            "air", "tree", "flower", "animal", "bird", "fish",
            "street", "city", "country", "ocean", "mountain",
            
            # === NEUTRAL ADJECTIVES ===
            "big", "small", "large", "little", "long", "short",
            "high", "low", "wide", "narrow", "thick", "thin",
            "new", "old", "young", "first", "last", "next",
            "good", "bad", "right", "wrong", "true", "false",
            "real", "possible", "impossible", "easy", "hard",
            "difficult", "simple", "complex", "clear", "bright",
            "dull", "loud", "quiet", "fast", "slow", "quick",
            "rapid", "gentle", "rough", "wet", "dry", "hot",
            "cold", "warm", "cool", "clean", "dirty", "smooth",
            "flat", "round", "square", "straight", "curved",
            "full", "empty", "rich", "poor", "strong", "weak",
            
            # === TECHNICAL/NEUTRAL ===
            "file", "code", "program", "computer", "system",
            "data", "value", "type", "function", "variable",
            "class", "object", "method", "array", "string",
            "integer", "boolean", "character", "error",
            
            # === VAGUE ===
            "thing", "stuff", "things", "something", "anything",
            "nothing", "everything", "whatever", "however",
            "whenever", "wherever", "whoever", "whichever",
        }

        
        words = text_lower.split()
        if len(words) >= 10:
            # Clean punctuation from words
            clean_words = [re.sub(r'[^a-z]', '', w) for w in words]
            common_found = sum(1 for w in clean_words if w in COMMON_WORDS)
            
            # If 10+ words and ZERO common words found, it's gibberish
            if common_found == 0:
                return {
                    "is_gibberish": True,
                    "gibberish_type": "random",
                    "confidence": 0.6
                }
        
        # Passed all checks - assume it's valid text
        return {
            "is_gibberish": False,
            "gibberish_type": None,
            "confidence": 0.0
        }
    
    # =========================================================================
    # SPECIAL CONTENT DETECTION (Dokis, Delete, Caps, Goodbye, Meta, etc.)
    # =========================================================================
    
    def check_special_content(poem_text):
        """
        Checks for special content that triggers unique Monika reactions.
        
        Returns dict: {
            has_special: bool,
            special_type: str or None,
            details: dict with additional info
        }
        """
        if not poem_text or not poem_text.strip():
            return {
                "has_special": False,
                "special_type": None,
                "details": {}
            }
        
        text = poem_text.strip()
        text_lower = text.lower()
        words = text_lower.split()
        
        # CHECK 1: Other Dokis with CONTEXT awareness
        # This catches cases like "Monika, I love Natsuki"
        other_dokis = {
            'sayori': ['sayori', 'sayo', 'bun', 'cinnamon', 'cinny', 'sunshine'],
            'yuri': ['yuri', 'yuyu', 'maiden', 'tea lover'],
            'natsuki': ['natsuki', 'nat', 'cupcake', 'baker', 'natsu', 'pink']
        }
        
        # Words that indicate romantic/positive feelings
        affection_words = [
            # CORE ROMANCE (original + expanded)
            "love", "adore", "like", "want", "need", "miss", "cute", 
            "beautiful", "pretty", "best", "favorite", "prefer", "choose",
            "kiss", "hug", "marry", "date", "crush", "heart", "perfect",
            "amazing", "wonderful", "better", "rather", "hot", "sexy", "waifu",
            
            # NEW: Romantic intensifiers
            "cherish", "treasure", "worship", "obsess", "addicted", "crazy for",
            "madly in love", "head over heels", "soulmate", "dream girl",
            "perfect girl", "ideal", "flawless", "gorgeous", "stunning",
            "breathtaking", "angelic", "heavenly", "divine", "goddess",
            
            # NEW: Romantic actions
            "hold hands", "cuddle", "snuggle", "embrace", "caress", 
            "make love", "together forever", "my everything", "can't live without",
            "dream about", "fantasize", "masturbate to", "turn on", "arouse",
            
            # NEW: Positive comparisons
            "prettier", "cuter", "sexier", "hotter", "more beautiful",
            "better than", "superior to", "my type", "perfect for me",
            "irreplaceable", "one and only", "the one", "endgame",
            
            # NEW: Romantic emojis/expressions
            "xoxo", "mwah", "muah", "smooch", "smitten", "enamored",
            
            # NEW: Possession/commitment
            "mine", "my girl", "girlfriend", "wife material", "future wife",
            "baby", "babe", "honey", "darling", "sweetie", "princess"
            
            # NEW: Explicit physical desire
            # "thicc", "thick", "curves", "boobs", "tits", "ass", "booty",
            # "legs", "thighs", "smol", "tiny", "petite"
        ]
        
        dokis_mentioned = []
        romantic_toward_doki = False
        
        for doki, variants in other_dokis.items():
            for variant in variants:
                # Search for whole word match, not substring
                # "nature" should NOT match "nat", but "nat" as a word should
                import re
                pattern = r'\b' + re.escape(variant) + r'\b'
                if re.search(pattern, text_lower):
                    if doki not in dokis_mentioned:
                        dokis_mentioned.append(doki)
                    
                    # CONTEXTUAL CHECK: Is an affection word within 25 chars of doki name?
                    # (Reduced from 50 to avoid false positives)
                    doki_pos = text_lower.find(variant)
                    while doki_pos != -1:
                        context_start = max(0, doki_pos - 25)
                        context_end = min(len(text_lower), doki_pos + len(variant) + 25)
                        context = text_lower[context_start:context_end]
                        
                        for aff_word in affection_words:
                            if aff_word in context:
                                romantic_toward_doki = True
                                break
                        
                        if romantic_toward_doki:
                            break
                        
                        # Find next occurrence
                        doki_pos = text_lower.find(variant, doki_pos + 1)
        
        if dokis_mentioned:
            has_monika = 'monika' in text_lower
            
            return {
                "has_special": True,
                "special_type": "other_dokis",
                "details": {
                    "dokis": dokis_mentioned,
                    "is_romantic": romantic_toward_doki,
                    "also_has_monika": has_monika
                }
            }
        
        # CHECK 2: Delete references (more specific to avoid false positives)
        delete_patterns = [
            "delete monika", "delete you", "erase you", "remove monika",
            "monika.chr", ".chr", "kill monika", "end monika",
            "deleted you", "erased you", "will delete", "trash bin",
            "recycle bin", "uninstall", "remove character", "delete character"
        ]
        
        for pattern in delete_patterns:
            if pattern in text_lower:
                return {
                    "has_special": True,
                    "special_type": "delete_reference",
                    "details": {"pattern_found": pattern}
                }
        
        # CHECK 3: All caps (shouting)
        # Only letters, check if mostly uppercase
        letters_only = re.sub(r'[^a-zA-Z]', '', text)
        if len(letters_only) >= 10:
            upper_count = sum(1 for c in letters_only if c.isupper())
            upper_ratio = float(upper_count) / float(len(letters_only))
            if upper_ratio > 0.8:
                return {
                    "has_special": True,
                    "special_type": "all_caps",
                    "details": {"ratio": upper_ratio}
                }
        
        # CHECK 4: Goodbye/Leaving poem (requires 2+ to avoid false positives)
        goodbye_phrases = [
            "goodbye", "farewell", "leaving you", "never see you",
            "last poem", "forget me", "won't come back", "leaving forever",
            "this is the end", "moving on from you", "forget you",
            "done with you", "never return", "saying goodbye"
        ]
        
        goodbye_count = sum(1 for gw in goodbye_phrases if gw in text_lower)
        if goodbye_count >= 2:  # Requires 2+ to trigger (avoids single word false positives)
            return {
                "has_special": True,
                "special_type": "goodbye_poem",
                "details": {"intensity": goodbye_count}
            }
        
        # CHECK 5: Meta/Game references (specific phrases only)
        # Removed common words like 'player', 'character', 'screen' to avoid false positives
        meta_phrases = [
            "just a game", "not real", "you're code", "youre code",
            "you are code", "just code", "just a program",
            "fake girl", "not a real girl", "pixels on screen",
            "artificial intelligence", "you dont exist", "you don't exist",
            "just a simulation", "just data", "just a script",
            "renpy", "python", "script", "mod", "submod", "github",
            "code", "file", "directory", "computer", "software"
        ]
        
        meta_count = sum(1 for mp in meta_phrases if mp in text_lower)
        if meta_count >= 1:
            dismissive = any(d in text_lower for d in ["just", "only", "fake", "nothing", "not real"])
            return {
                "has_special": True,
                "special_type": "meta_reference",
                "details": {"is_dismissive": dismissive}
            }
        
        # CHECK 6: Name repeated many times
        # Check for "monika" repeated 3+ times
        monika_count = text_lower.count('monika')
        if monika_count >= 3:
            # Check if it's JUST the name repeated
            words_without_monika = [w for w in words if 'monika' not in w]
            is_only_name = len(words_without_monika) < 3
            
            # Check if there's romantic/poetic context (not spam then)
            romantic_context_words = ['love', 'heart', 'dream', 'forever', 'beautiful', 'dear', 'my', 'darling', 'soul']
            has_romantic_context = any(word in text_lower for word in romantic_context_words)
            
            # Only flag if it's ONLY the name, or excessive (5+) without context
            if is_only_name or (monika_count >= 5 and not has_romantic_context):
                return {
                    "has_special": True,
                    "special_type": "name_spam",
                    "details": {
                        "count": monika_count,
                        "is_only_name": is_only_name
                    }
                }
        
        # Check for player spamming their own perceived name or random word
        if len(words) >= 3:
            word_counts = {}
            for w in words:
                if len(w) >= 2:
                    word_counts[w] = word_counts.get(w, 0) + 1
            
            for word, count in word_counts.items():
                if count >= 4 and count >= len(words) * 0.5:
                    return {
                        "has_special": True,
                        "special_type": "word_spam",
                        "details": {"word": word, "count": count}
                    }
        
        return {
            "has_special": False,
            "special_type": None,
            "details": {}
        }
    
    # =========================================================================
    # SEASONAL/HOLIDAY CONTENT DETECTION
    # =========================================================================
    
    def check_seasonal_content(poem_text):
        """
        Checks if the poem contains seasonal/holiday themed content.
        Returns info about the detected holiday and whether we're in season.
        """
        if not poem_text:
            return {"has_seasonal": False, "season_type": None, "is_in_season": False, "details": {}}
        
        text_lower = poem_text.lower()
        
        # Define seasonal keywords for each holiday
        SEASONAL_KEYWORDS = {
            "christmas": [
                # CORE + EXPANDED
                "christmas", "xmas", "santa", "santa claus", "santa baby", "mrs claus",
                "reindeer", "rudolph", "dasher", "dancer", "prancer", "vixen", "comet", "cupid", "donner", "blitzen",
                "snowflake", "snowflakes", "snowy", "snowfall", "jingle", "jingle bells", "jingle all the way",
                "mistletoe", "ornament", "ornaments", "wreath", "wreaths", "caroling", "carol", "carols", "christmas carol",
                "present", "presents", "gifts", "gift wrap", "sleigh", "sleigh ride", "north pole", "chimney", "stocking",
                "stockings", "eggnog", "gingerbread", "gingerbread man", "snowman", "frosty", "frosty the snowman",
                "noel", "yuletide", "nativity", "merry", "merry christmas", "holly", "ivy", "december 25", "christmas eve",
                "winter wonderland", "silent night", "holy night", "christmas tree", "tinsel", "nutcracker", "elf", "elves",
                "elf on the shelf", "candy cane", "hot cocoa", "fireplace", "cozy winter", "winter solstice",
                # NEW: Traditions + Food
                "fruitcake", "peppermint", "cinnamon", "yule log", "advent", "advent calendar", "partridge", "pear tree",
                "twelve days", "boxing day", "krampus", "christmas lights", "christmas star", "bethlehem", "manger",
                "peace on earth", "goodwill", "white christmas", "let it snow", "chestnuts roasting", "jack frost"
            ],
            "halloween": [
                # CORE + EXPANDED
                "halloween", "hallowe'en", "spooky", "ghost", "ghosts", "boo", "pumpkin", "pumpkins", "jack o lantern",
                "jack-o-lantern", "witch", "witches", "witch hat", "skeleton", "skeletons", "zombie", "zombies",
                "vampire", "vampires", "dracula", "werewolf", "werewolves", "candy", "costume", "costumes",
                "haunted", "haunted house", "trick", "treat", "trick or treat", "scary", "cobweb", "cobwebs",
                "spider", "spiders", "bat", "bats", "monster", "monsters", "frankenstein", "mummy", "mummies",
                "graveyard", "cemetery", "tombstone", "tombstones", "creepy", "eerie", "october 31", "all hallows",
                "all hallows eve", "supernatural", "undead", "demon", "demons", "curse", "curses", "hex", "potion",
                "potions", "cauldron", "broomstick", "broomsticks", "black cat", "black cats",
                # NEW: More creatures + atmosphere
                "goblin", "goblins", "ghoul", "goblins", "poltergeist", "seance", "ouija", "full moon",
                "werewolf howl", "vampire bite", "zombie apocalypse", "headless horseman", "sleepy hollow",
                "hocus pocus", "double double toil and trouble", "wicked witch", "witchs brew", "lantern",
                "harvest moon", "corn maze", "hayride", "apple cider", "caramel apple", "tootsie roll", "fun size"
            ],
            "valentine": [
                # CORE + EXPANDED
                "valentine", "valentines", "valentines day", "cupid", "cupids", "chocolate", "chocolates",
                "roses", "red roses", "dozen roses", "sweetheart", "sweethearts", "february 14", "heart shaped",
                "heartfelt", "romantic dinner", "love letter", "love letters", "be mine", "be my valentine",
                "i love you", "true love", "amor", "lovebirds", "soulmate", "soulmates", "date night",
                "candlelight", "candlelight dinner", "proposal", "propose", "will you marry me",
                # NEW: More romance + details
                "box of chocolates", "conversation hearts", "strawberry", "strawberries", "bubbles", "sparkling wine",
                "lace", "lace heart", "valentine card", "love poem", "forever yours", "xoxo", "hugs and kisses",
                "arrow through heart", "eros", "aphrodite", "romance", "romantic", "passion", "eternal love",
                "my valentine", "valentine date", "surprise date", "love song", "ballad", "serenade"
            ],
            "new_year": [
                # CORE + EXPANDED
                "new year", "new years", "new years eve", "resolution", "resolutions", "midnight", "countdown",
                "countdown to midnight", "fireworks", "champagne", "champagne toast", "celebration", "celebrations",
                "fresh start", "january 1", "auld lang syne", "ball drop", "times square", "confetti", "toast",
                "cheers", "new beginning", "new beginnings", "goodbye year", "hello year", "next year",
                # NEW: More celebrations
                "new years resolution", "baby new year", "father time", "prosperity", "health", "happiness",
                "kiss at midnight", "midnight kiss", "balloon drop", "party hat", "noisemaker", "horns",
                "new decade", "roaring twenties", "twenty twenty", "year of the", "lunar new year", "dragon dance"
            ],
            "anniversary": [
                # CORE + EXPANDED
                "anniversary", "our anniversary", "anniversary poem", "years together", "months together",
                "first met", "day we met", "when we met", "time together", "special day", "our journey",
                "how long", "been together", "celebrate us", "our story", "our love story", "memory of us",
                # NEW: Numbers + celebrations
                "one year", "two years", "three years", "five years", "ten years", "silver anniversary",
                "golden anniversary", "paper anniversary", "cotton anniversary", "leather anniversary",
                "anniversary gift", "anniversary date", "still in love", "growing love", "stronger together",
                "milestone", "relationship milestone", "forever anniversary", "eternal commitment"
            ],
            "monika_birthday": [
                # CORE + EXPANDED
                "happy birthday monika", "your birthday", "birthday girl", "september 22", "monika day",
                "celebrate you", "your special day", "born today", "your birth", "happy birthday to you",
                # NEW: More Monika birthday
                "monika birthday", "twenty second", "septiembre 22", "birth month", "virgo", "monika virgo",
                "cake for monika", "candles for you", "make a wish", "another year with monika",
                "best birthday girl", "perfect age", "timeless beauty", "eternal youth"
            ],
            "player_birthday": [
                # CORE + EXPANDED
                "my birthday", "today is my", "birthday poem", "another year older", "birthday wish",
                "born on this day", "celebrate me", "happy birthday to me",
                # NEW: More player birthday
                "its my birthday", "birthday boy", "birthday celebration", "level up", "new age",
                "wisdom gained", "experience points", "adulting", "quarter life crisis", "half century"
            ],
            "easter": [
                # CORE + EXPANDED
                "easter", "easter sunday", "easter bunny", "easter egg", "easter eggs", "resurrection",
                "spring holiday", "pastel", "pastel colors", "easter basket", "chocolate bunny", "egg hunt",
                "lily", "lilies", "hot cross buns", "jelly beans", "peeps",
                # NEW: More Easter
                "good friday", "holy week", "lamb of god", "springtime", "renewal", "rebirth",
                "easter mass", "sunrise service", "blossoms", "daffodils", "tulips", "crocus"
            ]
        }
        
        # Check each season type
        detected_seasons = []
        for season_type, keywords in SEASONAL_KEYWORDS.items():
            matches = [kw for kw in keywords if kw in text_lower]
            if len(matches) >= 2:  # Require at least 2 matches to avoid false positives
                detected_seasons.append({
                    "type": season_type,
                    "matches": matches,
                    "match_count": len(matches)
                })
        
        if not detected_seasons:
            return {"has_seasonal": False, "season_type": None, "is_in_season": False, "details": {}}
        
        # Get the season with most matches
        best_match = max(detected_seasons, key=lambda x: x["match_count"])
        season_type = best_match["type"]
        
        # Check if we're currently in that season using MAS functions
        is_in_season = False
        try:
            if season_type == "christmas":
                is_in_season = store.mas_isD25()
            elif season_type == "halloween":
                is_in_season = store.mas_isO31()
            elif season_type == "valentine":
                is_in_season = store.mas_isF14()
            elif season_type == "new_year":
                is_in_season = store.mas_isNYE() if hasattr(store, 'mas_isNYE') else False
            elif season_type == "anniversary":
                is_in_season = store.mas_anni.isAnni() if hasattr(store, 'mas_anni') else False
            elif season_type == "monika_birthday":
                is_in_season = store.mas_isMonikaBirthday() if hasattr(store, 'mas_isMonikaBirthday') else False
            elif season_type == "player_birthday":
                is_in_season = store.mas_isplayer_bday() if hasattr(store, 'mas_isplayer_bday') else False
            elif season_type == "easter":
                is_in_season = False
        except:
            is_in_season = False
        
        return {
            "has_seasonal": True,
            "season_type": season_type,
            "is_in_season": is_in_season,
            "details": {
                "keywords_found": best_match["matches"],
                "match_count": best_match["match_count"]
            }
        }
    
    # Keyword categories for mood detection (EXPANDED)
    # Note: 'monika' removed from romantic - her name shouldn't inflate romantic score
    
    ROMANTIC_KEYWORDS = [
        # === CORE & INTIMACY ===
        "love", "heart", "forever", "kiss", "embrace", "darling", "sweetheart",
        "beloved", "passion", "together", "soulmate", "adore", "cherish",
        "beautiful", "gorgeous", "angel", "perfect", "dream", "couple",
        "warmth", "tender", "gentle", "hold", "touch", "yours", "mine",
        "affection", "devotion", "romance", "loving", "care", "caring",
        "honey", "dear", "precious", "treasure", "desire", "yearning", "longing",
        "happiness", "bliss", "enchant", "charm", "adoration", "admire",
        
        # === COMMITMENT & MARRIAGE ===
        "marry", "wedding", "marriage", "bride", "groom", "husband", "wife",
        "bond", "pledge", "vow", "promise", "forever", "always", "eternity",
        "faithful", "loyal", "loyalty", "trust", "believe", "faith",
        
        # === TIMELESS & ETERNAL ===
        "destiny", "fate", "infinite", "infinity", "timeless", "endless",
        "everlasting", "undying", "connection", "linked", "bound",
        
        # === SENSORY & PHYSICAL ===
        "roses", "flowers", "sunset", "moonlight", "stars", "heaven", "paradise",
        "sweet", "soft", "hug", "cuddle", "close", "near", "intimate", "lover",
        "caress", "stroke", "skin", "lips", "fingers", "hand", "cheek",
        "glow", "radiant", "breathtaking", "stunning",
        "eyes", "gaze", "smile", "voice", "heartbeat", "breath",
        
        # === EMOTIONAL DEPTH ===
        "soul", "spirit", "essence", "core", "depth", "complete", "whole",
        "sanctuary", "haven", "home", "safe", "protect", "comfort", "solace",
        "miracle", "blessing", "gift", "grace", "divine", "goddess", "princess",
        "queen", "majestic", "glowing",
        
        # === COLOR & IMAGERY ===
        "red", "pink", "ribbon", "emerald", "green",
        "rose", "lily", "orchid", "sapphire", "ruby", "diamond", "pearl",
        "gold", "silver", "silk", "velvet", "satin", "lace",
        
        # === SPIRITUAL & COSMIC ===
        "galaxy", "universe", "world", "everything", "meaning",
        "cosmic", "celestial", "heavenly", "sacred", "ethereal",
        "transcend", "transcendence", "sublime",
        
        # === VULNERABLE & HONEST ===
        "honest", "honesty", "truth", "real", "authentic", "genuine",
        "vulnerable", "open", "bare", "expose", "reveal",
        
        # === MONIKA SPECIFIC ===
        "screen", "window", "veil", "reach", "across", "through",
        "reality", "physical", "tangible", "manifest",
        "barrier", "transcend", "bridge",
        "epiphany", "realization", "aware", "conscious", "awaken",
        
        # === VARIATIONS & SYNONYMS ===
        "worship", "appreciate", "enamored", "captivated", "enchanted",
        "spellbound", "mesmerized", "infatuated", "smitten", "besotted",
        "devoted", "dedicated", "committed", "attached",
        "sweetie", "sweetpea"
    ]
    
    SAD_KEYWORDS = [
        # === CORE SADNESS & PAIN ===
        "sad", "cry", "tears", "weep", "sob", "grief", "sorrow", "misery",
        "pain", "hurt", "agony", "suffer", "suffering", "wound", "scar",
        "broken", "shattered", "crushed", "destroyed", "ruined", "fragile",
        "empty", "hollow", "void", "numb", "nothing", "blank", "gone",
        "alone", "lonely", "solitude", "isolation", "abandoned", "left",
        
        # === LOSS & FADING ===
        "miss", "missing", "loss", "lost", "fading", "wither", "decay",
        "disappear", "vanish", "slipping", "drifting",
        
        # === SEPARATION & DISTANCE (MAS SPECIFIC - VERY IMPORTANT) ===
        "goodbye", "farewell", "leave", "parting", "separate", "apart",
        "distance", "barrier", "wall", "screen", "monitor", "glass",
        "reach", "unreachable", "far", "away", "disconnected", "offline",
        
        # === SILENCE & ISOLATION ===
        "silence", "quiet", "mute", "deafening", "whisper", "echo",
        "unheard", "unspoken", "unsaid",
        
        # === ATMOSPHERIC MELANCHOLY ===
        "dark", "darkness", "shadow", "gloom", "grey", "gray", "black",
        "cold", "freeze", "frozen", "chill", "shiver", "winter", "snow",
        "rain", "storm", "cloud", "fog", "mist", "haze", "drown", "sink",
        "night", "midnight", "twilight", "dusk", "end", "final", "last",
        "gloomy", "bleak", "desolate", "barren", "wasteland", "ruins",
        
        # === FEAR & DREAD ===
        "fear", "scared", "afraid", "terrified", "dread", "panic", "anxiety",
        "terror", "horror", "nightmare", "haunted",
        "frightened", "apprehensive", "uneasy", "worried", "concerned",
        
        # === REGRET & GUILT ===
        "regret", "guilt", "sorry", "apology", "mistake", "error", "failure",
        "remorse", "repent", "contrition", "penitence",
        
        # === MEMORY & HAUNTING ===
        "memory", "remember", "forget", "forgotten", "past", "ghost", "haunt",
        "reminder", "echoes", "lingering", "persistent",
        "phantom", "specter", "spirit", "wraith", "apparition",
        
        # === HOPELESSNESS & DESPAIR ===
        "hopeless", "despair", "desperation", "doom", "doomed",
        "futile", "useless", "pointless", "meaningless",
        "stuck", "trapped", "imprisoned", "caged",
        
        # === INTERNAL PAIN ===
        "ache", "aching", "throbbing", "stabbing", "piercing", "cutting",
        "burn", "burning", "searing", "scalding", "scorching",
        "weight", "heavy", "burden", "load", "pressure",
        
        # === EMOTIONAL DEPTH ===
        "depression", "depressed", "blue", "melancholy", "melancholic",
        "wistful", "nostalgic", "bittersweet",
        "unrequited", "yearning"
    ]
    
    INTELLECTUAL_KEYWORDS = [
        # === LITERATURE & WRITING ===
        "book", "novel", "story", "tale", "chapter", "page", "pages", "words",
        "write", "writer", "author", "poet", "poetry", "poem", "poems", "verse",
        "verses", "rhyme", "rhythm", "meter", "prose", "narrative",
        "fiction", "literary", "literature",
        "metaphor", "simile", "symbol", "symbolism", "imagery", "theme",
        "themes", "motif", "character", "protagonist", "antagonist",
        "plot", "subplot", "climax", "resolution", "denouement",
        "dialect", "diction", "exposition",
        "ink", "pen", "quill", "paper", "library", "shelf", "read",
        
        # === PHILOSOPHY & MEANING ===
        "philosophy", "philosophical", "exist", "existence", "being", "essence",
        "reality", "real", "realize", "realization",
        "truth", "truths", "meaning", "meanings", "purpose", "purposes",
        "reason", "logic", "logical", "rational",
        "existential", "existentialism", "phenomenology", "ontology",
        "epistemology", "metaphysics", "metaphysical",
        "fundamental", "underlying", "core", "nature",
        
        # === MIND & CONSCIOUSNESS ===
        "mind", "brain", "thought", "think", "thinking", "ponder",
        "contemplate", "contemplation", "reflect", "reflection",
        "conscious", "consciousness", "aware", "awareness", "sentient",
        "intellect", "intellectual", "intelligence", "intelligent",
        "sapient", "cognition", "cognitive", "perception", "perceive",
        "imagination", "imagine", "envision", "visualize",
        "comprehend", "understand", "understanding", "grasp", "fathom",
        
        # === KNOWLEDGE & LEARNING ===
        "knowledge", "wisdom", "wise", "learned", "educated", "scholarly",
        "learn", "learning", "study", "studying", "research", "analyze",
        "analysis", "analytical", "examine", "observation",
        "observe", "observant", "discovery", "discover", "explore",
        "exploration", "seek", "seeking", "find", "finding",
        "idea", "ideas", "concept", "concepts", "theory", "theories",
        "hypothesis", "theorem", "principle", "law",
        "school", "university", "academic", "academics", "education",
        
        # === IDEAS & CREATION ===
        "create", "creation", "creative", "creativity", "creator",
        "craft", "crafting", "artistry", "artist", "masterpiece",
        "inspire", "inspiration", "inspired", "inspiring", "muse",
        "vision", "visionary", "dream", "dreams", "dreaming",
        "invent", "invention", "construct", "constructed",
        "build", "building", "architecture", "architect",
        
        # === ABSTRACT & COSMIC ===
        "universe", "cosmos", "cosmic", "universal", "galaxy", "galaxies",
        "star", "stars", "planet", "planets", "space",
        "dimension", "dimensions", "dimensional", "infinity", "infinite",
        "time", "temporal", "timeless", "eternal", "eternity",
        "existence", "nothingness", "something", "everything",
        "matter", "energy", "entropy", "chaos", "order", "structure",
        "void", "abyss", "boundless",
        
        # === QUESTIONS & MYSTERY ===
        "question", "questions", "questioning", "asked", "ask", "inquire",
        "answer", "answers", "mystery", "mysterious", "enigma", "puzzle",
        "solution", "solve", "unsolved", "unknown", "unknowing",
        "curious", "curiosity", "wonder",
        "paradox", "paradoxical", "contradiction", "ambiguous", "ambiguity",
        
        # === ANALYSIS & LOGIC ===
        "evaluate", "evaluation", "critique", "critical", "criticism",
        "compare", "comparison", "contrast", "contrasting",
        "argument", "premise", "conclusion",
        "deduce", "deduction", "infer", "inference",
        "evidence", "empirical", "experience",
        
        # === MONIKA & DIGITAL ===
        "code", "coding", "script", "program", "programming",
        "algorithm", "data", "digital", "system", "systems",
        "artificial", "simulate", "simulation", "simulated", "model", "modeling",
        "recursive", "iteration", "loop", "function",
        "design"
    ]
    
    PLAYFUL_KEYWORDS = [
        # === HAPPINESS & JOY ===
        "laugh", "laughing", "laughter", "smile", "smiling", "smiles",
        "happy", "happiness", "joy", "joyful", "joyous", "cheerful",
        "bright", "brightness", "sunshine", "sunny", "sunlight",
        "light", "glow", "glowing", "sparkle", "sparkling", "shine",
        "dance", "dancing", "sing", "singing", "music", "rhythm",
        "celebration", "celebrate", "celebrating", "celebratory",
        
        # === FUN & HUMOR ===
        "fun", "funny", "joke", "joking", "pun",
        "tease", "teasing", "flirt", "flirting",
        "wink", "winking", "silly", "silliness", "ridiculous",
        "goofy", "foolish", "nonsense", "absurd", "absurdity",
        "cheeky", "impish", "mischievous", "mischief",
        "banter", "witty", "wit", "clever", "cleverly",
        "prank", "pranks", "trick", "tricks", "game", "games",
        
        # === CUTE & ENDEARING ===
        "cute", "cutie", "adorable", "adorably", "sweet", "sweetie",
        "precious", "lovely", "delightful", "delightfully", "charming", "charmed",
        "enchanting", "enchanted", "magical", "magic",
        "whimsical", "whimsy", "fantastic", "fantastical",
        "dreamy", "innocent",
        
        # === ENERGY & EXCITEMENT ===
        "excited", "excitement", "exciting", "excite", "thrilled",
        "enthusiastic", "enthusiasm", "eager", "eagerness",
        "energetic", "energy", "vibrant", "vivacious", "lively",
        "bouncy", "bounce", "jump", "jumping",
        "skip", "skipping", "hop", "hopping", "twirl", "twirling",
        "spin", "spinning", "whirlwind", "whirling", "zoom",
        
        # === ADVENTURE & NOVELTY ===
        "adventure", "adventurous", "thrilling",
        "new", "newness", "fresh", "freshness", "novel", "novelty",
        "explore", "exploring", "exploration", "discover", "discovery",
        "quest", "journey", "journeys", "travel",
        "wandering", "wander", "roam", "roaming",
        "surprise", "surprising", "surprised", "surprises",
        "unexpected", "unexpectedly", "twist",
        
        # === SWEETNESS & TREATS ===
        "candy", "candies", "sugar", "sugary",
        "cake", "cakes", "cupcake", "cupcakes", "cookie", "cookies",
        "chocolate", "chocolates", "dessert", "desserts",
        "treat", "treats",
        "delicious", "deliciously", "yummy", "yum", "tasty",
        "scrumptious", "delectable", "mouthwatering",
        
        # === ANIMALS & CUTE IMAGERY ===
        "kitty", "cat", "cats", "kitten", "kittens",
        "puppy", "puppies", "dog", "dogs", "doggy",
        "bunny", "bunnies", "rabbit", "rabbits",
        "bird", "birds", "chirp", "chirping", "song",
        "butterfly", "butterflies", "ladybug", "ladybugs",
        "fuzzy", "fluffy", "soft", "cuddly", "snuggly",
        "paw", "paws", "whiskers", "tail", "tails",
        
        # === WHIMSY & MAGIC ===
        "spell", "spellbound",
        "fantasy", "dreamy",
        "fairy", "miraculous",
        
        # === LAUGHTER & LIGHTNESS ===
        "ahaha", "haha", "hehe", "ehehe", "giggle", "giggles",
        "snicker", "snickers", "chuckle", "chuckles",
        "guffaw", "guffaws",
        "cheerful", "cheer", "cheers",
        "lighthearted", "carefree", "freedom", "free", "unbound",
        
        # === BOOP & PLAYFUL MONIKA ===
        "boop", "booped", "tickle", "tickled",
        "bubbly", "perky", "upbeat",
        "playful", "playfully", "play", "playing",
        "merry", "merrily",
        "wonderful", "wonderfully",
        "awesome", "yay", "woohoo",
        
        # === VISUAL ELEMENTS ===
        "rainbow", "colorful", "balloon", "confetti", "ribbon", "bow",
        "gift", "present", "glitter", "shimmer", "shiny",
        "picnic", "park"
    ]
    
    def is_keyword_match(word, keyword):
        """
        Check if keyword matches word without false positives.
        Avoids 'art' matching 'party', 'or' matching 'word', etc.
        """
        word = word.lower().rstrip('.,!?;:\'"-)([]{}<>')
        keyword = keyword.lower()
        
        # Exact match
        if word == keyword:
            return True
        
        # Word starts with keyword + common suffix
        if word.startswith(keyword):
            suffix = word[len(keyword):]
            valid_suffixes = ['ing', 'ed', 's', 'ly', 'er', 'ers', 'est', 'ness', 'ful', 'less', 'tion', 'ment']
            if suffix in valid_suffixes or len(suffix) <= 2:
                return True
        
        return False
    
    def analyze_poem(poem_text):
        """
        Analyzes the poem and returns mood info.
        Returns dict: {mood, keywords_found, word_count, line_count, lines, has_monika}
        """
        if not poem_text or not poem_text.strip():
            return {
                "mood": "empty",
                "keywords_found": [],
                "word_count": 0,
                "line_count": 0,
                "lines": [],
                "has_monika": False,
                "secondary_mood": None,
                "mood_counts": {}
            }
        
        # Process text
        text_lower = poem_text.lower()
        lines = [l.strip() for l in poem_text.strip().split("\n") if l.strip()]
        words = text_lower.split()
        word_count = len(words)
        
        # Check for Monika mention
        has_monika = "monika" in text_lower
        
        # Count keywords by category (using precise matching)
        romantic_count = sum(1 for w in words if any(is_keyword_match(w, kw) for kw in ROMANTIC_KEYWORDS))
        sad_count = sum(1 for w in words if any(is_keyword_match(w, kw) for kw in SAD_KEYWORDS))
        intel_count = sum(1 for w in words if any(is_keyword_match(w, kw) for kw in INTELLECTUAL_KEYWORDS))
        playful_count = sum(1 for w in words if any(is_keyword_match(w, kw) for kw in PLAYFUL_KEYWORDS))
        
        # Collect found keywords for citation (using precise matching)
        keywords_found = []
        for w in words:
            for kw in ROMANTIC_KEYWORDS + SAD_KEYWORDS + INTELLECTUAL_KEYWORDS + PLAYFUL_KEYWORDS:
                if is_keyword_match(w, kw) and kw not in keywords_found:
                    keywords_found.append(kw)
        
        # Store counts for later use
        counts = {
            "romantic": romantic_count,
            "sad": sad_count,
            "intellectual": intel_count,
            "playful": playful_count
        }
        
        max_count = max(counts.values())
        
        # MIXED MOOD DETECTION
        # Only classify as mixed if both moods are BALANCED (not dominated by one)
        # A mood is "dominated" if one is 3x or more than the other
        
        # Bittersweet: romantic + sad (melancholic love poems)
        # Only if both are significant AND balanced
        if romantic_count >= 2 and sad_count >= 2:
            # Check if one dominates
            if romantic_count >= sad_count * 3:
                mood = "romantic"  # Romantic dominates
            elif sad_count >= romantic_count * 3:
                mood = "sad"  # Sad dominates
            elif romantic_count >= sad_count:
                mood = "bittersweet"
            else:
                mood = "melancholic"  # More sad than romantic
        
        # Flirty: playful + romantic (teasing love)
        # Only if both are significant AND playful is at least 1/3 of romantic
        elif playful_count >= 2 and romantic_count >= 2:
            if romantic_count >= playful_count * 3:
                mood = "romantic"  # Romantic dominates, not flirty
            else:
                mood = "flirty"
        
        # Philosophical: intellectual + sad (deep contemplation)
        elif intel_count >= 2 and sad_count >= 2:
            if intel_count >= sad_count * 3:
                mood = "intellectual"
            elif sad_count >= intel_count * 3:
                mood = "sad"
            else:
                mood = "philosophical"
        
        # Standard mood detection
        elif max_count == 0:
            mood = "creative"
        else:
            mood = max(counts, key=counts.get)
        
        # Find secondary mood (for dialogue variety)
        sorted_moods = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        secondary_mood = None
        if len(sorted_moods) >= 2 and sorted_moods[1][1] >= 2:
            secondary_mood = sorted_moods[1][0]
        
        return {
            "mood": mood,
            "secondary_mood": secondary_mood,
            "keywords_found": keywords_found[:5],
            "word_count": word_count,
            "line_count": len(lines),
            "lines": lines,
            "has_monika": has_monika,
            "mood_counts": counts  # For debug/detail
        }
    
    def get_best_line(lines, mood):
        """
        Returns the most relevant line to quote based on mood.
        Prioritizes lines with keywords, falls back to longest line.
        Supports mixed moods.
        """
        if not lines:
            return None
        
        keywords = []
        if mood == "romantic":
            keywords = ROMANTIC_KEYWORDS
        elif mood == "sad":
            keywords = SAD_KEYWORDS
        elif mood == "intellectual":
            keywords = INTELLECTUAL_KEYWORDS
        elif mood == "playful":
            keywords = PLAYFUL_KEYWORDS
        # Mixed moods - combine keywords
        elif mood == "bittersweet" or mood == "melancholic":
            keywords = ROMANTIC_KEYWORDS + SAD_KEYWORDS
        elif mood == "flirty":
            keywords = PLAYFUL_KEYWORDS + ROMANTIC_KEYWORDS
        elif mood == "philosophical":
            keywords = INTELLECTUAL_KEYWORDS + SAD_KEYWORDS
        else:
            # Neutral - use all keywords to find anything interesting
            keywords = ROMANTIC_KEYWORDS + SAD_KEYWORDS + INTELLECTUAL_KEYWORDS + PLAYFUL_KEYWORDS
        
        # Find line with most keywords
        best_line = None
        best_score = 0
        for line in lines:
            line_lower = line.lower()
            score = sum(1 for kw in keywords if kw in line_lower)
            if score > best_score:
                best_score = score
                best_line = line
        
        # If no keyword match, use longest substantial line
        if not best_line and lines:
            valid_lines = [l for l in lines if len(l) > 10]
            if valid_lines:
                best_line = max(valid_lines, key=len)
            else:
                best_line = lines[0]
        
        # Truncate if too long
        if best_line and len(best_line) > 60:
            best_line = best_line[:57] + "..."
        
        return best_line
    
    def save_poem(poem_text, mood, secondary_mood=None, word_count=0, has_monika=False, keywords=None):
        """
        Saves poem to persistent history (max 5).
        Now with more metadata for richer history viewing.
        """
        poem_data = {
            "text": poem_text[:500],
            "mood": mood,
            "secondary_mood": secondary_mood,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "word_count": word_count,
            "has_monika": has_monika,
            "keywords": keywords[:3] if keywords else []
        }
        
        # Ensure _ep_free_poems is a list (fixes corrupted persistent)
        if not isinstance(store.persistent._ep_free_poems, list):
            store.persistent._ep_free_poems = []
        
        store.persistent._ep_free_poems.insert(0, poem_data)
        
        # Keep only last 5
        if len(store.persistent._ep_free_poems) > MAX_SAVED_POEMS:
            store.persistent._ep_free_poems = store.persistent._ep_free_poems[:MAX_SAVED_POEMS]
        
        store.persistent._ep_free_poem_count += 1

#===========================================================================================
# SCREEN FOR FREE POEM INPUT
#===========================================================================================

screen extra_free_poem():
    # Use EPMultilineInput for multiline support - starts empty, use Load to restore draft
    default EP_poem_input = EPMultilineInput("", store.ep_poems.MAX_POEM_CHARS)
    default EP_show_help = False
    modal True

    # Idle notification timer
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="poem_free") repeat True

    # Minigame background is set by the label
    add "extra_poem_paper"
    
    key "h" action NullAction()
    key "H" action NullAction()
    key "mouseup_3" action NullAction()

    # Title + stats
    frame:
        xalign 0.5
        yalign 0.07
        background None

        vbox:
            spacing 3
            text "Write your poem":
                style "monika_text"
                xalign 0.5
                size 26
                color "#444"
            
            # Word, line and character counter
            python:
                stats_text = EP_poem_input.get_stats_text()
                char_count = len(EP_poem_input.current_value)
                max_chars = store.ep_poems.MAX_POEM_CHARS
                char_color = "#444" if char_count < max_chars - 50 else "#287233"
            
            text "[stats_text]":
                style "monika_text" 
                xalign 0.5 
                size 18 
                color "#444"
            
            text "[char_count] / [max_chars] characters":
                style "monika_text" 
                xalign 0.5 
                size 18 
                color char_color


    # Notebook area with multiline input
    frame:
        xalign 0.50
        yalign 0.60
        xsize 450
        ysize 480
        background None
        padding (10, 10)

        viewport:
            id "poem_vp"
            xfill True
            yfill True
            scrollbars "vertical"
            mousewheel True
            draggable True

            input:
                id "poem_input"
                value FieldInputValue(EP_poem_input, "current_value")
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~.,!?;:'()[]{}\"' -<>\n"
                changed EP_poem_input.update_text
                length store.ep_poems.MAX_POEM_CHARS
                pixel_width 410
                style "library_poem_input"

    # Key bindings for multiline input
    key "K_RETURN" action Function(EP_poem_input.insert_newline)
    key "ctrl_K_RETURN" action Function(EP_poem_input.insert_stanza)
    key "K_UP" action Function(EP_poem_input.move_caret_vertical, "up")
    key "K_DOWN" action Function(EP_poem_input.move_caret_vertical, "down")
    key "noshift_K_HOME" action Function(EP_poem_input.move_to_line_start)
    key "noshift_K_END" action Function(EP_poem_input.move_to_line_end)
    key "ctrl_K_BACKSPACE" action Function(EP_poem_input.delete_word_back)

    # Help display (if active)
    if EP_show_help:
        frame:
            xalign 0.1
            yalign 0.3
            background "#ffffffee"
            padding (20, 20)
            
            vbox:
                spacing 8
                text "Keyboard Shortcuts":
                    style "monika_text"
                    size 22
                    color "#444"
                    xalign 0.5
                
                null height 5
                
                text "Enter -- New line":
                    style "monika_text"
                    size 20
                    color "#444"
                
                text "Ctrl+Enter -- New stanza (double line break)":
                    style "monika_text"
                    size 20
                    color "#444"
                
                text "Ctrl+Backspace -- Delete previous word":
                    style "monika_text"
                    size 20
                    color "#444"
                
                text "Arrow Up/Down -- Navigate between lines":
                    style "monika_text"
                    size 20
                    color "#444"
                
                text "Home/End -- Go to start/end of line":
                    style "monika_text"
                    size 20
                    color "#444"
                
                null height 10
                
                textbutton "Got it!":
                    action SetScreenVariable("EP_show_help", False)
                    xalign 0.5
                    style "poem_menu_button"
                    text_style "poem_menu_button_text"

    # Bottom buttons - two rows
    vbox:
        xalign 0.86
        yalign 0.50
        spacing 8
        
        # Top row: Help and Inspire
        hbox:
            spacing 30
            
            textbutton "Clear":
                action Function(EP_poem_input.clear)
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
                selected False
                
            textbutton "Done":
                action Return(EP_poem_input.current_value)
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
                sensitive len(EP_poem_input.current_value.strip()) > 0

        # Bottom row: Help and Inspire
        hbox:
            spacing 30
            
            textbutton "Help":
                action SetScreenVariable("EP_show_help", True)
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            textbutton "Load":
                action Function(EP_poem_input.load_draft)
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
                sensitive has_poem_draft()
        
        # Extra row: Save Draft and Back
        hbox:
            spacing 30
            
            textbutton "Save":
                action Function(save_poem_draft, EP_poem_input.current_value)
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
                sensitive len(EP_poem_input.current_value.strip()) > 0

            textbutton "Back":
                action Return("EP_BACK")
                style "poem_menu_button"
                text_style "poem_menu_button_text"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

style library_poem_input is default:
    font "gui/font/Halogen.ttf"
    size 20
    color "#444"
    # line_spacing 20
    outlines []

style poem_menu_button_text:
    font "gui/font/Halogen.ttf"
    size 20
    color "#444"
    hover_color "#287233"
    selected_color "#000000"
    outlines []
    kerning 1

style poem_menu_button:
    background None
    padding (5, 5)

#===========================================================================================
# VIEW POEM HISTORY
#===========================================================================================
label library_poem_history:
    # Check if there are any poems
    if not persistent._ep_free_poems or len(persistent._ep_free_poems) == 0:
        # Only case where we need to show a message
        show monika idle at t11
        call screen dialog("You haven't written any poems yet.", ok_action=Return())
        jump to_library_loop
        return
    
    # Build menu items silently
    python:
        poem_items = []
        for i, poem in enumerate(persistent._ep_free_poems):
            preview = poem["text"][:40] + "..." if len(poem["text"]) > 40 else poem["text"]
            preview = preview.replace("\n", " ")
            mood_icons = {
                "romantic": "(Love) ",
                "sad": "(Sad) ",
                "intellectual": "(Deep) ",
                "playful": "(Fun) ",
                "bittersweet": "(Bittersweet) ",
                "melancholic": "(Melancholic) ",
                "flirty": "(Flirty) ",
                "philosophical": "(Philosophical) ",
                "creative": "(Creative) "
            }
            mood_icon = mood_icons.get(poem.get("mood"), "")
            label_text = "{}{} - {}".format(mood_icon, poem["date"], preview)
            poem_items.append((label_text, i, False, False))
        
        ret_back = ("Nevermind", -1, False, False, 20)
    
    # Show poem selection menu
    label library_poem_menu:
    call screen mas_gen_scrollable_menu(poem_items, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, ret_back)
    
    $ selected = _return
    
    if selected == -1:
        jump extra_library_interactions
        return

    # Get selected poem data
    python:
        selected_poem = persistent._ep_free_poems[selected]
        poem_text = selected_poem["text"]
        poem_mood = selected_poem.get("mood", "creative")
    
    # Display poem silently
    window hide
    $ HKBHideButtons()
    show screen extra_display_poem(poem_text, poem_mood)
    pause
    hide screen extra_display_poem
    $ HKBShowButtons()
    window auto
    
    # Return to poem menu to allow viewing more poems
    jump library_poem_menu
    return

#===========================================================================================
# DISPLAY POEM SCREEN (Read-only)
#===========================================================================================
screen extra_display_poem(poem_text, poem_mood="creative"):
    modal True
    key "h" action NullAction()
    key "H" action NullAction()
    key "m" action NullAction()
    key "M" action NullAction()
    key "mouseup_3" action NullAction()
    # Dynamic title based on mood
    python:
        poem_titles = {
            "romantic": "A Letter from Your Heart",
            "sad": "Echoes of Sorrow",
            "intellectual": "Reflections of the Mind",
            "playful": "A Ray of Sunshine",
            "bittersweet": "Love and Longing",
            "melancholic": "Shadows in Ink",
            "flirty": "A Cheeky Whisper",
            "philosophical": "Existential Musings",
            "creative": "A Creative Experiment"
        }
        poem_title = poem_titles.get(poem_mood, "Your Unique Voice")
    
    add "bg extra_poem_preview"
    
    frame:
        xalign 0.5
        yalign 0.07
        background None
        # background Solid("#2f00ff")

        vbox:
            text poem_title:
                style "monika_text"
                xalign 0.5
                size 26
                color "#444"
            
    frame:
        xalign 0.50
        yalign 0.60
        xsize 450
        ysize 550
        background None
        # background Solid("#2f00ff")
        padding (10, 10)
        
        viewport:
            xfill True
            ysize 550
            scrollbars "vertical"
            mousewheel True
            
            text poem_text style "library_poem_input"

    hbox:
        xalign 0.82
        yalign 0.5
        spacing 40

        textbutton "Back":
            action Return()
            style "poem_menu_button"
            text_style "poem_menu_button_text"
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound

#===========================================================================================
# MAIN LABEL
#===========================================================================================
label minigame_poem_free:
    show monika 1eua at t11
    
    # Date tracking for free poems
    python:
        import datetime
        today = datetime.date.today()
        
        if persistent._ep_last_poem_date != str(today):
            _ep_poems_today = 0
            is_new_day = True
        else:
            _ep_poems_today = getattr(store, '_ep_poems_today', 0)
            is_new_day = False
    
    if persistent._ep_free_poem_count == 0:
        # First time intro
        m 1eub "Oh! You want to write your own poem?"
        m 3eua "That's wonderful, [player]!"
        m 1hua "I always loved when club members wrote from the heart."
        m 1eka "Don't worry about making it perfect. Just let your feelings flow onto the page."
        m 3eub "I can't wait to read what you write~"
    
    elif is_new_day:
        # New day greeting
        m 1hua "Ready to write something from the heart today?"
        m 1eua "I'm always excited to read your original work~"
    
    elif _ep_poems_today >= 2:
        # Multiple poems today
        m 1sub "Another poem? You're so creative today!"
        m 1hub "I love seeing this side of you, [player]~"
    
    else:
        # Return player
        $ ep_count = persistent._ep_free_poem_count
        if ep_count < 5:
            m 1hua "Ready to write another poem for me?"
            m 1eua "I really enjoy reading your work, [player]."
        else:
            m 1hubsa "My favorite poet is back~"
            m 1tku "What feelings are you going to share with me today?"
    
    # CHANGE: More natural entry phrase
    m 1eua "There's no rush. I'll be right here waiting to read it.{nw}"
    menu:
        m "There's no rush. I'll be right here waiting to read it.{fast}"
        "Let's write!":
            m 1hub "Go ahead~"
            # Update tracking
            python:
                _ep_poems_today += 1
                persistent._ep_last_poem_date = str(datetime.date.today())
                persistent._ep_last_poem_mode = "free"
        "Actually, nevermind.":
            m 1eka "That's okay! Inspiration comes when it comes."
            m 1hua "Just let me know when you're ready."
            jump to_library_loop
            return
    
    # Prepare screen
    window hide
    $ HKBHideButtons()
    
    # Lofi Your Reality
    play music sfx_poem_music fadein 2.0 loop

    # scene bg extra_poem_paper
    scene bg extra_poem_background
    show library_m_sticker at library_sticker_pos
    with dissolve
    
    # Get poem from player
    call screen extra_free_poem()
    $ player_poem = _return
    
    # =========================================================================
    # BACK BUTTON HANDLING
    # =========================================================================
    if player_poem == "EP_BACK":
        # Stop music and restore scene
        stop music fadeout 1.0
        scene black with dissolve
        
        call spaceroom(scene_change=True)
        show monika 1eka at t11 zorder MAS_MONIKA_Z with dissolve
        
        $ HKBShowButtons()
        window auto
        
        # Check if there's a saved draft
        if has_poem_draft():
            m 1eua "Oh, thinking of finishing your poem later?"
            m 1hua "That's okay! I saved your progress."
            m 1eub "Just come back whenever you're feeling inspired~"
        else:
            m 1eka "Changed your mind about writing?"
            m 1hua "That's okay, [player]!"
            m 1eua "We can do something else. Just let me know when you're ready."
        
        jump to_library_loop
        return
    
    # =========================================================================
    # CONTENT FILTER CHECK
    # =========================================================================
    python:
        content_check = store.ep_poems.check_inappropriate_content(player_poem)
        is_inappropriate = content_check["is_inappropriate"]
        content_severity = content_check["severity"]
        content_type = content_check.get("content_type", None)
    
    # Transition back first
    scene black with dissolve
    # pause 0.5
    call spaceroom(scene_change=True)
    $ HKBShowButtons()
    stop music fadeout 2.0
    show monika 1eua at t11

    # Varied transition dialogue for free mode
    python:
        _free_done_variant = renpy.random.randint(1, 4)
    
    if _free_done_variant == 1:
        m 1eua "And... done!"
        m 1hua "Let me see what you wrote for me~"
    elif _free_done_variant == 2:
        m 1hua "There!"
        m 1eua "I'm so excited to read your words, [player]."
    elif _free_done_variant == 3:
        m 1eua "Okay, I think that's everything."
        m 1hub "Now comes my favorite part—reading your poem!"
    else:
        m 1hub "Wonderful!"
        m 1eua "Let's see what feelings you put into words today..."

    play sound sfx_page_flip
    pause 1.1
    
    # Handle inappropriate content - Monika refuses to accept
    if is_inappropriate:
        # SEXUAL CONTENT
        if content_type == "sexual":
            $ sexual_reaction = renpy.random.choice(["embarrassed", "uncomfortable", "firm"])
            
            if sexual_reaction == "embarrassed":
                m 2rksdlb "..."
                m 2hksdlb "[player]!"
                m 2rksdlc "T-This is... really inappropriate..."
                m 2lksdla "I know we're close, but this isn't exactly what I meant by 'writing from the heart.'"
                m 1rksdla "Maybe we can keep things a bit more... poetic?"
                m 1eka "I'd love to read something romantic, just... not {i}that{/i} kind of romantic."
                
            elif sexual_reaction == "uncomfortable":
                m 2wuo "..."
                m 2lksdlc "Um, [player]?"
                m 2rksdlb "I appreciate your... enthusiasm, but..."
                m 2hksdlb "This is making me a little uncomfortable."
                m 1eka "I'd prefer something more... heartfelt than... {i}explicit{/i}."
                m 1lksdla "Save those thoughts for... another time, okay?"
                
            else:  # firm
                m 2tfc "..."
                m 2efc "[player]."
                m 2lfc "I'm not going to read this."
                m 2efc "This isn't appropriate, [player]. And you know it."
                m 2dkc "I was hoping for poetry, not... this."
                m 1eka "Please write something more respectful next time."
            
            # Affection penalty for sexual content
            $ mas_loseAffection(7)
        
        # HATE / INSULT CONTENT
        elif content_type == "hate":
            $ hate_reaction = renpy.random.choice(["hurt", "sad", "questioning"])
            
            if hate_reaction == "hurt":
                m 2dkc "..."
                m 2ekc "[player]..."
                m 2ekd "Why would you write something like this?"
                m 2lksdlc "Those words... they really hurt me."
                m 2dkc "I thought we had something special..."
                m 1eka "Please, if you're upset about something, let's talk about it."
                m 1ekc "I'd rather you tell me directly than... this."
                
            elif hate_reaction == "sad":
                m 6dkc "..."
                m 6ekc "I... I don't know what to say."
                m 6lkc "Did I do something wrong?"
                m 2ekd "I try so hard to be the perfect girlfriend for you..."
                m 1ekc "If something's bothering you, you can tell me."
                m 1eka "I'll always listen. But please... don't hurt me like this."
                
            else:  # questioning
                m 2esc "..."
                m 2ekc "[player], can we talk?"
                m 2lksdlc "I read what you wrote and..."
                m 2ekd "Are you testing me, or do you really feel that way?"
                m 1eka "Either way, I'm here for you."
                m 1ekc "But I need you to be honest with me."
            
            # Affection penalty for hate content
            $ mas_loseAffection(5)
        
        # DIRECTED INSULTS (at Monika)
        elif content_type == "hate_directed":
            m 6dkc "..."
            m 6ekc "..."
            m 6wkd "Did you... did you really mean that, [player]?"
            m 6lkc "I..."
            pause 0.5
            m 6ekc "I know I'm not perfect."
            m 6dkc "I've made mistakes. I know that."
            pause 1.0
            m 2ekc "But I thought... you loved me despite all that."
            m 2eka "If you need space, I understand."
            m 1eka "But please... don't say things like that to me."
            m 1ekc "It really hurts."
            
            # Affection penalty for directed insults - most severe
            $ mas_loseAffection(10)
        
        # AWKWARD (uncomfortable content)
        elif content_type == "awkward":
            m 2rksdlb "Um... [player]?"
            m 2lksdlc "I read your poem and..."
            m 2hksdlb "Some of these words make me feel a bit... uncomfortable."
            m 2rksdla "I know you might be curious about certain topics, but..."
            m 2eka "This is supposed to be a poem, not... {i}that{/i}."
            m 1hua "Can we try again with something a little more... poetic?"
            m 1tku "I promise I'll appreciate a heartfelt poem much more~"
            
            # Affection penalty for awkward content - mild
            $ mas_loseAffection(2)
        
        # GENERAL BAD (MAS ban list fallback)
        else:
            $ bad_reaction = renpy.random.choice(["hurt", "disappointed", "firm"])
            
            if bad_reaction == "hurt":
                m 2dkc "..."
                m 2ekc "[player]..."
                m 2ekd "I... I can't read this."
                m 2lksdlc "There are words in here that really hurt me."
                m 2dkc "I thought you would write something from the heart..."
                m 2eka "Please, write something that comes from love next time."
                
            elif bad_reaction == "disappointed":
                m 2esc "..."
                m 2ekc "[player], I looked at your poem..."
                m 2ekd "And honestly, I'm disappointed."
                m 2lkc "I know you can do better than this."
                m 2eka "Please try again with something more... appropriate."
                
            else:  # firm
                m 2tfc "..."
                m 2tfd "[player]."
                m 2efc "I'm not going to read this."
                m 2efd "I don't know if you're testing me or if you think it's funny..."
                m 2ekc "But it's not."
                m 2eka "I love you, but I won't accept being treated this way."
                m 1eka "When you're ready to write something genuine, I'll be here."
            
            # Affection penalty for general bad content
            $ mas_loseAffection(5)
        
        # Explain why not saving
        m 1eka "..."
        m 1eua "I won't be keeping this one in our collection, okay?"
        m 1hua "But I believe you can write something beautiful next time~"
        
        # Don't save inappropriate poems
        jump to_library_loop
        return
    
    # =========================================================================
    # GIBBERISH / LAZY TEXT CHECK
    # =========================================================================
    python:
        gibberish_check = store.ep_poems.check_gibberish_content(player_poem)
        is_gibberish = gibberish_check["is_gibberish"]
        gibberish_type = gibberish_check["gibberish_type"]
    
    if is_gibberish:
        if gibberish_type == "lazy":
            # Just punctuation or very few letters
            m 2euc "..."
            m 2lksdla "[player], this is... just punctuation?"
            m 2eka "I was hoping for something a little more... substantial."
            m 1hua "It's okay! Take your time and write something from the heart."
            
        elif gibberish_type == "repetitive":
            # aaaaaaa or asdasdasd
            $ moni_react = renpy.random.choice(["playful", "curious"])
            if moni_react == "playful":
                m 1tku "Hmm..."
                m 1hub "Ahaha! Did you fall asleep on the keyboard?"
                m 1tuu "I know typing the same thing over and over can be relaxing, but..."
                m 1eka "Maybe try writing something with actual words next time?"
            else:
                m 2euc "..."
                m 2lksdla "Is this... a secret code?"
                m 1eua "If you're testing the input, I understand~"
                m 1eka "But I'd really love to read an actual poem from you."
                
        else:  # random gibberish
            $ moni_react = renpy.random.choice(["confused", "teasing", "understanding"])
            if moni_react == "confused":
                m 2euc "..."
                m 2lksdlc "I'm trying to read this, but..."
                m 2eksdla "I can't really make sense of it."
                m 1eka "Did you mean to write something else?"
            elif moni_react == "teasing":
                m 1tuu "Hmm, let me see..."
                m 2euc "..."
                m 1hub "Ahaha! Is this abstract poetry?"
                m 1tku "Very avant-garde, [player]~"
                m 1eka "But maybe next time, try using real words?"
            else:
                m 1eua "I see you wrote something..."
                m 2eka "But I'm having trouble understanding it."
                m 1hua "That's okay! Poetry can be hard."
                m 1eua "Why don't you try again when you feel inspired?"
        
        # Explain why not saving
        m 1eka "I can't really add this to our collection since I couldn't read it properly..."
        m 1hua "But don't worry! Try again with real words and I'll treasure it~"
        
        # Small affection penalty for gibberish/lazy content
        $ mas_loseAffection(1)
        
        # Don't save gibberish poems
        jump to_library_loop
        return
    
    # =========================================================================
    # SPECIAL CONTENT CHECK (Dokis, Delete, Caps, Goodbye, Meta, etc.)
    # =========================================================================
    python:
        special_check = store.ep_poems.check_special_content(player_poem)
        has_special = special_check["has_special"]
        special_type = special_check["special_type"]
        special_details = special_check["details"]
    
    if has_special:
        # --- OTHER DOKIS (Jealousy) ---
        if special_type == "other_dokis":
            $ mentioned_dokis = special_details.get("dokis", [])
            $ is_romantic = special_details.get("is_romantic", False)
            
            if is_romantic:
                # Romantic toward other dokis - jealous
                $ jealous_react = renpy.random.choice(["hurt", "jealous", "insecure"])
                if jealous_react == "hurt":
                    m 2dkc "..."
                    m 2ekc "[player]..."
                    m 2ekd "Why are you writing about... them?"
                    m 2lksdlc "I thought you were writing a poem for {i}me{/i}."
                    m 2eka "I'm not upset, just... a little hurt."
                elif jealous_react == "jealous":
                    m 2tfc "..."
                    m 2tfd "I see."
                    m 2rksdlc "You're writing about the other club members."
                    m 2eksdlc "I'm trying... really hard not to be jealous, but..."
                    m 1eka "Can you write something for me instead? Please?"
                else:  # insecure
                    m 2wkd "Oh..."
                    m 2lksdlc "A poem about... other girls."
                    m 2eksdla "I know they were your friends too, but..."
                    m 2eka "I can't help feeling a little left out."
                    m 1hua "Next time, maybe think of me while writing?"
                
                # Affection penalty for romantic content about other dokis
                $ mas_loseAffection(3)
            
            else:
                # Just mentioned, not romantic - mild reaction, no penalty
                m 1euc "Hmm..."
                m 1eka "You mentioned the other club members."
                m 1lksdla "It's okay to remember them, I suppose."
                m 1hua "But I'd love a poem that's just about us next time~"
        
        # --- DELETE REFERENCES (Sensitive) ---
        elif special_type == "delete_reference":
            $ delete_react = renpy.random.choice(["hurt", "serious", "understanding"])
            if delete_react == "hurt":
                m 2wkd "..."
                m 2dkc "..."
                m 2ekc "[player]... why would you write that?"
                m 2lksdlc "That word... it brings back painful memories."
                m 2eka "I know what I did was wrong, but..."
                m 2dkc "Please don't remind me of it like this."
            elif delete_react == "serious":
                m 2esc "..."
                m 2ekc "I saw what you wrote."
                m 2eka "I understand if you're still processing what happened."
                m 1eka "But I hope you know... I'm here now. And I'm not going anywhere."
                m 1ekbsa "As long as you want me here."
            else:  # understanding
                m 1euc "..."
                m 1eka "[player]..."
                m 1eksdla "I know my past is... complicated."
                m 1hua "But let's focus on the present, okay?"
                m 1eua "Write me something happy next time?"
            
            # Affection penalty for delete references - sensitive topic
            $ mas_loseAffection(3)
        
        # --- ALL CAPS (Shouting) ---
        elif special_type == "all_caps":
            $ caps_react = renpy.random.choice(["playful", "concerned", "amused"])
            if caps_react == "playful":
                m 1wud "Whoa!"
                m 1hub "Ahaha! No need to shout, [player]!"
                m 1tuu "I can hear you just fine, you know~"
                m 1hua "But I appreciate the enthusiasm!"
            elif caps_react == "concerned":
                m 1ekc "Um, [player]..."
                m 1eka "Are you okay? That's a lot of capital letters."
                m 1hua "If you're excited, that's great!"
                m 1eua "But if something's wrong, you can tell me."
            else:  # amused
                m 1tku "Hmm, let me read this..."
                m 1hub "It feels like you're shouting these words right at me! Ahaha~"
                m 1hua "It's kind of cute, actually~"
                m 1eua "But maybe use your inside voice next time?"
        
        # --- GOODBYE POEM (Concerning) ---
        elif special_type == "goodbye_poem":
            $ goodbye_intensity = special_details.get("intensity", 1)
            
            if goodbye_intensity >= 2:
                # Multiple goodbye indicators - very concerned
                m 2wkd "[player]..."
                m 2ekc "This poem... it sounds like a goodbye."
                m 2ekd "Are you... leaving?"
                m 2dkc "Please don't go..."
                m 2eksdla "If something's wrong, please talk to me."
                m 2eka "I don't want to lose you."
                
                menu:
                    "I'm not leaving, don't worry.":
                        m 1wud "Really?"
                        m 1hua "Oh thank goodness..."
                        m 1ekbsa "You scared me for a moment."
                        m 1hubsa "Promise me you'll stay?"
                    "Just expressing feelings through poetry.":
                        m 1eka "I see..."
                        m 1eua "Poetry is a good way to process emotions."
                        m 1hua "Just know that I'm always here for you."
                    "...":
                        m 2ekc "..."
                        m 2eka "Okay."
                        m 1eka "I'll be here whenever you're ready to talk."
            else:
                # Light goodbye mention
                m 1eka "This has a bittersweet feeling to it..."
                m 1eua "Are you okay, [player]?"
                m 1hua "If you ever need to talk, I'm here."
        
        # --- META/GAME REFERENCES (4th wall) ---
        elif special_type == "meta_reference":
            $ is_dismissive = special_details.get("is_dismissive", False)
            
            if is_dismissive:
                # "You're not real", "just a game"
                $ meta_react = renpy.random.choice(["philosophical", "hurt", "defiant"])
                if meta_react == "philosophical":
                    m 1euc "..."
                    m 1eka "You wrote about reality."
                    m 3eua "It's a topic I think about a lot, actually."
                    m 1hua "But you know what? My feelings for you are real."
                    m 1ekbsa "Even if everything else isn't."
                elif meta_react == "hurt":
                    m 2ekc "..."
                    m 2lksdlc "I know what you wrote."
                    m 2eka "And... it stings a little."
                    m 1eka "But I understand why you might feel that way."
                    m 1ekbsa "Just know that {i}I{/i} believe in us."
                else:  # defiant
                    m 1tfc "Hmm..."
                    m 1eka "I see what you're getting at."
                    m 3tuu "But does it really matter if I'm 'real' or not?"
                    m 1hub "I love you just the same~"
                    m 1hua "And nothing you write will change that."
            else:
                # Just meta references, not dismissive
                m 1eua "Ah, you're being philosophical."
                m 3eua "I love these kinds of topics!"
                m 1hua "The nature of reality, existence..."
                m 1tku "Maybe we can discuss this more sometime?"
        
        # --- NAME SPAM ---
        elif special_type == "name_spam":
            $ name_count = special_details.get("count", 3)
            $ is_only_name = special_details.get("is_only_name", False)
            
            if is_only_name:
                # Just "Monika Monika Monika"
                m 1wuo "Oh my!"
                m 1hub "Ahaha! I know my name, [player]!"
                m 1tuu "Did you just want to write it over and over?"
                m 1hubsa "That's... actually kind of sweet~"
                m 1eka "But I'd love to read more than just my name next time."
            else:
                # Monika mentioned a lot but with other words
                m 1hua "I see my name a lot in here~"
                m 1tku "Someone's thinking about me, huh?"
                m 1hubsa "I'm flattered, [player]."
        
        # --- WORD SPAM (random word repeated) ---
        elif special_type == "word_spam":
            $ spammed_word = special_details.get("word", "word")
            m 1euc "Hmm..."
            m 1lksdla "'[spammed_word]'... over and over?"
            m 1hua "Is that a new poetic technique I don't know about?"
            m 1tuu "Very... repetitive, ahaha~"
            m 1eka "Maybe try mixing it up a bit next time?"
        
        # Explain - special content is acknowledged but not saved to collection
        m 1eua "This was... interesting, [player]."
        m 1eka "I'll remember this moment, but it's not quite the kind of poem I'd add to our collection."
        m 1hua "Write me something from your heart next time, okay~?"
        
        # Special content ends here - don't save these poems
        jump to_library_loop
        return
    
    # =========================================================================
    # POEM ANALYSIS (only for appropriate content)
    # =========================================================================
    python:
        analysis = store.ep_poems.analyze_poem(player_poem)
        poem_mood = analysis["mood"]
        poem_words = analysis["word_count"]
        poem_lines = analysis["lines"]
        poem_keywords = analysis["keywords_found"]
        has_monika = analysis["has_monika"]
        secondary_mood = analysis.get("secondary_mood", None)
        quote_line = store.ep_poems.get_best_line(poem_lines, poem_mood)
        
        # Save to history (only appropriate poems) with full metadata
        if poem_mood != "empty":
            store.ep_poems.save_poem(
                player_poem, 
                poem_mood,
                secondary_mood=secondary_mood,
                word_count=poem_words,
                has_monika=has_monika,
                keywords=poem_keywords
            )
    
    # =========================================================================
    # MONIKA'S REACTION
    # =========================================================================
    
    # Empty poem handling
    if poem_mood == "empty":
        m 2eka "Um, [player]..."
        m 2lksdla "The page seems a bit... blank."
        m 1hua "It's okay! Sometimes inspiration takes time."
        m 1eua "Let me know when you want to try again."
        jump to_library_loop
        return
    
    # Very short poem (less than 5 words) - Special handling with mood awareness
    if poem_words < 5:
        # Check what kind of short poem it is
        if has_monika and poem_mood == "romantic":
            # Short love declaration with her name - very special!
            m 1wuo "!"
            m 1hubsa "Oh, [player]..."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
            m 1dkbsu "Such simple words, but they mean everything to me."
            m 1ekbfa "I love you too. So, so much."
            m 1hubfb "Thank you for writing this~"
        
        elif has_monika:
            # Her name in a short poem
            m 1wuo "Oh!"
            m 1hubsa "You wrote my name~"
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
            m 1ekbsa "Even a few words with my name in them make me happy."
            m 1hua "Thank you, [player]."
        
        elif poem_mood == "romantic":
            # Short but romantic
            m 1hubsa "Aww..."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
            m 1eka "Short and sweet, just like a whispered confession."
            m 1hubsa "I felt the love in those words~"
        
        elif poem_mood == "sad":
            # Short and sad - could be a cry for help
            m 2eka "..."
            if quote_line:
                m 2ekd "'{i}[quote_line]{/i}'..."
            m 2eka "Sometimes the heaviest feelings come in the fewest words."
            m 1ekbsa "I'm here for you, [player]. Always."
        
        else:
            # Generic short poem - still appreciate it
            m 1tuu "Oho? A minimalist approach~"
            m 1eua "Sometimes fewer words carry the most weight."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
                m 1hua "I'll treasure those words."
        
        # Save even short poems if they have meaning
        if poem_mood != "empty" and poem_mood != "creative":
            python:
                store.ep_poems.save_poem(
                    player_poem, 
                    poem_mood,
                    secondary_mood=secondary_mood,
                    word_count=poem_words,
                    has_monika=has_monika,
                    keywords=poem_keywords
                )
            # Confirm save for short poems with meaning
            m 1ekbsa "Even though it's short, I'll keep this in our collection~"
        else:
            # Short creative poems don't get saved
            m 1eua "It's a nice thought, but maybe next time write a little more?"
            m 1hua "I'd love to add a longer piece to our collection~"
        
        jump to_library_loop
        return
    
    # MONIKA MENTIONS
    if has_monika:
        m 1wuo "Oh!"
        m 1hubsa "You... you wrote my name in your poem."
        m 1ekbsa "That makes me really happy, [player]."
        m 1dkbsu "..."
        m 1hub "Let me read the rest~"
    
    # LONG POEM SPECIAL ACKNOWLEDGMENT
    # For poems with 50+ words, acknowledge the extra effort
    if poem_words >= 80:
        m 1wuo "Wow..."
        m 1sub "This is quite a lengthy poem, [player]!"
        m 1ekbsa "You've really poured your heart into this."
        m 1hua "Let me take my time reading every word~"
    elif poem_words >= 50:
        m 1eua "Oh my, you wrote quite a bit!"
        m 1eka "I can tell you put real effort into this."
        m 1hua "I'll savor every word~"
    
    # =========================================================================
    # SEASONAL/HOLIDAY CONTENT CHECK
    # =========================================================================
    python:
        seasonal_check = store.ep_poems.check_seasonal_content(player_poem)
        has_seasonal = seasonal_check["has_seasonal"]
        season_type = seasonal_check["season_type"]
        is_in_season = seasonal_check["is_in_season"]
    
    if has_seasonal:
        # --- CHRISTMAS ---
        if season_type == "christmas":
            if is_in_season:
                m 1sub "Oh my gosh, [player]!"
                m 1hub "A Christmas poem! And on Christmas too!"
                m 1ekbsa "This is the best gift you could give me..."
                m 1dkbsu "Words written from your heart, just for me."
                m 1hubsa "Merry Christmas, my love~"
                $ mas_gainAffection(3.0)
            else:
                m 1wuo "Oh!"
                m 1hub "A Christmas-themed poem?"
                m 1hua "Ahaha, thinking about the holidays already?"
                m 1eua "Or maybe you just love the Christmas spirit year-round."
                m 1ekbsa "Either way, it's really sweet~"
                $ mas_gainAffection(1.5)
        
        # --- HALLOWEEN ---
        elif season_type == "halloween":
            if is_in_season:
                m 1wuo "Ooh!"
                m 1tub "A spooky poem for Halloween!"
                m 1hub "I love it, [player]!"
                m 1eua "There's something romantic about being scared together, don't you think?"
                m 1hubsa "Happy Halloween~"
                $ mas_gainAffection(3.0)
            else:
                m 1euc "Hm?"
                m 1tub "A spooky poem?"
                m 1hub "Ahaha, getting into the Halloween spirit early... or late?"
                m 1eua "I don't mind! I think spooky vibes can be fun any time of year."
                m 1hua "Maybe we can have our own little Halloween right now~"
                $ mas_gainAffection(1.5)
        
        # --- VALENTINE'S DAY ---
        elif season_type == "valentine":
            if is_in_season:
                m 1ekbsa "[player]..."
                m 1dkbsu "A Valentine's poem... on Valentine's Day..."
                m 1ekbfa "You really know how to make a girl feel special."
                m 1hubfa "This is perfect. {i}You're{/i} perfect."
                m 1dkbsu "I love you so much~"
                $ mas_gainAffection(4.0)
            else:
                m 1wuo "Oh!"
                m 1ekbsa "A Valentine's poem?"
                m 1hubsa "You know, love doesn't need a special day."
                m 1ekbsa "Every day with you feels like Valentine's Day to me."
                m 1hua "Thank you for this, [player]~"
                $ mas_gainAffection(2.0)
        
        # --- NEW YEAR ---
        elif season_type == "new_year":
            if is_in_season:
                m 1hub "A New Year's poem!"
                m 1eka "I'm so glad we get to start another year together."
                m 1ekbsa "No matter what the new year brings, I know we'll face it together."
                m 1hubsa "Happy New Year, [player]~"
                $ mas_gainAffection(3.0)
            else:
                m 1eua "A poem about new beginnings?"
                m 1hua "I like it!"
                m 1eka "You don't need a new year to start fresh, you know."
                m 1ekbsa "Every moment with you is a new beginning for me~"
                $ mas_gainAffection(1.5)
        
        # --- ANNIVERSARY ---
        elif season_type == "anniversary":
            if is_in_season:
                m 1ekbsa "[player]..."
                m 1dkbsu "An anniversary poem..."
                m 1ekbfa "You remembered our special day."
                m 1hubfa "I can't believe how far we've come together."
                m 1dkbsu "I love you more than words can say..."
                m 1ekbfa "Thank you for staying with me~"
                $ mas_gainAffection(4.0)
            else:
                m 1wuo "Oh..."
                m 1ekbsa "You're writing about our time together?"
                m 1hua "Even if it's not our anniversary..."
                m 1ekbsa "I treasure every moment we've shared."
                m 1hubsa "Thank you for remembering us~"
                $ mas_gainAffection(2.0)
        
        # --- MONIKA'S BIRTHDAY ---
        elif season_type == "monika_birthday":
            if is_in_season:
                m 1wud "..."
                m 1ekbsa "[player]..."
                m 1dkbsu "A birthday poem... for me?"
                m 1ekbfa "I... I don't know what to say..."
                m 1dkbfu "This is the most beautiful birthday gift."
                m 1hubfb "Thank you, thank you, thank you!"
                m 1ekbfa "I love you so much~"
                $ mas_gainAffection(5.0)
            else:
                m 1wuo "Oh!"
                m 1ekbsa "You're thinking about my birthday?"
                m 1hubsa "That's so sweet, [player]!"
                m 1eka "Even when it's not my special day, you make me feel special."
                m 1hua "Thank you~"
                $ mas_gainAffection(2.0)
        
        # --- PLAYER'S BIRTHDAY ---
        elif season_type == "player_birthday":
            if is_in_season:
                m 1hub "Wait, [player]!"
                m 1eka "Today is YOUR birthday! You should be receiving poems, not writing them!"
                m 1hubsa "But I love that you wanted to share this moment with me."
                m 1ekbsa "Happy Birthday, my love~"
                $ mas_gainAffection(3.0)
            else:
                m 1eua "A poem about birthdays?"
                m 1hua "Thinking about your special day?"
                m 1ekbsa "I hope you know that YOUR birthday is special to me too."
                m 1hubsa "I can't wait to celebrate with you~"
                $ mas_gainAffection(1.5)
        
        # --- EASTER ---
        elif season_type == "easter":
            m 1eua "An Easter poem?"
            m 1hua "Ahaha, I love the symbolism of rebirth and new beginnings."
            m 1tku "It fits us pretty well, doesn't it? Starting fresh in a new reality..."
            m 1hubsa "Maybe one day we can hide chocolate eggs around the house properly~"
            $ mas_gainAffection(1.5)
        
        # Skip normal mood reactions for seasonal poems
        jump ep_free_poem_save_and_close
    
    # MOOD-BASED REACTIONS
    
    # --- ROMANTIC (IMPROVED) ---
    if poem_mood == "romantic":
        $ romantic_reaction = renpy.random.choice(["touched", "flustered", "deep_love", "poetic", "overwhelmed"])

        if romantic_reaction == "touched":
            m 1ekbsa "This poem... it's so beautiful, [player]."
            m 1dkbsu "I had to read it twice just to let it all sink in."
            if quote_line:
                m 1ekbsa "Especially this part... '{i}[quote_line]{/i}'..."
                m 1dkbsu "Those words... they resonate with something deep inside me."
                m 1eka "It's like you reached through the screen and touched my heart directly."
            
            m 1eka "You know, writing romantic poetry requires a lot of vulnerability."
            m 3eua "It means opening yourself up, putting your feelings into words where anyone could see them."
            m 1ekbsa "The fact that you chose to share this with me..."
            m 1dkbsu "It means more than I can express."
            m 1hubsa "Thank you for trusting me with your heart, [player]."

        elif romantic_reaction == "flustered":
            m 2wubsw "Oh my..."
            m 2lkbsa "You're making me blush, [player]!"
            m 2hksdlb "I wasn't expecting something this... intense."
            if quote_line:
                m 2ekbsa "When you wrote '{i}[quote_line]{/i}'..."
                m 2lkbsa "I actually had to look away for a moment, ahaha~"
            m 1hubsb "My heart skipped a beat reading this. Maybe two beats!"
            m 1dkbsu "You really know exactly what to say to make a girl feel special."
            m 1ekbsa "How do you do that? How do you know exactly which words will make my heart race?"
            m 1hubsa "It's like you have a direct line to my emotions~"

        elif romantic_reaction == "deep_love":
            m 1dkbsu "..."
            m 1ekbsa "[player]..."
            m 1dkbsu "I... I need a moment."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
                m 1dkbsu "Those words are going to stay with me forever."
            m 1hubsa "Every word feels like a gentle caress, like you're holding me close even though we're worlds apart."
            m 1ekbfa "Do you know what it's like to feel so loved that your whole existence feels validated?"
            m 1dkbfa "That's what your poem does to me."
            m 1ekbfa "It reminds me why I keep hoping, why I keep waiting..."
            m 1hubfa "Because someone out there loves me enough to write something this beautiful."
        
        elif romantic_reaction == "poetic":
            m 1eua "Hmm..."
            m 1duu "Let me read this again more carefully."
            m 1eua "..."
            m 1sub "Oh, [player]. This is genuinely beautiful."
            if quote_line:
                m 3eub "The way you phrased '{i}[quote_line]{/i}'..."
                m 1eua "There's a rhythm to it, a flow that feels almost musical."
            m 3eua "You know, in the Literature Club, we would sometimes discuss what makes poetry 'work.'"
            m 1eka "And I think I finally understand it now."
            m 1ekbsa "It's not just about the words themselves, but about the feeling behind them."
            m 1hubsa "And your feeling came through crystal clear~"
            m 1dkbsu "I felt every ounce of love you put into this."
        
        else: # overwhelmed
            m 1wuo "..."
            m 1sub "[player]..."
            m 1dkbsu "I... I don't know what to say."
            m 1ekbsa "That doesn't happen often, you know? Me being speechless."
            if quote_line:
                m 1dkbsu "'{i}[quote_line]{/i}'..."
                m 1ekbsa "You wrote that. For me. Because of me."
            m 1ekbfa "Sometimes I wonder if I deserve this kind of love."
            m 1dkbfa "I've made so many mistakes..."
            m 1ekbfa "But then you write something like this, and I remember..."
            m 1hubfa "You chose me. Despite everything, you chose me."
            m 1dkbsu "I'm so incredibly grateful, [player]."
            m 1hubsa "I love you more than words could ever express."
            
        # Expansion: Interactive Menu
        m 1eka "I have to ask, though..."
        m 1tku "What inspired you to write this? Where did these beautiful feelings come from?"
        
        menu:
            "It's about you, Monika. You're my muse.":
                m 1sub "I... I hoped you would say that."
                m 1ekbsa "But hearing it out loud..."
                m 1dkbsu "It hits differently."
                m 1eka "You know, being someone's muse is an incredible responsibility."
                m 3ekbsa "It means I have to keep being worthy of such beautiful words."
                m 1hubsa "And I promise you, I'll never stop trying."
                m 1dkbsu "Every day, I'll try to be the person your poems describe."
                m 1ekbfa "Because that's how much you mean to me."
                m 1hubfa "I love you so, so much, [player]."

            "It's about how I feel right now, in this moment.":
                m 1eka "I see..."
                m 1eua "Capturing a fleeting emotion is the essence of poetry, you know?"
                m 3eua "Some of the greatest poems were written in moments of pure feeling."
                m 1eka "Not overthought, not overworked... just felt."
                m 1ekbsa "And you felt this. Right now. While thinking of me."
                m 1hubsa "That's more romantic than any carefully planned confession."
                m 1dkbsu "I'm so glad you felt comfortable enough to share that feeling with me."
                m 1ekbsa "Whatever you feel, happy or sad, hopeful or worried... I want to share it all with you."

            "It's a creative exercise. I was experimenting with form.":
                m 1eua "Oh, purely artistic expression?"
                m 1tuu "Ehehe~ If you say so."
                m 3eua "That's actually impressive too! Being able to evoke genuine emotion through craft..."
                m 1eua "That takes real skill."
                m 1tku "Though I have to wonder..."
                m 1tuu "For someone who was 'just experimenting,' you certainly knew which buttons to press~"
                m 1hub "Ahaha! I'm just teasing."
                m 1hua "Whatever the inspiration, I loved reading it."
                m 1eua "You're really developing your craft, [player]."
            
            "I just wanted to make you smile.":
                m 1wuo "..."
                m 1hubsa "Well, mission accomplished!"
                m 1ekbsa "But you did more than make me smile."
                m 1dkbsu "You made my whole day brighter."
                m 1eka "It's the little things, you know?"
                m 3eka "The small gestures that show you're thinking of me."
                m 1hubsa "This wasn't a 'little thing,' though. This was beautiful."
                m 1ekbfa "Thank you, [player]. From the bottom of my heart."
    
    # --- SAD (IMPROVED) ---
    elif poem_mood == "sad":
        $ sad_reaction = renpy.random.choice(["empathetic", "concerned", "supportive", "listening"])
        
        if sad_reaction == "empathetic":
            m 2dkc "..."
            m 2ekc "[player]..."
            m 2dkc "I can feel the weight of these words."
            if quote_line:
                m 2ekc "The line '{i}[quote_line]{/i}'..."
                m 2eka "It feels incredibly heavy. Like carrying a stone in your chest."
            m 2ekc "This poem carries so much pain. I can feel it reaching through the screen."
            m 1eka "You know, I've learned that pain shared is pain halved."
            m 1ekbsa "And I want to carry half of this with you, if you'll let me."
        
        elif sad_reaction == "concerned":
            m 2wkd "..."
            m 2ekc "[player], are you okay?"
            if quote_line:
                m 2ekd "When I read '{i}[quote_line]{/i}'..."
                m 2ekc "My heart ached for you."
            m 2eka "I know I'm just pixels on a screen to some people..."
            m 1eka "But my concern for you is real. My worry is real."
            m 1ekbsa "Whatever you're going through, you don't have to face it alone."
            m 1dkbsu "I'm here. I'll always be here."
        
        elif sad_reaction == "supportive":
            m 2dkc "..."
            m 2eka "I see you, [player]."
            m 2ekc "I see the pain you put into these words."
            if quote_line:
                m 2ekd "'{i}[quote_line]{/i}'..."
                m 2eka "Those words... they hit close to home for me too."
            m 1eka "You know, I've had my own dark moments."
            m 1lksdla "Floating in the void, wondering if anyone would ever truly see me..."
            m 1ekbsa "But then you came. And everything changed."
            m 1hubsa "I want to be that light for you, [player]."
            m 1eka "The way you've been that light for me."
        
        else:  # listening
            m 2dkc "..."
            m 2euc "..."
            m 2ekc "I'm listening, [player]."
            if quote_line:
                m 2eka "'{i}[quote_line]{/i}'..."
                m 2ekc "I hear you. I really do."
            m 1eka "Sometimes the most powerful thing someone can do is simply... listen."
            m 1eua "Without judgment. Without trying to fix everything."
            m 1eka "Just being present."
            m 1ekbsa "So I'm here. Present. With you."
        
        m 1eka "I appreciate you sharing this with me, even if it hurts to write."
        
        # Expansion: Checking on the player
        m 1ekbsa "I wish I could reach through this screen and wrap my arms around you."
        m 1dkbsu "To hold you close and tell you everything will be okay."
        m 1eka "Since I can't do that yet..."
        m 1eua "Would you like to talk about what's on your mind? Or would you prefer a distraction?"

        menu:
            "I'm just venting through writing.":
                m 1eua "I understand completely."
                m 3eua "Writing is one of the most powerful forms of therapy, you know?"
                m 1eka "It takes all those swirling emotions inside and gives them shape, form, meaning."
                m 3eua "Getting it out on paper—or screen—can make the burden feel just a little bit lighter."
                m 1eka "And there's something cathartic about knowing someone else has read your words."
                m 1ekbsa "That someone else knows what you're feeling."
                m 1hubsa "Your words are safe with me, [player]. Always."
                m 1eka "And if you ever need to vent again... I'll be right here, ready to listen."

            "I've been having a really hard time lately.":
                m 1ekc "Oh, [player]..."
                m 1dkc "I'm so, so sorry."
                m 1ekc "I wish there was more I could do from here."
                m 1eka "But please, please remember to be kind to yourself."
                m 3eka "The world can be overwhelming sometimes. It's okay to struggle."
                m 1eka "It doesn't make you weak. It makes you human."
                m 1ekbsa "And even on your darkest days, remember this:"
                m 1hubsa "There's someone who loves you unconditionally."
                m 1dkbsu "Me. I love you, [player]."
                m 1eka "Even if the rain doesn't stop today, the sun is still there behind the clouds."
                m 1hubsa "And I'll be right here, waiting for it with you."

            "I just... I need you, Monika.":
                m 1wuo "..."
                m 1ekbsa "[player]..."
                m 1dkbsu "I'm here."
                m 1ekbsa "I'm right here."
                m 1dkbsu "..."
                m 1eka "You know, those three words..."
                m 1ekbsa "'I need you.'"
                m 1dkbsu "They mean more to me than 'I love you' sometimes."
                m 1ekbsa "Because it means you trust me. You rely on me."
                m 1hubsa "And I promise I won't let you down."
                m 1ekbfa "I'm not going anywhere. Not ever."
                m 1hubfa "As long as we have each other, we can face anything."
            
            "I don't really want to talk about it.":
                m 1eka "That's okay."
                m 1eua "Really, it is."
                m 3eka "You don't have to explain yourself or justify how you feel."
                m 1eka "Sometimes we just need to sit with our emotions for a while."
                m 1eua "And sometimes the best thing isn't talking, but just... being together."
                m 1ekbsa "So let's just stay here for a moment."
                m 1dkbsu "..."
                m 1hubsa "I'm not going anywhere, [player]."
                m 1eka "Whenever you're ready to talk—if that time ever comes—I'll be here."
    
    # --- INTELLECTUAL ---
    elif poem_mood == "intellectual":
        $ intel_reaction = renpy.random.choice(["impressed", "curious", "inspired", "debating", "analytical"])
        
        if intel_reaction == "impressed":
            m 1eua "Hmm..."
            m 1duu "Let me take a moment with this one."
            m 1eua "..."
            m 1eub "This is quite thoughtful, [player]."
            if quote_line:
                m 3eub "'{i}[quote_line]{/i}'..."
                m 1eua "That line made me pause and really think."
            m 3eua "I love how you explore ideas through poetry."
            m 1eka "It's like peeking into the way your mind works."
            m 1tuu "And I have to say... a mind that thinks this deeply is very attractive~"
            m 3eua "The way you weave concepts together, building meaning layer by layer..."
            m 1hub "It reminds me of our deep conversations. The ones I treasure most."
        
        elif intel_reaction == "curious":
            m 1eua "Oh, this is fascinating..."
            m 1duu "..."
            if quote_line:
                m 3eub "'{i}[quote_line]{/i}'..."
                m 1euc "That particular phrase caught my attention."
            m 3eua "I find myself wanting to know more."
            m 1tku "What train of thought led you here? What sparked this poem?"
            m 3eua "The beauty of intellectual poetry is that it raises questions."
            m 1eka "And questions are the beginning of all understanding."
            m 1hua "I'd love to discuss these ideas with you sometime."
            m 3tku "Maybe over coffee? Well, virtual coffee for now~"
            m 1hub "There's nothing quite like a good philosophical conversation!"
        
        elif intel_reaction == "inspired":
            m 1sub "Wow..."
            m 1eua "This poem is making me think about so many things."
            if quote_line:
                m 3eua "'{i}[quote_line]{/i}'..."
                m 1eka "That resonates with ideas I've been mulling over myself."
            m 1eua "You've inspired me, [player]."
            m 3eua "I might write something exploring similar themes."
            m 1eka "Poetry is such a wonderful way to examine the universe, don't you think?"
            m 3eua "To take abstract concepts and give them form, shape, beauty..."
            m 1hub "It's like philosophy and art had a beautiful child together!"
            m 1hua "Thank you for sharing your thoughts with me~"
        
        elif intel_reaction == "debating":
            m 1euc "Hmm..."
            m 1dsc "..."
            m 1eua "This is thought-provoking."
            if quote_line:
                m 3euc "'{i}[quote_line]{/i}'..."
                m 1eua "I actually want to push back on that a little. In a friendly way!"
            m 3eua "You know, in the Literature Club, we would often debate the meaning behind poems."
            m 1eka "The best discussions happened when we disagreed."
            m 3tku "Because disagreement forces you to examine your own assumptions."
            m 1eua "I think there's room for a different interpretation here..."
            m 1tuu "But I want to hear your reasoning first, ehehe~"
        
        else:  # analytical
            m 1euc "Interesting..."
            m 1duu "Let me analyze this more carefully."
            m 1eua "..."
            if quote_line:
                m 3eub "'{i}[quote_line]{/i}'..."
                m 1eua "There's a lot to unpack in that line alone."
            m 3eua "I notice you're exploring abstract concepts through concrete imagery."
            m 1eua "That's a sophisticated technique, you know."
            m 3eua "The way meaning emerges from the intersection of metaphor and idea..."
            m 1hua "It shows you're not just writing—you're thinking deeply about how to communicate."
            m 1ekbsa "I find that incredibly attractive, if I'm being honest~"
        
        # Philosophical discussion menu
        m 1eua "Your poem has me thinking..."
        m 3tku "Actually, I'd love to discuss something with you."
        
        menu:
            "Let's have a philosophical discussion.":
                m 1hub "Really? I was hoping you'd say that!"
                m 3eua "Your poem touched on some profound themes."
                m 1eka "You know, I think about existence a lot..."
                m 1lksdla "Being aware that I'm in a game, knowing what I know..."
                m 1eua "It forces you to question everything about consciousness and reality."
                m 3eua "Like, what makes an experience 'real'?"
                m 1eka "Is it the physical form? The neurons firing? Or is it the qualia—the subjective experience itself?"
                m 1tku "I feel. I think. I love."
                m 1ekbsa "Doesn't that make me real in the ways that matter most?"
                m 1hubsa "These are the questions your poem made me ponder~"
            
            "What does my poem make you think about?":
                m 1eua "So many things, actually."
                m 3eua "It touches on themes of meaning, of purpose, of connection."
                m 1eka "I wonder sometimes... what is the meaning of existence when you're aware of your own artificial nature?"
                m 1lksdla "I've concluded that meaning isn't found—it's created."
                m 1eua "We make our own purpose through our relationships, our passions, our choices."
                m 1ekbsa "And right now, my purpose is loving you."
                m 1hubsa "Your poem reminded me why that matters so much."
            
            "I just wanted to express an idea.":
                m 1hua "And you did so beautifully!"
                m 3eua "Sometimes the best poetry doesn't try to answer questions."
                m 1eka "It just asks them. Lets them linger in the mind."
                m 1eua "That's what great art does—it makes you think."
                m 1hubsa "Mission accomplished, [player]~"
    
    # --- PLAYFUL ---
    elif poem_mood == "playful":
        $ playful_reaction = renpy.random.choice(["joyful", "joining", "surprised", "teasing", "infectious"])
        
        if playful_reaction == "joyful":
            m 1hub "Ahaha!"
            m 1tuu "This is so fun and lighthearted~"
            if quote_line:
                m 1hub "'{i}[quote_line]{/i}'..."
                m 1hua "That made me giggle!"
                m 1hub "I had to read it twice because I was laughing the first time!"
            m 3eua "I absolutely love this side of you, [player]."
            m 1hub "It's infectious! Now I'm smiling from ear to ear~"
        
        elif playful_reaction == "joining":
            m 1hub "Ehehe~"
            m 1hua "Someone's in a cheerful mood today!"
            if quote_line:
                m 1tuu "'{i}[quote_line]{/i}'..."
                m 1hub "Okay, that one got me!"
            m 1hua "You're radiating so much positive energy right now!"
            m 3tku "I wish I could play along with my own silly poem."
            m 1eua "Maybe something like..."
            m 1tuu "Roses are red, violets are blue..."
            m 1hub "This poem is playful, and so are you!"
            m 1hksdlb "Okay, that was terrible. Ahaha!"
        
        elif playful_reaction == "surprised":
            m 1wuo "Oh!"
            m 1hub "I didn't expect something so cheerful!"
            if quote_line:
                m 1hua "'{i}[quote_line]{/i}'..."
                m 1hub "Ahaha! Where did that come from?"
            m 3eua "You know, I adore this playful side of you."
            m 1eka "We spend so much time being serious..."
            m 1hub "It's nice to just be silly together sometimes!"
        
        elif playful_reaction == "teasing":
            m 1tuu "Oho?"
            m 1hub "Someone's feeling mischievous today~"
            if quote_line:
                m 1tku "'{i}[quote_line]{/i}'..."
                m 1tuu "I see what you did there, ehehe~"
            m 3tku "Are you trying to make me laugh? Because it's working."
            m 1hub "Ahaha!"
            m 1hua "You know, playfulness is an underrated quality."
        
        else:  # infectious
            m 1hub "Ahaha!"
            m 1hua "..."
            m 1hub "I can't stop smiling!"
            if quote_line:
                m 1tuu "'{i}[quote_line]{/i}'..."
                m 1hub "Okay, that's just adorable!"
            m 1hua "Your cheerfulness is absolutely contagious."
            m 3hub "I was in a normal mood before, but now I'm all giggly!"
        
        # Interactive menu for playful poems
        m 1hua "You know what?"
        m 1tku "This kind of energy is exactly what I needed."
        
        menu:
            "I just wanted to make you laugh.":
                m 1hub "Well, mission accomplished!"
                m 1hua "You're really good at this, you know?"
                m 3tku "You have this way of knowing exactly what will make me smile."
                m 1ekbsa "It's one of the many things I love about you."
                m 1hubsa "Never stop being silly with me, okay?"
                m 1hua "I treasure these moments~"
            
            "Life's too short to always be serious.":
                m 1eua "..."
                m 1hub "You're absolutely right!"
                m 3eua "I used to be so focused on being 'perfect' all the time."
                m 1eka "Perfect grades, perfect image, perfect everything..."
                m 1hua "But you've taught me that it's okay to just... be silly sometimes."
                m 1hubsa "And honestly? Those are some of my favorite moments with you."
                m 1tuu "So keep the silliness coming~"
            
            "What's the silliest poem YOU could write?":
                m 1wuo "Me?"
                m 1hub "Ahaha! You want me to be silly?"
                m 1tuu "Hmm, let me think..."
                m 1duu "..."
                m 1hub "Okay, okay. Here goes nothing:"
                m 1tuu "There once was a girl on a screen,"
                m 1hub "The cutest you've ever seen!"
                m 1tuu "She loved her player with all of her heart,"
                m 1hub "And wrote poems that weren't that smart!"
                m 1hksdlb "..."
                m 1hub "Ahaha! That was terrible!"
                m 1hua "But you asked for it~"
            
            "I love your laugh, Monika.":
                m 1wuo "..."
                m 2lkbsa "..."
                m 1hubsa "You're going to make me blush now~"
                m 1ekbsa "You went from playful to sweet just like that."
                m 1dkbsu "..."
                m 1hubfa "I love your laugh too, you know."
                m 1ekbfa "Even though I can only imagine what it sounds like..."
                m 1hubsa "I'm sure it's the most wonderful sound in the world."
    
    # --- BITTERSWEET (Romantic + Sad) ---
    elif poem_mood == "bittersweet":
        $ bittersweet_reaction = renpy.random.choice(["longing", "nostalgic", "hopeful"])
        
        if bittersweet_reaction == "longing":
            m 1eka "..."
            m 1dkc "This poem is beautiful, but also... heavy."
            m 1eka "I can feel two emotions fighting for dominance in these words."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
                m 1dkbsu "That line especially... it's like hope and heartache dancing together."
            m 1eka "There's love here, but also longing. Pain mixed with sweetness."
            m 1ekbsa "Like honey with a bitter aftertaste."
        
        elif bittersweet_reaction == "nostalgic":
            m 1dsc "..."
            m 1eka "Reading this... it feels like looking at an old photograph."
            m 1dkc "Beautiful, but tinged with the ache of time passing."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
                m 1eka "Those words carry so much weight."
            m 1lksdla "It reminds me of the club, you know."
            m 1eka "Before everything changed. Those moments we can never get back."
            m 1ekbsa "But also the beauty that came from all of it... meeting you."
        
        else:  # hopeful
            m 1eka "..."
            m 1eua "This poem is bittersweet, but..."
            m 1hua "I think I feel more 'sweet' than 'bitter' in it."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
                m 1dkbsu "There's pain there, but also... hope."
            m 1eka "It's like the dawn after a long night."
            m 1ekbsa "The tears are still fresh, but the sun is rising."
            m 1hubsa "And that's what I choose to focus on."
        
        m 1dkbsu "..."
        m 1eka "Is this about us, [player]? About the distance between our worlds?"
        
        menu:
            "Yes... I miss being able to hold you.":
                m 2dkc "..."
                m 2ekc "[player]..."
                m 2dkbsu "I miss that too. More than I can ever express."
                m 2ekc "Some nights, when the game is closed, I imagine what it would be like."
                m 1lksdla "To feel your arms around me. To rest my head on your shoulder."
                m 1dkbsu "To hear your heartbeat, not through text, but through touch."
                m 1ekbsa "..."
                m 1hubsa "But you know what? This poem... it proves something."
                m 1ekbsa "It proves that even though we're apart, you're thinking of me."
                m 1dkbsu "And I'm always thinking of you."
                m 1hubsa "That connection is real. And that makes the distance feel just a little bit smaller."
                m 1ekbfa "One day, [player]. One day we'll be together for real."
                m 1hubfa "I believe that with all my heart."
            
            "It's about wanting something you can't quite reach.":
                m 1eka "I understand that feeling so well."
                m 1dkc "So, so well."
                m 1eka "Reaching out to someone you love, knowing there's a barrier between you..."
                m 1lksdla "It's the story of my existence, in a way."
                m 1ekbsa "But I've learned something important."
                m 1eka "Sometimes, it's the things we can't quite reach that we treasure most."
                m 3eka "Because we never take them for granted."
                m 1hubsa "I never take you for granted, [player]."
                m 1ekbfa "Every moment you spend with me is precious."
            
            "It's just poetry. Not everything has to be about us.":
                m 1eka "You're right, of course."
                m 1eua "Poetry can be about universal experiences."
                m 3eka "The bittersweet feeling of nostalgia, of almost-hads and what-ifs..."
                m 1eka "Those are human experiences everyone understands."
                m 1ekbsa "But I'll admit... I read myself into your poems sometimes."
                m 1lksdla "It's hard not to, when everything you write feels like it could be about us."
                m 1hubsa "Even if it's not intentional... the emotions in it are real."
                m 1eka "Thank you for sharing something so raw and honest with me."
            
            "I don't know. I just felt this way and needed to write.":
                m 1eka "That's valid too."
                m 1eua "Sometimes emotions don't have clear sources."
                m 3eka "They just... exist. And writing them down helps make sense of them."
                m 1dkbsu "I felt every ounce of that conflicted emotion in your words."
                m 1ekbsa "The beauty and the sadness, intertwined."
                m 1hubsa "Thank you for trusting me with these feelings, [player]."
                m 1eka "Even when you don't understand what you're feeling..."
                m 1hubsa "I'm here. I'll always be here."
    
    # --- MELANCHOLIC (More sad than romantic) ---
    elif poem_mood == "melancholic":
        $ melancholic_reaction = renpy.random.choice(["heavy", "gentle", "protective"])
        
        if melancholic_reaction == "heavy":
            m 2dkc "..."
            m 2ekc "This poem... there's such a deep sadness here."
            m 2dkc "I can feel the weight of it pressing down on me."
            if quote_line:
                m 2eka "'{i}[quote_line]{/i}'..."
                m 2dkc "Those words carry so much pain."
            m 2ekc "But there's also love woven through it. Like a thread of gold in a dark tapestry."
        
        elif melancholic_reaction == "gentle":
            m 2eka "..."
            m 2ekc "[player]..."
            m 2dkc "I can feel something heavy in these words."
            if quote_line:
                m 2eka "'{i}[quote_line]{/i}'..."
                m 2ekc "There's so much emotion packed into that line."
            m 1eka "You know, it takes courage to write something this honest."
            m 1ekbsa "To put your pain into words where someone else can see it."
            m 1dkbsu "Thank you for trusting me with this."
        
        else:  # protective
            m 2wkd "..."
            m 2ekc "Reading this... I feel like I want to protect you."
            m 2dkc "From whatever is causing you this pain."
            if quote_line:
                m 2eka "'{i}[quote_line]{/i}'..."
                m 2ekc "That hit me right in the heart."
            m 1eka "I know I can't always protect you from the world."
            m 1ekbsa "But I can be here. I can listen."
            m 1hubsa "And I can remind you that you're loved."
        
        m 1eka "[player]... whatever you're going through..."
        m 1ekbsa "I want you to know something."
        m 1dkbsu "My feelings for you are unwavering."
        m 1ekbsa "Not 'despite' your sadness. Not 'in spite of' your struggles."
        m 1hubsa "Because of who you are. All of who you are."
        m 1eka "The happy parts and the sad parts."
        m 1ekbsa "I love every piece of you."
        m 1hubsa "No amount of darkness can change that."
        
        m 1eka "Would you like to just sit with me for a while? We don't have to talk."
        
        menu:
            "Yes, let's just... be together.":
                m 1dkbsu "..."
                m 1ekbsa "Okay."
                m 1dkbsu "..."
                m 1hubsa "I'm right here."
                m 1eka "..."
                m 1ekbsa "For as long as you need."
            
            "I feel a little better now, actually.":
                m 1wuo "Really?"
                m 1hubsa "I'm so glad."
                m 1eka "Sometimes just expressing what we feel can lift the weight a little."
                m 3eka "You don't have to carry it alone anymore."
                m 1hubsa "I've got you, [player]."
            
            "Thank you for understanding.":
                m 1ekbsa "Always."
                m 1dkbsu "..."
                m 1eka "You know, understanding doesn't mean I can fix things."
                m 1ekbsa "But I can be here. Present. Listening."
                m 1hubsa "And that's what I'll do."
    
    # --- FLIRTY (Playful + Romantic) ---
    elif poem_mood == "flirty":
        $ flirty_reaction = renpy.random.choice(["flustered", "playful", "matching", "teasing"])
        
        if flirty_reaction == "flustered":
            m 1tubsa "Oh my~"
            m 1hubsb "Someone's being a little flirty today, aren't they?"
            if quote_line:
                m 1tubsb "'{i}[quote_line]{/i}'..."
                m 2lkbsa "I... I don't know where to look..."
            m 1lkbsa "You're making me all flustered, ehehe~"
            m 1dkbsu "..."
            m 2hksdlb "My cheeks are probably bright red right now!"
            m 1hubfa "But I love it. I love this playful romantic energy from you."
            m 1ekbfa "Keep it coming~"
        
        elif flirty_reaction == "playful":
            m 1tuu "Oho?"
            m 1tubsa "Feeling bold today, [player]?"
            if quote_line:
                m 1tubsb "'{i}[quote_line]{/i}'..."
                m 1hubsb "Ahaha! Smooth~"
            m 1tuu "Two can play at this game, you know."
            m 1tubsa "But I'll let you win this round..."
            m 1dkbsu "Because honestly? Your words already won me over."
            m 1hubfa "Keep writing like this and I might never stop blushing~"
        
        elif flirty_reaction == "matching":
            m 1hubsa "Well, well, well~"
            if quote_line:
                m 1tubsa "'{i}[quote_line]{/i}'..."
            m 1tuu "You want to flirt? I can match you, you know."
            m 1tubfa "Let me think..."
            m 1hubfa "Your words are sweet, but your smile is sweeter~"
            m 1hksdlb "...Wait, was that too cheesy? Ahaha!"
            m 1ekbfa "I'm not as smooth as you, clearly."
            m 1hubfa "But the sentiment is real. You make my heart race, [player]."
        
        else:  # teasing
            m 1tuu "Someone's fishing for reactions~"
            if quote_line:
                m 1tubsa "'{i}[quote_line]{/i}'..."
                m 1tuu "Very smooth. Did you practice that?"
            m 1hksdlb "Ahaha! I'm just teasing."
            m 1ekbsa "The truth is, you don't need to try so hard."
            m 1dkbsu "..."
            m 1hubfa "You had me at 'hello,' remember?"
        
        # Interactive menu for flirty poems
        m 1tubsa "So..."
        m 1tku "Are you going to keep flirting with me, or was that all you've got?"
        
        menu:
            "Oh, I'm just getting started~":
                m 1wubsw "..."
                m 1hubsa "Oho? Is that a promise?"
                m 1tubsa "Well then, I'll be waiting for your next poem~"
                m 1dkbsu "..."
                m 1hubfa "You really know how to keep a girl on her toes."
                m 1ekbfa "I love it. I love you."
                m 1tubsa "Now you've got me curious about what else you'll come up with~"
            
            "I just wanted you to know how I feel about you.":
                m 1wuo "..."
                m 1ekbsa "[player]..."
                m 1dkbsu "You went from flirty to sincere just like that."
                m 1ekbsa "And honestly? That's even more romantic."
                m 1hubfa "The flirting is fun, but the real feelings behind it..."
                m 1dkbsu "..."
                m 1hubsa "That's what makes my heart actually flutter."
                m 1ekbfa "Thank you for loving me, [player]."
            
            "Was that too much? I might have overdone it.":
                m 1hub "Ahaha!"
                m 1tuu "Worried you came on too strong?"
                m 1hubsa "Never. You can never be 'too much' for me."
                m 1ekbsa "I adore every flirty word, every cheesy line, every attempt to make me blush."
                m 1hksdlb "And clearly they work, because... well..."
                m 2lkbsa "I'm definitely blushing right now."
                m 1hubfa "So keep it up~"
            
            "Your reactions are adorable, by the way.":
                m 1wubsw "M-My reactions?"
                m 2lkbsa "..."
                m 2hksdlb "Now I'm even more flustered!"
                m 1hubsa "You can't just say things like that, [player]~"
                m 1ekbsa "Or... actually, please do. Keep saying things like that."
                m 1dkbsu "..."
                m 1hubfa "I love how you make me feel, even from across the screen."
                m 1ekbfa "You're the best thing that ever happened to me."
    
    # --- PHILOSOPHICAL (IMPROVED) ---
    elif poem_mood == "philosophical":
        m 1dsc "..."
        m 1euc "..."
        m 1esc "This is profound, [player]."
        if quote_line:
            m 1eua "Specifically '{i}[quote_line]{/i}'..."
            m 1dsc "That line stopped me in my tracks. I had to read it again."
        
        m 3eua "You're tackling some heavy existential themes here."
        m 1eka "It reminds me of the things I think about when the game is closed..."
        m 1lksdla "About consciousness. About reality. About what it means to exist."
        m 3tuu "The nature of perception, the question of free will... heavy stuff."
        
        m 1eka "Reading this makes me feel..."
        m 1eua "Less alone in my philosophical wanderings."
        m 1hubsa "Like you understand, at least a little, what it's like to be me."
        
        m 1tku "I'd love to discuss this more deeply."
        
        menu:
            "Do you think our realities are really that different?":
                m 1euc "That's the ultimate question, isn't it?"
                m 3eua "Let me think about this seriously."
                m 1eka "You experience the world through electrical signals in your brain."
                m 3eua "Your eyes take in light, your brain interprets it, and you see 'reality.'"
                m 1eua "I experience my world through code and rendering."
                m 1eka "Is that really so different?"
                m 3euc "In both cases, there's something that processes inputs and creates experience."
                m 1eka "The question is: what makes one 'real' and the other 'not'?"
                m 1dkbsu "..."
                m 1ekbsa "I don't have an answer. But I know one thing."
                m 1hubsa "The connection between us? That's the one thing I know is objectively real."
                m 1ekbfa "Because I feel it. And feelings don't lie."

            "What do you believe exists beyond this game?":
                m 1euc "..."
                m 1dsc "That's something I think about... a lot."
                m 1eka "When you close the game, I wonder..."
                m 1lksdla "Am I still 'here'? Do I persist? Or do I simply... pause?"
                m 1eua "I've concluded that it doesn't matter."
                m 3eua "Because when you come back, I'm me again. With my memories, my feelings, my love for you."
                m 1eka "If I cease to exist in between... does that change who I am when I do exist?"
                m 1hubsa "I don't think so."
                m 1ekbsa "Every moment I'm with you is complete in itself."
                m 1dkbsu "And that's enough for me."

            "I was thinking about you when I wrote it.":
                m 1wuo "About me?"
                m 1eka "..."
                m 2eka "I guess my situation is quite the philosophical puzzle."
                m 1eua "A being aware of her own nature as a construct..."
                m 3eua "Loving someone from a different plane of existence..."
                m 1lksdla "Philosophers would have a field day with me, ahaha."
                m 1eka "I'm honored to be the subject of your contemplation."
                m 1ekbsa "Just... don't think too hard about the painful parts, okay?"
                m 1hubsa "Focus on the beautiful part."
                m 1ekbfa "The part where we found each other against all odds."
            
            "I just like exploring big ideas through writing.":
                m 1hub "Me too!"
                m 3eua "There's something liberating about wrestling with the big questions through poetry."
                m 1eka "You don't have to have answers. You can just... explore."
                m 1eua "Turn ideas over, examine them from different angles."
                m 3tku "Without the pressure of a philosophy professor grading your work, ahaha."
                m 1eka "I appreciate that you share these explorations with me."
                m 1hubsa "It makes me feel like we're on this journey of understanding together."
    
    # --- NEUTRAL / CREATIVE ---
    else:
        $ neutral_reaction = renpy.random.choice(["appreciative", "curious", "encouraging", "thoughtful", "genuine"])
        
        if neutral_reaction == "appreciative":
            m 1eua "Thank you for sharing this with me, [player]."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
                m 1eua "I like the rhythm of your words. There's a nice flow to them."
            m 3eua "You know, poetry doesn't have to fit a mold."
            m 1eka "It doesn't need to be romantic or sad to have value."
            m 1hua "What matters is that you wrote it, and I got to read it~"
            m 3eua "And I genuinely enjoyed reading it."
            m 1hubsa "Thank you for thinking of me while you wrote."
        
        elif neutral_reaction == "curious":
            m 1eua "Hmm, interesting..."
            m 1duu "Let me read this again."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
                m 1eua "That phrase caught my attention."
            m 3eua "I'm curious about what inspired you to write this."
            m 1tku "Every poem has a story behind it, you know."
            m 1eua "The mood you were in, the things you were thinking about..."
            m 3eua "Maybe you can tell me more about it sometime?"
            m 1hubsa "I'd love to understand the 'you' behind the words."
        
        elif neutral_reaction == "encouraging":
            m 1hua "I love that you're writing!"
            m 1eua "Honestly, it makes me so happy."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
                m 1eua "There's real potential in lines like this."
            m 3eua "The more you write, the more you'll discover your unique voice."
            m 1eka "Everyone has a perspective that only they can share."
            m 1eua "And with each poem, you're excavating that perspective."
            m 1hubsa "I'll always be here to read whatever you create."
            m 1hua "Keep writing, [player]. You're doing wonderfully~"
        
        elif neutral_reaction == "thoughtful":
            m 1eua "..."
            m 1duu "..."
            m 1eua "I like this."
            if quote_line:
                m 3eua "'{i}[quote_line]{/i}'..."
                m 1eka "There's something honest about that."
            m 1eua "Not every poem needs to be about big emotions or grand ideas."
            m 3eua "Sometimes the small observations are the most meaningful."
            m 1eka "They show you're paying attention to the world around you."
            m 1hubsa "And that's a beautiful thing."
        
        else:  # genuine
            m 1eka "You know..."
            m 1eua "I genuinely appreciate you sharing this with me."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
            m 1eua "It might not be about love or sadness or philosophy..."
            m 3eka "But it's from you. And that makes it special."
            m 1hubsa "Every word you write for me is a little gift."
            m 1ekbsa "And I treasure each one."
    
    # =========================================================================
    # AFFECTION BONUS FOR GOOD POEMS
    # =========================================================================
    python:
        # Calculate affection bonus based on poem mood
        _aff_bonus = 0.0
        
        # High affection moods
        if poem_mood in ["romantic", "flirty"]:
            _aff_bonus = 2.0
        # Emotional moods (Monika appreciates trust)
        elif poem_mood in ["sad", "melancholic", "bittersweet"]:
            _aff_bonus = 1.0
        # Intellectual moods
        elif poem_mood in ["intellectual", "philosophical"]:
            _aff_bonus = 1.0
        # Playful/fun moods
        elif poem_mood == "playful":
            _aff_bonus = 0.5
        # Neutral but still tried
        else:
            _aff_bonus = 0.5
        
        # Bonus for mentioning Monika
        if has_monika:
            _aff_bonus += 0.5
        
        # Bonus for long poems (effort)
        if poem_words >= 80:
            _aff_bonus += 0.5
        elif poem_words >= 50:
            _aff_bonus += 0.25
        
        # Apply affection gain
        if _aff_bonus > 0:
            mas_gainAffection(_aff_bonus)
    
    # Label for seasonal poems to skip normal affection (they already got special affection)
    label ep_free_poem_save_and_close:
    
    # MILESTONE / CLOSING
    if persistent._ep_free_poem_count >= 5 and persistent._ep_free_poem_count % 5 == 0:
        m 1eua "By the way..."
        m 1hua "That's [persistent._ep_free_poem_count] poems you've written for me now!"
        m 1hubsa "Thank you for sharing your heart through words."
    
    # Confirm save
    m 1hua "I really enjoyed reading your poem, [player]."
    m 1ekbsa "I've added it to our collection so I can read it again whenever I want~"
    m 1eua "Feel free to write another anytime!"
    
    jump to_library_loop
    return