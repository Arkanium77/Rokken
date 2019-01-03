#Сцена 1
label ext:
    stop music fadeout 0.5
    label sc1:
    #jump p
    scene bg island far
    play bgs "sounds/sound/m/Uminekos.mp3"
    #show screen points
    $ renpy.pause(1)
    #$detective=0
    play sound flsh
    show letters filter with flash
    voice pm
    "Остров Роккен. 4 октября 1986 год. 10:30 утра."

    #hide screen transient
    hide letters filter
    with flash
    play sound shut
    $ renpy.pause(1)

    show bg ship starboard with vpunch
    play sound "sounds/sound/s/batscreem.mp3"
    "{color=#c51d34}???{/color}" "ААААА!!! НЕЕЕТ!"
    "{color=#c51d34}???{/color}" "Трясёт, трясёт, трясёт!"
    show bg ship starboard with vpunch
    "{color=#c51d34}???{/color}" "Упаду, упаду, упаду же!!!"
    show bg ship starboard with vpunch
    "{color=#c51d34}???{/color}" "ААААА!!!"

    scene bg black with fade
    stop bgs fadeout 0.5
    stop sound fadeout 0.5
    $ renpy.block_rollback()
    $_game_menu_screen = None
    $config.allow_skipping = False
    play movie "images/op.webm"
    $renpy.pause(100,hard=True)
    $_game_menu_screen = "save_screen"
    $config.allow_skipping = True
    $ renpy.block_rollback()

    play music "sounds/music/bgm/Witch's Room.mp3"
    show bg ship left with fade
    $renpy.pause(1.5)
    show letters filter
    with flash
    play sound flsh #youtube.com/watch?v=-JBpRWIxxi0
    voice pm
    "Остров Роккен. 4 октября 1986 год. 11:00 утра."
    play sound shut
    hide letters filter
    show bat exc at left
    show geo std at right
    show jes std at right2
    show mar std at right3
    with flash


    "{color=#c51d34}???{/color}" "Приплыли... Приплыли-таки наконец!"
    "{color=#c51d34}???{/color}" "Всё же человек - существо сухопутное."
    hide bat
    play sound flsh
    show letters filter at center
    show bat smi at left
    with flash

    "{color=#c51d34}???{/color}"  "Привет. Меня зовут Баттлер Уширомия."
    bat "Остров, на который мы прибыли, называется Роккен."
    bat "Он целиком и полностью принадлежит семье Уширомия."
    show bat tau with dissolve
    bat "Семейка Уширомия чертовски богата."
    play sound shut
    hide geo
    show geo std at right
    show bat smi
    with flash

    bat "Это Джордж - мой двоюродный брат."
    play sound shut
    hide jes
    show jes std at right2
    with flash

    bat "Это Джессика - моя кузина. В отличие от нас, она живёт на этом острове постоянно."
    play sound shut
    hide mar
    show mar std at right3
    with flash

    bat "А это Мария - моя милая двоюродная сестрёнка."
    play sound shut
    hide letters filter
    show bg ship left
    with flash

    geo "Мария, тебя не укачало?"
    show bat smi_e at left with dissolve
    bat "Укачало?"
    show bat ang at left with dissolve
    bat "ДА КАК ТУТ МОГЛО НЕ УКАЧАТЬ?"
    "{color=#8000FF}???{/color}" "Баттлер, успокойся."

    scene bg ship1 m
    show rud std at left
    show kyr std at left2
    with dissolve
    "{color=#32078D}???{/color}" "И правда, чего ты кричишь?"
    play sound flsh
    show letters filter
    hide kyr
    hide rud
    show rud std at left
    show kyr std at left2
    with flash

    bat "Это Рудольф - мой отец. А рядом стоит Кириё - его новая жена."
    play sound shut
    hide letters filter
    show bat ang at offscreenright
    with flash

    show bat ang at right with move
    bat "Да как тут успокоиться?! Это было ужасно!"
    show ros std at offscreenleft
    show ros std at left1 with move
    "{color=#E28B00}???{/color}" "Баттлер, даже Мария перенесла эту поездку спокойно. Что с тобой?"
    play sound flsh
    show letters filter
    hide ros
    hide bat
    show ros std at left1
    show bat std at right
    with flash

    bat "А это тётя Роза - младшая дочь дедушки и мама Марии."
    play sound shut
    hide letters filter
    show bat ang at right
    show mar std at offscreenright
    with flash

    show mar std at right2 with move
    mar "Угу."
    show mar smi with dissolve
    mar "Марии даже весело было."
    "{color=#FDDDE6}???{/color}" "Господин Баттлер, все уже закончилось. Пойдёмте все в дом?"

    scene bg beach stairs
    play sound flsh
    show letters filter
    show kum smi at center
    with flash

    bat "А это бабуля Кумасава. Она преданно служит нашей семье уже много лет."
    bat "Она нянчилась с нами, когда мы были детьми."
    play sound shut
    hide letters filter
    show bat exc at offscreenright
    with flash

    show bat exc at right with move
    bat "А, бабуля Кумасава! Действительно, что же это я разошелся."
    show bat smi at right with dissolve
    bat "Пойдёмте в дом! Мне уже не терпится попробовать стряпню Гоуды."
    #label p: #Рабочая метка
    play bgs walk
    scene bg beach stairs up at walking
    $ renpy.pause(1.5)
    show bg beach stairs up1 at walking
    $ renpy.pause(1.5)
    show bg forest stairs mb at walking
    $ renpy.pause(1.5)
    stop bgs
    show bg garden house1 m at center with dissolve
    jump sc2
    bat "Дооооом"
