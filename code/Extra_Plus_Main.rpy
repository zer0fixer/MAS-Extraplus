#===========================================================================================
# SUBMOD
#===========================================================================================

#Submod created by ZeroFixer(u/UnderstandingAny7135), this submod is made for MAS brothers/sisters.
#Shoutout to u/my-otter-self at reddit, who proofread the whole mod.
# Source Code: https://github.com/zer0fixer/MAS-Extraplus

#====Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="ZeroFixer",
        name="Extra Plus",
        description="Expand your time with Monika with new minigames, dates, and interactions.",
        version="1.3.4",
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

    # #Just in case (Android Port).
    # # Setting for 'default_zoom_level'
    # if not hasattr(store.mas_sprites, "default_zoom_level"):
    #     store.mas_sprites.default_zoom_level = 1.0
    # # Fix for 'zoom_level'
    # if not hasattr(store.mas_sprites, "zoom_level"):
    #     store.mas_sprites.zoom_level = 1.0

#===========================================================================================
# VARIABLES
#===========================================================================================
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
    pictograms_font = store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "pictograms_icons.ttf")
    affection_icons = store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "peperrito_faces.ttf")

init -20 python in ep_tools:
    import store
    noises_submod = store.mas_submod_utils.isSubmodInstalled("Noises Submod")

init 20 python in ep_files:
    groceries_menu = [
        store.ep_files.GiftAction(_("Coffee"), "coffee"),
        store.ep_files.GiftAction(_("Chocolates"), "chocolates"),
        store.ep_files.GiftAction(_("Cupcake"), "cupcake"),
        store.ep_files.GiftAction(_("Fudge"), "fudge"),
        store.ep_files.GiftAction(_("Hot Chocolate"), "hotchocolate"),
        store.ep_files.GiftAction(_("Candy"), "candy"),
        store.ep_files.GiftAction(_("Candy Canes"), "candycane"),
        store.ep_files.GiftAction(_("Candy Corn"), "candycorn"),
        store.ep_files.GiftAction(_("Christmas Cookies"), "christmascookies")
    ]

    objects_menu_base = [
        store.ep_files.GiftAction(_("Promise Ring"), "promisering"),
        store.ep_files.GiftAction(_("Roses"), "roses"),
        store.ep_files.GiftAction(_("Quetzal Plushie"), "quetzalplushie"),
        store.ep_files.GiftAction(_("Thermos Mug"), "justmonikathermos")
    ]

    ribbons_menu = [
        store.ep_files.GiftAction(_("Black Ribbon"), "blackribbon"),
        store.ep_files.GiftAction(_("Blue Ribbon"), "blueribbon"),
        store.ep_files.GiftAction(_("Dark Purple Ribbon"), "darkpurpleribbon"),
        store.ep_files.GiftAction(_("Emerald Ribbon"), "emeraldribbon"),
        store.ep_files.GiftAction(_("Gray Ribbon"), "grayribbon"),
        store.ep_files.GiftAction(_("Green Ribbon"), "greenribbon"),
        store.ep_files.GiftAction(_("Light Purple Ribbon"), "lightpurpleribbon"),
        store.ep_files.GiftAction(_("Peach Ribbon"), "peachribbon"),
        store.ep_files.GiftAction(_("Pink Ribbon"), "pinkribbon"),
        store.ep_files.GiftAction(_("Platinum Ribbon"), "platinumribbon"),
        store.ep_files.GiftAction(_("Red Ribbon"), "redribbon"),
        store.ep_files.GiftAction(_("Ruby Ribbon"), "rubyribbon"),
        store.ep_files.GiftAction(_("Sapphire Ribbon"), "sapphireribbon"),
        store.ep_files.GiftAction(_("Silver Ribbon"), "silverribbon"),
        store.ep_files.GiftAction(_("Teal Ribbon"), "tealribbon"),
        store.ep_files.GiftAction(_("Yellow Ribbon"), "yellowribbon")
    ]

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

