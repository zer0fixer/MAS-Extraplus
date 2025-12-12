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

    # Detect 'submods' folder case-insensitively
    EP_submods_folder = find_submods_folder()

    # --- SUBMOD BASE PATH DEFINITIONS ---
    EP_ROOT = _join_path(EP_submods_folder, "ExtraPlus")
    EP_MINIGAMES = _join_path(EP_ROOT, "minigames")
    EP_DATES = _join_path(EP_ROOT, "dates")
    EP_CHIBIS = _join_path(EP_ROOT, "chibis")
    EP_OTHERS = _join_path(EP_ROOT, "others")
    EP_SFX = _join_path(EP_ROOT, "sfx")

    # Minigames folders
    EP_MG_SHELLGAME = _join_path(EP_MINIGAMES, "shellgame")
    EP_MG_RPS = _join_path(EP_MINIGAMES, "rockpaperscissors")
    EP_MG_BLACKJACK = _join_path(EP_MINIGAMES, "blackjack")
    EP_MG_TICTACTOE = _join_path(EP_MINIGAMES, "tictactoe")
    EP_MG_FRIDGE = _join_path(EP_MINIGAMES, "fridgemagnets")

    # Dates folders
    EP_DATE_CAFE = _join_path(EP_DATES, "cafe")
    EP_DATE_RESTAURANT = _join_path(EP_DATES, "restaurant")
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
        import datetime

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
        import datetime
        if not store.persistent.EP_dynamic_button_text:
            return _("Extra+")

        conditions = _evaluate_current_conditions()
        today_str = str(datetime.date.today())
        conditions_key = _build_conditions_key(conditions)

        if (store.persistent.EP_button_last_update != today_str
            or store.persistent.EP_button_conditions_key != conditions_key
            or store.persistent.EP_button_text is None):
            new_text = _button_text_conditions(conditions)
            store.persistent.EP_button_text = new_text
            store.persistent.EP_button_last_update = today_str
            store.persistent.EP_button_conditions_key = conditions_key
        return store.persistent.EP_button_text

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
    class GiftAction:
        """Handles the creation of a gift file and notifies the player."""
        def __init__(self, name, gift):
            self.name = name
            self.gift = gift

        def __call__(self):
            if create_gift_file(self.gift):
                messages = [ # These are already wrapped in _()
                    _("All set! The '{}' gift is ready for you.").format(self.name),
                    _("Here's a '{}' for Monika! I hope she loves it.").format(self.name),
                    _("Perfect! Your '{}' is ready for Monika.").format(self.name),
                    _("A '{}' for Monika! It's all set.").format(self.name),
                    _("Your '{}' gift has been created!").format(self.name),
                    _("One '{}' gift, coming right up! It's ready.").format(self.name)
                ]
                store.ep_chibis.chibika_notify(random.choice(messages))
                store.mas_checkReactions()

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
        import os
        import datetime

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
            # Misc
            store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "coin_heads.png"),
            store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "coin_tails.png"),
            store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "sprite_coin.png"),
            store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "maxwell_cat.png")
        ]
        for asset in static_assets:
            check_file(asset, found_assets, missing_assets)

        # --- 2. Chibi Assets ---
        all_chibi_costumes = store.ep_chibis.monika_costumes_ + store.ep_chibis.natsuki_costumes_ + store.ep_chibis.sayori_costumes_ + store.ep_chibis.yuri_costumes_
        for _, costume_data in all_chibi_costumes:
            doki_folder, idle_sprite, blink_sprite, hover_sprite = costume_data # No store prefix here, these are local to the loop
            chibi_sprites = [idle_sprite, blink_sprite, hover_sprite]
            for sprite in chibi_sprites:
                path = store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, doki_folder, "{}.png".format(sprite))
                check_file(path, found_assets, missing_assets)

        # --- 3. Chibi Accessories ---
        # These lists should match the ones in Extra_Plus_Main.rpy
        primary_accessories = ["clown_hair", "cat_ears", "christmas_hat", "demon_horns", "flowers_crown", "fox_ears", "graduation_cap", "halo", "heart_headband", "headphones", "neon_cat_ears", "hny", "party_hat", "rabbit_ears", "top_hat", "witch_hat"]
        secondary_accessories = ["black_bow_tie", "christmas_tree", "cloud", "coffee", "pumpkin", "hearts", "m_slice_cake", "moustache", "neon_blush", "monocle", "p_slice_cake", "patch", "speech_bubble", "sunglasses"]
        background_accessories = ["angel_wings", "balloon_decorations", "cat_tail", "fox_tail", "snowflakes"]

        for acc in primary_accessories:
            path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_0, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)

        for acc in secondary_accessories:
            path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_1, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)

        # Also check background accessories in their folder
        for acc in background_accessories:
            path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_2, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)


        # --- 4. Backgrounds (Manual List) ---
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
            # Tables & Chairs
            "mod_assets/monika/t/chair-extraplus_cafe.png",
            "mod_assets/monika/t/table-extraplus_cafe.png",
            "mod_assets/monika/t/table-extraplus_cafe-s.png",
            "mod_assets/monika/t/chair-extraplus_restaurant.png",
            "mod_assets/monika/t/table-extraplus_restaurant.png",
            "mod_assets/monika/t/table-extraplus_restaurant-s.png"
        ]
        for asset in background_assets:
            check_file(asset, found_assets, missing_assets)

        # --- 5. Blackjack Cards ---
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(1, 14):
                path = store.ep_folders._join_path(store.ep_folders.EP_MG_BLACKJACK, suit, "{}.png".format(value))
                check_file(path, found_assets, missing_assets)

        # --- 6. Date Accessories ---
        # This list is defined in Extra_Plus_Main.rpy
        for acs_tuple in store.extraplus_accessories:
            acs_name = acs_tuple[1]
            path = "mod_assets/monika/a/{}/0.png".format(acs_name)
            check_file(path, found_assets, missing_assets)

        # --- 6. Write Log File ---
        log_path = store.ep_folders._normalize_path(os.path.join(renpy.config.basedir, "characters", "extra_plus_asset_log.txt"))
        try:
            with open(log_path, 'w') as f:
                f.write("Extra+ Asset Linter Report - {}\n".format(datetime.datetime.now().strftime("%b %d, %Y %I:%M:%S %p")))
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

            renpy.notify(_("Asset check complete. See extra_plus_asset_log.txt in /characters."))

        except Exception as e:
            renpy.notify(_("Failed to write asset log: {}").format(e))

    def cleanup_old_files():
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
            renpy.notify(_("Some errors occurred during cleanup. Please check the logs."))


