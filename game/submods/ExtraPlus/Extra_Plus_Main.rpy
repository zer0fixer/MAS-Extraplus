################################################################################
## SUBMOD
################################################################################
#Submod created by ZeroFixer(u/UnderstandingAny7135), this submod is made for MAS brothers/sisters.
#Shoutout to u/my-otter-self at reddit, who proofread the whole mod.
# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="ZeroFixer",
        name="Extra Plus",
        description="A submod that adds an Extra+ button, as well as adding more content!",
        version="1.0"
    )

# Register the updater
init -990 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Plus",
            user_name="zer0fixer",
            repository_name="MAS-Extraplus",
            update_dir=""
        )

################################################################################
## VARIABLES
################################################################################
#Menus dialogues
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

#Boop count
default persistent.plus_boop = [0, 0, 0]
default boop_war_count = 0

#Pos
define chibi_xpos = 0.05
define chibi_ypos = 430

#????
define extra_old_bg = ""
define extra_chair = ""
define extra_table = ""
define ver_night = ""
define rng_global = ""
define show_chibika = None

#Minigames variables
#Cup coordinates
define cup_coordinates = [695, 925, 1155]
define cup_coordinates_real = [695, 925, 1155]
#Skin, It will depend on your concern for the other dokis, if you don't care about them at all, only the first two skins will come out.
define cup_list = ["cup", "cup_monika", "cup_yuri", "cup_natsuki", "cup_sayori"]
#PSR
default player_wins = 0
default moni_wins = 0
#SG
define minigames_menu = []
define original_cup = [0, 1, 2]
define ball_position = 1
default current_turn = 0
default shuffle_cups = 0
default comment = False
define your_choice = 0
define correct_answers = 0
define cup_speed = 0.5 #Default
define difficulty_sg = None

#Comments by moni on standard difficulties
define comments_good = ""
define comments_bad = ""
define complies = [
    "Great.",
    "Keep it up, [player]!",
    "Good.",
    "Amazing, [player]!",
    ]
define not_met = [
    "Oh, too bad~",
    "It's not that, [player].",
    "Try again~",
    "Don't get distracted, [player]."
    ]

################################################################################
## FUNCTIONS/CLASSES
################################################################################
init python:
    def Extraplus_show():
        probability = renpy.random.randint(1,50)
        if probability == 1:
            renpy.show_screen("chibika_chill")
        if mas_isDayNow():
            ver_night = ""
        elif not mas_isDayNow():
            ver_night = "-n"
        renpy.call_screen("submod_interactions")

    def ExtraButton():
        if not ExtraVisible():
            config.overlay_screens.append("extraplus_button")

    def ExtraVisible():
        return "extraplus_button" in config.overlay_screens

    def chibika_relax_drag(drags, drop):

        if not drop:
            drags[0].snap(chibi_xpos, chibi_ypos, 0.1)
            return

        store.chibika_relax = drags[0].drag_name
        store.chibiarea = drop.drag_name
        return True

    def chibi_dragged (drags, drop):

            if not drop:
                    if drags[0].drag_name == "chibika_relax":
                        drags[0].xpos = 0.05
                        drags[0].ypos = 430
            return

    # Also this code from line 144 to 168 doesn't belong to me, all the credit goes to the developers,
    # I used it so that monika had several expressions during the Extra+ loop. If the devs don't like me using it,
    # they can tell me and I will remove it to avoid inconvenience.


    # Clarification: Why did I use this particular code?
    # It is for the function of making monika boop and as it has another pose that prevented me from doing it with the Monika idle
    # I had no choice but to use it.

    #Monika idle v2 extra
    monika_extraplus = MASMoniIdleDisp(
        (
            MASMoniIdleExp("1eubla", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1hubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1eubla", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=30),
                    MASMoniIdleExp("1sua", duration=4),
                    MASMoniIdleExp("1ekblu", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
                    MASMoniIdleExp("1tuu", duration=30),
                    MASMoniIdleExp("1hua", duration=30),
                    MASMoniIdleExp("1eua", duration=30),
                ]
            ),
            MASMoniIdleExp("1eua_follow", duration=40),
            MASMoniIdleExp("1eka", duration=30),
            MASMoniIdleExp("1dubla", duration=30, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE))

        )
    )

    #Check if the selected cup is correct.
    class Verification(Action):

        def __init__(self, index, check_index, final_label):
            self.index = index
            self.check_index = check_index
            self.final_label = final_label

        def __call__(self):
            renpy.hide_screen("no_click")
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

    #A class that is used to display a list of available minigames, I had to do so because I didn't know how to adapt the TTT to the submod, sorry :p
    class minigame:
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

    #Select a glass randomly, so you won't see the same glass or maybe not, I'm terrible at programming.
    cup_skin = renpy.random.choice(cup_list)
    #Starts the Extra+ button
    ExtraButton()

