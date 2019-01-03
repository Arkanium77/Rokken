label p:
scene bg forest stairs s
show screen Rain
with flash
show bea std at Move((1.2,0.6), (-0.2, 0.6), 5.0,xanchor="center", yanchor="center")
$renpy.pause(5)
show bg beach s with flash
show bea std at Move((1.2,0.6), (0.5, 0.6), 4.0,xanchor="center", yanchor="center")
$renpy.pause(4)
show bea sad with dissolve
$renpy.pause(2)
show bea smi_e with vpunch
$renpy.pause(1)

hide bea
show bg garden rose1 s
with fade
$renpy.pause(2)

hide screen Rain
scene bg mb cor1 at running
$ renpy.pause(1.5)
show bg mb cor stairs s at running
$ renpy.pause(1.5)
show bg mb stairs down at running
$ renpy.pause(1.5)
show bg mb hall s at running
$ renpy.pause(1.5)
show screen Rain
show bg mb entrance s at running
$ renpy.pause(1)
show bg garden house1 s at center
show bat std at Move((-0.2, 0.6), (1.2,0.6), 5.0,xanchor="center", yanchor="center")
$renpy.pause(5)
show bg garden s at center
show bat std at Move((-0.2, 0.6), (0.5,0.6), 5.0,xanchor="center", yanchor="center")
$renpy.pause(5)
show bat ace1 with vpunch
$renpy.pause(2)
hide bat

hide screen Rain
show bg mb hall portrait zorder -2 with fade
show bat smi_e at Move((-0.2, 0.6), (0.4,0.6), 5.0,xanchor="center", yanchor="center")
show bea smi_e at Move((1.2, 0.6), (0.6,0.6), 5.0,xanchor="center", yanchor="center")
$renpy.pause(5)
show letters filter zorder -1
show rk
with flash
$renpy.pause(2)

scene bg black with fade
$renpy.pause(3)
#30
