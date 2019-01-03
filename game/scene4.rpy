
label sc4:
scene bg mb loundge m
play sound flsh
show kla std at left05
show nat std at left
show ros std at right4
show gen std at right
show letters filter
with flash

kla "Спасибо, Генджи. Ты можешь идти."
show gen at offscreenright with move
kla "И так..."

play sound "sounds/sound/s/whin.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva std at left2
show letters filter
with camera
#jump in1
rud "Ну, что, поговорим об отцовском наследстве?"
hid "Обычно ты всем заправляешь, Клаус. И мы вовсе непротив, в конце концов ты - наследник, но..."
show rud ace with vpunch
rud "Но сейчас ты просчитался!"
show rud std with dissolve
eva "Должно быть, немало денег ушло, чтоб отгрохать тот отель, братец? Да ещё и за островом ухаживать приходится..."

play sound "sounds/sound/s/whout.mp3"
scene bg mb loundge m
show kla std at left05
show nat std at left
show ros std at right4
show letters filter
with camerab
show kla exc1 with dissolve
rud "..."
show nat dou with dissolve
nat "О чём ты вообще?"

play sound "sounds/sound/s/whin1.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva std at left2
show letters filter
with camera
rud "И когда же он начнёт приносить прибыль, братец?"
show rud smi with dissolve
rud "Сам знаешь, когда предприятия не приносят прибыли их хозяев могут уличить в чём угодно..."
rud "В растратах средств в личных целях, например."
show eva smi with dissolve
eva "Я не понаслышке знаю о том, какие деньги могут уйти на стройку."
show eva std with dissolve
hid "Мы попытались выяснить, кто одолжил тебе такую огромную сумму."
rud "Но так и не нашли этого человека."
rud "И так, давай на чистоту: ты использовал деньги отца, чтоб устроить свои дела?"
eva "Да не \"использовал\", а попросту присвоил их себе!"
show eva ace with vpunch
eva "Такое вот преступление!"

play sound "sounds/sound/s/whout1.mp3"
scene bg mb loundge m
show kla std at left05
show nat std at left
show ros std at right4
show letters filter
with camerab
show nat ang with vpunch
nat "Да что ты такое несёшь! Как ты смеешь говорить в таком тоне о своём брате?!"
nat "О наследнике семьи Уширомия!"

play sound "sounds/sound/s/whin.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva ace at left2
show letters filter
with camera
eva "Так ведь он отца предаёт. Какой же из него наследник..?"

play sound "sounds/sound/s/whout.mp3"
scene bg mb loundge m
show kla std at left05
show nat std at left
show ros std at right4
show letters filter
with camerab
show nat ang with vpunch
nat "Выметайся отсюда!"

play sound "sounds/sound/s/whin1.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva std at left2
show letters filter
with camera
show eva ang with dissolve
eva "Помолчала бы! Приказывать мне? Третьей в семье - \"выметаться\"?!"
eva "Тебе не разрешено даже носить на одежде однокрылого орла!"
eva "Тебя взяли в семью только чтоб ты родила наследника Клаусу."
show eva std with dissolve
eva "Но ты и с этим не справилась."

play sound "sounds/sound/s/whout1.mp3"
scene bg mb loundge m
show kla std at left05
show nat ang at left
show ros std at right4
show letters filter
with camerab
show kla exc with dissolve
kla "Натсухи..."
show nat dou with dissolve
kla "Прошу, выйди."
show nat sad with dissolve
nat "Но, дорогой..."
show nat sad1 with dissolve
$renpy.pause(0.5)
show nat sad1 at offscreenright with move
#Звук хлопка дверью
show kla sad with dissolve
kla "Вот, Ева, почему ты всегда..."

play sound "sounds/sound/s/whin.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva ang at left2
show letters filter
with camera
eva "Нет, а почему я должна выслушивать это от безродной девки?!"
show hid dou with dissolve
hid "Ты перегибаешь палку. Опять. Успокойся."
play sound flsh
with flash

