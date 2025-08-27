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
        version="1.3.1"
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
default persistent.chibika_current_costume = blanket_monika
default persistent.current_sticker_dokis = blanket_monika

define -1 blanket_monika = ["sticker_up", "sticker_sleep", "sticker_baka"]
define -1 blanket_nat = ["nat_up", "nat_sleep", "nat_baka"]
define -1 blanket_sayo = ["sayo_up", "sayo_sleep", "sayo_baka"]
define -1 blanket_yuri = ["yuri_up", "yuri_sleep", "yuri_baka"]
define -1 android_chibi = ["android_sticker", "android_sticker_blink", "android_sticker_cat"]
define -1 casual_chibi = ["casual_sticker", "casual_sticker_blink", "casual_sticker_happy"]
define -1 bikini_chibi = ["bikini_sticker", "bikini_sticker_blink", "bikini_sticker_happy"]

default monika_costumes_ = [("Blanket", blanket_monika), ("Android", android_chibi), ("Casual", casual_chibi)]
default natsuki_costumes_ = [("Blanket", blanket_nat)]
default sayori_costumes_ = [("Blanket", blanket_sayo)]
default yuri_costumes_ = [("Blanket", blanket_yuri)]

define -1 chibi_sprites_0 = []
define -1 chibi_sprites_1 = []
default -1 persistent.chibi_accessory_1_ = "0nothing"
default -1 persistent.chibi_accessory_2_ = "0nothing"
default -1 persistent.hi_chibika = False
default -1 persistent.enable_drag_chibika = False

#====ExtraPlus Buttons
define minigames_menu = []
define tools_menu = []
define walk_menu = []

#====Misc
default stop_snike_time = False
default Minigame_TTT = [
    "'",
    "#0142a4",
    "0",
    "#a80000"
]
define -1 Pictograms_font = "Submods/ExtraPlus/submod_assets/Pictograms.ttf"
default plus_snack_time = None
default moldable_variable = None
define 3 extra_plus_file = os.path.join(renpy.config.basedir, "game", "Submods", "ExtraPlus", "Extra_Plus_Main.rpy")

#====BG
define extra_old_bg = None
define extra_chair = None
define extra_table = None

#====ZOOM
define player_zoom = None
default disable_zoom_button = None

