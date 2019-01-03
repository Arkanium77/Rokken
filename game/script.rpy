# Игра начинается здесь.
label start:

    transform left05:
        xalign 0.08
        yalign 1.0
        #linear 2.0 xalign 0.15
        #repeat

    transform left1:
        xalign 0.15
        yalign 1.0
        #linear 2.0 xalign 0.15
        #repeat
    transform left2:
        xalign 0.3
        yalign 1.0
        #linear 1.0 xalign 0.3
        #repeat
    transform left3:
        xalign 0.25
        yalign 1.0
        #linear 1.5 xalign 0.25
        #repeat
    transform left4:
        xalign 0.4
        yalign 1.0
        #linear 1.5 xalign 0.25
        #repeat

    transform right1:
        xalign 0.85
        yalign 1.0
        #linear 1.5 xalign 0.25
        #repeat
    transform right2:
        xalign 0.7
        yalign 1.0
    transform right3:
        xalign 0.8
        yalign 1.0
    transform right4:
        xalign 0.6
        yalign 1.0
    transform right5:
        xalign 0.45
        yalign 1.0


    transform walking:
        pos (0,0)
        linear 0.3 pos (-5,-3)
        linear 0.3 pos (0,0)
        pos (0,0)
        linear 0.3 pos (5,-3)
        linear 0.3 pos (0,0)
        repeat

    transform rainy:
        pos (0,0)
        linear 0.3 pos (-5,-3)
        linear 0.3 pos (0,0)
        pos (0,0)
        linear 0.3 pos (5,-3)
        linear 0.3 pos (0,0)
        repeat

    transform running:
        pos (0,0)
        linear 0.13 pos (-5,-3)
        linear 0.13 pos (0,0)
        pos (0,0)
        linear 0.13 pos (5,-3)
        linear 0.13 pos (0,0)
        repeat


    #################
    #    ТАЙМЕРЫ    #
    #################
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0


    #ВАРИАНТ С БАРОМ
    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01),
        false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.12 xmaximum 300 at alpha_dissolve


    #ВАРИАНТ СО СЧЁТЧИКОМ
    # screen countdown:
    #     timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    #     if time <= 2:
    #         text str(time) xalign 0.5 yalign 0.8 size 50 color "#FF0000" #at alpha_dissolve
    #     else:
    #         text str(time) xalign 0.5 yalign 0.8 size 50 color "#FFFFFF" at alpha_dissolve
    #




    #############################
    #   НАСТРОЙКА  NVL-РЕЖИМА   #
    #############################
    init python:
        gui.nvl_height=None
        gui.nvl_spacing = 15 #отступ между репликами в режиме NVL
        #style.nvl_dialogue.size = 60# Размер текста
        style.nvl_dialogue.drop_shadow = [(1, 1)] # Тень, числа это смещение тени по xy
        style.nvl_dialogue.drop_shadow_color = "#FFFFFF"
        style.nvl_dialogue.font=ffont
        style.nvl_dialogue.size=30
        #style.nvl_dialogue.slow_cps=15

    # nvl clear
    # letters "\nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел
    #  \nСвой город помню я родной с богатой рыбою рекой\nИдти вдоль речки коли смел - златые земли твой удел"
    # nvl hide
    # nvl clear

    style lett is say_dialogue:
        size style.say_dialogue.size+5
        #font "gui/Fonts/letteratrentadue.ttf"
        font ffont


    screen points:
        add "gui/overlay.png"
        text "Очки Детектива: [detective]" xalign 1.0 yalign 0.03 font ffont size 30
        #imagebutton idle "v.png" action SetVariable ("Money", Money+20) ypos 50
    screen stat:
        #on 'show' action SPlay1(pm, loop=False)

        # можно остановить только дождь SStop("rain"),
        # тогда начавшийся гром догремит и стихнет сам
        #on 'hide' action SStop("pm")
        add "gui/info.png"
        text "Статистика:" xalign 0.75 yalign 0.07 font ffont size 50
        $tmp=""
        if liekyr=="yes":
            $tmp= "Вы солгали Кириё."
        if liekyr=="no":
            $tmp="Вы не стали лгать Кириё."

        text "\nОчки детектива:"+" [detective]"+"\n\nОтношения:    "+" Клаус - [h] \n"+ "               Рудольф: [m] \n"+"               Ева: [l]\n"+"               Роза: [r]\n\n                             \n"+"[tmp]\n\n    \n"+"Логических последовательностей\n                     разгадано: [lg]  " xalign 0.99 yalign 0.2 font ffont size 30 slow_cps 15

        #imagebutton idle "v.png" action SetVariable ("Money", Money+20) ypos 50




        ############################
        #     Всякий питонокод     #
        ############################


    init -1 python:
        flash = Fade(.25, 0, .75, color="#fff")
        ffont="gui/Fonts/TrixieCyr-Plain.otf"
        ####################
        #    Переменные    #
        ####################
        h=0 #high - старшая ветвь - Клаус и Натсухи
        m=0 #middle - средняя ветвь - Ева и Хидеёши
        l=0 #low - младшая ветвь - Рудольф и Кириё
        r=0 #r - rose - Тётя Роза

        s=0 #s - servants - слуги

        detective=0 #detective - детективные навыки Баттлера



        flag=0
        flag1=0

        ####################
        #    TIMER MENU    #
        ####################
        timer_range = 0
        timer_jump = 0
        # time = the time the timer takes to count down to 0.
        # timer_range = a number matching time (bar only)
        # timer_jump = the label to jump to when time runs out
        #
        # label menu1:
        #     $ time = 5
        #     $ timer_range = 5
        #     $ timer_jump = 'menu1_slow'
        #     show screen countdown
        #     menu:
        #         "Choice 1":
        #             hide screen countdown
        #             e "You chose 'Choice 1'"
        #             jump menu1_end
        #         "Choice 2":
        #             hide screen countdown
        #             e "You chose 'Choice 2'"
        #             jump menu1_end
        #
        # label menu1_slow:
        #     e "You didn't choose anything."
        #
        # label menu1_end:
        #     e "Anyway, let's do something else."
    jump ext
    return
