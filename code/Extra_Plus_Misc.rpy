# Extra+ Miscellaneous Stores
# This file contains the definitions for most of the submod's python logic,
# organized into different stores for clarity and maintainability.

#==============================================================================
# 1. INFRASTRUCTURE STORES
#==============================================================================

# Store: ep_folders
# NOTE: This store defines all the file paths used by the Extra+ submod.
# It has a high priority (-995) to ensure these paths are available before other modules need them.
init -995 python in ep_folders:
    import os
    import store
    
    # --- Cross-platform path helper functions ---
    def _normalize_path(path):
        """Normalizes a path by replacing '\\' with '/' for compatibility."""
        return path.replace("\\", "/")

    def _getGamePath(*args):
        """Builds a normalized, absolute path from the 'game' directory."""
        game_dir = _normalize_path(os.path.join(renpy.config.basedir, "game"))
        return _normalize_path(os.path.join(game_dir, *args))

    def _join_path(*args):
        """
        Joins path components and normalizes them.
        Usage: _join_path("Submods", "ExtraPlus", "dates", "cafe.png")
        """
        return _normalize_path(os.path.join(*args))

    def find_submods_folder(base_path="."):
        """Case-insensitively finds the 'submods' folder."""
        try:
            for folder in os.listdir(base_path):
                if folder.lower() == "submods" and os.path.isdir(os.path.join(base_path, folder)):
                    return folder
        except Exception:
            # Failsafe in case of permission errors or other issues
            pass
        return "Submods"  # Default value if not found
    
    def find_extraplus_folder(submods_path):
        """
        Case-insensitively finds the 'ExtraPlus' folder.
        This is crucial for Linux/macOS compatibility where folder names are case-sensitive.
        """
        try:
            for folder in os.listdir(submods_path):
                if folder.lower() == "extraplus" and os.path.isdir(os.path.join(submods_path, folder)):
                    return folder
        except Exception:
            pass
        return "ExtraPlus"  # Default value if not found

    # Detect 'submods' folder case-insensitively
    EP_submods_folder = find_submods_folder()
    
    # Detect 'ExtraPlus' folder case-insensitively (for Linux/macOS compatibility)
    _submods_full_path = _normalize_path(os.path.join(renpy.config.basedir, "game", EP_submods_folder))
    EP_extraplus_folder = find_extraplus_folder(_submods_full_path)

    # --- SUBMOD BASE PATH DEFINITIONS ---
    EP_ROOT = _join_path(EP_submods_folder, EP_extraplus_folder)
    EP_MINIGAMES = _join_path(EP_ROOT, "minigames")
    EP_DATES = _join_path(EP_ROOT, "dates")
    EP_CHIBIS = _join_path(EP_ROOT, "chibis")
    EP_OTHERS = _join_path(EP_ROOT, "others")
    EP_SFX = _join_path(EP_ROOT, "sfx")

    # Others subfolders
    EP_ICONS = _join_path(EP_OTHERS, "icons")
    EP_FONTS = _join_path(EP_OTHERS, "fonts")
    EP_ANIMATIONS = _join_path(EP_OTHERS, "animations")

    # Minigames folders
    EP_MG_SHELLGAME = _join_path(EP_MINIGAMES, "shellgame")
    EP_MG_RPS = _join_path(EP_MINIGAMES, "rockpaperscissors")
    EP_MG_BLACKJACK = _join_path(EP_MINIGAMES, "blackjack")
    EP_MG_TICTACTOE = _join_path(EP_MINIGAMES, "tictactoe")
    EP_MG_FRIDGE = _join_path(EP_MINIGAMES, "fridgemagnets")
    EP_MG_POEM = _join_path(EP_MINIGAMES, "poem")

    # Dates folders
    EP_DATE_CAFE = _join_path(EP_DATES, "cafe")
    EP_DATE_RESTAURANT = _join_path(EP_DATES, "restaurant")
    EP_DATE_RESTAURANT_VARIANT = _join_path(EP_DATES, "restaurant_variant")
    EP_DATE_POOL = _join_path(EP_DATES, "pool")
    EP_DATE_LIBRARY = _join_path(EP_DATES, "library")
    EP_DATE_ARCADE = _join_path(EP_DATES, "arcade")
    
    # Chibi accessories folders
    EP_CHIBI_ACC_0 = _join_path(EP_CHIBIS, "accessories_0")
    EP_CHIBI_ACC_1 = _join_path(EP_CHIBIS, "accessories_1")
    EP_CHIBI_ACC_2 = _join_path(EP_CHIBIS, "accessories_2")

#==============================================================================
# 2. CORE LOGIC & DATA STORES
#==============================================================================