#====Windows Title
define backup_window_title = "Monika After Story   "
default persistent._save_window_title = "Monika After Story   "

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
    import time
    last_affection_notify_time = 0

    def make_bday_oki_doki():
        filepath = os.path.join(renpy.config.basedir, 'characters', 'oki doki')
        with open(filepath, "a"):
            pass  # just create an empty file
        config.overlay_screens.remove("bday_oki_doki")
        renpy.hide_screen("bday_oki_doki")

    def show_bday_screen():
        if mas_isMonikaBirthday():
            config.overlay_screens.append("bday_oki_doki")

    def notify_affection():
        global last_affection_notify_time
        current_time = time.time()
        if current_time - last_affection_notify_time >= 10:
            last_affection_notify_time = current_time
            renpy.notify("{1} {0:,.2f} {1}".format(mas_affection._get_aff(), get_monika_level()))

    def show_costume_menu(costumes, return_label):
        dokis_items = [SelectDOKI(name, cost) for name, cost in costumes]
        items = [(_("Nevermind"), return_label, 20)]
        renpy.call_screen("extra_gen_list", dokis_items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)

    def get_monika_level():
        affection = mas_affection._get_aff()
        if affection >= 400:
            icon = "8"
        elif affection >= 100:
            icon = "7"
        elif affection <= -30:
            icon = "!"
        else:
            icon = "&"
        formatted_icon = (
            "{size=+4}{color=#FFFFFF}{font=Submods/ExtraPlus/submod_assets/Pictograms.ttf}" + icon + "{/font}{/color}{/size}"
        )
        return formatted_icon

    def plus_files_exist():
        return os.path.isfile(os.path.normcase(extra_plus_file))

    #====Return a string that represents the gender of the player.
    def plus_player_gender():
        if persistent.gender == "M":
            return "boyfriend"
        elif persistent.gender == "F":
            return "girlfriend"
        else:
            return "beloved"

    #====RNG
    def rng_cup():
        if store.persistent._mas_pm_cares_about_dokis:
            store.cup_skin = renpy.random.choice(cup_list)
        elif not store.persistent._mas_pm_cares_about_dokis:
            store.cup_skin = renpy.random.choice(["cup.png", "cup_monika.png"])

    #====Save the name
    def save_title_windows():
        special_days = {
            mas_isplayer_bday: " Happy birthday, " + player + "!",
            mas_isNYD: " Happy New Year, " + player + "!",
            mas_isF14: " Happy Valentine's Day, " + player + "!",
            mas_isA01: " I know what you do, " + player + "~",
            mas_isMonikaBirthday: " Happy Birthday, " + persistent._mas_monika_nickname + "!",
            mas_isO31: " Happy Halloween, " + player + "!",
            mas_isD25Eve: " Merry Christmas Eve, " + player + "!",
            mas_isD25: " Merry Christmas, " + player + "!",
            mas_isNYE: " Happy New Year's Eve, " + player + "!",
        }

        for date_check, title in special_days.items():
            if date_check():
                config.window_title = title
                return

        config.window_title = persistent._save_window_title

    #====Functions for submod operation
    def Extraplus_show():
        store.player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        extra_button_zoom()
        renpy.invoke_in_new_context(renpy.call_screen, "submod_interactions")

    def ExtraButton():
        if not ExtraVisible():
            config.overlay_screens.append("extraplus_button")

    def ExtraVisible():
        return "extraplus_button" in config.overlay_screens
    
    #====Chibika
    def init_chibi():
        if store.persistent.hi_chibika == True:
            config.overlay_screens.append("doki_chibi_idle")
    
    def change_dokis(skin):
        persistent.chibika_current_costume = skin
        reset_chibi()
        renpy.jump("extra_dev_mode")

    def visible_chibi():
        return "doki_chibi_idle" in config.overlay_screens
        
    def remove_chibi():
        if visible_chibi():
            config.overlay_screens.remove("doki_chibi_idle")
            renpy.hide_screen("doki_chibi_idle")

    def add_remv_chibi():
        if not renpy.get_screen("doki_chibi_idle"):
            config.overlay_screens.append("doki_chibi_idle")
        elif renpy.get_screen("doki_chibi_idle"):
            config.overlay_screens.remove("doki_chibi_idle")
            renpy.hide_screen("doki_chibi_idle")

    def chibi_drag(drags, drop):
        if not drop and store.persistent.enable_drag_chibika:
            drags[0].snap(chibi_xpos, chibika_y_position, 0.7)

    def add_chibi():
        if not visible_chibi():
            config.overlay_screens.append("doki_chibi_idle")

    def reset_chibi():
        remove_chibi()
        if not visible_chibi():
            config.overlay_screens.append("doki_chibi_idle")

    def chibi_draw_sprites(st, at):
        objects = LiveComposite(
            (119, 188),
            (0, 0), MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/accessories/0/{}.png".format(persistent.chibi_accessory_1_)),
            (0, 0), MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/accessories/1/{}.png".format(persistent.chibi_accessory_2_))
            )
            
        return objects, 0.1

    def plus_actual_doki(st, at):
        objects = LiveComposite(
            (119, 188),
            (0, 0), MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/{}.png".format(persistent.chibika_current_costume[2]))
            )
        return objects, 0.1

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
        if store.mas_affection._get_aff() < 300:
            renpy.jump(sorry)

        if renpy.seen_label(view_label):
            store.mas_gainAffection(1,bypass=True)
            renpy.jump(extra_label)

        else:
            store.mas_gainAffection(5,bypass=True)
            
    def extra_seen_label(extra_label, view_label):
        if renpy.seen_label(view_label):
            renpy.jump(extra_label)

    ExtraButton()
    rng_cup()
    save_title_windows()
    show_bday_screen()
    
init 999 python:
    if plus_files_exist():
        init_chibi()
    else:
        remove_chibi()