init 20 python in ep_chibis:
    primary_accessories = [
        store.ep_chibis.DokiAccessory(_("Clown Hair"), "clown_hair", "primary"),
        store.ep_chibis.DokiAccessory(_("Cat Ears"), "cat_ears", "primary"),
        store.ep_chibis.DokiAccessory(_("Christmas Hat"), "christmas_hat", "primary"),
        store.ep_chibis.DokiAccessory(_("Demon Horns"), "demon_horns", "primary"),
        store.ep_chibis.DokiAccessory(_("Flowers Crown"), "flowers_crown", "primary"),
        store.ep_chibis.DokiAccessory(_("Fox Ears"), "fox_ears", "primary"),
        store.ep_chibis.DokiAccessory(_("Graduation Cap"), "graduation_cap", "primary"),
        store.ep_chibis.DokiAccessory(_("Halo"), "halo", "primary"),
        store.ep_chibis.DokiAccessory(_("Heart Headband"), "heart_headband", "primary"),
        store.ep_chibis.DokiAccessory(_("Headphones"), "headphones", "primary"),
        store.ep_chibis.DokiAccessory(_("Neon Cat Ears"), "neon_cat_ears", "primary"),
        store.ep_chibis.DokiAccessory(_("New Year's Headband"), "hny", "primary"),
        store.ep_chibis.DokiAccessory(_("Party Hat"), "party_hat", "primary"),
        store.ep_chibis.DokiAccessory(_("Rabbit Ears"), "rabbit_ears", "primary"),
        store.ep_chibis.DokiAccessory(_("Top Hat"), "top_hat", "primary"),
        store.ep_chibis.DokiAccessory(_("Witch Hat"), "witch_hat", "primary")
    ]
    secondary_accessories = [
        store.ep_chibis.DokiAccessory(_("Black Bow Tie"), "black_bow_tie", "secondary"),
        store.ep_chibis.DokiAccessory(_("Christmas Tree"), "christmas_tree", "secondary"),
        store.ep_chibis.DokiAccessory(_("Cloud"), "cloud", "secondary"),
        store.ep_chibis.DokiAccessory(_("Coffee"), "coffee", "secondary"),
        store.ep_chibis.DokiAccessory(_("Halloween Pumpkin"), "pumpkin", "secondary"),
        store.ep_chibis.DokiAccessory(_("Hearts"), "hearts", "secondary"),
        store.ep_chibis.DokiAccessory(_("[m_name]'s Cake"), "m_slice_cake", "secondary"),
        store.ep_chibis.DokiAccessory(_("Moustache"), "moustache", "secondary"),
        store.ep_chibis.DokiAccessory(_("Neon Blush"), "neon_blush", "secondary"),
        store.ep_chibis.DokiAccessory(_("Monocle"), "monocle", "secondary"),
        store.ep_chibis.DokiAccessory(_("[player]'s Cake"), "p_slice_cake", "secondary"),
        store.ep_chibis.DokiAccessory(_("Pirate Patch"), "patch", "secondary"),
        store.ep_chibis.DokiAccessory(_("Speech Bubble with Heart"), "speech_bubble", "secondary"),
        store.ep_chibis.DokiAccessory(_("Sunglasses"), "sunglasses", "secondary")
    ]
    background_accessories = [
        store.ep_chibis.DokiAccessory(_("Angel Wings"), "angel_wings", "background"),
        store.ep_chibis.DokiAccessory(_("Balloon Decorations"), "balloon_decorations", "background"),
        store.ep_chibis.DokiAccessory(_("Cat Tail"), "cat_tail", "background"),
        store.ep_chibis.DokiAccessory(_("Fox Tail"), "fox_tail", "background"),
        store.ep_chibis.DokiAccessory(_("Snowflakes"), "snowflakes", "background")
    ]
    notify_frame = store.ep_folders._join_path(store.ep_folders.EP_OTHERS,"notify.png")
    notify_icon = store.ep_folders._join_path(store.ep_folders.EP_OTHERS,"{}_icon.png")

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
default persistent.EP_dynamic_button_text = False
default persistent.EP_button_conditions_key = None
default persistent.EP_button_text = None
default persistent.EP_button_last_update = None
default persistent.EP_fridge_magnets_data = None
default persistent.EP_fridge_last_monika_post = None
#====SFX
define sfx_cup_shuffle = ep_folders._join_path(ep_folders.EP_SFX, "cup_shuffle.ogg")
define sfx_coin_flip = ep_folders._join_path(ep_folders.EP_SFX, "coin_flip_sfx.ogg")
define sfx_maxwell_theme = ep_folders._join_path(ep_folders.EP_SFX, "maxwell_theme.ogg")
define sfx_ttt_cross = ep_folders._join_path(ep_folders.EP_SFX, "ttt_cross.ogg")
define sfx_ttt_circle = ep_folders._join_path(ep_folders.EP_SFX, "ttt_circle.ogg")
define sfx_take_frigde = store.ep_folders._join_path(ep_folders.EP_SFX, "take.ogg")
define sfx_place_fridge = store.ep_folders._join_path(ep_folders.EP_SFX, "place.ogg")
define sfx_doki_heartbeats = store.ep_folders._join_path(ep_folders.EP_SFX, "heartbeats.ogg")
#====Windows Title
default persistent._save_window_title = "Monika After Story   "