################################################################################
## IMAGES
################################################################################
init python:
    #Desserts and objects
    # If you are not a Monika After Story developer, please note that the code used in lines 103 to 156 does not belong to me,
    # I used it to make Monika's date with the player more dynamic, so be careful if you are going to edit it.
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

init:
    #Minigames images
    image note_score = "submods/ExtraPlus/submod_assets/sprites/note_score.png"
    #TTT
    image notebook = "submods/ExtraPlus/submod_assets/sprites/notebook.png"
    image line_black = "submods/ExtraPlus/submod_assets/sprites/line.png"
    image line_player = "submods/ExtraPlus/submod_assets/sprites/line_player.png"
    image line_moni = "submods/ExtraPlus/submod_assets/sprites/line_moni.png"
    image ttt_cross:
        Text("8", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 200, color = "#002fff", outlines = [])
        on show:
            alpha 0.5
            linear 0.25 alpha 1.0

    image ttt_cross_cursor:
        Text("8", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 200, color = "#ff00f2", outlines = [])
        alpha 0.25
        truecenter

    image ttt_circle:
        Text("7", font = "submods/ExtraPlus/submod_assets/Pictograms.ttf", size = 200, color = "#009D71", outlines = [])
        on show:
            alpha 0.0
            linear 0.25 alpha 1.0

    #PSR
    image e_paper = "submods/ExtraPlus/submod_assets/sprites/paper.png"
    image e_rock = "submods/ExtraPlus/submod_assets/sprites/rock.png"
    image e_scissors = "submods/ExtraPlus/submod_assets/sprites/scissors.png"
    image card_back = "submods/ExtraPlus/submod_assets/sprites/card_back.png"
    #SG
    image cup:
        xanchor 0.5 yanchor 0.5
        contains:
            "submods/ExtraPlus/submod_assets/sprites/[cup_skin].png"
            xalign 0.5 yalign 0.5

    image cup_hover:
        contains:
            "submods/ExtraPlus/submod_assets/sprites/cup_hover.png"
            xalign 0.5 yalign 0.5

    image cup_idle:
        contains:
            "submods/ExtraPlus/submod_assets/sprites/cup_idle.png"
            xalign 0.5 yalign 0.

    image ball:
        xanchor 0.5 yanchor 0.5
        contains:
            "submods/ExtraPlus/submod_assets/sprites/ball.png"
            xalign 0.5 yalign 0.5

    #Chibika
    image sticker_baka = "submods/ExtraPlus/submod_assets/sprites/sticker_baka[ver_night].png"
    image sticker_sleep = "submods/ExtraPlus/submod_assets/sprites/sticker_sleep[ver_night].png"
    image sticker_up = "submods/ExtraPlus/submod_assets/sprites/sticker_up[ver_night].png"
    image pop_effect = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/pop_effect.png", (170, 170), (3, 3), .125, loop=False)
    image pop_effect_n = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/pop_effect-n.png", (170, 170), (3, 3), .125, loop=False)

    #Flip
    image coin_heads = "submods/ExtraPlus/submod_assets/sprites/coin_heads[ver_night].png"
    image coin_tails = "submods/ExtraPlus/submod_assets/sprites/coin_tails[ver_night].png"
    image coin_flip = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin.png", (100, 100), (3, 2), .125, loop=True)
    image coin_flip_n = anim.Filmstrip("submods/ExtraPlus/submod_assets/sprites/sprite_coin-n.png", (100, 100), (3, 2), .125, loop=True)

    #Boop
    image zoneone = im.Scale("mod_assets/other/transparent.png", 30, 30)
    image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)
    image zonethree = im.Scale("mod_assets/other/transparent.png", 40, 40)

    #Idle edit
    image monika staticpose = monika_extraplus

