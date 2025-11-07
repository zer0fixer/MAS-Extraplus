#===========================================================================================
# SUBMOD
#===========================================================================================

#Submod created by ZeroFixer(u/UnderstandingAny7135), this submod is made for MAS brothers/sisters.
#Shoutout to u/my-otter-self at reddit, who proofread the whole mod.

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
                "README.md"
            )
        )
        
#===========================================================================================
# VARIABLES
#===========================================================================================

#====Menus dialogues
define minigames_talk = [
    _("Choose one, [player]."),
    _("Want a new challenge?"),
    _("I would love to play with you~"),
    _("What will we play today?"),
    _("Let's have some fun!"),
    _("Time to show off your skills!"),
    _("Ready to play?"),
    _("Let's see how good you are!"),
    _("Which game do you want to try?"),
    _("Shall we play a game?"),
    _("I'm feeling lucky today, [player]."),
    _("Are you ready for some fun?"),
    _("Let's see if you can beat me!"),
    _("Time for some friendly competition!"),
    _("I'm up for any game you want to play."),
]

define date_talk = [
    _("I can't wait to see where you take me!"),
    _("What adventures await us today?"),
    _("I'm excited to spend time with you."),
    _("Let's make some great memories today."),
    _("I hope we have a wonderful time together."),
    _("Wherever we go, it will be perfect as long as we're together."),
    _("I'm open to any suggestion you have."),
    _("Let's do something fun and spontaneous!"),
    _("I'm so lucky to have you as my date!"),
    _("I can't wait to make more memories with you today."),
    _("I'm up for anything you want to do!"),
    _("Let's make this a date to remember."),
    _("I feel like today is going to be amazing!"),
    _("Wherever we end up, I'm happy as long as we're together."),
    _("Let's have an unforgettable time today!")
]

#====Boop count
default persistent.plus_boop = [0, 0, 0] #Nose, Cheeks, Headpat.
default boop_war_count = 0
default persistent.extra_boop = [0, 0, 0] #Hands, Ears.

#====Chibika and friends?
define chibi_xpos = 0.05
default chibika_y_position = 345 if store.mas_submod_utils.isSubmodInstalled("Noises Submod") else 385
default dating_ypos_value = 555 if store.mas_submod_utils.isSubmodInstalled("Noises Submod") else 595
default persistent.chibika_drag_x = chibi_xpos
default persistent.chibika_drag_y = 385

# Data structure for chibi outfits
# (Doki Folder, Base Sprite Name, Blink State, Hover State)
define -1 blanket_monika = ("darling", "idle", "blink", "hover")
define -1 blanket_nat = ("cupcake", "idle", "blink", "hover")
define -1 blanket_sayo = ("cinnamon", "idle", "blink", "hover")
define -1 blanket_yuri = ("teacup", "idle", "blink", "hover")
define -1 android_monika = ("darling", "android_idle", "android_blink", "android_hover")
define -1 bikini_monika = ("darling", "bikini_idle", "bikini_blink", "bikini_hover")
define -1 casual_monika = ("darling", "casual_idle", "casual_blink", "casual_hover")
define -1 casual_yuri = ("teacup", "casual_idle", "casual_blink", "casual_hover")
define -1 casual_nat = ("cupcake", "casual_idle", "casual_blink", "casual_hover")
define -1 casual_sayo = ("cinnamon", "casual_idle", "casual_blink", "casual_hover")

default persistent.chibika_current_costume = blanket_monika

define monika_costumes_ = [("Blanket", blanket_monika), ("Android", android_monika), ("Casual", casual_monika)]
define natsuki_costumes_ = [("Blanket", blanket_nat), ("Casual", casual_nat)]
define sayori_costumes_ = [("Blanket", blanket_sayo), ("Casual", casual_sayo)]
define yuri_costumes_ = [("Blanket", blanket_yuri), ("Casual", casual_yuri)]

default -1 persistent.chibi_accessory_1_ = "0nothing"
default -1 persistent.chibi_accessory_2_ = "0nothing"
default -1 persistent.hi_chibika = False
default -1 persistent.enable_drag_chibika = False

default -1 chibi_sprite_path = _ep_join(EP_CHIBIS, "{0}", "{1}.png")
default -1 chibi_accessory_path_0 = _ep_join(EP_CHIBI_ACC_0, "{}.png")
default -1 chibi_accessory_path_1 = _ep_join(EP_CHIBI_ACC_1, "{}.png")

#====ExtraPlus Buttons
define minigames_menu = []
define tools_menu = []
define walk_menu = []

#====Misc
default persistent.extraplus_dynamic_button_text = True
default last_affection_notify_time = 0 # Used for the affection notifier in the button.
default stop_snike_time = False # This variable seems to be a typo, should it be 'stop_snack_time'?
define -1 ep_pictograms_font = _ep_join(EP_OTHERS, "pictograms_icons.ttf")
define -1 ep_affection_icons = _ep_join(EP_OTHERS, "peperrito_faces.ttf")

#====SFX
define sfx_cup_shuffle = _ep_join(EP_SFX, "cup_shuffle.mp3")
define sfx_coin_flip = _ep_join(EP_SFX, "coin_flip_sfx.ogg")
define sfx_maxwell_theme = _ep_join(EP_SFX, "maxwell_theme.ogg")
define sfx_ttt_cross = _ep_join(EP_SFX, "ttt_cross.ogg")
define sfx_ttt_circle = _ep_join(EP_SFX, "ttt_circle.ogg")

default plus_snack_time = None  # Timer for snacks in dates
default extra_plus_random_outcome = None  # Used for various random choices in the submod
define 3 extra_plus_file = _ep_get_game_path(EP_ROOT, "Extra_Plus_Main.rpy")

#====BG (Date locations)
default extra_old_bg = None
default extra_chair = None
default extra_table = None

#====ZOOM
default extra_plus_player_zoom = None

#====Windows Title
define backup_window_title = "Monika After Story   "
default persistent._save_window_title = "Monika After Story   "

#====Comments by moni on standard difficulties

define _plus_complies = [
    _("Well done, [player]!"),
    _("Impressive, keep it up!"),
    _("You're doing great!"),
    _("Fantastic, [player]!"),
    _("Keep it up!"),
    _("You're making progress!"),
    _("Bravo, [player]!"),
    _("Outstanding, [player]!"),
    _("Way to go, [player]!"),
    _("Keep up the good work, [player]!"),
    _("You're doing fantastic!"),
    _("You're doing amazing!"),
]

define _plus_not_met = [
    _("Oh, too bad~"),
    _("It's not that, [player]."),
    _("Try again~"),
    _("Don't get distracted, [player]."),
    _("Keep practicing, [player]."),
    _("You'll get it next time!"),
    _("Better luck next try, [player]."),
    _("Don't give up, [player]!"),
    _("That's not quite it, [player]."),
    _("That wasn't the right answer, [player]."),
    _("Sorry, [player], that's not it."),
    _("Not quite, try focusing a bit more!")
]