init 5 python:
    #====New Monika idle
    extra_no_learning = MASMoniIdleDisp(
        (
            # Broken
            MASMoniIdleExp("6ckc", duration=60, aff_range=(None, mas_aff.BROKEN), tag="broken_exps"),
            # Distressed
            MASMoniIdleExp("6rkc", duration=(5, 10), aff_range=(mas_aff.DISTRESSED, mas_aff.DISTRESSED), tag="dist_exps"),
            MASMoniIdleExp("6lkc", duration=(5, 10), aff_range=(mas_aff.DISTRESSED, mas_aff.DISTRESSED), tag="dist_exps"),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExpRngGroup(
                        [
                            MASMoniIdleExp("6rktpc", duration=(5, 10)), # Replaces 6rktp
                            MASMoniIdleExp("6lktpc", duration=(5, 10))
                        ],
                        max_uses=4
                    ),
                    MASMoniIdleExpRngGroup(
                        [
                            MASMoniIdleExp("6rktdc", duration=(5, 10)),
                            MASMoniIdleExp("6lktdc", duration=(5, 10)) # Replaces 6lktd
                        ]
                    ),
                    MASMoniIdleExp("6dktdc", duration=(3, 5)) # Replaces 6dktd
                ],
                aff_range=(mas_aff.DISTRESSED, mas_aff.DISTRESSED),
                weight=2,
                tag="dist_exps"
            ),
            # Below 0 and Upset
            MASMoniIdleExp("2esc", duration=5, aff_range=(mas_aff.UPSET, mas_aff.NORMAL), conditional="mas_isBelowZero()", weight=None, repeatable=False, tag="below_zero_startup_exps"),
            MASMoniIdleExp("2esc", aff_range=(mas_aff.UPSET, mas_aff.NORMAL), conditional="mas_isBelowZero()", weight=95, tag="below_zero_exps"),
            MASMoniIdleExp("1tsc", aff_range=(mas_aff.UPSET, mas_aff.NORMAL), conditional="mas_isBelowZero()", weight=5, tag="below_zero_exps"), # Reemplazo de 5tsc
            # Normal
            MASMoniIdleExp("1esa", duration=60, aff_range=(mas_aff.NORMAL, mas_aff.NORMAL), conditional="not mas_isBelowZero()", tag="norm_exps"),
            # Happy
            MASMoniIdleExp("1eua", duration=60, aff_range=(mas_aff.HAPPY, mas_aff.HAPPY), tag="happy_exps"),
            # Affectionate
            MASMoniIdleExp("1eubla", duration=(25, 35), aff_range=(mas_aff.AFFECTIONATE, None), weight=10),
            MASMoniIdleExp("1hubsa", duration=(20, 30), aff_range=(mas_aff.AFFECTIONATE, None), weight=10),
            MASMoniIdleExp("1eubsa", duration=(20, 30), aff_range=(mas_aff.AFFECTIONATE, None), weight=10),
            MASMoniIdleExp("1ekblu", duration=(25, 35), aff_range=(mas_aff.AFFECTIONATE, None), weight=5),
            MASMoniIdleExp("1tuu", duration=(20, 30), aff_range=(mas_aff.AFFECTIONATE, None), weight=5),
            MASMoniIdleExp("1mubla", duration=(25, 35), aff_range=(mas_aff.AFFECTIONATE, None), weight=5),

            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=1),
                    MASMoniIdleExp("1sua", duration=4),
                    MASMoniIdleExp("1eua"),
                ],
                aff_range=(mas_aff.AFFECTIONATE, None),
                weight=15,
                tag="idle_star_eyes"
            ),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=1),
                    MASMoniIdleExp("1kua", duration=1),
                    MASMoniIdleExp("1eua"),
                ],
                aff_range=(mas_aff.AFFECTIONATE, None),
                weight=15,
                tag="idle_wink"
            ),
            MASMoniIdleExpRngGroup(
                [
                    MASMoniIdleExp("1eua", weight=70),
                    MASMoniIdleExp("1eua_follow", weight=30)# 30% to follow
                ],
                max_uses=1,
                aff_range=(mas_aff.AFFECTIONATE, mas_aff.AFFECTIONATE),
                weight=70,
                tag="aff_exps"
            ),
            MASMoniIdleExp("1hua", aff_range=(mas_aff.AFFECTIONATE, mas_aff.AFFECTIONATE), weight=15, tag="aff_exps"),
            # Enamored & Love
            MASMoniIdleExp("1eua", duration=5, aff_range=(mas_aff.ENAMORED, None), weight=None, repeatable=False, tag="enam_plus_startup_exps"),
            MASMoniIdleExpRngGroup(
                [
                    MASMoniIdleExp("1eua", weight=50),
                    MASMoniIdleExp("1eua_follow", weight=50)
                ],
                max_uses=1,
                aff_range=(mas_aff.ENAMORED, None),
                weight=60,
                tag="enam_love_no_lean_exps"
            ),
            MASMoniIdleExp("1tsu", aff_range=(mas_aff.ENAMORED, None), weight=15, tag="enam_love_no_lean_exps"),
            MASMoniIdleExp("1huu", aff_range=(mas_aff.ENAMORED, None), weight=15, tag="enam_love_no_lean_exps"),
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

            # Create MAS components internally
            self.cz_manager = mas_interactions.MASClickZoneManager()
            for zone_key, vx_list in self.zone_map.items():
                self.cz_manager.add(zone_key, MASClickZone(vx_list))
            
            self.interactable = MASZoomableInteractable(
                self.cz_manager,
                zone_actions={},  # Actions handled manually
                debug=False
            )
        
        def get_hovered_zone(self):
            """
            Gets the current zone under the mouse.
            """
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
        "extra_head":    [(550, 10), (730, 10), (730, 130), (550, 130)],
        # Nose (small and precise area)
        "extra_nose":    [(618, 235), (648, 235), (648, 265), (618, 265)],
        # Right cheek (Monika's right, screen left)
        "extra_cheek_r": [(675, 256), (715, 256), (715, 296), (675, 296)],
        # Left cheek (Monika's left, screen right)
        "extra_cheek_l": [(570, 256), (610, 256), (610, 296), (570, 296)],
        # Hands (wider area)
        "extra_hands":   [(600, 327), (690, 327), (690, 387), (600, 387)],
        # Right ear
        "extra_ear_r":   [(754, 195), (784, 195), (784, 225), (754, 225)],
        # Left ear
        "extra_ear_l":   [(514, 220), (544, 220), (544, 250), (514, 250)],
    }
    
    # Mapping of zones to actions (primary, alternate)
    # If there is only one action, it can be put as a direct string
    EP_boop_zone_actions = {
        "extra_head": ("monika_headpatbeta", "monika_headpat_long"),
        "extra_nose": ("monika_boopbeta", "monika_boopbeta_war"),
        "extra_cheek_l": ("monika_cheeksbeta", "monika_cheek_squish"), # <-- New secondary action
        "extra_cheek_r": ("monika_cheeksbeta", "monika_cheek_squish"), # <-- New secondary action
        "extra_hands": ("monika_handsbeta", "monika_hand_hold"),     # <-- New secondary action
        "extra_ear_l": ("monika_earsbeta", "monika_ear_rub"),      # <-- New secondary action
        "extra_ear_r": ("monika_earsbeta", "monika_ear_rub"),      # <-- New secondary action
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
    # Migrate old data structures to prevent crashes.
    # store.ep_chibis.migrate_chibi_costume_data()
    # store.ep_files.migrate_window_title_data()

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
        ("EP_acs_chocolatecake", "chocolatecake", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_fruitcake", "fruitcake", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_emptyplate", "emptyplate", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_coffeecup", "coffeecup", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_emptycup", "emptycup", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pasta", "extraplus_spaghetti", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pancakes", "extraplus_pancakes", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_candles", "extraplus_candles", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_icecream", "extraplus_icecream", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_pudding", "extraplus_lecheflanpudding", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_waffles","extraplus_waffles", store.MASPoseMap(default="0", use_reg_for_l=True), True),
        ("EP_acs_flowers", "extraplus_flowers", store.MASPoseMap(default="0", use_reg_for_l=True), True, 2),
        ("EP_acs_remptyplate", "extraplus_remptyplate", store.MASPoseMap(default="0", use_reg_for_l=True), True)
    ]

    for info in extraplus_accessories:
        name = info[0]
        acs = store.MASAccessory(*info)
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
image bg extra_fm = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_FRIDGE, "fridge_background.png"))
image extra_fm_box = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_MG_FRIDGE, "fridge_box.png"))

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
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessories)
    )

