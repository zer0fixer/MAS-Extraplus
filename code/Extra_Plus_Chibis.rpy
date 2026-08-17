#===========================================================================================
# EXTRA PLUS - CHIBI SYSTEM
# Class-based chibi management system for flexible character handling
# Compatible with Ren'Py 6.99 / Python 2
#===========================================================================================

# =============================================================================
# CHIBI CHARACTER CLASS
# Represents an individual chibi instance with its own state
# =============================================================================
init -15 python in ep_chibis:
    import store
    
    class ChibiCharacter(object):
        """
        Represents an individual chibi character with its own state.
        This allows creating multiple instances of the same or different characters.
        
        Attributes:
            id (str): Unique identifier for this chibi instance
            doki (str): Character type ("darling", "cupcake", "cinnamon", "teacup")
            costume (str): Current costume name ("blanket", "casual", etc.)
            x (float/int): X position on screen
            y (int): Y position on screen
            draggable (bool): Whether the chibi can be dragged
            visible (bool): Whether the chibi is currently visible
            click_count (int): Counter for click interactions
            is_angry (bool): Whether the chibi is in "angry" state (ran away)
            is_jumping (bool): Whether the chibi is currently jumping
            accessory_1 (str): Primary accessory slot (headwear)
            accessory_2 (str): Secondary accessory slot (held items)
            accessory_3 (str): Background accessory slot (wings, tails)
        """
        
        # Use __slots__ for memory efficiency (Python 2 compatible)
        __slots__ = [
            'id', 'doki', 'costume', 'x', 'y', 
            'draggable', 'visible', 'click_count', 
            'is_angry', 'is_jumping',
            'accessory_1', 'accessory_2', 'accessory_3',
            'blanket_color'  # Color tint for blanket costume
        ]
        
        # Available blanket colors for the tint overlay system
        # Format: { "color_name": ((R, G, B), display_name) }
        # The RGB values are applied to the white blanket overlay using im.Tint
        # Base sprite should have the blanket in GRAYSCALE
        # Overlay sprite (_blanket.png) should be WHITE where the blanket is
        BLANKET_COLORS = {
            "original": ((76, 153, 76), _("Original (Green)")),     # Forest green
            "red": ((220, 60, 60), _("Red")),                       # Warm red
            "blue": ((60, 100, 200), _("Blue")),                    # Royal blue
            "yellow": ((230, 200, 50), _("Yellow")),                # Golden yellow
            "magenta": ((200, 80, 180), _("Magenta")),              # Pink magenta
            "cyan": ((60, 200, 200), _("Cyan")),                    # Aqua cyan
            "purple": ((130, 80, 180), _("Purple")),                # Deep purple
            "orange": ((230, 130, 50), _("Orange")),                # Bright orange
            "pink": ((255, 150, 180), _("Pink")),                   # Soft pink
            "white": ((240, 240, 245), _("White")),                 # Off-white
        }
        
        # Registry of all available costumes per doki character
        # Format: { "doki_name": { "costume_name": (idle_sprite, blink_sprite, hover_sprite) } }
        COSTUMES = {
            "darling": {
                "blanket": ("idle", "blink", "hover"),
                "casual": ("casual_idle", "casual_blink", "casual_hover"),
                "android": ("android_idle", "android_blink", "android_hover"),
                "bikini": ("bikini_idle", "bikini_blink", "bikini_hover"),
            },
            "cupcake": {
                "blanket": ("idle", "blink", "hover"),
                "casual": ("casual_idle", "casual_blink", "casual_hover"),
            },
            "cinnamon": {
                "blanket": ("idle", "blink", "hover"),
                "casual": ("casual_idle", "casual_blink", "casual_hover"),
            },
            "teacup": {
                "blanket": ("idle", "blink", "hover"),
                "casual": ("casual_idle", "casual_blink", "casual_hover"),
            },
        }
        
        # Click response thresholds and messages per character
        CLICK_RESPONSES = {
            10: {
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
        
        def __init__(self, chibi_id, doki="darling", costume="blanket", x=0.025, y=385):
            """
            Initialize a new ChibiCharacter instance.
            
            IN:
                chibi_id (str): Unique identifier for this chibi
                doki (str): Character type (default: "darling")
                costume (str): Initial costume (default: "blanket")
                x (float/int): Initial X position (default: 0.025)
                y (int): Initial Y position (default: 385)
            """
            self.id = chibi_id
            self.doki = doki if doki in self.COSTUMES else "darling"
            self.costume = costume if costume in self.COSTUMES.get(self.doki, {}) else "blanket"
            self.x = x
            self.y = y
            self.draggable = False
            self.visible = True
            self.click_count = 0
            self.is_angry = False
            self.is_jumping = False
            self.accessory_1 = "0nothing"
            self.accessory_2 = "0nothing"
            self.accessory_3 = "0nothing"
            self.blanket_color = "original"  # Default: no color change
        
        @property
        def sprite_folder(self):
            """Returns the folder name for this doki's sprites."""
            return self.doki
        
        @property
        def sprites(self):
            """Returns tuple (idle, blink, hover) for the current costume."""
            return self.COSTUMES.get(self.doki, {}).get(self.costume, ("idle", "blink", "hover"))
        
        @property
        def idle_sprite(self):
            """Returns the idle sprite name."""
            return self.sprites[0]
        
        @property
        def blink_sprite(self):
            """Returns the blink sprite name."""
            return self.sprites[1]
        
        @property
        def hover_sprite(self):
            """Returns the hover sprite name."""
            return self.sprites[2]
        
        def get_sprite_path(self, state="idle"):
            """
            Returns the full path to the requested sprite.
            
            IN:
                state (str): Sprite state - "idle", "blink", or "hover"
                
            OUT:
                str: Full path to the sprite file
            """
            sprite_map = {"idle": 0, "blink": 1, "hover": 2}
            idx = sprite_map.get(state, 0)
            sprite_name = self.sprites[idx]
            return store.ep_folders._join_path(
                store.ep_folders.EP_CHIBIS, 
                self.doki, 
                "{}.png".format(sprite_name)
            )
        
        def get_accessory_path(self, slot):
            """
            Returns the path for an accessory in the specified slot.
            
            IN:
                slot (int): Accessory slot (1, 2, or 3)
                
            OUT:
                str: Full path to the accessory sprite
            """
            accessory_value = getattr(self, "accessory_{}".format(slot), "0nothing")
            path_map = {
                1: store.ep_chibis.accessory_path_0,
                2: store.ep_chibis.accessory_path_1,
                3: store.ep_chibis.accessory_path_2,
            }
            path_template = path_map.get(slot, store.ep_chibis.accessory_path_0)
            return path_template.format(accessory_value)
        
        def set_costume(self, costume_name):
            """
            Changes the costume if valid for this doki.
            
            IN:
                costume_name (str): Name of the costume to set
                
            OUT:
                bool: True if costume was changed, False otherwise
            """
            if costume_name in self.COSTUMES.get(self.doki, {}):
                self.costume = costume_name
                return True
            return False
        
        def set_doki(self, doki_name, costume="blanket"):
            """
            Changes the doki type and optionally the costume.
            
            IN:
                doki_name (str): Name of the doki to change to
                costume (str): Costume to use (default: "blanket")
                
            OUT:
                bool: True if doki was changed, False otherwise
            """
            if doki_name in self.COSTUMES:
                self.doki = doki_name
                if costume in self.COSTUMES[doki_name]:
                    self.costume = costume
                else:
                    self.costume = "blanket"
                return True
            return False
        
        def set_accessory(self, slot, accessory_name):
            """
            Sets an accessory in the specified slot.
            
            IN:
                slot (int or str): Slot number (1, 2, 3) or name ("primary", "secondary", "background")
                accessory_name (str): Name of the accessory file (without extension)
            """
            slot_map = {"primary": 1, "secondary": 2, "background": 3}
            if isinstance(slot, str):
                slot = slot_map.get(slot, 1)
            
            if slot in (1, 2, 3):
                setattr(self, "accessory_{}".format(slot), accessory_name)
        
        def clear_accessories(self):
            """Removes all accessories from this chibi."""
            self.accessory_1 = "0nothing"
            self.accessory_2 = "0nothing"
            self.accessory_3 = "0nothing"
        
        def handle_click(self):
            """
            Handles click interaction logic with responses.
            
            OUT:
                str or None: Response message if threshold reached, None otherwise
            """
            self.click_count += 1
            
            if self.click_count in self.CLICK_RESPONSES:
                responses = self.CLICK_RESPONSES[self.click_count]
                message = responses.get(self.doki, responses["default"])
                
                # Trigger notification
                chibika_notify(renpy.substitute(message), self.doki)
                
                # Check if chibi should run away
                if self.click_count >= 50:
                    self.is_angry = True
                    self.visible = False
                    self.click_count = 0
                    # Show poof effect
                    renpy.show_screen("chibi_visual_effect", x=self.x, y=self.y)
                    return message
                
                return message
            
            return None
        
        def reset_anger(self):
            """Resets the angry state and makes the chibi visible again."""
            self.is_angry = False
            self.visible = True
            self.click_count = 0
        
        def move_to(self, x, y):
            """
            Moves the chibi to the specified position.
            
            IN:
                x (float/int): New X position
                y (int): New Y position
            """
            self.x = x
            self.y = y
        
        def clone(self, new_id=None):
            """
            Creates a clone of this chibi with a new ID.
            
            IN:
                new_id (str or None): ID for the clone. If None, generates a random ID.
                
            OUT:
                ChibiCharacter: A new chibi instance with copied properties
            """
            if new_id is None:
                new_id = "{}_clone_{}".format(self.id, renpy.random.randint(1000, 9999))
            
            new_chibi = ChibiCharacter(new_id, self.doki, self.costume, self.x + 0.05, self.y)
            new_chibi.draggable = self.draggable
            new_chibi.accessory_1 = self.accessory_1
            new_chibi.accessory_2 = self.accessory_2
            new_chibi.accessory_3 = self.accessory_3
            new_chibi.blanket_color = self.blanket_color
            return new_chibi
        
        def set_blanket_color(self, color_name):
            """
            Sets the blanket color for this chibi.
            
            IN:
                color_name (str): Name of the color from BLANKET_COLORS
                
            OUT:
                bool: True if color was changed, False if invalid
            """
            if color_name in self.BLANKET_COLORS:
                self.blanket_color = color_name
                return True
            return False
        
        def get_blanket_rgb(self):
            """
            Returns the RGB color tuple for the current blanket color.
            
            OUT:
                tuple: (R, G, B) values 0-255
            """
            color_data = self.BLANKET_COLORS.get(self.blanket_color, ((76, 153, 76), "Original"))
            return color_data[0]
        
        def get_blanket_overlay_path(self, state="idle"):
            """
            Returns the path to the blanket overlay sprite for tinting.
            The overlay should be a white silhouette of just the blanket area.
            
            Uses a single overlay file since the blanket silhouette is identical
            across all states (idle, blink, hover).
            
            IN:
                state (str): Unused, kept for compatibility
                
            OUT:
                str: Path to the blanket overlay sprite
            """
            # Single overlay file per chibi - blanket shape is the same for all states
            return store.ep_folders._join_path(
                store.ep_folders.EP_CHIBIS, 
                self.doki, 
                "blanket.png"
            )
        
        def to_dict(self):
            """
            Serializes the chibi for saving to persistent.
            
            OUT:
                dict: Dictionary with all chibi properties
            """
            return {
                "id": self.id,
                "doki": self.doki,
                "costume": self.costume,
                "x": self.x,
                "y": self.y,
                "draggable": self.draggable,
                "visible": self.visible,
                "accessory_1": self.accessory_1,
                "accessory_2": self.accessory_2,
                "accessory_3": self.accessory_3,
                "blanket_color": self.blanket_color,
            }
        
        @classmethod
        def from_dict(cls, data):
            """
            Reconstructs a chibi from saved data.
            
            IN:
                data (dict): Dictionary with chibi properties
                
            OUT:
                ChibiCharacter: Restored chibi instance
            """
            chibi = cls(
                data.get("id", "unknown"),
                data.get("doki", "darling"),
                data.get("costume", "blanket"),
                data.get("x", 0.025),
                data.get("y", 385)
            )
            chibi.draggable = data.get("draggable", False)
            chibi.visible = data.get("visible", True)
            chibi.accessory_1 = data.get("accessory_1", "0nothing")
            chibi.accessory_2 = data.get("accessory_2", "0nothing")
            chibi.accessory_3 = data.get("accessory_3", "0nothing")
            chibi.blanket_color = data.get("blanket_color", "original")
            return chibi
        
        @classmethod
        def from_legacy_tuple(cls, chibi_id, legacy_tuple, x=0.025, y=385):
            """
            Creates a ChibiCharacter from the old tuple format.
            Legacy format: (folder, idle, blink, hover)
            
            IN:
                chibi_id (str): ID for the new chibi
                legacy_tuple (tuple): Old format costume tuple
                x (float/int): X position
                y (int): Y position
                
            OUT:
                ChibiCharacter: New chibi instance
            """
            try:
                doki = legacy_tuple[0]
                # Try to determine costume from idle sprite name
                idle_sprite = legacy_tuple[1]
                
                # Match sprite pattern to costume
                costume = "blanket"  # Default
                if "casual" in idle_sprite:
                    costume = "casual"
                elif "android" in idle_sprite:
                    costume = "android"
                elif "bikini" in idle_sprite:
                    costume = "bikini"
                
                return cls(chibi_id, doki, costume, x, y)
            except (IndexError, TypeError):
                return cls(chibi_id, "darling", "blanket", x, y)
        
        def __repr__(self):
            return "ChibiCharacter(id='{}', doki='{}', costume='{}')".format(
                self.id, self.doki, self.costume
            )


# =============================================================================
# CHIBI MANAGER CLASS
# Manages multiple chibi instances on screen
# =============================================================================
init -14 python in ep_chibis:
    
    class ChibiManager(object):
        """
        Manager for multiple chibi characters on screen.
        Handles registration, lookup, cloning, and persistence.
        """
        
        MAIN_CHIBI_ID = "main"
        
        def __init__(self):
            """Initialize the chibi manager."""
            self._chibis = {}  # Dict of id -> ChibiCharacter
            self._initialized = False
        
        def initialize(self):
            """
            Initialize the manager and load/migrate data.
            Should be called after persistent is available.
            """
            if self._initialized:
                return
            
            # Try to load from new format first
            if self._load_from_persistent():
                self._initialized = True
                return
            
            # If no new data, migrate from legacy format
            self._migrate_from_legacy()
            self._initialized = True
        
        def register(self, chibi):
            """
            Registers a chibi with the manager.
            
            IN:
                chibi (ChibiCharacter): The chibi to register
                
            OUT:
                ChibiCharacter: The registered chibi
            """
            self._chibis[chibi.id] = chibi
            return chibi
        
        def unregister(self, chibi_id):
            """
            Removes a chibi from the manager.
            Cannot remove the main chibi.
            
            IN:
                chibi_id (str): ID of the chibi to remove
                
            OUT:
                bool: True if removed, False otherwise
            """
            if chibi_id in self._chibis and chibi_id != self.MAIN_CHIBI_ID:
                del self._chibis[chibi_id]
                return True
            return False
        
        def get(self, chibi_id):
            """
            Gets a chibi by ID.
            
            IN:
                chibi_id (str): ID of the chibi to get
                
            OUT:
                ChibiCharacter or None: The chibi if found
            """
            return self._chibis.get(chibi_id)
        
        @property
        def main(self):
            """Returns the main chibi instance."""
            return self._chibis.get(self.MAIN_CHIBI_ID)
        
        @property
        def all(self):
            """Returns all registered chibis."""
            return list(self._chibis.values())
        
        @property
        def visible(self):
            """Returns all visible chibis."""
            return [c for c in self._chibis.values() if c.visible]
        
        @property
        def count(self):
            """Returns the number of registered chibis."""
            return len(self._chibis)
        
        @property
        def secondary_visible(self):
            """Returns all visible chibis except the main one."""
            if not store.persistent._mas_pm_cares_about_dokis:
                return []
            return [c for c in self._chibis.values() if c.visible and c.id != self.MAIN_CHIBI_ID]
        
        def create_clone(self, source_id=None, new_id=None, offset_x=0.05):
            """
            Creates a clone of a chibi.
            
            IN:
                source_id (str or None): ID of chibi to clone (None = main chibi)
                new_id (str or None): ID for the clone (None = auto-generate)
                offset_x (float): X offset for the clone's position
                
            OUT:
                ChibiCharacter or None: The new clone, or None if source not found
            """
            source = self.get(source_id) if source_id else self.main
            if source:
                clone = source.clone(new_id)
                clone.x = source.x + offset_x
                self.register(clone)
                return clone
            return None
        
        def remove_all_clones(self):
            """Removes all chibis except the main one."""
            to_remove = [cid for cid in self._chibis.keys() if cid != self.MAIN_CHIBI_ID]
            for cid in to_remove:
                del self._chibis[cid]
        
        def save(self):
            """Saves all chibi data to persistent storage."""
            data = {}
            for cid, chibi in self._chibis.items():
                data[cid] = chibi.to_dict()
            store.persistent._ep_chibis_manager_data = data
        
        def _load_from_persistent(self):
            """
            Loads chibis from persistent storage.
            
            OUT:
                bool: True if data was loaded, False otherwise
            """
            data = store.persistent._ep_chibis_manager_data
            if not data or not isinstance(data, dict):
                return False
            
            for cid, chibi_data in data.items():
                try:
                    self._chibis[cid] = ChibiCharacter.from_dict(chibi_data)
                except Exception:
                    pass
            
            return len(self._chibis) > 0
        
        def _migrate_from_legacy(self):
            """
            Migrates data from the old persistent format to the new system.
            Old format used:
                - persistent.chibika_current_costume (tuple)
                - persistent.chibika_drag_x, persistent.chibika_drag_y
                - persistent.enable_drag_chibika
                - persistent.chibi_accessory_1_, etc.
            """
            try:
                # Get legacy data
                legacy_costume = store.persistent.chibika_current_costume
                legacy_x = store.persistent.chibika_drag_x
                legacy_y = store.persistent.chibika_drag_y
                legacy_draggable = store.persistent.enable_drag_chibika
                
                # Determine default Y based on noises submod
                default_y = 345 if store.ep_tools.noises_submod else 385
                
                # Create main chibi from legacy data
                if legacy_costume and isinstance(legacy_costume, tuple) and len(legacy_costume) >= 4:
                    main_chibi = ChibiCharacter.from_legacy_tuple(
                        self.MAIN_CHIBI_ID,
                        legacy_costume,
                        legacy_x if legacy_x is not None else 0.025,
                        legacy_y if legacy_y is not None else default_y
                    )
                else:
                    main_chibi = ChibiCharacter(
                        self.MAIN_CHIBI_ID, 
                        "darling", 
                        "blanket",
                        0.025,
                        default_y
                    )
                
                # Apply legacy settings
                main_chibi.draggable = legacy_draggable if legacy_draggable is not None else False
                
                # Migrate accessories
                if hasattr(store.persistent, 'chibi_accessory_1_'):
                    main_chibi.accessory_1 = store.persistent.chibi_accessory_1_ or "0nothing"
                if hasattr(store.persistent, 'chibi_accessory_2_'):
                    main_chibi.accessory_2 = store.persistent.chibi_accessory_2_ or "0nothing"
                if hasattr(store.persistent, 'chibi_accessory_3_'):
                    main_chibi.accessory_3 = store.persistent.chibi_accessory_3_ or "0nothing"
                
                # Migrate blanket color if it exists
                saved_color = store.persistent._ep_chibi_blanket_color
                if saved_color and saved_color in ChibiCharacter.BLANKET_COLORS:
                    main_chibi.blanket_color = saved_color
                
                self.register(main_chibi)
                
            except Exception:
                # If anything fails, create a default main chibi
                default_y = 345 if store.ep_tools.noises_submod else 385
                self.register(ChibiCharacter(self.MAIN_CHIBI_ID, "darling", "blanket", 0.025, default_y))
        
        def sync_to_legacy(self):
            """
            Syncs the main chibi's state back to legacy persistent variables.
            This maintains backwards compatibility with code that still uses the old format.
            """
            main = self.main
            if not main:
                return
            
            # Sync costume as legacy tuple format
            sprites = main.sprites
            store.persistent.chibika_current_costume = (main.doki, sprites[0], sprites[1], sprites[2])
            
            # Sync position
            store.persistent.chibika_drag_x = main.x
            store.persistent.chibika_drag_y = main.y
            
            # Sync draggable state
            store.persistent.enable_drag_chibika = main.draggable
            
            # Sync accessories
            store.persistent.chibi_accessory_1_ = main.accessory_1
            store.persistent.chibi_accessory_2_ = main.accessory_2
            store.persistent.chibi_accessory_3_ = main.accessory_3


# =============================================================================
# GLOBAL MANAGER INSTANCE
# =============================================================================
init -13 python in ep_chibis:
    # Create the global manager instance
    chibi_manager = ChibiManager()


# =============================================================================
# INITIALIZATION - Load/migrate data when game starts
# =============================================================================
init 5 python in ep_chibis:
    # Initialize the manager (loads or migrates data)
    chibi_manager.initialize()


# =============================================================================
# HELPER FUNCTIONS - Convenience wrappers for common operations
# =============================================================================
init -12 python in ep_chibis:
    
    def get_main_chibi():
        """
        Returns the main chibi instance.
        
        OUT:
            ChibiCharacter: The main chibi
        """
        return chibi_manager.main
    
    def clone_main_chibi(new_id=None, offset_x=0.05):
        """
        Creates a clone of the main chibi.
        
        IN:
            new_id (str or None): ID for the clone
            offset_x (float): X position offset
            
        OUT:
            ChibiCharacter: The new clone
        """
        return chibi_manager.create_clone(new_id=new_id, offset_x=offset_x)
    
    def get_all_visible_chibis():
        """
        Returns all visible chibi instances.
        
        OUT:
            list: List of visible ChibiCharacter instances
        """
        return chibi_manager.visible
    
    def save_chibis():
        """Saves all chibi data and syncs to legacy format."""
        chibi_manager.save()
        chibi_manager.sync_to_legacy()
    
    def toggle_draggable():
        """
        Toggles the draggable state for the currently editing chibi.
        Syncs legacy persistent only when targeting the main chibi.
        """
        target = get_editing_chibi()
        if target:
            target.draggable = not target.draggable
            # Only sync legacy persistent for the main chibi
            if _editing_chibi_id == chibi_manager.MAIN_CHIBI_ID:
                store.persistent.enable_drag_chibika = target.draggable
            # Save immediately
            save_chibis()
        else:
            # Fallback to just toggling persistent
            store.persistent.enable_drag_chibika = not store.persistent.enable_drag_chibika


# =============================================================================
# LEGACY COMPATIBILITY LAYER
# These functions maintain compatibility with existing code
# =============================================================================
init -11 python in ep_chibis:
    
    def get_current_costume_tuple():
        """
        Returns the current costume in legacy tuple format for backwards compatibility.
        
        OUT:
            tuple: (doki, idle, blink, hover) format
        """
        main = chibi_manager.main
        if main:
            sprites = main.sprites
            return (main.doki, sprites[0], sprites[1], sprites[2])
        return ("darling", "idle", "blink", "hover")
    
    def set_costume_from_tuple(costume_tuple):
        """
        Sets the currently editing chibi's costume from a legacy tuple.
        Syncs legacy persistent only when targeting the main chibi.
        
        IN:
            costume_tuple (tuple): (doki, idle, blink, hover) format
        """
        target = get_editing_chibi()
        if target and costume_tuple and len(costume_tuple) >= 4:
            doki = costume_tuple[0]
            idle_sprite = costume_tuple[1]
            
            # Determine costume from sprite name
            costume = "blanket"
            if "casual" in idle_sprite:
                costume = "casual"
            elif "android" in idle_sprite:
                costume = "android"
            elif "bikini" in idle_sprite:
                costume = "bikini"
            
            target.set_doki(doki, costume)
            
            # Sync back to persistent only for main chibi
            if _editing_chibi_id == chibi_manager.MAIN_CHIBI_ID:
                store.persistent.chibika_current_costume = costume_tuple


# =============================================================================
# DYNAMIC DISPLAYABLE FUNCTIONS - Updated to use new system
# =============================================================================
init -10 python in ep_chibis:
    
    def draw_chibi_sprite(st, at, chibi_id=None, state="idle"):
        """
        Dynamic displayable function that draws a chibi sprite.
        Applies blanket color overlay when applicable.
        
        IN:
            st, at: Ren'Py displayable parameters
            chibi_id (str or None): ID of chibi to draw (None = main)
            state (str): Sprite state ("idle", "blink", "hover")
            
        OUT:
            tuple: (displayable, refresh_time)
        """
        chibi = chibi_manager.get(chibi_id) if chibi_id else chibi_manager.main
        if chibi:
            # Use the new overlay system for blanket colors
            sprite = get_chibi_sprite_with_blanket_color(chibi, state)
            return sprite, 1
        
        # Fallback to default
        return store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "darling", "idle.png"), 1
    
    def draw_tinted_chibi_idle(st, at):
        """DynamicDisplayable wrapper for idle sprite with color tinting."""
        return draw_chibi_sprite(st, at, state="idle")
    
    def draw_tinted_chibi_blink(st, at):
        """DynamicDisplayable wrapper for blink sprite with color tinting."""
        return draw_chibi_sprite(st, at, state="blink")
    
    def draw_tinted_chibi_hover(st, at):
        """DynamicDisplayable wrapper for hover sprite with color tinting."""
        return draw_chibi_sprite(st, at, state="hover")
    
    def draw_chibi_blink_effect(st, at):
        """
        DynamicDisplayable that handles the blink animation with color overlay.
        Alternates between idle and blink sprites at varying intervals.
        
        IN:
            st: Shown time
            at: Animation time
            
        OUT:
            tuple: (displayable, next_update_time)
        """
        chibi = chibi_manager.main
        if not chibi:
            return store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "darling", "idle.png"), 0.1
        
        # Determine if we should show blink or idle based on time
        # Blink cycle: mostly idle with occasional short blinks
        cycle_time = st % 4.0  # 4 second cycle
        
        # Blink happens around 3.5-3.6 seconds in the cycle (quick blink)
        if 3.5 <= cycle_time < 3.6:
            state = "blink"
            next_update = 0.1
        else:
            state = "idle"
            # Calculate time until next potential state change
            if cycle_time < 3.5:
                next_update = 3.5 - cycle_time
            else:
                next_update = 4.0 - cycle_time + 0.01
        
        # Use the new overlay system for blanket colors
        sprite = get_chibi_sprite_with_blanket_color(chibi, state)
        return sprite, next_update
    
    def get_main_sprite_path(state="idle"):
        """
        Returns the sprite path for the main chibi.
        Useful for ATL images and other places that need the path directly.
        
        IN:
            state (str): "idle", "blink", or "hover"
            
        OUT:
            str: Full path to the sprite
        """
        main = chibi_manager.main
        if main:
            return main.get_sprite_path(state)
        
        # Fallback to legacy persistent
        try:
            costume = store.persistent.chibika_current_costume
            sprite_map = {"idle": 1, "blink": 2, "hover": 3}
            idx = sprite_map.get(state, 1)
            return store.ep_chibis.sprite_path.format(costume[0], costume[idx])
        except (IndexError, TypeError):
            return store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "darling", "idle.png")
    
    def get_main_chibi_doki():
        """
        Returns the doki type of the main chibi.
        
        OUT:
            str: Doki type ("darling", "cupcake", "cinnamon", "teacup")
        """
        main = chibi_manager.main
        if main:
            return main.doki
        
        # Fallback to legacy
        try:
            return store.persistent.chibika_current_costume[0]
        except (IndexError, TypeError):
            return "darling"


