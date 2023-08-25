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
        description="A submod that adds an Extra+ button, as well as adding more content!",
        version="1.1.0"
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
    "Choose one, [player].",
    "Want a new challenge?",
    "I would love to play with you~",
    "What will we play today?",
    "Let's have some fun!",
    "Time to show off your skills!",
    "Ready to play?",
    "Let's see how good you are!",
    "Which game do you want to try?",
    "Shall we play a game?",
    "I'm feeling lucky today, [player].",
    "Are you ready for some fun?",
    "Let's see if you can beat me!",
    "Time for some friendly competition!",
    "I'm up for any game you want to play.",
]

define date_talk = [
    "I can't wait to see where you take me!",
    "What adventures await us today?",
    "I'm excited to spend time with you.",
    "Let's make some great memories today.",
    "I hope we have a wonderful time together.",
    "Wherever we go, it will be perfect as long as we're together.",
    "I'm open to any suggestion you have.",
    "Let's do something fun and spontaneous!",
    "I'm so lucky to have you as my date!",
    "I can't wait to make more memories with you today.",
    "I'm up for anything you want to do!",
    "Let's make this a date to remember.",
    "I feel like today is going to be amazing!",
    "Wherever we end up, I'm happy as long as we're together.",
    "Let's have an unforgettable time today!"
]

#====Boop count
default persistent.plus_boop = [0, 0, 0] #Nose, Cheeks, Headpat.
default boop_war_count = 0
default persistent.extra_boop = [0, 0, 0] #Hands, Ears.

#====Chibika
define chibi_xpos = 0.05
define chibi_ypos = 385
default persistent.chibika_current_costume = blanket_chibi
define -1 blanket_chibi = [
    "sticker_up",
    "sticker_sleep",
    "sticker_baka"
]
define -1 android_chibi = [
    "android_sticker",
    "android_sticker_blink",
    "android_sticker_cat"
]
define -1 casual_chibi = [
    "casual_sticker",
    "casual_sticker_blink",
    "casual_sticker_happy"
]
define -1 chibi_sprites_0 = []
define -1 chibi_sprites_1 = []
default -1 persistent.chibi_accessory_layer_1 = 0
default -1 persistent.chibi_accessory_layer_2 = 0
default -1 persistent.hi_chibika = False
default -1 persistent.enable_drag_chibika = False

#====ExtraPlus Buttons
define minigames_menu = []
define tools_menu = []
define walk_menu = []

#====Misc
default Minigame_TTT = [
    "'",
    "#0142a4",
    "0",
    "#a80000"
]
# define -1 pictograms_allow = "'0adikouzFW14578*^~"
define -1 Pictograms_font = "submods/ExtraPlus/submod_assets/Pictograms.ttf"

# define 20 extra_current_affection = int(mas_affection._get_aff())
default moldable_variable = None
define plus_file_list = []
define extra_folder = None

#====BG
define extra_old_bg = None
define extra_chair = None
define extra_table = None

#====ZOOM
define player_zoom = None
default disable_zoom_button = None

#====Windows Title
define backup_window_title = "Monika After Story   "
default persistent.save_window_title = None


#====Minigames variables
#====Cup coordinates

#====RPS
define rps_your_choice = 0
default player_wins = 0
default moni_wins = 0

#====SG
define original_cup = [0, 1, 2]
define ball_position = 1
default _current_turn = 0
default shuffle_cups = 0
define cup_speed = 0.5
define difficulty_sg = None
default _correct_answers = 0
default _plus_comment = False
default cup_choice = None
define cup_coordinates = [695, 925, 1155]
define cup_coordinates_real = [695, 925, 1155]
define cup_list = ["cup.png", "cup_monika.png", "cup_yuri.png", "cup_natsuki.png", "cup_sayori.png"]
default cup_skin = None

#====Comments by moni on standard difficulties

define _plus_complies = [
    "Well done, [player]!",
    "Impressive, keep it up!",
    "You're doing great!",
    "Fantastic, [player]!",
    "Keep it up!",
    "You're making progress!",
    "Bravo, [player]!",
    "Outstanding, [player]!",
    "Way to go, [player]!",
    "Keep up the good work, [player]!",
    "You're doing fantastic!",
    "You're doing amazing!",
]