image extra_chibi_hover = LiveComposite(
    (188, 188),
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_background_accessories),
    (0, 0), "chibi_hover_effect",
    (0, 0), DynamicDisplayable(store.ep_chibis.draw_foreground_accessories)
    )

image poof_effect = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_OTHERS, "poof.png"), (222, 222), (3, 3), 0.09, loop=False)

#====Coin
image coin_heads = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_OTHERS, "coin_heads.png"))
image coin_tails = MASFilterSwitch(ep_folders._join_path(ep_folders.EP_OTHERS, "coin_tails.png"))
image sprite_coin = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_OTHERS, "sprite_coin.png"), (100, 100), (3, 2), .125, loop=True)
image sprite_coin_n = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_OTHERS, "sprite_coin-n.png"), (100, 100), (3, 2), .125, loop=True)
image coin_moni:
    ConditionSwitch(
        "mas_isDayNow()", "sprite_coin",
        "mas_isNightNow()", "sprite_coin_n")

#====Idle edit
image monika staticpose = extra_no_learning

#====Misc
image maxwell_animation = anim.Filmstrip(ep_folders._join_path(ep_folders.EP_OTHERS, "maxwell_cat.png"), (297, 300), (10, 15), 0.0900, loop=False)

#===========================================================================================
# SCREEN
#===========================================================================================
#=== Buttons ===
screen extraplus_button():
    #Displays the Extra+ button on the overlay. Handles hotkeys and button actions for opening the Extra+ menu.
    zorder 15
    style_prefix "hkb"

    if store.mas_submod_utils.current_label == "mas_piano_setupstart":
        pass

    elif renpy.get_screen("hkb_overlay"):
        vbox: # Main button container
            xpos 0.05
            yanchor 1.0
            ypos 50

            $ buttons_text = _(store.ep_button.getDynamicButtonText())
            textbutton buttons_text action Function(store.ep_button.show_menu) sensitive store.mas_hotkeys.talk_enabled

        if store.mas_hotkeys.talk_enabled:
            key "x" action Function(store.ep_button.show_menu)
            key "a" action Function(store.ep_affection.notify_affection)


