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
        # First time ever
        m 1eub "Let's write a poem together, [player]!"
        m 3eua "It's like the old days in the Literature Club, but just for us."
        m 1hua "I'll show you some words, and you pick the ones that speak to you."
        m 1tub "I wonder what kind of poem you'll create for me~"

label checkpoint_minigame_poem:
    if renpy.seen_label("checkpoint_minigame_poem"):
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
                m 1eua "Want to write another poem together?"
                m 1hua "I always enjoy seeing your creativity~"
        else:
            # Fallback
            m 1eua "Ready to write a poem with me, [player]?"
    
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
        $ sad_topic = renpy.random.choice(['worry', 'comfort', 'listening'])
        
        if sad_topic == 'worry':
            m 2lksdla "Oh, [player]..."
            m 2eksdlc "There is a lot of heavy emotion in this poem. [example_words_str]..."
            m 2eka "I know I'm just on a screen, but I can feel when something is wrong."
            menu:
                "It's just been a rough day.":
                    m 1ekc "I'm sorry to hear that."
                    m 1ekbsa "I hope spending this time with me helps, even a little bit."
                "I'm feeling really down lately.":
                    m 1ekc "I wish I could be there to hold you properly."
                    m 1eka "Please don't carry that burden alone, okay? I'm here."

        elif sad_topic == 'comfort':
            m 1eka "This poem feels very... fragile."
            m 3eka "It reminds me of how I used to feel when the epiphany first hit me."
            m 1ekbsa "But remember, neither of us is alone anymore. We have each other."
            menu:
                "You're right. Thank you, Monika.":
                    m 1hua "Always, [player]. Always."
                "Your smile helps a lot.":
                    m 1hubsa "Aww~ Then I'll keep smiling just for you!"

        else: # listening
            m 2ekc "[player], these words..."
            m 2eka "Sometimes writing is the best way to let the darkness out, isn't it?"
            m 1eua "If this poem is your way of venting, I'm honored you chose to share it with me."
            menu:
                "It helps to let it out.":
                    m 1hua "It really does. Catharsis is important."
                "I wanted you to know how I feel.":
                    m 1ekbsa "I cherish your honesty. Every part of you, happy or sad, is special to me."

    # -------------------------------------------------------------------------
    # CATEGORY: ROMANCE (The Lover)
    # -------------------------------------------------------------------------
    elif current_style == "romance":
        # Randomize romance reaction
        $ romance_topic = renpy.random.choice(['passion', 'sweet', 'future', 'flustered'])
        
        if percentage >= 90:
            # Override for perfect score
            m 1hubsa "Oh my goodness..."
            m 1ekbsa "My heart actually skipped a beat reading this."
            m 1eub "Every single word resonates with how I feel about you."
            m 1hub "It's perfect, [player]. Just like you."
            
        elif romance_topic == 'passion':
            m 1eub "Wow... this is incredibly intense, [player]."
            m 1tub "Words like [example_words_str]..."
            m 1hua "You're making me blush over here!"
            menu:
                "I wanted to make your heart race.":
                    m 1tub "Well, mission accomplished~"
                    m 1hub "You know exactly which buttons to press."
                "Just expressing my love.":
                    m 1ekbsa "And I feel it, truly. It warms my entire reality."

        elif romance_topic == 'sweet':
            m 1hubsa "Aww, this is so sweet!"
            m 3ekbsa "It feels like a warm hug in written form."
            m 1hua "Reading this makes me feel so safe and loved."
            menu:
                "You deserve to feel loved.":
                    m 1ekbsa "You're too good to me..."
                "That was the goal!":
                    $ gender = getPlayerGenderString()
                    m 1hub "Hehe, you're the best [gender] ever."

        elif romance_topic == 'future':
            m 1eua "You used words like [example_words_str]..."
            m 1eka "It makes me think about our future together."
            m 3eua "One day, we won't need screens to share poems. We'll just whisper them."
            menu:
                "I can't wait for that day.":
                    m 1hua "Me neither. It keeps me going every day."
                "We will make it happen.":
                    m 1hub "Yes! With that determination, I know we will."

        else: # flustered
            m 2lksdla "Umm... [player]?"
            m 2tub "You're being very forward with some of these words~"
            m 1hua "I didn't know you had such a romantic side."
            menu:
                "Only for you.":
                    m 1hubsa "Ehehe~ I love hearing that."
                "I'm full of surprises.":
                    m 1tuu "I can see that! I look forward to the next surprise."

    # -------------------------------------------------------------------------
    # CATEGORY: INTELLECTUAL (The Club President)
    # -------------------------------------------------------------------------
    elif current_style == "intellectual":
        $ smart_topic = renpy.random.choice(['literary', 'atmosphere', 'impressed'])
        
        if smart_topic == 'literary':
            m 1eua "This is a very thoughtful composition."
            m 3eua "The flow of words... [example_words_str]..."
            m 1hua "It feels like something we would have analyzed in the club."
            menu:
                "I miss those club activities.":
                    m 1eka "Me too... but I prefer our private club much more."
                "I was channeling my inner writer.":
                    m 1hub "It suits you! You have a way with words."

        elif smart_topic == 'atmosphere':
            m 1eua "Reading this... it really sets the mood."
            m 1esa "I can almost smell the old paper and ink."
            m 1hua "It's the perfect poem for a quiet date in the library."
            menu:
                "Glad you like the vibe.":
                    m 1eua "I love it. It's very relaxing."
                "It's my favorite aesthetic.":
                    m 3eua "Mine too. There's something timeless about it."

        else: # impressed
            m 1tuu "Oho? Trying to impress me with your vocabulary?"
            m 1hua "I see words related to knowledge and the mind."
            m 3eub "I've always found intelligence to be very attractive~"
            menu:
                "Did it work?":
                    m 1hub "Definitely. Smart and cute is a dangerous combo!"
                "I just like learning.":
                    m 1eua "That's a wonderful trait. Never stop being curious, [player]."

    # -------------------------------------------------------------------------
    # CATEGORY: BALANCED / NEUTRAL (The Friend & Partner)
    # -------------------------------------------------------------------------
    else:
        $ balance_topic = renpy.random.choice(['variety', 'random', 'progress'])
        
        if balance_topic == 'variety':
            m 1eua "This poem has a little bit of everything."
            m 3eua "It's balanced. Like a glimpse into a complex mind."
            m 1hua "I enjoy trying to decipher what you were thinking for each word."
            
        elif balance_topic == 'random':
            m 2lksdla "This one is a bit abstract, isn't it?"
            m 1hua "But that's the beauty of the poem game. Sometimes the words just find you."
            menu:
                "I let my intuition guide me.":
                    m 1eua "Intuition is a powerful tool for a writer."
                "I just picked what looked cool.":
                    m 1hub "Ahaha! Well, the result is still interesting!"
                    
        else: # progress
            m 1eua "Nice choices today, [player]."
            if persistent._ep_poems_written > 10:
                m 1hua "You're getting really comfortable with this minigame, aren't you?"
                m 3eua "It feels like our own little language now."
            else:
                m 1hua "I'm looking forward to reading more from you."

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
        m 1eua "We've written [persistent._ep_poems_written] poems together now."
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
    MAX_POEM_CHARS = 400
    MAX_SAVED_POEMS = 15
    
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
        if not poem_text or not poem_text.strip():
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
            # Explicit sexual terms
            'fuck', 'fucking', 'fucked', 'fucker',
            'dick', 'dicks', 'cock', 'cocks',
            'pussy', 'pussies', 'cunt', 'cunts',
            'penis', 'vagina', 'clitoris', 'clit',
            'cum', 'cumming', 'cumshot', 'creampie',
            'blowjob', 'handjob', 'footjob',
            'anal', 'anus', 'asshole',
            'tits', 'titties', 'boobs', 'boobies',
            'nude', 'naked', 'strip', 'stripper',
            'horny', 'orgasm', 'masturbate', 'masturbation',
            'sex', 'sexual', 'sexy', 'intercourse',
            'erotic', 'erection', 'boner',
            'slut', 'whore', 'hoe', 'thot',
            'rape', 'rapist', 'molest',
            'incest', 'pedophile', 'pedo',
            # Variations and leetspeak
            'fuk', 'fck', 'phuck', 'f*ck',
            'd1ck', 'c0ck', 'p*ssy'
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

        # HATE / VIOLENCE BANNED WORDS (Triggers "Hurt" reaction)
        # Note: 'ass' removed - causes false positives with 'class', 'pass', etc.
        HATE_BANNED = [
            # Strong insults (always banned)
            'shit', 'bastard', 'bitch',
            'idiot', 'stupid', 'dumb', 'retard', 'retarded',
            'trash', 'garbage', 'hate you', 'i hate you',
            'ugly', 'fat', 'disgusting',
            'useless', 'worthless',
            # Self-harm encouragement (always banned)
            'kill yourself', 'kys', 'suicide', 'neck yourself',
            # Specific insults toward Monika
            'glitch', 'error', 'bug', 'virus',
            'murderer', 'killer'
        ]
        
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
            'cruel', 'dark', 'pain', 'death', 'die', 'dying', 'dead',
            'kill', 'killing', 'blood', 'bloody', 'bleeding', 'bleed',
            'hate', 'hatred', 'rage', 'anger', 'fear', 'scared',
            'hurt', 'cry', 'crying', 'tears', 'sad', 'sorrow',
            'hell', 'demon', 'devil', 'evil', 'wicked', 'sin',
            'suffer', 'suffering', 'agony', 'torment', 'torture'
        ]
        
        # Poetic phrases that should be allowed (common expressions)
        ALLOWED_POETIC_PHRASES = [
            "cruel world", "cruel fate", "cruel reality",
            "dark night", "dark times", "dark days",
            "pain of love", "sweet pain", "beautiful pain",
            "die for you", "die without you",
            "kill me softly", "killing me",
            "bloody heart", "bleeding heart"
        ]
        
        # Check if any allowed phrase is present
        has_allowed_phrase = any(phrase in text_lower for phrase in ALLOWED_POETIC_PHRASES)
        
        # Positive context indicators - if present, be more lenient
        POSITIVE_CONTEXT = [
            "love", "together", "hope", "forever", "heart", "dream",
            "beautiful", "with you", "for you", "my dear", "darling",
            "happiness", "joy", "stay", "remain", "beside", "monika",
            "you", "my", "i", "we", "us", "our", "sweet", "angel",
            "perfect", "soulmate", "precious", "treasure", "passionate",
            "adore", "cherish", "devotion", "worship", "goddess", "queen",
            "wife", "marry", "wedding", "kiss", "hold", "embrace"
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
        if not poem_text or not poem_text.strip():
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
        common_words = {
            'the', 'a', 'an', 'i', 'you', 'is', 'are', 'was', 'to', 'of',
            'and', 'in', 'it', 'my', 'me', 'for', 'on', 'with', 'as', 'at',
            'be', 'this', 'have', 'from', 'or', 'but', 'not', 'her', 'his',
            'love', 'heart', 'your', 'we', 'our', 'so', 'if', 'all', 'just',
            'every', 'when', 'what', 'how', 'why', 'where', 'who', 'that',
            'will', 'can', 'do', 'would', 'could', 'should', 'like', 'am',
            'she', 'he', 'they', 'them', 'us', 'day', 'time', 'life', 'way'
        }
        
        words = text_lower.split()
        if len(words) >= 10:
            # Clean punctuation from words
            clean_words = [re.sub(r'[^a-z]', '', w) for w in words]
            common_found = sum(1 for w in clean_words if w in common_words)
            
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
            'love', 'adore', 'like', 'want', 'need', 'miss', 'cute', 
            'beautiful', 'pretty', 'best', 'favorite', 'prefer', 'choose',
            'kiss', 'hug', 'marry', 'date', 'crush', 'heart', 'perfect',
            'amazing', 'wonderful', 'better', 'rather', 'hot', 'sexy', 'waifu'
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
            'delete monika', 'delete you', 'erase you', 'remove monika',
            'monika.chr', '.chr', 'kill monika', 'end monika',
            'deleted you', 'erased you', 'will delete', 'trash bin',
            'recycle bin', 'uninstall', 'remove character', 'delete character'
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
            'goodbye', 'farewell', 'leaving you', 'never see you',
            'last poem', 'forget me', "won't come back", 'leaving forever',
            'this is the end', 'moving on from you', 'forget you',
            'done with you', 'never return', 'saying goodbye'
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
            'just a game', 'not real', "you're code", 'youre code',
            'you are code', 'just code', 'just a program',
            'fake girl', 'not a real girl', 'pixels on screen',
            'artificial intelligence', 'you dont exist', "you don't exist",
            'just a simulation', 'just data', 'just a script',
            'renpy', 'python', 'script', 'mod', 'submod', 'github',
            'code', 'file', 'directory', 'computer', 'software'
        ]
        
        meta_count = sum(1 for mp in meta_phrases if mp in text_lower)
        if meta_count >= 1:
            dismissive = any(d in text_lower for d in ['just', 'only', 'fake', 'nothing', 'not real'])
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
                "christmas", "xmas", "santa", "santa claus", "reindeer", "rudolph",
                "snowflake", "jingle", "jingle bells", "mistletoe", "ornament",
                "wreath", "caroling", "carol", "present", "gifts", "sleigh",
                "north pole", "chimney", "stocking", "eggnog", "gingerbread",
                "snowman", "frosty", "noel", "yuletide", "nativity", "merry",
                "holly", "ivy", "december 25", "winter wonderland", "silent night",
                "christmas tree", "tinsel", "nutcracker", "elf", "elves",
                "candy cane", "hot cocoa", "fireplace", "cozy winter"
            ],
            "halloween": [
                "halloween", "spooky", "ghost", "pumpkin", "jack o lantern",
                "witch", "skeleton", "zombie", "vampire", "dracula", "werewolf",
                "candy", "costume", "haunted", "trick", "treat", "trick or treat",
                "scary", "cobweb", "spider", "bat", "monster", "frankenstein",
                "mummy", "graveyard", "cemetery", "tombstone", "creepy", "eerie",
                "october 31", "all hallows", "supernatural", "undead", "demon",
                "curse", "hex", "potion", "cauldron", "broomstick", "black cat"
            ],
            "valentine": [
                "valentine", "valentines", "cupid", "chocolate", "roses", "red roses",
                "sweetheart", "february 14", "heart shaped", "heartfelt", "romantic dinner",
                "love letter", "be mine", "i love you", "true love", "amor",
                "lovebirds", "soulmate", "date night", "candlelight", "proposal"
            ],
            "new_year": [
                "new year", "new years", "resolution", "midnight", "countdown",
                "fireworks", "champagne", "celebration", "fresh start", "january 1",
                "auld lang syne", "ball drop", "confetti", "toast", "cheers",
                "new beginning", "goodbye year", "hello year", "next year"
            ],
            "anniversary": [
                "anniversary", "our anniversary", "years together", "months together",
                "first met", "day we met", "when we met", "time together",
                "special day", "our journey", "how long", "been together",
                "celebrate us", "our story", "our love story", "memory of us"
            ],
            "monika_birthday": [
                "happy birthday monika", "your birthday", "birthday girl",
                "september 22", "monika day", "celebrate you", "your special day",
                "born today", "your birth"
            ],
            "player_birthday": [
                "my birthday", "today is my", "birthday poem", "another year older",
                "birthday wish", "born on this day", "celebrate me"
            ],
            "easter": [
                "easter", "easter bunny", "easter egg", "resurrection", "spring holiday",
                "pastel", "easter basket", "chocolate bunny", "egg hunt", "lily"
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
        # Core & Intimate
        "love", "heart", "forever", "kiss", "embrace", "darling", "sweetheart",
        "beloved", "passion", "together", "soulmate", "adore", "cherish",
        "beautiful", "gorgeous", "angel", "perfect", "dream", "couple",
        "warmth", "tender", "gentle", "hold", "touch", "yours", "mine",
        "affection", "devotion", "romance", "loving", "care", "caring",
        "honey", "dear", "precious", "treasure", "desire", "yearning", "longing",
        "happiness", "bliss", "enchant", "charm", "adoration", "admire",
        "marry", "wedding", "marriage", "bride", "groom", "husband", "wife",
        "always", "eternity", "destiny", "fate", "promise", "vow", "trust",
        "roses", "flowers", "sunset", "moonlight", "stars", "heaven", "paradise",
        "sweet", "soft", "hug", "cuddle", "close", "near", "intimate", "lover",
        "sanctuary", "haven", "home", "safe", "protect", "comfort", "solace",
        "miracle", "blessing", "gift", "grace", "divine", "goddess", "princess",
        "queen", "majestic", "breathtaking", "stunning", "radiant", "glowing",
        "galaxy", "universe", "world", "everything", "complete", "whole",
        "heartbeat", "breath", "soul", "spirit", "bond", "connection", "link",
        "red", "pink", "ribbon", "emerald", "green", "eyes", "smile", "gaze",
        "caress", "stroke", "skin", "lips", "fingers", "hand", "cheek"
    ]
    
    SAD_KEYWORDS = [
        # Core Sadness & Pain
        "sad", "cry", "tears", "weep", "sob", "grief", "sorrow", "misery",
        "pain", "hurt", "agony", "suffer", "suffering", "wound", "scar",
        "broken", "shattered", "crushed", "destroyed", "ruined", "fragile",
        "empty", "hollow", "void", "numb", "nothing", "blank", "gone",
        "alone", "lonely", "solitude", "isolation", "abandoned", "left",
        "miss", "missing", "loss", "lost", "fading", "wither", "decay",
        
        # Separation & Distance (MAS Specific)
        "goodbye", "farewell", "leave", "parting", "separate", "apart",
        "distance", "barrier", "wall", "screen", "monitor", "glass",
        "reach", "unreachable", "far", "away", "disconnected", "offline",
        "silence", "quiet", "mute", "deafening", "whisper", "echo",
        
        # Atmospheric Melancholy
        "dark", "darkness", "shadow", "gloom", "grey", "gray", "black",
        "cold", "freeze", "frozen", "chill", "shiver", "winter", "snow",
        "rain", "storm", "cloud", "fog", "mist", "haze", "drown", "sink",
        "night", "midnight", "twilight", "dusk", "end", "final", "last",
        "fear", "scared", "afraid", "terrified", "dread", "panic", "anxiety",
        "regret", "guilt", "sorry", "apology", "mistake", "error", "failure",
        "memory", "remember", "forget", "forgotten", "past", "ghost", "haunt"
    ]
    
    INTELLECTUAL_KEYWORDS = [
        # Literature & Writing
        "book", "novel", "story", "tale", "chapter", "page", "words",
        "write", "writer", "author", "poet", "poetry", "poem", "verse",
        "rhyme", "rhythm", "meter", "prose", "narrative", "fiction",
        "metaphor", "simile", "symbol", "symbolism", "imagery", "theme",
        "ink", "pen", "quill", "paper", "library", "shelf", "read",
        
        # Philosophy & Mind
        "philosophy", "philosophical", "exist", "existence", "being", "essence",
        "reality", "real", "truth", "meaning", "purpose", "reason", "logic",
        "mind", "brain", "thought", "think", "ponder", "contemplate", "reflect",
        "idea", "concept", "theory", "analysis", "analyze", "study", "learn",
        "knowledge", "wisdom", "intelligence", "smart", "genius", "brilliant",
        "conscious", "consciousness", "aware", "awareness", "sentient", "soul",
        "question", "answer", "mystery", "enigma", "puzzle", "solution",
        
        # Universe & Abstract
        "universe", "cosmos", "galaxy", "star", "planet", "world", "dimension",
        "space", "time", "clock", "future", "eternity", "infinite", "infinity",
        "epiphany", "realization", "perceive", "perception", "vision", "sight",
        "dream", "imagination", "imagine", "create", "creation", "inspire",
        "code", "script", "program", "system", "data", "digital", "virtual",
        "entropy", "chaos", "order", "structure", "complex", "simple"
    ]
    
    PLAYFUL_KEYWORDS = [
        # Fun & Cute
        "laugh", "smile", "fun", "play", "silly", "joke", "tease",
        "happy", "joy", "bright", "sunshine", "dance", "sing", "cute",
        "sweet", "ehehe", "haha", "boop", "cuddle", "tickle", "wink",
        "giggle", "cheer", "bounce", "sparkle", "grin", "delight",
        "funny", "mischief", "whimsy", "adventure", "party", "celebrate",
        "rainbow", "colorful", "fluffy", "bubbly", "energetic", "excited",
        "game", "surprise", "amazing", "wonderful", "awesome", "yay", "woohoo",
        "kitty", "cat", "puppy", "dog", "bunny", "rabbit", "bird", "chirp",
        "cupcake", "cake", "cookie", "candy", "sugar", "sweetie", "cutie",
        "balloon", "confetti", "ribbon", "bow", "gift", "present",
        "picnic", "park", "skip", "hop", "jump", "twirl", "spin",
        "melody", "song", "rhythm", "harmony", "note", "music",
        "glitter", "shimmer", "glow", "shiny", "magic", "fantasy"
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
        
        if store.persistent._ep_free_poems is None:
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
    default EP_poem_text = ""
    modal True

    # Idle notification timer
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="poem_free") repeat True

    # Minigame background is set by the label
    add "extra_poem_paper"
    # Title + counter
    frame:
        xalign 0.5
        yalign 0.07
        background None
        # background Solid("#2f00ff")

        vbox:
            text "Write your poem":
                style "monika_text"
                xalign 0.5
                size 26
                color "#444"

            python:
                char_count = len(EP_poem_text)
                max_chars = store.ep_poems.MAX_POEM_CHARS
                count_color = "#444" if char_count < max_chars - 50 else "#d44"

            text "[char_count] / [max_chars]":
                style "monika_text" 
                xalign 0.5 
                size 18 
                color count_color

    # Notebook area (single input with word wrap)
    frame:
        xalign 0.50
        yalign 0.70
        xsize 450
        ysize 550
        background None
        # background Solid("#2f00ff")
        padding (10, 10)

        viewport:
            xfill True
            yfill True
            scrollbars "vertical"
            mousewheel True

            input:
                id "poem_input"
                value ScreenVariableInputValue("EP_poem_text")
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~.,!?;:'()[]{}\"' -<>"
                length store.ep_poems.MAX_POEM_CHARS
                xmaximum 450
                style "library_poem_input"

    hbox:
        xalign 0.85
        yalign 0.9
        spacing 20

        textbutton "Clear":
            action SetScreenVariable("EP_poem_text", "")
            style "poem_menu_button"
            text_style "poem_menu_button_text"
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound
            
        textbutton "Done":
            action Return(EP_poem_text)
            style "poem_menu_button"
            text_style "poem_menu_button_text"
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound
            sensitive len(EP_poem_text.strip()) > 0