define _plus_not_met = [
    "Oh, too bad~",
    "It's not that, [player].",
    "Try again~",
    "Don't get distracted, [player].",
    "Keep practicing, [player].",
    "You'll get it next time!",
    "Better luck next try, [player].",
    "Don't give up, [player]!",
    "That's not quite it, [player].",
    "That wasn't the right answer, [player].",
    "Sorry, [player], that's not it.",
    "That wasn't the correct answer, [player]."
]

init 5 python:
    #====Monika idle v2
    monika_extraplus = MASMoniIdleDisp(
        (
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1eubla", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1hubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1eubla", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1esa", duration=30),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=30),
                    MASMoniIdleExp("1sua", duration=4),
                    MASMoniIdleExp("1ekblu", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
                    MASMoniIdleExp("1tuu", duration=30),
                    MASMoniIdleExp("1hua", duration=30),
                ]
            ),
            MASMoniIdleExp("1eua_follow", duration=40),
            MASMoniIdleExp("1kua", duration=1),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1mubla", duration=30, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1huu", duration=30),
        )
    )

#===========================================================================================
# FUNCTIONS
#===========================================================================================

init 5 python:
    #====Return a string that represents the gender of the player.
    def plus_player_gender():
        temp_person = "partner"
        if persistent.gender == "M":
            temp_person = "boyfriend"
        elif persistent.gender == "F":
            temp_person = "girlfriend"
        elif persistent.gender == "X" or persistent.gender != "X":
            temp_person = "beloved"
        return temp_person

    #====RNG
    def rng_cup():
        if store.persistent._mas_pm_cares_about_dokis:
            store.cup_skin = renpy.random.choice(cup_list)
        elif not store.persistent._mas_pm_cares_about_dokis:
            store.cup_skin = renpy.random.choice(["cup.png", "cup_monika.png"])

    #====Save the name
    def save_title_windows():
        if not store.persistent.save_window_title:
            config.window_title = store.backup_window_title
        else:
            config.window_title = persistent.save_window_title

    #====It checks if the files of a sprite exist.
    def check_file_status(plus_sprites, path):
        try:
            extra_folder = os.listdir(renpy.config.basedir + path)
            plus_file_list = [a for a in plus_sprites if a in extra_folder]
            if not set(plus_file_list) == set(plus_sprites):
                renpy.show("monika idle", at_list=[t11])
                renpy.call_screen("dialog", message="The files are not available...", ok_action=Jump("close_extraplus"))
        except OSError as e:
            renpy.show("monika idle", at_list=[t11])
            renpy.call_screen("dialog", message="Because there is a 'game' folder in the submod.", ok_action=Jump("close_extraplus"))   

    #====Functions for submod operation
    def Extraplus_show():
        show_chibika_chill()
        renpy.call_screen("submod_interactions")

    def ExtraButton():
        if not ExtraVisible():
            config.overlay_screens.append("extraplus_button")

    def ExtraVisible():
        return "extraplus_button" in config.overlay_screens
    
    #====Chibika
    def show_chibika_chill():
        if store.persistent.hi_chibika == True:
            if not visible_chibika_chill():
                config.overlay_screens.append("chibika_chill")
        elif renpy.random.randint(1,50) == 1:
            if not visible_chibika_chill():
                config.overlay_screens.append("chibika_chill")

    def visible_chibika_chill():
        return "chibika_chill" in config.overlay_screens
        
    def disable_chibika_chill():
        if visible_chibika_chill():
            config.overlay_screens.remove("chibika_chill")
            renpy.hide_screen("chibika_chill")

    def remove_show_chibika():
        if not renpy.get_screen("chibika_chill"):
            config.overlay_screens.append("chibika_chill")
        elif renpy.get_screen("chibika_chill"):
            config.overlay_screens.remove("chibika_chill")
            renpy.hide_screen("chibika_chill")

    def chibika_relax_drag(drags, drop):
        if not drop and store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
            drags[0].snap(chibi_xpos, 350, 0.7)
        if store.persistent.enable_drag_chibika == False:
            pass
        else:
            drags[0].snap(chibi_xpos, chibi_ypos, 0.7)
        return

    def draw_sprites(st, at):
        chibi_sprites_0_max = chibi_sprites_0[min(persistent.chibi_accessory_layer_1, len(chibi_sprites_0) - 1)]
        chibi_sprites_1_max = chibi_sprites_1[min(persistent.chibi_accessory_layer_2, len(chibi_sprites_1) - 1)]

        objects = LiveComposite(
            (119, 188),
            (0, 0), MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/accessories/0/{0}.png".format(chibi_sprites_0_max)),
            (0, 0), MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/accessories/1/{0}.png".format(chibi_sprites_1_max))
            )
        return objects, 0.1

    def chibi_costume_change():
        if persistent.chibika_current_costume == blanket_chibi:
            persistent.chibika_current_costume = android_chibi

        elif persistent.chibika_current_costume == android_chibi:
            persistent.chibika_current_costume = casual_chibi

        elif persistent.chibika_current_costume == casual_chibi:
            persistent.chibika_current_costume = blanket_chibi

        disable_chibika_chill()
        if not visible_chibika_chill():
            config.overlay_screens.append("chibika_chill")

    #====Zoom edit
    def extra_visible_zoom():
        return "button_custom_zoom" in config.overlay_screens

    def extra_button_zoom():
        if not extra_visible_zoom():
            config.overlay_screens.append("button_custom_zoom")

    def disable_button_zoom():
        if extra_visible_zoom():
            config.overlay_screens.remove("button_custom_zoom")
            renpy.hide_screen("button_custom_zoom")

    #====Saves temporaly the current room
    def mas_extra_location(locate=None):
        #====SAVE
        if locate:
            store.extra_chair = store.monika_chr.tablechair.chair
            store.extra_table = store.monika_chr.tablechair.table
            store.extra_old_bg = store.mas_current_background

        #====LOAD
        else:
            store.monika_chr.tablechair.chair = store.extra_chair
            store.monika_chr.tablechair.table = store.extra_table
            store.mas_current_background = store.extra_old_bg

    def extra_seen_background(sorry, extra_label, view_label):
        if store.mas_affection._get_aff() < 399:
            renpy.jump(sorry)

        if renpy.seen_label(view_label):
            store.mas_gainAffection(1,bypass=True)
            renpy.jump(extra_label)

        else:
            store.mas_gainAffection(5,bypass=True)
            pass
            
    def extra_seen_label(extra_label, view_label):
        if renpy.seen_label(view_label):
            renpy.jump(extra_label)
        else:
            pass

    ExtraButton()
    rng_cup()
    save_title_windows()

