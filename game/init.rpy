#==========================================
# Определение персонажей игры.
#==========================================

###################
#Младшее поколение#
###################
#Battler
define bat = Character('Баттлер', color="#c51d34")

#Jessica
define jes = Character('Джессика', color="#FFD800")

#George
define geo = Character('Джордж', color="#140543")

#Maria
define mar = Character('Мария', color="#ffa420")


###################
#      Семья      #
###################

#Rosa
define ros = Character('Роза', color="#E28B00")

#Eva
define eva = Character('Ева', color="#ff6d0f")
#Hideyoshi
define hid = Character('Хидеёши', color="#964B00")

#Rudolf
define rud = Character('Рудольф', color="#32078D")
#Kyrie
define kyr = Character('Кириё', color="#8000FF")

#Klaus
define kla = Character('Клаус', color="#B00000")
#Natsuhi
define nat = Character('Натсухи', color="#7b199a")

#Kinzo
define kin = Character('Кинзо', color="#000000")

###################
#     Прислуга    #
###################

#Shanon
define sha = Character('Шанон', color="#490005")
#Kanon
define kan = Character('Канон', color="#808080")

#Gendji
define gen = Character('Генджи', color="#6C92AF")
#Gohda
define goh = Character('Гоуда', color="#21421E")
#Kumasawa
define kum = Character('Кумасава', color="#FC6C85")
#Nanjo
define nan = Character('Доктор Нанджо', color="#43b152")

###################
#     Прочее      #
###################

#Beatrice
define bea = Character('Беатриче', color="#ffd700")

#Letters
define letters = Character(None, kind = nvl, color="#000000")

#Narrator
define narrator = Character(None,what_slow_cps = 10,what_slow_abortable = True,what_style="lett")



#=============================================================
#Объявление изображений
#=============================================================
init:
#                         ПЕРСОНАЖИ                           #

#emoji:
#    ace (торжество)
#    ang (angry - злость)
#    dou (от Doubt - сомнение)
#    exc (от Excitement - волнение)
#    sad  (грусть)
#    smi (smile - улыбка)
#    std (standart - обычный)

