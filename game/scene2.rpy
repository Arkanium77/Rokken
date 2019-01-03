#Сцена 2. Сад
label sc2:
    scene bg garden house1 m
    show geo std at offscreenright
    show jes std at offscreenright
    show bat smi at offscreenright
    show mar std at offscreenright

    show geo std at right4 with move
    show jes std at right2 with move
    show mar std at right3 with move
    show bat smi at right with move

    bat "Чую, чую запах вкусной еды!"
    show mar smi with dissolve
    mar "Еда, еда!"
    jes "Да ладно тебе, Баттлер. Не о том ты беспокоишься."
    show jes smi with dissolve
    show mar std with dissolve
    jes "Там ведь будет Шанон."
    #смущение
    show geo emb with dissolve
    geo "Шанон..."
    show hid std at offscreenleft
    show eva std at offscreenleft
    show hid std at left with move
    show eva std at left3 with move

    eva "Джордж, ты ничего не хочешь мне рассказать?"
    play sound flsh
    hide eva
    hide hid
    hide bat
    show letters filter
    show hid std at left
    show eva std at left3
    show bat smi at right
    with flash

    bat "Это тётя Ева и дядя Хидеёши - родители Джорджа."
    play sound shut
    hide letters filter
    hide mar
    hide bat
    show bat smi at right
    show mar std at right3
    with flash

    show geo exc with dissolve
    geo "Эээ... Нет?"
    show hid smi with dissolve
    hid "Да ладно тебе, Ева. Могут же у парня быть свои секреты."
    show hid std with dissolve
    jes "О, Канон!"

    #эффект перехода к сцене
    scene bg garden rose1 m with fade
    show kan std at right2
    kan "А?"
    play sound flsh
    hide kan
    show letters filter
    show kan std at right2
    with flash

    bat "Канон - прислуга."
    play sound shut
    hide letters filter
    show kan smi
    with flash

    kan "Доброе утро, госпожа Джессика."
    show kan std with dissolve
    show kan std at offscreenleft with move

    scene bg garden house1 m
    show geo std at right4
    show jes std at right2
    show bat smi at right
    show mar std at right3

    show hid std at left
    show eva std at left3
    with fade
    show jes sad with dissolve
    jes "К сожалению, Канон не очень разговорчив."
    bat "Пойдёмте скорее в дом! Я очень голоден!"
    #label p:
    play bgs walk
    scene bg mb entrance m at walking
    $ renpy.pause(1.5)
    scene bg mb hall m
    stop bgs
    show geo std at right4
    show jes std at right2
    show bat smi at right
    show mar std at right3


    bat "Эх, давненько я тут не был!"
    play sound flsh
    show letters filter
    hide bat
    show bat std at right
    with flash

    bat "Пожалуй, с тех самых пор как отец развёлся с мамой..."
    play sound shut
    hide letters filter
    hide mar
    show bat smi at right
    show mar std at right3
    with flash

    stop music fadeout 1.5
    bat "А... Что это за портрет? Раньше он здесь не висел."
    play sound flsh
    scene bg mb hall portrait with flash
    $renpy.pause(0.2,hard=True)
    play sound flsh
    scene bg mb portrait m with flash
    $renpy.pause(0.2,hard=True)
    play sound flsh
    scene bg mb portrait1 m with flash
    play music "sounds/music/bgm/Witch in gold.mp3"
    $renpy.pause(1,hard=True)

    geo "В прошлый раз когда семья собиралась его ещё не было..."
    jes "Дедушка совсем недавно его повесил. И ещё один такой же в его кабинете."
    #show mar smi at right3 with dissolve
    mar "А Мария знает, кто это! Это Беатриче."
    #show geo smi at right4 with dissolve
    geo "А, золотая ведьма Беатриче..."
    hide bat
    play sound flsh
    show letters filter with flash


    show bat std at offscreenright
    show bat std at right with move
    stop music fadeout 1.5
    bat "Позвольте, я немного расскажу вам о дедушке."
    play music "sounds/music/bgm/Witch in a Bottle.mp3" fadein 2
    #play music "sounds/music/bgm/Witch in gold.mp3"
    scene bg mb cab rev s
    play sound shut
    show kin ystd at left2
    show letters filter
    show bat std at right
    with flash

    bat "Кинзо Уширомия - глава семьи Уширомия. Тогда, в конце XIX начале XX века семья Уширомия владела несколькими прядильными и консервными заводами."
    bat "Свою империю дедушка строил в одиночку, без какой-либо помощи или ссуд."
    show bat smi with dissolve
    bat "И, стоит отметить, у него это неплохо получалось."
    show bat std with dissolve
    bat "Тогда, в 1923 году дедушкина компания была на подъёме."
    bat "Но первого сентября произошло великое землятрясение Канто."
    play sound "sounds/sound/s/earthquake.mp3"
    show kin ysad with vpunch
    bat "Оно разрушило всё, что строил дедушка. Да и людей много погибло..."
    bat "Тогда дедушка поклялся вернуть семье былое богатство и статус."
    bat "Никому доподлинно неизвестно, что произошло, но остатки средств, острый ум и, возможно, везение помогли дедушке вернуть и преумножить богатства семьи Уширомия."
    show bat smi with dissolve
    play sound shut
    show kin std with flash
    bat "Великий человек."
    show bat std with dissolve
    bat "Однако существует легенда..."
    show kin ace with dissolve
    bat "Она гласит, что дедушка обратился к тёмной магии и призвал ведьму себе в помощь."
    show kin smi with dissolve
    bat "По условиям контракта ведьма одолжила дедушке двадцать миллиардов йен в золоте."
    bat "И именно это золото помогло семье Уширомия стать теми, кем мы являемся сейчас."
    bat "Так же Кумасава когда-то рассказывала, что дедушка влюбился в ведьму и поселил её на острове."
    $renpy.pause(2)
    stop music fadeout 1.5
    #label p:
    play music "sounds/music/bgm/Witch in gold.mp3" fadein 3

    scene bg mb portrait m
    play sound flsh
    show geo std at right5
    show jes std at right4
    show bat smi at right
    show mar std at right3
    with flash

    bat "Ведьма значит..."
    show mar smi with dissolve
    mar "Ведьма-ведьма! Она всё магией может!"
    mar "Создать золото из ничего, починить сломанное, найти пропав..."
    play sound "sounds/sound/s/tapestop.mp3"
    stop music
    show bat smi_e with dissolve


    bat "Как жаль, что ведьм не бывает."
    play music "sounds/music/bgm/Fishy Aroma.mp3"
    bat "Просто глупые сказки."
    show mar sad with dissolve
    mar "Ведьмы бывают... уууу..."
    show jes ang with dissolve
    jes "Дурак! Не расстраивай ребёнка!"
    play sound "sounds/sound/s/punchse.mp3"
    show bat ang with vpunch
    bat "Ау. Больно же."
    jes "Живо извинись."
    show bat exc with dissolve
    stop music fadeout 3
    bat "А... Мария, прости. Конечно ведьмы бывают. Просто ляпнул не подумав..."
    show mar std
    show jes std
    with dissolve
    play music "sounds/music/bgm/Witch in gold.mp3"
    mar "Ты правда веришь в ведьм?"
    bat "Н-ну конечно!"
    show mar smi with dissolve
    mar "Здорово! Значит мы можем все вместе разгадать эпитафию ведьмы!"
    show bat std with dissolve
    bat "Эпитафию..?"
    show mar smi at left2 with move
    mar "Вот же. На табличке написано."

    show mar std with dissolve
    show bat std at left with move
    bat "Хм. Действительно, эпитафия..."
    #define config.nvl_list_length = 4

    voice pm
    letters "