# =============================================================================
# BLANKET COLOR FUNCTIONS - Tint overlay system for blanket sprites
# =============================================================================
init -9 python in ep_chibis:
    import os
    
    def get_current_filter():
        """
        Gets the current MAS filter (day/night/sunset).
        
        RETURNS: Current filter string
        """
        try:
            return store.mas_sprites.get_filter()
        except:
            return "day"
    
    def apply_filter_to_image(img_path):
        """
        Applies the current MAS filter to an image path.
        
        IN:
            img_path (str): Path to the image
            
        RETURNS: Filtered displayable
        """
        try:
            flt = get_current_filter()
            return store.mas_sprites._gen_im(flt, img_path)
        except:
            return img_path
    
    def get_tinted_blanket_composite(base_path, overlay_path, rgb_color):
        """
        Creates a composite image with a tinted blanket overlay.
        Applies the current MAS filter to both base and overlay.
        
        IN:
            base_path (str): Path to base sprite (with grayscale blanket)
            overlay_path (str): Path to white blanket overlay
            rgb_color (tuple): (R, G, B) color values 0-255
            
        OUT:
            displayable: LiveComposite with filtered base + tinted overlay
        """
        # Convert RGB from 0-255 to 0.0-1.0 for im.matrix.tint
        r = rgb_color[0] / 255.0
        g = rgb_color[1] / 255.0
        b = rgb_color[2] / 255.0
        
        # Apply current filter to base sprite
        filtered_base = apply_filter_to_image(base_path)
        
        # Create the tinted overlay using im.MatrixColor with tint matrix.
        # im.matrix.tint / im.MatrixColor are Ren'Py 6.99 APIs;
        # in Ren'Py 7.x they were deprecated. Fall back to showing the
        # overlay unmodified (no tinting) so the chibi still renders.
        try:
            tint_matrix = store.im.matrix.tint(r, g, b)
            tinted_overlay = store.im.MatrixColor(overlay_path, tint_matrix)
        except Exception:
            tinted_overlay = overlay_path
        
        # Apply time-of-day filter to the tinted overlay
        filtered_overlay = apply_filter_to_image(tinted_overlay)
        
        # Combine filtered base and filtered tinted overlay
        return store.LiveComposite(
            (188, 188),
            (0, 0), filtered_base,
            (0, 0), filtered_overlay
        )
    
    def get_chibi_sprite_with_blanket_color(chibi, state="idle"):
        """
        Returns the appropriate displayable for a chibi with blanket color applied.
        If the overlay file doesn't exist, returns the base sprite with filter.
        
        IN:
            chibi (ChibiCharacter): The chibi instance
            state (str): "idle", "blink", or "hover"
            
        OUT:
            displayable: The sprite (possibly with color overlay)
        """
        base_path = chibi.get_sprite_path(state)
        
        # Only apply color for blanket costume
        if chibi.costume != "blanket":
            # Still apply filter for day/night
            return apply_filter_to_image(base_path)
        
        overlay_path = chibi.get_blanket_overlay_path(state)
        
        # Check if overlay file exists
        if renpy.loadable(overlay_path):
            rgb_color = chibi.get_blanket_rgb()
            return get_tinted_blanket_composite(base_path, overlay_path, rgb_color)
        
        # Fallback to base sprite with filter if no overlay
        return apply_filter_to_image(base_path)
    
    def get_main_chibi_tinted_sprite(state="idle"):
        """
        Returns the main chibi's sprite with blanket color applied.
        
        IN:
            state (str): "idle", "blink", or "hover"
            
        OUT:
            displayable: The (possibly tinted) sprite
        """
        main = chibi_manager.main
        if not main:
            return store.ep_folders._join_path(store.ep_folders.EP_CHIBIS, "darling", "idle.png")
        
        return get_chibi_sprite_with_blanket_color(main, state)
    
    def set_main_blanket_color(color_name):
        """
        Sets the blanket color for the main chibi.
        Also saves to persistent for backwards compatibility.
        
        IN:
            color_name (str): Color name from BLANKET_COLORS
            
        OUT:
            bool: True if successful
        """
        main = chibi_manager.main
        if main:
            success = main.set_blanket_color(color_name)
            if success:
                store.persistent._ep_chibi_blanket_color = color_name
            return success
        return False
    
    def get_available_blanket_colors():
        """
        Returns list of available blanket colors for UI.
        
        OUT:
            list: List of (color_key, display_name) tuples
        """
        colors = ChibiCharacter.BLANKET_COLORS
        return [(key, colors[key][1]) for key in colors]
    
    class SelectBlanketColor(object):
        """Callable action that changes the editing chibi's blanket color."""
        __slots__ = ['name', 'color_key']
        
        def __init__(self, name, color_key):
            self.name = name
            self.color_key = color_key

        @property
        def display_name(self):
            """Returns the name with an asterisk if it's currently selected."""
            target = get_editing_chibi()
            if target:
                if target.blanket_color == self.color_key:
                    return self.name + " *"
            return self.name
        
        def __call__(self):
            target = get_editing_chibi()
            if target:
                target.set_blanket_color(self.color_key)
                # Only sync to persistent for main chibi
                if _editing_chibi_id == chibi_manager.MAIN_CHIBI_ID:
                    store.persistent._ep_chibi_blanket_color = self.color_key
            # Save and refresh chibi display
            save_chibis()
            renpy.restart_interaction()


