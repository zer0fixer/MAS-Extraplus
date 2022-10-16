#===========================================================================================
# SUBMOD
#===========================================================================================

#Submod created by ZeroFixer(u/UnderstandingAny7135), this submod is made for MAS brothers/sisters.
#Shoutout to u/my-otter-self at reddit, who proofread the whole mod.

#====Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="ZeroFixer",
        name="Extra Plus",
        description="A submod that adds an Extra+ button, as well as adding more content!\nOne location has been added, the restaurant!",
        version="1.0.4",
        version_updates={}
    )

#====Register the updater
init -990 python:
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
default monika_talk = ""
define minigames_talk = [
    "Choose one, [player].",
    "Want a new challenge?",
    "I would love to play with you~",
    "What will we play today?"
    ]
define date_talk = [
    "Where will you take me today?",
    "Where do you want to go?",
    "Where will we go?",
    "Any location in mind?"
    ]

#====Boop count
default persistent.plus_boop = [0, 0, 0]
default boop_war_count = 0

#====Pos
define chibi_xpos = 0.05
define chibi_ypos = 425
define chibika_sprite = ["sticker_baka.png","sticker_sleep.png","sticker_up.png"]
#====Misc
default extra_current_affection = _mas_getAffection()
define extra_old_bg = None
define extra_chair = None
define extra_table = None
define player_zoom = None
define minigames_menu = []
define tools_menu = []
define walk_menu = []
define rng_global = None
define backup_window_title = "Monika After Story   "
default persistent.save_window_title = None
default disable_zoom_button = None
define extra_error_messages = renpy.random.choice(["Hey, be more careful about adding submods.","The files are not available...","I think you forgot to place the submod files, ahaha~","You do have problems around here."])

#====Minigames variables
#====Cup coordinates
define cup_coordinates = [695, 925, 1155]
define cup_coordinates_real = [695, 925, 1155]
#====Skin, It will depend on your concern for the other dokis, if you don't care about them at all, only the first two skins will come out.
define cup_list = ["cup.png", "cup_monika.png", "cup_yuri.png", "cup_natsuki.png", "cup_sayori.png"]

#====PSR
default player_wins = 0
default moni_wins = 0

#====SG
define original_cup = [0, 1, 2]
define ball_position = 1
default current_turn = 0
default shuffle_cups = 0
default comment = False
define your_choice = 0
define correct_answers = 0
define cup_speed = 0.5
define difficulty_sg = None

#====Comments by moni on standard difficulties
define comments_good = ""
define comments_bad = ""
define complies = [
    "Great.",
    "Keep it up, [player]!",
    "Good.",
    "Amazing, [player]!"
    ]
define not_met = [
    "Oh, too bad~",
    "It's not that, [player].",
    "Try again~",
    "Don't get distracted, [player]."
    ]

init 10 python:
    #====Choose a random cup
    if store.persistent._mas_pm_cares_about_dokis:
        cup_skin = renpy.random.choice(cup_list)
    elif not store.persistent._mas_pm_cares_about_dokis:
        cup_skin = renpy.random.choice(["cup.png", "cup_monika.png"])

    #====Save the name
    config.window_title = persistent.save_window_title

    #====Date
    walk_menu = [
        ("Cafe", 'go_to_cafe'),
        ("Restaurant", 'go_to_restaurant')
        ]

    #====Minigamnes
    minigames_menu = [
        minigames("Shell Game", 'minigame_sg', None),
        minigames("Rock Paper Scissors", 'minigame_psr', None)
        ]

    #====Adds
    tools_menu = [
        ("View [m_name]'s Affection", 'aff_log'),
        ("Create a gift for [m_name]", 'make_gift'),
        ("Change the window's title", 'extra_window_title'),
        ("[m_name], I want to make a backup", 'mas_backup'),
        ("[m_name], can you flip a coin?", 'coinflipbeta'),
        ("Github Repository", 'github_submod')
    ]

init python:
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

