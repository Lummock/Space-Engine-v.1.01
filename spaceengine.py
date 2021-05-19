from typing import Mapping
from ursina import *
from random import randint, uniform
from random import choice
from ursina.shaders import basic_lighting_shader, unlit_shader
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import unlit_shader
import threading
from playsound import *

print("""
Space Engine 1.01, \"The Singularity Update\"
Made by Lummock on May 16th

Additions:
Space Background
Planetary Color Rules
Black Hole
Music
Efficient Mode
Hyperefficient Mode
Glare
Star Size Increase
Increased Planet Distance

""")

def play(sound):
    threading.Thread(target=playsound, args=(sound,), daemon=True).start()

#dev
efficientmode = False
hyperefficientmode = False





play('Space Ambience.mp3')

spedometer = 1

gassies = ['satrn.jpg', 'jupitr.jpg']
icies = ['urnas2.jpg', 'nptun2.jpeg']
terrestries = ['mrs.jpeg', 'mrcy.jpg', 'vens.jpg']
dwarfes = ['pto.jpg', 'crs']
moonse = ['encla.jpg', 'erpa.jpg', 'mun.jpg']


def update():
    global spedometer
    skee.world_position = camera.world_position
    if not hyperefficientmode:
        if held_keys['space'] != 1:
            for sun in entities:
                sun.rotation_z += time.dt*0.025 * spedometer * sun.sped
            for anchor in anchors:
                anchor.rotation_z += time.dt*0.025 * spedometer * anchor.sped
            #for planet in planets:
            #    planet.rotation_z += time.dt*planet.scale_x * 0.00325  * spedometer
            if efficientmode == False and hyperefficientmode == False:
                for moon in moons:
                    moon.rotation_z += time.dt*1 * spedometer
            Megaton2.rotation_x += time.dt*0.025 * spedometer * sun.sped
    if held_keys['shift'] == 1:
        player.speed = 100
    if held_keys['control'] == 1:
        player.speed = 1000
    elif not held_keys['shift'] == 1 and not held_keys['control'] == 1:
        player.speed = 1
    if held_keys['z'] == 1:
        player.y -= 0.0025 * time.dt * 100
        if held_keys['shift'] == 1:
            player.y -= 2.5 * time.dt * 20
        if held_keys['control'] == 1:
            player.y -= 2.5 * time.dt * 200
    if held_keys['x'] == 1:
        player.y += 0.0025 * time.dt * 100
        if held_keys['shift'] == 1:
            player.y += 2.5 * time.dt * 20
        if held_keys['control'] == 1:
            player.y += 2.5 * time.dt * 200
    if held_keys['r'] == 1:
        spedometer = 100000
    if held_keys['e'] == 1:
        spedometer = 10000
    #if held_keys['e'] != 1:
    #    spedometer = 1
    if held_keys['r'] != 1:
        spedometer = 1
        

def input(key):
    if key=='escape':
        exit()

app = Ursina()



entities = []
anchors = []
planets = []
moons = []
rings = []

#r = choice((0, 1555))
#g = choice((0, 1555))
#b = choice((0, 1555))

Helper = AmbientLight(color=color.rgb(1, 1, 1))

if hyperefficientmode:
    Helper = AmbientLight(color=color.rgb(50, 50, 50))
    rang = 500
    xyz = 40000
else:
    rang = 25
    xyz = 100

skee = Entity(model='sky_dome', texture='space6.jpg', shader=unlit_shader, scale=9900, double_sided=True, color=color.rgb(200, 200, 255))

Megaton = Entity(model='sky_dome', texture='space7.png', color=color.rgb(3000, 1000, 500), shader=unlit_shader, scale=60, x=0, y=0, z=0)
Megaton2 = Entity(model='sphere', color=color.black, shader=unlit_shader, scale=90.5, x=0, y=0, z=0)
Megaton3 = Entity(model='sky_dome', texture='space6.jpg', color=color.rgb(500, 1000, 3000), shader=unlit_shader, scale=40.9, x=0, y=0, z=0)
glare = Entity(model='plane', parent=Megaton2, scale=10, rotation_z=90, color=color.rgba(3000,300,0, 122), shader=None, rotation_y = 90, texture='glare.png', billboard=True)