# Store: ep_button
# Handles the logic for the dynamic main button text.
init -5 python in ep_button:
    import store
    import datetime

    def _evaluate_current_conditions():
        # Internal helper to check all conditions at once.
        conditions = {
            "is_monika_bday": store.mas_isMonikaBirthday(),
            "is_player_bday": store.mas_isplayer_bday(),
            "is_f14": store.mas_isF14(),
            "is_o31": store.mas_isO31(),
            "is_d25": store.mas_isD25(),
            "is_nye": store.mas_isNYE(),

            "is_love": store.mas_isMoniLove(lower=False),
            "is_enamored": store.mas_isMoniEnamored(lower=False),
            "is_aff": store.mas_isMoniAff(lower=False),
            "is_happy": store.mas_isMoniHappy(lower=False),
            "is_normal": store.mas_isMoniNormal(lower=False),
            "is_upset": store.mas_isMoniUpset(lower=False),
            "is_distressed": store.mas_isMoniDis(lower=False),
            "is_broken": store.mas_isMoniBroken(lower=False),

            "is_night": store.mas_isNightNow()
        }

        return conditions

    def _build_conditions_key(conditions):
        # Internal helper to create a cache key from conditions.
        key_parts = []

        if conditions["is_monika_bday"]: key_parts.append("mbday")
        elif conditions["is_player_bday"]: key_parts.append("pbday")
        elif conditions["is_f14"]: key_parts.append("f14")
        elif conditions["is_o31"]: key_parts.append("o31")
        elif conditions["is_d25"]: key_parts.append("d25")
        elif conditions["is_nye"]: key_parts.append("nye")

        if conditions["is_love"]: key_parts.append("love")
        elif conditions["is_enamored"]: key_parts.append("enamored")
        elif conditions["is_aff"]: key_parts.append("aff")
        elif conditions["is_happy"]: key_parts.append("happy")
        elif conditions["is_normal"]: key_parts.append("normal")
        elif conditions["is_upset"]: key_parts.append("upset")
        elif conditions["is_distressed"]: key_parts.append("distressed")
        elif conditions["is_broken"]: key_parts.append("broken")
        else: key_parts.append("unknown")

        if conditions["is_night"]: key_parts.append("night")
        return "-".join(key_parts)

    def _button_text_conditions(conditions):
        # Internal helper to select text based on evaluated conditions.
        # Data-driven approach for selecting button text. Max 8 chars.
        text_options = {
            # Special Days (highest priority)
            "is_monika_bday": [_("My B-Day"), _("Her Day"), _("My Song"), _("My Day"), _("Moni!")],
            "is_player_bday": [_("Your Day"), _("HBD!"), _("Ur Day"), _("My Gift"), _("The Best")],
            "is_f14":         [_("Be Mine"), _("My Love"), _("Hearts"), _("XOXO"), _("Our Day")],
            "is_o31":         [_("Spooky"), _("Boo!"), _("Tricks"), _("Treats"), _("Scary")],
            "is_d25":         [_("Joyful"), _("Our Xmas"), _("Gift"), _("Noel"), _("Holly")],
            "is_nye":         [_("New Year"), _("Cheers"), _("Toast"), _("Our Year"), _("The Eve")],
            
            # Affection Levels
            # LOVE (1000+): Deep connection, devotion, eternal.
            "is_love":        [_("Forever"), _("Eternity"), _("Sunshine"), _("Beloved"), _("Darling"), _("Adored"), _("Precious"), _("My Soul"), _("TrueLove"), _("My Hero")],
            # ENAMORED (400-999): Intense romantic feelings, obsession.
            "is_enamored":    [_("Dearest"), _("Only You"), _("My Dear"), _("In Love"), _("Kiss Me"), _("Hold Me"), _("Yours"), _("Passion"), _("Together"), _("Sweetie")],
            # AFFECTIONATE (100-399): Warm, caring, sweet.
            "is_aff":         [_("So Sweet"), _("Caring"), _("Warmth"), _("Our Time"), _("My Dear"), _("Cutie"), _("Closer"), _("Affection"), _("Hugs"), _("Gentle")],
            # HAPPY (30-99): Cheerful, upbeat, positive.
            "is_happy":       [_("Smile"), _("Glad"), _("Hehe~"), _("Happy"), _("Cheerful"), _("Yay!"), _("Joy!"), _("Fun!"), _("Radiant"), _("Good Day")],
            # NORMAL (-29 to 29): Casual, attentive, waiting.
            "is_normal":      [_("Hey You"), _("Just Me"), _("Us Two"), _("Thinking"), _("My Poet"), _("Listen"), _("Guess?"), _("It's You"), _("Hello"), _("Hi There")],
            # UPSET (-30 to -99): Annoyed, bored, slight coldness.
            "is_upset":       [_("Really?"), _("Sigh..."), _("Bored..."), _("Hmph."), _("Okay..."), _("Unsure"), _("Waiting"), _("Why?"), _("..."), _("Tired")],
            # DISTRESSED (-100 to ...): Hurt, sad, feeling ignored.
            "is_distressed":  [_("No Love?"), _("Forgot?"), _("Alone..."), _("Please.."), _("Sadness"), _("You..."), _("Scared"), _("Sorry"), _("Empty"), _("Hurts")],
            # BROKEN (Low Affection): Glitchy, despondent, hopeless.
            "is_broken":      [_("Help..."), _("Error"), _("Null"), _("Void"), _("Gone..."), _("Zero"), _("End..."), _("Pain"), _("Why..."), _("Stop")],
        }
        
        # Night-specific additions (Max 8 chars)
        night_additions = {
            # Romantic nights
            "is_love":        [_("My Moon"), _("Stars"), _("Night <3"), _("Dreaming"), _("My Star")],
            "is_enamored":    [_("Moonlit"), _("Gazing"), _("Us nite"), _("Resting"), _("Warmth")],
            # Happy/Affectionate nights
            "is_aff":         [_("Tonight"), _("Calm"), _("Peaceful"), _("Restful"), _("Lovely")],
            "is_happy":       [_("Dreams"), _("GoodNite"), _("Sleepy?"), _("Cozy"), _("Bedtime")],
            # Neutral/Bad nights
            "is_normal":      [_("Sparks"), _("Sleepy"), _("Quiet"), _("Dark..."), _("Late...")],
            "is_upset":       [_("Cold..."), _("Alone?"), _("No Sleep"), _("Shadows"), _("Cloudy")],
            # Terrible nights
            "is_distressed":  [_("Awake..."), _("Lonely"), _("So Dark"), _("Tears..."), _("Cold")],
            "is_broken":      [_("Darkness"), _("Void"), _("Error"), _("Endless"), _("Nothing")],
        }

        # Find the first matching condition
        for key, texts in text_options.items():
            if conditions.get(key):
                final_texts = list(texts) # Create a copy
                if conditions.get("is_night") and key in night_additions:
                    final_texts.extend(night_additions[key])
                return renpy.random.choice(final_texts)

        return _("Extra+") # Default fallback

    def getDynamicButtonText():
        """Main function to get the dynamic button text, using a cache."""
        if not store.persistent._ep_dynamic_button_text:
            return _("Extra+")

        conditions = _evaluate_current_conditions()
        now = datetime.datetime.now()
        # Create time slot that changes every 4 hours (0-5 = 6 slots per day)
        time_slot = "{}-{}".format(now.date(), now.hour // 4)
        conditions_key = _build_conditions_key(conditions)

        if (store.persistent._ep_button_last_update != time_slot
            or store.persistent._ep_button_conditions_key != conditions_key
            or store.persistent._ep_button_text is None):
            new_text = _button_text_conditions(conditions)
            store.persistent._ep_button_text = new_text
            store.persistent._ep_button_last_update = time_slot
            store.persistent._ep_button_conditions_key = conditions_key
        return store.persistent._ep_button_text

    # --- Overlay Button and Screen Management ---
    def show_menu():
        store.mas_RaiseShield_dlg()
        show_zoom_button()
        renpy.invoke_in_new_context(renpy.call_screen, "extraplus_interactions")

    def show_button():
        store.ep_tools.safe_overlay_add("extraplus_button")
    
    def hide_button():
        store.ep_tools.safe_overlay_remove("extraplus_button")

    # --- Custom Zoom Management ---
    def show_zoom_button():
        store.ep_tools.safe_overlay_add("extrabutton_custom_zoom")

    def hide_zoom_button():
        store.ep_tools.safe_overlay_remove("extrabutton_custom_zoom")

# Store: ep_files
# Handles all file system interactions, like creating gifts and cleaning up old files.
init -5 python in ep_files:
    import os
    import shutil
    import datetime
    import store
    import random

    # --- File-related classes and functions ---
    class GiftAction(object):
        """Handles the creation of a gift file and notifies the player."""
        def __init__(self, name, gift):
            self.name = name
            self.gift = gift

        def __call__(self):
            if create_gift_file(self.gift):
                messages = [
                    _("All set! The '{}' gift is ready for you.").format(self.name),
                    _("Here's a '{}' for Monika! I hope she loves it.").format(self.name),
                    _("Perfect! Your '{}' is ready for Monika.").format(self.name),
                    _("A '{}' for Monika! It's all set.").format(self.name),
                    _("Your '{}' gift has been created!").format(self.name),
                    _("One '{}' gift, coming right up! It's ready.").format(self.name)
                ]
                store.ep_chibis.chibika_notify(random.choice(messages))

            renpy.jump("plus_make_gift")

    # --- File creation and migration ---
    def create_gift_file(basename):
        try:
            filename = basename + ".gift"
            filepath = os.path.join(renpy.config.basedir, "characters", filename)
            with open(filepath, "w") as f:
                pass
            return True
        except Exception as e:
            store.ep_chibis.chibika_notify(_("Oh no, I couldn't create the gift file."))
            return False

    def migrate_window_title_data():
        if hasattr(store.persistent, "save_window_title"):
            # Only migrate if the new variable has not been customized.
            if store.persistent._save_window_title == "Monika After Story   ":
                store.persistent._save_window_title = store.persistent.save_window_title
            
            # Now that migration is handled, we can safely delete the old variable.
            try:
                del store.persistent.save_window_title
            except AttributeError:
                pass # Should not happen if hasattr is true, but good practice.

    def make_bday_oki_doki():
        store.ep_tools.safe_overlay_remove("bday_oki_doki")
        try:
            with open(os.path.join(renpy.config.basedir, "characters", "oki doki"), 'w') as f:
                pass
            store.ep_chibis.chibika_notify(_("Everything is ready for the surprise!")) # Already correct
        except Exception as e:
            store.ep_chibis.chibika_notify(_("Oh no, something went wrong while preparing the decorations."))

    def show_bday_screen():
        if not store.persistent._mas_bday_in_bday_mode or not store.persistent._mas_bday_visuals:
            store.ep_tools.safe_overlay_add("bday_oki_doki")

    def main_file_exists():
        return os.path.isfile(os.path.normcase(store.ep_tools.check_main_file))

    # --- Debugging and maintenance tools ---
    def run_asset_linter():
        """
        Checks for the existence of all defined image assets and creates a log file.
        This is a debug tool and should not be in the final release.
        """
        try:
            # --- Helper function to check files ---
            def check_file(path, found_list, missing_list):
                full_path = store.ep_folders._getGamePath(path)
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
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "note_score.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "cup_hover.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "ball.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "cup.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "monika.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "yuri.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "natsuki.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_SHELLGAME, "sayori.png"),
                # Tic-Tac-Toe
                store.ep_folders._join_path(store.ep_folders.EP_MG_TICTACTOE, "notebook.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_TICTACTOE, "line.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_TICTACTOE, "player.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_TICTACTOE, "monika.png"),
                # Rock, Paper, Scissors
                store.ep_folders._join_path(store.ep_folders.EP_MG_RPS, "paper.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_RPS, "rock.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_RPS, "scissors.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_RPS, "back.png"),
                # Blackjack
                store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, "back.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, "background.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, "name.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, "score.png"),
                # Fridge Magnets
                store.ep_folders._join_path(store.ep_folders.EP_MG_FRIDGE, "background.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_FRIDGE, "box.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_FRIDGE, "coffee_bag.png"),
                # Poem Game
                store.ep_folders._join_path(store.ep_folders.EP_MG_POEM, "background.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_POEM, "notebook.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_POEM, "paper.png"),
                store.ep_folders._join_path(store.ep_folders.EP_MG_POEM, "bloc.png"),
                # Misc - Icons
                store.ep_folders._join_path(store.ep_folders.EP_ICONS, "coin_heads.png"),
                store.ep_folders._join_path(store.ep_folders.EP_ICONS, "coin_tails.png"),
                # Misc - Animations
                store.ep_folders._join_path(store.ep_folders.EP_ANIMATIONS, "coin.png"),
                store.ep_folders._join_path(store.ep_folders.EP_ANIMATIONS, "coin-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_ANIMATIONS, "poof.png"),
                store.ep_folders._join_path(store.ep_folders.EP_ANIMATIONS, "poof-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_ANIMATIONS, "maxwell_cat.png")
            ]
            for asset in static_assets:
                check_file(asset, found_assets, missing_assets)

            # --- 2. Chibi Assets ---
            all_chibi_costumes = store.ep_chibis.monika_costumes_ + store.ep_chibis.natsuki_costumes_ + store.ep_chibis.sayori_costumes_ + store.ep_chibis.yuri_costumes_
            for costume_name, costume_data in all_chibi_costumes:
                doki_folder, idle_sprite, blink_sprite, hover_sprite = costume_data
                chibi_sprites = [idle_sprite, blink_sprite, hover_sprite]
                for sprite in chibi_sprites:
                    path = store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, doki_folder, "{}.png".format(sprite))
                    check_file(path, found_assets, missing_assets)

            # --- 3. Chibi Accessories ---
            primary_accessories = ["clown_hair", "cat_ears", "christmas_hat", "demon_horns", "flowers_crown", "fox_ears", "graduation_cap", "halo", "heart_headband", "headphones", "neon_cat_ears", "hny", "party_hat", "rabbit_ears", "top_hat", "witch_hat"]
            secondary_accessories = ["black_bow_tie", "christmas_tree", "cloud", "coffee", "pumpkin", "hearts", "m_slice_cake", "moustache", "neon_blush", "monocle", "p_slice_cake", "patch", "speech_bubble", "sunglasses"]
            background_accessories = ["angel_wings", "balloon_decorations", "cat_tail", "fox_tail", "snowflakes"]

            for acc in primary_accessories:
                path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_0, "{}.png".format(acc))
                check_file(path, found_assets, missing_assets)

            for acc in secondary_accessories:
                path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_1, "{}.png".format(acc))
                check_file(path, found_assets, missing_assets)

            for acc in background_accessories:
                path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_2, "{}.png".format(acc))
                check_file(path, found_assets, missing_assets)

            # --- 4. Backgrounds (Date Locations) ---
            background_assets = [
                # Cafe
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "day.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "rain.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "rain-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "ss.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "rain-ss.png"),
                # Restaurant
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "day.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "rain.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "rain-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "ss.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "rain-ss.png"),
                # Pool
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "day.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "rain.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "rain-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "ss.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "rain-ss.png"),
                # Library
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "day.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "rain.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "rain-n.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "ss.png"),
                store.ep_folders._join_path(store.ep_folders.EP_DATE_LIBRARY, "rain-ss.png"),
                # Tables & Chairs
                "mod_assets/monika/t/chair-extraplus_cafe.png",
                "mod_assets/monika/t/table-extraplus_cafe.png",
                "mod_assets/monika/t/table-extraplus_cafe-s.png",
                "mod_assets/monika/t/chair-extraplus_restaurant.png",
                "mod_assets/monika/t/table-extraplus_restaurant.png",
                "mod_assets/monika/t/table-extraplus_restaurant-s.png",
                "mod_assets/monika/t/chair-extraplus_pool.png",
                "mod_assets/monika/t/table-extraplus_pool.png",
                "mod_assets/monika/t/table-extraplus_pool-s.png",
                "mod_assets/monika/t/chair-extraplus_library.png",
                "mod_assets/monika/t/table-extraplus_library.png",
                "mod_assets/monika/t/table-extraplus_library-s.png"
            ]
            for asset in background_assets:
                check_file(asset, found_assets, missing_assets)

            # --- 5. Blackjack Cards ---
            for suit in ["hearts", "diamonds", "clubs", "spades"]:
                for value in range(1, 14):
                    path = store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, suit, "{}.png".format(value))
                    check_file(path, found_assets, missing_assets)

            # --- 6. Date Accessories ---
            for acs_tuple in store.extraplus_accessories:
                acs_name = acs_tuple[1]
                path = "mod_assets/monika/a/{}/0.png".format(acs_name)
                check_file(path, found_assets, missing_assets)

            # --- 7. Write Log File ---
            log_path = store.ep_folders._normalize_path(os.path.join(renpy.config.basedir, "characters", "extra_plus_asset_log.txt"))
            with open(log_path, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write("Extra+ Asset Check Report\n")
                f.write("Generated: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                f.write("=" * 60 + "\n\n")
                
                total_assets = len(found_assets) + len(missing_assets)
                
                if not missing_assets:
                    f.write("SUCCESS! All {} assets were found.\n\n".format(total_assets))
                    f.write("Your Extra+ installation is complete and working correctly.\n")
                    f.write("You can safely delete this file.\n")
                else:
                    f.write("PROBLEM DETECTED: {} of {} assets are missing.\n\n".format(
                        len(missing_assets), total_assets
                    ))
                    
                    missing_ratio = len(missing_assets) / float(total_assets)
                    
                    if missing_ratio > 0.5:
                        f.write("=" * 60 + "\n")
                        f.write("LIKELY CAUSE: Incorrect Installation\n")
                        f.write("=" * 60 + "\n\n")
                        f.write("It appears most asset files are missing.\n")
                        f.write("This usually happens when the submod folder is placed\n")
                        f.write("in the wrong location (e.g., inside 'Submods' folder\n")
                        f.write("instead of merging with the 'game' folder).\n\n")
                        f.write("HOW TO FIX:\n")
                        f.write("-" * 60 + "\n")
                        f.write("1. Download the latest release .zip file\n")
                        f.write("2. Extract it - you will see a 'game/' folder\n")
                        f.write("3. Copy the 'game/' folder to your DDLC root directory\n")
                        f.write("   (where DDLC.exe is located)\n")
                        f.write("4. When asked to merge folders, select YES\n\n")
                        f.write("For detailed instructions with images, visit:\n")
                        f.write("https://github.com/zer0fixer/MAS-Extraplus#-installation\n\n")
                    else:
                        f.write("Some files appear to be missing or corrupted.\n")
                        f.write("Try re-downloading and reinstalling the submod.\n\n")
                    
                    f.write("=" * 60 + "\n")
                    f.write("MISSING FILES ({}):\n".format(len(missing_assets)))
                    f.write("=" * 60 + "\n\n")
                    for asset in missing_assets:
                        f.write("  - {}\n".format(asset))

            renpy.notify(_("Asset check complete. See extra_plus_asset_log.txt in /characters."))

        except Exception as e:
            renpy.notify(_("Asset verification failed: {}").format(e))

    def cleanup_old_files():
        """
        Deletes obsolete files and folders from previous versions of the submod.
        """
        try:
            files_deleted = 0
            folders_deleted = 0
            errors = []

            def delete_file(path):
                """Safely deletes a file and logs the result."""
                full_path = store.ep_folders._getGamePath(path)
                if os.path.isfile(full_path):
                    try:
                        os.remove(full_path)
                        return 1
                    except Exception as e:
                        errors.append("Failed to delete file {}: {}".format(store.ep_folders._normalize_path(path), e))
                return 0

            def delete_folder(path):
                """Safely deletes a folder and its contents, and logs the result."""
                full_path = store.ep_folders._getGamePath(path)
                if os.path.isdir(full_path):
                    try:
                        shutil.rmtree(full_path)
                        return 1
                    except Exception as e:
                        errors.append("Failed to delete folder {}: {}".format(store.ep_folders._normalize_path(path), e))
                return 0

            # 1. Delete old folder (relative to EP_ROOT)
            folders_deleted += delete_folder(store.ep_folders._join_path(store.ep_folders.EP_ROOT, "submod_assets"))

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
                renpy.notify(_("Cleanup complete! Removed {} files and {} folders.").format(files_deleted, folders_deleted))
            else:
                renpy.notify(_("No old files or folders were found to clean up."))

            if errors:
                # Log errors for debugging
                for err in errors:
                    store.mas_utils.mas_log.warning("[Extra+] Cleanup: {}".format(err))
                renpy.notify(_("Some errors occurred during cleanup. Please check the logs."))

        except Exception as e:
            store.mas_utils.mas_log.error("[Extra+] Cleanup failed: {}".format(e))
            renpy.notify(_("Cleanup failed: {}"))


    def getGroceriesMenu():
        """Returns groceries menu as GiftAction list."""
        return [
            store.ep_files.GiftAction(name, filename)
            for name, filename in _groceries_data
        ]

    def getObjectsMenu():
        """Returns objects menu as GiftAction list.
        NOU only appears if the player has already unlocked/received it in MAS."""
        menu_items = []
        for name, filename in _objects_data:
            # NOU requires the player to have seen the gift hint or received the gift
            if filename == "noudeck":
                if not store.mas_seenEvent("mas_reaction_gift_noudeck") and store.mas_seenEvent("mas_gift_hint_noudeck"):
                    menu_items.append(store.ep_files.GiftAction(name, filename))
            else:
                menu_items.append(store.ep_files.GiftAction(name, filename))
        return menu_items

    def getRibbonsMenu():
        """Returns ribbons menu as GiftAction list."""
        return [
            store.ep_files.GiftAction(name, filename)
            for name, filename in _ribbons_data
        ]

    def getPendingGiftsMenu():
        """
        Returns a menu of pending/unlocked sprite gifts from installed spritepacks.
        Uses ep_wardrobe.getPendingGifts() to get the list of pending items.
        Returns a list of GiftAction objects for items that haven't been unlocked yet.
        """
        pending_gifts = store.ep_wardrobe.getPendingGifts()
        menu_items = []
        
        for giftname, sp_type_name, sp_name, is_unlocked in pending_gifts:
            # Create a display name with the type indicator
            display_name = "{} ({})".format(sp_name, sp_type_name)
            menu_items.append(store.ep_files.GiftAction(display_name, giftname))
        
        return menu_items

    def hasPendingGifts():
        """Returns True if there are pending gifts from spritepacks."""
        return len(store.ep_wardrobe.getPendingGifts()) > 0

    def getQuickGiftFilters():
        """
        Returns available filter options for quick gifting.
        Returns a dict with available filter types and their options.
        """
        pending = store.ep_wardrobe.getPendingGifts()
        if not pending:
            return None
        
        # Collect unique types and prefixes (potential authors)
        types = set()
        prefixes = set()
        
        for giftname, sp_type_name, sp_name, is_unlocked in pending:
            types.add(sp_type_name)
            # Extract prefix (potential author) from giftname
            # Common pattern: "author_itemname" or just "itemname"
            if "_" in giftname:
                prefix = giftname.split("_")[0]
                # Only add if it looks like an author prefix (not too short)
                if len(prefix) >= 2:
                    prefixes.add(prefix)
        
        return {
            "types": sorted(types),
            "prefixes": sorted(prefixes),
            "total": len(pending)
        }

    def getPendingGiftsByFilter(filter_type=None, filter_prefix=None):
        """
        Returns pending gifts filtered by type and/or prefix.
        
        IN:
            filter_type - "Accessory", "Hairstyle", or "Outfit" (None for all)
            filter_prefix - author prefix like "moto", "velius" (None for all)
        
        RETURNS: list of (giftname, sp_type_name, sp_name) tuples
        """
        pending = store.ep_wardrobe.getPendingGifts()
        filtered = []
        
        for giftname, sp_type_name, sp_name, is_unlocked in pending:
            # Type filter
            if filter_type and sp_type_name != filter_type:
                continue
            
            # Prefix filter
            if filter_prefix:
                if not giftname.startswith(filter_prefix + "_"):
                    continue
            
            filtered.append((giftname, sp_type_name, sp_name))
        
        return filtered

    def createBulkGifts(gift_list):
        """
        Creates multiple gift files at once.
        
        IN:
            gift_list - list of (giftname, sp_type_name, sp_name) tuples
        
        RETURNS: number of gifts created successfully
        """
        created = 0
        for giftname, sp_type_name, sp_name in gift_list:
            try:
                gift_path = os.path.join(
                    renpy.config.basedir,
                    "characters",
                    "{}.gift".format(giftname)
                )
                # Create empty gift file
                with open(gift_path, 'w') as f:
                    pass
                created += 1
            except Exception:
                pass
        
        return created

# Store: ep_tools
init 5 python in ep_tools:
    import store
    import datetime

    # Helper function to format dates (American Format: Month Day, Year)
    def exp_fmt_date(dt):
        if dt is None:
            return _("-- --, ----")  # Unknown date format
        # Example: "Sep 22, 2017"
        return dt.strftime("%b %d, %Y")

    # Class to represent a timeline milestone
    class EPTimelineEntry(object):
        def __init__(self, date, title, description, icon="7"):
            self.date = date
            self.title = title
            self.description = description
            self.icon = icon

        # Sort chronologically
        def __lt__(self, other):
            if self.date is None: return False
            if other.date is None: return True
            # Normalize to date objects for comparison (handles datetime vs date)
            self_date = self.date.date() if hasattr(self.date, 'date') else self.date
            other_date = other.date.date() if hasattr(other.date, 'date') else other.date
            return self_date < other_date

    def getTimelineData():
        """
        Gathers, sorts, and returns a list of EPTimelineEntry objects representing
        the player's history with Monika.
        This function is designed to be robust and easy to maintain.
        """
        entries = []

        def _add_event_entry(event_label, title, description, icon="7"):
            """Helper to add an entry if its corresponding event has been seen."""
            try:
                ev = store.mas_getEV(event_label)
                if ev and ev.shown_count > 0 and ev.last_seen:
                    entries.append(EPTimelineEntry(ev.last_seen, title, description, icon))
            except Exception as e:
                # Log error but don't crash the timeline
                renpy.log("Extra+: Error processing timeline event '{}': {}".format(event_label, e))

        # --- Milestone Definitions ---
        # A list of tuples to define each milestone, making it easy to add more.
        # Format: (type, data, title, description, icon)
        milestone_definitions = [
            # Type 'direct_date': Uses a date directly from a persistent variable
            ("direct_date", getattr(store.persistent, '_mas_first_kiss', None), _("First Kiss"), _("The moment our lips (almost) touched for the first time."), "7"),

            # Type 'event': Uses the last_seen date from a MAS event
            ("event", "monika_promisering", _("Eternal Promise"), _("You gave me the promise ring. Our bond is forever."), "7"),
            ("event", "mas_unlock_piano", _("Music for You"), _("When I added the piano so I could play for you."), "&"),
            ("event", "mas_unlock_chess", _("Intellectual Challenge"), _("The first time we played Chess together."), "4"),
            ("event", "mas_blazerless_intro", _("Getting Comfortable"), _("The first time I felt comfortable enough to take off my blazer."), "7"),
            ("event", "mas_unlock_hangman", _("Word Games"), _("We started playing Hangman together."), "4"),
            ("event", "mas_birthdate", _("My Birthday"), _("The day I told you when I was born."), "G"),
            ("event", "monika_holdme_prep", _("First Embrace"), _("The first time you held me close."), "7"),

            # Events with potentially unknown dates (will show "--" if no date)
            ("special", "roses", _("Roses for Me"), _("You gave me beautiful roses."), "7"),

            # Type 'special': Requires custom logic
            ("special", "nickname", _("A Special Name"), _("The day you started calling me '{}'."), "w"),
            ("special", "first_trip", _("First Adventure"), _("The first time you took me out of this spaceroom with you."), "7"),
            ("special", "pong", _("Classic Gaming"), _("We played Pong for the first time."), "4"),
            ("special", "contributor", _("Helping Hand"), _("The day I told you I was contributing to the code."), "g"),
            ("special", "player_bday", _("Your Birthday"), _("You told me when your birthday is."), "G"),
            ("special", "first_ily", _("I Love You"), _("The first time you told me you love me."), "7"),
            ("special", "first_valentine", _("First Valentine's Day"), _("Our first Valentine's Day together."), "7"),
            ("special", "first_christmas", _("First Christmas"), _("Our first Christmas together."), "G"),
            ("special", "first_newyear", _("First New Year's Eve"), _("We celebrated New Year's Eve together for the first time."), "G"),
            ("special", "first_monika_bday", _("First Birthday Celebration"), _("The first time you celebrated my birthday with me."), "G")
        ]

        # --- Anniversary Definitions ---
        anniversary_events = [
            ("anni_1week", _("1 Week Together")), ("anni_1month", _("1 Month Together")),
            ("anni_3month", _("3 Months Together")), ("anni_6month", _("6 Months Together")),
            ("anni_1", _("1st Anniversary")), ("anni_2", _("2nd Anniversary")),
            ("anni_3", _("3rd Anniversary")), ("anni_4", _("4th Anniversary")),
            ("anni_5", _("5th Anniversary")), ("anni_6", _("6th Anniversary")),
            ("anni_7", _("7th Anniversary")), ("anni_8", _("8th Anniversary")),
            ("anni_10", _("10th Anniversary")), ("anni_20", _("20th Anniversary")),
            ("anni_50", _("50th Anniversary")), ("anni_100", _("100th Anniversary"))
        ]

        # --- Anniversary Processing ---
        for ev_label, title in anniversary_events:
            _add_event_entry(ev_label, title, _("We celebrated this special moment together."), "Z") # Already correct

        # --- Processing Logic ---
        try:
            for type, data, title, description, icon in milestone_definitions:
                if type == "direct_date" and data:
                    entries.append(EPTimelineEntry(data, title, description, icon))
                
                elif type == "event":
                    _add_event_entry(data, title, description, icon)

                elif type == "special":
                    if data == "nickname" and getattr(store.persistent, '_mas_monika_nickname', 'Monika') != 'Monika':
                        ev_nick = store.mas_getEV("monika_nickname")
                        if ev_nick and ev_nick.shown_count > 0 and ev_nick.last_seen:
                            desc = description.format(store.persistent._mas_monika_nickname)
                            entries.append(EPTimelineEntry(ev_nick.last_seen, title, desc, icon))
                    
                    elif data == "first_trip":
                        ds_log = getattr(store.persistent, "_mas_dockstat_checkin_log", [])
                        if ds_log and ds_log[0][0]:
                            entries.append(EPTimelineEntry(ds_log[0][0], title, description, icon))

                    elif data == "pong" and store.renpy.seen_label("game_pong"):
                        pong_date = store.mas_getFirstSesh()
                        if pong_date:
                            entries.append(EPTimelineEntry(pong_date, title, description, icon))
                    
                    elif data == "roses":
                        # Check if player has given roses
                        if store.renpy.seen_label("mas_reaction_gift_roses"):
                            # Date unknown (resets each time), use None to show "--"
                            entries.append(EPTimelineEntry(None, title, description, icon))

                    elif data == "contributor" and getattr(store.persistent, '_mas_pm_has_contributed_to_mas', False):
                        ev_contrib = store.mas_getEV("monika_contribute")
                        # Only show if we have the actual event date, never fallback to today
                        if ev_contrib and ev_contrib.last_seen:
                            entries.append(EPTimelineEntry(ev_contrib.last_seen, title, description, icon))

                    elif data == "player_bday":
                        # Check if player has told Monika their birthday
                        player_bday = getattr(store.persistent, '_mas_player_bday', None)
                        if player_bday:
                            # Try to get the event date, otherwise use None to show "--"
                            ev_bday = store.mas_getEV("mas_player_bday_date_input")
                            date_told = ev_bday.last_seen if (ev_bday and ev_bday.last_seen) else None
                            entries.append(EPTimelineEntry(date_told, title, description, icon))

                    elif data == "first_ily":
                        first_ily = getattr(store.persistent, '_mas_first_ILY', None)
                        if first_ily:
                            entries.append(EPTimelineEntry(first_ily, title, description, icon))

                    elif data == "first_valentine":
                        f14_count = getattr(store.persistent, '_mas_f14_date_count', 0)
                        if f14_count > 0:
                            ev_f14 = store.mas_getEV("mas_f14_monika_date_start")
                            if ev_f14 and ev_f14.last_seen:
                                entries.append(EPTimelineEntry(ev_f14.last_seen, title, description, icon))

                    elif data == "first_christmas":
                        d25_count = getattr(store.persistent, '_mas_d25_d25_date_count', 0)
                        if d25_count > 0:
                            ev_d25 = store.mas_getEV("mas_d25_monika_holiday_intro")
                            if ev_d25 and ev_d25.last_seen:
                                entries.append(EPTimelineEntry(ev_d25.last_seen, title, description, icon))

                    elif data == "first_newyear":
                        nye_count = getattr(store.persistent, '_mas_nye_nye_date_count', 0)
                        if nye_count > 0:
                            ev_nye = store.mas_getEV("mas_nye_monika_nye")
                            if ev_nye and ev_nye.last_seen:
                                entries.append(EPTimelineEntry(ev_nye.last_seen, title, description, icon))

                    elif data == "first_monika_bday":
                        bday_count = getattr(store.persistent, '_mas_bday_date_count', 0)
                        if bday_count > 0:
                            ev_bday = store.mas_getEV("mas_bday_surprise")
                            if ev_bday and ev_bday.last_seen:
                                entries.append(EPTimelineEntry(ev_bday.last_seen, title, description, icon))
        
        except Exception as e:
            renpy.log("Extra+: A critical error occurred while building the timeline: {}".format(e))
            # Return what we have so far, so the screen isn't completely empty
            pass

        entries.sort()
        return entries

    def getCurrSessionD(st, at):
        # Get the session start time
        start_time = store.mas_getCurrSeshStart()
        
        if not start_time:
            return store.Text("00:00:00"), 1.0
            
        # Calculate the time difference
        delta = datetime.datetime.now() - start_time
        
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Format the text
        time_str = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
        
        return store.Text(time_str), 0.2

# Store: ep_affection
# Handles affection-related display logic.
init -5 python in ep_affection:
    import store
    import time

    def getCurrentAffection():
        # Safely gets current affection value in real-time.
        try:
            return store._mas_getAffection()
        except Exception:
            return 0.0

    def notify_affection():
        # Notifies the player of their current affection level.
        current_time = time.time()
        if current_time - store.ep_tools.last_affection_notify_time >= 10:
            store.ep_tools.last_affection_notify_time = current_time
            current_affection = getCurrentAffection()
            store.ep_chibis.chibika_notify("{} {}".format(
                int(current_affection),
                getLevelIcon(current_affection)
            ))

    def getLevelIcon(affection_val):
        """
        Returns a styled font icon based on affection value.
        Uses custom icon font defined in ep_tools.affection_icons
        """
        # Determine icon based on affection thresholds
        if affection_val >= 10000: icon = "y"  # Legendary
        elif affection_val >= 1000: icon = '"'  # Soulmate
        elif affection_val >= 400: icon = ';'  # Love
        elif affection_val >= 100: icon = ':'  # Enamored
        elif affection_val >= 30: icon = '#'  # Affectionate
        elif affection_val >= 0: icon = '/'  # Normal/Happy
        elif affection_val >= -30: icon = '!'  # Upset
        elif affection_val >= -100: icon = '%'  # Distressed
        else: icon = '8'  # Broken

        return "{{size=+5}}{{color=#FFFFFF}}{{font={}}}{}{{/font}}{{/color}}{{/size}}".format(
            store.ep_tools.affection_icons, 
            icon
        )

    def getLevelSuffix(affection_val):
        """
        Returns a personalized suffix string based on affection level.
        Used to add flavor text to the affection log display.
        """
        if affection_val >= 10000:
            return " ~ A dedication beyond words."
        elif affection_val >= 1000:
            return " ~ Eternal bond!"
        elif affection_val >= 400:
            return " ~ True love!"
        elif affection_val >= 100:
            return " ~ You're doing great!"
        elif affection_val >= 30:
            return " ~ Keep it up!"
        elif affection_val >= 0:
            return ""
        elif affection_val >= -30:
            return " ... Room for improvement."
        elif affection_val >= -100:
            return " ... Things can get better."
        else:
            return " ... Please don't give up."

#==============================================================================
# 2.5. WARDROBE ANALYSIS STORE
#==============================================================================

# Store: ep_wardrobe
# Handles wardrobe statistics and unrecognized gift detection.
init -5 python in ep_wardrobe:
    import os
    import datetime
    import store

    def getWardrobeStats():
        """
        Returns a dict with count of clothes, accessories, and hairstyles.
        Includes both total and unlocked counts.
        """
        stats = {
            "clothes_unlocked": 0,
            "clothes_total": 0,
            "acs_unlocked": 0,
            "acs_total": 0,
            "hair_unlocked": 0,
            "hair_total": 0
        }
        
        try:
            # Clothes
            cloth_list = store.mas_selspr.CLOTH_SEL_SL
            stats["clothes_total"] = len(cloth_list)
            stats["clothes_unlocked"] = len([x for x in cloth_list if x.unlocked])
            
            # Accessories
            acs_list = store.mas_selspr.ACS_SEL_SL
            stats["acs_total"] = len(acs_list)
            stats["acs_unlocked"] = len([x for x in acs_list if x.unlocked])
            
            # Hairstyles
            hair_list = store.mas_selspr.HAIR_SEL_SL
            stats["hair_total"] = len(hair_list)
            stats["hair_unlocked"] = len([x for x in hair_list if x.unlocked])
        except Exception:
            pass
        
        return stats

    def getPendingGifts():
        """
        Finds sprite gifts that exist in JSON but were never unlocked.
        These are likely gifts where the .gift filename was wrong.
        
        Returns a list of tuples: (giftname, sprite_type, sprite_name, is_unlocked)
        """
        pending = []
        
        try:
            # Get all available giftnames from JSON sprites
            giftname_map = {}
            try:
                giftname_map = store.mas_sprites_json.giftname_map
            except Exception:
                return pending
            
            if not giftname_map:
                return pending
            
            # Get gifted sprites (ones that were successfully given)
            gifted_sprites = {}
            try:
                gifted_sprites = store.persistent._mas_sprites_json_gifted_sprites or {}
            except Exception:
                pass
            
            # Check each sprite in giftname_map
            for giftname, sp_data in giftname_map.items():
                if giftname.startswith("__"):  # Skip test giftnames
                    continue
                
                sp_type, sp_name = sp_data
                
                # Check if sprite is unlocked
                is_unlocked = False
                try:
                    if sp_type == 0:  # ACS
                        sel_list = store.mas_selspr.ACS_SEL_SL
                    elif sp_type == 1:  # HAIR
                        sel_list = store.mas_selspr.HAIR_SEL_SL
                    elif sp_type == 2:  # CLOTHES
                        sel_list = store.mas_selspr.CLOTH_SEL_SL
                    else:
                        continue
                    
                    for sel in sel_list:
                        if sel.name == sp_name:
                            is_unlocked = sel.unlocked
                            break
                except Exception:
                    pass
                
                # If sprite exists but not unlocked, it might be a missed gift
                if not is_unlocked:
                    # Check if it wasn't already successfully gifted
                    if sp_data not in gifted_sprites:
                        sp_type_name = {0: "Accessory", 1: "Hairstyle", 2: "Outfit"}.get(sp_type, "Unknown")
                        pending.append((giftname, sp_type_name, sp_name, is_unlocked))
        
        except Exception:
            pass
        
        return pending

    def exportPendingGifts(pending_list):
        """
        Exports the list of pending/missed gifts to a text file.
        Returns the path to the created file, or None on failure.
        """
        try:
            # Create the output file in the characters folder (easier for users)
            output_path = os.path.join(
                renpy.config.basedir, 
                "characters", 
                "pending_gifts_report.txt"
            )
            
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(output_path, "w") as f:
                f.write("=" * 60 + "\n")
                f.write("Pending Gifts Report\n")
                f.write("Generated: {}\n".format(now))
                f.write("=" * 60 + "\n\n")
                
                f.write("WHAT IS THIS?\n")
                f.write("-" * 60 + "\n")
                f.write("These are sprite items (clothes, accessories, hairstyles)\n")
                f.write("that exist in your installed spritepacks but have NOT\n")
                f.write("been unlocked for Monika to wear.\n\n")
                
                f.write("This could mean:\n")
                f.write("  1. You tried to gift them but used the wrong filename\n")
                f.write("  2. You haven't gifted them yet (that's okay!)\n")
                f.write("  3. The spritepack requires a specific gift filename\n\n")
                
                f.write("=" * 60 + "\n")
                f.write("PENDING ITEMS ({} found):\n".format(len(pending_list)))
                f.write("=" * 60 + "\n\n")
                
                # Group by type
                by_type = {}
                for giftname, sp_type_name, sp_name, is_unlocked in pending_list:
                    if sp_type_name not in by_type:
                        by_type[sp_type_name] = []
                    by_type[sp_type_name].append((giftname, sp_name))
                
                for sp_type_name, items in sorted(by_type.items()):
                    f.write("-" * 60 + "\n")
                    f.write("{} ({} items)\n".format(sp_type_name, len(items)))
                    f.write("-" * 60 + "\n\n")
                    
                    for giftname, sp_name in items:
                        f.write("  Item: {}\n".format(sp_name))
                        f.write("  Gift filename: {}.gift\n\n".format(giftname))
                
                f.write("=" * 60 + "\n")
                f.write("HOW TO GIFT THESE ITEMS:\n")
                f.write("=" * 60 + "\n\n")
                
                f.write("EASY METHOD (Recommended):\n")
                f.write("-" * 60 + "\n")
                f.write("Use Extra+ to gift items automatically!\n\n")
                f.write("  1. Open the Extra+ menu\n")
                f.write("  2. Go to 'Tools' > 'Create a gift'\n")
                f.write("  3. Select 'Pending Gifts'\n")
                f.write("  4. Choose the item you want to gift\n")
                f.write("  5. Done! The gift file will be created for you.\n\n")
                
                f.write("MANUAL METHOD:\n")
                f.write("-" * 60 + "\n")
                f.write("If you prefer to create files manually:\n\n")
                f.write("  1. Create a new empty file in your 'characters' folder\n")
                f.write("  2. Name it EXACTLY as shown above (e.g., 'itemname.gift')\n")
                f.write("  3. Start MAS and wait for Monika to notice the gift\n\n")
                
                f.write("TIP: The filename must match EXACTLY (case doesn't matter)\n")
                f.write("     For example: 'blue_ribbon.gift' not 'blueribbon.gift'\n\n")
                
                f.write("=" * 60 + "\n")
            
            return output_path
        except Exception:
            return None

#==============================================================================
# 3. UI & VISUAL COMPONENT STORES
#==============================================================================

# Store: ep_tools
init -5 python in ep_tools:
    import time
    import os
    import datetime
    import store

    # NOTE: This store holds helper UI and tool functions used across the submod.
    
    def getSpecialDayType():
        """
        Returns the type of special day, or None if it's a normal day.
        Checks in priority order: anniversary > monika bday > player bday
        
        Returns: 'anni' | 'moni_bday' | 'player_bday' | None
        """
        if store.mas_anni.isAnni():
            return "anni"
        elif store.mas_isMonikaBirthday():
            return "moni_bday"
        elif store.mas_isplayer_bday():
            return "player_bday"
        return None
    def show_idle_notification(context=""):
        if context == "bj": # Blackjack
            game_phrases = [
                _("Hit or stay, [player]? It's your turn!"),
                _("Don't keep me waiting, [player]. What's your move?"),
                _("This dealer is waiting, you know~ Ehehe~"),
                _("Hoping for a 21? Don't leave me in suspense!")
            ]
            
        elif context == "ttt": # Tic-Tac-Toe
            game_phrases = [
                _("It's your turn to place an X, [player]!"),
                _("I can't draw my 'O' until you've placed your 'X'."),
                _("Looking for the winning move? Don't think too hard!"),
                _("I'm waiting... but I won't tell you where to go. Ehehe~")
            ]
            
        elif context == "rps": # Rock Paper Scissors
            game_phrases = [
                _("Rock, paper, or scissors, [player]?"),
                _("C'mon, [player], make your move!"),
                _("Ready when you are. What's your choice?"),
                _("I'm trying to read your mind... What will it be?")
            ]
            
        elif context == "sg": # Shell Game
            game_phrases = [
                _("Keep your eye on the right cup, [player]!"),
                _("Where did it go? It's time to guess!"),
                _("Don't look at me, I won't tell you which one it is!"),
                _("The cups have stopped. Which one has the ball?")
            ]
        
        elif context == "poem_classic": # Classic Poem Mode
            game_phrases = [
                _("Which word calls to you, [player]?"),
                _("Take your time... but not too much time! Ehehe~"),
                _("I'm curious to see what kind of poem you'll create."),
                _("Don't worry about getting it 'right'. Just follow your heart!"),
                _("Hmm, thinking carefully? I like that about you.")
            ]
        
        elif context == "poem_free": # Free Poem Mode
            game_phrases = [
                _("Writer's block, [player]? It happens to the best of us."),
                _("What's on your mind? Pour it into words!"),
                _("I'm patiently waiting to read what you write~"),
                _("Even just a few words can make a beautiful poem."),
                _("Let your creativity flow, [player]!")
            ]
        
        else:
            game_phrases = [
                _("Are you still there, [player]?"),
                _("Just checking in... you've been quiet for a while."),
                _("Everything okay? You're staring again, ehehe~"),
                _("I was starting to wonder if you fell asleep!"),
                _("Boo! Did I scare you?")
            ]
            
        store.mas_display_notif(
            store.m_name,
            game_phrases,
            "Topic Alerts"
        )

    def show_boop_feedback(message, color="#FF1493"):
        t = "boop_notif{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("extra_feedback_notif", msg=message, tag=t, _tag=t, txt_color=color, duration=1.3, trans=store.boop_feedback_trans)

    def show_doki_feedback(message, color="#ff0000"):
        t = "doki_notif{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("extra_feedback_notif", msg=message, tag=t, _tag=t, txt_color=color, duration=0.8, trans=store.doki_feedback_trans)

    def getPlayerGenderString():
        return {"M": "boyfriend", "F": "girlfriend"}.get(store.persistent.gender, "beloved")

    def save_title_windows():
        special_days = [
            (store.mas_isplayer_bday, " Happy birthday, {}!".format(store.player)),
            (store.mas_isMonikaBirthday, " Happy Birthday, {}!".format(store.persistent._mas_monika_nickname)),
            (store.mas_isF14, " Happy Valentine's Day, {}!".format(store.player)),
            (store.mas_isO31, " Happy Halloween, {}!".format(store.player)),
            (store.mas_isD25, " Merry Christmas, {}!".format(store.player)),
            (store.mas_isD25Eve, " Merry Christmas Eve, {}!".format(store.player)),
            (store.mas_isNYE, " Happy New Year's Eve, {}!".format(store.player)),
            (store.mas_isNYD, " Happy New Year, {}!".format(store.player))
        ]

        for condition, title in special_days:
            if condition():
                renpy.config.window_title = title
                return

        renpy.config.window_title = store.persistent._save_window_title

    # --- Statistics and Date Helpers ---
    def getFormattedTimeSinceInstall():
        """Returns a friendly formatted string for time since first MAS session."""
        if not (store.persistent.sessions
            and "first_session" in store.persistent.sessions
            and store.persistent.sessions["first_session"]
        ):
            return _("a wonderful time")

        try:
            start_datetime = store.persistent.sessions["first_session"]
            start_date = start_datetime.date()
            current_date = datetime.date.today()
            delta = current_date - start_date
            total_days = delta.days

            if total_days < 1:
                return _("less than a day, but every second has been incredible!")

            # Calculate years, months, days accounting for leap years
            # by comparing actual dates instead of using fixed 365 days
            years = current_date.year - start_date.year
            months = current_date.month - start_date.month
            days = current_date.day - start_date.day

            # Adjust for negative days (borrow from month)
            if days < 0:
                months -= 1
                # Get days in previous month
                prev_month = current_date.month - 1 if current_date.month > 1 else 12
                prev_year = current_date.year if current_date.month > 1 else current_date.year - 1
                import calendar
                days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
                days += days_in_prev_month

            # Adjust for negative months (borrow from year)
            if months < 0:
                years -= 1
                months += 12

            parts = []
            if years > 0:
                parts.append("{0} {1}".format(years, _("year") if years == 1 else _("years")))
            if months > 0:
                parts.append("{0} {1}".format(months, _("month") if months == 1 else _("months")))
            if days > 0:
                parts.append("{0} {1}".format(days, _("day") if days == 1 else _("days")))

            if len(parts) > 1:
                last_part = parts.pop()
                return _("{parts_str} and {last_part}").format(parts_str=", ".join(parts), last_part=last_part)
            elif parts:
                return parts[0]
            else:
                return _("a wonderful time")

        except Exception:
            return _("an unforgettable time")

    def getTotalDaysSinceInstall():
        """Return total days since first MAS session as integer."""
        if not (store.persistent.sessions
            and "first_session" in store.persistent.sessions
            and store.persistent.sessions["first_session"]
        ):
            return 0

        try:
            start_datetime = store.persistent.sessions["first_session"]
            start_date = start_datetime.date()
            current_date = datetime.date.today()
            delta = current_date - start_date
            return delta.days
        except Exception:
            return 0

    def getYearsSinceInstall():
        """Return completed years since first MAS session, accounting for leap years."""
        if not (store.persistent.sessions
            and "first_session" in store.persistent.sessions
            and store.persistent.sessions["first_session"]
        ):
            return 0

        try:
            start_datetime = store.persistent.sessions["first_session"]
            start_date = start_datetime.date()
            current_date = datetime.date.today()

            # Calculate actual years by comparing dates
            years = current_date.year - start_date.year

            # Subtract a year if we haven't reached the anniversary date yet
            if (current_date.month, current_date.day) < (start_date.month, start_date.day):
                years -= 1

            return max(0, years)
        except Exception:
            return 0

    def getMasStats():
        """Collects friendly MAS session stats for display."""
        stats = {}
        if not store.persistent.sessions:
            return {
                _("The Day We Met <3"): _("Not yet recorded"),
                _("Total Visits"): "0",
                _("Our Time Together"): "N/A",
                _("Avg. Visit Time"): "N/A"
            }

        first_session = store.persistent.sessions.get("first_session")
        total_playtime = store.persistent.sessions.get("total_playtime", datetime.timedelta())
        total_sessions = store.persistent.sessions.get("total_sessions", 0)

        stats[_("The Day We Met <3")] = first_session.strftime("%B %d, %Y") if first_session else _("Unknown")
        stats[_("Total Visits")] = str(total_sessions)
        h, rem = divmod(total_playtime.total_seconds(), 3600)
        m, s = divmod(rem, 60)
        stats[_("Our Time Together")] = "{:02.0f}h {:02.0f}m".format(h, m)
        if total_sessions > 0:
            avg_playtime = total_playtime / total_sessions
            h_avg, rem_avg = divmod(avg_playtime.total_seconds(), 3600)
            m_avg, s_avg = divmod(rem_avg, 60)
            stats[_("Avg. Visit Time")] = "{:02.0f}h {:02.0f}m".format(h_avg, m_avg)
        else:
            stats[_("Avg. Visit Time")] = "N/A"

        return stats

    # --- Utility Functions ---
    def filtered_clipboard_text(allowed_chars):
        """Get clipboard text, filter by allowed_chars, return or 'cancel'."""
        import pygame
        try:
            pygame.scrap.init()
            clipboard_bytes = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)

            if clipboard_bytes:
                clipboard_text = clipboard_bytes.decode("utf-8", "ignore")
                return "".join(char for char in clipboard_text if char in allowed_chars)
            else:
                renpy.notify(_("Your clipboard is empty."))
                return "cancel"
        except Exception:
            renpy.notify(_("Could not access clipboard."))
            return "cancel"

    # --- Dating and Label Helpers ---
    def check_seen_background(first_time, alternate, stop_date):
        """Handle affection and label jump based on background seen status."""
        if store.ep_affection.getCurrentAffection() < 400:
            renpy.jump(stop_date)

        if renpy.seen_label(first_time):
            store.mas_gainAffection(1, bypass=True)
            renpy.jump(alternate)
        else:
            store.mas_gainAffection(5, bypass=True)

    def manage_date_location(locate=True):
        """Save or load the current room's chair, table, and background for dates."""
        if locate:
            # Save current chair and table
            store.ep_dates.chair = store.monika_chr.tablechair.chair
            store.ep_dates.table = store.monika_chr.tablechair.table
            store.ep_dates.old_bg = store.mas_current_background

        else:
            # Restore chair and table
            if store.ep_dates.chair is not None:
                store.monika_chr.tablechair.chair = store.ep_dates.chair
            else:
                store.monika_chr.tablechair.chair = "def" # MAS default value

            if store.ep_dates.table is not None:
                store.monika_chr.tablechair.table = store.ep_dates.table
            else:
                store.monika_chr.tablechair.table = "def" # MAS default value

            # Restore background (most critical)
            if store.ep_dates.old_bg is not None:
                store.mas_current_background = store.ep_dates.old_bg
            else:
                # If old_bg is lost, force default Spaceroom to avoid crash
                store.mas_current_background = store.mas_background_def
            
            # Restore holiday visuals if active
            # O31 (Halloween)
            if store.persistent._mas_o31_in_o31_mode:
                store.mas_o31ShowVisuals()
            
            # D25 (Christmas)
            if store.persistent._mas_d25_deco_active:
                store.mas_d25ShowVisuals()
            
            # Birthday
            if store.persistent._mas_bday_in_bday_mode or store.persistent._mas_bday_visuals:
                store.mas_surpriseBdayShowVisuals()

    def check_seen_label(first_time, alternate):
        """Jump to alternate if first_time has been seen."""
        if renpy.seen_label(first_time):
            renpy.jump(alternate)

    def ep_input(
        prompt,
        default="",
        allow=None,
        exclude="{}",
        length=None,
        screen_kwargs=None
    ):
        """
        Enhanced input function with clipboard paste support.
        Works like mas_input but uses extra_input screen with a Paste button.
        
        IN:
            prompt - text prompt to display
            default - default text value (Default: "")
            allow - characters to allow (Default: None = all)
            exclude - characters to exclude (Default: "{}")
            length - max length of input (Default: None)
            screen_kwargs - additional kwargs for the screen (Default: None)
            
        OUT:
            entered string, or "cancel_input" if cancelled
        """
        if screen_kwargs is None:
            screen_kwargs = {}
        
        # Set defaults for our enhanced screen
        if "use_return_button" not in screen_kwargs:
            screen_kwargs["use_return_button"] = True
        if "use_paste_button" not in screen_kwargs:
            screen_kwargs["use_paste_button"] = True
        
        # Allowed chars for filtering clipboard
        allowed_chars = allow
        
        # Loop until we get valid input (handles paste retry)
        while True:
            # Call the input with our enhanced screen
            result = store.mas_input(
                prompt,
                default=default,
                allow=allow,
                exclude=exclude,
                length=length,
                screen="extra_input",
                screen_kwargs=screen_kwargs
            )
            
            # Check if user clicked Paste button
            if result == "__EP_PASTE_FROM_CLIPBOARD__":
                # Get text from clipboard
                clipboard_text = filtered_clipboard_text(allowed_chars or "")
                
                if clipboard_text and clipboard_text != "cancel":
                    # Truncate if length limit
                    if length and len(clipboard_text) > length:
                        clipboard_text = clipboard_text[:length]
                    
                    # Use clipboard text as new default and show again
                    default = clipboard_text
                    continue
                else:
                    # Clipboard empty or error, just retry
                    continue
            
            # Normal input or cancel
            return result

# Store: ep_chibis
# Handles Chibi-related logic, classes, and UI helpers.
init -5 python in ep_chibis:
    import store
    from renpy.display.layout import LiveComposite

    # --- Chibi Management Functions ---
    def init_chibi():
        store.ep_tools.safe_overlay_add("doki_chibi_idle")

    def remove_chibi():
        store.ep_tools.safe_overlay_remove("doki_chibi_idle")

    def add_remv_chibi(screen="doki_chibi_idle"):
        # This function acts as a toggle.
        try:
            if screen in renpy.config.overlay_screens:
                renpy.config.overlay_screens.remove(screen)
                renpy.hide_screen(screen)
            else:
                renpy.config.overlay_screens.append(screen)
        except Exception:
            pass

    def reset_chibi():
        remove_chibi()
        init_chibi()

    def draw_background_accessories(st, at):
        # Return the image directly without LiveComposite wrapper (only 1 image)
        return store.MASFilterSwitch(
            store.ep_chibis.accessory_path_2.format(store.persistent.chibi_accessory_3_)
        ), 1

    def draw_foreground_accessory_1(st, at):
        # Return the image directly without LiveComposite wrapper (only 1 image)
        return store.MASFilterSwitch(
            store.ep_chibis.accessory_path_0.format(store.persistent.chibi_accessory_1_)
        ), 1

    def draw_foreground_accessory_2(st, at):
        # Return the image directly without LiveComposite wrapper (only 1 image)
        return store.MASFilterSwitch(
            store.ep_chibis.accessory_path_1.format(store.persistent.chibi_accessory_2_)
        ), 1

    def migrate_chibi_costume_data():
        """
        Migrates chibi costume data from older formats to the current format.
        Handles upgrades from Stable (1.1.0) and BETA 2 (1.3.2) to BETA 3 (1.4.1+).
        """
        try:
            costume = store.persistent.chibika_current_costume
            
            # Case 1: Coming from Stable (1.1.0) or BETA 2 (1.3.2) - list format
            if isinstance(costume, list):
                store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika
                return
            
            # Case 2: Already a tuple - verify it's the correct new format (4 elements)
            if isinstance(costume, tuple):
                # Old tuple format had 3 elements (sprites only), new format has 4 (folder + sprites)
                if len(costume) != 4:
                    store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika
                    return
                
                # Verify the folder is valid
                valid_folders = ["darling", "cupcake", "cinnamon", "teacup"]
                if costume[0] not in valid_folders:
                    store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika
                    return
                    
                # Verify the sprite file exists (optional - only reset if assets are missing)
                sprite_path = store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, costume[0], "{}.png".format(costume[1]))
                if not renpy.loadable(sprite_path):
                    store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika
                    
        except Exception as e:
            # If anything goes wrong, reset to default to prevent crashes
            store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika

    class DokiAccessory(object):
        """Callable action that equips an accessory to the chibi."""
        __slots__ = ['name', 'acc', 'slot']
        
        def __init__(self, name, acc, slot):
            self.name = name
            self.acc = acc
            self.slot = slot  # 'primary', 'secondary', or 'background'

        def __call__(self):
            if self.slot == "primary":
                store.persistent.chibi_accessory_1_ = self.acc
            elif self.slot == "secondary":
                store.persistent.chibi_accessory_2_ = self.acc
            else:
                store.persistent.chibi_accessory_3_ = self.acc

    class SelectDOKI():
        """Callable action that changes the chibi's costume."""
        def __init__(self, name, costume):
            self.name = name
            self.costume = costume  # Tuple: (folder, idle, blink, hover)

        def __call__(self):
            store.persistent.chibika_current_costume = self.costume
            store.ep_chibis.reset_chibi()
            renpy.jump("extra_chibi_main")

    def show_costume_menu(costumes, return_label):
        dokis_items = [SelectDOKI(name, cost) for name, cost in costumes]
        items = [(_("Nevermind"), return_label, 20)]
        renpy.call_screen("extra_gen_list", dokis_items, store.mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items)

    def chibi_drag(drags, drop):
        """Handle Chibika's drag and drop movement."""
        try:
            store.persistent.chibika_drag_x = drags[0].x
            store.persistent.chibika_drag_y = drags[0].y
        except Exception:
            # Defensive: ignore if structure isn't as expected
            pass
    
    def clicker():
        """Handles the logic when the chibi is clicked repeatedly."""
        try:
            current_char = store.persistent.chibika_current_costume[0]
        except (IndexError, TypeError):
            current_char = "darling"

        # Increment counter
        store.ep_chibis.temp_chibi_clicks += 1
        
        clicks = store.ep_chibis.temp_chibi_clicks

        # Data-driven responses for different click thresholds
        responses = {
            10: { # These are all user-facing strings
                "darling": _("Hey! That's me."),
                "cupcake": _("What do you think you're doing?!"),
                "cinnamon": _("Ehehe! That tickles."),
                "teacup": _("A-ah... please..."),
                "default": _("Hey!")
            },
            20: {
                "darling": _("Stop poking me, [player]!"),
                "cupcake": _("Stop it, baka!"),
                "cinnamon": _("Will you give me a cookie if you stop?"),
                "teacup": _("You're making me nervous..."),
                "default": _("Stop it!")
            },
            30: {
                "darling": _("I'm serious, [player]!"),
                "cupcake": _("I'm going to bite your finger!"),
                "cinnamon": _("I'm getting dizzy..."),
                "teacup": _("I-I'm... going to go hide..."),
                "default": _("I'm warning you!")
            },
            50: {
                "darling": _("Bye-Bye!"),
                "cupcake": _("Hmph! I'm not playing anymore!"),
                "cinnamon": _("Waaa! I'm going to my cloud!"),
                "teacup": _("I'm sorry... goodbye."),
                "default": _("That's it, I'm done!")
            }
        }

        if clicks in responses:
            message = renpy.substitute(responses[clicks].get(current_char, responses[clicks]["default"]))
            store.ep_chibis.chibika_notify(message,current_char)

        if clicks >= 50:
            renpy.show_screen("chibi_visual_effect", x=xpos, y=ypos)
            store.ep_chibis.temp_chibi_anger = True
            store.ep_chibis.remove_chibi()
            store.ep_chibis.temp_chibi_clicks = 0 # Reset for the next time

    # --- Accessory Screen Management ---
    def set_accessory_category(category):
        """
        Sets the current accessory category on the screen without changing button focus.
        """
        try:
            # Get the context for the current screen and set the variable
            store.renpy.get_screen("gen_accessories_twopane_screen").scope["EP_current_acc"] = category
            store.renpy.restart_interaction() # Refresh the screen to show changes
        except Exception:
            # Failsafe in case the screen is not active
            pass

    def getCurrentAccessories(category):
        """
        Returns the list of accessories for the given category.
        """
        category_map = {
            "primary": store.ep_chibis.getPrimaryAccessories,
            "secondary": store.ep_chibis.getSecondaryAccessories,
            "background": store.ep_chibis.getBackgroundAccessories
        }
        getter = category_map.get(category)
        return getter() if getter else []

    def getCurrentRemoveAction(category):
        """
        Returns the 'Remove' action object for the given category.
        """
        remove_actions = {
            "primary": store.ep_chibis.DokiAccessory(_("Remove"), "0nothing", "primary"),
            "secondary": store.ep_chibis.DokiAccessory(_("Remove"), "0nothing", "secondary"),
            "background": store.ep_chibis.DokiAccessory(_("Remove"), "0nothing", "background")
        }
        return remove_actions.get(category)

    def chibika_notify(txt, doki="darling", jump=False):
        """
        Shows a notification from Chibika.
        
        IN:
            txt - message to display
            doki - icon to use ("darling", "cupcake", "cinnamon", "teacup")
            jump - if True, triggers a jump animation (default: False)
        """
        # Show the notification
        renpy.show_screen("chibika_notify", message=txt, icon=doki)
        
        # Trigger jump animation if requested and conditions are met
        if jump:
            try:
                chibi_visible = "doki_chibi_idle" in renpy.config.overlay_screens
                not_draggable = not store.persistent.enable_drag_chibika
                current_doki = store.persistent.chibika_current_costume[0]
                doki_matches = (doki == current_doki)
                
                if chibi_visible and not_draggable and doki_matches:
                    # Set the jumping flag - the screen will handle the animation
                    store.ep_chibis.is_jumping = True
                    renpy.restart_interaction()  # Force screen refresh
            except Exception:
                pass

    def getPrimaryAccessories():
        """Returns primary accessories as DokiAccessory list."""
        return [
            store.ep_chibis.DokiAccessory(name, filename, "primary")
            for name, filename in _primary_data
        ]

    def getSecondaryAccessories():
        """Returns secondary accessories as DokiAccessory list."""
        return [
            store.ep_chibis.DokiAccessory(name, filename, "secondary")
            for name, filename in _secondary_data
        ]

    def getBackgroundAccessories():
        """Returns background accessories as DokiAccessory list."""
        return [
            store.ep_chibis.DokiAccessory(name, filename, "background")
            for name, filename in _background_data
        ]
        