menu:
    "Почему тётя Ева так ненавидит Натсухи?":
        hide kyr
        show bat std at left
        show kyr std at right
        with flash
        $detective+=1
        bat "Слушай, а почему Ева так ненавидит Натсухи?"
        kyr "Ты же слышал, однокрылый орёл и всё такое."
        bat "Хорошо, другой вопрос: почему {i}именно Натсухи{/i} запретили носить герб?"
        stop music fadeout 2.0
        bat "Ведь и ты, и дядя Хидеёши, хоть и не родились в семье Уширомия, а герб на одежде носите."
        show kyr dou with dissolve
        #"sounds/music/bgm/Future.mp3"
        play music "sounds/music/bgm/Future.mp3" #"sounds/music/bgm/Witch in gold.mp3" fadein 2.0
        kyr "Это не самый простой вопрос. Полагаю, это похоже на историю с твоей мамой."
        kyr "Рудольф, как и Клаус, выбрал себе партию по любви, наплевав на правила, которым принято следовать в нашей среде."
        kyr "Пойми правильно, твой отец никогда не отличался особыми моральными принципами, особенно в молодости."
        bat "Да уж. Я представляю. В конце концов, это же я на 15 лет выбыл из семьи Уширомия из-за его \"принципов\"."
        show kyr std with dissolve
        kyr "Не суди его строго. В конце концов, твою мать, Асуму, он действительно любил. И даже сбежал из семьи на какое-то время."
        kyr "Так вот, пока они были женаты, Асуму так же было запрещено носить однокрылого орла на одежде. Такова традиция."
        kyr "А я и Хидеёши всё же иного происхождения люди."
        bat "Ты её хорошо знала?"
        show kyr ang with dissolve
        kyr "Настолько хорошо, насколько положено знать друг друга двум женщинам, имеющим детей от одного мужчины."
        bat "Прости. Глупость сморозил."
        show kyr std with dissolve
        kyr "Ничего страшного. В конце концов во взаимоотношениях семьи Уширомия - сам чёрт ногу сломит."
        kyr "И, если Бог даст, вам придётся легче, чем нам."
        kyr "Вот. Только, если моральные принципы Рудольфа несколько... адаптивны, то Клаус - человек-кремень."
        kyr "Он привёз свою возлюбленную на остров и плевать хотел на мнение остальных."
        kyr "В каком-то роде он сильно выиграл от этого - Натсухи действительно умная женщина и сильно помогает ему. И действительно любит."
        show kyr smi with dissolve
        kyr "А Ева - бесится. Хоть она и любит мужа, но она следовала правилам и выходила за \"подходящую пару\". Вот ей и ест глаза чужое счастье."
        bat "Ясненько..."
        stop music fadeout 2.0
        hide bat
        hide kyr


    "Продолжить слушать":
        play sound shut

        stop music fadeout 2.0
play sound shut
show kyr std behind hid at right
with flash
show eva std with dissolve
eva "Ну и ладно. И так..."
play music "sounds/music/bgm/Banquet of a Neverending Night.mp3" fadein 1.0
show hid ace with dissolve
hid "Клаус, если примешь наши условия - мы позволим тебе и дальше распоряжаться отцовским наследством."

play sound "sounds/sound/s/whout1.mp3"
scene bg mb loundge m
show kla exc at left05
show ros std at right4
show letters filter
with camerab
kla "Условия..?"

play sound "sounds/sound/s/whin1.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva ang at left2
show letters filter
with camera
show rud ace with vpunch
rud "Условие первое:"
rud "Ты разрешишь поиски отцовского золота."
show eva ace with vpunch
eva "Условие второе:"
eva "Ты разделишь золото на всех."
show hid ace with dissolve
hid "Наследник семьи получает половину, а остальное делится на всех."
eva "Из двадцати миллиардов ты получишь десять. Я, Роза и Рудольф по три. Остаток же станет резервом и покроет долги, например, твои за отель."
rud "Условие четвёртое:"
rud "Золото делится сразу после смерти отца, но десять процентов ты выплатишь каждому из нас сейчас, как задаток."
show hid std with dissolve
hid "Что думаешь? Это не такие уж непосильная сумма для тебя."

play sound "sounds/sound/s/whout.mp3"
scene bg mb loundge m
show kla std at left05
show ros std at right4
show letters filter
with camerab
kla "Я люблю эту семью..."
show kla tau with dissolve
kla "Хидеёши, я слышал кто-то тайно выкупил контрольный пакет акций твоей компании..."

play sound "sounds/sound/s/whin.mp3"
scene bg mb loundge rev
show rud std at right1
show kyr std at right
show hid std at right5
show eva ang at left2
show letters filter
with camera
show hid exc with dissolve
hid "Как ты..."
kla "А тебя, Рудольф, как я слышал, американский суд оштрафовал на несколько миллионов долларов? Печально."
kla "Но ведь это не такая уж непосильная сумма для тебя?"
show rud exc with dissolve
rud "Не думаю, что это тебя касалось."

play sound "sounds/sound/s/whout1.mp3"
scene bg mb loundge m
show kla tau at left05
show ros std at right4
show letters filter
with camerab
kla "А ты, Роза..."
show ros exc with dissolve
ros "Что - Роза? Я же ничего не..."
kla "А тебе и не надо. У тебя дела никогда не шли хорошо."
show kla ace with vpunch
kla "Я бы с удовольствием помог своим дорогим родственничкам, будь у меня такая возможность."
kla "Вот только сейчас на руках денег у меня совсем нет. Как и у вас."
show kla std with dissolve
kla "Как вы и сказали, было бы здорово сейчас найти отцовское золото."
show ros std with dissolve
show kla smi with dissolve
kla "Может, попытаемся разгадать эпитафию Беатриче? Ха-ха."
stop music fadeout 2.0

scene bg mb cor m
play sound flsh
show kyr std at left
show bat std at right3
with flash

