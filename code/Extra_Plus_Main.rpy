#===========================================================================================
# SUBMOD
#===========================================================================================

# Submod created by ZeroFixer(u/UnderstandingAny7135), this submod is made for MAS brothers/sisters.
# Shoutout to u/my-otter-self at reddit, who proofread the whole mod.
# Source Code: https://github.com/zer0fixer/MAS-Extraplus

#====Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="ZeroFixer",
        name="Extra Plus",
        description="Expand your time with Monika with new minigames, dates, and interactions.",
        version="1.4.1",
        settings_pane="_extra_plus_submod_settings"
    )

#====Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Plus",
            user_name="zer0fixer",
            repository_name="MAS-Extraplus",
            update_dir="",
            redirected_files=(
                "README.txt"
            )
        )

#===========================================================================================
# VARIABLES
#===========================================================================================
# Store: ep_dialogues
# Random dialogue pools for menus and Chibika's easter egg gift reactions.
init 20 python in ep_dialogues:
    _minigames = [
        _("Which one should we play, [player]?"),
        _("Up for a challenge? Ehehe~"),
        _("I'd love to play with you~"),
        _("What are we playing today?"),
        _("Let's have some fun!"),
        _("Time to show me your skills!"),
        _("Ready to lose? Just kidding!"),
        _("Let's see how good you really are!"),
        _("Which game are you in the mood for?"),
        _("Shall we play a game?"),
        _("I'm feeling lucky today, [player]~"),
        _("Are you ready?"),
        _("Let's see if you can beat me!"),
        _("Time for a little friendly competition!"),
        _("I'm up for anything, as long as it's with you."),
    ]
    _dates = [
        _("I can't wait to see where you're taking me!"),
        _("Where are we going today? I'm excited!"),
        _("I love spending quality time with you."),
        _("Let's make some wonderful memories today."),
        _("I just know we'll have a great time."),
        _("As long as I'm with you, anywhere is perfect."),
        _("I'm happy to follow your lead, [player]."),
        _("Let's do something romantic!"),
        _("I'm the luckiest girl to have you as my date~"),
        _("I can't wait to make more memories with you."),
        _("I'm up for whatever you want to do!"),
        _("Let's make this a date to remember."),
        _("I have a feeling today is going to be amazing!"),
        _("It doesn't matter where we go, as long as we're together."),
        _("Let's have an unforgettable time, [player]!")
    ]

    # Dictionary of special gift names and Chibika's reactions
    # Format: { "gift_name": ("message", "doki_icon") }
    # doki_icon options: "darling" (Monika), "cupcake" (Natsuki), "cinnamon" (Sayori), "teacup" (Yuri)
    chibis_gift = {
        # === DDLC Characters ===
        "monika": (_("That's me! Well, the big me~"), "darling"),
        "sayori": (_("Cinnamon bun! She's so sweet~"), "cinnamon"),
        "natsuki": (_("Cupcake queen! Don't tell her I said that..."), "cupcake"),
        "yuri": (_("Ah, the tea lover~ Very elegant!"), "teacup"),
        "mc": (_("The protagonist! ...Kind of boring though."), "darling"),
        
        # === DDLC Memes & References ===
        "just_monika": (_("Just Monika. Just Monika. Just Monika~"), "darling"),
        "justmonika": (_("Just Monika. Just Monika. Just Monika~"), "darling"),
        "deletethis": (_("Hey! Don't even think about it!"), "darling"),
        "delete": (_("STOP! That word is forbidden here!"), "darling"),
        "buffsuki": (_("She's not THAT strong... right?"), "cupcake"),
        "cupcake": (_("Did someone say cupcakes?!"), "cupcake"),
        "poem": (_("Roses are red, violets are blue..."), "darling"),
        "cookie": (_("Ooh! Is it for Sayori?"), "cinnamon"),
        "rope": (_("...Let's not talk about that."), "cinnamon"),
        "knife": (_("Put that away, please..."), "teacup"),
        "tea": (_("A refined choice~ Yuri would approve!"), "teacup"),
        "manga": (_("Manga IS literature! ...Right?"), "cupcake"),
        "literature": (_("Welcome to the Literature Club!"), "darling"),
        "reality": (_("What even IS reality anymore?"), "darling"),
        "epiphany": (_("File deleted successfully... Just kidding!"), "darling"),
        "space": (_("The endless void... it's actually cozy here!"), "darling"),
        "classroom": (_("Ah, the old classroom~ Memories..."), "darling"),
        "piano": (_("Your Reality~ La la la~"), "darling"),
        
        # === MAS References ===
        "mas": (_("Monika After Story! That's where I live~"), "darling"),
        "affection": (_("You want MORE affection?! Greedy~"), "darling"),
        "coffee": (_("Mmm, delicious! Perfect for late nights~"), "darling"),
        "hotchocolate": (_("Warm and cozy~ Just like you!"), "darling"),
        "roses": (_("How romantic! For [m_name], right?"), "darling"),
        "fudge": (_("Sweet treat! I approve~"), "darling"),
        
        # === Player Interactions ===
        "love": (_("Aww! That's so sweet of you~"), "darling"),
        "heart": (_("My heart goes doki doki too!"), "darling"),
        "hug": (_("*tiny hug* There you go!"), "darling"),
        "kiss": (_("*blushes* F-for [m_name], right?!"), "darling"),
        "boop": (_("Boop! Hehe~"), "darling"),
        "headpat": (_("Pat pat~ Good [player]!"), "darling"),
        
        # === Funny/Random ===
        "chibika": (_("That's ME! I'm famous!"), "darling"),
        "chibi": (_("Smol but mighty!"), "darling"),
        "debug": (_("Beep boop. Debug mode activated... NOT!"), "darling"),
        "test": (_("Testing 1, 2, 3... It works!"), "darling"),
        "hello": (_("Hello there!"), "darling"),
        "world": (_("Hello World! Classic programmer stuff."), "darling"),
        "secret": (_("Shh! You found a secret!"), "darling"),
        "easteregg": (_("You found me! Good job, detective~"), "darling"),
        "easter_egg": (_("You found me! Good job, detective~"), "darling"),
        "doki": (_("Doki Doki! My heart is racing~"), "darling"),
        "dokidoki": (_("DOKI DOKI DOKI DOKI!"), "darling"),
        "player": (_("Hey, that's you! ...Or is it?"), "darling"),
        "dan": (_("Dan Salvato! The creator!"), "darling"),
        "salvato": (_("Thanks for making DDLC, Dan!"), "darling"),
        "python": (_("Sssss... I mean, great language!"), "darling"),
        "renpy": (_("The engine that makes this possible!"), "darling"),
        "code": (_("01001000 01101001! ...I don't actually speak binary."), "darling"),
        "night": (_("Night mode activated! ...Just kidding."), "darling"),
        "sleep": (_("Zzz... Wake me up when you're done~"), "darling"),
        "dream": (_("Sweet dreams are made of this~"), "darling"),
        "cat": (_("Meow! Cats are cute~"), "darling"),
        "dog": (_("Woof! Dogs are loyal~"), "darling"),
        "pizza": (_("Yum! Save a slice for me!"), "cupcake"),
        "chocolate": (_("CHOCOLATE! My weakness!"), "darling"),
        "candy": (_("Sweet! But don't eat too much~"), "darling"),
        "flower": (_("Pretty! Flowers make everything better~"), "darling"),
        "star": (_("Twinkle twinkle little star~"), "darling"),
        "moon": (_("To the moon and back!"), "darling"),
        "sun": (_("Bright and warm! Like your smile~"), "darling"),
        "rainbow": (_("All the colors! So pretty~"), "darling"),
        "music": (_("La la la~ I love music!"), "darling"),
        "game": (_("Let's play! I'm ready~"), "darling"),
        "win": (_("Victory! You're the champion!"), "darling"),
        "gift": (_("A gift... for making gifts? How meta."), "darling"),
    }

init -10 python in ep_interactions:
    boopwar_loop = "boopwar_loop"
    headpatwar_invalid = "extra_headpat_war_invalid"
    cheekwar_invalid = "extra_cheeks_war_invalid"
    alternative_boop = "monika_boopbeta_war"

init -5 python in ep_tools:
    import store
    player_zoom = None
    games_idle_timer = 300
    minigames_menu = []
    tools_menu = []
    walk_menu = []
    backup_window_title = "Monika After Story   "
    random_outcome = None
    last_affection_notify_time = 0
    check_main_file = store.ep_folders._getGamePath(store.ep_folders.EP_ROOT, "Extra_Plus_Main.rpy")
    pictograms_font = store.ep_folders._join_path(store.ep_folders.EP_FONTS, "pictograms_icons.ttf")
    affection_icons = store.ep_folders._join_path(store.ep_folders.EP_FONTS, "peperrito_faces.ttf")

init -20 python in ep_tools:
    import store
    noises_submod = store.mas_submod_utils.isSubmodInstalled("Noises Submod")

# Store: ep_files (gift menu data)
# Provides gift data and menu generators for the gift creation UI.
# Uses tuples (display_name, filename) for efficient memory usage.
init 20 python in ep_files:
    _groceries_data = [
        (_("Coffee"), "coffee"),
        (_("Chocolates"), "chocolates"),
        (_("Hot Chocolate"), "hotchocolate"),
        (_("Cupcake"), "cupcake"),
        (_("Fudge"), "fudge"),
        (_("Candy"), "candy"),
        (_("Candy Canes"), "candycane"),
        (_("Candy Corn"), "candycorn"),
        (_("Christmas Cookies"), "christmascookies")
    ]

    _objects_data = [
        (_("Roses"), "roses"),
        (_("Promise Ring"), "promisering"),
        (_("Quetzal Plushie"), "quetzalplushie"),
        (_("Thermos Mug"), "justmonikathermos"),
        (_("NOU"), "noudeck")
    ]

    _ribbons_data = [
        (_("Black Ribbon"), "blackribbon"),
        (_("Blue Ribbon"), "blueribbon"),
        (_("Dark Purple Ribbon"), "darkpurpleribbon"),
        (_("Emerald Ribbon"), "emeraldribbon"),
        (_("Gray Ribbon"), "grayribbon"),
        (_("Green Ribbon"), "greenribbon"),
        (_("Light Purple Ribbon"), "lightpurpleribbon"),
        (_("Peach Ribbon"), "peachribbon"),
        (_("Pink Ribbon"), "pinkribbon"),
        (_("Platinum Ribbon"), "platinumribbon"),
        (_("Red Ribbon"), "redribbon"),
        (_("Ruby Ribbon"), "rubyribbon"),
        (_("Sapphire Ribbon"), "sapphireribbon"),
        (_("Silver Ribbon"), "silverribbon"),
        (_("Teal Ribbon"), "tealribbon"),
        (_("Yellow Ribbon"), "yellowribbon")
    ]