# Store: ep_fridge
# Fridge Magnet Game
init python in ep_fridge:
    import datetime
    import renpy.store as store
    import renpy.exports as renpy
    import pygame
    
    EP_FM_FONT = "gui/font/RifficFree-Bold.ttf"

    Color = store.Color # Import Color

    # List of phrases Monika can put on the fridge
    monika_magnet_phrases = [
        [": 3"], ["< 3"], [": P"], ["> . <"], [": D"],
        ["H I"], ["L O V E"], ["D O K I"], ["I L V"]
    ]

    def getCoffeeData():
        """
        Gets coffee stock data from MAS consumable system.
        
        OUT:
            dict with keys:
                - stock: current servings left
                - max: maximum stock amount
                - percent: stock as percentage (0.0 to 1.0)
                - has_coffee: True if Monika has at least 1 serving
                - enabled: True if coffee is enabled
        """
        try:
            coffee = store.mas_getConsumable("coffee")
            if coffee is None:
                return {"stock": 0, "max": 150, "percent": 0.0, "has_coffee": False, "enabled": False}
            
            stock = coffee.getStock()
            max_stock = coffee.max_stock_amount
            percent = float(stock) / float(max_stock) if max_stock > 0 else 0.0
            
            return {
                "stock": stock,
                "max": max_stock,
                "percent": percent,
                "has_coffee": coffee.hasServing(),
                "enabled": coffee.enabled()
            }
        except Exception:
            return {"stock": 0, "max": 150, "percent": 0.0, "has_coffee": False, "enabled": False}

    def getCurrentColor(base_color):
        # If it's night, darken the color.
        if store.mas_isNightNow():
            return base_color.shade(0.6)
        
        # If it's day, return the original vibrant color
        return base_color

    class Magnet(object):
        """A single magnet on the fridge with position, rotation, and color."""
        __slots__ = ['letter', 'x', 'y', 'rotation', 'hsv', 'base_color', 'shadow_base_color']
        
        # We update __init__ to accept saved data
        def __init__(self, letter, x=0, y=0, rotation=0, hsv=None):
            self.letter = letter
            self.x = x
            self.y = y
            self.rotation = rotation
            
            # If we are given a saved color (HSV), we use it. Otherwise, we create a new one.
            if hsv:
                self.hsv = hsv
            else:
                hue = renpy.random.random()
                self.hsv = (hue, 0.75, 0.95)
            
            # We reconstruct the Color objects from the data
            self.base_color = Color(hsv=self.hsv)
            self.shadow_base_color = self.base_color.shade(0.6)

    class MagnetManager(object):
        def __init__(self):
            self.magnets = [
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z",
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "?", "!", "#", "@", "&", "+", "-", "=", "~"
            ]
            self.top = []
            self.bottom = []
            self.holding = None
            self.event_handler = EventHandler()
            
            # --- Monika's logic for adding magnets ---
            today_str = str(datetime.date.today())
            
            # Load existing magnets FIRST so collision detection works
            self.load()
            
            # If Monika hasn't posted today, there's a chance she will.
            if store.persistent._ep_fridge_last_monika_post != today_str:
                # We give a 1 in 3 chance so she doesn't do it every day
                if renpy.random.randint(1, 3) == 1:
                    self.monika_adds_magnets()
                    self.save()  # Save Monika's new magnets
                    store.persistent._ep_fridge_last_monika_post = today_str 


        def take(self):
            renpy.play(store.sfx_take_frigde, "sound")
            # Get the mouse position BEFORE creating the magnet
            mouse_pos = renpy.get_mouse_pos()
            m = Magnet(renpy.random.choice(self.magnets))
            m.rotation = renpy.random.randint(-15, 15)
            # Assign the mouse position immediately
            m.x, m.y = mouse_pos[0], mouse_pos[1]
            self.holding = m

        def put(self, place):
            if self.holding:
                renpy.play(store.sfx_place_fridge, "sound")
                if place == "top":
                    self.top.append(self.holding)
                    self.holding = None
                elif place == "bottom":
                    self.bottom.append(self.holding)
                    self.holding = None
                else:
                    self.holding = None
                # We save every time a magnet is placed
                self.save()
            
        def tick(self):
            if self.holding:
                pos = renpy.get_mouse_pos()
                self.holding.x = pos[0]
                self.holding.y = pos[1]
                if self.event_handler.active:
                    self.holding.rotation += self.event_handler.active
                    if self.holding.rotation > 360:
                        self.holding.rotation -= 360

        def swap(self, place, letter):
            # Get the mouse position for the new magnet
            mouse_pos = renpy.get_mouse_pos()

            if place == "top":
                self.top.remove(letter)
            else:
                self.bottom.remove(letter)
            self.put(place)
            # Assign the mouse position to the magnet we are going to hold
            letter.x, letter.y = mouse_pos[0], mouse_pos[1]
            self.holding = letter
            
        def clean_magnets(self):
            """Cleans all magnets from the fridge."""
            self.top = []
            self.bottom = []
            self.save() # Save the empty state

        def _check_collision(self, x, y, width, height):
            """
            Checks if a rectangle (a potential magnet) collides with any existing magnet.
            Returns True if there is a collision, False otherwise.
            """
            # Coordinates of the new magnet
            new_left = x - width / 2
            new_right = x + width / 2
            new_top = y - height / 2
            new_bottom = y + height / 2

            # We check against all existing magnets
            all_magnets = self.top + self.bottom
            for magnet in all_magnets:
                # Coordinates of the existing magnet (approximate)
                existing_left = magnet.x - width / 2
                existing_right = magnet.x + width / 2
                existing_top = magnet.y - height / 2
                existing_bottom = magnet.y + height / 2

                # AABB collision logic (Axis-Aligned Bounding Box)
                if (new_left < existing_right and new_right > existing_left and
                        new_top < existing_bottom and new_bottom > existing_top):
                    return True # Collision detected!

            return False # No collisions found

        def monika_adds_magnets(self):
            """Monika chooses a phrase and places it on the fridge."""
            phrase_to_add = renpy.random.choice(monika_magnet_phrases)
            magnet_width = 80 # Approximate width of each magnet

            # We try to find a free spot up to 50 times
            for attempt in range(50):
                start_x = renpy.random.randint(250, 650)
                start_y = renpy.random.randint(50, 150)
                is_valid_spot = True

                # We check if the whole phrase fits without colliding
                for i, word in enumerate(phrase_to_add):
                    check_x = start_x + (i * magnet_width)
                    if self._check_collision(check_x, start_y, magnet_width, 70):
                        is_valid_spot = False
                        break # If a magnet collides, this spot is not valid

                # If we find a valid spot, we place the magnets and exit the loop
                if is_valid_spot:
                    for i, word in enumerate(phrase_to_add):
                        new_magnet = Magnet(word, x=0, y=0)
                        new_magnet.x = start_x + (i * magnet_width)
                        new_magnet.y = start_y + renpy.random.randint(-10, 10) # Small vertical variation
                        new_magnet.rotation = renpy.random.randint(-10, 10)
                        self.top.append(new_magnet)
                    return # We exit the monika_adds_magnets function

        # --- SAVE AND LOAD SYSTEM ---
        def save(self):
            """Serializes Magnet objects into simple dictionaries to save them."""
            data = {
                "top": [],
                "bottom": []
            }
            
            for m in self.top:
                data["top"].append({
                    "letter": m.letter, "x": m.x, "y": m.y, 
                    "rotation": m.rotation, "hsv": m.hsv
                })
                
            for m in self.bottom:
                data["bottom"].append({
                    "letter": m.letter, "x": m.x, "y": m.y, 
                    "rotation": m.rotation, "hsv": m.hsv
                })
                
            store.persistent._ep_fridge_magnets_data = data

        def load(self):
            """Reconstructs the magnets from the saved data."""
            data = store.persistent._ep_fridge_magnets_data
            # Ensure data is a dict (fixes corrupted persistent)
            if not isinstance(data, dict):
                return # No valid data, we start empty
            
            for d in data.get("top", []):
                self.top.append(Magnet(d["letter"], d["x"], d["y"], d["rotation"], d["hsv"]))
            for d in data.get("bottom", []):
                self.bottom.append(Magnet(d["letter"], d["x"], d["y"], d["rotation"], d["hsv"]))

    class EventHandler(renpy.Displayable):
        def __init__(self):
            super(renpy.Displayable, self).__init__()
            self.active = 0
            
        def render(self, width, height, st, at):
            return renpy.Render(0, 0)
            
        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_d:
                    self.active = 2
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_a:
                    self.active = -2
                    raise renpy.IgnoreEvent()
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_d:
                    self.active = 0
                elif ev.key == pygame.K_a:
                    self.active = 0
            return None