# init -1 python:
#     chibika_y_position = 345 if store.mas_submod_utils.isSubmodInstalled("Noises Submod") else 385
#     dating_ypos_value = 555 if store.mas_submod_utils.isSubmodInstalled("Noises Submod") else 595
    # if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
    #     chibika_y_position = 345
    # else:
    #     chibika_y_position = chibi_ypos

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
            file_path = os.path.join(renpy.config.basedir, 'characters', self.gift)
            with open(file_path, 'a') as f:
                messages = [
                    _("Oh! You got me a {}! Thank you!").format(self.name),
                    _("A {}? For me? You're so sweet!").format(self.name),
                    _("Wow! Is this a {}? I love it!").format(self.name),
                    _("You shouldn't have! But I'm so happy you gave me a {}!").format(self.name),
                    _("Eee! A {}! You're the best!").format(self.name)
                ]
                renpy.notify(random.choice(messages))
            renpy.jump('plus_make_gift')

    class DokiAccessory():
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
        def __init__(self, name, costume):
            self.name = name
            self.costume = costume

        def __call__(self):
            persistent.chibika_current_costume = self.costume
            reset_chibi()
            renpy.jump("extra_dev_mode")

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
image note_score = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/note_score.png")

#====TTT
image notebook = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/notebook.png")
image line_black = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/line.png")
image line_player = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/line_player.png")
image line_moni = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/line_moni.png")
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
image e_paper = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/paper.png")
image e_rock = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/rock.png")
image e_scissors = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/scissors.png")
image card_back = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/card_back.png")

#====SG
image extra_cup = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/{}".format(cup_skin))
image extra_cup_hover = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/cup_hover.png")
image extra_cup_idle = im.Scale("mod_assets/other/transparent.png", 200, 260)
image extra_ball = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/ball.png")
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
image chibi_blink_effect:
    block:
        MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/{}.png".format(persistent.chibika_current_costume[0]))
        block:
            choice:
                3
            choice:
                5
            choice:
                7
        MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/{}.png".format(persistent.chibika_current_costume[1]))
        choice 0.02:
            block:
                choice:
                    8
                choice:
                    6
                choice:
                    4
                MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/{}.png".format(persistent.chibika_current_costume[0]))
        choice 0.098:
            pass
        0.06
        repeat

image chibika_base = LiveComposite(
    (119, 188),
    (0, 40), "chibi_blink_effect",
    (0, 0), DynamicDisplayable(chibi_draw_sprites)
    )

image hover_sticker = LiveComposite(
    (119, 188), 
    (0, 40), DynamicDisplayable(plus_actual_doki),
    (0, 0), DynamicDisplayable(chibi_draw_sprites)
    )
#====Coin
image coin_heads = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/coin_heads.png")
image coin_tails = MASFilterSwitch("Submods/ExtraPlus/submod_assets/sprites/coin_tails.png")
image sprite_coin = anim.Filmstrip("Submods/ExtraPlus/submod_assets/sprites/sprite_coin.png", (100, 100), (3, 2), .125, loop=True)
image sprite_coin_n = anim.Filmstrip("Submods/ExtraPlus/submod_assets/sprites/sprite_coin-n.png", (100, 100), (3, 2), .125, loop=True)
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

        $ buttons_text = _("Extra+")
        if renpy.get_screen("hkb_overlay"):
            if mas_hotkeys.talk_enabled:
                key "a" action Function(notify_affection)
                key "x" action Function(Extraplus_show)
                textbutton buttons_text action Function(Extraplus_show)
            elif mas_submod_utils.current_label == "mas_piano_setupstart":
                text _("")
            else:
                textbutton buttons_text

#====Submod options
screen submod_interactions():
    zorder 50
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 210

        textbutton _("Close") action [Hide("submod_interactions"), Jump("close_extraplus")]
        textbutton _("Date") action [Hide("submod_interactions"), Jump("plus_walk")]
        textbutton _("Minigame") action If(mas_affection._get_aff() >= 30, true=[Hide("submod_interactions"), Jump("plus_minigames")], false=None)
        textbutton _("Addition") action [Hide("submod_interactions"), Jump("plus_tools")]
        textbutton _("Boop") action If(mas_affection._get_aff() >= 30, true=[Hide("submod_interactions"), Jump("show_boop_screen")], false=None)