init python:
    #====It checks if the files of a minigame or background exist.
    def validate_files(sprite, type=None):
        extra_files = []
        extra_sprites = sprite
        if type:
            file_list = os.listdir(renpy.config.basedir + '/game/submods/ExtraPlus/submod_assets/sprites')
        else:
            file_list = os.listdir(renpy.config.basedir + '/game/submods/ExtraPlus/submod_assets/backgrounds')
        for i in extra_sprites:
            if i in file_list:
                extra_files.append(i)
        if set(extra_files) == set(extra_sprites):
            pass
        elif not set(extra_files) == set(extra_sprites):
            renpy.show("monika idle", at_list=[t11])
            renpy.call_screen("dialog", message="[extra_error_messages]", ok_action=Jump("close_extraplus"))

    #====Function for the creation of a gift
    def gift_append(plus_name, plus_gift):
        global extra_name
        extra_name = plus_name
        filepath = os.path.join(renpy.config.basedir + '/characters',plus_gift)
        f = open(filepath,"a")
        renpy.notify("The [extra_name] File has been successfully created.")
        renpy.jump("make_gift")

    #====Functions for submod operation
    def Extraplus_show():
        if renpy.random.randint(1,40) == 1:
            show_chibika_chill()
        renpy.call_screen("submod_interactions")

    def ExtraButton():
        if not ExtraVisible():
            config.overlay_screens.append("extraplus_button")

    def ExtraVisible():
        return "extraplus_button" in config.overlay_screens
    
    #====The representation of the devs?
    def show_chibika_chill():
        if not visible_chibika_chill():
            config.overlay_screens.append("chibika_chill")

    def visible_chibika_chill():
        return "chibika_chill" in config.overlay_screens
        
    def disable_chibika_chill():
        if visible_chibika_chill():
            config.overlay_screens.remove("chibika_chill")
            renpy.hide_screen("chibika_chill")

    def chibika_relax_drag(drags, drop):
        if not drop:
            if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
                drags[0].snap(chibi_xpos, 390, 0.7)
            else:
                drags[0].snap(chibi_xpos, chibi_ypos, 0.7)
            return
        return True

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

    #====Saves the current room
    def mas_extra_location(locate=None):
        #====SAVE
        if locate == True:
            store.extra_chair = store.monika_chr.tablechair.chair
            store.extra_table = store.monika_chr.tablechair.table
            store.extra_old_bg = store.mas_current_background

        #====LOAD
        else:
            store.monika_chr.tablechair.chair = store.extra_chair
            store.monika_chr.tablechair.table = store.extra_table
            store.mas_current_background = store.extra_old_bg

    def extra_seen_label(sorry, extra_label, view_label):
        if store.extra_current_affection < 399:
            renpy.jump(sorry)

        if renpy.seen_label(view_label):
            store.mas_gainAffection(1,bypass=True)
            renpy.jump(extra_label)
        else:
            store.mas_gainAffection(5,bypass=True)
            pass
            
    #====Extraplus button
    ExtraButton()

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
                global your_choice
                your_choice = self.index

            if self.index == self.check_index:
                global comments_good
                comments_good = renpy.substitute(renpy.random.choice(complies))
                if self.final_label == "check_label":
                    global correct_answers
                    global comment
                    correct_answers += 1
                    comment = True
                renpy.jump(self.final_label)
            else:
                global comments_bad
                global comment
                comment = False
                comments_bad = renpy.substitute(renpy.random.choice(not_met))
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
        def __init__(self, name, gift, preparation = None):
            self.name = name
            self.gift = gift
            self.preparation = preparation

        def __call__(self, *args, **kwargs):
            if self.preparation:
                self.preparation(self.name, self.gift)
                if not self.name or self.gift:
                    renpy.notify("Ehehe~")
                    renpy.jump("close_extraplus")

#===========================================================================================
# IMAGES
#===========================================================================================