# =============================================================================
# MULTI-CHIBI DISPLAY SYSTEM
# Enables showing multiple doki chibis on screen simultaneously
# =============================================================================
init -8 python in ep_chibis:
    
    # Default positions for secondary dokis (spread across the bottom)
    DOKI_POSITIONS = {
        "cupcake":  {"x": 0.15, "y": 385},
        "cinnamon": {"x": 0.27, "y": 385},
        "teacup":   {"x": 0.40, "y": 385},
    }
    
    # ---- Editing State ----
    # Tracks which chibi is currently selected for customization.
    # Used by DokiAccessory, SelectDOKI, SelectBlanketColor, toggle_draggable, etc.
    _editing_chibi_id = "main"
    
    def set_editing_chibi(chibi_id):
        """
        Sets which chibi is currently being customized.
        
        IN:
            chibi_id (str): ID of the chibi to edit
        """
        global _editing_chibi_id
        _editing_chibi_id = chibi_id
        renpy.restart_interaction()
    
    def get_editing_chibi():
        """
        Returns the ChibiCharacter currently selected for editing.
        Falls back to main chibi if the selected one doesn't exist
        or if the player doesn't care about the other dokis.
        
        OUT:
            ChibiCharacter: The chibi being edited
        """
        if not store.persistent._mas_pm_cares_about_dokis:
            return chibi_manager.main

        target = chibi_manager.get(_editing_chibi_id)
        if target:
            return target
        return chibi_manager.main
    
    def get_editing_chibi_id():
        """
        Returns the ID of the chibi currently selected for editing.
        Respects the cares_about_dokis check.
        
        OUT:
            str: Chibi ID
        """
        if not store.persistent._mas_pm_cares_about_dokis:
            return "main"
        return _editing_chibi_id
    
    # Display names for the chibi selector UI
    DOKI_DISPLAY_NAMES = {
        "main": _("Chibika"),
        "cupcake": _("Chibisuki"),
        "cinnamon": _("Chibiyori"),
        "teacup": _("Chibiyuri"),
    }
    
    def toggle_main_visibility():
        """
        Toggles only the main chibi's visibility without affecting
        the overlay or secondary chibis.
        """
        main = chibi_manager.main
        if main:
            main.visible = not main.visible
            save_chibis()
            renpy.restart_interaction()
    
    def is_main_visible():
        """
        Checks if the main chibi is currently visible.
        
        OUT:
            bool: True if main chibi exists and is visible
        """
        main = chibi_manager.main
        return main is not None and main.visible
    
    # Cache for displayable objects per chibi ID
    # The DynamicDisplayable children update automatically, so this cache
    # only needs to be cleared if a chibi is completely removed/replaced.
    _chibi_displayable_cache = {}
    
    def _create_chibi_draw_functions(chibi_id):
        """
        Creates DynamicDisplayable draw functions for a given chibi_id.
        Closures capture chibi_id to avoid variable binding issues in loops.
        
        Accessories use None as redraw interval (only update on restart_interaction),
        avoiding continuous polling while staying reactive to changes.
        
        IN:
            chibi_id (str): ID of the chibi
            
        OUT:
            dict: Dictionary of draw functions
        """
        def _draw_blink(st, at):
            chibi = chibi_manager.get(chibi_id)
            if not chibi:
                return store.Null(), 1.0
            
            cycle_time = st % 4.0
            if 3.5 <= cycle_time < 3.6:
                state = "blink"
                next_update = 0.1
            else:
                state = "idle"
                if cycle_time < 3.5:
                    next_update = 3.5 - cycle_time
                else:
                    next_update = 4.0 - cycle_time + 0.01
            
            sprite = get_chibi_sprite_with_blanket_color(chibi, state)
            return sprite, next_update
        
        def _draw_hover(st, at):
            chibi = chibi_manager.get(chibi_id)
            if not chibi:
                return store.Null(), 1.0
            return get_chibi_sprite_with_blanket_color(chibi, "hover"), 1
        
        def _draw_bg_acc(st, at):
            chibi = chibi_manager.get(chibi_id)
            accessory = chibi.accessory_3 if chibi else "0nothing"
            return store.MASFilterSwitch(
                store.ep_chibis.accessory_path_2.format(accessory)
            ), 1
        
        def _draw_fg_acc1(st, at):
            chibi = chibi_manager.get(chibi_id)
            accessory = chibi.accessory_1 if chibi else "0nothing"
            return store.MASFilterSwitch(
                store.ep_chibis.accessory_path_0.format(accessory)
            ), 1
        
        def _draw_fg_acc2(st, at):
            chibi = chibi_manager.get(chibi_id)
            accessory = chibi.accessory_2 if chibi else "0nothing"
            return store.MASFilterSwitch(
                store.ep_chibis.accessory_path_1.format(accessory)
            ), 1
        
        return {
            "blink": _draw_blink,
            "hover": _draw_hover,
            "bg_acc": _draw_bg_acc,
            "fg_acc1": _draw_fg_acc1,
            "fg_acc2": _draw_fg_acc2,
        }
    
    def get_chibi_displayables(chibi_id):
        """
        Returns cached 'base' and 'hover' LiveComposite displayables for a chibi.
        
        Uses DynamicDisplayable for all layers. Accessories use None as redraw
        interval so they only update on restart_interaction() calls, not polling.
        
        IN:
            chibi_id (str): ID of the chibi
            
        OUT:
            dict: {"base": LiveComposite, "hover": LiveComposite}
        """
        if chibi_id not in _chibi_displayable_cache:
            funcs = _create_chibi_draw_functions(chibi_id)
            
            base = store.LiveComposite(
                (188, 188),
                (0, 0), store.DynamicDisplayable(funcs["bg_acc"]),
                (0, 0), store.DynamicDisplayable(funcs["blink"]),
                (0, 0), store.DynamicDisplayable(funcs["fg_acc1"]),
                (0, 0), store.DynamicDisplayable(funcs["fg_acc2"]),
            )
            hover = store.LiveComposite(
                (188, 188),
                (0, 0), store.DynamicDisplayable(funcs["bg_acc"]),
                (0, 0), store.DynamicDisplayable(funcs["hover"]),
                (0, 0), store.DynamicDisplayable(funcs["fg_acc1"]),
                (0, 0), store.DynamicDisplayable(funcs["fg_acc2"]),
            )
            _chibi_displayable_cache[chibi_id] = {"base": base, "hover": hover}
        
        return _chibi_displayable_cache[chibi_id]
    
    def invalidate_displayable_cache(chibi_id=None):
        """
        Clears cached displayables. Normally not needed since
        DynamicDisplayable children update automatically, but useful
        if a chibi is removed and re-created with different structure.
        
        IN:
            chibi_id (str or None): Specific chibi to clear, or None for all
        """
        if chibi_id:
            _chibi_displayable_cache.pop(chibi_id, None)
        else:
            _chibi_displayable_cache.clear()
    
    def show_doki(doki_id):
        """
        Shows a single secondary doki. Restores saved settings if available
        from persistent, otherwise creates with defaults.
        
        IN:
            doki_id (str): ID of the doki to show (cupcake, cinnamon, teacup)
        """
        if doki_id not in DOKI_POSITIONS:
            return
        
        existing = chibi_manager.get(doki_id)
        if existing:
            # Already registered, just make sure it's visible
            existing.visible = True
            save_chibis()
            reset_chibi()
            return
        
        # Check if we have saved data for this doki in persistent
        saved_data = store.persistent._ep_chibis_manager_data
        if saved_data and isinstance(saved_data, dict) and doki_id in saved_data:
            # Restore from saved settings
            chibi = ChibiCharacter.from_dict(saved_data[doki_id])
            chibi.visible = True
        else:
            # Create fresh with defaults
            pos = DOKI_POSITIONS[doki_id]
            default_y = 345 if store.ep_tools.noises_submod else 385
            chibi = ChibiCharacter(
                doki_id, doki_id, "blanket",
                pos["x"], pos.get("y", default_y)
            )
        
        chibi_manager.register(chibi)
        save_chibis()
        reset_chibi()
    
    def hide_doki(doki_id):
        """
        Hides a single secondary doki by setting visible=False.
        Does NOT unregister — keeps all settings intact.
        
        IN:
            doki_id (str): ID of the doki to hide
        """
        if doki_id not in DOKI_POSITIONS:
            return
        
        chibi = chibi_manager.get(doki_id)
        if chibi:
            chibi.visible = False
            save_chibis()
        
        # If we were editing this doki, switch back to main
        if _editing_chibi_id == doki_id:
            set_editing_chibi(chibi_manager.MAIN_CHIBI_ID)
        
        renpy.restart_interaction()
    
    def toggle_doki(doki_id):
        """
        Toggles visibility of a single doki.
        
        IN:
            doki_id (str): ID of the doki to toggle
        """
        if is_doki_visible(doki_id):
            hide_doki(doki_id)
        else:
            show_doki(doki_id)
    
    def is_doki_visible(doki_id):
        """
        Checks if a specific doki is currently visible.
        
        IN:
            doki_id (str): ID of the doki to check
            
        OUT:
            bool: True if the doki is registered and visible
        """
        chibi = chibi_manager.get(doki_id)
        return chibi is not None and chibi.visible

    def show_all_dokis():
        """
        Shows all 3 secondary dokis at once.
        Each one restores saved settings individually.
        """
        for doki_id in DOKI_POSITIONS:
            show_doki(doki_id)
    
    def hide_extra_dokis():
        """
        Hides all secondary dokis by setting visible=False.
        Settings are preserved in the manager.
        """
        for doki_id in DOKI_POSITIONS:
            chibi = chibi_manager.get(doki_id)
            if chibi:
                chibi.visible = False
        
        # If editing a secondary doki, switch back to main
        if _editing_chibi_id in DOKI_POSITIONS:
            set_editing_chibi(chibi_manager.MAIN_CHIBI_ID)
        
        save_chibis()
        renpy.restart_interaction()
    
    def are_extra_dokis_visible():
        """
        Checks if any secondary dokis are currently visible.
        
        OUT:
            bool: True if at least one secondary doki is active
        """
        for doki_id in DOKI_POSITIONS:
            if is_doki_visible(doki_id):
                return True
        return False
    
    def toggle_all_dokis():
        """
        Toggles between showing all 4 dokis and just the main chibi.
        """
        if are_extra_dokis_visible():
            hide_extra_dokis()
        else:
            show_all_dokis()
    
    # Map chibi IDs to their canonical doki name for costume filtering
    DOKI_ID_MAP = {
        "main": "darling",
        "cupcake": "cupcake",
        "cinnamon": "cinnamon",
        "teacup": "teacup",
    }
    
    # Map doki names to their costume list attribute names
    DOKI_COSTUME_MAP = {
        "darling": "monika_costumes_",
        "cupcake": "natsuki_costumes_",
        "cinnamon": "sayori_costumes_",
        "teacup": "yuri_costumes_",
    }
    
    def get_costumes_for_editing_chibi():
        """
        Returns the costume list for the chibi currently being edited.
        Ensures each chibi only shows their own doki's outfits.
        
        OUT:
            list: List of (name, costume_tuple) pairs for the editing chibi's doki
        """
        target = get_editing_chibi()
        if target:
            doki = target.doki
        else:
            doki = "darling"
        
        costume_attr = DOKI_COSTUME_MAP.get(doki, "monika_costumes_")
        return getattr(store.ep_chibis, costume_attr, [])
    
    def make_drag_handler(chibi_id):
        """
        Creates a drag callback closure for a specific chibi.
        
        IN:
            chibi_id (str): ID of the chibi this handler is for
            
        OUT:
            function: Drag callback compatible with Ren'Py's drag system
        """
        def _handler(drags, drop):
            try:
                chibi = chibi_manager.get(chibi_id)
                if chibi:
                    chibi.move_to(drags[0].x, drags[0].y)
                
                # Only sync legacy persistent for the main chibi
                if chibi_id == chibi_manager.MAIN_CHIBI_ID:
                    store.persistent.chibika_drag_x = drags[0].x
                    store.persistent.chibika_drag_y = drags[0].y
                
                # Save positions to persistent so they survive restarts
                save_chibis()
            except Exception:
                pass
        return _handler
    
    def click_chibi(chibi_id):
        """
        Click handler for any chibi (main or secondary).
        Handles click counting and anger/poof logic.
        
        IN:
            chibi_id (str): ID of the clicked chibi
        """
        chibi = chibi_manager.get(chibi_id)
        if not chibi:
            return
        
        chibi.handle_click()
        
        if chibi.is_angry:
            if chibi_id == chibi_manager.MAIN_CHIBI_ID:
                # Main chibi: remove from overlay (existing behavior)
                store.ep_chibis.temp_chibi_anger = True
                remove_chibi()
            else:
                # Secondary chibi: just hide it, don't affect the overlay
                # It will reappear when show_all_dokis() is called again
                pass


# =============================================================================
# PERSISTENT VARIABLES FOR NEW SYSTEM
# =============================================================================
default persistent._ep_chibis_manager_data = None
default persistent._ep_chibi_blanket_color = "original"