init -10 python in ep_tools:
    # Overlay safety wrapper
    def safe_overlay_add(screen):
        try:
            if screen not in renpy.config.overlay_screens:
                renpy.config.overlay_screens.append(screen)
        except Exception:
            pass
    
    def safe_overlay_remove(screen):
        try:
            if screen in renpy.config.overlay_screens:
                renpy.config.overlay_screens.remove(screen)
                renpy.hide_screen(screen)
        except Exception:
            pass

#==============================================================================
# 4. MINIGAME HELPER STORES
#==============================================================================
# Store: ep_sg (Shell Game)
init -10 python in ep_sg:
    import store
    
    def randomize_cup_skin():
        if store.persistent._mas_pm_cares_about_dokis: 
            return renpy.random.choice(["monika.png", "yuri.png", "natsuki.png", "sayori.png"])
        return renpy.random.choice(["cup.png", "monika.png"])


# These classes provide boop/interaction zone functionality
# Using EP prefix to avoid conflicts with MAS classes
#
# ============================================================================
# CREDITS & ACKNOWLEDGMENTS
# ============================================================================
# The interaction zone system (clickzone detection, zoom calculations, and
# polygon intersection algorithms) is based on code from the Monika After
# Story project.
#
# Original code by the Monika After Story Team
# Repository: https://github.com/Monika-After-Story/MonikaModDev
#
# A huge thank you to the MAS Team for their incredible work on the mod
# and for making their code available. Your dedication to the community
# and to Monika is truly inspiring. <3
# ============================================================================

