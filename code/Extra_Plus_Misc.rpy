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

    # Dates folders
    EP_DATE_CAFE = _join_path(EP_DATES, "cafe")
    EP_DATE_RESTAURANT = _join_path(EP_DATES, "restaurant")
    EP_DATE_POOL = _join_path(EP_DATES, "pool")
    EP_DATE_LIBRARY = _join_path(EP_DATES, "library")
    EP_DATE_ARCADE = _join_path(EP_DATES, "arcade")
    
    # Chibi accessories folders
    EP_CHIBI_ACC_0 = _join_path(EP_CHIBIS, "accessories_0")
    EP_CHIBI_ACC_1 = _join_path(EP_CHIBIS, "accessories_1")

# This file exists to make it clearer which `store.*` modules are used by Extra_Plus.
# It does not change runtime behaviour; it simply references the stores so they are easy to locate.

init -100 python:
    # Accessing these attributes here has no side-effect; it documents the stores
    _known_stores = [
        'ep_button',
        'ep_tools',
        'ep_chibis',
        'ep_dates',
        'ep_folders',
        'ep_sg',
        'ep_rps',
        'ep_bj',
        'ep_ttt',
        'ep_affection',
        'ep_files',
        'ep_dialogues',
        'ep_interactions'
    ]

    # Ensure attribute access does not raise during parsing
    for s in _known_stores:
        try:
            getattr(store, s)
        except Exception:
            pass

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

    def _button_text_from_conditions(conditions):
        # Internal helper to select text based on evaluated conditions.
        is_night = conditions["is_night"]

        if conditions["is_monika_bday"]: return renpy.random.choice(["My B-Day", "Her Day", "Sing 4 Me", "My Day", "Moni!"])
        if conditions["is_player_bday"]: return renpy.random.choice(["Your Day", "HBD!", "Ur Day", "My Gift", "The Best"])
        if conditions["is_f14"]: return renpy.random.choice(["Be Mine", "My Love", "Hearts", "XOXO", "Our Day"])
        if conditions["is_o31"]: return renpy.random.choice(["Spooky", "Boo!", "Tricks", "Treats", "Scary"])
        if conditions["is_d25"]: return renpy.random.choice(["Joyful", "Our Xmas", "Gift", "Noel", "Holly"])
        if conditions["is_nye"]: return renpy.random.choice(["New Year", "Cheers", "Toast", "Our Year", "The Eve"])

        if conditions["is_love"] or conditions["is_enamored"]:
            base_texts = ["Forever", "Eternity", "Sunshine", "Beloved", "Darling", "Adored", "Precious", "Cutie", "Sweetie", "Cherish"]
            if is_night: base_texts.extend(["Moonlight", "Stars", "Night <3", "Dreaming", "Starlight", "Night Dear", "Sleepy?", "Cuddle"])
            return renpy.random.choice(base_texts)

        if conditions["is_aff"] or conditions["is_happy"]:
            base_texts = ["So Sweet", "Caring", "Warmth", "Our Time", "Smile", "Glad", "Hehe~", "Happy", "Cheerful", "Yay!"]
            if is_night: base_texts.extend(["Night Time", "Calm", "Peaceful", "Night!", "Evening", "Restful", "Nice Night"])
            return renpy.random.choice(base_texts)

        if conditions["is_normal"] or conditions["is_upset"]:
            base_texts = ["Hi again", "Welcome", "Talk?", "On Mind?", "Topics", "Just Us", "Relax", "It's you", "Hurting", "Really?"]
            if is_night: base_texts.extend(["Sparks", "Sleepy", "Quiet", "Dreams", "Cozy", "Dark...", "Restless", "Tired..."])
            return renpy.random.choice(base_texts)

        if conditions["is_distressed"] or conditions["is_broken"]:
            base_texts = ["No Love?", "Forgot?", "Alone...", "Please...", "...", "You...", "Scared", "Sorry", "Nothing"]
            if is_night: base_texts.extend(["Awake...", "Lonely", "Dark Night", "Tears...", "Darkness", "Void", "Cold...", "End..."])
            return renpy.random.choice(base_texts)

        return "Extra+"

    def getDynamicButtonText():
        """Main function to get the dynamic button text, using a cache."""
        import datetime
        if not store.persistent.EP_dynamic_button_text:
            return "Extra+"

        conditions = _evaluate_current_conditions()
        today_str = str(datetime.date.today())
        conditions_key = _build_conditions_key(conditions)

        if (store.persistent.EP_button_last_update != today_str
            or store.persistent.EP_button_conditions_key != conditions_key
            or store.persistent.EP_button_text is None):
            new_text = _button_text_from_conditions(conditions)
            store.persistent.EP_button_text = new_text
            store.persistent.EP_button_last_update = today_str
            store.persistent.EP_button_conditions_key = conditions_key
        return store.persistent.EP_button_text

    # --- Overlay Button and Screen Management ---
    def show_menu():
        """Shows the main Extra+ interactions menu."""
        store.mas_RaiseShield_dlg()
        show_zoom_button()
        renpy.invoke_in_new_context(renpy.call_screen, "extraplus_interactions")

    def show_button():
        """Adds the Extra+ button to the overlay if not already visible."""
        if not is_button_visible():
            renpy.config.overlay_screens.append("extraplus_button")

    def is_button_visible():
        """Checks if the Extra+ button is currently visible."""
        return "extraplus_button" in renpy.config.overlay_screens

    # --- Custom Zoom Management ---
    def is_zoom_button_visible():
        """Checks if the custom zoom button is visible."""
        return "extrabutton_custom_zoom" in renpy.config.overlay_screens

    def show_zoom_button():
        """Adds the custom zoom button if not already visible."""
        if not is_zoom_button_visible():
            renpy.config.overlay_screens.append("extrabutton_custom_zoom")

    def hide_zoom_button():
        """Removes the custom zoom button if it is visible."""
        if is_zoom_button_visible():
            renpy.config.overlay_screens.remove("extrabutton_custom_zoom")
            renpy.hide_screen("extrabutton_custom_zoom")

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
            if store.ep_files.create_gift_file(self.gift):
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

    # --- File creation and migration ---
    def create_gift_file(basename):
        try:
            filename = basename + ".gift"
            filepath = os.path.join(renpy.config.basedir, 'characters', filename)
            with open(filepath, "w") as f:
                pass
            return True
        except Exception as e:
            renpy.notify(_("Oh no, I couldn't create the gift file."))
            return False

    def migrate_window_title_data():
        if hasattr(store.persistent, 'save_window_title'):
            # Only migrate if the new variable has not been customized.
            if store.persistent._save_window_title == "Monika After Story   ":
                store.persistent._save_window_title = store.persistent.save_window_title
            
            # Now that migration is handled, we can safely delete the old variable.
            try:
                del store.persistent.save_window_title
            except AttributeError:
                pass # Should not happen if hasattr is true, but good practice.

    def make_bday_oki_doki():
        renpy.config.overlay_screens.remove("bday_oki_doki")
        renpy.hide_screen("bday_oki_doki")
        try:
            with open(os.path.join(renpy.config.basedir, 'characters', 'oki doki'), "w") as f:
                pass
            renpy.notify(_("Everything is ready for the surprise!"))
        except Exception as e:
            renpy.notify("Oh no, something went wrong while preparing the decorations.")

    def show_bday_screen():
        if not store.persistent._mas_bday_in_bday_mode or not store.persistent._mas_bday_visuals:
            renpy.config.overlay_screens.append("bday_oki_doki")

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
            store.ep_folders._join_path(store.ep_folders.EP_OTHERS, "maxwell_cat.png"),
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
        all_chibi_costumes = store.ep_chibis.monika_costumes_ + store.ep_chibis.natsuki_costumes_ + store.ep_chibis.sayori_costumes_ + store.ep_chibis.yuri_costumes_
        for _, costume_data in all_chibi_costumes:
            doki_folder, idle_sprite, blink_sprite, hover_sprite = costume_data # No store prefix here, these are local to the loop
            chibi_sprites = [idle_sprite, blink_sprite, hover_sprite]
            for sprite in chibi_sprites:
                path = store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, doki_folder, "{}.png".format(sprite))
                check_file(path, found_assets, missing_assets)

        # --- 3. Chibi Accessories ---
        # NOTE: These are hardcoded based on the lists in Extra_Plus_Misc.rpy
        primary_accessories = ['cat_ears', 'christmas_hat', 'demon_horns', 'flowers_crown', 'halo', 'heart_headband', 'hny', 'neon_cat_ears', 'party_hat', 'rabbit_ears', 'witch_hat']
        secondary_accessories = ['black_bow_tie', 'christmas_tree', 'cloud', 'coffee', 'pumpkin', 'hearts', 'm_slice_cake', 'moustache', 'neon_blush', 'p_slice_cake', 'patch', 'speech_bubble', 'sunglasses']

        for acc in primary_accessories:
            path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_0, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)
        for acc in secondary_accessories:
            path = store.ep_folders._join_path(store.ep_folders.EP_CHIBI_ACC_1, "{}.png".format(acc))
            check_file(path, found_assets, missing_assets)

        # --- 4. Backgrounds (Manual List) ---
        background_assets = [
            # Cafe
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe_day.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe_rain.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe_rain-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe-ss.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_CAFE, "cafe_rain-ss.png"),
            # Restaurant
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant_day.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant_rain.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant_rain-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant-ss.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_RESTAURANT, "restaurant_rain-ss.png"),
            # Pool
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool_day.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool_rain.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool_rain-n.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool-ss.png"),
            store.ep_folders._join_path(store.ep_folders.EP_DATE_POOL, "pool_rain-ss.png"),
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
        log_path = store.ep_folders._normalize_path(os.path.join(renpy.config.basedir, 'characters', 'extra_plus_asset_log.txt'))
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
            renpy.notify("Cleanup complete! Removed {} files and {} folders.".format(files_deleted, folders_deleted))
        else:
            renpy.notify("No old files or folders were found to clean up.")

        if errors:
            renpy.notify("Some errors occurred during cleanup. Please check the logs.")