init 5 python:
    #====New Monika idle
    extra_no_learning = MASMoniIdleDisp(
        (
            # Broken (how dared you, monster?)
            MASMoniIdleExp("6ckc", duration=60, aff_range=(None, mas_aff.BROKEN), tag="broken_exps"),
            # Distressed
            MASMoniIdleExp("6rkc", duration=(5, 10), aff_range=(mas_aff.DISTRESSED, mas_aff.DISTRESSED), tag="dist_exps"),
            MASMoniIdleExp("6lkc", duration=(5, 10), aff_range=(mas_aff.DISTRESSED, mas_aff.DISTRESSED), tag="dist_exps"),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExpRngGroup(
                        [
                            MASMoniIdleExp("6rktpc", duration=(5, 10)),
                            MASMoniIdleExp("6lktpc", duration=(5, 10))
                        ],
                        max_uses=4
                    ),
                    MASMoniIdleExpRngGroup(
                        [
                            MASMoniIdleExp("6rktdc", duration=(5, 10)),
                            MASMoniIdleExp("6lktdc", duration=(5, 10))
                        ]
                    ),
                    MASMoniIdleExp("6dktdc", duration=(3, 5))
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
            # Enamored & Love (combinados para no usar pose 5)
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
init -1 python:
    import pygame

    # Create a new clickzone map for Extra+ boops
    # NOTE: These are rectangular for simplicity, but can be complex polygons.
    # Using more accurate polygons based on original imagebutton areas.
    extra_plus_cz_map = {
        # Coords from original imagebuttons: (x, y, w, h) -> polygon
        # Head: ("zonetwo", 550, 10, ...) -> zonetwo is 180x120
        "extra_head": [(550, 10), (730, 10), (730, 130), (550, 130)],
        # Nose: ("zoneone", 618, 235, ...) -> zoneone is 30x30
        "extra_nose": [(618, 235), (648, 235), (648, 265), (618, 265)],
        # Right Cheek: ("zonethree", 675, 256, ...) -> zonethree is 40x40
        "extra_cheek_r": [(675, 256), (715, 256), (715, 296), (675, 296)],
        # Left Cheek: ("zonethree", 570, 256, ...)
        "extra_cheek_l": [(570, 256), (610, 256), (610, 296), (570, 296)],
        # Hands: ("zonefour", 600, 327, ...) -> zonefour is 90x60
        "extra_hands": [(600, 327), (690, 327), (690, 387), (600, 387)],
        # Right Ear: ("zoneone", 754, 195, ...)
        "extra_ear_r": [(754, 195), (784, 195), (784, 225), (754, 225)],
        # Left Ear: ("zoneone", 514, 220, ...)
        "extra_ear_l": [(514, 220), (544, 220), (544, 250), (514, 250)],
    }

    # Create a clickzone manager
    extra_plus_boop_cz_manager = mas_interactions.MASClickZoneManager()

    for zone_key, vx_list in extra_plus_cz_map.items():
        extra_plus_boop_cz_manager.add(zone_key, MASClickZone(vx_list))

    # Define actions for each zone (primary and alternate)
    extra_plus_boop_zone_actions = {
        "extra_head": ("monika_headpatbeta", "monika_headpat_long"),
        "extra_nose": ("monika_boopbeta", "monika_boopbeta_war"),
        "extra_cheek_l": "monika_cheeksbeta",
        "extra_cheek_r": "monika_cheeksbeta",
        "extra_hands": "monika_handsbeta",
        "extra_ear_l": "monika_earsbeta",
        "extra_ear_r": "monika_earsbeta",
    }

    # Create the interactable.
    # Instantiate the base MASZoomableInteractable. We only need it for check_over.
    extra_plus_boop_interactable = MASZoomableInteractable(
        extra_plus_boop_cz_manager,
        zone_actions={k: (v[0] if isinstance(v, tuple) else v) for k, v in extra_plus_boop_zone_actions.items()}
    )

init -9 python in mas_interactions:
    # Define zone keys
    ZONE_EXTRA_HEAD = "extra_head"
    ZONE_EXTRA_NOSE = "extra_nose"
    ZONE_EXTRA_CHEEK_L = "extra_cheek_l"
    ZONE_EXTRA_CHEEK_R = "extra_cheek_r"
    ZONE_EXTRA_HANDS = "extra_hands"
    ZONE_EXTRA_EAR_L = "extra_ear_l"
    ZONE_EXTRA_EAR_R = "extra_ear_r"

    def handle_primary_boop_action():
        """
        Handles the primary (left-click) action on a boop zone and jumps if valid.
        """
        x, y = renpy.get_mouse_pos()
        hovered_zone_key = store.extra_plus_boop_interactable.check_over(x, y)

        if hovered_zone_key:
            # During boop war, only the nose is a valid target.
            if store.boop_war_active:
                if hovered_zone_key == ZONE_EXTRA_NOSE:
                    renpy.jump("boopwar_loop")
                # Handle clicks on other zones during boop war
                elif hovered_zone_key == ZONE_EXTRA_HEAD:
                    renpy.jump("extra_headpat_dis")
                elif hovered_zone_key in [ZONE_EXTRA_CHEEK_L, ZONE_EXTRA_CHEEK_R]:
                    renpy.jump("extra_cheeks_dis")
                return # Ignore other zones like hands/ears during war

            # Normal interaction
            action = store.extra_plus_boop_zone_actions.get(hovered_zone_key)
            primary_action = action[0] if isinstance(action, tuple) else action

            if primary_action and renpy.has_label(primary_action):
                renpy.jump(primary_action)

    def handle_alternate_boop_action():
        """
        Checks for an alternate action on the hovered boop zone and jumps if valid.
        This prevents jumping to a 'None' label.
        """
        x, y = renpy.get_mouse_pos()
        hovered_zone_key = store.extra_plus_boop_interactable.check_over(x, y)

        if hovered_zone_key and not store.boop_war_active:
            action = store.extra_plus_boop_zone_actions.get(hovered_zone_key)
            # Check if the action is a tuple and has an alternate action (at index 1)
            if isinstance(action, tuple) and len(action) > 1 and action[1]:
                if action[1] == "monika_boopbeta_war":
                    store.boop_war_active = True
                renpy.jump(action[1])
        # If no valid zone or alternate action, do nothing.
        return

#===========================================================================================
# FOLDERS
#===========================================================================================
init -995 python:
    import os
    # --- Cross-platform path helper functions (adapted from FontSwitcher) ---
    # Moved to the top level of the python block to be accessible by all functions.
    def _ep_normalize_path(path):
        """Normalizes a path by replacing '\\' with '/' for compatibility."""
        return path.replace("\\", "/")

    def _ep_get_game_path(*args):
        """Builds a normalized, absolute path from the 'game' directory."""
        game_dir = _ep_normalize_path(os.path.join(renpy.config.basedir, "game"))
        # Simply joins the game base directory with all provided arguments.
        # The arguments should already be correctly formed relative paths
        # (e.g., using EP_submods_folder or EP_ROOT).
        return _ep_normalize_path(os.path.join(game_dir, *args))
    
    def _ep_join(*args):
        """
        Joins path components and normalizes them.
        Usage: _ep_join("Submods", "ExtraPlus", "dates", "cafe.png")
        """
        return _ep_normalize_path(os.path.join(*args))

    def find_submods_folder(base_path="."):
        for folder in os.listdir(base_path):
            if folder.lower() == "submods" and os.path.isdir(os.path.join(base_path, folder)):
                return folder
        return "Submods"  # Default value if not found

    # Detect 'submods' folder case-insensitively
    EP_submods_folder = find_submods_folder()
    
    # ==========================================
    # SUBMOD BASE PATH DEFINITIONS
    # ==========================================
    
    # Submod root folder
    EP_ROOT = _ep_join(EP_submods_folder, "ExtraPlus")
    
    # Main subfolders
    EP_MINIGAMES = _ep_join(EP_ROOT, "minigames")
    EP_DATES = _ep_join(EP_ROOT, "dates")
    EP_CHIBIS = _ep_join(EP_ROOT, "chibis")
    EP_OTHERS = _ep_join(EP_ROOT, "others")
    EP_SFX = _ep_join(EP_ROOT, "sfx")
    
    # Specific minigames
    EP_MG_SHELLGAME = _ep_join(EP_MINIGAMES, "shellgame")
    EP_MG_RPS = _ep_join(EP_MINIGAMES, "rockpaperscissors")
    EP_MG_BLACKJACK = _ep_join(EP_MINIGAMES, "blackjack")
    EP_MG_TICTACTOE = _ep_join(EP_MINIGAMES, "tictactoe")
    
    # Date folders
    EP_DATE_CAFE = _ep_join(EP_DATES, "cafe")
    EP_DATE_RESTAURANT = _ep_join(EP_DATES, "restaurant")
    EP_DATE_POOL = _ep_join(EP_DATES, "pool")
    EP_DATE_LIBRARY = _ep_join(EP_DATES, "library")
    EP_DATE_ARCADE = _ep_join(EP_DATES, "arcade")
    
    # Chibi subfolders
    EP_CHIBI_ACC_0 = _ep_join(EP_CHIBIS, "accessories_0")
    EP_CHIBI_ACC_1 = _ep_join(EP_CHIBIS, "accessories_1")

#===========================================================================================
# FUNCTIONS
#===========================================================================================
init 5 python:
    import time
    import datetime

    def show_boop_feedback(message, color="#ff69b4"):
        """
        Shows a floating text message on the screen at the mouse position.
        Used for visual feedback during boop interactions.
        """
        t = "boop_notif{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("boop_feedback_notif", msg=message, tag=t, _tag=t, txt_color=color)

    def create_gift_file(filename):
        """
        Creates an empty .gift file in the characters directory.
        
        Args:
            filename (str): The name of the gift file (e.g., "roses.gift").
        """
        filepath = os.path.join(renpy.config.basedir, 'characters', filename)
        with open(filepath, "a"):
            pass  # Just create an empty file

    def migrate_chibi_costume_data():
        """
        Migrates `persistent.chibika_current_costume` between old and new data structures
        to prevent crashes when switching between submod versions.
        """
        # Case 1: Old data (list) exists. Migrate to new format (tuple).
        # This happens when updating from an old version to this one.
        if isinstance(persistent.chibika_current_costume, list):
            persistent.chibika_current_costume = blanket_monika

        # Case 2: New data (tuple) exists, but the game might be running an older script.
        # This handles downgrading from a newer version.
        # We check if the first element is a string, which is characteristic of the new tuple format.
        elif isinstance(persistent.chibika_current_costume, tuple) and isinstance(persistent.chibika_current_costume[0], basestring): # Use 'str' for Python 3 compatibility
            # If it's a tuple with a string, it's the new format.
            # We check if the expected file for the new format exists. If not, we revert.
            if not renpy.loadable(_ep_join(EP_CHIBIS, "darling", "idle.png")):
                persistent.chibika_current_costume = ["sticker_up", "sticker_sleep", "sticker_baka"]

    def make_bday_oki_doki():
        """Creates the 'oki doki' file for Monika's birthday surprise."""
        config.overlay_screens.remove("bday_oki_doki")
        renpy.hide_screen("bday_oki_doki")
        try:
            # Create the 'oki doki' file
            with open(os.path.join(renpy.config.basedir, 'characters', 'oki doki'), 'w') as f:
                pass
            renpy.notify("Everything is ready for the surprise!")
        except Exception as e:
            renpy.notify("Oh no, something went wrong while preparing the decorations.")
        

    def show_bday_screen():
        """Show birthday screen if it's Monika's birthday and files are missing."""
        if not persistent._mas_bday_in_bday_mode or not persistent._mas_bday_visuals:
            config.overlay_screens.append("bday_oki_doki")

    def _get_current_affection_safe():
        """
        Safely gets the current affection by reading directly from persistent.
        This avoids cache issues between the log and the UI.
        
        OUT:
            float - current affection without cache
        """
        try:
            # Read directly from the mod's internal data
            raw_data = store.mas_affection.__get_data()
            
            if raw_data and len(raw_data) > 0:
                return raw_data[0]  # The first element is the affection value
            else:
                # If raw_data is None or empty, use the standard method
                return store._mas_getAffection()
        
        except Exception as e:
            # Fallback silencioso en caso de error
            return store._mas_getAffection()

    def notify_affection():
        """Notify the player of their affection value every 10 seconds."""
        current_time = time.time()
        if current_time - store.last_affection_notify_time >= 10:
            store.last_affection_notify_time = current_time
            current_affection = _get_current_affection_safe()
            renpy.notify("{1} {0} {1}".format(
                int(current_affection), 
                store.get_monika_level_from_value(current_affection)
            ))

    def show_costume_menu(costumes, return_label):
        """Show a menu to select a costume."""
        dokis_items = [SelectDOKI(name, cost) for name, cost in costumes]
        items = [(_("Nevermind"), return_label, 20)]
        renpy.call_screen("extra_gen_list", dokis_items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)

    def get_monika_level_from_value(affection_val):
        """Return Monika's affection level as an icon string."""
        if affection_val >= 1000:
            icon = "\""
        elif affection_val >= 400:
            icon = ";"
        elif affection_val >= 100:
            icon = "2"
        elif affection_val >= 30:
            icon = "#"
        elif affection_val <= -30:
            icon = "%"
        elif affection_val <= -100:
            icon = "8"
        else:
            icon = "/"

        formatted_icon = (
            "{size=+5}{color=#FFFFFF}{font=" + ep_affection_icons + "}" + icon + "{/font}{/color}{/size}"

        )
        return formatted_icon

    def plus_files_exist():
        """Check if the main Extra Plus file exists."""
        return os.path.isfile(os.path.normcase(extra_plus_file))

    def plus_player_gender():
        """Return a string for the player's gender."""
        # Refactored to use a dictionary for a more concise and Pythonic approach.
        return {"M": "boyfriend", "F": "girlfriend"}.get(persistent.gender, "beloved")

    def extra_rng_cup():
        """Randomly select a cup skin."""
        if store.persistent._mas_pm_cares_about_dokis:
            store.sg_cup_skin = renpy.random.choice(sg_cup_list)
        else:
            store.sg_cup_skin = renpy.random.choice(["cup.png", "monika.png"])

    def save_title_windows():
        """Set the window title based on special days or default."""
        # Refactored to use a data-driven approach for better readability and maintenance.
        special_days = [
            (mas_isplayer_bday, " Happy birthday, {}!".format(player)),
            (mas_isMonikaBirthday, " Happy Birthday, {}!".format(persistent._mas_monika_nickname)),
            (mas_isF14, " Happy Valentine's Day, {}!".format(player)),
            (mas_isO31, " Happy Halloween, {}!".format(player)),
            (mas_isD25, " Merry Christmas, {}!".format(player)),
            (mas_isD25Eve, " Merry Christmas Eve, {}!".format(player)),
            (mas_isNYE, " Happy New Year's Eve, {}!".format(player)),
            (mas_isNYD, " Happy New Year, {}!".format(player))
        ]

        for condition, title in special_days:
            if condition():
                config.window_title = title
                return

        config.window_title = persistent._save_window_title

    def Extraplus_show():
        """Show the Extra Plus interactions screen."""
        mas_RaiseShield_dlg()
        extra_button_zoom()
        renpy.invoke_in_new_context(renpy.call_screen, "extraplus_interactions")

    def ExtraButton():
        """Add the Extra Plus button to the overlay if not visible."""
        if not ExtraVisible():
            config.overlay_screens.append("extraplus_button")

    def ExtraVisible():
        """Check if the Extra Plus button is visible."""
        return "extraplus_button" in config.overlay_screens
    
    def extra_init_chibi():
        """Initialize Chibika if enabled in settings."""
        if not extra_visible_chibi():
            config.overlay_screens.append("doki_chibi_idle")

    def extra_visible_chibi():
        """Check if Chibika is currently visible."""
        return "doki_chibi_idle" in config.overlay_screens
        
    def extra_remove_chibi():
        """Remove Chibika from the overlay if visible."""
        if extra_visible_chibi():
            config.overlay_screens.remove("doki_chibi_idle")
            renpy.hide_screen("doki_chibi_idle")

    def add_remv_chibi():
        """Toggle Chibika's visibility."""
        # Refactored to be a proper toggle function.
        if extra_visible_chibi():
            extra_remove_chibi()
        else:
            extra_init_chibi()

    def chibi_drag(drags, drop):
        """Handle Chibika's drag and drop movement."""
        persistent.chibika_drag_x = drags[0].x
        persistent.chibika_drag_y = drags[0].y

    def extra_reset_chibi():
        """Remove and re-add Chibika to reset her position."""
        extra_remove_chibi()
        if not extra_visible_chibi():
            config.overlay_screens.append("doki_chibi_idle")

    def chibi_draw_accessories(st, at):
        """Draw Chibika's accessories as a LiveComposite."""
        objects = LiveComposite(
            (119, 188),
            (0, 0), MASFilterSwitch(chibi_accessory_path_0.format(persistent.chibi_accessory_1_)),
            (0, 0), MASFilterSwitch(chibi_accessory_path_1.format(persistent.chibi_accessory_2_))
            )
        return objects, 0.5

    def extra_visible_zoom():
        """Check if the custom zoom button is visible."""
        return "extrabutton_custom_zoom" in config.overlay_screens

    def extra_button_zoom():
        """Add the custom zoom button if not visible."""
        if not extra_visible_zoom():
            config.overlay_screens.append("extrabutton_custom_zoom")

    def disable_button_zoom(): # This function is now only used to hide the button when exiting menus.
        """Remove the custom zoom button if visible."""
        if extra_visible_zoom():
            config.overlay_screens.remove("extrabutton_custom_zoom")
            renpy.hide_screen("extrabutton_custom_zoom")

    def mas_extra_location(locate=None):
        """Save or load the current room's chair, table, and background."""
        if locate:
            store.extra_chair = store.monika_chr.tablechair.chair
            store.extra_table = store.monika_chr.tablechair.table
            store.extra_old_bg = store.mas_current_background

        else:
            store.monika_chr.tablechair.chair = store.extra_chair
            store.monika_chr.tablechair.table = store.extra_table
            store.mas_current_background = store.extra_old_bg
            
    def extra_seen_background(sorry, extra_label, view_label):
        """Handle affection and label jump based on background seen status."""
        if store.mas_affection._get_aff() < 300:
            renpy.jump(sorry)

        if renpy.seen_label(view_label):
            store.mas_gainAffection(1,bypass=True)
            renpy.jump(extra_label)

        else:
            store.mas_gainAffection(5,bypass=True)
            
    def extra_seen_label(extra_label, view_label):
        """Jump to extra_label if view_label has been seen."""
        if renpy.seen_label(view_label):
            renpy.jump(extra_label)

    def get_formatted_time_since_install():
        """
        Calculates the time since MAS was first run using persistent.sessions
        and returns it as a formatted string.
        """
        if not (persistent.sessions
            and "first_session" in persistent.sessions
            and persistent.sessions["first_session"]
        ):
            return "a wonderful time"

        try:
            start_datetime = persistent.sessions["first_session"]
            start_date = start_datetime.date()
            current_date = datetime.date.today()
            delta = current_date - start_date
            total_days = delta.days

            if total_days < 1:
                return "less than a day, but every second has been incredible!"

            years = total_days // 365
            remaining_days = total_days % 365
            months = remaining_days // 30
            days = remaining_days % 30

            parts = []
            if years > 0:
                parts.append("{0} {1}".format(years, "year" if years == 1 else "years"))
            if months > 0:
                parts.append("{0} {1}".format(months, "month" if months == 1 else "months"))
            if days > 0:
                parts.append("{0} {1}".format(days, "day" if days == 1 else "days"))

            if len(parts) > 1:
                last_part = parts.pop()
                return ", ".join(parts) + " and " + last_part
            elif parts:
                return parts[0]
            else:
                return "a wonderful time"

        except Exception as e:
            return "an unforgettable time"

    def get_total_days_since_install():
            """
            Calculates the total number of days since MAS was first run.
            Returns an integer.
            """
            if not (persistent.sessions
                and "first_session" in persistent.sessions
                and persistent.sessions["first_session"]
            ):
                return 0

            try:
                start_datetime = persistent.sessions["first_session"]
                start_date = start_datetime.date()
                current_date = datetime.date.today()
                delta = current_date - start_date
                return delta.days

            except Exception as e:
                return 0

    def extra_get_mas_stats():
        """
        Collects session stats from MAS by reading the pre-calculated
        persistent data, using friendly display names.
        """
        stats = {}
        
        # Failsafe in case session data has not been created yet
        if not persistent.sessions:
            return {
                "The Day We Met <3": "Not yet recorded",
                "Visits to The Spaceroom": "0",
                "Our Time Together": "N/A",
                "Average Time per Visit": "N/A"
            }

        # --- Get data directly from the persistent object ---
        first_session = persistent.sessions.get("first_session")
        total_playtime = persistent.sessions.get("total_playtime", datetime.timedelta())
        total_sessions = persistent.sessions.get("total_sessions", 0)

        # --- Format data for display with friendly names ---
        stats["The Day We Met <3"] = first_session.strftime("%B %d, %Y") if first_session else "Unknown"
        stats["Visits to The Spaceroom"] = str(total_sessions)
        h, rem = divmod(total_playtime.total_seconds(), 3600)
        m, s = divmod(rem, 60)
        stats["Our Time Together"] = "{:02.0f}h {:02.0f}m".format(h, m)
        if total_sessions > 0:
            avg_playtime = total_playtime / total_sessions
            h_avg, rem_avg = divmod(avg_playtime.total_seconds(), 3600)
            m_avg, s_avg = divmod(rem_avg, 60)
            stats["Average Time per Visit"] = "{:02.0f}h {:02.0f}m".format(h_avg, m_avg)
        else:
            stats["Average Time per Visit"] = "N/A"

        return stats

    def filtered_clipboard_text(allowed_chars):
        """
        Gets text from the clipboard, filters it based on allowed_chars, and returns the result.
        Compatible with Ren'Py 6.99 using pygame.
        Returns the filtered text, or "cancel" if the clipboard is empty or an error occurs.
        """
        import pygame
        try:
            pygame.scrap.init()
            clipboard_bytes = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)

            if clipboard_bytes:
                clipboard_text = clipboard_bytes.decode('utf-8', 'ignore')
                return "".join(char for char in clipboard_text if char in allowed_chars)
            else:
                renpy.notify(_("Your clipboard is empty."))
                return "cancel"
        except Exception as e:
            # Failsafe in case clipboard access is blocked or fails
            renpy.notify(_("Could not access clipboard."))
            return "cancel"

    migrate_chibi_costume_data()
    extra_rng_cup()
    if plus_files_exist():
        ExtraButton()
    
init 999 python:
    if store.persistent.hi_chibika:
        extra_init_chibi()
    else:
        extra_remove_chibi()

    if mas_isMonikaBirthday():
        show_bday_screen()

    save_title_windows()

init -1 python:
    renpy.music.register_channel("maxwellcat", "sfx", True)

#===========================================================================================
# CLASSES
#===========================================================================================
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
                store.sg_cup_choice = self.index

            if self.index == self.check_index:
                store.sg_plus_comment = True
            else:
                store.sg_plus_comment = False

            renpy.jump(self.final_label)

    class extra_minigames:
        """Represents a minigame with a name, label, and optional preparation."""
        def __init__(self, name, label = None, preparation = None):
            self.label = label
            self.name = name
            self.preparation = preparation

        def __call__(self, *args, **kwargs):
            if self.preparation:
                self.preparation(self, *args, **kwargs)
            if self.label and not kwargs.get("restart"):
                renpy.call_in_new_context(self.label)

        def set_state(self, value):
            self.state = value

    class extra_gift:
        """Handles the creation of a gift file and notifies the player."""
        def __init__(self, name, gift):
            self.name = name
            self.gift = gift

        def __call__(self):
            create_gift_file(self.gift)
            messages = [
                _("All set! The '{}' gift is ready for you.").format(self.name),
                _("Here's a '{}' for Monika! I hope she loves it.").format(self.name),
                _("Perfect! Your '{}' is ready for Monika.").format(self.name),
                _("A '{}' for Monika! It's all set.").format(self.name),
                _("Your '{}' gift has been created!").format(self.name),
                _("One '{}' gift, coming right up! It's ready.").format(self.name)
            ]
            renpy.notify(random.choice(messages))
            store.mas_checkReactions()
            renpy.jump('plus_make_gift')

    class DokiAccessory():
        """Represents a Chibika accessory and applies it when called."""
        def __init__(self, name, acc, category):
            self.name = name
            self.acc = acc
            self.category = category

        def __call__(self):
            if self.category == "primary":
                persistent.chibi_accessory_1_ = self.acc
                renpy.jump("sticker_primary")
            else:
                persistent.chibi_accessory_2_ = self.acc
                renpy.jump("sticker_secondary")

    class SelectDOKI():
        """Lets the player select a Chibika costume and applies it."""
        def __init__(self, name, costume):
            self.name = name
            self.costume = costume

        def __call__(self):
            persistent.chibika_current_costume = self.costume
            extra_reset_chibi()
            renpy.jump("extra_dev_mode")

#===========================================================================================
# IMAGES
#===========================================================================================
init python:
    extraplus_accessories = [
        ("extraplus_acs_chocolatecake", "chocolatecake", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_fruitcake", "fruitcake", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_emptyplate", "emptyplate", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_coffeecup", "coffeecup", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_emptycup", "emptycup", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_pasta", "extraplus_spaghetti", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_pancakes", "extraplus_pancakes", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_candles", "extraplus_candles", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_icecream", "extraplus_icecream", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_pudding", "extraplus_lecheflanpudding", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_waffles","extraplus_waffles", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("extraplus_acs_flowers", "extraplus_flowers", MASPoseMap(default="0", use_reg_for_l=True), True, 2),
        ("extraplus_acs_remptyplate", "extraplus_remptyplate", MASPoseMap(default="0", use_reg_for_l=True), True)
    ]

    for info in extraplus_accessories:
        name = info[0]
        acs = MASAccessory(*info)
        vars()[name] = acs
        store.mas_sprites.init_acs(acs)

    class RPSChoice:
        def __init__(self, name, value, image, beats):
            self.name = name
            self.value = value
            self.image = image
            self.beats = beats

    for suit in ["hearts", "diamonds", "clubs", "spades"]:
        for value in range(1, 14):
            renpy.image("card {} {}".format(suit, value), MASFilterSwitch(
                _ep_join(EP_MG_BLACKJACK, suit, "{}.png".format(value))
            ))

#====Rock Paper Scissors
image extra_paper = MASFilterSwitch(_ep_join(EP_MG_RPS, "paper.png"))
image extra_rock = MASFilterSwitch(_ep_join(EP_MG_RPS, "rock.png"))
image extra_scissors = MASFilterSwitch(_ep_join(EP_MG_RPS, "scissors.png"))
image extra_card_back = MASFilterSwitch(_ep_join(EP_MG_RPS, "back.png"))

#====Shell Game
image note_score = MASFilterSwitch(_ep_join(EP_MG_SHELLGAME, "note_score.png"))
image extra_cup = MASFilterSwitch(_ep_join(EP_MG_SHELLGAME, "{}".format(sg_cup_skin)))
image extra_cup_hover = MASFilterSwitch(_ep_join(EP_MG_SHELLGAME, "cup_hover.png"))
image extra_cup_idle = im.Scale("mod_assets/other/transparent.png", 200, 260)
image extra_ball = MASFilterSwitch(_ep_join(EP_MG_SHELLGAME, "ball.png"))

#====Tic-Tac-Toe
image extra_notebook = MASFilterSwitch(_ep_join(EP_MG_TICTACTOE, "notebook.png"))
image extra_line_black = MASFilterSwitch(_ep_join(EP_MG_TICTACTOE, "line.png"))
image extra_line_player = MASFilterSwitch(_ep_join(EP_MG_TICTACTOE, "player.png"))
image extra_line_moni = MASFilterSwitch(_ep_join(EP_MG_TICTACTOE, "monika.png"))

#====Blackjack-21
image bjcard back = MASFilterSwitch(_ep_join(EP_MG_BLACKJACK, "back.png"))
image bg desk_21 = MASFilterSwitch(_ep_join(EP_MG_BLACKJACK, "background.png"))
image bj_name_plate = MASFilterSwitch(_ep_join(EP_MG_BLACKJACK, "name.png"))
image bj_notescore = MASFilterSwitch(_ep_join(EP_MG_BLACKJACK, "score.png"))

#====Chibi
image chibi_blink_effect:
    block:
        MASFilterSwitch(chibi_sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[1]))
        block:
            choice:
                3
            choice:
                5
            choice:
                7
        MASFilterSwitch(chibi_sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[2]))
        choice 0.02:
            block:
                choice:
                    8
                choice:
                    6
                choice:
                    4
                MASFilterSwitch(chibi_sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[1]))
        choice 0.098:
            pass
        0.06
        repeat

