import os
import time
import copy


def screen_memory(y, x):
    mem = []
    for i in range(x):
        mem.append([])
        for j in range(y):
            mem[i].append(" ")

    return mem


def ter_draw(background_d, delay, sprites_json):
    # draw sprites

    screen = copy.deepcopy(background_d)
    for sprite in sprites_json:
        if not(sprites_json[sprite]["Type"] == "DEAD"):
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
            if sprites_json[object_s]["Type"] == item and not(sprites_json[sprite]["Type"] == "DEAD"):
                for i in range(len(sprites_json[object_s]["Graphic"])):
                    for j in range(len(sprites_json[object_s]["Graphic"][i])):
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"] = {}
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"]["x"] = j + sprites_json[object_s]["x"]
                        hit_boxes["compare_points"][f"{object_s}:{i},{j}"]["y"] = i + sprites_json[object_s]["y"]

    # Memory protect stage

    # Top and bottom sides for memory

    for j in range(resolution_y):
        hit_boxes["compare_points"][f"Stage x:{-1},{j}"] = {}
        hit_boxes["compare_points"][f"Stage x:{-1},{j}"]["x"] = -1
        hit_boxes["compare_points"][f"Stage x:{-1},{j}"]["y"] = j

    for j in range(resolution_y):
        hit_boxes["compare_points"][f"Stage x:{resolution_x},{j}"] = {}
        hit_boxes["compare_points"][f"Stage x:{resolution_x},{j}"]["x"] = resolution_x
        hit_boxes["compare_points"][f"Stage x:{resolution_x},{j}"]["y"] = j

    # Left and right sides for memory

    for j in range(resolution_x):
        hit_boxes["compare_points"][f"Stage y:{j},{-1}"] = {}
        hit_boxes["compare_points"][f"Stage y:{j},{-1}"]["x"] = j
        hit_boxes["compare_points"][f"Stage y:{j},{-1}"]["y"] = -1

    for j in range(resolution_x):
        hit_boxes["compare_points"][f"Stage y:{j},{resolution_y}"] = {}
        hit_boxes["compare_points"][f"Stage y:{j},{resolution_y}"]["x"] = j
        hit_boxes["compare_points"][f"Stage y:{j},{resolution_y}"]["y"] = resolution_y

    # Check stage
    for o_point in hit_boxes["compare_points"]:
        for s_point in hit_boxes["sprite_points"]:
            if hit_boxes["sprite_points"][s_point] == hit_boxes["compare_points"][o_point]:
                collide = True

    # Transform stage
    if not collide:
        sprites_json[sprite][axis] = sprites_json[sprite][axis] + change


def collision(sprite, collide_sprites, sprites_json):
    collide = False
    # Hit point
    hit_boxes = {
        "sprite_points": {

        },
        "compare_points": {

        }
    }

    # Sprite stage
    for i in range(len(sprites_json[sprite]["Graphic"])):
        for j in range(len(sprites_json[sprite]["Graphic"][i])):
            hit_boxes["sprite_points"][f"{i},{j}"] = {}
            hit_boxes["sprite_points"][f"{i},{j}"]["x"] = j + sprites_json[sprite]["x"]
            hit_boxes["sprite_points"][f"{i},{j}"]["y"] = i + sprites_json[sprite]["y"]

    # object_s stage
    for object_s in sprites_json:
        for item in collide_sprites:
            if sprites_json[object_s]["Type"] == item and not(sprites_json[sprite]["Type"] == "DEAD"):
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
    return collide


def sprite_create(sprites_json, name, s_type, graphic, x, y):
    sprites_json[name] = {}
    sprites_json[name]["Type"] = s_type
    sprites_json[name]["Graphic"] = graphic
    sprites_json[name]["y"] = y
    sprites_json[name]["x"] = x