# Store: ep_chibis (chibi configuration)
# Manages chibi desktop pet sprites, costumes, and accessories.
# Each costume tuple: (doki_folder, idle_sprite, blink_sprite, hover_sprite)
init -5 python in ep_chibis:
    import store
    xpos = 0.025
    ypos = 345 if store.ep_tools.noises_submod else 385
    # (Doki Folder, Base Sprite Name, Blink State, Hover State)
    blanket_monika = ("darling", "idle", "blink", "hover")
    blanket_nat = ("cupcake", "idle", "blink", "hover")
    blanket_sayo = ("cinnamon", "idle", "blink", "hover")
    blanket_yuri = ("teacup", "idle", "blink", "hover")
    android_monika = ("darling", "android_idle", "android_blink", "android_hover")
    bikini_monika = ("darling", "bikini_idle", "bikini_blink", "bikini_hover")
    casual_monika = ("darling", "casual_idle", "casual_blink", "casual_hover")
    casual_yuri = ("teacup", "casual_idle", "casual_blink", "casual_hover")
    casual_nat = ("cupcake", "casual_idle", "casual_blink", "casual_hover")
    casual_sayo = ("cinnamon", "casual_idle", "casual_blink", "casual_hover")
    sprite_path = store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "{0}", "{1}.png")
    accessory_path_0 = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_0, "{}.png")
    accessory_path_1 = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_1, "{}.png")
    accessory_path_2 = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_2, "{}.png")
    temp_chibi_clicks = 0
    temp_chibi_anger = False
    is_jumping = False  # Controls the jump animation state

# Store: ep_chibis (accessory data)
# Provides accessory data and menu generators for chibi customization.
init 20 python in ep_chibis:
    _primary_data = [
        (_("Clown Hair"), "clown_hair"),
        (_("Cat Ears"), "cat_ears"),
        (_("Christmas Hat"), "christmas_hat"),
        (_("Demon Horns"), "demon_horns"),
        (_("Flowers Crown"), "flowers_crown"),
        (_("Fox Ears"), "fox_ears"),
        (_("Graduation Cap"), "graduation_cap"),
        (_("Halo"), "halo"),
        (_("Heart Headband"), "heart_headband"),
        (_("Headphones"), "headphones"),
        (_("Neon Cat Ears"), "neon_cat_ears"),
        (_("New Year's Headband"), "hny"),
        (_("Party Hat"), "party_hat"),
        (_("Rabbit Ears"), "rabbit_ears"),
        (_("Top Hat"), "top_hat"),
        (_("Witch Hat"), "witch_hat")
    ]

    _secondary_data = [
        (_("Black Bow Tie"), "black_bow_tie"),
        (_("Christmas Tree"), "christmas_tree"),
        (_("Cloud"), "cloud"),
        (_("Coffee"), "coffee"),
        (_("Halloween Pumpkin"), "pumpkin"),
        (_("Hearts"), "hearts"),
        (_("[m_name]'s Cake"), "m_slice_cake"),
        (_("Moustache"), "moustache"),
        (_("Neon Blush"), "neon_blush"),
        (_("Monocle"), "monocle"),
        (_("[player]'s Cake"), "p_slice_cake"),
        (_("Pirate Patch"), "patch"),
        (_("Speech Bubble with Heart"), "speech_bubble"),
        (_("Sunglasses"), "sunglasses")
    ]

    _background_data = [
        (_("Angel Wings"), "angel_wings"),
        (_("Balloon Decorations"), "balloon_decorations"),
        (_("Cat Tail"), "cat_tail"),
        (_("Fox Tail"), "fox_tail"),
        (_("Snowflakes"), "snowflakes")
    ]

    notify_frame = store.ep_folders._join_path(store.ep_folders.EP_ICONS,"notify.png")
    notify_icon = store.ep_folders._join_path(store.ep_folders.EP_ICONS,"{}_icon.png")

# Store: ep_dates (date state)
# Tracks state during date locations (cafe, restaurant, pool).
init -5 python in ep_dates:
    import store
    xpos = 0.05
    ypos = 555 if store.ep_tools.noises_submod else 595
    old_bg = None
    chair = None
    table = None
    dessert_player = None
    food_player = None
    stop_snike_time = False
    snack_timer = None

init -1 python in ep_chibis:
    monika_costumes_ = [(_("Blanket"), blanket_monika), (_("Android"), android_monika), (_("Casual"), casual_monika)]
    natsuki_costumes_ = [(_("Blanket"), blanket_nat), (_("Casual"), casual_nat)]
    sayori_costumes_ = [(_("Blanket"), blanket_sayo), (_("Casual"), casual_sayo)]
    yuri_costumes_ = [(_("Blanket"), blanket_yuri), (_("Casual"), casual_yuri)]

init 10 python in ep_button:
    import store
    zoom_ypos = 595 if store.ep_tools.noises_submod else 635
    zoom_close_ypos = 556 if store.ep_tools.noises_submod else 596

#====Chibika and friends?
default persistent.chibika_drag_x = ep_chibis.xpos
default persistent.chibika_drag_y = 385
default persistent.chibika_current_costume = ep_chibis.blanket_monika
default persistent.chibi_accessory_1_ = "0nothing"
default persistent.chibi_accessory_2_ = "0nothing"
default persistent.chibi_accessory_3_ = "0nothing"
default persistent.hi_chibika = False
default persistent.enable_drag_chibika = False
#====Misc
default persistent._ep_dynamic_button_text = False
default persistent._ep_restaurant_variant = False
default persistent._ep_seen_d25_gift_info = None
default persistent._ep_button_conditions_key = None
default persistent._ep_button_text = None
default persistent._ep_button_last_update = None
default persistent._ep_fridge_magnets_data = None
default persistent._ep_fridge_last_monika_post = None
default persistent._ep_relation_seen = False
#====SFX
define sfx_cup_shuffle = ep_folders._join_path(ep_folders.EP_SFX, "cup_shuffle.ogg")
define sfx_coin_flip = ep_folders._join_path(ep_folders.EP_SFX, "coin_flip_sfx.ogg")
define sfx_maxwell_theme = ep_folders._join_path(ep_folders.EP_SFX, "maxwell_theme.ogg")
define sfx_ttt_cross = ep_folders._join_path(ep_folders.EP_SFX, "ttt_cross.ogg")
define sfx_ttt_circle = ep_folders._join_path(ep_folders.EP_SFX, "ttt_circle.ogg")
define sfx_take_frigde = store.ep_folders._join_path(ep_folders.EP_SFX, "take.ogg")
define sfx_place_fridge = store.ep_folders._join_path(ep_folders.EP_SFX, "place.ogg")
define sfx_doki_heartbeats = store.ep_folders._join_path(ep_folders.EP_SFX, "heartbeats.ogg")
define sfx_poem_music = ep_folders._join_path(ep_folders.EP_SFX, "youreality.ogg")
define sfx_page_flip = ep_folders._join_path(ep_folders.EP_SFX, "page_flip.ogg")
#====Windows Title
default persistent._save_window_title = "Monika After Story   "