#Процесс программирования игр в жанре ВН

#Язык Python и движок Ren'py
#как средства программирования игр


init python:
    renpy.music.register_channel("bgs", "sfx", loop=True)


    def Ani(img_name, frames, delay=.1, loop=True, reverse=True, effect=None, start=1, ext="png", **properties):
        args = []
        for i in range(start, start + frames):
            args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            for i in range(start + frames - 2, start, -1):
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                if loop or (i > start + 1):
                    args.append(delay)
                    args.append(effect)
        return anim.TransitionAnimation(*args, **properties)
    # время появления/затухания звуков
    fade_time = 1.0
    # регистрируем каналы, чтобы звуки не прерывали друг друга
    channels = ["rain", "thunder1", "thunder2", "thunder3"]
    for i in channels:
        renpy.music.register_channel(i, "sfx", True)
    # воспроизводим звуки на своих каналах
    # либо на канале sound, если нужный канал не зарегистрирован
    def splay(name, channel=None, loop=False, fadein=fade_time, fadeout=fade_time):
        if not channel in channels:
            channel = None
        if channel is None:
            if name in channels:
                channel = name
            else:
                channel = "sound"

        fn = "sounds/" + name + ".ogg"

        renpy.music.play(fn, channel=channel, loop=loop, fadeout=fadeout, fadein=fadein)
    # постепенно останавливаем звуки или один звук, если на входе не список
    def sstop(channel=channels, fadeout=fade_time):
        if isinstance(channel, list):
            for i in channel:
                renpy.music.stop(i, fadeout=fadeout)
        else:
            renpy.music.stop(channel, fadeout=fadeout)
    # новое положение молний
    xa = renpy.random.random()
    def newxa():
        global xa
        xa = renpy.random.random()
        renpy.restart_interaction()
    # функция → action
    SPlay = renpy.curry(splay)
    SStop = renpy.curry(sstop)
    NewXA = renpy.curry(newxa)


    def splay1(name, channel=None, loop=True, fadein=fade_time, fadeout=fade_time):
        if not channel in channels:
            channel = None
        if channel is None:
            if name in channels:
                channel = name
            else:
                channel = "sound"

        fn = name

        renpy.music.play(fn, channel=channel, loop=loop, fadeout=fadeout, fadein=fadein)
    # постепенно останавливаем звуки или один звук, если на входе не список
    # def sstop1(channel=channels, fadeout=fade_time):
    #     if isinstance(channel, list):
    #         for i in channel:
    #             renpy.music.stop(i, fadeout=fadeout)
    #     else:
    #         renpy.music.stop(channel, fadeout=fadeout)
    SPlay1 = renpy.curry(splay1)
    #SStop1 = renpy.curry(sstop1)