bat "Ясненько... Не думал, что всё так плохо."
play music "sounds/music/bgm/Checkmate.mp3" fadein 2.0
kyr "Вот я и хотела спросить, не узнал ли ты чего-то, что смогло бы нам помочь?"
$liekyr=0
if flag>0 or flag1>0:
    label kyrmen:
    show kyr std
    show bat smi
    with dissolve
    menu:
            " "
            "Мы обсуждали эпитафию..." if flag==1:
                $ renpy.block_rollback()
                bat "Мы обсуждали эпитафию с ребятами."
                kyr "Вы о чём-то узнали?"
                bat "Мне кажется, что эпитафия создана не для того чтоб её разгадывать."
                bat "Судя по тексту, если \"взять ключ\", начать разгадывать эпитафию, произойдёт что-то плохое."
                kyr "И, всё же, золото существут. Просто поверь."
                show kyr dou1 with dissolve
                kyr "Другое дело, конечно, что эпитафия может быть ложным следом..."
                kyr "Мне надо об этом подумать."
                $flag=0
                jump kyrmen

            "Мы пытались решить эпитафию." if flag==2:
                $ renpy.block_rollback()
                bat "Мы с ребятами пытались решить эпитафию."
                kyr "Вы о чём-то узнали?"
                bat "Мне кажется, что эпитафия создана не для того чтоб её разгадывать."
                bat "Судя по тексту, если \"взять ключ\", начать разгадывать эпитафию, произойдёт что-то плохое."
                bat "Кроме того, ключ - что-то живое. Или хотя бы содержащее информацию. Иначе текст становится бессмыслицей."
                kyr "Да, я тоже думала об этом. Молодец."
                show kyr dou1 with dissolve
                kyr "И, всё же, золото существут. Просто поверь."
                kyr "Другое дело, конечно, что эпитафия может быть ложным следом..."
                kyr "Мне надо об этом подумать."
                $flag=0
                jump kyrmen


            "У меня есть кое какие мысли по поводу эпитафии." if flag==3:
                    $ renpy.block_rollback()
                    bat "У меня есть кое какие мысли по поводу эпитафии."
                    kyr "Вот как?"
                    bat "Мне кажется, что эпитафия создана не для того чтоб её разгадывать. Это инструкция, но вовсе не к поиску золота."
                    bat "Судя по тексту, если \"взять ключ\", начать разгадывать эпитафию, произойдёт что-то плохое."
                    bat "Кроме того, ключ - что-то живое. Или хотя бы содержащее информацию. Иначе текст становится бессмыслицей."
                    show bat ace with vpunch
                    bat "И кроме того, в самом конце становится очевидно, что простое следование описанному в эпитафии, в лучшем случае, не принесёт ничего."
                    show kyr ace with vpunch
                    kyr "А в худшем - просто убьёт идиота."
                    kyr "Да, я тоже думала об этом. Молодец."
                    show bat smi
                    show kyr smi
                    with dissolve
                    kyr "Действительно хорошая работа. Вот тебе ещё пища для размышлений..."
                    kyr "Табличка с эпитафией выглядит старой, но определённо не настолько, чтоб поверить в то, что Кинзо её дала \"вечная ведьма\"."
                    kyr "Точно, конечно, не определить, но, я полагаю, ей около пятнадцати лет."
                    $detective+=2
                    kyr "А вот портрету действительно меньше трех лет."
                    show bat std
                    bat "Ясненько..."
                    show kyr dou1 with dissolve
                    kyr "И, всё же, золото существут. Просто поверь."
                    kyr "Так что давай попробуем решить эту загадку. В конце концов выиграют от этого все."
                    init python:
                        lg=0
                    $lg+=1
                    $flag=0
                    jump kyrmen


            "Мне пришла в голову одна идея о том, почему эпитафия вообще появилась здесь." if flag1==1:
                $ renpy.block_rollback()
                $flag1=0
                $lg+=1
                bat "Мне пришла в голову одна идея о том, почему эпитафия вообще появилась здесь."
                kyr "Не веришь в историю о вечной любви?"
                bat "Верю. Но не верю в вечно живущих ведьм и возможностьвоскресить умершего."
                kyr "И так, по твоему..."
                bat "Я думаю, что у дедушки был ещё один ребёнок. Дочь, от этой самой \"ведьмы\" Беатриче. Вернее, конечно, обычной женщины, но..."
                bat "И, вот теперь, этот ребёнок появился. Думаю, она очень похожа на мать и Кинзо, в силу того, что достаточно стар, просто поверил в то, что это его \"Беатриче\"."
                show kyr dou1 with dissolve
                kyr "А предприимчивая девушка не стала разубеждать старика..."
                bat "Именно."
                kyr "Звучит правдоподобно. И как я проморгала такой вариант... Это плохо."
                kyr "Ты рассказывал кому-то ещё?"
                menu:
                    "Тётя Роза знает.":
                        $liekyr="no"
                        bat "Я догадался во время разговора с тётей Розой. Так что знает она."
                        bat "И она обещала рассказать Клаусу."
                        kyr "Жаль. Впрочем..."
                        show kyr ace with vpunch
                        kyr "Нет ничего, что нельзя повернуть в свою пользу!"
                        show bat smi with dissolve
                        bat "Я знал, что ты так скажешь."
                        jump kyrmen
                    "Нет.":
                        $liekyr="yes"
                        bat "Нет, я никому не рассказывал."
                        kyr "Славно. Не стоит их беспокоить. Думаю, мы справимся без лишнего шума."
                        jump kyrmen