################################################################################
## SCREEN
################################################################################
#Simply display the button in the loop
screen extraplus_button():
    zorder 12
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 50

        if renpy.get_screen("hkb_overlay"):
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    text _("")
                else:
                    textbutton _("Extra+")
            #I know this is rather orthodox, I will improve it later.
            elif mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.UPSET or mas_curr_affection == mas_affection.DISTRESSED or mas_curr_affection == mas_affection.BROKEN:
                textbutton _("Extra+")
            else:
                textbutton _("Extra+") action Jump("show_extraplus")

#Areas where you can interact with moni
screen submod_interactions():
    zorder 50
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 170

        textbutton _("Close") action [Hide("submod_interactions"), Jump("back_extra")]

        textbutton _("Go to") action [Hide("submod_interactions"), Jump("walk_extra")]

        textbutton _("Minigame") action [Hide("submod_interactions"), Jump("minigames_extra")]

        textbutton _("Addition") action [Hide("submod_interactions"), Jump("tools_extra")]

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

#Will be displayed when the player selects a cup
screen shell_game_minigame():
    zorder 50
    style_prefix "hkb"
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
        textbutton _("Quit") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

    add "note_score"
    vbox:
        xpos 0.905
        ypos 0.015
        text "Turn : [current_turn]"  size 30 style "monika_text"
        text "Reply : [correct_answers]"  size 30 style "monika_text"

#Loop PSR
screen PSR_mg():
    zorder 50
    imagebutton:
        idle "card_back"
        action NullAction()
        xalign 0.7
        yalign 0.1
    imagebutton:
        idle "e_rock"
        hover "e_rock"
        at hover_card
        action [SetVariable("your_choice", 1), Hide("PSR"), Jump("psr_loop")]
        xalign 0.5
        yalign 0.7

    imagebutton:
        idle "e_paper"
        hover "e_paper"
        at hover_card
        action [SetVariable("your_choice", 2), Hide("PSR"), Jump("psr_loop")]
        xalign 0.7
        yalign 0.7

    imagebutton:
        idle "e_scissors"
        hover "e_scissors"
        at hover_card
        action [SetVariable("your_choice", 3), Hide("PSR"), Jump("psr_loop")]
        xalign 0.9
        yalign 0.7

    style_prefix "hkb"
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Quit") action [Hide("PSR"), Jump("psr_quit")]

    add "note_score"
    vbox:
        xpos 0.905
        ypos 0.015
        text "[m] : [moni_wins]"  size 30 style "monika_text"
        text "[player] : [player_wins]"  size 30 style "monika_text"

#Restrict the player from advancing in the conversation.
screen no_click():
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()

    imagebutton:
        idle "mod_assets/other/transparent.png"
        action NullAction()

#A small Easter egg
screen chibika_chill():
    zorder 60
    draggroup:
        drag:
            drag_name "chibika_relax"
            idle_child "sticker_sleep"
            hover_child "sticker_up"
            selected_hover_child "sticker_baka"
            dragged chibika_relax_drag
            xpos chibi_xpos ypos chibi_ypos

#Minigames options
screen minigame_ui():
    style_prefix "talk_choice"
    vbox:
        for i in minigames_menu:
            textbutton i.name action [Function(i), Hide("minigame_ui")]

        textbutton _("Nevermind") action [Hide("minigame_ui"), Jump("return_extra")]

#Cafe loop
screen cafe_loop():
    if monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        pass
    else:
        timer 1800.0 action [Hide("cafe_loop"), Jump("monika_no_dessert")]

    style_prefix "hkb"
    zorder 50
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 0.5
        textbutton _("Ask") action [Hide("cafe_loop"), Jump("cafe_talkdemo")]

    imagebutton:
        idle "zoneone"
        xpos 620
        ypos 235
        action [Hide("cafe_loop"), Jump("monika_boopcafebeta")]

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

################################################################################
## TRANSFORM
################################################################################
transform hover_card:
    on idle:
        pause .15
        yoffset 0
        easein .175 yoffset 10

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

################################################################################
## BACKGROUNG
################################################################################
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