screen extraplus_interactions():
    #Shows the main Extra+ interactions menu, letting the player choose between date, minigames, tools, or boop options.
    zorder 50
    style_prefix "hkb"
    vbox: # Main menu container
        xpos 0.05
        yanchor 1.0
        ypos 210

        use extra_close_button()
        textbutton _("Dates") action Jump("extraplus_walk")
        textbutton _("Games") action Jump("extraplus_minigames") sensitive (store.ep_affection.getCurrentAffection() >= 30)
        textbutton _("Tools") action Jump("extraplus_tools")
        textbutton _("Boop") action Jump("show_boop_screen") sensitive (store.ep_affection.getCurrentAffection() >= 100)

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

    vbox:
        key "x" action Jump(jump_action)
        textbutton _("Close") action Jump(jump_action)

#=== Chibis ===
screen doki_chibi_idle():
    #Displays Chibika on the screen, allowing for dragging if enabled.
    zorder 52
    if renpy.get_screen("hkb_overlay"):
        if persistent.enable_drag_chibika:
            drag:
                child "extra_chibi_base"
                selected_hover_child "extra_chibi_hover"
                dragged store.ep_chibis.chibi_drag
                drag_offscreen True
                xpos persistent.chibika_drag_x
                ypos persistent.chibika_drag_y

        else:
            # We use a button instead of a static image
            imagebutton:
                idle "extra_chibi_base"
                # hover "extra_chibi_hover" # Visual feedback (glow/change) on hover
                xpos store.ep_chibis.xpos
                ypos store.ep_chibis.ypos
                action Function(store.ep_chibis.clicker) # Call the secret function
                focus_mask True # Important: Only allows clicks on the figure, not the transparent box


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
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos store.ep_button.zoom_ypos

        if renpy.get_screen("hkb_overlay"):
            textbutton _("Zoom") action Show("extra_custom_zoom") sensitive not (renpy.get_screen("say") or renpy.get_screen("choice") or renpy.get_screen("extra_gen_list"))

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
screen shell_game_minigame():
    #Displays the shell game minigame interface, letting the player pick a cup and quit the game.
    zorder 50
    style_prefix "hkb"
    use extra_no_click()
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="sg") repeat True

    for i in range(3):
        imagebutton:
            xanchor 0.5 yanchor 0.5
            xpos store.ep_sg.cup_coordinates[i]
            ypos 250
            idle "extra_sg_cup_idle"
            hover "extra_sg_cup_hover"
            focus_mask "extra_sg_cup_hover"
            action SGVerification(i, store.ep_sg.ball_position, "sg_check_label")
    
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