#▲ Обязательные, но их может быть и больше. В таком случае они именуются ace1,sad9 и так далее. Или же постфиксом smi_evil и так далее
#Их следует добавлять после основного блока.

    ###################
    #Младшее поколение#
    ###################

    #Battler
    image bat ace= "/images/sprites/bat/ace.png"
    image bat ang= "/images/sprites/bat/ang.png"
    image bat dou= "/images/sprites/bat/dou.png"
    image bat exc= "/images/sprites/bat/exc.png"
    image bat sad= "/images/sprites/bat/sad.png"
    image bat smi= "/images/sprites/bat/smi.png"
    image bat std= "/images/sprites/bat/std.png"

    image bat ace1= "/images/sprites/bat/ace1.png"
    image bat ace_f= "/images/sprites/bat/ace#fullscreen.png"
    image bat smi_e= "/images/sprites/bat/smi#evil.png"
    image bat tau= "/images/sprites/bat/tau.png"#От taunt - насмешка, ухмылка, провокация
    #image bat std_g= "/images/sprites/bat/std#good.png"

    #Jessica
    image jes ace= "/images/sprites/jes/ace.png"
    image jes ang= "/images/sprites/jes/ang.png"
    image jes dou= "/images/sprites/jes/dou.png"
    image jes exc= "/images/sprites/jes/exc.png"
    image jes sad= "/images/sprites/jes/sad.png"
    image jes smi= "/images/sprites/jes/smi.png"
    image jes std= "/images/sprites/jes/std.png"

    image jes exc1= "/images/sprites/jes/exc1.png"

    #George
    #У джорджа много спрайтов в альтернативной позе. Возможно, стоит их использовать?
    image geo ace= "/images/sprites/geo/ace.png"
    image geo ang= "/images/sprites/geo/ang.png"
    image geo dou= "/images/sprites/geo/dou.png"
    image geo exc= "/images/sprites/geo/exc.png"
    image geo sad= "/images/sprites/geo/sad.png"
    image geo smi= "/images/sprites/geo/smi.png"
    image geo std= "/images/sprites/geo/std.png"

    #embarrassment - emb - смущение
    image geo emb= "/images/sprites/geo/emb.png"
    image geo emb1= "/images/sprites/geo/emb1.png"
    image geo exc1= "/images/sprites/geo/exc1.png"

    #Maria
    image mar ace= "/images/sprites/mar/ace.png"
    image mar ang= "/images/sprites/mar/ang.png"
    image mar dou= "/images/sprites/mar/dou.png"
    image mar exc= "/images/sprites/mar/exc.png"
    image mar sad= "/images/sprites/mar/sad.png"
    image mar smi= "/images/sprites/mar/smi.png"
    image mar std= "/images/sprites/mar/std.png"

    image mar exc1= "/images/sprites/mar/exc1.png"
    image mar ace1= "/images/sprites/mar/ace1.png"

    ###################
    #      Семья      #
    ###################

    #Rosa
    image ros ace= "/images/sprites/ros/ace.png"
    image ros ang= "/images/sprites/ros/ang.png"
    image ros dou= "/images/sprites/ros/dou.png"
    image ros exc= "/images/sprites/ros/exc.png"
    image ros sad= "/images/sprites/ros/sad.png"
    image ros smi= "/images/sprites/ros/smi.png"
    image ros std= "/images/sprites/ros/std.png"

    image ros exc1= "/images/sprites/ros/exc1.png"
    image ros dou1= "/images/sprites/ros/dou1.png"
    image ros sad1= "/images/sprites/ros/sad1.png"
    image ros ang1= "/images/sprites/ros/ang1.png"


    #Eva
    image eva ace= "/images/sprites/eva/ace.png"
    image eva ang= "/images/sprites/eva/ang.png"
    image eva dou= "/images/sprites/eva/dou.png"
    image eva exc= "/images/sprites/eva/exc.png"
    image eva sad= "/images/sprites/eva/sad.png"
    image eva smi= "/images/sprites/eva/smi.png"
    image eva std= "/images/sprites/eva/std.png"

    image eva exc1= "/images/sprites/eva/exc1.png"
    image eva dou1= "/images/sprites/eva/dou1.png"
    image eva ace1= "/images/sprites/eva/ace1.png"

    #Hideyoshi
    image hid ace= "/images/sprites/hid/ace.png"
    image hid ang= "/images/sprites/hid/ang.png"
    image hid dou= "/images/sprites/hid/dou.png"
    image hid exc= "/images/sprites/hid/exc.png"
    image hid sad= "/images/sprites/hid/sad.png"
    image hid smi= "/images/sprites/hid/smi.png"
    image hid std= "/images/sprites/hid/std.png"


    #Rudolf
    image rud ace= "/images/sprites/rud/ace.png"
    image rud ang= "/images/sprites/rud/ang.png"
    image rud dou= "/images/sprites/rud/dou.png"
    image rud exc= "/images/sprites/rud/exc.png"
    image rud sad= "/images/sprites/rud/sad.png"
    image rud smi= "/images/sprites/rud/smi.png"
    image rud std= "/images/sprites/rud/std.png"

    image rud exc1= "/images/sprites/rud/exc1.png"
    image rud sad1= "/images/sprites/rud/sad1.png"

    #Kyrie
    image kyr ace= "/images/sprites/kyr/ace.png"
    image kyr ang= "/images/sprites/kyr/ang.png"
    image kyr dou= "/images/sprites/kyr/dou.png"
    image kyr exc= "/images/sprites/kyr/exc.png"
    image kyr sad= "/images/sprites/kyr/sad.png"
    image kyr smi= "/images/sprites/kyr/smi.png"
    image kyr std= "/images/sprites/kyr/std.png"

    image kyr dou1= "/images/sprites/kyr/dou1.png"


    #Klaus
    image kla ace= "/images/sprites/kla/ace.png"
    image kla ang= "/images/sprites/kla/ang.png"
    image kla dou= "/images/sprites/kla/dou.png"
    image kla exc= "/images/sprites/kla/exc.png"
    image kla sad= "/images/sprites/kla/sad.png"
    image kla smi= "/images/sprites/kla/smi.png"
    image kla std= "/images/sprites/kla/std.png"

    image kla exc1= "/images/sprites/kla/exc1.png"
    image kla tau= "/images/sprites/kla/tau.png"

    #Natsuhi
    image nat ace= "/images/sprites/nat/ace.png"
    image nat ang= "/images/sprites/nat/ang.png"
    image nat dou= "/images/sprites/nat/dou.png"
    image nat exc= "/images/sprites/nat/exc.png"
    image nat sad= "/images/sprites/nat/sad.png"
    image nat smi= "/images/sprites/nat/smi.png"
    image nat std= "/images/sprites/nat/std.png"

    image nat sad1= "/images/sprites/nat/sad1.png"


    #Kinzo
    image kin ace= "/images/sprites/kin/ace.png"
    image kin ang= "/images/sprites/kin/ang.png"
    image kin dou= "/images/sprites/kin/dou.png"
    image kin exc= "/images/sprites/kin/exc.png"
    image kin sad= "/images/sprites/kin/sad.png"
    image kin smi= "/images/sprites/kin/smi.png"
    image kin std= "/images/sprites/kin/std.png"

    image kin ystd= "/images/sprites/kin/ystd.png"
    image kin yace= "/images/sprites/kin/yace.png"
    image kin ysad= "/images/sprites/kin/ysad.png"

    ###################
    #     Прислуга    #
    ###################

    #Shanon
    image sha ace= "/images/sprites/sha/ace.png"
    image sha ang= "/images/sprites/sha/ang.png"
    image sha dou= "/images/sprites/sha/dou.png"
    image sha exc= "/images/sprites/sha/exc.png"
    image sha sad= "/images/sprites/sha/sad.png"
    image sha smi= "/images/sprites/sha/smi.png"
    image sha std= "/images/sprites/sha/std.png"

    image sha emb= "/images/sprites/sha/emb.png"
    image sha emb1= "/images/sprites/sha/emb1.png"

    #Kanon
    image kan ace= "/images/sprites/kan/ace.png"
    image kan ang= "/images/sprites/kan/ang.png"
    image kan dou= "/images/sprites/kan/dou.png"
    image kan exc= "/images/sprites/kan/exc.png"
    image kan sad= "/images/sprites/kan/sad.png"
    image kan smi= "/images/sprites/kan/smi.png"
    image kan std= "/images/sprites/kan/std.png"


    #Gendji
    image gen ace= "/images/sprites/gen/ace.png"
    #image gen ang= "/images/sprites/gen/ang.png"    #Нет у него злости
    image gen dou= "/images/sprites/gen/dou.png"
    image gen exc= "/images/sprites/gen/exc.png"
    image gen sad= "/images/sprites/gen/sad.png"
    #image gen smi= "/images/sprites/gen/smi.png"    #Нет у него улыбки
    image gen std= "/images/sprites/gen/std.png"

    #Gohda
    image goh ace= "/images/sprites/goh/ace.png"
    image goh ang= "/images/sprites/goh/ang.png"
    image goh dou= "/images/sprites/goh/dou.png"
    image goh exc= "/images/sprites/goh/exc.png"
    image goh sad= "/images/sprites/goh/sad.png"
    image goh smi= "/images/sprites/goh/smi.png"
    image goh std= "/images/sprites/goh/std.png"

    image goh exc1= "/images/sprites/goh/exc1.png"

    #Kumasawa
    image kum ace= "/images/sprites/kum/ace.png"
    image kum ang= "/images/sprites/kum/dou.png" #ang и doa исполняет один и тот же спрайт
    image kum dou= "/images/sprites/kum/dou.png"
    image kum exc= "/images/sprites/kum/exc.png"
    image kum sad= "/images/sprites/kum/sad.png"
    image kum smi= "/images/sprites/kum/smi.png"
    image kum std= "/images/sprites/kum/std.png"

    #Nanjo
    image nan ace= "/images/sprites/nan/ace.png"
    image nan ang= "/images/sprites/nan/ang.png"
    image nan dou= "/images/sprites/nan/dou.png"
    image nan exc= "/images/sprites/nan/exc.png"
    image nan sad= "/images/sprites/nan/sad.png"
    image nan smi= "/images/sprites/nan/smi.png"
    image nan std= "/images/sprites/nan/std.png"


    ###################
    #     Прочее      #
    ###################

    #Beatrice
    image bea ace= "/images/sprites/bea/ace.png"
    image bea ang= "/images/sprites/bea/ang.png"
    image bea dou= "/images/sprites/bea/dou.png"
    image bea exc= "/images/sprites/bea/exc.png"
    image bea sad= "/images/sprites/bea/sad.png"
    image bea smi= "/images/sprites/bea/smi.png"
    image bea std= "/images/sprites/bea/std.png"

    image bea ang1= "/images/sprites/bea/ang1.png"
    image bea dou1= "/images/sprites/bea/dou1.png"
    image bea smi1= "/images/sprites/bea/smi1.png"
    image bea smi_e= "/images/sprites/bea/smi#evil.png"
    image bea smi_e1= "/images/sprites/bea/smi#evil1.png"


    #Letters
    image letters filter= "/images/bg/filter.png"