image chibi_hover_effect:
    block:
        MASFilterSwitch(chibi_sprite_path.format(persistent.chibika_current_costume[0], persistent.chibika_current_costume[3]))

image extra_chibi_base = LiveComposite(
    (119, 188),
    (0, 40), "chibi_blink_effect",
    (0, 0), DynamicDisplayable(chibi_draw_accessories)
    )

image extra_chibi_hover = LiveComposite(
    (119, 188), 
    (0, 40), "chibi_hover_effect",
    (0, 0), DynamicDisplayable(chibi_draw_accessories)
    )

#====Coin
image coin_heads = MASFilterSwitch(_ep_join(EP_OTHERS, "coin_heads.png"))
image coin_tails = MASFilterSwitch(_ep_join(EP_OTHERS, "coin_tails.png"))
image sprite_coin = anim.Filmstrip(_ep_join(EP_OTHERS, "sprite_coin.png"), (100, 100), (3, 2), .125, loop=True)
image sprite_coin_n = anim.Filmstrip(_ep_join(EP_OTHERS, "sprite_coin-n.png"), (100, 100), (3, 2), .125, loop=True)
image coin_moni:
    ConditionSwitch(
        "mas_isDayNow()", "sprite_coin",
        "mas_isNightNow()", "sprite_coin_n")