screen RPS_mg():
    #Shows the Rock-Paper-Scissors minigame interface, with buttons for each choice and a quit button.
    zorder 50
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="rps") repeat True

    # Monika's card back
    imagebutton idle "extra_card_back":
        action NullAction()
        xalign 0.7
        yalign 0.1

    # Player's choices
    $ x_positions = [0.5, 0.7, 0.9]
    for i, choice in enumerate(ep_rps.choices):
        imagebutton:
            idle choice.image
            hover choice.image at hover_card
            action [SetField(ep_rps, "your_choice", choice.value), Hide("RPS_mg"), Jump("rps_loop")]
            xalign x_positions[i]
            yalign 0.7

    # Quit button
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Quit") style "hkb_button" action Jump("rps_quit")

screen extra_no_click():
    #Disables advancing the dialogue or clicking, used to restrict player input during certain events.
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()

    imagebutton:
        idle "mod_assets/other/transparent.png"
        action NullAction()

screen score_minigame(game=None):
    #Shows the current score for a minigame (RPS or Shell Game) with player and opponent stats.
    key "h" action NullAction()
    key "mouseup_3" action NullAction()
    python:
        if game == "rps":
            first_text = "Monika"
            second_text = player
            first_score = ep_rps.moni_wins
            second_score = ep_rps.player_wins
            
        elif game == "sg":
            first_text = "Turns"
            second_text = "Score"
            first_score = ep_sg.current_turn
            second_score = ep_sg.correct_answers
        
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.025
        text "[first_text] : [first_score]"  size 25 style "monika_text"
        text "[second_text] : [second_score]"  size 25 style "monika_text"

# === Interactions ===
screen boop_revamped():
    zorder 49
    
    timer 900 action Jump("boop_timer_expired") # 15 minute timer
    
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
            text _(" Cheeks\n Head\n Nose\n Ears\n Hands\n"):
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
        interaction_manager = store.EP_interaction_manager
        nose_zone_key = store.mas_interactions.ZONE_EXTRA_NOSE
        current_zoom = store.mas_sprites.zoom_level
        nose_cz = interaction_manager.cz_manager.get(
            nose_zone_key,
            current_zoom
        )

        nose_zone = None
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
    
    if boop_enable:
        use boop_capture_overlay(label_boop)
    
    vbox:
        xpos store.ep_dates.xpos
        yanchor 1.0
        ypos store.ep_dates.ypos
        
        textbutton _("Talk"):
            style "hkb_button"
            action Jump(ask)