#===========================================================================================
# CLASSES
#===========================================================================================
#====Check if the selected cup is correct.
    class Verification(Action):
        def __init__(self, index, check_index, final_label):
            self.index = index
            self.check_index = check_index
            self.final_label = final_label

        def __call__(self):
            renpy.hide_screen("extra_no_click")
            renpy.hide_screen("shell_game_minigame")

            if self.final_label == "check_label":
                store.cup_choice = self.index

            if self.index == self.check_index:
                store._correct_answers += 1
                store._plus_comment = True
            else:
                store._plus_comment = False

            renpy.jump(self.final_label)

    #====A class that is used to display a list of available minigames
    class minigames:
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

    #====Class for use in gift creation
    class extra_gift:
        def __init__(self, name, gift):
            self.name = name
            self.gift = gift

        def __call__(self):
            global extraplus_gift
            extraplus_gift = (self.name, self.gift)
            file_path = os.path.join(renpy.config.basedir, 'characters', extraplus_gift[1])
            with open(file_path, 'a') as f:
                renpy.notify('The [extraplus_gift[0]] File has been successfully created.')
            renpy.jump('plus_make_gift')

#====Misc
init 10 python:
    chibi_sprites_0_path = renpy.config.basedir + "/game/submods/ExtraPlus/submod_assets/sprites/accessories/0/"
    chibi_sprites_1_path = renpy.config.basedir + "/game/submods/ExtraPlus/submod_assets/sprites/accessories/1/"
    if os.path.exists(chibi_sprites_0_path) and os.path.exists(chibi_sprites_1_path):
        chibi_sprites_0 = [(os.path.splitext(i)[0]) for i in os.listdir(chibi_sprites_0_path)]
        chibi_sprites_1 = [(os.path.splitext(j)[0]) for j in os.listdir(chibi_sprites_1_path)]
        show_chibika_chill()
    else:
        disable_chibika_chill()