# экран для дождя и грома
screen Rain:
    # включаем и выклюяаем дождь вместе с экраном
    on 'show' action SPlay("rain", loop=True)
    # можно остановить только дождь SStop("rain"),
    # тогда начавшийся гром догремит и стихнет сам
    on 'hide' action SStop()
    # псевдо-рандомные раскаты
    timer 10 repeat True action SPlay("thunder1")
    timer 25 repeat True action SPlay("thunder2")
    timer 40 repeat True action SPlay("thunder3")
    # картинка с молниями
    #timer .1 repeat True action NewXA()
    #add "light":
    #    xalign xa
    # дождь
    add "rain":
        alpha .15

init:
    # пустая картинка
    image none = Null(1, 1)
    # анимация дождя
    image rain = Ani("rain", 5, .1, reverse=False)
    # анимация молнии
    # image lightning = Ani("lightning", 3, .025)
    # # мерцание молнии
    # image light:
    #     yalign 0 yanchor 0
    #     # пусто
    #     "none"
    #     4.5
    #     xzoom 1.0
    #     "lightning"
    #     .1
    #     "none"
    #     .1
    #     "lightning"
    #     .1
    #     "none"
    #     1.5
    #     # зеркальное отражение
    #     xzoom -1.0
    #     "lightning"
    #     .1
    #     "none"
    #     .05
    #     "lightning"
    #     .1
    #     repeat




    # time = the time the timer takes to count down to 0.
    # timer_range = a number matching time (bar only)
    # timer_jump = the label to jump to when time runs out

    # label menu1:
    #     $ time = 5
    #     $ timer_range = 5
    #     $ timer_jump = 'menu1_slow'
    #     show screen countdown
    #     menu:
    #         "Choice 1":
    #             hide screen countdown
    #             bat "You chose 'Choice 1'"
    #             jump menu1_end
    #         "Choice 2":
    #             hide screen countdown
    #             bat "You chose 'Choice 2'"
    #             jump menu1_end
    #
    # label menu1_slow:
    #     bat "You didn't choose anything."
    #
    # label menu1_end:
    #     bat "Anyway, let's do something else."
    # label menu2:
    #     $ time = 5
    #     $ timer_range = 5
    #     $ timer_jump = 'menu2_v2'
    #     show screen countdown
    #     menu:
    #         "Choice 1 fast":
    #             hide screen countdown
    #             bat "You chose 'Choice 1' fast"
    #             jump menu2_end
    #         "Choice 2 fast":
    #             hide screen countdown
    #             bat "You chose 'Choice 2' fast"
    #             jump menu2_end
    #
    # label menu2_v2:
    #     $ time = 5
    #     $ timer_range = 5
    #     $ timer_jump = 'menu2_slow'
    #     show screen countdown
    #     menu:
    #         "Choice 1 slow":
    #             hide screen countdown
    #             bat "You chose 'Choice 1', but were slow"
    #             jump menu2_end
    #         "Choice 2":
    #             hide screen countdown
    #             bat "You chose 'Choice 2', but were slow"
    #             jump menu2_end
    #
    # label menu2_slow:
    #     bat "You were really slow and didn't choose anything."
    #
    # label menu2_end:
    #     bat "Anyway, let's do something else."