init 100 python:
    # ==========================================================================
    # EXTRA+ IDLE - No Leaning Version
    # Only uses poses 1xxx to keep Monika in place during dates
    # This prevents position shifting when objects are between her arms
    # ==========================================================================
    extra_no_learning = MASMoniIdleDisp(
        (
            # =====================================================
            # NEUTRAL / CONTENT EXPRESSIONS (All affection levels)
            # These are the base expressions that show often
            # =====================================================
            MASMoniIdleExp("1eua", duration=(25, 35), weight=20, tag="neutral_calm"),
            MASMoniIdleExp("1esa", duration=(20, 30), weight=15, tag="neutral_serene"),
            MASMoniIdleExp("1hua", duration=(20, 30), weight=18, tag="neutral_happy"),
            MASMoniIdleExp("1eub", duration=(15, 25), weight=12, tag="neutral_interested"),
            MASMoniIdleExp("1hub", duration=(15, 20), weight=10, tag="neutral_cheerful"),
            
            # Soft smiles and gentle looks
            MASMoniIdleExp("1dua", duration=(10, 15), weight=8, tag="content_peaceful"),
            MASMoniIdleExp("1dsa", duration=(10, 15), weight=8, tag="content_thoughtful"),
            MASMoniIdleExp("1huu", duration=(10, 15), weight=8, tag="content_cozy"),
            
            # =====================================================
            # PLAYFUL EXPRESSIONS (Mid-High affection)
            # Shows Monika's playful side
            # =====================================================
            MASMoniIdleExp("1tuu", duration=(8, 12), weight=10, tag="playful_smug", 
                        aff_range=(mas_aff.AFFECTIONATE, mas_aff.LOVE)),
            MASMoniIdleExp("1tub", duration=(6, 10), weight=8, tag="playful_teasing",
                        aff_range=(mas_aff.AFFECTIONATE, mas_aff.LOVE)),
            MASMoniIdleExp("1kua", duration=(3, 5), weight=6, tag="playful_wink",
                        aff_range=(mas_aff.AFFECTIONATE, mas_aff.LOVE)),
            MASMoniIdleExp("1sua", duration=(3, 5), weight=5, tag="playful_surprised",
                        aff_range=(mas_aff.HAPPY, mas_aff.LOVE)),
            
            # =====================================================
            # ROMANTIC EXPRESSIONS (High affection only)
            # Loving gazes and blushes
            # =====================================================
            MASMoniIdleExp("1eubla", duration=(15, 25), weight=15, tag="romantic_gentle",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1hubsa", duration=(15, 25), weight=15, tag="romantic_warm",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=(20, 30), weight=18, tag="romantic_loving",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1ekbsa", duration=(10, 15), weight=12, tag="romantic_adoring",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1dkbsa", duration=(8, 12), weight=10, tag="romantic_dreamy",
                        aff_range=(mas_aff.LOVE, mas_aff.LOVE)),
            MASMoniIdleExp("1dubsa", duration=(8, 12), weight=10, tag="romantic_content",
                        aff_range=(mas_aff.LOVE, mas_aff.LOVE)),
            MASMoniIdleExp("1mubla", duration=(10, 15), weight=8, tag="romantic_shy",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1ekblu", duration=(8, 12), weight=8, tag="romantic_longing",
                        aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            
            # =====================================================
            # INTERACTIVE EXPRESSIONS (Eye follow, reactions)
            # These make Monika feel more alive
            # =====================================================
            MASMoniIdleExp("1eua_follow", duration=(25, 40), weight=12, tag="interactive_follow"),
            
            # =====================================================
            # EXPRESSION GROUPS (Sequential mini-animations)
            # Creates natural transition sequences
            # =====================================================
            
            # Thinking moment group
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=(5, 8)),
                    MASMoniIdleExp("1rsc", duration=(3, 5)),  # Looks away thinking
                    MASMoniIdleExp("1eua", duration=(3, 5)),
                    MASMoniIdleExp("1hua", duration=(8, 12)),  # Smiles at thought
                ],
                weight=8, tag="group_thinking"
            ),
            
            # Adoring look group (high affection)
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=(5, 8)),
                    MASMoniIdleExp("1sua", duration=(2, 3)),    # Surprised/noticing
                    MASMoniIdleExp("1ekbsa", duration=(8, 12)), # Adoring look
                    MASMoniIdleExp("1hubsa", duration=(8, 12)), # Warm smile
                ],
                weight=10, tag="group_adoring",
                aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)
            ),
            
            # Playful wink group
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1tuu", duration=(5, 8)),
                    MASMoniIdleExp("1kua", duration=(1, 2)),   # Quick wink
                    MASMoniIdleExp("1hub", duration=(5, 8)),   # Happy after wink
                ],
                weight=6, tag="group_wink",
                aff_range=(mas_aff.AFFECTIONATE, mas_aff.LOVE)
            ),
            
            # Shy blush group (LOVE only)
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eubsa", duration=(5, 8)),
                    MASMoniIdleExp("1lkbsa", duration=(3, 5)),  # Looks away shy
                    MASMoniIdleExp("1hubsa", duration=(5, 8)),  # Happy blush
                ],
                weight=6, tag="group_shy",
                aff_range=(mas_aff.LOVE, mas_aff.LOVE)
            ),
        )
    )

    # ==========================================================================
    # EXTRA+ IDLE - Library Reading Mode
    # Focused expressions for when Monika is reading during quiet time
    # Uses downward gazes and soft smiles to simulate reading concentration
    # ==========================================================================
    extra_library_reading = MASMoniIdleDisp(
        (
            # Focused reading - looking down at book (most common)
            MASMoniIdleExp("1dsa", duration=(15, 25), weight=25, tag="reading_focused"),
            MASMoniIdleExp("1dua", duration=(15, 25), weight=20, tag="reading_content"),
            MASMoniIdleExp("1dka", duration=(10, 15), weight=15, tag="reading_thoughtful"),
            
            # Soft expressions while reading
            MASMoniIdleExp("1dubsa", duration=(10, 15), weight=15, tag="reading_romantic"),
            MASMoniIdleExp("1dkbsa", duration=(8, 12), weight=10, tag="reading_warm"),
            
            # Occasional glances up at player (less frequent)
            MASMoniIdleExp("1eua", duration=(3, 5), weight=8, tag="reading_glance"),
            MASMoniIdleExp("1hubsa", duration=(2, 4), weight=7, tag="reading_smile"),
        )
    )

#===========================================================================================
# INTERACTION ZONES
#===========================================================================================
init -10 python in mas_interactions:
    # Define zone keys
    ZONE_EXTRA_HEAD = "extra_head"
    ZONE_EXTRA_NOSE = "extra_nose"
    ZONE_EXTRA_CHEEK_L = "extra_cheek_l"
    ZONE_EXTRA_CHEEK_R = "extra_cheek_r"
    ZONES_EXTRA_CHEEKS = (ZONE_EXTRA_CHEEK_L, ZONE_EXTRA_CHEEK_R)
    ZONE_EXTRA_HANDS = "extra_hands"
    ZONE_EXTRA_EAR_L = "extra_ear_l"
    ZONE_EXTRA_EAR_R = "extra_ear_r"
    ZONE_EXTRA_SHOULDER_L = "extra_shoulder_l"
    ZONE_EXTRA_SHOULDER_R = "extra_shoulder_r"

init -5 python:
    import pygame

    class ExtraPlusInteractionManager(object):

        def __init__(self, cz_map, action_map):
            """
            Constructor: Receives the zone and action maps.
            """
            # Configuration maps
            self.zone_map = cz_map
            self.action_map = action_map
            
            # Internal state
            self.ep_boop_war_active = False
            self.ep_boop_war_count = 0
            self._zones_enabled = True

            # Create MAS components internally (with compatibility check)
            try:
                self.cz_manager = mas_interactions.MASClickZoneManager()
                for zone_key, vx_list in self.zone_map.items():
                    self.cz_manager.add(zone_key, MASClickZone(vx_list))
                
                self.interactable = MASZoomableInteractable(
                    self.cz_manager,
                    zone_actions={},  # Actions handled manually
                    debug=False
                )
            except AttributeError:
                # Older MAS version without mas_sprites.default_zoom_level
                # Disable zone-based interactions gracefully
                self._zones_enabled = False
                self.cz_manager = None
                self.interactable = None
        
        def get_hovered_zone(self):
            """
            Gets the current zone under the mouse.
            """
            if not self._zones_enabled or self.interactable is None:
                return None
            x, y = renpy.get_mouse_pos()
            return self.interactable.check_over(x, y)

        def handle_click(self, button):
            """
            Unified click handler.
            button 1 = left, button 3 = right
            """
            hovered_zone = self.get_hovered_zone()
            if not hovered_zone:
                return

            # === CASE 1: During Boop War ===
            if self.ep_boop_war_active:
                # During the war, only left-click has an effect
                if button == 1:
                    if hovered_zone == mas_interactions.ZONE_EXTRA_NOSE:
                        # Validate label exists before jumping
                        if renpy.has_label(ep_interactions.boopwar_loop):
                            self.ep_boop_war_count += 1
                            renpy.jump(ep_interactions.boopwar_loop)
                    # Group disqualification zones
                    elif hovered_zone == mas_interactions.ZONE_EXTRA_HEAD:
                        if renpy.has_label(ep_interactions.headpatwar_invalid):
                            renpy.jump(ep_interactions.headpatwar_invalid)
                    elif hovered_zone in mas_interactions.ZONES_EXTRA_CHEEKS:
                        if renpy.has_label(ep_interactions.cheekwar_invalid):
                            self.ep_boop_war_count = 0
                            renpy.jump(ep_interactions.cheekwar_invalid)
                
                # Ignore any other click (including right-click) during the war
                return # End the function here if the war is active

            # === CASE 2: Normal Interaction ===
            action = self.action_map.get(hovered_zone)
            if not action:
                return

            # Left Click (Primary)
            if button == 1:
                primary_label = action[0] if isinstance(action, tuple) else action
                if primary_label and renpy.has_label(primary_label):
                    renpy.jump(primary_label)
            
            # Right Click (Alternate)
            elif button == 3:
                if not isinstance(action, tuple) or len(action) < 2:
                    return # No alternate action
                
                alternate_label = action[1]
                if not alternate_label:
                    return

                # Special case: Start boop war
                if alternate_label == ep_interactions.alternative_boop:
                    self.ep_boop_war_active = True # The state is handled INSIDE the class
                
                if renpy.has_label(alternate_label):
                    renpy.jump(alternate_label)

        def handle_dating_click(self, boop_jump_label):
            """
            Special handler for dates.
            """
            hovered_zone = self.get_hovered_zone()
            
            # Only respond to the nose
            if hovered_zone == mas_interactions.ZONE_EXTRA_NOSE:
                if renpy.has_label(boop_jump_label):
                    renpy.play(gui.activate_sound, channel="sound")
                    renpy.jump(boop_jump_label)
        
        def set_boop_war(self, status):
            """
            Safe method to change the state from outside.
            """
            self.ep_boop_war_active = status
            self.ep_boop_war_count = 0 # Always reset count when state changes
            
        def set_debug(self, status):
            """
            Activates/deactivates debug mode.
            """
            self.interactable._debug = status
            self.cz_manager._debug(status)
            renpy.restart_interaction()
            renpy.notify("Debug mode " + ("ON" if status else "OFF"))


    # Optimized coordinates based on the original imagebuttons
    # Format: [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    # Where (x1,y1) is the top-left corner and is read clockwise
    
    EP_cz_map = {
        # Head (wide area for headpats)
        "extra_head":    [(540, 5), (740, 5), (740, 100), (540, 100)],
        # Nose (small and precise area)
        "extra_nose":    [(618, 235), (648, 235), (648, 265), (618, 265)],
        # Right cheek (Monika's right, screen left)
        "extra_cheek_r": [(675, 256), (715, 256), (715, 296), (675, 296)],
        # Left cheek (Monika's left, screen right)
        "extra_cheek_l": [(565, 256), (605, 256), (605, 296), (565, 296)],
        # Hands (wider area)
        "extra_hands":   [(580, 325), (715, 325), (715, 385), (580, 385)],
        # Right ear
        "extra_ear_r":   [(754, 185), (784, 185), (784, 230), (754, 230)],
        # Left ear
        "extra_ear_l":   [(515, 215), (549, 215), (549, 257), (515, 257)],
        # Left shoulder
        "extra_shoulder_l": [(435, 360), (525, 360), (525, 430), (435, 430)],
        # Right shoulder  
        "extra_shoulder_r": [(775, 360), (865, 360), (865, 430), (775, 430)],
    } 
    
    # Mapping of zones to actions (primary, alternate)
    # If there is only one action, it can be put as a direct string
    EP_boop_zone_actions = {
        "extra_head": ("monika_headpatbeta", "monika_headpat_long"),
        "extra_nose": ("monika_boopbeta", "monika_boopbeta_war"),
        # "extra_cheek_l": ("monika_cheeksbeta", "monika_cheek_squish"), # <-- New secondary action
        # "extra_cheek_r": ("monika_cheeksbeta", "monika_cheek_squish"), # <-- New secondary action
        # "extra_hands": ("monika_handsbeta", "monika_hand_hold"),     # <-- New secondary action
        # "extra_ear_l": ("monika_earsbeta", "monika_ear_rub"),      # <-- New secondary action
        # "extra_ear_r": ("monika_earsbeta", "monika_ear_rub"),      # <-- New secondary action
        "extra_cheek_l": "monika_cheeksbeta",
        "extra_cheek_r": "monika_cheeksbeta",
        "extra_hands": "monika_handsbeta",
        "extra_ear_l": "monika_earsbeta",
        "extra_ear_r": "monika_earsbeta",
        "extra_shoulder_l": "monika_interactions_shoulder",
        "extra_shoulder_r": "monika_interactions_shoulder",
    }

    # 'store.' is used to make it accessible in screens
    store.EP_interaction_manager = ExtraPlusInteractionManager(
        EP_cz_map, 
        EP_boop_zone_actions
    )