for i in range(rang):

    spacepositionx = randint(-xyz, xyz)
    spacepositiony = randint(-xyz, xyz)
    spacepositionz = randint(-xyz, xyz)

    if not hyperefficientmode:
        skel = uniform(0.75, 1.50)
    else:
        skel = uniform(75, 150)

    if hyperefficientmode == False:
        Sun2 = PointLight(color=color.rgb(1555 / 100, 1555 / 100, 1555 / 100), parent=Megaton2, x=spacepositionx, y=spacepositiony, z=spacepositionz)#shadows=True)
        Sun = Entity(model='sphere', parent=Sun2, scale=(skel, skel, skel), color=color.rgb(15555,15555,15555), shader=None, sped=randint(10, 15) / 100)
        entities.append(Sun)
        glare = Entity(model='plane', parent=Sun, rotation_z=90, scale=(skel * 2, skel * 2, skel * 2), color=color.rgb(1555,1555,1555), shader=None, rotation_y = 90, texture='glare.png', billboard=True)
    else:
        Sun = Entity(model='sphere', scale=(skel, skel, skel), color=color.rgb(15555,15555,15555), shader=None, sped=randint(10, 15) / 100, x=spacepositionx, y=spacepositiony, z=spacepositionz, )


    planetypes = {
        'dwarf':0.0125,
        'terra':0.025,
        'gassy':0.20,
        'iceys':0.105,
    }
    prevx = 1.5



    for i in range(randint(2,10)):
        anchore = Entity(model='cube', parent=Sun, color=color.rgba(0, 0, 0, 0), sped=randint(10, 150) / 1000)
        anchors.append(anchore)
        scrap, siz = choice(list(planetypes.items()))
        skel = uniform(siz - (siz // 3), siz + (siz // 3))
        if scrap == 'dwarf':
            texta = choice(dwarfes)
            g = randint(-100, 100)
            b = randint(-100, 200)
            r = randint(-100, 200)
        if scrap == 'terra':
            texta = choice(terrestries)
            g = randint(-100, 100)
            b = randint(-100, 200)
            r = randint(-100, 200)
        if scrap == 'iceys':
            texta = choice(icies)
            g = randint(25, 200)
            b = randint(50, 200)
            r = randint(-100, 100)
        if scrap == 'gassy':
            texta = choice(gassies)
            g = randint(50, 100)
            b = randint(-100, 50)
            r = randint(0, 200)
        if not hyperefficientmode:
            i = Entity(parent=anchore, model='sphere', subdivisions=3, x=prevx * 1.2, y=0, z=0, scale=(skel, skel, skel), color=color.rgb(r,g,b), shader=basic_lighting_shader, texture=texta)
        else:
            i = Entity(parent=anchore, model='sphere', subdivisions=3, x=prevx * 1.3, y=0, z=0, scale=(skel, skel, skel), color=color.rgb(r,g,b))
        i.rotation_x = 90

        if not hyperefficientmode:
            print("XYZ: " + str(i.x) + " " + str(i.y) + " " + str(i.z))
            print("COLOR: " + str(r) + " " + str(g) + " " + str(b))
            planets.append(i)
        e = randint(0, 1)
        if efficientmode == False and hyperefficientmode == False:
            if skel > 1:
                r = randint(0, 4)
                if r == 2:
                    #r = uniform(0.0, 1.0)
                    r = 0
                    ring = Entity(parent=anchore, x=i.x, y=i.y, z=i.z, model='plane', scale=(i.scale_x + 2, i.scale_x + 2, i.scale_y + 2), color=color.rgba(255, 255, 255, 255), texture='ring.png', double_sided = True)
                    ring.rotation_x = 90
                    rings.append(ring)
                    #ring.rotation_x = 90
                    print("HAS RING: TRUE")
                else:
                    print("HAS RING: FALSE")
            if e == 1 or skel > 0.5:
                print("HAS MOON: TRUE")
                prevd = 0.75
                muns = randint(0, 8)
                print("NUMBER OF MOONS: " + str(muns))
                for j in range(muns):
                    scrap, siz = choice(list(planetypes.items()))
                    skel = uniform(siz - (siz // 3), siz + (siz // 3))
                    skel /= 10
                    r = randint(0, 200)
                    g = randint(0, 200)
                    b = randint(0, 200)
                    texta = choice(moonse)
                    mun = Entity(parent=i, model='sphere', x=uniform(prevd + 2, prevd * 2), y=0, z=choice((-prevd, prevd, 0)), scale=(skel, skel, skel), color=color.rgb(r,g,b), shader=basic_lighting_shader, texture=texta)
                    moons.append(mun)
        prevx *= 1.7

    #for i in range(randint(2, 7)):
    #    planit(i)

window.color = color.rgb(0, 0, 0)

player = FirstPersonController(gravity=0, speed=10)
#EditorCamera()
camera.rotation_x = 0

#player.add_script(NoclipMode())

app.run()
