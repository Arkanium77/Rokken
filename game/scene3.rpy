#Сцена 3. Пляж и сад
label sc3:
    scene bg beach m
    show geo std at right4
    show jes std at right2
    show bat smi at right
    show mar std at right3
    with fade

    bat "Эх, славная погодка!"
    jes "Только надоедливых чаек что-то не слышно."
    show bat std with dissolve
    bat "Хм. Действительно."
    geo "Значит, шторм будет?"
    play sound "sounds/sound/s/Uu~.wav"
    mar "Пикник, пикник!"
    show bat smi with dissolve
    bat "Да уж, мы ведь пришли веселиться. Идём, Мария!"

    show bat smi at offscreenright
    show mar std at offscreenright
    with move

    show geo smi with dissolve
    geo "Пойдём, Джессика. Будет не честно, если они всё съедят без нас."

    show jes std at offscreenright
    show geo std at offscreenright
    with move

    scene bg beach rest
    show geo std at right2
    show jes std at right
    show bat smi at left
    show mar std at center
    with fade

    bat "Уф. Больше в меня и не влезет! А ещё ведь ужин..."
    mar "А теперь давайте разгадывать эпитафию Золотой Ведьмы!"
    show bat std with dissolve
    bat "Такой славный денёк, что и думать об этой жути не хочется."
    bat "Может завтра, когда гроза будет?"
    show mar dou with dissolve
    mar "Но я хочу сейчас."
    bat "Ну може..."
    show jes ang with dissolve
    jes "Баттлер!"
    show jes std with dissolve
    geo "Мария, а почему тебе так нравятся ведьмы?"
    show mar smi with dissolve
    mar "Ведьмы потрясные!"
    mar "Они магией всё могут!"
    mar "Сделать еду из ничего, превратить камень в золото, воскресить умерших."
    show geo smi with dissolve
    geo "Да, действительно, здорово."
    bat "Здорово. Но вспомните эпитафию."
    bat "Она же жуткая. Убийства, смерти..."
    show geo std
    show mar dou
    with dissolve
    mar "Но магии без жертв не бывает. Иначе, какая ценность в чуде?"
    show bat ace1 with vpunch
    stop music
    play sound "sounds/sound/s/tapestop.mp3"
    bat "Значит и не нужны такие чудеса! Ведьм не бывает."
    play music "sounds/music/bgm/Suspicion.mp3"
    mar "Как это не бывает? А как же золото, которое помогло дедушке?"


    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    menu:
        bat "Надо ей что-то ответить!"

        "Может быть он просто нашёл его.":
            $detective+=2
            hide screen countdown
            show bat ace1 with vpunch
            bat "Может быть он просто нашёл его!"
            bat "Мало ли кладов осталось в Японии. А ведь ещё война..."
            mar "Неплохой вариант. Но... Ты сам-то в это веришь?"
            mar "Веришь в то, что такое состояние может быть простой удачей?"
            show bat std with dissolve
            bat "Я не..."
            jump menu1_end

        "Наверное, у дедушки просто были накопления.":
            hide screen countdown
            show bat std with dissolve
            $detective+=1
            bat "Наверное... У него просто были какие-то накопления!"
            bat "Ну, а потом с помощью своих навыков и удачи он превратил их в богатства семьи Уширомия."
            mar "Я верю в таланты дедушки, но будь у него накопления, достаточные для возрождения мануфактур..."
            mar "...разве стал бы кто-то придумывать легенды, если бы объяснение было настолько простым?"
            jump menu1_end

        "Может, кто-то и одолжил золото. Но точно не ведьма!":
            hide screen countdown
            show bat ace1 with vpunch

            bat "Может и было золото! Может кто-то его и одолжил!"
            show bat ace1 with vpunch
            bat "Но точно не ведьма!"
            mar "И кто же мог одолжить дедушке ДВАДЦАТЬ МИЛЛИОНОВ ЙЕН? Да ещё и в золоте?"
            show bat std with dissolve
            bat "Мало ли в Японии богачей? Да и партнёры по бизнесу у него могли остаться."#Кривовато. Да.
            jump menu1_end


    label menu1_slow:
        hide screen countdown
        show bat ace1 with vpunch
        $detective-=1
        bat "Я... Не знаю."
        show bat std with dissolve
        bat "Но в ведьм верить не хочу."
        show mar ace with dissolve
        mar "Хе-хе-хе."
        show mar std with dissolve

    label menu1_end:
    mar "Эх, Баттлер. Магию нельзя увидеть, если не веришь."
    mar "Беатриче точно убьёт тебя первым."
    show bat dou with dissolve
    bat "Убьёт..?"
    voice pm
    "Мария роется в сумке."
    voice pm
    "Вскоре она достаёт оттуда два амулета."
    show mar smi with dissolve
    show scorpio with dissolve
    mar "Вот! Это поможет!"
    stop music fadeout 3.0
    hide scorpio
    with dissolve
    play music "sounds/music/bgm/Starmachine2000.mp3" fadein 1.0
    show mar smi at left1 with move
    $renpy.pause(0.2)
    show mar smi at center with move

    #"Мария протягивает амулет Баттлеру."
    #"На амулетах изображены странные символы, расположенные по кругу и выпуклый скорпион в его центре."
    mar "Скорпионы защищают от магии. Надеюсь, это поможет."
    show bat smi with dissolve
    bat "Ну, спасибо, Мария. Теперь мне будет спокойнее."
    show mar dou with dissolve
    mar "Я бы и вам дала, но..."
    mar "Но теперь у меня остался только один амулет."
    show geo smi with dissolve
    geo "Ничего страшного, Мария."
    geo "Отдай его Джессике. В конце концов она на острове живёт постоянно, ей нужнее."
    show geo std
    show mar std
    with dissolve
    mar "Угу."
    show mar std at right with move
    $renpy.pause(0.2)
    show mar std at center with move
    show jes smi with dissolve
    jes "Спасибо, Мария!"
    show jes std
    show bat std
    with dissolve
    bat "И всё же, эта эпитафия..."
    mar "Что - эпитафия?"
    bat "Вроде как, по легенде, ведьма заберёт всё, что есть у семьи Уширомия и только разгадав эпитафию мы сможем найти золото и сохранить богатство."
    bat "Но в эпитафии сплошные жуткие убийства и никаких подсказок."
    geo "Ну, на то это и загадка, головоломка."
    show geo smi with dissolve
    geo "Было бы странно, если бы она была простой и понятной."
    show geo std with dissolve
    mar "Угу."
    stop music fadeout 1.0
    bat "И всё же, смотри..."
    play sound flsh
    show letters filter
    with flash
    play music "sounds/music/bgm/The candles dance.mp3" fadein 1.0
    voice pm
    "Сейчас у вас [detective] очков детектива."
    voice pm
    "Вы заработали их выбирая те или иные варианты диалога в прошлом."
    voice pm
    "Эти очки будут использоваться в игре, для того, чтобы Баттлер мог построить какую либо сложную теорию или узнать что-то, скрытое от глаз остальных."
    voice pm
    "Их число может меняться как в большую сторону - так и в меньшую, как скрыто, вроде того, что происходило раньше, так и явно, когда в вариантах выбора будет отдельно указано, сколько очков вы потратите для его использования."
    voice pm
    "Теперь вы будете видеть их количество в правом углу экрана."
    show screen points with dissolve
    voice pm
    "Следите за ними и постарайтесь собрать побольше, ведь вся эта история - загадка, которую обязательно надо решить."
    voice pm
    "Так же в игре присутствуют диалоги, где при большом количестве очков детектива вы можете увидеть дополнительные реплики."
    voice pm
    "Следующий - как раз такой."
    stop music fadeout 3.0
    play sound shut
    hide letters
    with flash

    play music "sounds/music/bgm/Organ short #600 million in C minor.mp3" fadein 3.0
    bat "И, всё же, смотри..."

    $flag=0
    if(detective>0):
        $flag=1
        bat "В начале эпитафии есть небольшой кусочек, в котором описывается некоторая местность и, в котором говорится о \"ключе\"."
        bat "Однако позже следует фраза: {=lett}\n\"И если в руки тот ключ ты возьмешь,\n
        Свой путь вперед по правилам начнешь.\""
        show geo dou with dissolve
        geo "И что это значит?"
        bat "Ну, например, то, что если \"не взять ключ\", то ничего и не произойдёт..."
        show geo std with dissolve
        if(detective>5):
            $flag+=1
            bat "Далее начинаются убийства. И, более того..."
            bat "{=lett}\"Сумерки первые. Ключ отберет\n
            Шесть человек. Каждый жертвой падет.\""
            bat "А это вполне может быть указателем на то, что \"ключ\" - это что-то живое."
            show mar smi with dissolve
            mar "Ведьма, ведьма!"
            bat "Да нет. Даже если допустить, что ведьмы существуют..."
            mar "Существуют!"
            bat"...{i}допустить{/i}, что они существуют - Беатриче ведь мертва, разве нет?"
            show mar dou with dissolve
            mar "Воскреснет! В эпитафии же написано!"
            bat "В эпитафии написано, что воскреснет, если всё случится. А ключ в ней появляется куда раньше - стало быть не ведьма."
            $detective+=1
            show mar std
            show geo exc
            with dissolve
            geo "Но почему живое? Это ведь может быть и устройство, выбирающее что-то случайным образом и даже книга с инструкцией..."
            show bat exc with dissolve
            bat "Да... Об этом я как-то не подумал."
            show geo std
            show bat std
            with dissolve
            bat "Но, всё же, очевидно, что здесь не всё стоит понимать буквально."
            if(detective>10):
                $flag+=1
                bat "Смотрим дальше..."
                bat "Так, убийства... смерть в коленях... не сносить головы..."
                bat "..."
                bat "А, вот!"
                bat "{=lett}\"Свой путь к десятым сумеркам пройдешь,\n
                На землю золотую попадешь.\""
                show jes dou with dissolve
                jes "Значит ли это, что придётся \"выживать\" чтоб получить сокровища?"
                bat "Скорее уж наоборот, что просто \"выживать\" не получится."
                jes "Это ещё почему?"
                bat "Эти {=lett}золотые земли{=say_dialogue} вполне могут быть метафорой рая, загробного мира."
                bat "И ещё, потом сказано, что {=lett}\nТого, кто мудр, ведьма наградит.\n
                Сокровища она ему вручит."
                show jes std with dissolve
                bat "Стало быть, награду получит не сильнейший, а умнейший."
                show bat ace with vpunch
                bat "Тот, кто разгадает эпитафию!"
                show mar ace with vpunch
                mar "Мария разгадает!"
                show jes smi with dissolve
                jes "Вы такие забавные!"
    stop music fadeout 4.0
    voice pm
    "Так, за разгадыванием эпитафии пролетело время."

    show bat smi
    show jes std
    show geo std
    show mar std
    with dissolve
    play music "sounds/music/bgm/Witch's Room.mp3" fadein 5.0
    geo "Ладненько, пора бы собираться."
    bat "И то верно, еда-то давно кончилась."
    show jes smi with dissolve
    jes "Тебе лишь бы поесть!"
    show jes std with dissolve
    bat "Нет, ну а что? Это дело я люблю. Пошли в особняк, вдруг там что-то найдётся."
    show bat smi at offscreenright
    show jes std at offscreenright
    show geo std at offscreenright
    show mar std at offscreenright
    with move

    play bgs walk
    scene bg beach m at walking
    $ renpy.pause(1.5)
    show bg beach stairs at walking
    $ renpy.pause(1.5)
    show bg beach stairs up at walking
    $ renpy.pause(1.5)
    show bg beach stairs up1 at walking
    $ renpy.pause(1.5)
    show bg forest stairs mb at walking
    $ renpy.pause(1.5)
    show bg garden house1 m at center with dissolve
    stop bgs
    show geo std at offscreenleft
    show jes std at offscreenleft
    show bat smi at offscreenleft
    show mar std at offscreenleft
    $renpy.pause(0.5)
    show geo std at right2
    show jes std at right
    show bat smi at left
    show mar std at center
    with move
    $renpy.pause(0.5)

    with vpunch
    play sound "sounds/sound/s/Uuu~ Uuu~.wav"
    mar "Ууу! Ууу!"
    jes "Что случилось, Мария?"
    mar "Роза!"
    show rose_cg with dissolve
    jes "Действительно странная роза..."
    bat "Наверное, жуки постарались. Жалко."
    geo "Ну-ка, а если вот так..."
    show rose1_cg with fade
    geo "Теперь она особенная."
    mar "Угу!"
    show geo smi
    show mar smi
    hide rose_cg
    hide rose1_cg
    geo "Приглядывай за ней, пока мы не уедем. Вдруг сможем её вылечить."
    mar "Хорошо! Буду приглядывать!"
    show mar std with dissolve
    show bat smi at right1 with move
    bat "Джес, а Джордж всегда был таким?"
    jes "Каким?"
    bat "Ну, знаешь, собранным, умным, добрым..."
    show jes smi with dissolve
    jes "Нет конечно. Но людям свойственно взрослеть."
    jes "Один ты, как был в  семь лет балбесом - так и остался."
    show jes std with dissolve
    show bat exc with dissolve
    bat "Ну уж какой есть."
    show bat smi with dissolve
    geo "Ладненько, пошли в дом. Надо вещи разобрать, да и..."
    show geo emb with dissolve
    geo "Вещи надо помочь разобрать. Не правильно это, что Канон и Шанон за нас всё делают."
    mar "Точно! Вещи! Я же Сакутаро в сумке оставила, а вдруг он Шанон понравится и она его заберёт!"

    show jes std at offscreenright
    show geo std at offscreenright
    show mar std at offscreenright
    with move

    bat "Эй, Джес!"
    show jes at right with move
    jes "Чего?"
    show bat exc with dissolve
    bat "А какая из комнат моя? Особняк же громандный, а я тут сто лет не был."
    jes "Идём, я покажу."

    show jes std at offscreenright
    show bat smi at offscreenright
    with move
    play bgs walk
    scene bg mb entrance m at walking
    $ renpy.pause(1.5)
    stop bgs
    play bgs walkw
    show bg mb hall m at walking
    $ renpy.pause(1.5)
    show bg mb hall stairs m at walking
    $ renpy.pause(1.5)
    show bg mb hall stairs1 m at walking
    $ renpy.pause(1.5)
    show bg mb cor stairs m at walking
    $ renpy.pause(1.5)
    show bg mb cor1 at walking
    $ renpy.pause(1.5)
    stop bgs
    show kyr std at left
    show bg mb cor m at center
    with dissolve
    show bat smi at offscreenright
    show jes std at offscreenright
    jes "...и, вот, следующая комната - твоя."
    show bat smi at right3
    show jes std at right
    with move
    bat "Спасибо, что проводила."
    kyr "Баттлер..."
    show jes smi with dissolve
    jes "Здравствуйте, тётя Кириё."
    bat "Привет."
    show kyr smi with dissolve
    kyr "Я украду у тебя Баттлера на минутку?"
    show jes std with dissolve
    jes "Да я, собственно, вас оставлю. Баттлер просто попросил меня проводить его к комнате."
    show kyr std with dissolve
    kyr "Ну, теперь он в надёжных руках."
    jes "Ладно, тогда я пойду."
    show jes at offscreenright with move
    stop music fadeout 2.5
    bat "Всё в порядке?"
    kyr "Ну, как сказать..."
    play music "sounds/music/bgm/Love examination.mp3" fadein 1.0
    show bat std with dissolve
    bat "Расскажешь мне?"
    kyr "Да, конечно."
    kyr "После того как вы ушли мы перебрались в малую гостинную..."

    jump sc4