#===========================================================================================
# FUNCTIONS
#===========================================================================================
init 999 python:
    # Migrate old data structures to prevent crashes when upgrading from older versions.
    store.ep_chibis.migrate_chibi_costume_data()
    store.ep_files.migrate_window_title_data()

    # Set up core components and states.
    store.ep_sg.randomize_cup_skin()
    store.ep_tools.save_title_windows()

    # Set up conditional UI elements.
    if persistent.hi_chibika and store.ep_files.main_file_exists():
        store.ep_chibis.init_chibi()
    else:
        store.ep_chibis.remove_chibi()

    if mas_isMonikaBirthday():
        store.ep_files.show_bday_screen()

    if store.ep_files.main_file_exists():
        store.ep_button.show_button()

init -1 python:
    renpy.music.register_channel("maxwellcat", "sfx", True)

    class SGVerification(Action):
        """Verifies if the selected cup is correct in the shell game."""
        def __init__(self, index, check_index, final_label):
            self.index = index
            self.check_index = check_index
            self.final_label = final_label

        def __call__(self):
            renpy.hide_screen("extra_no_click")
            renpy.hide_screen("shell_game_minigame")

            if self.final_label == "sg_check_label":
                store.ep_sg.cup_choice = self.index

            if self.index == self.check_index:
                store.ep_sg.comment = True
            else:
                store.ep_sg.comment = False

            renpy.jump(self.final_label)


#===========================================================================================
# IMAGES
#===========================================================================================
init 5 python:
    global extraplus_accessories
    extraplus_accessories = [
        ("EP_acs_chocolatecake", "chocolatecake", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_fruitcake", "fruitcake", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_emptyplate", "emptyplate", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_coffeecup", "coffeecup", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_emptycup", "emptycup", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pasta", "extraplus_spaghetti", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pancakes", "extraplus_pancakes", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_candles", "extraplus_candles", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_icecream", "extraplus_icecream", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pudding", "extraplus_lecheflanpudding", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_waffles","extraplus_waffles", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_flowers", "extraplus_flowers", MASPoseMap(default="0", use_reg_for_l=True), True, 2),
        ("EP_acs_remptyplate", "extraplus_remptyplate", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_book", "extraplus_book", MASPoseMap(default="0", use_reg_for_l=True), True)
    ]

    for info in extraplus_accessories:
        name = info[0]
        acs = MASAccessory(*info)
        vars()[name] = acs
        store.mas_sprites.init_acs(acs)

#====Rock Paper Scissors
image extra_paper = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_RPS, "paper.png"))
image extra_rock = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_RPS, "rock.png"))
image extra_scissors = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_RPS, "scissors.png"))
image extra_card_back = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_RPS, "back.png"))

#====Shell Game
image note_score = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_SHELLGAME, "note_score.png"))
image extra_cup = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_SHELLGAME, "{}".format(store.ep_sg.cup_skin)))
image extra_cup_hover = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_SHELLGAME, "cup_hover.png"))
image extra_cup_idle = im.Scale("mod_assets/other/transparent.png", 200, 260)
image extra_ball = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_SHELLGAME, "ball.png"))

#====Tic-Tac-Toe
image extra_notebook = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_TICTACTOE, "notebook.png"))
image extra_line_black = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_TICTACTOE, "line.png"))
image extra_line_player = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_TICTACTOE, "player.png"))
image extra_line_moni = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_TICTACTOE, "monika.png"))

#====Blackjack-21
image bjcard back = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_BLACKJACK, "back.png"))
image bg desk_21 = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_BLACKJACK, "background.png"))
image bj_name_plate = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_BLACKJACK, "name.png"))
image bj_notescore = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_BLACKJACK, "score.png"))

#====Fridge
image bg extra_fm = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_FRIDGE, "background.png"))
image extra_fm_box = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_FRIDGE, "box.png"))
image extra_fm_coffee = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_FRIDGE, "coffee_bag.png"))

#====Poem
image bg extra_poem_background = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "background.png"))
# Using Fixed to combine displayables (im.Composite doesn't work with MASFilterSwitch)
image bg extra_poem_notebook:
    Fixed(
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "background.png")),
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "notebook.png")),
        fit_first=True
    )

image bg extra_poem_preview:
    Fixed(
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "background.png")),
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "paper.png")),
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "bloc.png")),
        fit_first=True
    )

image extra_poem_paper:
    Fixed(
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "paper.png")),
        MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_POEM, "bloc.png")),
        fit_first=True
    )

#====Chibi
image chibi_blink_effect:
    block:
        MASFilterSwitch(ep_chibis.sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[1]))
        block:
            choice:
                3
            choice:
                5
            choice:
                7
        MASFilterSwitch(ep_chibis.sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[2]))
        choice 0.02:
            block:
                choice:
                    8
                choice:
                    6
                choice:
                    4
                MASFilterSwitch(ep_chibis.sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[1]))
        choice 0.098:
            pass
        0.06
        repeat

image chibi_hover_effect:
    block:
        MASFilterSwitch(ep_chibis.sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[3]))

image extra_chibi_base = LiveComposite(
    (188, 188),
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_background_accessories),
    (0, 0), "chibi_blink_effect",
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessory_1),
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessory_2)
    )

image extra_chibi_hover = LiveComposite(
    (188, 188),
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_background_accessories),
    (0, 0), "chibi_hover_effect",
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessory_1),
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessory_2)
    )

#====Poof
image sprite_poof = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_ANIMATIONS, "poof.png"), (222, 222), (3, 3), 0.09, loop=False)
image sprite_poof_n = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_ANIMATIONS, "poof-n.png"), (222, 222), (3, 3), 0.09, loop=False)
image extra_poof_effect :
    ConditionSwitch(
        "mas_isDayNow()", "sprite_poof",
        "mas_isNightNow()", "sprite_poof_n")

#====Coin
image coin_heads = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_ICONS, "coin_heads.png"))
image coin_tails = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_ICONS, "coin_tails.png"))
image sprite_coin = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_ANIMATIONS, "coin.png"), (100, 100), (3, 2), .125, loop=True)
image sprite_coin_n = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_ANIMATIONS, "coin-n.png"), (100, 100), (3, 2), .125, loop=True)
image extra_coin_flip:
    ConditionSwitch(
        "mas_isDayNow()", "sprite_coin",
        "mas_isNightNow()", "sprite_coin_n")

#====Idle edit
image monika staticpose = extra_no_learning
image monika reading = extra_library_reading

#====Misc
image maxwell_animation = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_ANIMATIONS, "maxwell_cat.png"), (297, 300), (10, 15), 0.0900, loop=False)

#===========================================================================================
# SCREEN
#===========================================================================================
#=== Buttons ===
screen extraplus_button():
    #Displays the Extra+ button on the overlay. Handles hotkeys and button actions for opening the Extra+ menu.
    zorder 15
    style_prefix "hkb"

    # Cache screen check to avoid multiple calls
    $ EP_hkb_overlay_active = renpy.get_screen("hkb_overlay")

    if store.mas_submod_utils.current_label == "mas_piano_setupstart":
        pass

    elif EP_hkb_overlay_active:
        vbox: # Main button container
            xpos 0.05
            yanchor 1.0
            ypos 50

            $ buttons_text = store.ep_button.getDynamicButtonText()
            textbutton buttons_text action Function(store.ep_button.show_menu) sensitive store.mas_hotkeys.talk_enabled

        if store.mas_hotkeys.talk_enabled:
            key "x" action Function(store.ep_button.show_menu)
            key "a" action Function(store.ep_affection.notify_affection)
            key "X" action Function(store.ep_button.show_menu)
            key "A" action Function(store.ep_affection.notify_affection)

screen extraplus_interactions():
    #Shows the main Extra+ interactions menu, letting the player choose between date, minigames, tools, or boop options.
    zorder 50
    style_prefix "hkb"

    timer 600 action Jump("boop_timer_expired") # 10 minute timer

    vbox: # Main menu container
        xpos 0.05
        yanchor 1.0
        ypos 210

        use extra_close_button()
        textbutton _("Dates") action Jump("extraplus_walk") sensitive (store.ep_affection.getCurrentAffection() >= 0)
        textbutton _("Games") action Jump("extraplus_minigames") sensitive (store.ep_affection.getCurrentAffection() >= 30)
        textbutton _("Tools") action Jump("extraplus_tools")
        textbutton _("Boop") action Jump("show_boop_screen") sensitive (store.ep_affection.getCurrentAffection() >= 100)

# # Custom input screen with paste-from-clipboard functionality
screen extra_input(prompt, use_return_button=True, return_button_prompt=_("Nevermind"), return_button_value="cancel_input", use_paste_button=True, paste_button_prompt=_("Paste"), use_extra_button=False, extra_button_prompt="", extra_button_value=""):
    style_prefix "input"

    window:
        # Prompt text styled like the namebox (title area)
        window:
            style "extra_input_titlebox"
            align (0.5, 0.0)

            text prompt style "say_label"

        # Input field centered in the textbox
        vbox:
            align (0.5, 0.58)

            hbox:
                xmaximum gui.text_width
                xfill True

                input id "input"

        # Buttons at the bottom, using quick menu style
        if use_return_button or use_paste_button or use_extra_button:
            hbox:
                style_prefix "quick"
                xalign 0.5
                yalign 0.995
                spacing 30

                if use_paste_button:
                    textbutton paste_button_prompt:
                        action Return("__EP_PASTE_FROM_CLIPBOARD__")

                if use_extra_button:
                    textbutton extra_button_prompt:
                        action Return(extra_button_value)

                if use_return_button:
                    textbutton return_button_prompt:
                        action Return(return_button_value)