#====Boop
image zoneone = im.Scale("mod_assets/other/transparent.png", 30, 30)
image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)
image zonethree = im.Scale("mod_assets/other/transparent.png", 40, 40)
image zonefour = im.Scale("mod_assets/other/transparent.png", 90, 60)

#====Idle edit
image monika staticpose = extra_no_learning

#====Misc
image maxwell_animation = anim.Filmstrip(_ep_join(EP_OTHERS, "maxwell_cat.png"), (297, 300), (10, 15), 0.0900, loop=False)

#===========================================================================================
# SCREEN
#===========================================================================================
screen extraplus_button():
    #Displays the Extra+ button on the overlay. Handles hotkeys and button actions for opening the Extra+ menu.
    zorder 15
    style_prefix "hkb"

    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 50

        $ buttons_text = _(get_dynamic_button_text())
        if renpy.get_screen("hkb_overlay"):
            if mas_hotkeys.talk_enabled:
                key "a" action Function(notify_affection)
                key "x" action Function(Extraplus_show)
                textbutton buttons_text action Function(Extraplus_show)
            elif mas_submod_utils.current_label == "mas_piano_setupstart":
                text _("")
            else:
                textbutton buttons_text

screen extraplus_interactions():
    #Shows the main Extra+ interactions menu, letting the player choose between date, minigames, tools, or boop options.
    zorder 50
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 210

        use extra_close_button("close_extraplus")
        textbutton _("Dates") action Jump("extraplus_walk")
        textbutton _("Games") action If(mas_affection._get_aff() >= 30, true=Jump("extraplus_minigames"), false=NullAction())
        textbutton _("Tools") action Jump("extraplus_tools")
        textbutton _("Boop") action If(mas_affection._get_aff() >= 30, true=Jump("show_boop_screen"), false=NullAction())

