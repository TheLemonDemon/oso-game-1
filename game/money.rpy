image cash_bundle_1:
    "items/cash_bundle.png"
    xalign 0.5
    yalign 0.55
    zoom 4.0

label money_get:
    if money == 0:
        "A player should never see this text."
    elif money == 1:
        show cash_bundle_1
        "You now have {b}some money{/b}!"
        hide cash_bundle_1
        return

label dolly:
    scene bg mainstreet
    show dolly
    if party_bs:
        jump .dbs
    elif dolly_first == False:
        jump .dfirst
    else:
        jump .drepeat

label .dbs:
    show posty neutral
    show bs follow behind posty
    p "_" #todo: #111 Dolly quickly rejects Brand Soda, saying they've already spoken.
    jump mainstreet

label .dfirst:
    show posty neutral
    p "meeting dolly first time" # TODO: #35 initial dolly conversation; transition seamlessly into money checking tree
    jump .money_check

label .drepeat:
    show posty neutral
    p "revisiting dolly" # TODO: #36 repeat dolly conversation; transition seamlessly into money checking tree
    jump .money_check

label .money_check:
    if money == 0:
        if item.red_cash:
            show redcash
            p "i have red cash" # TODO: #37 Posty offers the red cash since she lacks real money
            jump mainstreet
        else:
            p "i have nothing" # todo: #38 posty has no money
            jump mainstreet
    elif money == 1:
        show cash_bundle_1
        p "i have some money" # todo: #39 posty has "some" money
        jump mainstreet