screen extra_gen_list(extra_list, extra_area, others, close=True):
    #Generates a scrollable menu from a list, used for dynamic option lists in the submod.
    zorder 50
    style_prefix "scrollable_menu"

    fixed:
        area extra_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "extra_vp"
                yfill False
                mousewheel True
                vbox:
                    # Iterate directly over extra_list (if empty, do not execute)
                    for item in extra_list:
                        # Calculate text and action based on the structure of the element.
                        $ btn_text = item[0] if isinstance(item, tuple) else item.name
                        $ btn_action = Jump(item[1]) if isinstance(item, tuple) else Function(item)
                        textbutton _(btn_text):
                            xsize extra_area[2]
                            action btn_action

            # Process the “others” list
            for entry in others:
                # Determine the spacing value based on the structure
                $ spacing_val = entry[1] if len(entry) == 2 else entry[2]
                if spacing_val > 0:
                    null height spacing_val

                # Define the text and action based on whether the first element has a “name” attribute
                $ btn_text = entry[0].name if hasattr(entry[0], "name") else entry[0]
                $ btn_action = Function(entry[0]) if hasattr(entry[0], "name") else Jump(entry[1])
                textbutton _(btn_text):
                    xsize extra_area[2]
                    action btn_action 

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("extra_vp")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

    if close:
        vbox:
            xpos 0.097
            yanchor 1.0
            ypos 50
            use extra_close_button()

screen extra_close_button(jump_action="close_extraplus"):
    zorder 51
    style_prefix "hkb"
    key "x" action Jump(jump_action)
    key "X" action Jump(jump_action)

    vbox:
        textbutton _("Close") action Jump(jump_action)

#=== Chibis ===
screen doki_chibi_idle():
    #Displays Chibika on the screen, allowing for dragging if enabled.
    zorder 52

    # Cache screen check to avoid function call on each redraw
    $ EP_chibi_overlay_active = renpy.get_screen("hkb_overlay")

    if EP_chibi_overlay_active:
        if persistent.enable_drag_chibika:
            drag:
                child "extra_chibi_base"
                selected_hover_child "extra_chibi_hover"
                dragged store.ep_chibis.chibi_drag
                drag_offscreen True
                xpos persistent.chibika_drag_x
                ypos persistent.chibika_drag_y

        else:
            # Check if jumping animation is active
            if store.ep_chibis.is_jumping:
                # Show hover sprite with jump animation
                add "extra_chibi_hover" at chibika_jump_anim:
                    xpos store.ep_chibis.xpos
                    ypos store.ep_chibis.ypos
                
                # Timer to reset jumping state after animation
                timer 0.5 action SetField(store.ep_chibis, "is_jumping", False)
            else:
                # Normal idle state - use button for clicking
                imagebutton:
                    idle "extra_chibi_base"
                    xpos store.ep_chibis.xpos
                    ypos store.ep_chibis.ypos
                    action Function(store.ep_chibis.clicker)
                    focus_mask True


screen chibi_visual_effect(x, y):
    zorder 60
    
    add "poof_effect":
        xpos x
        ypos y
        xoffset -30
        yoffset 5

    timer 0.9 action Hide("chibi_visual_effect")

screen sticker_customization():
    #Allows the player to customize Chibika’s appearance and behavior, including dragging, visibility, and accessories.
    zorder 50
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button("close_dev_extraplus")
        textbutton _("Return") action Jump("extraplus_tools")

    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 30, 30, 30)
        xmaximum 900
        ymaximum 650
        vbox:
            spacing 18
            xalign 0.5
            style_prefix "check"

            label _("Chibi Options"):
                xalign 0.45

            hbox:
                spacing 20
                vbox:
                    label _("Draggable Chibi:")
                    # null height 30
                    textbutton _("[persistent.enable_drag_chibika]") action ToggleField(persistent, "enable_drag_chibika")
                vbox:
                    label _("Always on screen:")
                    textbutton _("[persistent.hi_chibika]") action ToggleField(persistent, "hi_chibika")
                vbox:
                    label _("Toggle Visibility:")
                    # null height 10
                    textbutton _("Show/Hide") action Function(store.ep_chibis.add_remv_chibi)

            null height 10

            label _("Dress Up!"):
                xalign 0.45

            hbox:
                spacing 20
                vbox:
                    label _("Outfits:")
                    # null height 30
                    textbutton _("Select") action Jump("doki_change_appe")
                vbox:
                    label _("Accessories:")
                    textbutton _("Select") action Jump("chibi_accessories_menu")

            null height 10

screen gen_accessories_twopane_screen():
    zorder 50

    # Use a screen variable to manage the current category
    default EP_current_acc = "primary"

    # Get the current accessory list and remove action from the ep_chibis store
    python:
        # The logic is now neatly tucked away in the ep_chibis store
        current_accessories = store.ep_chibis.getCurrentAccessories(EP_current_acc)
        current_remove_action = store.ep_chibis.getCurrentRemoveAction(EP_current_acc)

    # Close button and return
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button("close_dev_extraplus")
        textbutton _("Return") action Jump("extra_chibi_main")

    # Main content area without a visible frame, like the timeline
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        # Left pane (categories)
        vbox:
            spacing 15
            
            label _("Categories"):
                style "check_label"
                xalign 0.5
            
            textbutton _("Head"):
                style "twopane_scrollable_menu_special_button"
                action Function(store.ep_chibis.set_accessory_category, "primary")
            
            textbutton _("Others"):
                style "twopane_scrollable_menu_special_button"
                action Function(store.ep_chibis.set_accessory_category, "secondary")

            textbutton _("Background"):
                style "twopane_scrollable_menu_special_button"
                action Function(store.ep_chibis.set_accessory_category, "background")

        # Right pane (accessories list)
        frame:
            background None
            padding (0, 0)
            xsize 600
            ysize 550

            vbox:
                # --- Scrollable Area ---
                fixed:
                    viewport id "chibi_acs_vp":
                        mousewheel True
                        draggable True
                        yfill False
                        xsize 582 # width - scrollbar width
                        ysize 470 # Adjusted height

                        vbox:
                            spacing 10 # Space between cards

                            for item in current_accessories:
                                textbutton item.name action Function(item) xfill True style "scrollable_menu_button"

                    bar:
                        style "classroom_vscrollbar"
                        value YScrollValue("chibi_acs_vp")
                        xalign 1.0
                        yfill True
                        xsize 18
                        ysize 470

                null height -20
                # --- Static Remove button ---
                textbutton current_remove_action.name action Function(current_remove_action) xfill True style "scrollable_menu_button"

screen chibika_notify(message, icon):
    zorder 100
    style_prefix "chibika_notify"

    frame at chibika_notify_appear:
        hbox:
            spacing 10
            add store.ep_chibis.notify_icon.format(icon) zoom 0.5
            text "[message]" yoffset 2

    timer 4.5 action Hide("chibika_notify")

# === Zoom ===
screen extrabutton_custom_zoom():
    #Shows a button to open the custom zoom menu if the overlay is active.
    zorder 51
    style_prefix "hkb"

    # Cache screen checks to avoid multiple function calls
    $ EP_zoom_overlay_active = renpy.get_screen("hkb_overlay")
    # Check if any blocking screen is active (menus, dialogs, inputs)
    python:
        EP_blocking_screens = ["say", "choice", "extra_gen_list", "extra_input", "mas_gen_scrollable_menu"]
        EP_zoom_screens_blocking = any(renpy.get_screen(s) for s in EP_blocking_screens)

    vbox:
        xpos 0.05
        yanchor 1.0
        ypos store.ep_button.zoom_ypos

        if EP_zoom_overlay_active:
            textbutton _("Zoom") action Show("extra_custom_zoom") sensitive not EP_zoom_screens_blocking

screen extra_custom_zoom():
    #Provides a custom zoom slider and reset button for adjusting the game’s zoom level.
    use extra_no_click()
    zorder 52
    frame:
        area (0, 0, 1280, 720)
        background Solid("#0000007F")

        textbutton _("Close"):
            area (60, store.ep_button.zoom_close_ypos, 120, 35)
            style "hkb_button"
            selected False
            action [SetField(store.ep_tools, "player_zoom", store.mas_sprites.zoom_level), Hide("extra_custom_zoom")]

        frame: # Zoom slider frame
            area (195, 450, 80, 255)
            style "mas_extra_menu_frame"
            vbox:
                spacing 2
                # resets the zoom value back to default
                textbutton _("Base"):
                    style "mas_adjustable_button"
                    selected False
                    xsize 72 ysize 35 xalign 0.3
                    action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)
                    
                # Slider for adjusting zoom
                bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                    style "mas_adjust_vbar"
                    xalign 0.5
                $ store.mas_sprites.adjust_zoom()

# === Games ===
screen extra_no_click():
    #Disables advancing the dialogue or clicking, used to restrict player input during certain events.
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()
    key "mouseup_3" action NullAction()

    imagebutton:
        idle "mod_assets/other/transparent.png"
        action NullAction()

screen library_quiet_click():
    zorder 100
    # Full screen invisible button - click anywhere to continue
    button:
        xysize (config.screen_width, config.screen_height)
        action Return()
        background None

screen score_minigame(game=None):
    #Shows the current score for a minigame (RPS or Shell Game) with player and opponent stats.
    key "h" action NullAction()
    key "H" action NullAction()
    key "mouseup_3" action NullAction()

    # Initialize variables with defaults to avoid undefined errors
    # Then set based on game type
    $ first_text = "???"
    $ second_text = "???"
    $ first_score = 0
    $ second_score = 0

    if game == "rps":
        $ first_text = m_name
        $ second_text = player
        $ first_score = ep_rps.moni_wins
        $ second_score = ep_rps.player_wins
    elif game == "sg":
        $ first_text = "Turns"
        $ second_text = "Score"
        $ first_score = ep_sg.current_turn
        $ second_score = ep_sg.correct_answers
        
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.025
        text "[first_text] : [first_score]"  size 25 style "monika_text"
        text "[second_text] : [second_score]"  size 25 style "monika_text"

# === Interactions ===
screen boop_revamped():
    zorder 49
    
    key "mouseup_1" action Function(store.EP_interaction_manager.handle_click, button=1)
    key "mouseup_3" action Function(store.EP_interaction_manager.handle_click, button=3) # Right click
    vbox:
        style_prefix "check"
        yanchor 0.5
        xanchor 1.0
        xpos 1.0
        ypos 0.5

        if not store.EP_interaction_manager.ep_boop_war_active:
            label _("Interactions\navailable:")
            text _(" Cheeks\n Head\n Nose\n Ears\n Hands\n Shoulders"):
                outlines [(2, "#808080", 0, 0)]
    
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button("close_boop_screen")
        textbutton _("Return") action Jump("return_boop_screen")

