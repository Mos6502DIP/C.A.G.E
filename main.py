import os
import time
import copy
import keyboard



def screen_memory(y, x):
    mem = []
    for i in range(x):
        mem.append([])
        if i % 2 == 0:
            for j in range(y):
                if j % 2 == 0:
                    mem[i].append(" ")
                else:
                    mem[i].append("#")
        else:
            for j in range(y):
                if j % 2 == 0:
                    mem[i].append("#")
                else:
                    mem[i].append(" ")
    return mem


def draw(background, delay, sprites):
    #draw sprites

    screen = copy.deepcopy(background)
    for sprite in sprites:
        for i in range(len(sprites[sprite]["graphic"])):
            for j in range(len(sprites[sprite]["graphic"][i])):
                screen[sprites[sprite]["y"]+i][sprites[sprite]["x"]+j] = sprites[sprite]["graphic"][i][j]

    #print to screen
    time.sleep(delay)
    os.system("cls")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in screen]))


# declarations.
background = screen_memory(30, 9)

sprites = {}

sprites["Apple"] = {}

sprites["Apple"]["graphic"] = [["1","2"],["3","4"]]

sprites["Apple"]["y"] = 0

sprites["Apple"]["x"] = 0




# main loop
while True:
    draw(background, 0.2, sprites) #BackGround Is a 2d array # Draw delay #Json which sprites are stored under
    if keyboard.is_pressed('d'):
        sprites["Apple"]["x"] += 1
        print("Right")
    if keyboard.is_pressed('a'):
        sprites["Apple"]["x"] -= 1
        print("Left")
    if keyboard.is_pressed('s'):
        sprites["Apple"]["y"] += 1
        print("Down")

    if keyboard.is_pressed('w'):
        sprites["Apple"]["y"] -= 1
        print("up")