#===========================================================================================
# IMAGES
#===========================================================================================
init python:

    plus_accessories = [
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

    for info in plus_accessories:
        name = info[0]
        acs = MASAccessory(*info)
        vars()[name] = acs
        store.mas_sprites.init_acs(acs)

#====Minigames images
image note_score = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/note_score.png")

#====TTT
image notebook = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/notebook.png")
image line_black = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line.png")
image line_player = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line_player.png")
image line_moni = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line_moni.png")
image ttt_cross:
    Text(
        Minigame_TTT[0],
        font = Pictograms_font,
        size = 180,
        color = Minigame_TTT[1],
        outlines = []
    )
    on show:
        alpha 0.5
        linear 0.25 alpha 1.0
image ttt_cross_cursor:
    Text(
        Minigame_TTT[0],
        font = Pictograms_font,
        size = 180,
        color = Minigame_TTT[1],
        outlines = []
    )
    alpha 0.25
    truecenter
image ttt_circle:
    Text(
        Minigame_TTT[2],
        font = Pictograms_font,
        size = 180,
        color = Minigame_TTT[3],
        outlines = []
    )
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
        
#====RPS
image e_paper = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/paper.png")
image e_rock = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/rock.png")
image e_scissors = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/scissors.png")
image card_back = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/card_back.png")

#====SG
image extra_cup = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/[cup_skin]")
image extra_cup_hover = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/cup_hover.png")
image extra_cup_idle = im.Scale("mod_assets/other/transparent.png", 200, 260)
image extra_ball = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/ball.png")
image cup:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_cup"
        xalign 0.5 yalign 0.5
image cup_hover:
    contains:
        "extra_cup_hover"
        xalign 0.5 yalign 0.5
image cup_idle:
    contains:
        "extra_cup_idle"
        xalign 0.5 yalign 0.
image ball:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_ball"
        xalign 0.5 yalign 0.5

#====Chibika
image chibika_blink_effect:
    block:
        MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/{0}.png".format(persistent.chibika_current_costume[0]))
        block:
            choice:
                3
            choice:
                5
            choice:
                7
        MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/{0}.png".format(persistent.chibika_current_costume[1]))
        choice 0.02:
            block:
                choice:
                    8
                choice:
                    6
                choice:
                    4
                MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/{0}.png".format(persistent.chibika_current_costume[0]))
        choice 0.098:
            pass
        0.06
        repeat


image chibika_base = LiveComposite(
    (119, 188),
    (0, 40), "chibika_blink_effect",
    (0, 0), DynamicDisplayable(draw_sprites)
    )

image hover_sticker = LiveComposite(
    (119, 188),
    (0, 40), ConditionSwitch(
        "blanket_chibi == persistent.chibika_current_costume", MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/sticker_baka.png"),
        "android_chibi == persistent.chibika_current_costume", MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/android_sticker_cat.png"),
        "casual_chibi == persistent.chibika_current_costume", MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/casual_sticker_happy.png")),
    (0, 0), DynamicDisplayable(draw_sprites)
    )

#====Coin
image coin_heads = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/coin_heads.png")
image coin_tails = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/coin_tails.png")
image coin_moni:
    ConditionSwitch(
        "mas_isDayNow()", anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin.png", (100, 100), (3, 2), .125, loop=True),
        "mas_isNightNow()", anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin-n.png", (100, 100), (3, 2), .125, loop=True))

#====Boop
image zoneone = im.Scale("mod_assets/other/transparent.png", 30, 30)
image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)
image zonethree = im.Scale("mod_assets/other/transparent.png", 40, 40)
image zonefour = im.Scale("mod_assets/other/transparent.png", 90, 60)

#====Idle edit
image monika staticpose = monika_extraplus

#===========================================================================================
# SCREEN
#===========================================================================================
#====Simply display the button in the loop
screen extraplus_button():
    zorder 15
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 50

        if renpy.get_screen("hkb_overlay"):
            if mas_hotkeys.talk_enabled:
                textbutton ("Extra+"):
                    action Jump("view_extraplus")
            elif mas_submod_utils.current_label == "mas_piano_setupstart":
                text ("")
            else:
                textbutton ("Extra+")

#====Submod options
screen submod_interactions():
    zorder 50
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 210

        textbutton ("Close") action [Hide("submod_interactions"), Jump("close_extraplus")]
        textbutton ("Date") action [Hide("submod_interactions"), Jump("plus_walk")]
        textbutton ("Minigame") action If(mas_affection._get_aff() >= 30, true=[Hide("submod_interactions"), Jump("plus_minigames")], false=None)
        textbutton ("Addition") action [Hide("submod_interactions"), Jump("plus_tools")]
        textbutton ("Boop") action If(mas_affection._get_aff() >= 30, true=[Hide("submod_interactions"), Jump("show_boop_screen")], false=None)

#====GAME
screen sticker_customization():
    zorder 50
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        textbutton ("Close") style "hkb_button" action [Hide("sticker_customization"), Jump("close_dev_extraplus")]
        textbutton ("Return") style "hkb_button" action [Hide("sticker_customization"), Jump("plus_tools")]
    frame:
        padding (50, 10, 0, 20)
        xpos 800
        yanchor 1.0
        ypos 660
        vbox:
            style_prefix "check"
            label _("Auto Position:")
            textbutton _("[persistent.enable_drag_chibika]") action ToggleField(persistent, "enable_drag_chibika")

            label _("Show permanently:")
            textbutton _("[persistent.hi_chibika]") action ToggleField(persistent, "hi_chibika")
            
            label _("Show/Hide:")
            textbutton _("Click here!") action Function(remove_show_chibika)
            
            if mas_affection._get_aff() >= 1000:
                label _("Alternative version:")
                textbutton _("Click here!") action Function(chibi_costume_change)

            label _("Sprite One:")
            hbox:
                style_prefix "music_menu"
                spacing 20
                textbutton _(" <") action SetField(persistent, "chibi_accessory_layer_1", max(persistent.chibi_accessory_layer_1 - 1, 0))
                text _(" [persistent.chibi_accessory_layer_1]")
                textbutton _(" >") action SetField(persistent, "chibi_accessory_layer_1", min(persistent.chibi_accessory_layer_1 + 1, len(chibi_sprites_0) - 1))

            label _("Sprite two:")
            hbox:
                style_prefix "music_menu"
                spacing 20
                textbutton _(" <") action SetField(persistent, "chibi_accessory_layer_2", max(persistent.chibi_accessory_layer_2 - 1, 0))
                text _(" [persistent.chibi_accessory_layer_2]")
                textbutton _(" >") action SetField(persistent, "chibi_accessory_layer_2", min(persistent.chibi_accessory_layer_2 + 1, len(chibi_sprites_1) - 1))

#====Boop
screen boop_revamped():
    zorder 50
    vbox:
        style_prefix "check"
        xpos 1000
        yanchor 1.0
        ypos 260
        label _("Interactions\navailable:")
        text _("Cheeks\n Head\n Nose\n Hears\n Hands\n") outlines [(2, "#808080", 0, 0)]

    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        textbutton ("Close") style "hkb_button" action [Hide("extra_gen_list"), Jump("close_boop_screen")]
        textbutton ("Return") style "hkb_button" action [Hide("extra_gen_list"), Jump("return_boop_screen")]

    #Head
    imagebutton idle "zonetwo":
        xpos 550 ypos 10
        action [Hide("submod_interactions"), Jump("monika_headpatbeta")] alternate [Hide("submod_interactions"), Jump("monika_headpat_long")]

    #Nose
    imagebutton idle "zoneone":
        xpos 618 ypos 235
        action [Hide("submod_interactions"), Jump("monika_boopbeta")] alternate [Hide("submod_interactions"), Jump("monika_boopbeta_war")]

    #Cheeks
    imagebutton idle "zonethree":
        xpos 675 ypos 256
        action [Hide("submod_interactions"), Jump("monika_cheeksbeta")]

    imagebutton idle "zonethree":
        xpos 570 ypos 256
        action [Hide("submod_interactions"), Jump("monika_cheeksbeta")]

    #Hands
    imagebutton idle "zonefour":
        xpos 600 ypos 327
        action [Hide("submod_interactions"), Jump("monika_handsbeta")]

    #Ears
    imagebutton idle "zoneone":
        xpos 754 ypos 195
        action [Hide("submod_interactions"), Jump("monika_earsbeta")]
    
    #Ear or Hair?
    imagebutton idle "zoneone":
        xpos 514  ypos 220
        action [Hide("submod_interactions"), Jump("monika_earsbeta")]

screen button_custom_zoom():
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
            textbutton ("Zoom") action If(store.disable_zoom_button, true = None, false = Show("extra_custom_zoom"))

screen extra_custom_zoom():
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
            action [SetField(store, "player_zoom", store.mas_sprites.zoom_level), Hide("extra_custom_zoom")]

        frame:
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
                    
                # actual slider for adjusting zoom
                bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                    style "mas_adjust_vbar"
                    xalign 0.5
                $ store.mas_sprites.adjust_zoom()

#====Will be displayed when the player selects a cup
screen shell_game_minigame():
    zorder 50
    style_prefix "hkb"
    use extra_no_click()
    
    for i in range(3):
        imagebutton:
            xanchor 0.5 yanchor 0.5
            xpos cup_coordinates[i]
            ypos 250
            idle "cup_idle"
            hover "cup_hover"
            focus_mask "cup_hover"
            action Verification(i, ball_position, "check_label")
    
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton ("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

#====Loop RPS
screen RPS_mg():
    zorder 50
    #Letter from Monika
    imagebutton idle "card_back":
        action NullAction()
        xalign 0.7
        yalign 0.1
    #Rock
    imagebutton idle "e_rock":
        hover "e_rock" at hover_card
        action [SetVariable("rps_your_choice", 1), Hide("RPS_mg"), Jump("rps_loop")]
        xalign 0.5
        yalign 0.7
    #Paper
    imagebutton idle "e_paper":
        hover "e_paper" at hover_card
        action [SetVariable("rps_your_choice", 2), Hide("RPS_mg"), Jump("rps_loop")]
        xalign 0.7
        yalign 0.7
    #Scissors
    imagebutton idle "e_scissors":
        hover "e_scissors" at hover_card
        action [SetVariable("rps_your_choice", 3), Hide("RPS_mg"), Jump("rps_loop")]
        xalign 0.9
        yalign 0.7

    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton ("Quit") style "hkb_button" action [Hide("RPS_mg"), Jump("rps_quit")]

#====Restrict the player from advancing in the conversation.
screen extra_no_click():
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()

    imagebutton:
        idle "mod_assets/other/transparent.png"
        action NullAction()

#====A small Easter egg
screen chibika_chill():
    zorder 60
    if renpy.get_screen("hkb_overlay"):
        drag:
            child "chibika_base"
            selected_hover_child "hover_sticker"
            dragged chibika_relax_drag
            if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
                xpos chibi_xpos ypos 350
            else:
                xpos chibi_xpos ypos chibi_ypos


#====Current minigame score
screen score_minigame(game=None):
    python:
        if game == "rps":
            first_text = "Monika"
            second_text = player
            first_score = store.moni_wins
            second_score = store.player_wins
            
        elif game == "sg":
            first_text = "Turn"
            second_text = "Good"
            first_score = store._current_turn
            second_score = store._correct_answers
        
    add "note_score"
    vbox:
        xpos 0.910
        ypos 0.025
        text "[first_text] : [first_score]"  size 25 style "monika_text"
        text "[second_text] : [second_score]"  size 25 style "monika_text"

#====Simple menu generator
screen extra_gen_list(extra_list, extra_area, others, close=None):
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
                    if isinstance(extra_list[0], tuple):
                        for i in extra_list:
                            textbutton i[0]:
                                xsize extra_area[2]
                                action [Hide("extra_gen_list"), Jump(i[1])]
                    else:
                        for m in extra_list:
                            textbutton m.name:
                                xsize extra_area[2]
                                action [Hide("extra_gen_list"), Function(m)]

            for items in others:
                if items[2] > 0:
                    null height items[2]

                textbutton _(items[0]):
                    xsize extra_area[2]
                    action [Hide("extra_gen_list"), Jump(items[1])]

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

    if close:
        vbox:
            xpos 0.097 ypos 50
            yanchor 1.0

            textbutton ("Close") style "hkb_button" action [Hide("extra_gen_list"), Jump("close_extraplus")]

#====Background loop
screen dating_loop(acs, acs_two, ask, finish, label_boop, boop_enable=None):
    if monika_chr.is_wearing_acs(acs) or monika_chr.is_wearing_acs(acs_two):
        pass
    else:
        timer 900.0 action [Hide("dating_loop"), Jump(finish)]

    zorder 50
    vbox:
        xpos 0.05 yanchor 1.0
        if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
            ypos 555
        else:
            ypos 595
        textbutton ("Talk") style "hkb_button" action [Hide("dating_loop"), Jump(ask)]

    #Noise
    if boop_enable == True:
        imagebutton:
            idle "zoneone"
            xpos 620 ypos 235
            action [Hide("dating_loop"), Jump(label_boop)]

#====Boop war?
screen boop_event(timelock, endlabel, editlabel):
    timer timelock action [Hide("boop_event"), Jump(endlabel)]
    zorder 50
    style_prefix "hkb"
    #Noise
    imagebutton:
        idle "zoneone"
        xpos 620 ypos 235
        action [Hide("boop_event"), Jump(editlabel)]
    if boop_war_count >= 25:
        #Head
        imagebutton idle "zonetwo":
            xpos 550 ypos 10
            action [Hide("boop_event"), Jump("headpat_dis")]
        #Cheeks
        imagebutton idle "zoneone":
            xpos 700 ypos 256
            action [Hide("boop_event"), Jump("cheeks_dis")]
        imagebutton idle "zoneone":
            xpos 550
            ypos 256
            action [Hide("boop_event"), Jump("cheeks_dis")]

    if boop_war_count >= 1:
        add "note_score"
        vbox:
            xpos 0.915
            ypos 0.040
            text "Boops : [boop_war_count]"  size 30 style "monika_text"

screen force_mouse_move():
    on "show":
        action MouseMove(x=412, y=237, duration=.3)
    timer .6 repeat True action MouseMove(x=412, y=237, duration=.3)

#===========================================================================================
# TRANSFORM
#===========================================================================================

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

#===========================================================================================
# BACKGROUNG
#===========================================================================================

#====Cafe====#

#Day images
image submod_background_cafe_day = "submods/ExtraPlus/submod_assets/backgrounds/cafe.png"
image submod_background_cafe_rain = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"
image submod_background_cafe_overcast = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"
image submod_background_cafe_snow = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"

#Night images
image submod_background_cafe_night = "submods/ExtraPlus/submod_assets/backgrounds/cafe-n.png"
image submod_background_cafe_rain_night = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"
image submod_background_cafe_overcast_night = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"
image submod_background_cafe_snow_night = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"

#Sunset images
image submod_background_cafe_ss = "submods/ExtraPlus/submod_assets/backgrounds/cafe-ss.png"
image submod_background_cafe_rain_ss = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"
image submod_background_cafe_overcast_ss = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"
image submod_background_cafe_snow_ss = "submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"

init -1 python:
    submod_background_cafe = MASFilterableBackground(
        "submod_background_cafe",
        "Cafe (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_cafe_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_cafe_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_cafe_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_cafe_snow_ss",
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
        entry_pp=store.mas_background._cafe_entry,
        exit_pp=store.mas_background._cafe_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _cafe_entry(_old, **kwargs):
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

        store.monika_chr.tablechair.table = "submod_cafe"
        store.monika_chr.tablechair.chair = "submod_cafe"

    def _cafe_exit(_new, **kwargs):
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

#====Restaurant====#

#Day images
image submod_background_extraplusr_restaurant_day = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant.png"
image submod_background_extraplusr_restaurant_rain = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain.png"
image submod_background_extraplusr_restaurant_overcast = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain.png"
image submod_background_extraplusr_restaurant_snow = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain.png"

#Night images
image submod_background_extraplusr_restaurant_night = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant-n.png"
image submod_background_extraplusr_restaurant_rain_night = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-n.png"
image submod_background_extraplusr_restaurant_overcast_night = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-n.png"
image submod_background_extraplusr_restaurant_snow_night = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-n.png"

#Sunset images
image submod_background_extraplusr_restaurant_ss = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant-ss.png"
image submod_background_extraplusr_restaurant_rain_ss = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-ss.png"
image submod_background_extraplusr_restaurant_overcast_ss = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-ss.png"
image submod_background_extraplusr_restaurant_snow_ss = "Submods/ExtraPlus/submod_assets/backgrounds/extraplusr_restaurant_rain-ss.png"

init -1 python:
    submod_background_restaurant = MASFilterableBackground(
        "submod_background_restaurant",
        "Restaurant (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplusr_restaurant_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplusr_restaurant_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplusr_restaurant_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplusr_restaurant_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplusr_restaurant_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplusr_restaurant_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplusr_restaurant_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplusr_restaurant_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_extraplusr_restaurant_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_extraplusr_restaurant_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_extraplusr_restaurant_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_extraplusr_restaurant_snow_ss",
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
        entry_pp=store.mas_background._restaurant_entry,
        exit_pp=store.mas_background._restaurant_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _restaurant_entry(_old, **kwargs):
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

        store.monika_chr.tablechair.table = "submod_restaurant"
        store.monika_chr.tablechair.chair = "submod_restaurant"


    def _restaurant_exit(_new, **kwargs):
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