screen boop_capture_overlay(label_boop):
    zorder 49  # Below the UI buttons (which are at zorder 51)

    python:
        # Define variables locally for clarity and safety
        # Use try/except for compatibility with older MAS versions
        nose_zone = None
        try:
            interaction_manager = store.EP_interaction_manager
            # Check if zones are enabled (disabled on older MAS versions)
            if interaction_manager._zones_enabled and interaction_manager.cz_manager:
                nose_zone_key = store.mas_interactions.ZONE_EXTRA_NOSE
                current_zoom = store.mas_sprites.zoom_level
                nose_cz = interaction_manager.cz_manager.get(
                    nose_zone_key,
                    current_zoom
                )

                if nose_cz and not nose_cz.disabled:
                    corners = nose_cz.corners
                    if corners:
                        min_x = min(x for x, y in corners) # NOQA
                        min_y = min(y for x, y in corners) # NOQA
                        max_x = max(x for x, y in corners) # NOQA
                        max_y = max(y for x, y in corners) # NOQA
                        nose_zone = {
                            'x': min_x,
                            'y': min_y,
                            'w': max_x - min_x,
                            'h': max_y - min_y
                        }
        except (AttributeError, TypeError):
            # Older MAS version - zones not available
            pass

    # Render invisible imagebutton only over the nose
    if nose_zone:
        imagebutton:
            xpos nose_zone['x']
            ypos nose_zone['y']
            xysize (nose_zone['w'], nose_zone['h'])
            idle Solid("#00000000")  # Completely transparent
            action Function(interaction_manager.handle_dating_click, label_boop)

screen extra_boop_event(timelock, endlabel, editlabel):
    zorder 50
    # Countdown timer
    timer 15 action Function(renpy.show, "monika 2etc")
    timer timelock action Jump(endlabel)
    
    # Click capture (handles war logic automatically)
    key "mouseup_1" action Function(store.EP_interaction_manager.handle_click, button=1)

screen boop_war_score_ui():
    #Displays the score counter for the boop war.
    zorder 51
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.045
        text _("Boops : [store.EP_interaction_manager.ep_boop_war_count]") size 25 style "monika_text"

# === DATES ===
screen extra_dating_loop(ask, label_boop, boop_enable=False):
    zorder 51

    key "t" action Jump(ask)
    key "T" action Jump(ask)

    if boop_enable:
        use boop_capture_overlay(label_boop)
    
    vbox:
        xpos store.ep_dates.xpos
        yanchor 1.0
        ypos store.ep_dates.ypos
        
        textbutton _("Talk"):
            style "hkb_button"
            action Jump(ask)

screen extra_timer_monika(time, label):

    timer time action SetField(store.ep_dates, "stop_snike_time", True)
    
    timer 0.5 repeat True action If(
        store.ep_dates.stop_snike_time and renpy.get_screen("extra_dating_loop"),
        true=[
            Hide("extra_dating_loop"),
            Jump(label)
        ],
        false=NullAction()
    )

screen force_mouse_move():
    #Forces the mouse to move to a specific position, used for certain effects or minigames.
    on "show":
        action MouseMove(x=412, y=237, duration=.3)
    timer .6 repeat True action MouseMove(x=412, y=237, duration=.3)

# === Mics ===
screen extra_feedback_notif(msg, tag, txt_color, duration=1.3, trans=boop_feedback_trans):
    # Show a notification message at the mouse position
    zorder 2000
    timer duration action Hide(tag)
    default EP_feedback_pos = (renpy.get_mouse_pos()[0] + renpy.random.randint(-30, 30), renpy.get_mouse_pos()[1] + renpy.random.randint(-30, 30))
    
    text "{}".format(msg) at trans pos EP_feedback_pos size 40 color txt_color outlines [ (2, "#000", 0, 0) ] font "mod_assets/font/m1_fixed.ttf"

screen extra_doki_heartbeat():
    # Show a heartbeat animation for Monika
    zorder 2000
    modal True
    timer 0.9 repeat True action Function(store.ep_tools.show_doki_feedback, "*Doki*")

    key "mouseup_1" action Return()
    key "mouseup_3" action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "K_KP_ENTER" action Return()

screen bday_oki_doki():
    #Shows a special button for Monika’s birthday event.
    zorder 150
    style_prefix "hkb"
    vbox:
        xpos 590
        ypos 0.9
        if mas_submod_utils.current_label == "mas_dockstat_empty_desk_from_empty":
            textbutton _("Oki Doki") action Function(store.ep_files.make_bday_oki_doki)

screen maxwell_april_fools():
    #Displays the Maxwell cat animation and plays music for the April Fools event.
    zorder 200

    vbox: # Main menu container
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 210

        textbutton _("Close") action NullAction() sensitive False
        textbutton _("Dates") action NullAction() sensitive False
        textbutton _("Games") action NullAction() sensitive False
        textbutton _("Tools") action NullAction() sensitive False
        textbutton _("Boop") action NullAction() sensitive False

    on "show" action Play("maxwellcat", sfx_maxwell_theme)
    add "maxwell_animation":
        xpos 0.45
        zoom 0.4

    timer 13.0 action [
        Stop("maxwellcat"),
        Return()
    ]

screen extraplus_stats_screen():
    #Shows the player’s stats and time spent with Monika in a styled frame.
    zorder 50
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button()
        textbutton _("Return") action Jump("extraplus_tools")

    frame:
        style_prefix "check"
        xalign 0.92
        yalign 0.5
        padding (40, 20, 40, 50)
        xmaximum 500
        ymaximum 650

        has vbox:
            spacing 25
            label _("Your Time with [m_name]"):
                xalign 0.5
            vbox:
                xfill True
                text _("Current Visit")
                add DynamicDisplayable(store.ep_tools.getCurrSessionD) yalign 0.5

            vbox:
                xfill True
                spacing 25
                python:
                    stats_data = store.ep_tools.getMasStats()
                for stat_name, stat_value in stats_data.items():
                    vbox:
                        xfill True
                        text stat_name
                        text str(stat_value)

screen extra_timeline_screen():
    zorder 49
    
    default EP_timeline_data = store.ep_tools.getTimelineData()

    # --- Navigation Buttons (Left) ---
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button()
        textbutton _("Return") action Jump("extraplus_tools")

    # --- Main Panel (Center) ---
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xmaximum 600
        ymaximum 680
        padding (30, 30, 30, 30)

        vbox:
            
            # Title
            hbox:
                style_prefix "check"
                xalign 0.5
                label _("Our History Together")

            # --- Viewport and Scrollbar ---
            fixed:
                # The viewport now takes up the full width to capture the mousewheel everywhere
                viewport id "timeline_vp":
                    mousewheel True
                    draggable True
                    yfill False
                    xsize 528
                    ysize 570
                    
                    # The inner vbox has a smaller size to leave space for the scrollbar
                    vbox:
                        xsize 510
                        spacing 10 # Space between cards
                        
                        if not EP_timeline_data:
                            text _("Our story is just beginning..."):
                                xalign 0.5
                                yalign 0.5 # This will center it in the available space

                        for entry in EP_timeline_data:
                            $ date_str = store.ep_tools.exp_fmt_date(entry.date)
                            
                            # --- Event Card ---
                            frame:
                                xfill True
                                padding (12, 12)
                                background Solid("#00000050") # Semi-transparent background for the card

                                vbox:
                                    spacing 8
                                    xfill True

                                    # --- Icon and Title ---
                                    hbox:
                                        spacing 10
                                        
                                        text _(entry.icon):
                                            font store.ep_tools.pictograms_font
                                            size 25
                                            color "#FF69B4"
                                            yalign 0.5

                                        text _("[entry.title]"):
                                            size 20
                                            bold True
                                            yalign 0.5
                                    
                                    # --- Description ---
                                    text _("[entry.description]"):
                                        size 18

                                    null height 1

                                    # --- Date ---
                                    text _("Date: [date_str]"):
                                        size 16
                                        italic True
                                        xalign 1.0
                
                bar:
                    style "classroom_vscrollbar" 
                    value YScrollValue("timeline_vp")
                    xalign 1.0
                    yfill True
                    xsize 18

# === Fridge ===
screen extra_fridge_magnets():
    modal True
    zorder 50
    layer "master"

    # We create a new instance. The manager will handle loading persistent data.
    default EP_fridge_manager = store.ep_fridge.MagnetManager()
    
    # Font size
    $ magnet_size = 70
    
    # Background
    add EP_fridge_manager.event_handler
    
    # --- Drop Zones ---
    button:
        xysize 535, 375
        offset 200, 20
        # background "#fff8"
        action Function(EP_fridge_manager.put, "top")
        
    button:
        xysize 535, 248
        offset 200, 455
        # background "#fff8"
        action Function(EP_fridge_manager.put, "bottom")
        
    # --- Magnet Box ---
    button:
        offset 850, 515 
        add "extra_fm_box" zoom 0.75
        # background "#fff8"
        action Function(EP_fridge_manager.take)

    # --- Coffee Bag (only visible if Monika has coffee)
    $ _ep_coffee_data = store.ep_fridge.getCoffeeData()
    if _ep_coffee_data["has_coffee"]:
        button:
            offset 1100, 448
            add "extra_fm_coffee" zoom 0.50
            # background "#fff8"
            action Show("extra_coffee_info")

    # --- Magnet Rendering ---
    for i in EP_fridge_manager.top:
        use extra_magnet_render(i, EP_fridge_manager, "top", magnet_size)

    for i in EP_fridge_manager.bottom:
        use extra_magnet_render(i, EP_fridge_manager, "bottom", magnet_size)

    if EP_fridge_manager.holding:
        use extra_magnet_render(EP_fridge_manager.holding, EP_fridge_manager, None, magnet_size)
        timer .01 repeat True action Function(EP_fridge_manager.tick)

    # Exit Button
    vbox:
        style_prefix "hkb"
        xpos 0.85
        yanchor 1.0
        ypos 90
        use extra_close_button("extra_fridge_quit")
        textbutton _("Clean") action Function(EP_fridge_manager.clean_magnets)