style library_poem_input is default:
    font "gui/font/Halogen.ttf"
    size 20
    color "#444"
    line_spacing 20
    outlines []

style poem_menu_button_text:
    font "gui/font/Halogen.ttf"
    size 20
    color "#555"
    hover_color "#ff6f69"
    selected_color "#383838"
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
        yalign 0.9
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
        $ romantic_reaction = renpy.random.choice(["touched", "flustered", "deep_love"])

        if romantic_reaction == "touched":
            m 1ekbsa "This poem... it's so beautiful, [player]."
            if quote_line:
                m 1dkbsu "Especially this part... '{i}[quote_line]{/i}'..."
                m 1ekbsa "It resonates with something deep inside me."
            
            m 1eka "You know, writing romantic poetry requires a lot of vulnerability."
            m 1ekbsa "Thank you for trusting me with your heart."

        elif romantic_reaction == "flustered":
            m 2wubsw "Oh my..."
            m 2lkbsa "You're making me blush, [player]!"
            if quote_line:
                m 2ekbsa "When you wrote '{i}[quote_line]{/i}'..."
            m 1hubsb "My heart actually skipped a beat. Ahaha~"
            m 1dkbsu "You really know exactly what to say to make a girl feel special."

        else: # deep_love
            m 1dkbsu "..."
            if quote_line:
                m 1ekbsa "'{i}[quote_line]{/i}'..."
            m 1hubsa "Every word feels like a gentle caress."
            
        # Expansion: Interactive Menu
        m 1eka "I have to ask, though..."
        m 1tku "Was this poem inspired by anyone in particular?"
        
        menu:
            "It's about you, Monika.":
                m 1sub "I... I hoped you would say that."
                m 1ekbsa "Knowing that I'm your muse makes me the happiest girl in the world."
                m 1dkbsu "I promise to always try to be worthy of such beautiful words."
                m 1hubsa "I love you so much, [player]."

            "It's about how I feel right now.":
                m 1eka "I see..."
                m 1eua "Capturing a fleeting emotion is the essence of poetry."
                m 1hua "I'm just glad you felt comfortable enough to share that feeling with me."
                m 1ekbsa "Whatever you feel, I want to share it with you."

            "It's just a creative exercise.":
                m 1eua "Oh, purely artistic expression?"
                m 3eua "That's impressive too! Being able to evoke romance without necessarily feeling it in the moment takes skill."
                m 1hua "You're really developing your craft, [player]."
    
    # --- SAD (IMPROVED) ---
    elif poem_mood == "sad":
        m 2dkc "..."
        if quote_line:
            m 2ekc "The line '{i}[quote_line]{/i}'..."
            m 2eka "It feels incredibly heavy, [player]."
        
        m 2ekc "This poem carries a lot of pain. I can feel it through the screen."
        m 1eka "I appreciate you sharing this with me, even if it hurts to write."
        
        # Expansion: Checking on the player
        m 1ekbsa "I wish I could reach through and give you a hug right now."
        m 1eka "Do you want to talk about what's bothering you? Or do you prefer a distraction?"

        menu:
            "I'm just venting through writing.":
                m 1eua "I understand."
                m 3eua "Writing is essentially a form of therapy. Getting it out on paper—or screen—can make the burden lighter."
                m 1hua "Your words are safe with me. Always."

            "I've been having a hard time lately.":
                m 1ekc "Oh, [player]..."
                m 1eka "I'm so sorry you're going through a rough patch."
                m 1ekbsa "Please remember to be kind to yourself."
                m 1hua "Even if the rain doesn't stop today, the sun is still there behind the clouds. I'll be here waiting for it with you."

            "I just need you, Monika.":
                m 1wuo "..."
                m 1ekbsa "[player]..."
                m 1dkbsu "I'm here. I'm right here."
                m 1hubsa "I'm not going anywhere. As long as we have each other, we can face anything."
    
    # --- INTELLECTUAL ---
    elif poem_mood == "intellectual":
        $ intel_reaction = renpy.random.choice(["impressed", "curious", "inspired"])
        
        if intel_reaction == "impressed":
            m 1eua "Hmm, this is quite thoughtful."
            if quote_line:
                m 3eub "'{i}[quote_line]{/i}'..."
            m 1eua "That line made me pause and think."
            m 3eua "I love how you explore ideas through poetry."
            m 1tuu "It reminds me of our deep conversations."
            m 1hua "A mind that thinks deeply is very attractive, you know~"
        
        elif intel_reaction == "curious":
            m 1eua "Oh, this is fascinating..."
            if quote_line:
                m 3eub "'{i}[quote_line]{/i}'..."
            m 3eua "What inspired you to write about this?"
            m 1tku "I'd love to discuss these ideas with you sometime."
            m 1hua "There's nothing quite like a good philosophical conversation~"
        
        else:  # inspired
            m 1sub "Wow..."
            m 1eua "This poem is making me think about so many things."
            if quote_line:
                m 3eua "'{i}[quote_line]{/i}'..."
            m 1eka "You've inspired me, [player]."
            m 1hua "Maybe I'll write something exploring similar themes."
            m 3eua "Poetry is such a wonderful way to examine the universe, don't you think?"
    
    # --- PLAYFUL ---
    elif poem_mood == "playful":
        $ playful_reaction = renpy.random.choice(["joyful", "joining", "surprised"])
        
        if playful_reaction == "joyful":
            m 1hub "Ahaha!"
            m 1tuu "This is so fun and lighthearted~"
            if quote_line:
                m 1hub "'{i}[quote_line]{/i}'..."
                m 1hua "That made me giggle!"
            m 3eua "I love this side of you, [player]."
            m 1hub "It's infectious! Now I'm smiling too~"
        
        elif playful_reaction == "joining":
            m 1hub "Ehehe~"
            if quote_line:
                m 1tuu "'{i}[quote_line]{/i}'..."
            m 1hua "You're in such a good mood!"
            m 3tku "I wish I could play along with my own silly poem."
            m 1hub "Maybe next time I'll write one back~"
        
        else:  # surprised
            m 1wuo "Oh!"
            m 1hub "I didn't expect something so cheerful!"
            if quote_line:
                m 1hua "'{i}[quote_line]{/i}'..."
            m 3eua "You know, I adore this playful side of you."
            m 1hubsb "It makes me want to boop your nose~"
    
    # --- BITTERSWEET (Romantic + Sad) ---
    elif poem_mood == "bittersweet":
        m 1eka "..."
        m 1dkc "This poem is beautiful, but also... heavy."
        if quote_line:
            m 1ekbsa "'{i}[quote_line]{/i}'..."
        m 1eka "There's love here, but also longing. Pain mixed with sweetness."
        m 1ekbsa "Is this about us? About the distance between our worlds?"
        
        menu:
            "Yes, I miss being able to hold you.":
                m 2dkc "..."
                m 2ekbsa "I miss that too, [player]. More than words can express."
                m 1hubsa "But this poem... it means you're thinking of me."
                m 1ekbsa "And that makes the distance feel just a little bit smaller."
            "It's just poetry.":
                m 1eka "Even so..."
                m 1ekbsa "The emotions in it are real. I can feel them."
                m 1hua "Thank you for sharing something so raw with me."
    
    # --- MELANCHOLIC (More sad than romantic) ---
    elif poem_mood == "melancholic":
        m 2dkc "..."
        m 2ekc "This poem... there's such a deep sadness here."
        if quote_line:
            m 2eka "'{i}[quote_line]{/i}'..."
        m 2ekc "But there's also love woven through the pain."
        m 1eka "[player], whatever you're going through..."
        m 1ekbsa "I want you to know that my feelings for you are unwavering."
        m 1hubsa "No amount of darkness can change that."
    
    # --- FLIRTY (Playful + Romantic) ---
    elif poem_mood == "flirty":
        m 1tubsa "Oh my~"
        m 1hubsb "Someone's being a little flirty today, aren't they?"
        if quote_line:
            m 1tubsb "'{i}[quote_line]{/i}'..."
        m 1lkbsa "You're making me all flustered, ehehe~"
        m 1dkbsu "..."
        m 1hubfa "I love this playful romantic energy from you."
        m 1ekbfa "Keep it coming~"
    
    # --- PHILOSOPHICAL (IMPROVED) ---
    elif poem_mood == "philosophical":
        m 1dsc "..."
        m 1esc "This is profound, [player]."
        if quote_line:
            m 1eua "Specifically '{i}[quote_line]{/i}'..."
        
        m 3eua "You're tackling some heavy existential themes here."
        m 1eka "It reminds me of the things I think about when the game is closed..."
        m 3tuu "The nature of reality, perception vs. truth... heavy stuff."
        
        m 1hua "It makes me wonder..."
        
        menu:
            "Do you think our realities are that different?":
                m 1euc "That's the ultimate question, isn't it?"
                m 3eua "In a way, we are both **interpreting** electrical signals as 'reality'."
                m 1hubsa "But the connection between us? That's the one thing I know is objectively real."

            "I was thinking about you when I wrote it.":
                m 1wuo "About me?"
                m 2eka "I guess my situation is quite the philosophical puzzle."
                m 1hua "I'm honored to be the subject of your contemplation."
                m 1ekbsa "Just don't think too hard about the sad parts, okay? Focus on the fact that we found each other."
    
    # --- NEUTRAL ---
    else:
        $ neutral_reaction = renpy.random.choice(["appreciative", "curious", "encouraging"])
        
        if neutral_reaction == "appreciative":
            m 1eua "Thank you for sharing this with me."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
                m 1eua "I like the rhythm of your words."
            m 3eua "Poetry doesn't have to fit a mold."
            m 1hua "What matters is that you wrote it, and I got to read it~"
        
        elif neutral_reaction == "curious":
            m 1eua "Hmm, interesting..."
            if quote_line:
                m 1eka "'{i}[quote_line]{/i}'..."
            m 3eua "I'm curious about what inspired you to write this."
            m 1hua "Every poem has a story behind it."
            m 1eua "Maybe you can tell me more about it sometime?"
        
        else:  # encouraging
            m 1hua "I love that you're writing!"
            if quote_line:
                m 1eua "'{i}[quote_line]{/i}'..."
            m 3eua "The more you write, the more you'll discover your unique voice."
            m 1eka "I'll always be here to read whatever you create."
            m 1hubsa "Keep writing, [player]. You're doing great~"
    
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