init python:
    #====Cafe====#
    #====Desserts and objects

    extraplus_acs_chocolatecake = MASAccessory(
        "chocolatecake",
        "chocolatecake",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_chocolatecake)

    extraplus_acs_fruitcake = MASAccessory(
        "fruitcake",
        "fruitcake",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_fruitcake)

    extraplus_acs_emptyplate = MASAccessory(
        "emptyplate",
        "emptyplate",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_emptyplate)

    extraplus_acs_coffeecup = MASAccessory(
        "coffeecup",
        "coffeecup",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_coffeecup)

    extraplus_acs_emptycup = MASAccessory(
        "emptycup",
        "emptycup",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_emptycup)

    #====Restaurant====#

    extraplus_acs_pasta = MASAccessory(
        "extraplus_spaghetti",
        "extraplus_spaghetti",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_pasta)

    extraplus_acs_pancakes = MASAccessory(
        "extraplus_pancakes",
        "extraplus_pancakes",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_pancakes)

    extraplus_acs_candles = MASAccessory(
        "extraplus_candles",
        "extraplus_candles",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_candles)

    extraplus_acs_icecream = MASAccessory(
        "extraplus_icecream",
        "extraplus_icecream",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_icecream)

    extraplus_acs_pudding = MASAccessory(
        "extraplus_lecheflanpudding",
        "extraplus_lecheflanpudding",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_pudding)   

    extraplus_acs_waffles = MASAccessory(
        "extraplus_waffles",
        "extraplus_waffles",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_waffles) 

    extraplus_acs_flowers = MASAccessory(
        "extraplus_flowers",
        "extraplus_flowers",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True,
        rec_layer=2
    )
    store.mas_sprites.init_acs(extraplus_acs_flowers)
    
    extraplus_acs_remptyplate = MASAccessory(
        "extraplus_remptyplate",
        "extraplus_remptyplate",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(extraplus_acs_remptyplate)    

#====Minigames images
image note_score = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/note_score.png")

#====TTT
image notebook = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/notebook.png")
image line_black = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line.png")
image line_player = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line_player.png")
image line_moni = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/line_moni.png")
image ttt_cross:
    Text("'", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 180, color = "#51a8ff", outlines = [])
    on show:
        alpha 0.5
        linear 0.25 alpha 1.0
image ttt_cross_cursor:
    Text("'", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 180, color = "#2e97ff", outlines = [])
    alpha 0.25
    truecenter
image ttt_circle:
    Text("0", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 180, color = "#ff5c5c", outlines = [])
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
        
#====PSR
image e_paper = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/paper.png")
image e_rock = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/rock.png")
image e_scissors = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/scissors.png")
image card_back = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/card_back.png")

#====SG
image extra_cup = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/[cup_skin]")
image extra_cup_hover = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/cup_hover.png")
image extra_cup_idle = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/cup_idle.png")
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
image sticker_baka = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/sticker_baka.png")
image sticker_sleep = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/sticker_sleep.png")
image sticker_up = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/sticker_up.png")
image sticker_eyes:
    "sticker_up"
    choice:
        4.5
    choice:
        3.5
    choice:
        "sticker_sleep"
        2.5
    choice:
        1.5
    choice:
        0.5
    "sticker_sleep"
    .25
    repeat

#====Coin
image coin_heads = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/coin_heads.png")
image coin_tails = MASFilterSwitch("submods/ExtraPlus/submod_assets/sprites/coin_tails.png")
image coin_flip = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin.png", (100, 100), (3, 2), .125, loop=True)
image coin_flip_n = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin-n.png", (100, 100), (3, 2), .125, loop=True)
image coin_moni:
    ConditionSwitch(
        "mas_isDayNow()", "coin_flip",
        "mas_isNightNow()", "coin_flip_n")

#====Boop
image zoneone = im.Scale("mod_assets/other/transparent.png", 30, 30)
image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)
image zonethree = im.Scale("mod_assets/other/transparent.png", 40, 40)

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
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    text Null()
                else:
                    textbutton ("Extra+")
            elif store.extra_current_affection < 29:
                textbutton ("Extra+")
            else:
                textbutton ("Extra+") action Jump("view_extraplus")

#====Submod options
screen submod_interactions():
    zorder 50
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 210

        textbutton ("Close") action [Hide("submod_interactions"), Jump("close_extraplus")]

        textbutton ("Go to") action [Hide("submod_interactions"), Jump("walk_extra")] 

        textbutton ("Minigame") action [Hide("submod_interactions"), Jump("minigames_extra")]

        textbutton ("Addition") action [Hide("submod_interactions"), Jump("tools_extra")]

        textbutton ("Boop") action [Hide("submod_interactions"), Jump("show_boop_screen")]