show kyr std with dissolve
kyr "Ясненько. Что ж, спасибо."
stop music fadeout 2.0
play sound "sounds/sound/s/Thunder.wav"
show bat std with dissolve
bat "Эх, буря приближается."
play music "sounds/music/bgm/Golden slaughterer.mp3"
kyr "Да, что верно то верно... Будет буря..."
show kyr exc with dissolve
kyr "Эй, там же Мария! Что она одна делает во дворе?"
bat "Хм. Не знаю. Пойду, приведу её в дом."
show bat at offscreenright with move

play bgs runw
scene bg mb cor1 at running
$ renpy.pause(1)
show bg mb cor stairs s at running
$ renpy.pause(1)
show bg mb stairs down at running
$ renpy.pause(1)
show bg mb hall s at running
$ renpy.pause(1)
stop bgs
play bgs run
show bg mb entrance s at running
$ renpy.pause(1)
show bg garden house1 s at center
stop bgs

show mar dou at left
show geo std at left4
show ros std at offscreenright
show bat std at offscreenright
show jes std at center

mar "Ууу! Роза Марии!"
show bat std at right with move
bat "Мария! Джордж!"
stop music fadeout 5.0
bat "Что вы тут делаете?"
play music "sounds/music/bgm/Rain.mp3" fadein 3.0
geo "Да вот, роза потерялась..."
bat "Думаю, она вместе с остальными, в гостинной."
jes "Да не та Роза, дубина!"
mar "Мама!"
show ros std at left3 with move
ros "Что у вас тут случилось?"
mar "Розу потеряли. Розу Марии."
geo "Мы ленточку повязали специально, чтобы она выделялась, но..."
mar "Ууу! Уууу!"
mar "Здесь была! Уууу!"
show ros exc with dissolve
mar "Найди её, мама!"
stop music fadeout 5.0
ros "Перестань \"укать\"."
mar "Ууууу!"
show ros ang with dissolve
ros "Прекращай!"
mar "УУУУУУУУ!"
play music "sounds/music/bgm/Golden slaughterer.mp3" fadein 3.0
show ros ang1 with vpunch
ros "СКАЗАЛА ЖЕ, ПРЕКРАЩАЙ!"
show mar sad with hpunch
play sound "/sounds/sound/s/slap.mp3"
show bat dou
show geo dou
show jes dou
with dissolve
mar "Роза! Роза Марии! Ууу!"
mar "Ууу, ууу..."
show ros ang with dissolve
bat "Тётя Роза, насилие - не лучший выход."
ros "Ей девять лет! Четвёртый класс окончила!"
ros "Знал бы ты как её за это в школе дразнят!"
ros "В дом, Мария! Мы возвращаемся."
mar "УУУУУУУ!"
ros "Я ЖЕ СКАЗАЛА! ПРЕКРАЩАЙ!"
play sound "/sounds/sound/s/slap1.mp3"
$renpy.pause(0.4)
play sound "/sounds/sound/s/slap2.mp3"
show bat at right4 with move
bat "Тётя Роза!"
show geo at right2 with move
geo "Нам не стоит лезть в их проблемы. Пойдём."
bat "Наверное, ты прав..."
stop music fadeout 4.0
show bat at offscreenright
show geo at offscreenright
show jes at offscreenright
with move

scene bg sky s with fade
$renpy.pause(2,hard=True)
show screen Rain
with dissolve
$renpy.pause(5,hard=True)
$sstop("rain")
hide screen Rain
show bg mb cor s
play music "sounds/music/bgm/Love examination.mp3"
show geo std at left
show jes std at left2
show bat smi at right
show kan std at center
with fade

kan "Ужин подан."

bat "А ведь ещё недавно мне казалось, что я наелся."
show bat smi with dissolve
bat "К счастью, это не так."
show geo smi
show jes smi
with dissolve

jes "Баттлер! Ты опять!"
show geo std at offscreenright
show jes std at offscreenright
show bat smi at offscreenright
with move
kan "А где госпожа Мария?"
stop music fadeout 1.0
show geo std at right
show jes std at right3
show bat std at right2
with move
bat "Она разве не с тётей Розой?"
kan "Нет. Госпожа Роза в гостинной, но госпожу Марию я там не видел."
bat "Неужели..."
play music "<from 72>sounds/music/bgm/Golden slaughterer.mp3" fadein 3.0
play bgs runw
scene bg mb cor1 at running
$ renpy.pause(1)
show bg mb cor stairs s at running
$ renpy.pause(1)
show bg mb stairs down at running
$ renpy.pause(1)
show bg mb hall s at running
$renpy.pause(1)
stop bgs
play bgs run
show bg mb entrance s at running
show screen Rain
stop bgs
$ renpy.pause(1)

scene bg garden house1 s
show geo dou at offscreenright
show jes dou at offscreenright
show bat std at offscreenright
show ros sad1 at left
ros "Мария!"
show geo dou at right
show jes dou at right3
show bat std at right2
with move
bat "Тётя Роза!"
ros "Ребята! Мария не с вами? Вы не видели её?"
bat "Нет. Мы ведь её тогда с вами оставили..."
ros "Ох. Это я виновата. Что же я наделала..."
hide screen Rain

scene bg garden house1 s
play sound flsh
show ros ang at left3
show mar sad at left
show letters filter
with flash