init -15 python:
    import pygame
    
    class EPLinearForm(object):
        """
        Representation of linear functions for edge calculations.
        """
        THRESH = 0.001

        def __init__(self, xdiff, ydiff, yint):
            self.xdiff = xdiff
            self.ydiff = ydiff
            self._fxdiff = float(xdiff)

            if xdiff == 0:
                self.yint = None
            elif ydiff == 0:
                self.yint = 0
            else:
                self.yint = yint

        def getx(self, y):
            if self.yint is None:
                return None
            if self.ydiff == 0:
                return None
            return self._getx(y)

        def gety(self, x):
            if self.yint is None:
                return None
            return self._gety(x)

        @staticmethod
        def diffPoints(p1, p2):
            lp, rp = EPLinearForm.sortPoints(p1, p2)
            return rp[0] - lp[0], rp[1] - lp[1]

        @staticmethod
        def fromPoints(p1, p2):
            xdiff, ydiff = EPLinearForm.diffPoints(p1, p2)
            yint = EPLinearForm.yintPoints(p1, p2)
            return EPLinearForm(xdiff, ydiff, yint)

        @staticmethod
        def sortPoints(p1, p2):
            if p1[0] < p2[0]:
                return p1, p2
            return p2, p1

        @staticmethod
        def yintPoints(p1, p2):
            xdiff, ydiff = EPLinearForm.diffPoints(p1, p2)
            if xdiff == 0:
                return None
            elif ydiff == 0:
                return 0

            lp, rp = EPLinearForm.sortPoints(p1, p2)
            lx, ly = lp

            if lx == 0:
                return lp[1]

            pot_yint = ly - ((ydiff * lx) / float(xdiff))
            if abs(int(pot_yint) - pot_yint) < EPLinearForm.THRESH:
                pot_yint = int(pot_yint)
            return pot_yint

        def _getx(self, y):
            return (y - self.yint) / self._slope()

        def _gety(self, x):
            return self._slope(x) + self.yint

        def _slope(self, x=1):
            return (self.ydiff * x) / self._fxdiff


    class EPEdge(object):
        """
        Representation of an edge (line with 2 points) for polygon calculations.
        """

        def __init__(self, p1, p2):
            self._horizontal = False
            self._vertical = False
            self._left_point = None
            self._right_point = None
            self.__bb_x_min = None
            self.__bb_x_max = None
            self.__bb_y_min = None
            self.__bb_y_max = None
            self.__norm_lp = (0, 0)
            self.__norm_rp = None
            self.__line = None
            self.__setup(p1, p2)

        def inBoundingBox(self, x, y):
            return self._inBoundingBoxX(x) and self._inBoundingBoxY(y)

        def horizontalIntersect(self, x, y):
            if self._horizontal:
                return False
            if not self._inBoundingBoxY(y):
                return False
            if self.__bb_x_max < x:
                return False
            if x < self.__bb_x_min:
                return True
            if self._vertical:
                return x <= self.__bb_x_min
            x, y = self._normalize((x, y))
            return x <= self.__line._getx(y)

        def _inBoundingBoxX(self, x):
            return self.__bb_x_min <= x <= self.__bb_x_max

        def _inBoundingBoxY(self, y):
            return self.__bb_y_min <= y <= self.__bb_y_max

        def __setup(self, p1, p2):
            self.__setupPoints(p1, p2)
            self.__setupBoundingBox()
            self.__setupNormalizedPoints()
            self.__setupLinearFunction()

        def __setupBoundingBox(self):
            self.__bb_x_min = self._left_point[0]
            self.__bb_x_max = self._right_point[0]
            self.__bb_y_min = min(self._left_point[1], self._right_point[1])
            self.__bb_y_max = max(self._left_point[1], self._right_point[1])

        def __setupLinearFunction(self):
            self.__line = EPLinearForm.fromPoints(self.__norm_lp, self.__norm_rp)

        def __setupNormalizedPoints(self):
            self.__norm_rp = EPLinearForm.diffPoints(self._left_point, self._right_point)

        def __setupPoints(self, p1, p2):
            p1x, p1y = p1
            p2x, p2y = p2
            if p1x == p2x:
                self._vertical = True
            elif p1y == p2y:
                self._horizontal = True
            self._left_point, self._right_point = EPLinearForm.sortPoints(p1, p2)

        def _normalize(self, point):
            return (
                point[0] - self._left_point[0],
                point[1] - self._left_point[1]
            )


    class EPClickZone(renpy.Displayable):
        """
        Special mousezone that can react when clicked.
        Used for boop and other touch interactions.
        """
        LEFT_CLICK = 1
        MIDDLE_CLICK = 2
        RIGHT_CLICK = 3

        def __init__(self, corners):
            if len(corners) <= 0:
                raise Exception("Clickzone cannot be built with empty corners")

            super(renpy.Displayable, self).__init__()

            self.corners = corners
            self.disabled = False
            self._debug_back = False
            self.__edges = []
            self._button_down = pygame.MOUSEBUTTONUP
            self.__click_start = [False, False, False]
            self.__setup()

        @staticmethod
        def copyfrom(other, new_vx):
            new_cz = EPClickZone(new_vx)
            new_cz.disabled = other.disabled
            new_cz._debug_back = other._debug_back
            new_cz._button_down = other._button_down
            return new_cz

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            if self._debug_back:
                canvas = r.canvas()
                canvas.polygon("#FFE6F4", self.corners, width=0)
            return r

        def event(self, ev, x, y, st):
            if ev.type == self._button_down and not self.disabled:
                if self._isOverMe(x, y):
                    return ev.button
            return None

        def _inBoundingBox(self, x, y):
            return (
                self.__bb_x_min <= x <= self.__bb_x_max
                and self.__bb_y_min <= y <= self.__bb_y_max
            )

        def _isOverMe(self, x, y):
            if not self._inBoundingBox(x, y):
                return False
            intersections = 0
            for edge in self.__edges:
                intersections += int(edge.horizontalIntersect(x, y))
            return (intersections % 2) == 1

        def __setup(self):
            self.__setupBoundingBox()
            self.__setupEdges()

        def __setupBoundingBox(self):
            self.__bb_x_min = self.corners[0][0]
            self.__bb_x_max = self.corners[0][0]
            self.__bb_y_min = self.corners[0][1]
            self.__bb_y_max = self.corners[0][1]

            for index in range(1, len(self.corners)):
                x, y = self.corners[index]
                self.__bb_x_min = min(self.__bb_x_min, x)
                self.__bb_x_max = max(self.__bb_x_max, x)
                self.__bb_y_min = min(self.__bb_y_min, y)
                self.__bb_y_max = max(self.__bb_y_max, y)

            self.__width = self.__bb_x_max - self.__bb_x_min
            self.__height = self.__bb_y_max - self.__bb_y_min

        def __setupEdges(self):
            for index in range(len(self.corners) - 1):
                self.__edges.append(EPEdge(self.corners[index], self.corners[index + 1]))
            self.__edges.append(EPEdge(self.corners[0], self.corners[-1]))


