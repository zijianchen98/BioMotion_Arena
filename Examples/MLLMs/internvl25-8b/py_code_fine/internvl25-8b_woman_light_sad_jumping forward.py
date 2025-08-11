
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation  # Library for animating plots

# Define the number of frames
num_frames = 30

# Define the number of point lights per body part
num_lights_per_body_part = 5

# Ensure total number of point lights needed
total_lights = num_frames * 4 * num_lights_per_body_part

# Define the initial positions of the lights
initial_positions = {
    "head": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "upper_arm": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "lower_arm": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "hand": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "hip": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "upper_leg": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "lower_leg": np.zeros((num_frames, num_lights_per_body_part, 2)),
    "foot": np.zeros((num_frames, num_lights_per_body_part, 2)),
}

# Set the seed for the random number generator
np.random.seed(0)

# Calculate the initial random positions for the lights
for body_part, positions in initial_positions.items():
    positions[:, :, 0] = np.random.uniform(-1.5, 1.5, (num_frames, num_lights_per_body_part))
    positions[:, :, 1] = np.random.uniform(-1.5, 1.5, (num_frames, num_lights_per_body_part))

# Define the animation update function
def update(frame):
    # Update the positions of the lights based on the motion of the body parts
    for body_part, positions in initial_positions.items():
        # Calculate intermediate positions
        intermediate_positions = np.zeros((num_frames, num_lights_per_body_part, 2))
        if body_part == "head":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
        elif body_part == "upper_arm":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
        elif body_part == "lower_arm":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
        elif body_part == "hand":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
        elif body_part == "hip":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
        elif body_part == "upper_leg":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
        elif body_part == "lower_leg":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))
        elif body_part == "foot":
            intermediate_positions[:, :, 0] = np.linspace(0, 1, num_frames) * positions[:, :, 0] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.ones((num_frames, num_lights_per_body_part))
            intermediate_positions[:, :, 1] = np.linspace(0, 1, num_frames) * positions[:, :, 1] + (
                1 - np.linspace(0, 1, num_frames)
            ) * np.zeros((num_frames, num_lights_per_body_part))

        # Update the positions of the lights for the current frame
        positions[:, :, 0] = intermediate_positions[:, :, 0]
        positions[:, :, 1] = intermediate_positions[:, :, 1]

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_axis_off()

scat = ax.scatter([], [], c='white')

# Set up the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=True, interval=50, repeat=False
)

plt.show()