ros "Пойдём! Мария!"
mar "Уууууу!"
show ros ang1 with dissolve
ros "Тогда оставайся и ищи сама!"
mar "Буду! Мария будет искать!"
ros "Как хочешь!"
show ros at offscreenright with move
scene bg garden rose s
show ros ang at offscreenleft
show letters filter
show ros ang at left2 with move
show ros sad1 with dissolve
ros "Мария... Ну почему ты..."
show ros sad1 at offscreenright with move
$renpy.pause(1)

scene bg garden house1 s
play sound shut
show geo dou at right
show jes dou at right3
show bat std at right2
show ros sad1 at left
show screen Rain
with flash

bat "Вот как..."
geo "Ну что ж, надо искать!"
geo "Мария!"
show geo at offscreenleft with move
jes "Ты где, Мария!"
show jes at offscreenright with move
ros "Мария!"
show ros at offscreenright with move
bat "Мария! Ау?"
show bat at offscreenright with move

show bg garden rose s with camera
show bat std at center with move
bat "МАРИЯ?"
show bat at offscreenleft with move
show bg garden rose1 s with camera
show bat std at center with move
bat "Мария, где ты?!"
show bat at offscreenright with move

show bg garden s
show mar sad at left2
with camerab
bat "Мария!"
show bat at right2 with move
stop music fadeout 4.0
bat "Она здесь! Я нашёл!"
mar "Роза... Не могу найти..."

show ros at left
show geo at center
show jes at right
with move
play music "<from 3>sounds/music/bgm/Future.mp3" fadein 2.0
ros "Мария! Прости меня, прости!"
mar "Роза... Потерялась..."
ros "Ох, Мария, прости меня..."
mar "Мама не виновата..."
show bat smi
show geo std
show jes std
with dissolve
bat "Хорошо, что она нашлась"
geo "Ну и напугала же ты нас."
jes "Даже и не промокла почти. Мария, у тебя что, зонтик был? А где он?"
stop music fadeout 3.0
play music "<from 0 to 10>sounds/music/bgm/Witch in gold.mp3" fadein 2.0
show mar std with dissolve
mar "У меня не было. Но у Беатриче был. Она помогала мне искать."
show bat dou with dissolve
bat "Беатриче, да?"
geo "Не важно. Главное, что Мария нашлась."
show bat smi with dissolve
bat "И верно! Идём в дом, Канон сказал, что еда уже готова."
show bat smi at offscreenright
show geo std  at offscreenright
show jes std  at offscreenright
show ros std  at offscreenright
show mar std  at offscreenright
with move
hide screen Rain
stop music fadeout 3.0

scene bg mb dining
play music "sounds/music/bgm/Black Lilliana.mp3" fadein 4.0
show bat smi at left
show ros std  at right
show mar std  at right1
show rud std at center
show kyr std at left2
with fade
ros "...И вот, кто-то там был и держал для неё зонтик, пока она искала розу."
show mar smi
show bat std
with dissolve
mar "Это Беатриче!"
bat "Ведьм не быва..."
ros "Вот, так всё и было. Ребята говорят, что это не они."

play sound "sounds/sound/s/whin.mp3"
scene bg mb dining rev
show hid std at left
show eva std at left3
show gen std at offscreenright
show nan std at right1
show kla std at right2
show nat std at center
with camera
kla "Мы оставались в гостинной, так что ничего не знаем об этом."
nat "Я с Генджи занималась бумагами. Мы тоже непричём."
kla "Кстати, Генджи..."
show gen at right with move
gen "Никто из слуг этого так же не мог сделать, господин Клаус. Канон помогал Гоуде на кухне, а Шанон и Кумасава занимались приготовлением комнат и гостевого домика."
show kla smi with dissolve
kla "Я даже спросить не успел! Не удивительно, что отец тебя так ценит. Ты можешь идти."
show gen at offscreenright with move
show nan smi with dissolve
nan "Ну, я уж точно не тяну на красавицу-Беатриче."
nan "Но, всё же, я был у Кинзо, мы играли в шахматы. К слову, он опять победил."
show nan std with dissolve