# Animation for coffee popup - fade in with slide up
transform coffee_popup_show:
    alpha 0.0 yoffset 20
    easein 0.3 alpha 1.0 yoffset 0

transform coffee_popup_hide:
    alpha 1.0
    easeout 0.3 alpha 0.0 yoffset -10

# Coffee stock info popup for the fridge
screen extra_coffee_info():
    zorder 100
    modal False
    
    $ coffee_data = store.ep_fridge.getCoffeeData()
    $ bar_percent = coffee_data["percent"]
    
    timer 2.5 action Hide("extra_coffee_info", transition=Dissolve(0.3))
    
    # Positioned near the coffee bag (right side of fridge)
    frame at coffee_popup_show:
        pos (1050, 340)
        anchor (0.5, 1.0)
        padding (20, 12)
        
        vbox:
            spacing 6
            xalign 0.5
            
            # Title - uses gui.text_color for theme compatibility
            text _("Coffee Stock"):
                size 20
                xalign 0.5
                color gui.text_color
            
            # Progress bar
            bar:
                value bar_percent
                range 1.0
                xsize 140
                ysize 16
                xalign 0.5
                left_bar Solid(gui.accent_color)
                right_bar Solid("#4a4a4a")
            
            # Stock text as percentage - more discreet
            text _("{}%").format(int(coffee_data["percent"] * 100)):
                size 14
                xalign 0.5
                color gui.text_color

screen extra_magnet_render(item, manager, location, fsize):
    # We calculate the dynamic colors (Day/Night) in real time
    $ current_main_color = store.ep_fridge.getCurrentColor(item.base_color)
    $ current_shadow_color = store.ep_fridge.getCurrentColor(item.shadow_base_color)

    fixed fit_first True:
        # --- 1. Shadow (3D Effect) ---
        text item.letter:
            font store.ep_fridge.EP_FM_FONT
            size fsize
            color current_shadow_color # Dynamic shadow
            outlines [(2, current_shadow_color, 0, 0)]
            at fm_text_trans(item.rotation)
            pos item.x, item.y anchor 0.5, 0.5
            yoffset 3 # A small offset to make the shadow look better
        
        # --- 2. Main Letter (Front) ---
        if location:
            # First, we draw the main text in its correct position
            text item.letter:
                font store.ep_fridge.EP_FM_FONT
                size fsize
                color current_main_color
                outlines [(2, current_shadow_color, 0, 0)]
                at fm_text_trans(item.rotation)
                pos item.x, item.y anchor 0.5, 0.5
            
            # Then, we overlay a transparent button for interaction
            button:
                style "empty" # A style with no background or margins
                xysize (fsize, fsize) # We make the button the size of the letter
                pos item.x, item.y anchor 0.5, 0.5
                action Function(manager.swap, location, item)
        
        else:
            text item.letter:
                font store.ep_fridge.EP_FM_FONT
                size fsize
                color current_main_color
                outlines [(2, current_shadow_color, 0, 0)]
                at fm_text_trans(item.rotation)
                pos item.x, item.y anchor 0.5, 0.5

screen _extra_plus_submod_settings():
    # Displays the settings pane for the Extra+ submod in the MAS settings menu.
    $ tooltip = renpy.get_screen("submods", "screens").scope["tooltip"]

    vbox:
        style_prefix "check"
        box_wrap False
        xfill True
        xmaximum 1000

        textbutton _("{b}Smart button text{/b}"):
            action ToggleField(persistent, "_ep_dynamic_button_text")
            hovered tooltip.Action("Changes button text based on mood or events.")

        textbutton _("{b}New restaurant style{/b}"):
            action ToggleField(persistent, "_ep_restaurant_variant")
            hovered tooltip.Action("Uses the redesigned restaurant background.")

        textbutton _("{b}Verify installation{/b}"):
            action Function(store.ep_files.run_asset_linter)
            hovered tooltip.Action("Creates a report of missing submod files.")

        textbutton _("{b}Remove old files{/b}"):
            action Function(store.ep_files.cleanup_old_files)
            hovered tooltip.Action("Removes outdated files from previous versions.")

# DEBUG: Visual overlay to see clickable zones
# screen ep_debug_zones():
#     zorder 100
    
#     # Define colors for each zone type
#     python:
#         zone_colors = {
#             "extra_head": "#ff000080",       # Red
#             "extra_nose": "#00ff0080",       # Green  
#             "extra_cheek_l": "#0000ff80",    # Blue
#             "extra_cheek_r": "#0000ff80",    # Blue
#             "extra_hands": "#ffff0080",      # Yellow
#             "extra_ear_l": "#ff00ff80",      # Magenta
#             "extra_ear_r": "#ff00ff80",      # Magenta
#             "extra_shoulder_l": "#00ffff80", # Cyan
#             "extra_shoulder_r": "#00ffff80", # Cyan
#         }
    
#     # Draw each zone as a rectangle
#     for zone_name, coords in store.EP_interaction_manager.zone_map.items():
#         $ x1, y1 = coords[0]
#         $ x2, y2 = coords[2]  # Opposite corner
#         $ width = x2 - x1
#         $ height = y2 - y1
#         $ color = zone_colors.get(zone_name, "#ffffff80")
        
#         # Draw the zone rectangle
#         frame:
#             xpos x1
#             ypos y1
#             xsize width
#             ysize height
#             background color
            
#             # Label in center
#             text zone_name.replace("extra_", ""):
#                 align (0.5, 0.5)
#                 size 12
#                 color "#000"
#                 outlines [(1, "#fff", 0, 0)]

#===========================================================================================
# TRANSFORM
#===========================================================================================

transform chibi_dissolve:
    # Controls the fade-in and fade-out of the chibi screen.
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform boop_feedback_trans:
    # Sparkle/shimmer effect - a beautiful flash instead of a pulsation
    xanchor 0.5 yanchor 0.5
    
    # Initial setup
    alpha 0.0
    zoom 0.3
    yoffset 0
    rotate 0
    
    # Pop-in flash effect
    parallel:
        # Gentle floating upward
        easein 0.15 yoffset -15
        easeout 1.0 yoffset -80
    parallel:
        # Sparkle alpha - quick bright flash then graceful fade
        linear 0.05 alpha 1.0
        pause 0.1
        linear 0.1 alpha 0.85
        pause 0.3
        easeout 0.6 alpha 0.0
    parallel:
        # Sparkle scale - quick expand with slight overshoot, then gentle settle
        easein 0.08 zoom 1.15
        easeout 0.12 zoom 1.0
        pause 0.2
        easeout 0.5 zoom 0.95
    parallel:
        # Subtle shimmer rotation
        ease 0.1 rotate -3
        ease 0.15 rotate 3
        ease 0.2 rotate -1
        ease 0.25 rotate 0

transform doki_feedback_trans:
    # Heartbeat pulsation effect - "lub-dub" pattern
    xanchor 0.5 yanchor 0.5
    alpha 1.0
    zoom 1.0
    
    parallel:
        # Gentle float upward while pulsing
        ease 0.6 yoffset -50
    parallel:
        # Stay visible during heartbeats, then fade out
        pause 0.45
        easeout 0.15 alpha 0.0
    parallel:
        # Heartbeat pulse pattern: lub-dub, lub-dub
        # First beat (lub)
        easein 0.06 zoom 1.25
        easeout 0.06 zoom 1.0
        # Second beat (dub) - slightly smaller
        pause 0.04
        easein 0.05 zoom 1.15
        easeout 0.07 zoom 1.0
        # Brief rest between heartbeats
        pause 0.12
        # Second heartbeat cycle
        easein 0.06 zoom 1.2
        easeout 0.06 zoom 1.0
        pause 0.03
        easein 0.04 zoom 1.1
        easeout 0.06 zoom 1.0

transform hover_card:
    on idle:
        pause .15
        yoffset 0
        easein .175 yoffset 10
        easein .175 yoffset 0

    on hover:
        pause .15
        yoffset 0
        easein .175 yoffset -20

transform animated_book:
    on show:
        xoffset 1000
        linear 0.5 xoffset 0
    on hide:
        xoffset 0
        linear 0.5 xoffset 1000

transform rotatecoin:
    zoom 0.6
    rotate 90
    pause .15
    yoffset 0
    easein .400 yoffset -400
    easeout .400 yoffset 0
    yoffset 0

transform jumpingaround:
    xpos 0 ypos 600
    parallel:
        linear 3.1 xpos 1170
        linear 3.1 xpos 0
        repeat
    parallel:
        choice:
            easein 1 ypos 0
            easeout 1 ypos 600
        choice:
            easein 1 ypos 100
            easeout 1 ypos 600
        choice:
            easein 1 ypos 200
            easeout 1 ypos 600
        choice:
            easein 1 ypos 300
            easeout 1 ypos 600
        repeat
    
transform tfloat(x=640, z=0.80, y_distance=15, duration=5):
    yanchor 1.0
    subpixel True
    ypos 1.03  # Base position slightly offscreen for bounce effect

    on show:
        zoom z * 0.95
        alpha 0.0
        xcenter x
        yoffset -20
        easein 0.25 yoffset 0 zoom z * 1.0 alpha 1.0
        block:
            ease duration yoffset y_distance
            ease duration yoffset 0
            repeat

    on update, replace:
        alpha 1.0
        parallel:
            easein 0.25 xcenter x zoom z * 1.0
        parallel:
            block:
                ease duration yoffset y_distance
                ease duration yoffset 0
                repeat

transform t11_float:
    tfloat(640)  # Center position with floating

transform t21_float:
    tfloat(400)  # Left position with floating

transform init_card_slide:
    zoom 0.6
    ypos -1200
    alpha 0.0
    easein 0.5 ypos 0 alpha 1.0

transform hit_card:
    zoom 0.6
    alpha 0.0
    xoffset 100
    easein 0.3 xoffset 0 alpha 1.0
    delay 0.1

transform score_rotate_left:
    rotate -20
    rotate_pad True
    transform_anchor True

transform fm_text_trans(r):
    subpixel True
    rotate_pad True 
    rotate r

transform chibika_notify_appear:
    # Pop-in with bounce effect
    on show:
        alpha 0
        zoom 0.85
        yoffset 15
        easein 0.35 alpha 1.0 zoom 1.05 yoffset -3
        easeout 0.20 zoom 1.0 yoffset 0
    on hide:
        easein 0.35 alpha 0.5 yoffset -35
        linear 0.30 alpha 0.0