Свой город помню я родной\n
С богатой рыбою рекой.\n
Коль хочешь земли золота найти,\n
Иди себе вдоль речки, ключ ищи.\n\n

И вот, как по течению пройдешь,\n
В печальную деревню попадешь.\n
Двое расскажут про берег такой,\n
Где дремлет ключ к той земле золотой.\n\n

И если в руки тот ключ ты возьмешь,\n
Свой путь вперед по правилам начнешь.\n
Сумерки первые. Ключ отберет\n
Шесть человек. Каждый жертвой падет.\n\n

Вторые сумерки когда наступают,\n
Живые ближайших двоих разрывают.\n
Сумерки третьи настанут, и вот\n
Имя мое всяк живой вознесет.\n\n"

    nvl clear
    voice pm
    letters "
Четвертые сумерки. Не сносить головы!\n
Пятые. Гибель приходит от раны в груди.\n
Шестые. Смерть разрывает живот.\n
Седьмые - в коленях костлявая ждет.\n\n

Восьмые сумерки что нам принесут?\n
Ноги из жизни легко унесут.\n
Когда же сумерки девятые придут,\n
Воскреснет ведьма, остальные все умрут.\n\n

Свой путь к десятым сумеркам пройдешь,\n
На землю золотую попадешь.\n
Того, кто мудр, ведьма наградит.\n
Сокровища она ему вручит.\n\n

Все золото земли той можешь получить,\n
Иль мёртвых всех из праха воскресить\n
Любовь утраченную возвратить\n
И ведьму в сон на века погрузить.\n\n"
    nvl clear
    voice pm
    letters "\n\n