screen extra_timer_monika(time):
    #Runs a timer that sets a variable when finished, used for timed events.
    timer time action SetField(store.ep_dates, "stop_snike_time", True)


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
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90
        textbutton _("Close") action NullAction() sensitive False
        textbutton _("Return") action NullAction() sensitive False

    vbox:
        style_prefix "check"
        yanchor 0.5
        xanchor 1.0
        xpos 1.0
        ypos 0.5
        label _("Interactions\navailable:")
        text _(" Cheeks\n Head\n Nose\n Ears\n Hands\n") outlines [(2, "#808080", 0, 0)]

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
    # add "extra_fm_background"
    add EP_fridge_manager.event_handler
    
    # --- Drop Zones ---
    button:
        xysize 535, 375
        offset 200, 20
        background "#fff8"
        action Function(EP_fridge_manager.put, "top")
        
    button:
        xysize 535, 248
        offset 200, 455
        background "#fff8"
        action Function(EP_fridge_manager.put, "bottom")
        
    # --- Magnet Box ---
    button:
        offset 870, 520 
        add "extra_fm_box" zoom 0.70
        background "#fff8"
        action Function(EP_fridge_manager.take)

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
        xpos 0.05
        yanchor 1.0
        ypos 90
        textbutton _("Clean") action Function(EP_fridge_manager.clean_magnets)
        use extra_close_button("extra_fridge_quit")

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

        textbutton _("{b}Enable dynamic button text{/b}"):
            action ToggleField(persistent, "EP_dynamic_button_text")
            hovered tooltip.Action("If enabled, the submod button text will change based on affection, events, or time of day. If disabled, it will always say 'Extra+'.")

        textbutton _("{b}Check for missing files{/b}"):
            action Function(store.ep_files.run_asset_linter)
            hovered tooltip.Action("This will check if all submod files are installed correctly and create a log file in the 'characters' folder.")

        textbutton _("{b}Clean up old files{/b}"):
            action Function(store.ep_files.cleanup_old_files)
            hovered tooltip.Action("This will remove obsolete files and folders from previous versions of the submod.")

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
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURANTE THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

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
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

#====Restaurant (Updated paths)

#Day images
image EP_submod_background_restaurant_day = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "day.png")
image EP_submod_background_restaurant_rain = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain.png")

#Night images
image EP_submod_background_restaurant_night = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "n.png")
image EP_submod_background_restaurant_rain_night = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain-n.png")

#Sunset images
image EP_submod_background_restaurant_ss = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "ss.png")
image EP_submod_background_restaurant_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_RESTAURANT, "rain-ss.png")

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
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURANTE THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

        store.monika_chr.tablechair.table = "extraplus_restaurant"
        store.monika_chr.tablechair.chair = "extraplus_restaurant"


    def _extra_restaurant_exit(_new, **kwargs):
        """
        Exit programming point for restaurant background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

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
    EP_background_extrapool = MASFilterableBackground(
        "EP_background_extrapool",
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
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURANTE THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

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
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

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
    EP_background_extralibrary = MASFilterableBackground(
        "EP_background_extralibrary",
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
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURANTE THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

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
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

#====Arcade (Updated paths)

#Day images
image EP_submod_background_arcade_day = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "day.png")
image EP_submod_background_arcade_rain = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain.png")

#Night images
image EP_submod_background_arcade_night = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "n.png")
image EP_submod_background_arcade_rain_night = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain-n.png")

#Sunset images
image EP_submod_background_arcade_ss = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "ss.png")
image EP_submod_background_arcade_rain_ss = ep_folders._join_path(ep_folders.EP_DATE_ARCADE, "rain-ss.png")

init -1 python:
    EP_background_extra_arcade = MASFilterableBackground(
        "EP_background_extra_arcade",
        "Arcade (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "EP_submod_background_arcade_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "EP_submod_background_arcade_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "EP_submod_background_arcade_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "EP_submod_background_arcade_rain_ss",
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
        entry_pp=store.mas_background._extra_arcade_entry,
        exit_pp=store.mas_background._extra_arcade_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _extra_arcade_entry(_old, **kwargs):
        """
        Entry programming point for arcade background

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURANTE THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """
        if kwargs.get("startup"):
            pass

        else:
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

        store.monika_chr.tablechair.table = "extraplus_arcade"
        store.monika_chr.tablechair.chair = "extraplus_arcade"

    def _extra_arcade_exit(_new, **kwargs):
        """
        Exit programming point for arcade background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"
