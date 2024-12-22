import pgzrun
import random

TITLE = "satellite game"
WIDTH = 600
HEIGHT = 500

satellites = []
line_coordinates = []
satellite_number = 1
satellite_index = 0

def spawn_satellites():
    global satellites
    for i in range(8):
        satellite = Actor("satellite")
        satellite.pos = (
            random.randint(50,WIDTH-50),
            random.randint(50,HEIGHT-50)
        )
        satellites.append(satellite)

def draw():
    satellite_number = 1

    screen.blit("space", (0,0))
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(
            str(satellite_number),
            center=(satellite.x, satellite.y+20),
            fontsize=20
        )
        satellite_number += 1
    if len(line_coordinates) > 0:
        screen.draw.line(
            line_coordinates[0][0],
            line_coordinates[0][1],
            "white"
        )

def on_mouse_down(pos):
    global line_coordinates
    global satellite_index
    if satellites[satellite_index].collidepoint(pos):
        if satellite_index > 0:
            line_coordinates.append(
                (
                satellites[satellite_index-1].pos,
                satellites[satellite_index].pos
                )
            )
        print(line_coordinates)
        satellite_index += 1

spawn_satellites()

pgzrun.go()