#====Boop
screen boop_revamped():
    zorder 50
    vbox:
        style_prefix "check"
        xpos 1000
        yanchor 1.0
        ypos 120
        label _("Interactions\navailable:")
        text _("Cheeks, Head, Nose") outlines [(2, "#808080", 0, 0)]

    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 90

        textbutton ("Close") style "hkb_button" action [Hide("list_scrolling"), Jump("close_boop_screen")]
        textbutton ("Return") style "hkb_button" action [Hide("list_scrolling"), Jump("return_boop_screen")]

    #Head
    imagebutton:
        idle "zonetwo"
        xpos 550
        ypos 10
        action [Hide("submod_interactions"), Jump("monika_headpatbeta")]
        alternate [Hide("submod_interactions"), Jump("monika_headpat_long")]

    #Nose
    imagebutton:
        idle "zoneone"
        xpos 618
        ypos 235
        action [Hide("submod_interactions"), Jump("monika_boopbeta")]
        alternate [Hide("submod_interactions"), Jump("monika_boopbeta_war")]

    #Cheeks
    imagebutton:
        idle "zonethree"
        xpos 675
        ypos 256
        action [Hide("submod_interactions"), Jump("monika_cheeksbeta")]
        alternate [Hide("submod_interactions"), Jump("monika_cheeks_long")]
    imagebutton:
        idle "zonethree"
        xpos 570
        ypos 256
        action [Hide("submod_interactions"), Jump("monika_cheeksbeta")]
        alternate [Hide("submod_interactions"), Jump("monika_cheeks_long")]

screen button_custom_zoom():
    zorder 51
    style_prefix "hkb"
    vbox:
        if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
            xpos 0.05
            yanchor 1.0
            ypos 595
        else:
            xpos 0.05
            yanchor 1.0
            ypos 635
        if renpy.get_screen("hkb_overlay"):
            if store.disable_zoom_button:
                textbutton ("Zoom")
            else:
                textbutton ("Zoom") action Show("extra_custom_zoom")

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
            action [SetVariable("player_zoom", store.mas_sprites.zoom_level), Hide("extra_custom_zoom")]

        frame:
            area (195, 450, 80, 255)
            style "mas_extra_menu_frame"
            vbox:
                spacing 2
                label "Zoom":
                    text_style "mas_extra_menu_label_text"
                    xalign 0.5

                # resets the zoom value back to default
                textbutton _("Reset"):
                    style "mas_adjustable_button"
                    selected False
                    xsize 72
                    ysize 35
                    xalign 0.3
                    action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)

                # actual slider for adjusting zoom
                bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                    style "mas_adjust_vbar"
                    xalign 0.5
                $ store.mas_sprites.adjust_zoom()