#====GAME
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
                    textbutton _("Show/Hide") action Function(add_remv_chibi)

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
                    label _("Head Accessories:")
                    textbutton _("Select") action Jump("sticker_primary")
                vbox:
                    label _("F/B Accessories:")
                    textbutton _("Select") action Jump("sticker_secondary")

            null height 10

screen boop_revamped():
    #Displays the boop interaction menu, showing available zones (cheeks, head, nose, ears, hands) and related actions.
    zorder 49

    timer 900 action Jump("boop_timer_expired")

    # This transparent button catches all mouse events.
    imagebutton idle "mod_assets/other/transparent.png" action NullAction()

    key "mouseup_1" action Function(mas_interactions.handle_primary_boop_action)
    key "mouseup_3" action Function(mas_interactions.handle_alternate_boop_action)

    vbox:
        style_prefix "check"
        yanchor 0.5
        xanchor 1.0
        xpos 1.0
        ypos 0.5
        if not boop_war_active:
            label _("Interactions\navailable:")
            text _(" Cheeks\n Head\n Nose\n Ears\n Hands\n") outlines [(2, "#808080", 0, 0)]

    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        use extra_close_button("close_boop_screen")
        textbutton _("Return") action Jump("return_boop_screen")

screen extrabutton_custom_zoom():
    #Shows a button to open the custom zoom menu if the overlay is active.
    zorder 51
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
            ypos 595
        else:
            ypos 635

        if renpy.get_screen("hkb_overlay"):
            # El botón se desactiva (atenúa) automáticamente si la pantalla de diálogo 'say' está visible.
            # Usamos renpy.get_screen("say"), que es compatible con versiones antiguas de Ren'Py.
            textbutton _("Zoom") action Show("extra_custom_zoom") sensitive not renpy.get_screen("say")

