import os
import time
import copy
import keyboard

# Functions

def screen_memory(y: int, x: int) -> list[list[str]]:
    """
    Creates a 2D array to store screen data

    Uses list comprehension for increased performance
    """

    return [[" " for j in range(y)] for i in range(x)] # Use list comprehension for increased performance


def draw(background_d: list, delay: float | int, sprites_json: dict) -> None:
    """
    Draws all sprites to the screen memory then updates the screen
    """

    # Make a copy of the screen parsed
    screen = copy.deepcopy(background_d)

    # Loop over all sprites in the json and render each one chunk by chunk
    for sprite in sprites_json:
        for i in range(len(sprites_json[sprite]["Graphic"])):
            for j in range(len(sprites_json[sprite]["Graphic"][i])):
                screen[sprites_json[sprite]["y"]+i][sprites_json[sprite]["x"]+j] = sprites_json[sprite]["Graphic"][i][j]

    # Clear the terminal and then print screen memory
    time.sleep(delay)
    os.system("cls")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in screen]))


# Sprite, Axis, Amount, Sprite type it will collide with, Sprites json, display resolution


def transform(sprite: dict, axis: str, change: float | int, collide_sprites: list, sprites_json: dict, resolution_x: int, resolution_y: int) -> None:
    """
    Translate (?) a sprite along a given axis at specified distance.
    Only if it does not collide with any sprites parsed as a parameter
    """
    collide = False
    # Hit point
    hit_boxes = {
        "sprite_points": {},
        "compare_points": {}
    }

    # Direction stage

    deltaX = 0
    deltaY = 0

    if axis == "x":
        deltaX = deltaX + change
    elif axis == "y":
        deltaY = deltaY + change

    # Sprite stage
    for i in range(len(sprites_json[sprite]["Graphic"])):
        for j in range(len(sprites_json[sprite]["Graphic"][i])):
            hit_boxes["sprite_points"][f"{i},{j}"] = {}
            hit_boxes["sprite_points"][f"{i},{j}"]["x"] = j + sprites_json[sprite]["x"] + deltaX
            hit_boxes["sprite_points"][f"{i},{j}"]["y"] = i + sprites_json[sprite]["y"] + deltaY

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


def sprite_create(sprites_json: dict, name: str, s_type:str, graphic: list[str], x: int, y: int) -> None:
    """
    Creates a sprite with a given name, type and graphic at given coords
    """
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
