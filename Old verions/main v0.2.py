import os
import time
import copy
import keyboard

# Functions


def screen_memory(y, x):
    mem = []
    for i in range(x):
        mem.append([])
        for j in range(y):
            mem[i].append(" ")

    return mem


def draw(background_d, delay, sprites_json):
    # draw sprites

    screen = copy.deepcopy(background_d)
    for sprite in sprites_json:
        for i in range(len(sprites_json[sprite]["Graphic"])):
            for j in range(len(sprites_json[sprite]["Graphic"][i])):
                screen[sprites_json[sprite]["y"]+i][sprites_json[sprite]["x"]+j] = sprites_json[sprite]["Graphic"][i][j]

    # print to screen
    time.sleep(delay)
    os.system("cls")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in screen]))
# Sprite, Axis, Amount, Sprite type it will collide with, Sprites json, display resolution


def transform(sprite, axis, change, collide_sprites, sprites_json, resolution_x, resolution_y):
    collide = False
    # Hit point
    hit_boxes = {
        "sprite_points": {

        },
        "compare_points": {

        }
    }

    # Direction stage

    x_change = 0

    y_change = 0

    if axis == "x":
        x_change = x_change + change
    elif axis == "y":
        y_change = y_change + change
    # Sprite stage
    for i in range(len(sprites_json[sprite]["Graphic"])):
        for j in range(len(sprites_json[sprite]["Graphic"][i])):
            hit_boxes["sprite_points"][f"{i},{j}"] = {}
            hit_boxes["sprite_points"][f"{i},{j}"]["x"] = j + sprites_json[sprite]["x"] + x_change
            hit_boxes["sprite_points"][f"{i},{j}"]["y"] = i + sprites_json[sprite]["y"] + y_change

    # object_s stage
    for object_s in sprites_json:
        for item in collide_sprites:
            if sprites_json[object_s]["Type"] == item:
                for i in range(len(sprites_json[object_s]["Graphic"])):
                    for j in range(len(sprites_json[object_s]["Graphic"][i])):
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"] = {}
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"]["x"] = j + sprites_json[object_s]["x"]
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"]["y"] = i + sprites_json[object_s]["y"]

    

    # Check stage
    for o_point in hit_boxes["compare_points"]:
        for s_point in hit_boxes["sprite_points"]:
            if hit_boxes["sprite_points"][s_point] == hit_boxes["compare_points"][o_point]:
                collide = True

    # Transform stage
    if not collide:
        sprites_json[sprite][axis] = sprites_json[sprite][axis] + change


def sprite_create(sprites_json, name, s_type, graphic, x, y):
    sprites_json[name] = {}
    sprites_json[name]["Type"] = s_type
    sprites_json[name]["Graphic"] = graphic
    sprites_json[name]["y"] = y
    sprites_json[name]["x"] = x


# declarations.

res_x = 30

res_y = 9

background = screen_memory(res_x, res_y)

sprites = {}

# Level Sprites

# Rock

sprite_create(sprites,  # sprites json
              "Rock_1",  # name
              "Level",  # Layer/Type
              [["+", "-", "+"],
               ["|", "1", "|"],
               ["+", "-", "+"]],
              6,  # x pos
              0  # y pos
              )

sprite_create(sprites,  # sprites json
              "Rock_2",  # name
              "Level",  # Layer/Type
              [["+", "-", "+"],
               ["|", "2", "|"],
               ["+", "-", "+"]],
              6,  # x pos
              6  # y pos
              )

sprite_create(sprites,  # sprites json
              "Rock_3",  # name
              "Level",  # Layer/Type
              [["+", "-", "+"],
               ["|", "3", "|"],
               ["+", "-", "+"]],
              12,  # x pos
              3  # y pos
              )

# Player Sprites

# Debug

sprite_create(sprites,  # sprites json
              "Debug",  # name
              "Player",  # Layer/Type
              [["X", "Y"],  # graphic
               ["3", "4"]],
              0,  # x pos
              0  # y pos
              )

# Main loop

while True:
    sprites["Debug"]["Graphic"][1] = [str(sprites["Debug"]["x"]), str(sprites["Debug"]["y"])]
    if keyboard.is_pressed('d'):
        transform("Debug", "x", 1, ["Level"], sprites, res_x, res_y)
        # Sprite, Axis, Amount, Sprite types collide with (null) for no sprites, Sprites json, display resolution
    if keyboard.is_pressed('a'):
        transform("Debug", "x", -1, ["Level"], sprites, res_x, res_y)
    if keyboard.is_pressed('s'):
        transform("Debug", "y", 1, ["Level"], sprites, res_x, res_y)
    if keyboard.is_pressed('w'):
        transform("Debug", "y", -1, ["Level"], sprites, res_x, res_y)

    draw(background, 0.1, sprites)  # BackGround Is a 2d array # Draw delay #Json which sprites are stored under