screen extra_custom_zoom():
    #Provides a custom zoom slider and reset button for adjusting the game’s zoom level.
    use extra_no_click()
    zorder 52
    frame:
        area (0, 0, 1280, 720)
        background Solid("#0000007F")

        textbutton _("Close"):
            if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
                area (60, 556, 120, 35)
            else:
                area (60, 596, 120, 35)
            style "hkb_button"
            action [SetField(store, "extra_plus_player_zoom", store.mas_sprites.zoom_level), Hide("extra_custom_zoom")]

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

screen shell_game_minigame():
    #Displays the shell game minigame interface, letting the player pick a cup and quit the game.
    zorder 50
    style_prefix "hkb"
    use extra_no_click()
    
    for i in range(3):
        imagebutton:
            xanchor 0.5 yanchor 0.5
            xpos sg_cup_coordinates[i]
            ypos 250
            idle "extra_sg_cup_idle"
            hover "extra_sg_cup_hover"
            focus_mask "extra_sg_cup_hover"
            action SGVerification(i, sg_ball_position, "sg_check_label")
    
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

screen RPS_mg():
    #Shows the Rock-Paper-Scissors minigame interface, with buttons for each choice and a quit button.
    zorder 50

    # Monika's card back
    imagebutton idle "extra_card_back":
        action NullAction()
        xalign 0.7
        yalign 0.1

    # Player's choices
    $ x_positions = [0.5, 0.7, 0.9]
    for i, choice in enumerate(extra_rps_choices):
        imagebutton:
            idle choice.image
            hover choice.image at hover_card
            action [SetVariable("rps_your_choice", choice.value), Hide("RPS_mg"), Jump("rps_loop")]
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

screen doki_chibi_idle():
    #Displays Chibika on the screen, allowing for dragging if enabled.
    zorder 52
    if renpy.get_screen("hkb_overlay"):
        if persistent.enable_drag_chibika:
            drag:
                child "extra_chibi_base"
                selected_hover_child "extra_chibi_hover"
                dragged chibi_drag
                drag_offscreen True
                xpos persistent.chibika_drag_x
                ypos persistent.chibika_drag_y
        else:
            add "extra_chibi_base":
                xpos chibi_xpos
                ypos chibika_y_position

screen score_minigame(game=None):
    #Shows the current score for a minigame (RPS or Shell Game) with player and opponent stats.
    key "h" action NullAction()
    key "mouseup_3" action NullAction()
    python:
        if game == "rps":
            first_text = "Monika"
            second_text = player
            first_score = store.extra_moni_wins
            second_score = store.extra_player_wins
            
        elif game == "sg":
            first_text = "Turns"
            second_text = "Score"
            first_score = store.sg_current_turn
            second_score = store.sg_correct_answers
        
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.025
        text "[first_text] : [first_score]"  size 25 style "monika_text"
        text "[second_text] : [second_score]"  size 25 style "monika_text"


screen extra_gen_list(extra_list, extra_area, others, close=None):
    #Generates a scrollable menu from a list, used for dynamic option lists in the submod.
    zorder 50
    style_prefix "scrollable_menu"
    fixed:
        area extra_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "viewport"
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
            value YScrollValue("viewport")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

    if close:
        vbox:
            xpos 0.097
            yanchor 1.0
            ypos 50
            use extra_close_button("close_extraplus")

screen dating_loop(ask, label_boop, boop_enable=False):
    #Displays a simple menu for dating events, with a talk button and optional boop interaction.
    zorder 51
    vbox:
        xpos 0.05 yanchor 1.0
        ypos dating_ypos_value
        textbutton _("Talk") style "hkb_button" action Jump(ask)

    #Noise
    if boop_enable == True:
        imagebutton:
            idle "zoneone"
            xpos 620 ypos 235
            action Jump(label_boop)

screen extra_timer_monika(time):
    #Runs a timer that sets a variable when finished, used for timed events.
    timer time action SetVariable("stop_snike_time", True)


screen boop_event(timelock, endlabel, editlabel):
    #Handles the boop war event, showing interactive zones and a score counter.
    timer timelock action Jump(endlabel)
    zorder 50

    # This transparent button ensures the screen can receive key events.
    imagebutton idle "mod_assets/other/transparent.png" action NullAction()

    # Use the same logic as the main boop screen to handle clicks.
    # The handle_primary_boop_action function already knows what to do when boop_war_active is True.
    key "mouseup_1" action Function(mas_interactions.handle_primary_boop_action)

screen force_mouse_move():
    #Forces the mouse to move to a specific position, used for certain effects or minigames.
    on "show":
        action MouseMove(x=412, y=237, duration=.3)
    timer .6 repeat True action MouseMove(x=412, y=237, duration=.3)

screen boop_war_score_ui():
    #Displays the score counter for the boop war.
    zorder 51
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.045
        text _("Boops : [boop_war_count]") size 25 style "monika_text"

screen bday_oki_doki():
    #Shows a special button for Monika’s birthday event.
    zorder 150
    style_prefix "hkb"
    vbox:
        xpos 590
        ypos 0.9
        if mas_submod_utils.current_label == "mas_dockstat_empty_desk_from_empty":
            textbutton _("Oki Doki") action Function(make_bday_oki_doki)

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

        use extra_close_button("close_extraplus")
        textbutton _("Return") action Jump("extraplus_tools")

    frame:
        style_prefix "check"
        xalign 0.92
        yalign 0.5
        padding (40, 20, 40, 50)
        xmaximum 500
        ymaximum 650

        has vbox:
            spacing 30
            label _("Your Time with [m_name]"):
                xalign 0.5
            vbox:
                xfill True
                spacing 30
                python:
                    stats_data = extra_get_mas_stats()
                for stat_name, stat_value in stats_data.items():
                    vbox:
                        xfill True
                        text stat_name
                        text str(stat_value)

screen _extra_plus_submod_settings():
    # Displays the settings pane for the Extra+ submod in the MAS settings menu.
    $ tooltip = renpy.get_screen("submods", "screens").scope["tooltip"]

    vbox:
        style_prefix "check"
        box_wrap False
        xfill True
        xmaximum 1000

        textbutton _("{b}Enable dynamic button text{/b}"):
            action ToggleField(persistent, "extraplus_dynamic_button_text")
            hovered tooltip.Action("If enabled, the submod button text will change based on affection, events, or time of day. If disabled, it will always say 'Extra+'.")

        textbutton _("{b}Check for missing files{/b}"):
            action Function(extra_plus_asset_linter)
            hovered tooltip.Action("This will check if all submod files are installed correctly and create a log file in the 'characters' folder.")

        textbutton _("{b}Clean up old files{/b}"):
            action Function(extra_plus_cleanup_old_files)
            hovered tooltip.Action("This will remove obsolete files and folders from previous versions of the submod.")

screen boop_feedback_notif(msg, tag, txt_color):
    zorder 2000
    timer 1.3 action Hide(tag)
    default p = renpy.get_mouse_pos()
    text "{}".format(msg) at boop_feedback_trans pos p size 30 color txt_color outlines [ (2, "#000", 0, 0) ]

# screen boop_feedback_notif(msg, tag, txt_color):
#     zorder 2000
#     timer 1.3 action Hide(tag)
#     default p = renpy.get_mouse_pos()
#     text "{}".format(msg) at boop_feedback_trans pos p size 40 color txt_color outlines [ (1, "#000", 0, 0) ] style "monika_text"

screen extra_close_button(jump_action="close_extraplus"):
    zorder 51
    style_prefix "hkb"

    vbox:
        key "x" action Jump(jump_action)
        textbutton _("Close") action Jump(jump_action)

#===========================================================================================
# TRANSFORM
#===========================================================================================

transform boop_feedback_trans:
    parallel:
        ease 1.2 yoffset -150
    parallel:
        pause 0.1
        ease 1.1 alpha 0

transform monika_card_flip:
    yzoom -1.0

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
    
#===========================================================================================
# BACKGROUNG
#===========================================================================================

