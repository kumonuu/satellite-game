import pgzrun
import random
import time

TITLE = "satellite game"
WIDTH = 600
HEIGHT = 500

satellites = []
line_coordinates = []
satellite_number = 1
satellite_index = 0
start_time = time.time()
time_taken = 0

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
    global time_taken
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
        for coordinate in line_coordinates:
            screen.draw.line(
                coordinate[0],
                coordinate[1],
                "white"
            )

    if len(line_coordinates) < 7:
        time_taken = time.time() - start_time
        time_taken = round(time_taken, 1)
        screen.draw.text(str(time_taken), center=(20,20), fontsize=20)
    else:
        screen.draw.text(str(time_taken), center=(20,20), fontsize=20)


def update():
    pass

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
        print(len(line_coordinates))
        satellite_index += 1
    else:
        line_coordinates = []
        satellite_index = 0

spawn_satellites()

pgzrun.go()