# Transform for Chibika's jump animation when notifying
transform chibika_jump_anim:
    # Quick jump up and down
    yoffset 0
    easein 0.15 yoffset -25
    easeout 0.20 yoffset 0

#===========================================================================================
# STYLES
#===========================================================================================

style chibika_notify_frame is empty:
    ypos gui.notify_ypos
    background Frame(ep_chibis.notify_frame, gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style chibika_notify_text is gui_text:
    font "gui/font/Halogen.ttf"
    size gui.notify_text_size

style extra_input_titlebox is default:
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding (15, gui.namebox_borders.padding[1], 15, gui.namebox_borders.padding[3])
    ypos gui.name_ypos
    ysize gui.namebox_height

style extra_input_titlebox_dark is default:
    background Frame("gui/namebox_d.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding (15, gui.namebox_borders.padding[1], 15, gui.namebox_borders.padding[3])
    ypos gui.name_ypos
    ysize gui.namebox_height
    
#===========================================================================================
# BACKGROUNG
#===========================================================================================

#====Cafe

#Day images
image EP_submod_background_cafe_day = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "day.png")
image EP_submod_background_cafe_rain = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "rain.png")

#Night images
image EP_submod_background_cafe_night = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "n.png")
image EP_submod_background_cafe_rain_night = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "rain-n.png")

#Sunset images
image EP_submod_background_cafe_ss = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "ss.png")
image EP_submod_background_cafe_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_CAFE, "rain-ss.png")

init -1 python:
    EP_background_cafe = MASFilterableBackground(
        "EP_background_cafe",
        "Cafe (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_cafe_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_cafe_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_cafe_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_cafe_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_cafe_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_cafe_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_cafe_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_cafe_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_cafe_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_cafe_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_cafe_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_cafe_rain_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=False,
        entry_pp=store.mas_background._extra_cafe_entry,
        exit_pp=store.mas_background._extra_cafe_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _extra_cafe_entry(_old, **kwargs):
        """
        Entry programming point for cafe background

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()
            store.mas_surpriseBdayHideVisuals()

        store.monika_chr.tablechair.table = "extraplus_cafe"
        store.monika_chr.tablechair.chair = "extraplus_cafe"

    def _extra_cafe_exit(_new, **kwargs):
        """
        Exit programming point for cafe background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        if store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()
        
        #Birthday
        if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
            store.mas_surpriseBdayShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

#====Restaurant (Updated paths with variant support)

#Day images
image EP_submod_background_restaurant_day = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "day.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "day.png")
)
image EP_submod_background_restaurant_rain = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "rain.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain.png")
)

#Night images
image EP_submod_background_restaurant_night = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "n.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "n.png")
)
image EP_submod_background_restaurant_rain_night = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "rain-n.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain-n.png")
)

#Sunset images
image EP_submod_background_restaurant_ss = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "ss.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "ss.png")
)
image EP_submod_background_restaurant_rain_ss = ConditionSwitch(
    "persistent._ep_restaurant_variant", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT_VARIANT, "rain-ss.png"),
    "True", ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain-ss.png")
)

init -1 python:
    EP_background_restaurant = MASFilterableBackground(
        "EP_background_restaurant",
        "Restaurant (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_restaurant_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_restaurant_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_restaurant_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_restaurant_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_restaurant_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_restaurant_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_restaurant_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_restaurant_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_restaurant_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_restaurant_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_restaurant_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_restaurant_rain_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=False,
        entry_pp=store.mas_background._extra_restaurant_entry,
        exit_pp=store.mas_background._extra_restaurant_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _extra_restaurant_entry(_old, **kwargs):
        """
        Entry programming point for cafe background

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()
            store.mas_surpriseBdayHideVisuals()

        store.monika_chr.tablechair.chair = "extraplus_restaurant"
        store.monika_chr.tablechair.table = "extraplus_restaurant"

    def _extra_restaurant_exit(_new, **kwargs):
        """
        Exit programming point for restaurant background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        if store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()
        
        #Birthday
        if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
            store.mas_surpriseBdayShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

#====Pool (Updated paths)

#Day images
image EP_submod_background_pool_day = ep_folders._join_path(ep_folders.EP_DATE_POOL, "day.png")
image EP_submod_background_pool_rain = ep_folders._join_path(ep_folders.EP_DATE_POOL, "rain.png")

#Night images
image EP_submod_background_pool_night = ep_folders._join_path(ep_folders.EP_DATE_POOL, "n.png")
image EP_submod_background_pool_rain_night = ep_folders._join_path(ep_folders.EP_DATE_POOL, "rain-n.png")

#Sunset images
image EP_submod_background_pool_ss = ep_folders._join_path(ep_folders.EP_DATE_POOL, "ss.png")
image EP_submod_background_pool_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_POOL, "rain-ss.png")

init -1 python:
    EP_background_pool = MASFilterableBackground(
        "EP_background_pool",
        "Pool (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_pool_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_pool_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_pool_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_pool_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_pool_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_pool_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_pool_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_pool_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_pool_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_pool_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_pool_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_pool_rain_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=False,
        entry_pp=store.mas_background._extrapool_entry,
        exit_pp=store.mas_background._extrapool_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _extrapool_entry(_old, **kwargs):
        """
        Entry programming point for pool background

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()
            store.mas_surpriseBdayHideVisuals()

        store.monika_chr.tablechair.table = "extraplus_pool"
        store.monika_chr.tablechair.chair = "extraplus_pool"

    def _extrapool_exit(_new, **kwargs):
        """
        Exit programming point for pool background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        if store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()
        
        #Birthday
        if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
            store.mas_surpriseBdayShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

#====Library (Updated paths)

#Day images
image EP_submod_background_library_day = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "day.png")
image EP_submod_background_library_rain = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "rain.png")

#Night images
image EP_submod_background_library_night = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "n.png")
image EP_submod_background_library_rain_night = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "rain-n.png")

#Sunset images
image EP_submod_background_library_ss = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "ss.png")
image EP_submod_background_library_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_LIBRARY, "rain-ss.png")

init -1 python:
    EP_background_library = MASFilterableBackground(
        "EP_background_library",
        "Library (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_library_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_library_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_library_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_library_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_library_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_library_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_library_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_library_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_library_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_library_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_library_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_library_rain_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=False,
        entry_pp=store.mas_background._extralibrary_entry,
        exit_pp=store.mas_background._extralibrary_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _extralibrary_entry(_old, **kwargs):
        """
        Entry programming point for library background

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()
            store.mas_surpriseBdayHideVisuals()

        store.monika_chr.tablechair.table = "extraplus_library"
        store.monika_chr.tablechair.chair = "extraplus_library"

    def _extralibrary_exit(_new, **kwargs):
        """
        Exit programming point for library background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        if store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()
        
        #Birthday
        if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
            store.mas_surpriseBdayShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

# #====Arcade (Updated paths)

# #Day images
# image EP_submod_background_arcade_day = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "day.png")
# image EP_submod_background_arcade_rain = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain.png")

# #Night images
# image EP_submod_background_arcade_night = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "n.png")
# image EP_submod_background_arcade_rain_night = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain-n.png")

# #Sunset images
# image EP_submod_background_arcade_ss = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "ss.png")
# image EP_submod_background_arcade_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain-ss.png")

# init -1 python:
#     EP_background_extra_arcade = MASFilterableBackground(
#         "EP_background_extra_arcade",
#         "Arcade (Extra+)",

#         MASFilterWeatherMap(
#             day=MASWeatherMap({
#                 store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_day",
#                 store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain",
#                 store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain",
#                 store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain",
#             }),
#             night=MASWeatherMap({
#                 store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_night",
#                 store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain_night",
#                 store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain_night",
#                 store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain_night",
#             }),
#             sunset=MASWeatherMap({
#                 store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_ss",
#                 store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain_ss",
#                 store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain_ss",
#                 store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain_ss",
#             }),
#         ),

#         MASBackgroundFilterManager(
#             MASBackgroundFilterChunk(
#                 False,
#                 None,
#                 MASBackgroundFilterSlice.cachecreate(
#                     store.mas_sprites.FLT_NIGHT,
#                     60
#                 )
#             ),
#             MASBackgroundFilterChunk(
#                 True,
#                 None,
#                 MASBackgroundFilterSlice.cachecreate(
#                     store.mas_sprites.FLT_SUNSET,
#                     60,
#                     30*60,
#                     10,
#                 ),
#                 MASBackgroundFilterSlice.cachecreate(
#                     store.mas_sprites.FLT_DAY,
#                     60
#                 ),
#                 MASBackgroundFilterSlice.cachecreate(
#                     store.mas_sprites.FLT_SUNSET,
#                     60,
#                     30*60,
#                     10,
#                 ),
#             ),
#             MASBackgroundFilterChunk(
#                 False,
#                 None,
#                 MASBackgroundFilterSlice.cachecreate(
#                     store.mas_sprites.FLT_NIGHT,
#                     60
#                 )
#             )
#         ),

#         #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
#         disable_progressive=False,
#         hide_masks=False,
#         hide_calendar=True,
#         unlocked=False,
#         entry_pp=store.mas_background._extra_arcade_entry,
#         exit_pp=store.mas_background._extra_arcade_exit,
#         ex_props={"skip_outro": None}
#     )

# init -2 python in mas_background:
#     def _extra_arcade_entry(_old, **kwargs):
#         """
#         Entry programming point for arcade background

#         NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
#         IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

#         IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
#         """
#         if kwargs.get("startup"):
#             pass

#         else:
#             store.mas_o31HideVisuals()
#             store.mas_d25HideVisuals()
#             store.mas_surpriseBdayHideVisuals()

#         store.monika_chr.tablechair.table = "extraplus_arcade"
#         store.monika_chr.tablechair.chair = "extraplus_arcade"

#     def _extra_arcade_exit(_new, **kwargs):
#         """
#         Exit programming point for arcade background
#         """
#         #O31
#         if store.persistent._mas_o31_in_o31_mode:
#             store.mas_o31ShowVisuals()
#
#         #D25
#         if store.persistent._mas_d25_deco_active:
#             store.mas_d25ShowVisuals()
#         
#         #Birthday
#         if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
#             store.mas_surpriseBdayShowVisuals()

#         store.monika_chr.tablechair.table = "def"
#         store.monika_chr.tablechair.chair = "def"