#                         ФОНЫ                           #

#day:
#    m   (morning - утро)
#    e   (evening - вечер)
#    n   (night - ночь)

#weather:
#    s   (storm - буря)

#situation
#    rest  (отдых)
#    sky   (небо)
#    up    (вверх)
#    mb    (mainbuilding - главное здание)
#    far   (далеко)
#    rev   (reverse - задний)


#▲ Обязательные, но их может быть и больше.
#Их следует добавлять после основного блока.

    ###################
    #       Пляж      #
    ###################

    image bg beach ls m= "/images/bg/beach/beach_landscape_mor.bmp"
    image bg beach ls n= "/images/bg/beach/beach_landscape_night.bmp"
    image bg beach ls s= "/images/bg/beach/beach_landscape_storm.bmp"
    image bg beach ls1 m= "/images/bg/beach/beach_landscape1.bmp"
    image bg beach ls1 n= "/images/bg/beach/beach_landscape1_night.bmp"
    image bg beach ls1 s= "/images/bg/beach/beach_landscape1_storm.bmp"

    image bg beach m= "/images/bg/beach/beach_mor.bmp"
    image bg beach s= "/images/bg/beach/beach_storm.bmp"
    image bg beach rest= "/images/bg/beach/beach_rest.bmp"
    image bg beach rest s= "/images/bg/beach/beach_rest_storm.bmp"

    image bg beach sky= "/images/bg/beach/beach_sky.bmp"

    image bg beach stairs= "/images/bg/beach/beach_stairs.bmp"
    image bg beach stairs up= "/images/bg/beach/beach_stairs_up.bmp"
    image bg beach stairs up1= "/images/bg/beach/beach_stairs_up1.bmp"

    image bg beach cliff= "/images/bg/beach/cliff.bmp"
    image bg beach cliff up= "/images/bg/beach/cliff_up.bmp"

    ###################
    #       Лес       #
    ###################

    image bg forest path m= "/images/bg/forest/forest_path.bmp"
    image bg forest path n= "/images/bg/forest/forest_path_night.bmp"
    image bg forest path s= "/images/bg/forest/forest_path_storm.bmp"
    image bg forest path1 m= "/images/bg/forest/forest_path1.bmp"
    image bg forest path1 n= "/images/bg/forest/forest_path1_night.bmp"
    image bg forest path1 s= "/images/bg/forest/forest_path1_storm.bmp"

    image bg forest stairs m= "/images/bg/forest/forest_stairs.bmp"
    image bg forest stairs n= "/images/bg/forest/forest_stairs_night.bmp"
    image bg forest stairs s= "/images/bg/forest/forest_stairs_storm.bmp"
    image bg forest stairs mb= "/images/bg/forest/stairs_mb.bmp"

    image bg forest tower n= "/images/bg/forest/night_tower.bmp"

    image bg forest well m= "/images/bg/forest/well.bmp"
    image bg forest well n= "/images/bg/forest/well_night.bmp"
    image bg forest well s= "/images/bg/forest/well_storm.bmp"
    image bg forest well far m= "/images/bg/forest/well_far.bmp"
    image bg forest well far n= "/images/bg/forest/well_far_night.bmp"
    image bg forest well far s= "/images/bg/forest/well_far_storm.bmp"

    ###################
    #       Сад       #
    ###################

    #alcove
    image bg garden alcove m= "/images/bg/garden/alcove/alcove_m.bmp"
    image bg garden alcove n= "/images/bg/garden/alcove/alcove_night.bmp"
    image bg garden alcove s= "/images/bg/garden/alcove/alcove_storm.bmp"

    #garden
    image bg garden arch= "/images/bg/garden/garden/arch.bmp"
    image bg garden bush= "/images/bg/garden/garden/bush_secret.bmp"
    image bg garden bush n= "/images/bg/garden/garden/bush_secret_night.bmp"
    image bg garden build= "/images/bg/garden/garden/garden_building.bmp"
    image bg garden build1= "/images/bg/garden/garden/garden_building1.bmp"
    image bg garden build2= "/images/bg/garden/garden/garden_building2.bmp"
    image bg garden build3= "/images/bg/garden/garden/garden_building3.bmp"

    image bg garden m= "/images/bg/garden/garden/garden.bmp"
    image bg garden n= "/images/bg/garden/garden/garden_night.bmp"
    image bg garden s= "/images/bg/garden/garden/garden_storm.bmp"

    image bg garden rose m= "/images/bg/garden/garden/rose.bmp"
    image bg garden rose n= "/images/bg/garden/garden/rose_night.bmp"
    image bg garden rose s= "/images/bg/garden/garden/rose_storm.bmp"
    image bg garden rose1 m= "/images/bg/garden/garden/rose1.bmp"
    image bg garden rose1 n= "/images/bg/garden/garden/rose1_night.bmp"
    image bg garden rose1 s= "/images/bg/garden/garden/rose1_storm.bmp"
    image bg garden roses m= "/images/bg/garden/garden/roses.bmp"
    image bg garden roses n= "/images/bg/garden/garden/roses_night.bmp"

    #house
    image bg garden house m= "/images/bg/garden/house/house.bmp"
    image bg garden house n= "/images/bg/garden/house/house_night.bmp"
    image bg garden house s= "/images/bg/garden/house/house_storm.bmp"
    image bg garden house1 m= "/images/bg/garden/house/house1.bmp"
    image bg garden house1 n= "/images/bg/garden/house/house1_night.bmp"
    image bg garden house1 s= "/images/bg/garden/house/house1_storm.bmp"
    image bg garden house2 m= "/images/bg/garden/house/house2.bmp"
    image bg garden house2 n= "/images/bg/garden/house/house2_night.bmp"
    image bg garden house2 s= "/images/bg/garden/house/house2_storm.bmp"
    image bg garden house3 m= "/images/bg/garden/house/house3.bmp"

    ############################
    #  Гостевой дом (с улицы)  #
    ############################

    image bg gh m= "/images/bg/guesthouse/guesthouse.bmp"
    image bg gh n= "/images/bg/guesthouse/guesthouse_night.bmp"
    image bg gh s= "/images/bg/guesthouse/guesthouse_storm.bmp"

    image bg gh1 m= "/images/bg/guesthouse/guesthouse1.bmp"
    image bg gh1 n= "/images/bg/guesthouse/guesthouse1_night.bmp"
    image bg gh1 s= "/images/bg/guesthouse/guesthouse1_storm.bmp"

    ####################
    #  Главное здание  #
    ####################

    #corridors
    image bg mb cor= "/images/bg/mb/corridors/cor.bmp"
    image bg mb cor n= "/images/bg/mb/corridors/cor_night.bmp"
    image bg mb cor s= "/images/bg/mb/corridors/cor_storm.bmp"

    image bg mb cor stairs= "/images/bg/mb/corridors/cor_stairs.bmp"
    image bg mb cor stairs n= "/images/bg/mb/corridors/cor_stairs_night.bmp"
    image bg mb cor stairs s= "/images/bg/mb/corridors/cor_stairs_storm.bmp"

    image bg mb cor1= "/images/bg/mb/corridors/cor1.bmp"

    image bg mb cor2= "/images/bg/mb/corridors/cor2.bmp"
    image bg mb cor2 n= "/images/bg/mb/corridors/cor2_night.bmp"
    image bg mb cor2 s= "/images/bg/mb/corridors/cor2_storm.bmp"

    image bg mb door= "/images/bg/mb/corridors/door.bmp"
    image bg mb door close= "/images/bg/mb/corridors/doo_closer.bmp"

    image bg mb wdw m= "/images/bg/mb/corridors/window.bmp"
    image bg mb wdw n= "/images/bg/mb/corridors/window_night.bmp"
    image bg mb wdw s= "/images/bg/mb/corridors/window_storm.bmp"

    image bg mb stairs close= "/images/bg/mb/corridors/stairs_close.bmp"
    image bg mb stairs down= "/images/bg/mb/corridors/stairs_down.bmp"
    image bg mb stairs up= "/images/bg/mb/corridors/stairs_up.bmp"

    #rooms
    image bg mb cab m= "/images/bg/mb/rooms/cab.bmp"
    image bg mb cab n= "/images/bg/mb/rooms/cab_night.bmp"
    image bg mb cab s= "/images/bg/mb/rooms/cab_storm.bmp"
    image bg mb cab1 m= "/images/bg/mb/rooms/cab1.bmp"
    image bg mb cab1 n= "/images/bg/mb/rooms/cab1_night.bmp"
    image bg mb cab1 s= "/images/bg/mb/rooms/cab1_storm.bmp"
    image bg mb cab rev m= "/images/bg/mb/rooms/cab_reverse.bmp"
    image bg mb cab rev n= "/images/bg/mb/rooms/cab_reverse_night.bmp"
    image bg mb cab rev s= "/images/bg/mb/rooms/cab_reverse_storm.bmp"

    image bg mb dining= "/images/bg/mb/rooms/dining.bmp"
    image bg mb dining center= "/images/bg/mb/rooms/dining_center.bmp"
    image bg mb dining center n= "/images/bg/mb/rooms/dining_center_night.bmp"
    image bg mb dining center s= "/images/bg/mb/rooms/dining_center_storm.bmp"
    image bg mb dining rev= "/images/bg/mb/rooms/dining_reverse.bmp"

    image bg mb hall m= "/images/bg/mb/rooms/hall.bmp"
    image bg mb hall n= "/images/bg/mb/rooms/hall_night.bmp"
    image bg mb hall s= "/images/bg/mb/rooms/hall_storm.bmp"
    image bg mb hall portrait= "/images/bg/mb/rooms/hall_portrait.bmp"
    image bg mb hall stairs m= "/images/bg/mb/rooms/hall_stairs.bmp"
    image bg mb hall stairs n= "/images/bg/mb/rooms/hall_stairs_night.bmp"
    image bg mb hall stairs1 m= "/images/bg/mb/rooms/hall_stairs1.bmp"
    image bg mb hall stairs1 n= "/images/bg/mb/rooms/hall_stairs1_night.bmp"
    image bg mb hall stairs1 s= "/images/bg/mb/rooms/hall_stairs1_storm.bmp"

    image bg mb kitchen m= "/images/bg/mb/rooms/kitchen.bmp"
    image bg mb kitchen n= "/images/bg/mb/rooms/kitchen_night.bmp"
    image bg mb kitchen s= "/images/bg/mb/rooms/kitchen_storm.bmp"
    image bg mb kitchen rev= "/images/bg/mb/rooms/kitchen_reverse.bmp"

    image bg mb loundge m= "/images/bg/mb/rooms/loundge.bmp"
    image bg mb loundge n= "/images/bg/mb/rooms/loundge_night.bmp"
    image bg mb loundge s= "/images/bg/mb/rooms/loundge_storm.bmp"
    image bg mb loundge rev= "/images/bg/mb/rooms/loundge_reverse.bmp"
    image bg mb loundge1 m= "/images/bg/mb/rooms/loundge2.bmp"

    image bg mb portrait m= "/images/bg/mb/rooms/portrait.bmp"
    image bg mb portrait1 m= "/images/bg/mb/rooms/portrait1.bmp"
    image bg mb portrait1 n= "/images/bg/mb/rooms/portrait1_night.bmp"

    image bg mb room m= "/images/bg/mb/rooms/room.bmp"
    image bg mb room n= "/images/bg/mb/rooms/room_night.bmp"
    image bg mb room s= "/images/bg/mb/rooms/room_storm.bmp"

    image bg mb room jes m= "/images/bg/mb/rooms/room_jes.bmp"
    image bg mb room jes n= "/images/bg/mb/rooms/room_jes_night.bmp"
    image bg mb room jes rev= "/images/bg/mb/rooms/room_jes_reverse.bmp"
    image bg mb room jes rev n= "/images/bg/mb/rooms/room_jes_reverse_night.bmp"
    image bg mb room jes rev s= "/images/bg/mb/rooms/room_jes_reverse_storm.bmp"

    image bg mb room nat m= "/images/bg/mb/rooms/room_nat.bmp"
    image bg mb room nat n= "/images/bg/mb/rooms/room_nat_night.bmp"
    image bg mb room nat rev= "/images/bg/mb/rooms/room_nat_reverse.bmp"

    image bg mb servant m= "/images/bg/mb/rooms/servant.bmp"
    image bg mb servant n= "/images/bg/mb/rooms/servant_night.bmp"
    image bg mb servant s= "/images/bg/mb/rooms/servant_storm.bmp"

    image bg mb vip m= "/images/bg/mb/rooms/vip.bmp"
    image bg mb vip n= "/images/bg/mb/rooms/vip_night.bmp"
    image bg mb vip s= "/images/bg/mb/rooms/vip_storm.bmp"
    image bg mb vip rev= "/images/bg/mb/rooms/vip_reverse.bmp"
    image bg mb vip wdw m= "/images/bg/mb/rooms/vip_window.bmp"
    image bg mb vip wdw n= "/images/bg/mb/rooms/vip_window_night.bmp"
    image bg mb vip wdw s= "/images/bg/mb/rooms/vip_window_storm.bmp"

    #other
    image bg mb backd m= "/images/bg/mb/backdoor.bmp"
    image bg mb backd n= "/images/bg/mb/backdoor_night.bmp"
    image bg mb backd s= "/images/bg/mb/backdoor_storm.bmp"

    image bg mb boil= "/images/bg/mb/boil.bmp"
    image bg mb boil1= "/images/bg/mb/boil1.bmp"

    image bg mb entrance m= "/images/bg/mb/mb_entrance.bmp"
    image bg mb entrance n= "/images/bg/mb/mb_entrance_night.bmp"
    image bg mb entrance s= "/images/bg/mb/mb_entrance_storm.bmp"

    ###################
    #     Остров      #
    ###################

    image bg island= "/images/bg/island/island.bmp"
    image bg island far= "/images/bg/island/island_far.bmp"
    image bg island1 far= "/images/bg/island/island1_far.bmp"
    image bg island up= "/images/bg/island/island_up.bmp"
    image bg island chapel= "/images/bg/island/chapel.bmp"

    ###################
    # Гостевой домик  #
    ###################

    #rooms
    image bg ingh dining= "/images/bg/insidegh/rooms/dining.bmp"

    image bg ingh dorm= "/images/bg/insidegh/rooms/dorm.bmp"
    image bg ingh dorm n= "/images/bg/insidegh/rooms/dorm_night.bmp"
    image bg ingh dorm s= "/images/bg/insidegh/rooms/dorm_storm.bmp"
    image bg ingh dorm bed= "/images/bg/insidegh/rooms/dorm_bed.bmp"
    image bg ingh dorm bed n= "/images/bg/insidegh/rooms/dorm_bed_night.bmp"
    image bg ingh dorm bed s= "/images/bg/insidegh/rooms/dorm_ded_storm.bmp"

    image bg ingh library= "/images/bg/insidegh/rooms/library.bmp"

    image bg ingh loundge= "/images/bg/insidegh/rooms/loundge.bmp"
    image bg ingh loundge n= "/images/bg/insidegh/rooms/loundge_night.bmp"
    image bg ingh loundge s= "/images/bg/insidegh/rooms/loundge_storm.bmp"
    image bg ingh loundge special= "/images/bg/insidegh/rooms/loundge_special.bmp"
    image bg ingh loundge rev= "/images/bg/insidegh/rooms/loundge_reverse.bmp"
    image bg ingh loundge rev n= "/images/bg/insidegh/rooms/loundge_reverse_night.bmp"
    image bg ingh loundge rev s= "/images/bg/insidegh/rooms/loundge_reverse_storm.bmp"

    image bg ingh room= "/images/bg/insidegh/rooms/room.bmp"
    image bg ingh room n= "/images/bg/insidegh/rooms/room_night.bmp"
    image bg ingh room s= "/images/bg/insidegh/rooms/room_storm.bmp"
    image bg ingh room bed= "/images/bg/insidegh/rooms/room_bed.bmp"
    image bg ingh room bed n= "/images/bg/insidegh/rooms/room_bed_night.bmp"

    image bg ingh servant= "/images/bg/insidegh/rooms/servant.bmp"

    #corridors
    image bg ingh cor m= "/images/bg/insidegh/corridors/cor.bmp"
    image bg ingh cor n= "/images/bg/insidegh/corridors/cor_night.bmp"
    image bg ingh cor s= "/images/bg/insidegh/corridors/cor_storm.bmp"

    image bg ingh cor stairs= "/images/bg/insidegh/corridors/cor_stairs.bmp"
    image bg ingh cor stairs n= "/images/bg/insidegh/corridors/cor_stairs_night.bmp"
    image bg ingh cor stairs s= "/images/bg/insidegh/corridors/cor_stairs_storm.bmp"
    image bg ingh cor door m= "/images/bg/insidegh/corridors/stairs_door.bmp"
    image bg ingh cor door n= "/images/bg/insidegh/corridors/stairs_door_night.bmp"

    ###################
    #      Море       #
    ###################

    image bg sea m= "/images/bg/sea/sea.bmp"
    image bg sea waves= "/images/bg/sea/waves.bmp"
    image bg sea waves1= "/images/bg/sea/waves1.bmp"
    image bg sea waves s= "/images/bg/sea/waves_storm.bmp"

    ###################
    #      Порт       #
    ###################

    image bg ship port= "/images/bg/ship/port.bmp"

    image bg ship m= "/images/bg/ship/ship.bmp"
    image bg ship s= "/images/bg/ship/ship_storm.bmp"
    image bg ship inside= "/images/bg/ship/ship_inside.bmp"
    image bg ship left= "/images/bg/ship/ship_left.bmp"
    image bg ship starboard= "/images/bg/ship/starboard.bmp"
    image bg ship1 m= "/images/bg/ship/ship1.bmp"

    ###################
    #      Небо       #
    ###################

    image bg sky m= "/images/bg/sky/sky.bmp"
    image bg sky e= "/images/bg/sky/sky_even.bmp"
    image bg sky s= "/images/bg/sky/sky_storm.bmp"
    image bg sky1 e= "/images/bg/sky/sky_even2.bmp"

    ###################
    #   Подземелье    #
    ###################

    image bg subway arch= "/images/bg/subway/subway_arch.bmp"
    image bg subway arch1= "/images/bg/subway/subway1_arch.bmp"

    image bg subway bridge= "/images/bg/subway/subway_bridge.bmp"
    image bg subway bridge1= "/images/bg/subway/subway1_bridge.bmp"

    image bg subway door= "/images/bg/subway/subway_door.bmp"
    image bg subway room= "/images/bg/subway/subway_room.bmp"
    image bg subway stairs= "/images/bg/subway/subway_stairs.bmp"
    image bg subway wall= "/images/bg/subway/subway_wall.bmp"

    ###################
    #    Подсобка     #
    ###################

    image bg wh= "/images/bg/warehouse/warehouse.bmp"
    image bg wh1= "/images/bg/warehouse/warehouse1.bmp"

    image bg wh gate= "/images/bg/warehouse/gate.bmp"
    image bg wh gate1= "/images/bg/warehouse/gate1.bmp"



    ###################
    #     Прочее      #
    ###################
    image bg clock="clockcity.jpg"
    image bg horror="horror.jpg"
    image bg horror1="/images/bg/horror1.jpg"
    image bg magiclibrary="magiclibrary.jpg"
    image bg library="library.jpg"
    image bg mansion="mansion.jpg"
    image bg mansion_w="mansion_wood.jpg"
    image bg office="office.jpg"
    image bg office_s="office_simple.jpg"

    image bg rosewide="/images/bg/rosewide.bmp"
    image bg room_true="room_true.jpg"
    image bg rain_static="/images/bg/rain.png"
    image bg scorpio="/images/bg/scorpio.png"
    image bg letter="/images/bg/letter.png"
    image bg ring="/images/bg/ring.png"
    image bg black="/images/bg/black.png"
    image rk="images/rok1.png"
    image rose_cg="/images/bg/rose.png"
    image rose1_cg="/images/bg/rose1.png"

    ###################
    #     ЗВУКИ       #
    ###################
    $pm="sounds/sound/pm2.mp3"#pm.mp3, pm1.mp3, pm2.mp3
    $run="sounds/sound/run.mp3"
    $runw="sounds/sound/runw.mp3"
    $walk="sounds/sound/walk.mp3"
    $walkw="sounds/sound/walkw.mp3"
    $shut="sounds/sound/shut.mp3"
    $flsh="sounds/sound/flsh.mp3"

    ###################
    #     МУЗЫКА      #
    ###################



    #
    #
    #
    init:
        $ camera = ImageDissolve("images/bg/camera.png", 0.5, 100, reverse=False)
        $ camerab = ImageDissolve("images/bg/camera.png", 0.5, 100, reverse=True)