#====Cafe

#Day images
image submod_background_cafe_day = _ep_join(EP_DATE_CAFE, "cafe_day.png")
image submod_background_cafe_rain = _ep_join(EP_DATE_CAFE, "cafe_rain.png")

#Night images
image submod_background_cafe_night = _ep_join(EP_DATE_CAFE, "cafe-n.png")
image submod_background_cafe_rain_night = _ep_join(EP_DATE_CAFE, "cafe_rain-n.png")

#Sunset images
image submod_background_cafe_ss = _ep_join(EP_DATE_CAFE, "cafe-ss.png")
image submod_background_cafe_rain_ss = _ep_join(EP_DATE_CAFE, "cafe_rain-ss.png")

init -1 python:
    submod_background_cafe = MASFilterableBackground(
        "submod_background_cafe",
        "Cafe (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_rain_ss",
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

#====Restaurant (Rutas actualizadas)

#Day images
image submod_background_extraplus_restaurant_day = _ep_join(EP_DATE_RESTAURANT, "restaurant_day.png")
image submod_background_extraplus_restaurant_rain = _ep_join(EP_DATE_RESTAURANT, "restaurant_rain.png")

#Night images
image submod_background_extraplus_restaurant_night = _ep_join(EP_DATE_RESTAURANT, "restaurant-n.png")
image submod_background_extraplus_restaurant_rain_night = _ep_join(EP_DATE_RESTAURANT, "restaurant_rain-n.png")

#Sunset images
image submod_background_extraplus_restaurant_ss = _ep_join(EP_DATE_RESTAURANT, "restaurant-ss.png")
image submod_background_extraplus_restaurant_rain_ss = _ep_join(EP_DATE_RESTAURANT, "restaurant_rain-ss.png")

init -1 python:
    submod_background_restaurant = MASFilterableBackground(
        "submod_background_restaurant",
        "Restaurant (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplus_restaurant_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplus_restaurant_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplus_restaurant_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplus_restaurant_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplus_restaurant_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplus_restaurant_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplus_restaurant_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplus_restaurant_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplus_restaurant_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplus_restaurant_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplus_restaurant_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplus_restaurant_rain_ss",
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

#====Pool (Rutas actualizadas)

#Day images
image submod_background_extrapool_day = _ep_join(EP_DATE_POOL, "pool_day.png")
image submod_background_extrapool_rain = _ep_join(EP_DATE_POOL, "pool_rain.png")

#Night images
image submod_background_extrapool_night = _ep_join(EP_DATE_POOL, "pool-n.png")
image submod_background_extrapool_rain_night = _ep_join(EP_DATE_POOL, "pool_rain-n.png")

#Sunset images
image submod_background_extrapool_ss = _ep_join(EP_DATE_POOL, "pool-ss.png")
image submod_background_extrapool_rain_ss = _ep_join(EP_DATE_POOL, "pool_rain-ss.png")

init -1 python:
    submod_background_extrapool = MASFilterableBackground(
        "submod_background_extrapool",
        "Pool (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extrapool_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extrapool_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extrapool_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extrapool_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extrapool_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extrapool_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extrapool_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extrapool_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extrapool_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extrapool_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extrapool_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extrapool_rain_ss",
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

#====Library (Rutas actualizadas)

#Day images
image submod_background_extralibrary_day = _ep_join(EP_DATE_LIBRARY, "library_day.png")
image submod_background_extralibrary_rain = _ep_join(EP_DATE_LIBRARY, "library_rain.png")

#Night images
image submod_background_extralibrary_night = _ep_join(EP_DATE_LIBRARY, "library-n.png")
image submod_background_extralibrary_rain_night = _ep_join(EP_DATE_LIBRARY, "library_rain-n.png")

#Sunset images
image submod_background_extralibrary_ss = _ep_join(EP_DATE_LIBRARY, "library-ss.png")
image submod_background_extralibrary_rain_ss = _ep_join(EP_DATE_LIBRARY, "library_rain-ss.png")

init -1 python:
    submod_background_extralibrary = MASFilterableBackground(
        "submod_background_extralibrary",
        "Library (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extralibrary_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extralibrary_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extralibrary_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extralibrary_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extralibrary_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extralibrary_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extralibrary_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extralibrary_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extralibrary_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extralibrary_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extralibrary_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extralibrary_rain_ss",
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

#====Arcade (Rutas actualizadas)

#Day images
image submod_background_extra_arcade_day = _ep_join(EP_DATE_ARCADE, "arcade_day.png")
image submod_background_extra_arcade_rain = _ep_join(EP_DATE_ARCADE, "arcade_rain.png")

#Night images
image submod_background_extra_arcade_night = _ep_join(EP_DATE_ARCADE, "arcade-n.png")
image submod_background_extra_arcade_rain_night = _ep_join(EP_DATE_ARCADE, "arcade_rain-n.png")

#Sunset images
image submod_background_extra_arcade_ss = _ep_join(EP_DATE_ARCADE, "arcade-ss.png")
image submod_background_extra_arcade_rain_ss = _ep_join(EP_DATE_ARCADE, "arcade_rain-ss.png")

init -1 python:
    submod_background_extra_arcade = MASFilterableBackground(
        "submod_background_extra_arcade",
        "Arcade (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extra_arcade_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extra_arcade_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extra_arcade_rain",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extra_arcade_rain",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extra_arcade_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extra_arcade_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extra_arcade_rain_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extra_arcade_rain_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extra_arcade_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extra_arcade_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extra_arcade_rain_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extra_arcade_rain_ss",
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


#===========================================================================================
# DEBUGGING
#===========================================================================================

init -2 python:
    def extra_plus_asset_linter():
        """
        Checks for the existence of all defined image assets and creates a log file.
        This is a debug tool and should not be in the final release.
        """
        import os
        import datetime

        # --- Helper function to check files ---
        def check_file(path, found_list, missing_list):
            full_path = _ep_get_game_path(path)
            if os.path.isfile(full_path):
                found_list.append(path)
            else:
                missing_list.append(path)

        # --- Lists to store results ---
        found_assets = []
        missing_assets = []

        # --- 1. Static and Minigame Assets ---
        static_assets = [
            # Shell Game
            _ep_join(EP_MG_SHELLGAME, "note_score.png"),
            _ep_join(EP_MG_SHELLGAME, "cup_hover.png"),
            _ep_join(EP_MG_SHELLGAME, "ball.png"),
            _ep_join(EP_MG_SHELLGAME, "cup.png"),
            _ep_join(EP_MG_SHELLGAME, "monika.png"),
            _ep_join(EP_MG_SHELLGAME, "yuri.png"),
            _ep_join(EP_MG_SHELLGAME, "natsuki.png"),
            _ep_join(EP_MG_SHELLGAME, "sayori.png"),
            # Tic-Tac-Toe
            _ep_join(EP_MG_TICTACTOE, "notebook.png"),
            _ep_join(EP_MG_TICTACTOE, "line.png"),
            _ep_join(EP_MG_TICTACTOE, "player.png"),
            _ep_join(EP_MG_TICTACTOE, "monika.png"),
            # Rock, Paper, Scissors
            _ep_join(EP_MG_RPS, "paper.png"),
            _ep_join(EP_MG_RPS, "rock.png"),
            _ep_join(EP_MG_RPS, "scissors.png"),
            _ep_join(EP_MG_RPS, "back.png"),
            # Blackjack
            _ep_join(EP_MG_BLACKJACK, "back.png"),
            _ep_join(EP_MG_BLACKJACK, "background.png"),
            _ep_join(EP_MG_BLACKJACK, "name.png"),
            _ep_join(EP_MG_BLACKJACK, "score.png"),
            # Misc
            _ep_join(EP_OTHERS, "coin_heads.png"),
            _ep_join(EP_OTHERS, "coin_tails.png"),
            _ep_join(EP_OTHERS, "sprite_coin.png"),
            _ep_join(EP_OTHERS, "maxwell_cat.png"),
            # Date Tables & Chairs
            "mod_assets/monika/t/chair-extraplus_cafe.png",
            "mod_assets/monika/t/table-extraplus_cafe.png",
            "mod_assets/monika/t/table-extraplus_cafe-s.png",
            "mod_assets/monika/t/chair-extraplus_restaurant.png",
            "mod_assets/monika/t/table-extraplus_restaurant.png",
            "mod_assets/monika/t/table-extraplus_restaurant-s.png",
        ]
        for asset in static_assets:
            check_file(asset, found_assets, missing_assets)

        # --- 2. Chibi Assets ---
        all_chibi_costumes = store.monika_costumes_ + store.natsuki_costumes_ + store.sayori_costumes_ + store.yuri_costumes_
        for _, costume_data in all_chibi_costumes:
            doki_folder, idle_sprite, blink_sprite, hover_sprite = costume_data # No store prefix here, these are local to the loop
            chibi_sprites = [idle_sprite, blink_sprite, hover_sprite]
            for sprite in chibi_sprites:
                path = _ep_join(EP_CHIBIS, doki_folder, "{}.png".format(sprite))
                check_file(path, found_assets, missing_assets)

        # --- 3. Chibi Accessories ---
        # NOTE: These are hardcoded based on the lists in Extra_Plus_Misc.rpy
        primary_accessories = ['cat_ears', 'christmas_hat', 'demon_horns', 'flowers_crown', 'halo', 'heart_headband', 'hny', 'neon_cat_ears', 'party_hat', 'rabbit_ears', 'witch_hat']
        secondary_accessories = ['black_bow_tie', 'christmas_tree', 'cloud', 'coffee', 'pumpkin', 'hearts', 'm_slice_cake', 'moustache', 'neon_blush', 'p_slice_cake', 'patch', 'speech_bubble', 'sunglasses']

        for acc in primary_accessories:
            path = _ep_join(EP_CHIBI_ACC_0, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)
        for acc in secondary_accessories:
            path = _ep_join(EP_CHIBI_ACC_1, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)

        # --- 4. Backgrounds (Manual List) ---
        background_assets = [
            # Cafe
            _ep_join(EP_DATE_CAFE, "cafe_day.png"),
            _ep_join(EP_DATE_CAFE, "cafe_rain.png"),
            _ep_join(EP_DATE_CAFE, "cafe-n.png"),
            _ep_join(EP_DATE_CAFE, "cafe_rain-n.png"),
            _ep_join(EP_DATE_CAFE, "cafe-ss.png"),
            _ep_join(EP_DATE_CAFE, "cafe_rain-ss.png"),
            # Restaurant
            _ep_join(EP_DATE_RESTAURANT, "restaurant_day.png"),
            _ep_join(EP_DATE_RESTAURANT, "restaurant_rain.png"),
            _ep_join(EP_DATE_RESTAURANT, "restaurant-n.png"),
            _ep_join(EP_DATE_RESTAURANT, "restaurant_rain-n.png"),
            _ep_join(EP_DATE_RESTAURANT, "restaurant-ss.png"),
            _ep_join(EP_DATE_RESTAURANT, "restaurant_rain-ss.png"),
            # Pool
            _ep_join(EP_DATE_POOL, "pool_day.png"),
            _ep_join(EP_DATE_POOL, "pool_rain.png"),
            _ep_join(EP_DATE_POOL, "pool-n.png"),
            _ep_join(EP_DATE_POOL, "pool_rain-n.png"),
            _ep_join(EP_DATE_POOL, "pool-ss.png"),
            _ep_join(EP_DATE_POOL, "pool_rain-ss.png"),
            # Library
            # _ep_join(EP_DATE_LIBRARY, "library_day.png"),
            # _ep_join(EP_DATE_LIBRARY, "library_rain.png"),
            # _ep_join(EP_DATE_LIBRARY, "library-n.png"),
            # _ep_join(EP_DATE_LIBRARY, "library_rain-n.png"),
            # _ep_join(EP_DATE_LIBRARY, "library-ss.png"),
            # _ep_join(EP_DATE_LIBRARY, "library_rain-ss.png"),
            # Arcade
            # _ep_join(EP_DATE_ARCADE, "arcade_day.png"),
            # _ep_join(EP_DATE_ARCADE, "arcade_rain.png"),
            # _ep_join(EP_DATE_ARCADE, "arcade-n.png"),
            # _ep_join(EP_DATE_ARCADE, "arcade_rain-n.png"),
            # _ep_join(EP_DATE_ARCADE, "arcade-ss.png"),
            # _ep_join(EP_DATE_ARCADE, "arcade_rain-ss.png"),
        ]
        for asset in background_assets:
            check_file(asset, found_assets, missing_assets)

        # --- 5. Blackjack Cards ---
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(1, 14):
                path = _ep_join(EP_MG_BLACKJACK, suit, "{}.png".format(value))
                check_file(path, found_assets, missing_assets)

        # --- 6. Date Accessories ---
        # This list is defined in Extra_Plus_Main.rpy
        for acs_tuple in store.extraplus_accessories:
            acs_name = acs_tuple[1]
            path = "mod_assets/monika/a/{}/0.png".format(acs_name)
            check_file(path, found_assets, missing_assets)

        # --- 6. Write Log File ---
        log_path = _ep_normalize_path(os.path.join(renpy.config.basedir, 'characters', 'extra_plus_asset_log.txt'))
        try:
            with open(log_path, 'w') as f:
                f.write("Extra+ Asset Linter Report - {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                f.write("="*80 + "\n\n")

                if not missing_assets:
                    f.write("SUCCESS: All {} assets were found!\n".format(len(found_assets)))
                else:
                    f.write("ERROR: Found {} missing assets.\n".format(len(missing_assets)))
                    f.write("-" * 30 + "\n")
                    for asset in missing_assets:
                        f.write("MISSING: {}\n".format(asset))

                f.write("\n\n")
                f.write("--- Found Assets ({}) ---\n".format(len(found_assets)))
                for asset in found_assets:
                    f.write("FOUND: {}\n".format(asset))

            renpy.notify("Asset check complete. See extra_plus_asset_log.txt in /characters.")

        except Exception as e:
            renpy.notify("Failed to write asset log: {}".format(e))

    def extra_plus_cleanup_old_files():
        """
        Deletes obsolete files and folders from previous versions of the submod.
        """
        import os
        import shutil

        files_deleted = 0
        folders_deleted = 0
        errors = []

        def delete_file(path):
            """Safely deletes a file and logs the result."""
            full_path = _ep_get_game_path(path)
            if os.path.isfile(full_path):
                try:
                    os.remove(full_path)
                    return 1
                except Exception as e:
                    errors.append("Failed to delete file {}: {}".format(_ep_normalize_path(path), e))
            return 0

        def delete_folder(path):
            """Safely deletes a folder and its contents, and logs the result."""
            full_path = _ep_get_game_path(path)
            if os.path.isdir(full_path):
                try:
                    shutil.rmtree(full_path)
                    return 1
                except Exception as e:
                    errors.append("Failed to delete folder {}: {}".format(_ep_normalize_path(path), e))
            return 0

        # 1. Delete old folder (relative to EP_ROOT)
        folders_deleted += delete_folder(_ep_join(EP_ROOT, "submod_assets"))

        # 2. Delete old table/chair assets (relative to game directory)
        table_chair_files = [
            "mod_assets/monika/t/chair-submod_cafe.png",
            "mod_assets/monika/t/chair-submod_restaurant.png",
            "mod_assets/monika/t/table-submod_cafe.png",
            "mod_assets/monika/t/table-submod_cafe-s.png",
            "mod_assets/monika/t/table-submod_restaurant.png",
            "mod_assets/monika/t/table-submod_restaurant-s.png"
        ]
        for f in table_chair_files:
            files_deleted += delete_file(f)
        
        # 3. Delete old accessory files (relative to game directory)
        for acs_tuple in store.extraplus_accessories:
            acs_file_name_base = acs_tuple[1]
            files_deleted += delete_file("mod_assets/monika/a/acs-{}-0.png".format(acs_file_name_base))

        # --- Final Notification ---
        if files_deleted > 0 or folders_deleted > 0:
            renpy.notify("Cleanup complete! Removed {} files and {} folders.".format(files_deleted, folders_deleted))
        else:
            renpy.notify("No old files or folders were found to clean up.")

        if errors:
            renpy.notify("Some errors occurred during cleanup. Please check the logs.")
