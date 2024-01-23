from cage import main as cage
import keyboard

# Game setup
res_x = 30

res_y = 9

background = cage.screen_memory(res_x, res_y)

sprites = {}

# Level Sprites

# Rock

cage.sprite_create(sprites,  # sprites json
                   "Rock_1",  # name
                   "Level",  # Layer/Type
                   [["+", "-", "+"],
                    ["|", "1", "|"],
                    ["+", "-", "+"]],
                   6,  # x pos
                   0  # y pos
                   )

cage.sprite_create(sprites,  # sprites json
                   "Rock_2",  # name
                   "Level",  # Layer/Type
                   [["+", "-", "+"],
                    ["|", "2", "|"],
                    ["+", "-", "+"]],
                   6,  # x pos
                   6  # y pos
                   )

cage.sprite_create(sprites,  # sprites json
                   "Rock_3",  # name
                   "Level",  # Layer/Type
                   [["+", "-", "+"],
                    ["|", "3", "|"],
                    ["+", "-", "+"]],
                   12,  # x pos
                   3  # y pos
                   )
# UI

cage.sprite_create(sprites,  # sprites json
                   "Coin_UI",  # name
                   "UI",  # Layer/Type
                   [["Coins:", "1"]],  # graphic
                   28,  # x pos
                   0  # y pos
                   )

# Coins

cage.sprite_create(sprites,  # sprites json
                   "Coin_1",  # name
                   "Coin_1",  # Layer/Type
                   [["C"]],  # graphic
                   20,  # x pos
                   5  # y pos
                   )

# Player Sprites

# Debug

cage.sprite_create(sprites,  # sprites json
                   "Debug",  # name
                   "Player",  # Layer/Type
                   [["X", "Y"],  # graphic
                    ["3", "4"]],
                   0,  # x pos
                   0  # y pos
                   )
# Game variables

coins = 0

# Main loop

while True:
    # Sprite Graphic

    sprites["Debug"]["Graphic"][1] = [str(sprites["Debug"]["x"]), str(sprites["Debug"]["y"])]

    sprites["Coin_UI"]["Graphic"][0][1] = coins

    # User input
    if keyboard.is_pressed('d'):
        cage.transform("Debug", "x", 1, ["Level"], sprites, res_x, res_y)
        # Sprite, Axis, Amount, Sprite types collide with (null) for no sprites, Sprites json, display resolution
    if keyboard.is_pressed('a'):
        cage.transform("Debug", "x", -1, ["Level"], sprites, res_x, res_y)
    if keyboard.is_pressed('s'):
        cage.transform("Debug", "y", 1, ["Level"], sprites, res_x, res_y)
    if keyboard.is_pressed('w'):
        cage.transform("Debug", "y", -1, ["Level"], sprites, res_x, res_y)

    # Sprite logic

    if cage.collision("Debug", ["Coin_1"], sprites):
        coins += 1
        sprites["Coin_1"]["Type"] = "DEAD"



    # Draw

    cage.ter_draw(background, 0.06, sprites)
    # BackGround Is a 2d array # Draw delay #Json which sprites are stored under