play sound "sounds/sound/s/whout.mp3"
scene bg mb dining
show bat smi at left
show ros std  at right
show mar std  at right1
show rud std at center
show kyr std at left2
with camerab
bat "Так кто одолжил Марии зонтик?"
mar "Беатриче!"
bat "Да ну тебя. Кто это мог бы..."
mar "А ещё она сказала, что Мария ведьмина по... Посланница!"
show bat std with dissolve
bat "Посланница..?"
mar "Угу. Мама, мы докушали?"
show ros smi with dissolve
ros "Да, Мария."
mar "Вот! Ведьма сказала прочитать, когда все докушают!"
show letter with camera
stop music fadeout 3.0
nan "На конверте печать Кинзо!"
mar "Читаю!"
hide mar
play music "sounds/music/bgm/Organ short #600 million in C minor.mp3"
show mar dou at right1 with vpunch
hide screen points
voice pm
letters "Добро пожаловать на остров Роккен, Семья Уширомия. \n
Я - советница господина Киндзо по алхимии. Зовут меня Беатриче. \n
Служила я долго и преданно, честно выполняя договор. \n
Однако сегодня господин Киндзо объявил, что срок моей службы подошёл к концу. \n
Поэтому, попрошу вас принять тот факт, что я больше не семейная советница по алхимии. \n
Пришло время разъяснить вам некоторые пункты договора."
rud "Быть не может!"
$style.nvl_dialogue.slow_cps=0
voice pm
letters "Я, Беатриче, одолжила Киндзо большое количество золота на определённых договором условиях."
show mar ace1 with vpunch
voice pm
letters "Условие первое: после расторжения договора золото вернут мне."
voice pm
letters "Условие второе: в качестве процента я получу всё, что есть у семьи Уширомия."
kla "Ну, это уж слишком!"
nvl clear
$style.nvl_dialogue.slow_cps=15
voice pm
letters "К счастью для вас, Киндзо поставил со своей стороны третье условие, благодаря которому вы все можете сохранить богатство и честь.\n
Если вы выполните его, я навсегда потеряю право на золото и процент."
voice pm
letters "Особое условие: Если кто либо найдёт спрятанное золото, о котором говорится в договоре, Беатриче откажется от вышеупомянутых прав."
voice pm
letters "Иначе говоря, если кто либо из вас доберётся до спрятанного золота, то я верну всё, даже то, что уже заберу к тому времени.\n"
eva "Даже прислуга?!"
nvl clear
voice pm
letters"\n\n\n\n\n\nКроме того, как вы видите, Киндзо передал мне кольцо главы семьи Уширомия. А значит, право быть главой семьи перешло ко мне и печать тому подтверждение.
Место где спрятано золото указано в эпитафии у портрета, каждый может найти его. Я верну всё, как только вы найдёте золото.\n
Постарайтесь обставить Киндзо в сообразительности. От всей души молюсь, чтобы вы {i}блеснули умом{/i} этой ночью."
voice pm
letters "Золотая ведьма Беатриче."
stop music fadeout 3.0
hide nvl
nvl clear
play music "sounds/music/bgm/Prison strip.mp3" fadein 3.0
show mar std
show bat dou
show kyr dou
show ros dou
show rud dou
hide letter
show screen points
with camerab
ros "Это какая-то глупая шутка!"
rud "Да не может такого быть!"

play sound "sounds/sound/s/whout1.mp3"
scene bg mb dining rev
show hid dou at left
show eva dou at left3
show gen dou at offscreenright
show nan dou at right1
show kla dou at right2
show nat dou at center
with camera

kla "Но кольцо-то настоящее..."
eva "И всё равно! Значит отца обманули!"
rud "Ну же, братец, ты то точно был в курсе всех отцовских дел!"
show kla exc1 with dissolve
kla "Я вёл ВСЕ дела семьи последние три года. Но ничего об этом не знаю."
show eva ang with vpunch
eva "Мы должны что-то предпринять!"


show ros std  at offscreenleft
show rud std at offscreenleft
show kyr std at offscreenleft
kla "К отцу!"
play bgs runw
$renpy.pause(0.3)
play sound runw
show hid dou at offscreenright
show eva dou at offscreenright
show gen dou at offscreenright
show nan dou at offscreenright
show kla dou at offscreenright
show nat dou at offscreenright
show ros std  at offscreenright
show rud std at offscreenright
show kyr std at offscreenright
with MoveTransition(1.3)
stop sound fadeout 1
stop bgs fadeout 0.5

#stop music fadeout 4.0
play sound "sounds/sound/s/whin1.mp3"
#play music "<from 58>sounds/music/bgm/Prison strip.mp3" fadein 3.0
scene bg mb dining
show jes dou at offscreenleft
show bat std at left
show geo dou at offscreenright
show mar std  at right1
with camerab
bat "Да уж..."
show jes dou at left2
show geo dou at right2
with move
jes "Не к добру всё это..."
geo "Перемены вообще не к добру. А уж такие..."
show bat dou with dissolve
bat "А зная содержание эпитафии, остаётся ожидать худшего."
stop music fadeout 2.0

scene bg mb room n
play sound flsh
show bat std at left
show kyr std at offscreenright
show letters filter
with flash


voice pm
"Остров Роккен. 4 октября 1986 год. 21:30 вечера."

play sound shut
hide letters
with flash

play music "<from 28>sounds/music/bgm/Checkmate.mp3" fadein 3.0
show kyr at right with move
bat "И что было у дедушки?"
kyr "Да ничего, по сути, не было."

scene bg mb cor2 s
play sound flsh
show kla ang at right2
show letters filter
with flash

kla "Отец! Ты слышишь! Открывай!"
eva "Ты никогда не рассказывал нам про договор!"
rud "Как это понимать - передал кольцо главы?!"
play sound shut
show kyr std at right
show bat std at left
with flash

kyr "Он никого не впустил. Только рыкнул из-за двери, что всё правда и, что {=lett}игра началась."
bat "Значит, всё правда? Ну, про золото..."
if liekyr!=0:
    show kyr ace with vpunch
    kyr "И про дочь! Чем больше обстоятельств выясняется - тем больше я склоняюсь к этой версии."
    $detective+=1
    show kyr std with dissolve
kyr "Так или иначе... Как думаешь, есть ли на острове девятнадцатый?"