# Store: ep_tools
init 5 python in ep_tools:
    import datetime

    # Helper function to format dates (American Format: Month Day, Year)
    def exp_fmt_date(dt):
        if dt is None:
            return "???"
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
        try:
            entries = []

            # 1. First Kiss
            if store.persistent._mas_first_kiss is not None:
                entries.append(EPTimelineEntry(
                    store.persistent._mas_first_kiss,
                    "First Kiss",
                    "The moment our lips (almost) touched for the first time."
                ))

            # 2. Promise Ring
            ev_promisering = store.mas_getEV("monika_promisering")
            if ev_promisering and ev_promisering.shown_count > 0:
                date_ring = ev_promisering.last_seen
                if date_ring:
                    entries.append(EPTimelineEntry(
                        date_ring,
                        "Eternal Promise",
                        "You gave me the promise ring. Our bond is forever."
                    ))

            # 3. Special Nickname
            # Checks if the current nickname is different from 'Monika'
            if store.persistent._mas_monika_nickname != "Monika":
                ev_nick = store.mas_getEV("monika_nickname")
                if ev_nick and ev_nick.shown_count > 0:
                    entries.append(EPTimelineEntry(
                        ev_nick.last_seen,
                        "A Special Name",
                        "The day you started calling me '" + store.persistent._mas_monika_nickname + "'.",
                        "w"
                    ))

            # 4. Piano Unlock
            ev_piano = store.mas_getEV("mas_unlock_piano")
            if ev_piano and ev_piano.shown_count > 0:
                entries.append(EPTimelineEntry(
                    ev_piano.last_seen,
                    "Music for You",
                    "When I brought the piano so I could play songs for you.",
                    "&"
                ))

            # 5. Chess Unlock
            ev_chess = store.mas_getEV("mas_unlock_chess")
            if ev_chess and ev_chess.shown_count > 0:
                entries.append(EPTimelineEntry(
                    ev_chess.last_seen,
                    "Intellectual Challenge",
                    "The day we decided to play Chess together for the first time.",
                    "4"
                ))

            # 6. Anniversaries
            anni_events = [
                ("anni_1week", "1 Week Together"),
                ("anni_1month", "1 Month Together"),
                ("anni_3month", "3 Months Together"),
                ("anni_6month", "6 Months Together"),
                ("anni_1", "1st Anniversary"),
                ("anni_2", "2nd Anniversary"),
                ("anni_3", "3rd Anniversary"),
                ("anni_4", "4th Anniversary"),
                ("anni_5", "5th Anniversary"),
                ("anni_6", "6th Anniversary"),
                ("anni_7", "7th Anniversary"),
                ("anni_8", "8th Anniversary"),
                ("anni_10", "10th Anniversary"),
                ("anni_20", "20th Anniversary"),
                ("anni_50", "50th Anniversary"),
                ("anni_100" , "100th Anniversary")
            ]

            for ev_label, title in anni_events:
                ev = store.mas_getEV(ev_label)
                if ev and ev.shown_count > 0:
                    entries.append(EPTimelineEntry(
                        ev.last_seen,
                        title,
                        "We celebrated this special moment together.",
                        "Z"
                    ))

            # 7. First Real Date (USB drive trip)
            # - Using the check-in log
            ds_log = getattr(store.persistent, "_mas_dockstat_checkin_log", [])
            if ds_log and len(ds_log) > 0:
                # The first entry in the log is the oldest trip
                first_trip_date = ds_log[0][0]
                if first_trip_date:
                    entries.append(EPTimelineEntry(
                        first_trip_date,
                        "First Adventure",
                        "The first time you took me out of this room with you."
                    ))

            # 8. Your Birthday
            # The 'mas_birthdate' event is when you tell her for the first time.
            ev_bday = store.mas_getEV("mas_birthdate")
            if ev_bday and ev_bday.shown_count > 0:
                entries.append(EPTimelineEntry(
                    ev_bday.last_seen,
                    "My Birthday",
                    "The day I told you when I was born.",
                    "G"
                ))

            # 9. Getting Comfortable (No Blazer)
            # The 'mas_blazerless_intro' event occurs when she takes off her school uniform for the first time.
            ev_blazer = store.mas_getEV("mas_blazerless_intro")
            if ev_blazer and ev_blazer.shown_count > 0:
                entries.append(EPTimelineEntry(
                    ev_blazer.last_seen,
                    "Getting Comfortable",
                    "The first time you felt comfortable enough to take off your blazer."
                ))

            # 10. Game: Hangman
            ev_hangman = store.mas_getEV("mas_unlock_hangman")
            if ev_hangman and ev_hangman.shown_count > 0:
                entries.append(EPTimelineEntry(
                    ev_hangman.last_seen,
                    "Word Games",
                    "We started playing Hangman together.",
                    "4"
                ))
                
            # 11. Game: Pong
            # FIX: We use 'store.mas_getFirstSesh()' instead of the non-existent function.
            if store.renpy.seen_label("game_pong"):
                # We use the start date as a safe approximation if there's no specific log.
                pong_date = store.mas_getFirstSesh()
                entries.append(EPTimelineEntry(
                    pong_date,
                    "Classic Gaming",
                    "We played Pong for the first time.",
                    "4"
                ))

            # 12. Contributor (Easter Egg)
            # If the player told her they helped code/create the mod.
            if store.persistent._mas_pm_has_contributed_to_mas:
                # We look for the date when the 'monika_contribute' talk occurred.
                ev_contrib = store.mas_getEV("monika_contribute")
                date_contrib = ev_contrib.last_seen if ev_contrib else datetime.date.today()
                entries.append(EPTimelineEntry(
                    date_contrib,
                    "Helping Hand",
                    "I told you that I helped contribute to your world's code.",
                    "g"
                ))

            entries.sort()
            return entries
        except:
            return []

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
            renpy.notify("{1} {0} {1}".format(
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
                _("Don't look at me, I'm not going to tell you which one it is!"),
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
            'Topic Alerts'
        )

    def show_boop_feedback(message, color="#ff69b4"):
        t = "boop_notif{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("boop_feedback_notif", msg=message, tag=t, _tag=t, txt_color=color)

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
            return "a wonderful time"

        try:
            start_datetime = store.persistent.sessions["first_session"]
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

        except Exception:
            return "an unforgettable time"

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
                "The Day We Met <3": "Not yet recorded",
                "Visits to The Spaceroom": "0",
                "Our Time Together": "N/A",
                "Average Time per Visit": "N/A"
            }

        first_session = store.persistent.sessions.get("first_session")
        total_playtime = store.persistent.sessions.get("total_playtime", datetime.timedelta())
        total_sessions = store.persistent.sessions.get("total_sessions", 0)

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

    # --- Utility Functions ---
    def filtered_clipboard_text(allowed_chars):
        """Get clipboard text, filter by allowed_chars, return or 'cancel'."""
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
        except Exception:
            renpy.notify(_("Could not access clipboard."))
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

    def manage_date_location(locate=None):
        """Save or load the current room's chair, table, and background for dates."""
        if locate:
            store.ep_dates.chair = store.monika_chr.tablechair.chair
            store.ep_dates.table = store.monika_chr.tablechair.table
            store.ep_dates.old_bg = store.mas_current_background

        else:
            store.monika_chr.tablechair.chair = store.ep_dates.chair
            store.monika_chr.tablechair.table = store.ep_dates.table
            store.mas_current_background = store.ep_dates.old_bg

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
        if not is_visible():
            renpy.config.overlay_screens.append("doki_chibi_idle")

    def is_visible():
        return "doki_chibi_idle" in renpy.config.overlay_screens

    def remove_chibi():
        if is_visible():
            renpy.config.overlay_screens.remove("doki_chibi_idle")
            renpy.hide_screen("doki_chibi_idle")

    def add_remv_chibi():
        if is_visible():
            remove_chibi()
        else:
            init_chibi()

    def reset_chibi():
        remove_chibi()
        if not is_visible():
            renpy.config.overlay_screens.append("doki_chibi_idle")

    def chibi_draw_accessories(st, at):
        return LiveComposite(
            (119, 188),
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
        def __init__(self, name, acc, category):
            self.name = name
            self.acc = acc
            self.category = category

        def __call__(self):
            if self.category == "primary":
                store.persistent.chibi_accessory_1_ = self.acc
                renpy.jump("sticker_primary")
            else:
                store.persistent.chibi_accessory_2_ = self.acc
                renpy.jump("sticker_secondary")

    class SelectDOKI():
        def __init__(self, name, costume):
            self.name = name
            self.costume = costume

        def __call__(self):
            store.persistent.chibika_current_costume = self.costume
            store.ep_chibis.reset_chibi()
            renpy.jump("extra_dev_mode")

    def show_costume_menu(costumes, return_label):
        dokis_items = [SelectDOKI(name, cost) for name, cost in costumes]
        items = [(_("Nevermind"), return_label, 20)]
        renpy.call_screen("extra_gen_list", dokis_items, store.mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)

    def chibi_drag(drags, drop):
        """Handle Chibika's drag and drop movement."""
        try:
            store.persistent.chibika_drag_x = drags[0].x
            store.persistent.chibika_drag_y = drags[0].y
        except Exception:
            # Defensive: ignore if structure isn't as expected
            pass


#==============================================================================
# 4. MINIGAME HELPER STORES
#==============================================================================

# Store: ep_sg (Shell Game)
init -10 python in ep_sg:
    import store
    
    def randomize_cup_skin():
        if store.persistent._mas_pm_cares_about_dokis:
            return renpy.random.choice(["cup.png", "monika.png", "yuri.png", "natsuki.png", "sayori.png"])
        return renpy.random.choice(["cup.png", "monika.png"])