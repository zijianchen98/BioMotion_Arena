
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point lights
lights = [
    {"x": 100, "y": 100, "z": 100, "radius": 5},
    {"x": 200, "y": 200, "z": 200, "radius": 5},
    {"x": 300, "y": 300, "z": 300, "radius": 5},
    {"x": 400, "y": 400, "z": 400, "radius": 5},
    {"x": 500, "y": 500, "z": 500, "radius": 5},
    {"x": 600, "y": 600, "z": 600, "radius": 5},
    {"x": 700, "y": 700, "z": 700, "radius": 5},
    {"x": 800, "y": 800, "z": 800, "radius": 5},
    {"x": 900, "y": 900, "z": 900, "radius": 5},
    {"x": 1000, "y": 1000, "z": 1000, "radius": 5},
    {"x": 1100, "y": 1100, "z": 1100, "radius": 5},
    {"x": 1200, "y": 1200, "z": 1200, "radius": 5},
    {"x": 1300, "y": 1300, "z": 1300, "radius": 5},
    {"x": 1400, "y": 1400, "z": 1400, "radius": 5}
]

# Define the action
def walk(action):
    if action == 0:
        # Start walking
        lights[0]["x"] = 100
        lights[0]["y"] = 100
        lights[0]["z"] = 100
        lights[1]["x"] = 200
        lights[1]["y"] = 200
        lights[1]["z"] = 200
        lights[2]["x"] = 300
        lights[2]["y"] = 300
        lights[2]["z"] = 300
        lights[3]["x"] = 400
        lights[3]["y"] = 400
        lights[3]["z"] = 400
        lights[4]["x"] = 500
        lights[4]["y"] = 500
        lights[4]["z"] = 500
        lights[5]["x"] = 600
        lights[5]["y"] = 600
        lights[5]["z"] = 600
        lights[6]["x"] = 700
        lights[6]["y"] = 700
        lights[6]["z"] = 700
        lights[7]["x"] = 800
        lights[7]["y"] = 800
        lights[7]["z"] = 800
        lights[8]["x"] = 900
        lights[8]["y"] = 900
        lights[8]["z"] = 900
        lights[9]["x"] = 1000
        lights[9]["y"] = 1000
        lights[9]["z"] = 1000
        lights[10]["x"] = 1100
        lights[10]["y"] = 1100
        lights[10]["z"] = 1100
        lights[11]["x"] = 1200
        lights[11]["y"] = 1200
        lights[11]["z"] = 1200
        lights[12]["x"] = 1300
        lights[12]["y"] = 1300
        lights[12]["z"] = 1300
        lights[13]["x"] = 1400
        lights[13]["y"] = 1400
        lights[13]["z"] = 1400
        lights[14]["x"] = 1500
        lights[14]["y"] = 1500
        lights[14]["z"] = 1500
    elif action == 1:
        # Stop walking
        lights[0]["x"] = 100
        lights[0]["y"] = 100
        lights[0]["z"] = 100
        lights[1]["x"] = 200
        lights[1]["y"] = 200
        lights[1]["z"] = 200
        lights[2]["x"] = 300
        lights[2]["y"] = 300
        lights[2]["z"] = 300
        lights[3]["x"] = 400
        lights[3]["y"] = 400
        lights[3]["z"] = 400
        lights[4]["x"] = 500
        lights[4]["y"] = 500
        lights[4]["z"] = 500
        lights[5]["x"] = 600
        lights[5]["y"] = 600
        lights[5]["z"] = 600
        lights[6]["x"] = 700
        lights[6]["y"] = 700
        lights[6]["z"] = 700
        lights[7]["x"] = 800
        lights[7]["y"] = 800
        lights[7]["z"] = 800
        lights[8]["x"] = 900
        lights[8]["y"] = 900
        lights[8]["z"] = 900
        lights[9]["x"] = 1000
        lights[9]["y"] = 1000
        lights[9]["z"] = 1000
        lights[10]["x"] = 1100
        lights[10]["y"] = 1100
        lights[10]["z"] = 1100
        lights[11]["x"] = 1200
        lights[11]["y"] = 1200
        lights[11]["z"] = 1200
        lights[12]["x"] = 1300
        lights[12]["y"] = 1300
        lights[12]["z"] = 1300
        lights[13]["x"] = 1400
        lights[13]["y"] = 1400
        lights[13]["z"] = 1400
        lights[14]["x"] = 1500
        lights[14]["y"] = 1500
        lights[14]["z"] = 1500

# Create the animation
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1600)
    ax.set_ylim(0, 1600)
    ax.set_zlim(0, 1600)
    ax.set_aspect('equal')
    walk(i % 2)

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