menu men1:
    " "
    "Девятнадцатый? С чего ты взяла?":
        bat "Девятнадцатый? С чего ты взяла?"
        kyr "Ну, как же! А зонт? Кто-то ведь держал его для Марии."
        kyr "В любом случае, постарайся подумать над этим."
        kyr "Это очень важно для всех нас."
        bat "Ведь если девятнадцатого не существует - под удар попадают свои..."
        kyr "Они в любом случае попадают. Ведь кто-то из нас мог быть в сговоре с девятнадцатым."
        kyr "Или, например, исполнять указания девятнадцатого, в то время, как самого его на острове и нет."

    "Ну, кто-то же дал Марии зонт. {=lett}\[Требуется 5 ОД\]":
        if detective>=5:
            $detective-=5
            bat "Ну, кто-то же дал Марии зонт."
            bat "Да и не стал бы дедушка сам такое проворачивать, наверное..."
            bat "А это значит, что кольцо действительно было передано кому-то."
            bat "И раз уж ещё никто не объявил, что он новый глава семьи, значит это не один из вас, законных наследников."
            show bat ace with vpunch
            bat "А значит - есть девятнадцатый!"
            kyr "Это было бы слишком очевидно, Баттлер"
            show bat std with dissolve
            kyr "Всегда нужно стараться понять причину, а не изучать следствие."
            kyr "Нужно, так сказать..."
            show kyr ace with vpunch
            kyr "...повернуть шахматную доску!"
            show bat smi
            show kyr smi
            with dissolve
            bat "Шахматы... Это в твоём стиле."
            show bat std
            show kyr std
            with dissolve
            kyr "Так вот, стоит повернуть шахматную доску и становится очевидно - девятнадцатого просто не может быть."
            kyr "Ведь если он скрывается от нас, то зачем пришёл передавать письмо лично? Мог бы отправить его по почте, или с одним из рыбаков в конце концов."
            kyr "А это значит, что \"Беатриче\" - один из восемнадцати. Один из нас..."
            bat "В такой версии много пробелов..."
            kyr "Молодец. Критично мыслить - это правильный путь."
            kyr "Вот только..."
            show kyr ace with vpunch
            kyr "Мы с тобой здесь. И мы можем эти пробелы заполнить."
            show kyr std with dissolve
            kyr "Так что старайся, Баттлер. Ищи улики и разгадывай логические цепочки. И тогда - мы узнаем правду."
            kyr "Мария, вступавшая с этим неизвестным в контакт - ключ к разгадке."
        else:
            jump men1
    "Это было бы слишком очевидно! {=lett}\[Требуестся 7 ОД\]":
        if detective>=7:
            $detective-=7
            show bat ace with vpunch
            bat "Это было бы слишком очевидно!"
            bat "Всегда нужно стараться понять причину, а не изучать следствие."
            bat "Нужно, так сказать..."
            show kyr ace with vpunch
            kyr "...повернуть шахматную доску!"
            show bat smi
            show kyr smi
            with dissolve
            bat "Ты ведь сама меня этому научила!"
            show bat std
            show kyr std
            with dissolve
            bat "Так вот, стоит повернуть шахматную доску и становится очевидно - девятнадцатого просто не может быть."
            bat "Ведь если он скрывается от нас, то зачем пришёл передавать письмо лично? Мог бы отправить его по почте или с одним из рыбаков в конце концов."
            bat "А это значит, что \"Беатриче\" - один из восемнадцати. Один из нас..."
            kyr "Конечно, в такой версии много пробелов..."
            show bat ace1 with vpunch
            bat "Но я заполню их и узнаю правду!"
            kyr "Именно! А ключом к разгадке будет Мария. Она ведь его видела."
            $lg+=1
        else:
            jump men1


scene bg mb room n
show bat std at left
show rud std at offscreenright
show kyr std at right
$renpy.pause(1)
play sound "sounds/sound/s/knockr.mp3"
show rud at right2 with move
rud "А, ты здесь, Кириё. Нужно ещё поговорить."
kyr "Как там отец?"
rud "Уже и не отвечает. Мы, наверное, всю ночь просидим..."
rud "А ты чем займёшься, Баттлер?"
show bat smi with dissolve
bat "Пойду в гостевой домик с Джессикой и остальными. В карты играть."
rud "Вот как..."
show rud dou with dissolve
rud "Будешь к концу разговора на ногах - побеседуем?"
show bat std with dissolve
bat "Да ты сам не свой!"
show rud smi with dissolve
stop music fadeout 4.0
rud "{cps=15}Может быть...{cps=10} меня сегодня убьют..."

##ВНИМАНИЕ:  КЛАУC ПОКАЗАЛ СЛИТОК НАТСУХИ, НО БАТТЛЕР ОБ ЭТОМ НЕ ЗНАЕТ

play music "sounds/music/bgm/The candles dance.mp3" fadein 3.0
scene bg mb cor n
show geo std at left
show jes std at right2
show bat std at right
show mar std at center
show sha std at left2
with fade
jes "О, Шанон! Пойдёшь играть с нами?"
show sha emb with dissolve
sha "Да. Господин Джордж пригласил..."
jes "Отлично! А если Канон не занят, то позови и его."
show sha std with dissolve
sha "Да! Я сейчас! Быстро догоню вас!"
show sha at offscreenleft with move
bat "Ну, двинули!"

