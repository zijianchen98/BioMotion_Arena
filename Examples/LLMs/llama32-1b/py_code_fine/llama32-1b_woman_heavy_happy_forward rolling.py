
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HUMAN_SIZE = 100

# Define parameters
FRONT_PITCH = 50
FRONT_SPEED = 2
REAR_PITCH = 30
REAR_SPEED = 1.5
FORWARD_SPEED = 1
FORWARD_SPEED_RAMP = 0.8

# Define the human body as a collection of points
class HumanBody:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pitch = 0
        self.rear_pitch = 0

    def move(self, front_speed, rear_speed):
        self.x += front_speed
        self.y += rear_speed

        # Keep the human body within the boundaries
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT

        # Apply the front and rear pitches
        self.pitch += front_speed / 10
        self.rear_pitch += rear_speed / 10

        # Ensure the pitches stay within the bounds of the human body
        self.pitch = max(-HUMAN_SIZE / 2, min(HUMAN_SIZE / 2, self.pitch))
        self.rear_pitch = max(-HUMAN_SIZE / 2, min(HUMAN_SIZE / 2, self.rear_pitch))

# Create a figure and axis
fig, ax = plt.subplots()

# Create the human body
human_body = HumanBody(WIDTH / 2, HEIGHT / 2)

# Create the point lights
light1 = patches.Patch(color=WHITE, alpha=0.5)
light2 = patches.Patch(color=WHITE, alpha=0.5)
light3 = patches.Patch(color=WHITE, alpha=0.5)
light4 = patches.Patch(color=WHITE, alpha=0.5)
light5 = patches.Patch(color=WHITE, alpha=0.5)
light6 = patches.Patch(color=WHITE, alpha=0.5)
light7 = patches.Patch(color=WHITE, alpha=0.5)
light8 = patches.Patch(color=WHITE, alpha=0.5)
light9 = patches.Patch(color=WHITE, alpha=0.5)
light10 = patches.Patch(color=WHITE, alpha=0.5)
light11 = patches.Patch(color=WHITE, alpha=0.5)
light12 = patches.Patch(color=WHITE, alpha=0.5)
light13 = patches.Patch(color=WHITE, alpha=0.5)
light14 = patches.Patch(color=WHITE, alpha=0.5)
light15 = patches.Patch(color=WHITE, alpha=0.5)

# Set the axis limits
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)

# Function to update the plot
def update(frame):
    global human_body, light1, light2, light3, light4, light5, light6, light7, light8, light9, light10, light11, light12, light13, light14, light15

    # Move the human body
    human_body.move(FORWARD_SPEED, FORWARD_SPEED_RAMP)

    # Update the point lights
    light1.set_xy((human_body.x + FRONT_PITCH, human_body.y))
    light2.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH))
    light3.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + FRONT_PITCH))
    light4.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 2 * FRONT_PITCH))
    light5.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 3 * FRONT_PITCH))
    light6.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 4 * FRONT_PITCH))
    light7.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 5 * FRONT_PITCH))
    light8.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 6 * FRONT_PITCH))
    light9.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 7 * FRONT_PITCH))
    light10.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 8 * FRONT_PITCH))
    light11.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 9 * FRONT_PITCH))
    light12.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 10 * FRONT_PITCH))
    light13.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 11 * FRONT_PITCH))
    light14.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 12 * FRONT_PITCH))
    light15.set_xy((human_body.x + FRONT_PITCH, human_body.y + FRONT_PITCH + 13 * FRONT_PITCH))

    # Set the axis limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    return light1, light2, light3, light4, light5, light6, light7, light8, light9, light10, light11, light12, light13, light14, light15

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=15, interval=20)

# Show the animation
plt.show()