# Store: ep_tools
init 5 python in ep_tools:
    import store
    import datetime

    # Helper function to format dates (American Format: Month Day, Year)
    def exp_fmt_date(dt):
        if dt is None:
            return _("???")
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
            return self.date < other.date

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
            ("direct_date", getattr(store.persistent, '_mas_first_kiss', None), _("First Kiss"), _("The moment our lips (almost) touched for the first time."), "7"), # Already correct from previous request

            # Type 'event': Uses the last_seen date from a MAS event
            ("event", "monika_promisering", _("Eternal Promise"), _("You gave me the promise ring. Our bond is forever."), "7"),
            ("event", "mas_unlock_piano", _("Music for You"), _("When I added the piano so I could play for you."), "&"),
            ("event", "mas_unlock_chess", _("Intellectual Challenge"), _("The first time we played Chess together."), "4"),
            ("event", "mas_blazerless_intro", _("Getting Comfortable"), _("The first time you felt comfortable enough to take off your blazer."), "7"),
            ("event", "mas_unlock_hangman", _("Word Games"), _("We started playing Hangman together."), "4"),
            ("event", "mas_birthdate", _("My Birthday"), _("The day I told you when I was born."), "G"),

            # Type 'special': Requires custom logic
            ("special", "nickname", _("A Special Name"), _("The day you started calling me '{}'."), "w"),
            ("special", "first_trip", _("First Adventure"), _("The first time you took me out of this room with you."), "7"),
            ("special", "pong", _("Classic Gaming"), _("We played Pong for the first time."), "4"),
            ("special", "contributor", _("Helping Hand"), _("The day I told you I was contributing to the code."), "g")
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

                    elif data == "contributor" and getattr(store.persistent, '_mas_pm_has_contributed_to_mas', False):
                        ev_contrib = store.mas_getEV("monika_contribute")
                        date_contrib = ev_contrib.last_seen if (ev_contrib and ev_contrib.last_seen) else datetime.date.today()
                        entries.append(EPTimelineEntry(date_contrib, title, description, icon))
        
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

    def getCurrentAffection():
        # Safely gets affection to avoid cache issues.
        try:
            raw_data = store.mas_affection.__get_data()
            if raw_data and len(raw_data) > 0:
                return raw_data[0]
            else:
                return store._mas_getAffection()
        except Exception:
            return store._mas_getAffection()

    def notify_affection():
        # Notifies the player of their current affection level.
        import time
        current_time = time.time()
        if current_time - store.ep_tools.last_affection_notify_time >= 10:
            store.ep_tools.last_affection_notify_time = current_time
            current_affection = getCurrentAffection()
            store.ep_chibis.chibika_notify("{1} {0} {1}".format(
                int(current_affection),
                getLevelIcon(current_affection)
            ))

    def getLevelIcon(affection_val):
        # Returns a font icon based on affection value.
        if affection_val >= 1000: icon = '"'
        elif affection_val >= 400: icon = ';'
        elif affection_val >= 100: icon = '2'
        elif affection_val >= 30: icon = '#'
        elif affection_val <= -30: icon = '%'
        elif affection_val <= -100: icon = '8'
        else: icon = '/'

        return "{size=+5}{color=#FFFFFF}{font=" + store.ep_tools.affection_icons + "}" + icon + "{/font}{/color}{/size}"

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

    def show_boop_feedback(message, color="#ff69b4"):
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

            if total_days < 1: # This is a full sentence, better to translate it as a whole.
                return _("less than a day, but every second has been incredible!")

            years = total_days // 365
            remaining_days = total_days % 365
            months = remaining_days // 30
            days = remaining_days % 30

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
                renpy.notify(_("Your clipboard is empty.")) # Already correct
                return "cancel"
        except Exception:
            renpy.notify(_("Could not access clipboard.")) # Already correct
            return "cancel"

    # --- Dating and Label Helpers ---
    def check_seen_background(first_time, alternate, stop_date):
        """Handle affection and label jump based on background seen status."""
        if store.mas_affection._get_aff() < 400:
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
            # Restaurar silla y mesa
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

    def check_seen_label(first_time, alternate):
        """Jump to alternate if first_time has been seen."""
        if renpy.seen_label(first_time):
            renpy.jump(alternate)


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
        except: pass

    def reset_chibi():
        remove_chibi()
        init_chibi()

    def draw_background_accessories(st, at):
        return LiveComposite(
            (188, 188),
            (0, 0), store.MASFilterSwitch(store.ep_chibis.accessory_path_2.format(store.persistent.chibi_accessory_3_))
        ), 5

    def draw_foreground_accessories(st, at):
        return LiveComposite(
            (188, 188),
            (0, 0), store.MASFilterSwitch(store.ep_chibis.accessory_path_0.format(store.persistent.chibi_accessory_1_)),
            (0, 0), store.MASFilterSwitch(store.ep_chibis.accessory_path_1.format(store.persistent.chibi_accessory_2_))
        ), 5

    def migrate_chibi_costume_data():
        if isinstance(store.persistent.chibika_current_costume, list):
            store.persistent.chibika_current_costume = store.ep_chibis.blanket_monika
        elif isinstance(store.persistent.chibika_current_costume, tuple) and isinstance(store.persistent.chibika_current_costume[0], basestring):
            if not renpy.loadable(store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "darling", "idle.png")):
                store.persistent.chibika_current_costume = ["sticker_up", "sticker_sleep", "sticker_baka"]

    class DokiAccessory():
        def __init__(self, name, acc, slot):
            self.name = name
            self.acc = acc
            self.slot = slot

        def __call__(self):
            if self.slot == "primary":
                store.persistent.chibi_accessory_1_ = self.acc
            elif self.slot == "secondary":
                store.persistent.chibi_accessory_2_ = self.acc
            else:
                store.persistent.chibi_accessory_3_ = self.acc

    class SelectDOKI():
        def __init__(self, name, costume):
            self.name = name
            self.costume = costume

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
        current_char = store.persistent.chibika_current_costume[0]

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
            "primary": store.ep_chibis.primary_accessories,
            "secondary": store.ep_chibis.secondary_accessories,
            "background": store.ep_chibis.background_accessories
        }
        return category_map.get(category, [])

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

    def chibika_notify(txt, doki="darling"):
        """Shows a notification from Chibika."""
        renpy.show_screen("chibika_notify", message=txt, icon=doki)

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

    def getCurrentColor(base_color):
        # If it's night, darken the color.
        if store.mas_isNightNow():
            return base_color.shade(0.6)
        
        # If it's day, return the original vibrant color
        return base_color

    class Magnet:
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

    class MagnetManager:
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
            
            # If Monika hasn't posted today, there's a chance she will.
            if store.persistent.EP_fridge_last_monika_post != today_str:
                # We give a 1 in 3 chance so she doesn't do it every day
                if renpy.random.randint(1, 3) == 1:
                    self.monika_adds_magnets()
                    store.persistent.EP_fridge_last_monika_post = today_str
                
            # We load the magnets (the player's and Monika's if she just placed them)
            self.load() 


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
            for _ in range(50):
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
                
            store.persistent.EP_fridge_magnets_data = data

        def load(self):
            """Reconstructs the magnets from the saved data."""
            data = store.persistent.EP_fridge_magnets_data
            if not data:
                return # No saved data, we start empty
            
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
        except: pass
    
    def safe_overlay_remove(screen):
        try:
            if screen in renpy.config.overlay_screens:
                renpy.config.overlay_screens.remove(screen)
                renpy.hide_screen(screen)
        except: pass


init -10 python in ep_sg:
    import store
    
    def randomize_cup_skin():
        if store.persistent._mas_pm_cares_about_dokis: return renpy.random.choice(["monika.png", "yuri.png", "natsuki.png", "sayori.png"])
        renpy.random.choice(["cup.png", "monika.png"])