#Will be displayed when the player selects a cup
screen shell_game_minigame():
    zorder 50
    style_prefix "hkb"
    use extra_no_click()
    
    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_coordinates[0]
        ypos 250
        idle "cup_idle"
        hover "cup_hover"
        focus_mask "cup_hover"
        action Verification(0, ball_position, "check_label")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_coordinates[1]
        ypos 250
        idle "cup_idle"
        hover "cup_hover"
        focus_mask "cup_hover"
        action Verification(1, ball_position, "check_label")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_coordinates[2]
        ypos 250
        idle "cup_idle"
        hover "cup_hover"
        focus_mask "cup_hover"
        action Verification(2, ball_position, "check_label")

    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton ("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

#====Loop PSR
screen PSR_mg():
    zorder 50
    #Letter from Monika
    imagebutton:
        idle "card_back"
        action NullAction()
        xalign 0.7
        yalign 0.1
    #Rock
    imagebutton:
        idle "e_rock"
        hover "e_rock"
        at hover_card
        action [SetVariable("your_choice", 1), Hide("PSR"), Jump("psr_loop")]
        xalign 0.5
        yalign 0.7
    #Paper
    imagebutton:
        idle "e_paper"
        hover "e_paper"
        at hover_card
        action [SetVariable("your_choice", 2), Hide("PSR"), Jump("psr_loop")]
        xalign 0.7
        yalign 0.7
    #Scissors
    imagebutton:
        idle "e_scissors"
        hover "e_scissors"
        at hover_card
        action [SetVariable("your_choice", 3), Hide("PSR"), Jump("psr_loop")]
        xalign 0.9
        yalign 0.7

    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton ("Quit") style "hkb_button" action [Hide("PSR"), Jump("psr_quit")]

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
    zorder 49
    if renpy.get_screen("hkb_overlay"):
        draggroup:
            drag:
                child "sticker_eyes"
                selected_hover_child "sticker_baka"
                dragged chibika_relax_drag
                if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
                    xpos chibi_xpos ypos 390
                else:
                    xpos chibi_xpos ypos chibi_ypos

#====Current minigame score
screen score_minigame(game=None):
    if game == "psr":
        $ first_text = "Monika"
        $ second_text = player
        $ first_score = store.moni_wins
        $ second_score = store.player_wins
    elif game == "sg":
        $ first_text = "Turn"
        $ second_text = "Good"
        $ first_score = store.current_turn
        $ second_score = store.correct_answers
        
    add "note_score"
    vbox:
        xpos 0.905
        ypos 0.015
        text "[first_text] : [first_score]"  size 30 style "monika_text"
        text "[second_text] : [second_score]"  size 30 style "monika_text"

#====Simple menu generator with use of classes
screen list_scrolling(variable, extra_area, scroll_align, label, close=None):
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
                    for l_name in variable:
                        textbutton l_name[0]:
                            xsize extra_area[2]
                            action [Hide("list_scrolling"), Jump(l_name[1])]
            null height 20
            textbutton ("Nevermind") action [Hide("list_generator"), Jump(label)]    
        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align
    if close == True:
        vbox:
            xpos 0.097
            yanchor 1.0
            ypos 50

            textbutton ("Close") style "hkb_button" action [Hide("list_scrolling"), Jump("close_extraplus")]

#====Simple menu generator
screen list_generator(items, display_area, scroll_align, label, close=None):
    zorder 50
    style_prefix "scrollable_menu"

    fixed:
        area display_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    for i in items:
                        textbutton i.name:
                            xsize display_area[2]
                            action [Function(i), Hide("list_generator"), Jump("close_extraplus")]
            null height 20
            textbutton ("Nevermind") action [Hide("list_generator"), Jump(label)]
        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align
    if close == True:
        vbox:
            xpos 0.097
            yanchor 1.0
            ypos 50

            textbutton ("Close") style "hkb_button" action [Hide("list_scrolling"), Jump("close_extraplus")]

#====Background loop
screen dating_loop(acs, acs_two, ask, finish, label_boop, boop_enable=None):
    if monika_chr.is_wearing_acs(acs) or monika_chr.is_wearing_acs(acs_two):
        pass
    else:
        timer 900.0 action [Hide("dating_loop"), Jump(finish)]

    zorder 50
    vbox:
        if store.mas_submod_utils.isSubmodInstalled("Noises Submod"):
            xpos 0.05
            yanchor 1.0
            ypos 555
        else:
            xpos 0.05
            yanchor 1.0
            ypos 595
        textbutton ("Talk") style "hkb_button" action [Hide("dating_loop"), Jump(ask)]
    #Noise
    if boop_enable == True:
        imagebutton:
            idle "zoneone"
            xpos 620
            ypos 235
            action [Hide("dating_loop"), Jump(label_boop)]

#====Boop war?
screen boop_event(timelock, endlabel, editlabel):
    timer timelock action [Hide("boop_event"), Jump(endlabel)]
    zorder 50
    style_prefix "hkb"
    #Noise
    imagebutton:
        idle "zoneone"
        xpos 620
        ypos 235
        action [Hide("boop_event"), Jump(editlabel)]
    if boop_war_count >= 25:
        #Head
        imagebutton:
            idle "zonetwo"
            xpos 550
            ypos 10
            action [Hide("boop_event"), Jump("headpat_dis")]
        #Cheeks
        imagebutton:
            idle "zoneone"
            xpos 700
            ypos 256
            action [Hide("boop_event"), Jump("cheeks_dis")]
        imagebutton:
            idle "zoneone"
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