play bgs walkw
scene bg mb cor stairs n at walking
$renpy.pause(1.5,hard=True)
show bg mb stairs down at walking
$renpy.pause(1.5,hard=True)
show bg mb hall n at walking
$renpy.pause(1.5,hard=True)
stop bgs
play bgs walk
show bg mb entrance n at walking
$renpy.pause(1.5,hard=True)
show bg garden house1 n at walking
$renpy.pause(1.5,hard=True)
show bg garden n at walking
$renpy.pause(1.5,hard=True)
show bg garden rose1 n at walking
$renpy.pause(1.5,hard=True)
show bg gh n at walking
$renpy.pause(1.5,hard=True)
stop bgs
play bgs walkw
show bg ingh cor stairs n at walking
$renpy.pause(1.5,hard=True)
show bg ingh loundge n at center
stop bgs
show geo std at left
show sha std at offscreenleft
show jes std at right2
show bat std at right
with fade
geo "Мария совсем устала. Я отнёс её в кровать."
bat "Да уж, не простой денёк."
show sha std at left2 with move
sha "Канон будет здесь. Как и Генджи с Кумасавой. Но нам дали задание патрулировать дом, следить чтоб с вами ничего не случилось."
show sha sad with dissolve
sha "Так что поиграть мы не сможем... Простите..."
geo "Ну что ты, Шанон! Ничего страшного! Пойдём-ка. Мне нужно тебе кое что сказать."
stop music fadeout 4.0
show geo at offscreenleft
show sha at offscreenleft
with move

bat "Куда это они?"
jes "Я видела у Джорджа ма-а-аленькую такую бархатную коробочку."
show bat exc with dissolve
bat "Он что, предложение собрался делать?!"
show bat smi with dissolve
bat "Я и не знал, что у них всё так серьёзно."
jes "...пойдём посмотрим?"
bat "Что?"
jes "Пойдём посмотрим! Ну же!"
show bat at offscreenleft
show jes at offscreenleft
with move

scene bg garden bush n
show bat std at left
show jes std at right
with fade
bat "Уф! Успели!"
play music "<from 23>sounds/music/bgm/Hope.mp3" fadein 2.0
jes "Тише ты!"

scene bg garden alcove n
show sha std at left2
show geo std at right2
with dissolve
show geo emb with dissolve
geo "Шанон... Нет, Саё..."
show sha emb with dissolve
sha "Господин Джордж..."
geo "Хочу показать тебе кое что."
sha "Что же?"
show geo emb1 with dissolve
geo "Вот..."
show ring with camera
geo "Возьми его."
sha "Я... Я не могу принять важе предложение."
hide ring with camerab
geo "Но я не прошу, а приказываю."
sha "Ну, раз приказываете... Придётся подчиниться."
show geo emb with dissolve
geo "Это мой последний приказ. Ответь мне завтра без слов."
sha "Как это?"
geo "Кольца носят на пальцах. Если понравилось - надень на любой."
sha "Го... Джордж..."
show geo smi with dissolve
geo "Ну, жду твоего ответа завтра."

scene bg garden bush n
show bat std at left
show jes std at right
with fade
show bat smi with dissolve
bat "Ну и хорош же братишка Джордж! Это ж надо \"Я не прошу, а приказываю\"..."
jes "Да ну тебя, дурак. Мне кажется - очень романтичная сцена."
show bat std with dissolve
bat "А вот теперь пора бежать назад, не дело это, если он раньше вернётся и..."
stop music fadeout 3.0
show bat at offscreenleft
show jes at offscreenleft
with move
$renpy.pause(2)
scene bg ingh dorm bed n
play sound flsh
show bat std at left
show letters filter
with flash

voice pm
"Остров Роккен. 5 октября 1986 год. 02:25 ночи."
play sound shut
hide letters
with flash

play music "<from 19>sounds/music/bgm/Fishy Aroma.mp3" fadein 3.0
bat "Здорово поиграли!"
bat "Хотя и трудный был денёк. С ног валюсь!"
hide screen points
play bgs pm
show screen stat
$config.allow_skipping = False
$renpy.pause(20,hard=True)
stop bgs fadeout 2
bat "Кроме того... О чём говорил отец? Об описаниях из эпитафии? Или о чём-то связаном с семейным бизнесом?"
hide screen stat

$config.allow_skipping = True
show bat smi with dissolve
bat "Ну, ладно.  Утро вечера мудренее."


stop music fadeout 3.0
scene bg black with fade
voice pm
"Так закончился первый день на острове Роккен."
voice pm
"Это начало действительно жуткой и загадочой истории."
voice pm
"И чтобы распутать её нам предстоит не только пережить три дня на Роккене, но и разгадать его тайны, а на это может уйти очень много попыток."
play sound "sounds/sound/s/horror.wav"
voice pm
"Не понимаете, о чём речь?"
voice pm
"О, уже совсем скоро поймёте."

#Эндинг
scene bg black
$ renpy.block_rollback()
$_game_menu_screen = None
$config.allow_skipping = False
play movie "images/ed.webm"
$renpy.pause(93,hard=True)
$_game_menu_screen = "save_screen"
$config.allow_skipping = True
