
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOWING_SPEED = 0.01

# Define the subject and action
SUBJECT_X, SUBJECT_Y = WIDTH // 2, HEIGHT // 2
ACTION_X, ACTION_Y = 200, 200

# Define the point light source
POINT_LIGHT_X, POINT_LIGHT_Y = 0, 0
POINT_LIGHT_Z = 100

# Define the motion parameters
N_POINTS = 1000
T steps = 100
T_STEP = 0.01
X_SPEED = 0
Y_SPEED = 0

# Initialize the figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Initialize the point light source
def point_light(x, y, z):
    ax.scatter(x, y, z, color=WHITE, s=10, alpha=0.5)

# Update the point light source position
def update_light():
    global X_SPEED, Y_SPEED
    X_SPEED = np.random.uniform(-BOWING_SPEED, BOWING_SPEED)
    Y_SPEED = np.random.uniform(-BOWING_SPEED, BOWING_SPEED)
    point_light(SUBJECT_X + X_SPEED, SUBJECT_Y + Y_SPEED, POINT_LIGHT_Z)

# Animate the point light source
for i in range(N_POINTS):
    ax.clear()
    ax.set_xlim(-WIDTH, WIDTH)
    ax.set_ylim(-HEIGHT, HEIGHT)
    ax.set_zlim(-HEIGHT, HEIGHT)
    point_light(ACTION_X + X_SPEED, ACTION_Y + Y_SPEED, POINT_LIGHT_Z)
    update_light()
    plt.draw()
    plt.pause(T_STEP)
    T_STEP += T_STEP
