label restaurant_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_icecream):
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            m 3eub "Also, I'll put this plate away, I won't be long."
            $ monika_chr.remove_acs(extraplus_acs_candles)
            $ monika_chr.remove_acs(extraplus_acs_pasta)
            $ monika_chr.remove_acs(extraplus_acs_icecream)
        else:
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            $ monika_chr.remove_acs(extraplus_acs_candles)

    elif monika_chr.is_wearing_acs(extraplus_acs_flowers):
        if monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
            m 3eua "I must put this plate away."
            m 3eua "Also, I'll put this cup away, it won't be long now."
            $ monika_chr.remove_acs(extraplus_acs_pancakes)
            $ monika_chr.remove_acs(extraplus_acs_pudding)
        else:
            m 3eua "I must put this plate away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_pancakes)
            $ monika_chr.remove_acs(extraplus_acs_pudding)

    call mas_transition_to_emptydesk from monika_hide_exp_3
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    jump restore_bg
    return

label monika_no_food:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        $ monika_chr.remove_acs(extraplus_acs_pasta)
        $ monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pasta."
        m 1eub "I really enjoyed it~"
        m "Now I'll grab some dessert. Be right back!"
        call mas_transition_to_emptydesk from monika_hide_exp_2
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_icecream)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        $ monika_chr.remove_acs(extraplus_acs_pancakes)
        $ monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pancakes."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        call mas_transition_to_emptydesk from monika_hide_exp_2
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        $ monika_chr.remove_acs(extraplus_acs_waffles)
        $ monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my waffles."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        call mas_transition_to_emptydesk from monika_hide_exp_2
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    if food_player is True:
        m 1etb "By the way, have you finished your food yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your food yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a drink with you."
    m 1hua "Let me know if you want to come back again."
    jump to_restaurant_loop
    return

init python:
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
        keep_on_desk=True
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