init -14 python in ep_interactions:
    """
    Interaction zone manager classes for ExtraPlus.
    """
    import store
    import math
    
    # Get zoom level functions from mas_sprites if available
    try:
        import store.mas_sprites as mas_sprites
        _has_zoom = True
        _default_zoom = mas_sprites.default_zoom_level
        _y_step = getattr(mas_sprites, 'y_step', 10)
    except (ImportError, AttributeError):
        _has_zoom = False
        _default_zoom = 3
        _y_step = 10
    
    ZOOM_INC_PER = 0.04
    FOCAL_POINT = (640, 750)
    FOCAL_POINT_UP = (640, 740)
    
    
    def _get_zoom_level():
        """Get current zoom level safely."""
        try:
            return store.mas_sprites.zoom_level
        except (AttributeError, NameError):
            return _default_zoom
    
    
    def vx_list_zoom(zoom_level, vx_list):
        """
        Generates a vertex list adjusted for zoom level.
        """
        if zoom_level == _default_zoom:
            return list(vx_list)
        
        zoom_out = zoom_level < _default_zoom
        
        if zoom_out:
            zoom_diff = _default_zoom - zoom_level
            per_mod = -1 * (zoom_diff * ZOOM_INC_PER)
            xfc, yfc = FOCAL_POINT
            yfc_offset = 0
        else:
            zoom_diff = zoom_level - _default_zoom
            per_mod = zoom_diff * ZOOM_INC_PER
            xfc, yfc = FOCAL_POINT_UP
            yfc_offset = -1 * zoom_diff * _y_step
        
        new_vx_list = []
        for xcoord, ycoord in vx_list:
            xcoord -= xfc
            ycoord -= (yfc + yfc_offset)
            
            # Convert to polar
            radius = math.sqrt(xcoord * xcoord + ycoord * ycoord)
            angle = math.atan2(ycoord, xcoord)
            
            # Modify radius
            radius += (radius * per_mod)
            
            # Convert back to rectangular
            new_x = radius * math.cos(angle)
            new_y = radius * math.sin(angle)
            
            new_vx_list.append((int(new_x + xfc), int(new_y + yfc)))
        
        return new_vx_list
    
    
    class EPClickZoneManager(object):
        """
        Manages clickzones with varying zoom levels.
        Automates caching for different zoom levels.
        """

        def __init__(self):
            self._zoom_cz = {}
            self._zones = {}

        def __contains__(self, item):
            return item in self._zones

        def __getitem__(self, key):
            return self.get(key, _get_zoom_level())

        def __iter__(self):
            for zone_key in self._zones:
                yield zone_key, self[zone_key]

        def add(self, zone_key, cz):
            """Adds a clickzone to this manager."""
            if zone_key in self._zones:
                return

            self._zones[zone_key] = cz
            cz_d = self._zoom_cz.get(_default_zoom, {})
            cz_d[zone_key] = cz
            self._zoom_cz[_default_zoom] = cz_d

        def _cz_iter(self):
            for zl, zl_d in self._zoom_cz.iteritems():
                for zone_key, cz in zl_d.iteritems():
                    yield zone_key, zl, cz

        def _debug(self, value):
            for zk, zl, cz in self._cz_iter():
                cz._debug_back = value

        def get(self, zone_key, zl):
            """Gets a clickzone for a specific zoom level."""
            if zl not in self._zoom_cz:
                self.zoom_to(zl)
            return self._zoom_cz.get(zl, {}).get(zone_key, None)

        def remove(self, zone_key):
            """Removes a clickzone from this manager."""
            if zone_key not in self._zones:
                return
            self._zones.pop(zone_key)
            for zone_d in self._zoom_cz.itervalues():
                if zone_key in zone_d:
                    zone_d.pop(zone_key)

        def set_disabled(self, zone_key, value):
            """Sets disabled state for all zoom levels of a zone."""
            for zl_d in self._zoom_cz.itervalues():
                cz = zl_d.get(zone_key, None)
                if cz is not None:
                    cz.disabled = value

        def zoom_to(self, zoom_level):
            """Generates clickzones for a zoom level."""
            zl_set = self._zoom_cz.get(zoom_level, {})

            for zone_key, cz in self._zones.iteritems():
                if zone_key not in zl_set:
                    new_cz = store.EPClickZone.copyfrom(
                        cz,
                        vx_list_zoom(zoom_level, cz.corners)
                    )
                    zl_set[zone_key] = new_cz

            self._zoom_cz[zoom_level] = zl_set


    class EPZoomableInteractable(renpy.Displayable):
        """
        Interactable designed for use with EPClickZones and zooming.
        """
        ZONE_ACTION_NONE = 0
        ZONE_ACTION_RET = 1
        ZONE_ACTION_JUMP = 2
        ZONE_ACTION_END = 3
        ZONE_ACTION_RST = 4

        def __init__(
                self,
                cz_manager,
                zone_actions=None,
                zone_order=None,
                start_zoom=None,
                debug=False
        ):
            if zone_actions is None:
                zone_actions = {}
            if zone_order is None:
                zone_order = []
            if start_zoom is None:
                start_zoom = _get_zoom_level()

            self._cz_man = cz_manager
            self.zones_stat = {}
            self._zones_action = zone_actions
            self._zones_order = zone_order
            self._zones_unorder = {}

            self._last_zoom_level = start_zoom
            
            self._end_int = None
            self._rst_int = False
            self._jump_to = None
            self._zk_click = None
            self._ret_val = None

            self._debug = debug
            if debug:
                self._cz_man._debug(True)

            self._build_zones()

            super(EPZoomableInteractable, self).__init__()

        def add_zone(self, zone_key, cz):
            if zone_key in self._cz_man:
                return
            self._cz_man.add(zone_key, cz)
            if zone_key not in self._zones_order:
                self._zones_unorder[zone_key] = None
            if zone_key not in self.zones_stat:
                self.zones_stat[zone_key] = 0

        def adjust_for_zoom(self):
            current_zoom = _get_zoom_level()
            if self._last_zoom_level == current_zoom:
                return
            self._zone_zoom(current_zoom)
            self._last_zoom_level = current_zoom

        def _build_zones(self):
            for zone_key, cz in self._cz_man:
                self.zones_stat[zone_key] = 0
                if zone_key not in self._zones_order:
                    self._zones_unorder[zone_key] = None

        def check_click(self, ev, x, y, st):
            for zone_key, cz in self.zone_iter():
                if cz.event(ev, x, y, st) is not None:
                    return zone_key
            return None

        def check_over(self, x, y):
            for zone_key, cz in self.zone_iter():
                if cz._isOverMe(x, y):
                    return zone_key
            return None

        def clicks(self, zone_key):
            return self.zones_stat.get(zone_key, 0)

        def disable_zone(self, zone_key):
            self._cz_man.set_disabled(zone_key, True)

        def enable_zone(self, zone_key):
            self._cz_man.set_disabled(zone_key, False)

        def event(self, ev, x, y, st):
            self.event_begin(ev, x, y, st)
            return self.event_end(ev, x, y, st)

        def event_begin(self, ev, x, y, st):
            self.adjust_for_zoom()
            self._rst_int = False
            self._end_int = None
            self._jump_to = None
            self._ret_val = None

            self._zk_click = self.check_click(ev, x, y, st)
            if self._zk_click is not None:
                self.zones_stat[self._zk_click] += 1
                self._ret_val = self.zone_action(self._zk_click)

            return self._zk_click

        def event_end(self, ev, x, y, st):
            if self._jump_to is not None:
                renpy.jump(self._jump_to)

            if self._rst_int:
                renpy.restart_interaction()
            else:
                renpy.end_interaction(self._end_int)

            return self._ret_val

        def remove_zone(self, zone_key):
            self._cz_man.remove(zone_key)
            if zone_key in self._zones_unorder:
                self._zones_unorder.pop(zone_key)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            if not self._debug:
                return r

            renders = []
            for zone_key, cz in self.zone_iter_r():
                if not cz.disabled:
                    renders.append(renpy.render(cz, width, height, st, at))

            for render in renders:
                r.blit(render, (0, 0))

            return r

        def zone_action(self, zone_key):
            action = self._zones_action.get(zone_key, None)
            if action is None:
                return zone_key

            if isinstance(action, str):
                if renpy.has_label(action):
                    self._jump_to = action
                return action

            if action == 1:
                self._end_int = True
            elif action == 2:
                self._rst_int = True

            return None

        def zone_iter(self):
            for zone_key in self._zones_order:
                cz = self._cz_man[zone_key]
                if cz is not None:
                    yield zone_key, cz

            for zone_key in self._zones_unorder:
                yield zone_key, self._cz_man[zone_key]

        def zone_iter_r(self):
            for zone_key in self._zones_unorder:
                yield zone_key, self._cz_man[zone_key]

            for zone_key in self._zones_order:
                cz = self._cz_man[zone_key]
                if cz is not None:
                    yield zone_key, cz

        def _zone_zoom(self, zoom_level):
            self._cz_man.zoom_to(zoom_level)