#====GAME
screen sticker_customization():
    zorder 50
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        textbutton _("Close") style "hkb_button" action [Hide("sticker_customization"), Jump("close_dev_extraplus")]
        textbutton _("Return") style "hkb_button" action [Hide("sticker_customization"), Jump("plus_tools")]
    frame:
        padding (50, 10, 20, 20)
        xpos 800
        yanchor 1.0
        ypos 660
        vbox:
            xalign 0.5 
            style_prefix "check"
            label _("Auto Position:")
            textbutton _("[persistent.enable_drag_chibika]") action ToggleField(persistent, "enable_drag_chibika")

            label _("Show permanently:")
            textbutton _("[persistent.hi_chibika]") action ToggleField(persistent, "hi_chibika")
            
            label _("Show / Hide:")
            textbutton _("Click here!") action Function(add_remv_chibi)

            label _("Clothing:")
            textbutton _("Hey!") action [Hide("sticker_customization"), Jump("doki_change_appe")]

            label _("Body Accessories:")
            textbutton _("Choice!") action [Hide("sticker_customization"), Jump("sticker_primary")]

            label _("Others Accessories:")
            textbutton _("Choice again!") action [Hide("sticker_customization"), Jump("sticker_secondary")]

#====Boop
screen boop_revamped():
    zorder 50

    # Sección de Interacciones Disponibles
    vbox:
        style_prefix "check"
        yanchor 0.5
        xanchor 1.0
        xpos 1.0
        ypos 0.5
        label _("Interactions\navailable:")
        text _("Cheeks\n Head\n Nose\n Ears\n Hands\n") outlines [(2, "#808080", 0, 0)]

    # Botones de Cierre y Retorno
    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90
        textbutton _("Close") action [Hide("extra_gen_list"), Jump("close_boop_screen")]
        textbutton _("Return") action [Hide("extra_gen_list"), Jump("return_boop_screen")]

    # Definición de zonas interactivas con coordenadas
    default zones = [
        ("zonetwo", 550, 10, "monika_headpatbeta", "monika_headpat_long"),  # Head
        ("zoneone", 618, 235, "monika_boopbeta", "monika_boopbeta_war"),  # Nose
        ("zonethree", 675, 256, "monika_cheeksbeta", None),  # Right Cheek
        ("zonethree", 570, 256, "monika_cheeksbeta", None),  # Left Cheek
        ("zonefour", 600, 327, "monika_handsbeta", None),  # Hands
        ("zoneone", 754, 195, "monika_earsbeta", None),  # Right Ear
        ("zoneone", 514, 220, "monika_earsbeta", None)   # Left Ear / Hair
    ]

    # Generar botones de imagen dinámicamente
    for zone, xpos, ypos, primary_action, alt_action in zones:
        imagebutton idle zone xpos xpos ypos ypos action [Hide("submod_interactions"), Jump(primary_action)]
        if alt_action:
            imagebutton idle zone xpos xpos ypos ypos alternate [Hide("submod_interactions"), Jump(alt_action)]

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
            textbutton _("Zoom") action If(store.disable_zoom_button, true = None, false = Show("extra_custom_zoom"))

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
        textbutton _("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

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
        textbutton _("Quit") style "hkb_button" action [Hide("RPS_mg"), Jump("rps_quit")]

#====Restrict the player from advancing in the conversation.
screen extra_no_click():
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()

    imagebutton:
        idle "mod_assets/other/transparent.png"
        action NullAction()

#====Chibika
screen doki_chibi_idle():
    zorder 75
    if renpy.get_screen("hkb_overlay"):
        drag:
            child "chibika_base"
            selected_hover_child "hover_sticker"
            dragged chibi_drag
            ypos chibika_y_position
            xpos chibi_xpos

#====Current minigame score
screen score_minigame(game=None):
    key "h" action NullAction()
    key "mouseup_3" action NullAction()
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
                    # Itera directamente sobre extra_list (si está vacía, no se ejecuta)
                    for item in extra_list:
                        # Calcula texto y acción según la estructura del elemento.
                        $ btn_text = item[0] if isinstance(item, tuple) else item.name
                        $ btn_action = Jump(item[1]) if isinstance(item, tuple) else Function(item)
                        textbutton _(btn_text):
                            xsize extra_area[2]
                            action btn_action

            # Procesa la lista "others"
            for entry in others:
                # Determinar el valor de espaciado según la estructura
                $ spacing_val = entry[1] if len(entry) == 2 else entry[2]
                if spacing_val > 0:
                    null height spacing_val

                # Define el texto y la acción basados en si el primer elemento tiene atributo "name"
                $ btn_text = entry[0].name if hasattr(entry[0], "name") else entry[0]
                $ btn_action = [Hide("extra_gen_list"), Function(entry[0])] if hasattr(entry[0], "name") else [Hide("extra_gen_list"), Jump(entry[1])]
                textbutton _(btn_text):
                    xsize extra_area[2]
                    action btn_action

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

    if close:
        vbox:
            xpos 0.097 ypos 50
            yanchor 1.0
            textbutton _("Close") style "hkb_button" action [Hide("extra_gen_list"), Jump("close_extraplus")]

#====Background loop
screen dating_loop(ask, label_boop, boop_enable=None):
    zorder 50
    # $ dating_ypos_value = 555 if store.mas_submod_utils.isSubmodInstalled("Noises Submod") else 595
    vbox:
        xpos 0.05 yanchor 1.0
        ypos dating_ypos_value
        textbutton _("Talk") style "hkb_button" action [Hide("dating_loop"), Jump(ask)]

    #Noise
    if boop_enable == True:
        imagebutton:
            idle "zoneone"
            xpos 620 ypos 235
            action [Hide("dating_loop"), Jump(label_boop)]

screen _timer_monika(time):
    timer time action SetVariable("stop_snike_time", True)


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
            text _("Boops : [boop_war_count]") size 30 style "monika_text"

screen force_mouse_move():
    on "show":
        action MouseMove(x=412, y=237, duration=.3)
    timer .6 repeat True action MouseMove(x=412, y=237, duration=.3)

screen bday_oki_doki():
    zorder 15
    style_prefix "hkb"
    vbox:
        xpos 590
        ypos 0.9
        if mas_submod_utils.current_label == "mas_dockstat_empty_desk_from_empty":
            textbutton _("Oki Doki") action Function(make_bday_oki_doki)

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

transform pool_float(x=640, z=0.80, y=25, t=3.2):
    on show:
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        ease t yoffset y
        ease t yoffset 0
        repeat
    on replace:
        ease t yoffset y
        ease t yoffset 0
        repeat

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

#====Cafe====#

#Day images
image submod_background_cafe_day = "Submods/ExtraPlus/submod_assets/backgrounds/cafe.png"
image submod_background_cafe_rain = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"
image submod_background_cafe_overcast = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"
image submod_background_cafe_snow = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain.png"

#Night images
image submod_background_cafe_night = "Submods/ExtraPlus/submod_assets/backgrounds/cafe-n.png"
image submod_background_cafe_rain_night = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"
image submod_background_cafe_overcast_night = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"
image submod_background_cafe_snow_night = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-n.png"

#Sunset images
image submod_background_cafe_ss = "Submods/ExtraPlus/submod_assets/backgrounds/cafe-ss.png"
image submod_background_cafe_rain_ss = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"
image submod_background_cafe_overcast_ss = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"
image submod_background_cafe_snow_ss = "Submods/ExtraPlus/submod_assets/backgrounds/cafe_rain-ss.png"

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

#====Pool====#

#Day images
image submod_background_pool_day = "Submods/ExtraPlus/submod_assets/backgrounds/pool.png"
image submod_background_pool_rain = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain.png"
image submod_background_pool_overcast = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain.png"
image submod_background_pool_snow = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain.png"

#Night images
image submod_background_pool_night = "Submods/ExtraPlus/submod_assets/backgrounds/pool-n.png"
image submod_background_pool_rain_night = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-n.png"
image submod_background_pool_overcast_night = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-n.png"
image submod_background_pool_snow_night = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-n.png"

#Sunset images
image submod_background_pool_ss = "Submods/ExtraPlus/submod_assets/backgrounds/pool-ss.png"
image submod_background_pool_rain_ss = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-ss.png"
image submod_background_pool_overcast_ss = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-ss.png"
image submod_background_pool_snow_ss = "Submods/ExtraPlus/submod_assets/backgrounds/pool_rain-ss.png"

init -1 python:
    submod_background_pool = MASFilterableBackground(
        "submod_background_pool",
        "Pool (Extra+)",

        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_pool_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_pool_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_pool_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_pool_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_pool_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_pool_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_pool_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_pool_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_pool_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_pool_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_pool_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_pool_snow_ss",
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
        entry_pp=store.mas_background._pool_entry,
        exit_pp=store.mas_background._pool_exit,
        ex_props={"skip_outro": None}
    )

init -2 python in mas_background:
    def _pool_entry(_old, **kwargs):
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

        store.monika_chr.tablechair.table = "submod_pool"
        store.monika_chr.tablechair.chair = "submod_pool"

    def _pool_exit(_new, **kwargs):
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