Спи, Беатриче, моя дорогая.\n
Ведьма любимая. Золотая.\n"
    hide nvl
    nvl clear

    show bat dou with dissolve
    bat "Странная она какая-то..."
    hide nvl
    nvl clear
    play sound "sounds/sound/s/Auuu~.wav"
    mar "Это ключ, ключ!"
    geo "Ключ к чему?"
    mar "Это ключ к золоту Беатриче!"
    geo "А, это те самые двадцать миллиардов йен..."
    jes "Было бы неплохо их найти."
    stop music fadeout 2.0
    show bat smi with dissolve
    play music "sounds/music/bgm/Home.mp3" fadein 2.0
    bat "Этим мы займемся после обеда."
    show sha std at offscreenright
    sha "Господин Баттлер, если вам так не терпится..."
    show sha std at right with move
    sha "То вы можете пройти в столовую прямо сейчас."
    show sha smi with dissolve
    sha "Гоуда подаст обед с минуты на минуту."
    hide bat
    hide sha
    play sound flsh
    show letters filter
    show bat std at left
    show sha smi at right
    with flash

    bat "Шанон - прислуга. Сестра-близнец Канона."
    play sound shut
    hide letters
    hide bat
    hide mar
    show bat smi at left
    show mar std at left2
    with flash

    show geo emb1 with dissolve
    geo "Шанон."
    show geo emb1 at left1 with move
    show sha emb with dissolve
    sha "Здравствуйте, господин Джордж."
    sha "Проходите в столовую, прошу."


    #label p:
    scene bg mb dining
    show goh std at offscreenleft
    show bat std at left
    show rud std at right1
    show kyr std at right
    show kla std at right4
    show nat std at right5
    with fade
    show kyr smi with dissolve
    kyr "... Когда там открывается твой отель, Клаус?"

    show rud smi with dissolve
    rud "Нас-то позовешь на открытие?"
    play sound flsh
    show letters filter
    hide bat
    hide kla
    hide nat
    show bat smi at left
    show kla std at right4
    show nat std at right5
    with flash

    bat "Это тётя Натсухи и дядя Клаус - родители Джессики."
    play sound shut
    hide letters filter
    with flash

    show kla dou with dissolve
    kla "Видишь ли, братец..."
    show kyr std with dissolve
    show goh std at left2 with move
    goh "Обед готов!"
    play sound flsh
    show letters filter
    hide bat
    hide goh
    show goh std at left2
    show bat smi at left
    with flash

    bat "Гоуда - шеф-повар."
    stop music fadeout 2
    play sound shut
    hide letters filter
    hide bat
    hide goh
    hide nat
    show goh std at left2
    show bat smi at left
    show nat std at right5
    with flash

    show kla std with dissolve
    kla "Поговорим после ужина."
    play music "sounds/music/bgm/Waltz Op. 34.mp3" fadein 1.0
    show rud smi with dissolve
    rud "Поговорим, обязательно поговорим."
    show rud std with dissolve
    hide bat
    play sound flsh
    show letters filter
    show bat smi at left
    with flash


    $men=[]

    bat "Во время семейных обедов происходит много интересного."
    bat "Даже, казалось бы, незначительная фраза может открыть вам самые глубокие тайны семейства."
    bat "И так..."

    menu:
        bat "Кому я должен уделить внимание?"
        "Рудольф и Кириё"  if not "l" in men:
            jump din1
        "Клаус и Натсухи"  if not "h" in men:
            jump din2
        "Ева и Хидеёши"  if not "m" in men:
            jump din3
        "Тётя Роза"  if not "r" in men:
            jump din4

    label dinS:
    menu:
        bat "Я могу поговорить с кем-то ещё."
        "Рудольф и Кириё"  if not "l" in men:
            jump din1
        "Клаус и Натсухи"  if not "h" in men:
            jump din2
        "Ева и Хидеёши"  if not "m" in men:
            jump din3
        "Тётя Роза"  if not "r" in men:
            jump din4

    label din1:
        $ men.append("l")
        # блокируем перемотку назад к выбору
        $ renpy.block_rollback()
        play sound shut
        scene bg mb dining rev m
        show bat smi at left
        show rud std at right3
        show kyr std at right
        with flash

        bat "Отец, а что там с отелем?"
        rud "Ну, понимаешь, нам: мне, Еве, Розе - кажется, что Клаус, пользуясь своим положением, расстрачивает отцовские деньги, часть из которых принадлежит нам всем."
        menu:
            bat "Возможно..."
            "У вас есть доказательства?":
                python:
                    detective+=1
                    h+=1
                    m+=1
                    l+=1
                    r+=1
                    s+=1
                #bat "Тут изменилось количество очков детектива. Сейчас их [detective]"
                bat "Есть ли у вас какие-то доказательства?"
                rud "Да, мы кое-что нашли."
                show rud dou with dissolve
                rud "Но, к сожалению, недостаточно."
                rud "Мы не сможем предъявить ему никаких обвинений."
                rud "Все мы в той или иной мере пользуемся отцовскими деньгами."
                show rud exc with dissolve
                rud "Но он тратит куда больше, чем все мы."
                menu:
                    "Он же наследник.":
                        python:
                            h+=3
                            l-=3
                        bat "В конце концов он наследник."
                        show rud ang with dissolve
                        rud "Сын, я тебя не понимаю!"
                        rud "Ты придерживаешься его стороны?!"
                        bat "Я просто хочу разобраться в этом деле."
                        bat "Ведь раз он наследник, то и дедушкиных денег ему достанется больше..."
                        show rud exc1 with dissolve
                        rud "Верно, пятьдесят процентов. В то время как мы поделим оставшееся поровну."
                        bat "Так что..."
                        rud "Не стоит. Я понял, что ты имел в виду."
                        show rud dou with dissolve
                        rud "Может быть ты и прав."
                        $l+=1
                        show rud std with dissolve
                        jump dinI
                    "Понимаю, понимаю...":
                        python:
                            h-=3
                            l+=3
                        bat "Да, я понимаю тебя."
                        show rud smi with dissolve
                        rud "Я рад, что мы сошлись во мнениях."
                        rud "Мы не хотим обобрать собственного брата. Лишь добиться справедливости."
                        show rud std with dissolve
                        jump dinI

            "Отель может принести гораздо большую прибыль.":
                python:
                    h+=3
                    l-=3
                    detective+=1
                bat "Но, отец, отель может принести гораздо большую прибыль."
                show rud ang with dissolve
                rud "А где гарантии?!"
                rud "Кто может гарантировать, что деньги не будут потрачены на что-то другое?"
                rud "Или что бизнес не прогорит?"
                show rud exc1 with dissolve
                rud "Откуда нам знать, что все будет хорошо?"
                bat "Ты переживаешь за свою часть?"
                show rud ang with dissolve
                rud "Конечно, черт возьми, переживаю!"
                menu:
                    "Тебе нужно больше доверять брату.":
                        python:
                            h+=1
                            detective+=2
                        bat "Думаю, тебе нужно больше доверять своему брату."
                        rud "Вздор!"
                        show rud std with dissolve
                        rud "Запомни, доверять нужно только себе!"
                        show bat std with dissolve
                        bat "Я понимаю тебя, но не могу с тобой согласиться."
                        jump dinI

                    "Понимаю, понимаю...":
                        python:
                            h-=3
                            l+=3
                        bat "Да, я понимаю тебя."
                        show rud smi with dissolve
                        rud "Я рад, что мы сошлись во мнениях."
                        rud "Мы ведь не хотим обобрать собственного брата. Лишь добиться справедливости."
                        show rud std with dissolve
                        jump dinI

            "Он, действительно, что-то скрывает.":
                python:
                    h-=3
                    l+=3
                bat "Давненько я не видел дядю Клауса... Однако, он действительно выглядит подозрительно."
                show kyr smi with dissolve
                kyr "И почему же тебе так кажется?"
                show bat smi with dissolve
                bat "Он же как иллюстрация ко всему, что ты мне рассказывала."
                bat "Отвечает не сразу, юлит, даже своё лицо не может удержать спокойным."
                show kyr std
                show rud smi
                show bat std
                with dissolve
                rud "Да уж! Клаус никогда не отличался спокойным нравом."
                menu:
                    "Как и любой из вас.":
                        python:
                            h+=2
                            l+=2
                            detective+=2
                        bat "Как и ты, и тётя Роза, и тётя Ева."
                        show bat smi with dissolve
                        bat "Видно, семейная черта."
                        show rud exc with dissolve
                        rud "Ложь!"
                        show kyr smi with dissolve
                        kyr "Что правда, то правда."
                        kyr "Видимо, все в отца пошли."
                        jump dinI

                    "И как он ещё управляет компанией, не умея скрывать эмоции?":
                        python:
                            h-=1
                            l-=1
                        bat "И как он ещё управляет компанией, настолько неумело скрывая свои эмоции?"
                        show kyr dou1 with dissolve
                        kyr "А ты не задумывался над тем, что он только в кругу семьи такой?"
                        bat "Возможно."
                        bat "Но почему?"
                        show kyr std with dissolve
                        kyr "Может он просто нам доверяет?"
                        show bat smi with dissolve
                        bat "Может быть."
                        jump dinI



    label din2:
        $ men.append("h")
        # блокируем перемотку назад к выбору
        $ renpy.block_rollback()
        play sound shut
        scene bg mb dining rev m
        show bat smi at left
        show kla std at right3
        show nat std at right
        with flash


        bat "Дядя Клаус, что там с отелем?"
        bat "Как у вас обстоят дела с ним?"
        kla "О, Баттлер. Как добрался?"
        show kla smi with dissolve
        kla "С отелем все прекрасно, он строится."
        show kla std with dissolve
        menu:
            "Расскажите про конфликт в семье.":
                python:
                    detective+=1
                bat "А что за конфликт в семье?"
                bat "Я слышал, что это как-то связано с отелем."
                show kla exc1 with dissolve
                kla "Ааа, это..."
                show kla smi with dissolve
                kla "Всё в порядке. Просто небольшие недопонимания."
                bat "Расскажите. Вдруг я смогу чем-то помочь."
                show kla exc with dissolve
                kla "Эх, ладно."
                show kla sad with dissolve
                kla "На самом деле, твой отец, Ева и Роза не хотят поддержать меня с отелем."
                kla "Они считают, что я просто потрачу все деньги, а мой бизнес в итоге прогорит."
                menu:
                    "Может у них есть повод так считать?":
                        python:
                            h-=1
                            l+=1
                            m+=1
                            r-=1
                        show bat std with dissolve
                        bat "А вы не думали, что у них есть повод так считать?"
                        show kla ang with dissolve
                        kla "Да какой повод?!"
                        kla "Мой бизнес постепенно приносит плоды."
                        show kla exc with dissolve
                        kla "Да, он требует каких-то вложений, но все же..."
                        show kla ace with dissolve #vpunch
                        kla "Я уверен, он будет приносить прибыль! И вы все это увидите."
                        bat "Возможно это и так. Тогда попробуйте убедить в этом остальных."
                        bat "Думаю, что вам нужно привести убедительные доводы и все."
                        show kla std with dissolve
                        kla "Возможно, ты прав."
                        jump dinI

                    "Я не согласен с мнением остальных.":
                        python:
                            h+=3
                            l-=3
                            m-=1
                            r+=1
                        show bat dou with dissolve
                        bat "Возможно, вам покажется это странным, но я не согласен с мнением моего отца и остальных."
                        bat "Я думаю, что вы должны стоять на своем."
                        show kla smi with dissolve
                        kla "А ты не так плох, как кажется."
                        kla "Умеешь распознать правильную сторону."
                        nat "Баттлер, а почему же ты не согласен с отцом?"
                        show bat std with dissolve
                        bat "Отель - это прибыльный бизнес."
                        bat "Когда вы его достроите, то ваши доходы увеличатся."
                        bat "А значит, вы сможете вернуть те деньги, которые брали для строительства."
                        bat "Все должны быть довольны."
                        kla "Ха, а в твоей голове что-то есть."
                        show kla dou with dissolve
                        kla "Посмотрим чем это закончится в итоге."
                        jump dinI

            "Вы хотите поделить наследство дедушки?":
                python:
                    detective+=2
                bat "Я слышал, что старшее поколение хочет поделить наследство дедушки."
                bat "Как мне кажется, вы не очень-то за."
                show nat ang with dissolve
                nat "Они просто хотят забрать все себе!"
                nat "У остальных начались проблемы с делами. Им необходимы сейчас дополнительные вложения."
                menu:
                    "Только это является причиной?":
                        python:
                            h+=1
                            l+=1
                            m+=1
                            r+=1
                            detective+=2
                        bat "Только по этой причине вы против?"
                        show kla exc1
                        show nat std
                        with dissolve
                        kla "Если честно, то нет..."
                        show kla exc with dissolve
                        kla "Ты знаешь, что я строю отель."
                        kla "Мне необходимы отцовские деньги, чтобы строительство не остановилось."
                        bat "Почему вы это не объясните всем остальным?"
                        kla "Эх, Баттлер. Это сложно..."
                        kla "В этой семье каждый сам за себя."
                        kla "Никто не станет помогать просто так."
                        kla "Всегда приходится рассчитывать только на свои силы."
                        show kla sad with dissolve
                        kla "Если сейчас прекратятся вложения, то мой бизнес рухнет."
                        show bat std with dissolve
                        bat "Однако остальным кажется, что вы просто хотите присвоить всё себе."
                        show kla exc1 with dissolve
                        kla "Боюсь, меня не так поняли..."
                        show kla exc with dissolve
                        kla "Стоит еще раз поговорить с остальными."
                        jump dinI

                    "Но раздел наследства все равно произойдет.":
                        python:
                            h-=2
                            l+=2
                            m+=2
                            detective+=1
                        bat "Вы же понимаете, что раздел наследства рано или поздно произойдет."
                        show kla exc1
                        show nat ang
                        with dissolve
                        kla "Да, мы это понимаем."
                        kla "Но не сейчас."
                        kla "Я знаю почему всем остальным так нужны деньги отца."
                        bat "Почему?"
                        show kla exc with dissolve
                        kla "Как говорила Натсухи, у всех остальных появились проблемы в делах."
                        kla "Именно по этой причине все хотят поделить наследство."
                        bat "В конечном итоге, это всем принесет прибыль..."
                        bat "Тогда почему вы против?"
                        show kla exc1 with dissolve
                        kla "Не все так просто..."
                        kla "Боюсь, им не помогут отцовские деньги."
                        kla "Они, можно сказать, выкинут их на ветер."
                        show bat dou with dissolve
                        bat "Не соглашусь с вами..."
                        show bat std with dissolve
                        bat "Вы не знаете, что у них происходит."
                        bat "Поэтому и не вам судить."
                        jump dinI

            "А что там с золотом Беатриче?":
                python:
                    detective+=2
                bat "Расскажите про золото Беатриче."
                show kla dou with dissolve
                kla "Ааа, это..."
                show kla std with dissolve
                kla "Отец разместил в холле портрет Беатриче."
                kla "Насколько я знаю, еще один портрет висит у него в кабинете."
                bat "Зачем он это сделал?"
                kla "Ты же сам знаешь про существование легенды. Отец верит в Беатриче."
                menu:
                    "А зачем нужна эпитафия?":
                        python:
                            detective+=3
                        show bat dou with dissolve
                        bat "К чему тогда эта эпитафия?"
                        bat "Может вы подробнее поясните это мне?"
                        show kla smi with dissolve
                        kla "Отец говорил, что это ключ к золоту Беатриче."
                        kla "Когда-то ведьма Беатриче одолжила отцу приличную сумму денег."
                        kla "Однако по долгам нужно платить."
                        show bat std with dissolve
                        bat "Как?"
                        show kla std with dissolve
                        kla "В эпитафии сказано, что Беатриче забирает в качестве платы всё, что принадлежит семье Уширомия."
                        kla "Но отец поставил ведьме условие, которое позволит оставить ведьму ни с чем."
                        show kla smi with dissolve
                        kla "Тем не менее, это все глупые сказки."
                        kla "Или ты веришь в это?"
                        show bat ace1 with dissolve
                        bat "Нет."
                        bat "Я твердо убежден, что ведьм не бывает!"
                        jump dinI

                    "Все это глупости.":
                        python:
                            detective-=3
                        show bat ace1 with dissolve
                        bat "Все это сказки!"
                        bat "Ведьм не бывает!"
                        show kla tau
                        show bat std
                        with dissolve
                        kla "Может и так."
                        show kla std with dissolve
                        kla "Однако в каждой легенде есть доля правды."
                        kla "Деньги ведь не могли появиться из ниоткуда."
                        kla "Особенно в таком количестве."
                        show bat ace1 with dissolve
                        bat "Все равно, ведьм не бывает."
                        show kla tau with dissolve
                        kla "Хорошо, пусть каждый останется при своем мнении."
                        jump dinI

    label din3:
        $ men.append("m")
        # блокируем перемотку назад к выбору
        $ renpy.block_rollback()
        play sound shut
        scene bg mb dining rev m
        show bat smi at left
        show hid std at right3
        show eva std at right
        with flash

        eva "Баттлер..."
        show bat exc with dissolve
        bat "Да, тётя Ева?"
        eva "О чём вы там говорили в саду?"
        eva "Про Шанон и Джорджа."
        menu:
            bat "Надо что-то ответить!"
            "Да так, ничего такого.":
                $detective+=1
                bat "Да так, ничего такого."
                bat "Шутили, веселились."
                show bat exc with dissolve
                bat "Я, например, очень хотел есть."
                show hid smi with dissolve
                hid "Наш человек!"
                bat "Вот и зашёл разговор о Шанон. Ничего такого."
                show bat smi with dissolve
                show eva dou with dissolve
                show hid std with dissolve
                eva "Да? А мене показалось, что я видела совсем другую сцену."
                menu:
                    "Вам просто показалось.":
                        python:
                            m+=1
                            detective+=1
                        show bat std with dissolve
                        bat "Вам просто показалось."
                        eva "Но я же своими глазами видела как он по..."
                        hid "Ева!"
                        show hid ang with dissolve
                        hid "Вам обоим явно следует вести себя потише."
                        show bat sad
                        show eva sad
                        with dissolve
                        eva "Ох, да, дорогой."
                        eva "Действительно, что-то мы раскричались."
                        bat "Простите."
                        show hid std with dissolve
                        bat "Я уверен, вы поняли, что я имел в виду."

                        show eva std with dissolve
                        eva "Да ладно, что уж там."
                        show bat std with dissolve
                        eva "Баттлер, не передашь мне ещё немного буйабеса?"
                        jump dinI

                    "А даже если и так, то какое вам дело?":
                        python:
                            m+=2
                            detective+=1
                        bat "А даже если и другую."
                        show bat std with dissolve
                        bat "Вам не кажется, что Джордж уже не маленький ребёнок?"
                        bat "Вам стоит дать ему немного больше свободы."
                        show eva ang with dissolve
                        eva "Больше свободы?! Да я что только не делаю для Джорджа!"
                        eva "Он самостоятельный, он учится в лучшей академии Токио, он..."
                        bat "Именно поэтому вам и стоит чуть больше ему доверять."
                        #show hid std with dissolve
                        hid "Ева, действительно. Хватит."
                        show eva dou with dissolve
                        eva "Но..."
                        hid "Я тоже считаю, что Джордж вполне способен и сам определить, что лучше для него."
                        show hid smi with dissolve
                        hid "А ты не промах! Не испугался её."
                        show eva smi with dissolve
                        eva "Ну хватит! Делаешь из меня какую-то ужасную фурию."
                        jump dinI

            "Ну... Понимаете, это немного сложно объяснить...":
                bat "Ну... Понимаете, это немного сложно объяснить..."
                show eva smi with dissolve
                eva "Ну же, Баттлер, я не кусаюсь."
                eva "Поверь, мы желаем Джорджу только добра."
                hid "Что бы там ни было, мы верим Джорджу."
                menu:
                    "Думаю, сложно не заметить, что Джордж и Шанон...":
                        python:
                            m-=1
                            detective-=1
                        show bat exc with dissolve
                        bat "Думаю, сложно было не заметить, что Джордж и Шанон..."
                        bat "Ну..."
                        bat "Неровно дышат друг к другу."
                        show eva dou with dissolve
                        eva "Я, конечно, предполагала что-то подобное..."
                        show eva ang with dissolve
                        eva "Но Шанон!"
                        eva "Простая служанка!"
                        eva "Почему?! Он же учится в лучшей академии Токио!"
                        eva "Ему уж точно было из чего выбирать!"
                        show hid smi with dissolve
                        hid "Так ведь сердцу не прикажешь, Ева."
                        show bat smi with dissolve
                        hid "Вспомни как мы сами познакомились."
                        show eva dou with dissolve
                        eva "Н-но мы - это совсем другое дело..."
                        hid "Ты и в правду так думаешь?"
                        hid "Вспомни-вспомни."
                        show eva smi with dissolve
                        eva "А может быть ты и прав..."
                        jump dinI

                    "А раз верите, то, может быть, у него и спросите?":
                        python:
                            m+=1
                            detective+=1
                        show bat std with dissolve
                        bat "А раз верите, то, может быть, у него и спросите?"
                        bat "В конце-концов Джордж далеко не ребёнок."
                        show bat exc with dissolve
                        bat "Иногда рядом с ним мне кажется, что я не на два года младше него, а на все десять."
                        show eva dou with dissolve
                        eva "Н-но..."
                        show hid smi with dissolve
                        hid "А мне кажется, что он прав. Я бы и спрашивать не стал."
                        hid "Я уверен, Джордж прекрасно знает, что для него лучше."
                        show hid std with dissolve
                        hid "Он ведь куда умнее и рассудительнее сверстниуов, ты же знаешь."
                        show eva smi with dissolve
                        eva "Да, Джордж он такой..."
                        jump dinI

            "Мы просто шутили. Джорджу ведь нравится Шанон.":
                python:
                    m-=3
                    detective-=1
                show bat exc with dissolve
                bat "Мы просто шутили. Джорджу ведь нравится Шанон."
                show eva ang with vpunch
                eva "ЧТО?"
                show bat std
                show hid ang
                with dissolve
                hid "Ева!"
                show hid std with dissolve
                eva "Что значит \"Нравится Шанон\"?"
                eva "В каком это смысле?"
                eva "Она же служанка! Вещь!"
                hid "Ева! Успокойся."
                eva "Успокоиться?! Да как можно? Необразованная служанка! Вещь!"
                eva "А ведь мог бы выбрать себе невестой умницу и красавицу Хелен!"
                eva "Или Тисэ. Она может обладает и не лучшим характером, зато является единственной наследницей конгломерата Умэномори "

                menu:
                    "Может быть, не стоит называть Шанон \"вещью\"?":
                        python:
                            m-=1
                            detective+=3
                        show bat exc with dissolve
                        bat "Тётя Ева, может быть вам не стоит называть Шанон \"вещью\"?"
                        show eva with vpunch #ПРОВЕРКА
                        eva "Да ты просто не понимаешь ничего!"
                        show bat std with dissolve
                        bat "Так объясните мне. Только спокойно."
                        show eva std with dissolve
                        eva "Видишь ли Баттлер... О семье Уширомия ходит много легенд."
                        eva "Например, легенда о золотой ведьме."
                        bat "Да, мы сегодня её вспоминали."
                        eva "Так вот, кроме сказок про золото, по легенде, Беатриче стала советником семьи Уширомия по алхимии и чёрной магии."
                        eva "Не знаю уж, про что именно отец с ней советовался, но именно он начал называть слуг, принадлежащих семье Уширомия вещами."
                        eva "Тем самым он дал им и право носить однокрылого орла на одежде, как у членов семьи, ведь \"Вещи принадлежат семье. А значит и метка об этом говорящая должна быть\"."
                        show eva smi with dissolve
                        eva "А слово Главы Семейства - закон. Даже если многие об этом забыли."
                        show bat dou with dissolve
                        bat "Не нравятся мне эти сказки про ведьм..."
                        jump dinI

                    "Я гляжу жизнь Джорджа уже распланирована.":
                        python:
                            m+=1
                            detective+=2
                        show bat std with dissolve
                        bat "Я гляжу жизнь Джорджа распланирована на много лет вперёд."
                        show bat smi_e with dissolve
                        bat "Может вы уже и пару для его детей придумали?"
                        show eva std with dissolve
                        eva "Ну, это зависит от пола, конечно. Если родится девочка, то семья Тса..."
                        show eva dou with dissolve
                        eva "Не важно."
                        eva "В любом случае, партия с любой девицей из академии была бы выгоднее..."
                        show hid smi with dissolve
                        hid "Ловко он тебя поймал, а, Ева?"
                        show bat smi
                        show hid std
                        with dissolve
                        hid "Я всегда говорил, что тебе стоит чуть меньше думать за других людей."
                        show hid smi with dissolve
                        hid "В конце концов они ведь всё равно сделают по своему. Имеют право."
                        show eva sad with dissolve
                        eva "Но я же хочу как лучше..."
                        show hid std with dissolve
                        hid "Как и я. Мы все хотим для Джорджа только лучшего."
                        hid "Именно поэтому нам стоит прислушиваться к его мнению. Он ведь у нас молодец."
                        show eva std with dissolve
                        eva "Да, Джордж молодец..."
                        jump dinI


    label din4:
        $ men.append("r")
        # блокируем перемотку назад к выбору
        $ renpy.block_rollback()
        play sound shut
        scene bg mb dining rev m
        show bat smi at left
        show ros std at right3
        with flash

        bat "Тётя Роза, а расскажите подробнее про эту ведьму?"
        show ros exc1 with dissolve
        ros "А? Какую ведьму?"
        show bat dou with dissolve
        bat "Ну, Беатриче, золотая ведьма..."
        bat "Мария рассказывала. Ну, не сама же она это придумала..."
        show ros exc with dissolve
        ros "Понимаешь... Мария очень восприимчива."
        ros "Наслушалась рассказов вашего дедушки и верит в них."
        ros "У нас весь дом книжками про магию завален. Я, конечно, стараюсь её не ограничивать лишний раз, но..."
        ros "Иногда это очень и очень страшные сказки."
        #bat "Да, что есть, то есть... И эпитафия эта..."
        menu:
            "Разве стоит давать читать такие сказки ребёнку?":
                python:
                    r+=1
                    detective+=1
                show bat std with dissolve
                bat "Да, сказки, и эпитафия эта, действительно, страшные. Разве стоит давать их читать ребёнку?"
                ros "Ну, что сделано - то сделано."
                show ros std with dissolve
                ros "Ты пойми, Мария умная, куда умнее своих сверстников."
                show ros sad with dissolve
                ros "Просто она...  Немного другая."
                menu:
                    "Да я ведь не спорю, умная.":
                        python:
                            r+=3
                        show bat smi with dissolve
                        bat "Да я ведь не спорю, умная."
                        show ros std with dissolve
                        bat "Вон, и книжки читает."
                        show bat exc with dissolve
                        bat "Я в её возрасте больше с друзьями бегал. Уж точно глупее был."
                        ros "Я в тебе не сомневалась."
                        show bat smi_e with dissolve
                        bat "Что значит - не сомневались, тётя Роза?"
                        show ros smi with dissolve
                        ros "Ничего, ничего."
                        show ros std
                        show bat smi
                        with dissolve
                        ros "И, всё же..."
                        ros "Я бы хотела чтобы она бегала с друзьями."
                        show ros sad with dissolve
                        ros "Чтобы у неё были друзья."
                        ros "Я ведь работаю много, не могу ей достаточно времени уделять..."
                        jump dinI


                    "Но, всё же, надо с этим что-то делать.":
                        python:
                            r-=1
                            detective+=1
                        bat "Но, всё же, надо с этим что-то делать."
                        bat "Дети ведь всегда боятся чего-то странного, а ведь..."
                        show ros ang with dissolve
                        ros "Мария не странная!"
                        show ros exc with dissolve
                        ros "Но в чём-то ты прав. Друзей у неё, действительно, нет..."
                        ros "Я ведь работаю много, не могу ей достаточно времени уделять."

                        bat "Так разве работа - важнее ребёнка?"
                        show ros ang with dissolve
                        ros "Не важнее. Но это ведь всё ради неё!"
                        ros "Чтоб она ни в чём не нуждалась!"

                        bat "Так ведь семья Уширомия - одна из богатейших семей Японии."
                        bat "Разве не можем мы как-то помочь?"
                        show ros std with dissolve
                        ros "Эх, ничего ты не знаешь, Баттлер"
                        ros "Ты на семейных собраниях уже двенадцать лет не был."
                        ros "И видно, хорошим человеком вырос."
                        ros "Но эта семья - другое дело."
                        ros "Никто здесь не поможет \"просто так\". И рассчитывать всегда приходится только на себя."
                        show bat sad with dissolve
                        ros "Так что позволь нам решать свои проблемы самим. Тут так принято."
                        ros "Да и сделать ты ничего не с этим не сможешь."
                        jump dinI

            "И всё же, может быть вы можете что-то рассказать про ведьму и эпитафию?":
                python:
                    detective+=2
                show bat std with dissolve
                bat "И всё же, может быть вы можете что-то рассказать про ведьму и эпитафию?"
                show ros std with dissolve
                ros "На самом деле, я могу рассказать не больше, чем Ева."
                show ros smi with dissolve
                ros "Если у кого и спрашивать про ведьм - так это у Марии."
                bat "Но, всё-таки..."
                show ros std with dissolve
                ros "По легенде Беатриче - ведьма, с которой Кинзо заключил контракт."
                ros "Подробностями я никогда не интересовалась, но, когда мы были детьми, ходили слухи, что на острове, действительно, живёт одна женщина."
                ros "Так что ведьма или нет, но когда-то Беатриче жила на этом острове."
                ros "Впрочем, когда я уехала с острова чтобы поступить в университет - уже никто и ничего про неё не говорил."
                ros "Может быть умерла, может быть ей надоело жить на далёком от цивилизации острове."
                menu:
                    "Значит... Беатриче - всего лишь человек?":
                        python:
                            r+=1
                            l+=1
                            detective+=1
                        ros "Значит... Беатриче - всего лишь человек?"
                        ros "Кто знает. Я, конечно, не верю в ведьм, но ваш дедушка - умный и рациональный человек."
                        ros "И он по сей день верит, что Беатриче - бессмертная золотая ведьма."
                        ros "Вот и эпитафию эту жуткую написал..."
                        show bat dou with dissolve
                        bat "Да уж, жуткая. Все эти \"разрывает живот\" и \"воскреснет ведьма - остальные все умрут\"."
                        ros "А главное совсем не понятно, что он хотел ей сказать."
                        show bat std with dissolve
                        bat "Мария говорила, что это ключ к золоту."
                        ros "Может быть и так. Но лично я совсем не вижу в тексте эпитафии подсказок к тому, как его искать."
                        ros "И вообще: мало ли, что имелось ввиду под \"золотом\"."
                        ros "Может быть речь вообще идёт об абсолютно других дорогих отцу вещах, вроде семейных ценностей или знаний."
                        bat "Вы будете пытаться её разгадать?"
                        show ros smi with dissolve
                        ros "Найти золото было бы здорово!"
                        ros "Но лично я понятия не имею как разгадывать такие загадки. Если твой отец и Кириё возьмутся, то я, конечно, присоединюсь."
                        jump dinI

                    "Почему дедушка сейчас вспомнил о ней?":
                        python:
                            r+=1
                            h+=1
                            detective+=3
                        bat "Но почему дедушка вспомнил о ней сейчас?"
                        show bat smi with dissolve
                        bat "Ведь когда я был маленьким о ней только Кумасава и рассказывала, а тут..."
                        show ros exc with dissolve
                        ros "Но... Баттлер, отец никогда о ней не забывал. Он всегда любил её и часто упоминал в разговорах."
                        show ros smi with dissolve
                        ros "Другое дело, что детям этих разговоров слышать не положено."
                        show ros std with dissolve
                        ros "И всё же... Это интересный вопрос. В последние годы отец сильно сдал."
                        ros "И вдруг загорелся идеей о возвращении своей ведьмы. Значит, что-то действительно случилось."
                        bat "Но ведь мёртвые не воскресают. Это довольно глу..."
                        show bat std with dissolve
                        bat "А... А у них с дедушкой не могло быть... Ребёнка?"
                        show ros exc with dissolve
                        ros "Я никогда не думала о таком."
                        ros "Но, может быть, ты и прав. Появление дочери, так похожей на саму Беатриче вполне могло подстегнуть отца к действиям."
                        ros "Может быть даже наследство..."
                        show ros exc1
                        $renpy.pause(1)
                        ros "Баттлер, ты не хочешь рассказать об этой теории Кириё? Она точно может придумать больше, чем я."
                        #with flash
                        $flag1=1
                        #bat "flag1=[flag1]"
                        ros "А я поговорю с Клаусом."
                        jump dinI

            "Что вы думаете про отель дяди Клауса?":
                python:
                    r+=1
                    detective+=1
                show bat std with dissolve
                bat "Тётя Роза, так что насчет отеля дяди Клауса?"
                bat "Что вы об этом думаете?"
                show ros ace with dissolve
                ros "Не знаю..."
                ros "На самом деле, я стараюсь сохранить нейтралитет."
                bat "Почему?"
                show ros sad with dissolve
                ros "Потому что от меня ничего не зависит..."
                ros "Если бы я могла хоть как-то на всё это повлиять, то конечно же не осталась в стороне."
                bat "Однако что вам мешает высказать своё мнение?"
                show ros exc with dissolve
                ros "Баттлер, в нашей семье не всё так просто..."
                bat "И всё же, разве вы получите что-то, сохраняя нейтралитет?"
                bat "Вы не думали, что можете потерять и то, что сейчас имеете, если никого не поддержите?"
                bat "Вы ведь можете оказаться против всех, а не вместе со всеми."
                show ros sad with dissolve
                ros "Возможно..."
                ros "Однако пока я буду стоять на своём."
                bat "Тётя, а всё же, кто в этой истории прав, на ваш взгляд."
                bat "Кого бы вы могли поддержать?"
                menu:
                    "Дядю Клауса?":
                        python:
                            h+=1
                            r+=1
                            detective+=3
                        bat "Дядю Клауса?"
                        show ros std with dissolve
                        ros "Думаю, да."
                        bat "Почему?"
                        ros "Он является законным наследником состояния семьи Уширомия."
                        ros "Тогда почему мы должны мешать строительству его отеля?"
                        show bat dou with dissolve
                        bat "Потому что дядя Клауса потратит все деньги только на себя и свой бизнес."
                        bat "Он ничего не оставит остальным наследникам."
                        show ros ang with dissolve
                        ros "Это не так!"
                        ros "Я не согласна!"
                        ros "Клаус - порядочный человек. Он никогда так не пуступит со своей семьей."
                        ros "А мы все - его семья."
                        ros "Отель будет приносить много прибыли."
                        ros "И какой-то процент Клаус обязательно будет делить между нами."
                        ros "Он никогда не оставит нас!"
                        show bat std with dissolve
                        bat "Хорошо, тётя Роза."
                        bat "Ваша позиция мне ясна."
                        bat "Не хочу с вами спорить или как-то вас переубеждать."
                        show bat smi with dissolve
                        bat "Извините, если я вас задел... Не хотел этого."
                        show ros std with dissolve
                        ros "Ничего."
                        jump dinI

                    "Моего отца и остальных?":
                        python:
                            r+=1
                            detective-=1
                        bat "Возможно это были бы мой отец и остальные наследники семьи Уширомия?"
                        show ros ace with dissolve
                        ros "Боюсь, Баттлер, я встала бы на сторону Клауса."
                        ros "Я не имею ничего против твоего отца и остальных, но..."
                        ros "Клаус - законный наследник состояния вашего дедушки."
                        ros "Поэтому пусть он и распоряжается сейчас деньгами."
                        show bat dou with dissolve
                        bat "Но как так?"
                        bat "Я тоже не имею ничего против дяди Клауса. Многие его идеи и мысли мне близки, однако..."
                        bat "Он может прогореть, и тогда вся семья Уширомия придёт в упадок."
                        show ros std with dissolve
                        ros "Баттлер, не беспокойся об этом."
                        ros "Клаус - умный и хитрый человек. Он сможет в любой ситуации выкрутиться."
                        ros "Я уверена, что отель будет процветать. Просто нужно немного подождать."
                        ros "Надеюсь, это поймут и остальные члены семьи."
                        show bat std with dissolve
                        bat "Может быть."
                        jump dinI

    label dinI:
        if len(men)<2 :
            scene bg mb dining m
            show bat std at left
            hide bat
            show letters filter
            show bat std at left
            with fade
            jump dinS

        scene bg mb dining m
        show bat std at left
        with fade


    # bat "И тут внезапно прибегает Зомай с дробовиком."
    # bat "Конец."
    # bat "Ну почти..."
    # bat "И все СЧАСТЛИВЫ!"
    # bat "Вот теперь конец."

    show nan std behind bat at offscreenleft
    show nan std at left2 with move
    "{color=#A8E4A0}???{/color}" "Ох-ох, простите! Я опоздал на обед!"
    play sound flsh
    show letters filter behind nan with flash


    bat "Доктор Нанджо. Близкий друг и лечащий врач дедушки."
    play sound shut
    hide letters
    with flash

    nan "Заигрались с Кинзо в шахматы!"
    kla "Ничего страшного. Обед же ещё не закончен. Присаживайтесь."
    scene bg mb dining rev m
    show nan std at right2
    show bat std at left
    show gen std behind bat at offscreenleft

    with fade
    bat "Доктор Нанджо, могу я задать вам вопрос?"
    nan "Конечно-конечно, молодой человек! Спрашивайте!"
    bat "Вот вы с дедушкой давно дружите?"
    nan "Да, очень давно. Наверное, даже дольше, чем существует Ushiromia Group."
    menu:
        bat "Значит..."
        "...вы знали его ещё до сделки с ведьмой?":
            bat "Значит... вы знали его ещё до сделки с ведьмой?"
            show nan exc with dissolve
            nan "Сделки с ведьмой? Молодой человек, как можно!"
            nan "Кинзо всего добился сам."

        "...вы можете рассказать мне о его романе с Беатриче?":
            bat "Значит...вы можете рвссказать мне о его романе с Беатриче?"
            show nan ang with dissolve
            nan "Молодой человек, да как можно!"
            nan "Такое спрашивать непозволительно в вашем-то возрасте."


    show nan std with dissolve
    nan "Хотя, конечно, Беатриче существовала. Кинзо много рассказывал о ней."
    nan "Да что там \"рассказывал\"! Он и сейчас о ней частенько вспоминает."
    bat "Вот и портрет с эпитафией повесил..."
    nan "А! Да-да! Портрет он заказал очень известному мастеру, который, как считалось, давно ушёл на покой."
    nan "А эпитафию сочинил, видимо, сам."
    show nan smi with dissolve
    nan "Хотя и рассказывал мне, что именно эти слова указала в контракте \"ведьма\"."
    bat "Довольно мрачные слова, не находите?"
    show nan std with dissolve
    nan "Молодой человек, вы просто не можете этого понять."
    nan "Мы, старики, немного иначе относимся к смерти."
    nan "Быть может для Кинзо этот стих - размышление о перерождении души, о высоких материях."
    nan "Просто облачённый в форму песенки про десять негритят."
    nan "Возможно, он жаждет исполнения этой эпитафии, потому что хочет увидеть свою возлюбленную."
    nan "Всегда можно найти рациональное объяснение."
    bat "Хм. Я не подумал об этом."
    bat "Спасибо, доктор Нанджо. Я запомню эти слова."
    $detective+=5


    kla "Генджи!"
    stop music fadeout 2.0
    show gen std at left2 with move
    play sound flsh
    show letters filter behind gen with flash

    bat "Генджи. Мажордом семьи Уширомия и доверенное лицо дедушки."
    play sound shut
    hide letters filter
    with flash

    gen "Да, господин Клаус?"
    kla "Прикажи подать чай в малую гостинную. Мы закончили с обедом и хотим обсудить дела в семейном кругу."
    play music "sounds/music/unsorted/Melody (instrumental).mp3" fadein 1.5
    gen "Будет исполнено."
    show gen std at offscreenleft with move
    show jes std at offscreenright
    show jes std at right with move
    jes "Баттлер, пойдём к морю? Мария хотела чтоб мы устроили пикник."
    show bat smi with dissolve
    bat "Хоть мы и только что поели - пикник это хорошо. Идём."
    show bat smi at offscreenleft
    show jes std at offscreenleft
    with move

    nan "Эх, молодёжь!"
    jump sc3
    #scene mb dining


##Возле каждого with flash поставить play sound flsh на входе и play sound shut на выходе
