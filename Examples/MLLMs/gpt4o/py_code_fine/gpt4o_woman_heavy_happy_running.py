
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define the biomechanical motion of point-lights for a "running sadman"
def generate_running_sadman_frame(frame, num_points=15):
    # Parameters for motion
    amplitude = 0.5     # Vertical movement amplitude
    frequency = 0.03    # Horizontal movement speed

    # Base positions of the points (centered around origin `(0, 0)`)
    base_coordinates = np.array([
        [0, 3],    # Top head
        [-0.5, 2], [0.5, 2],  # Shoulders
        [-1, 1], [0, 1], [1, 1],  # Chest and arms
        [-1.5, 0], [-0.5, 0], [0.5, 0], [1.5, 0],  # Hip & pelvis
        [-1, -1], [1, -1],  # Thighs
        [-1, -2], [1, -2],  # Knees
        [-1, -3], [1, -3]   # Feet
    ])

    # Simulate realistic running motion
    displacements = np.zeros_like(base_coordinates)
    time = frame * frequency

    # Head bobbing movement
    displacements[0, 1] += amplitude * np.sin(2 * np.pi * time / 1.5)  

    # Shoulder and arm swing
    displacements[1, 1] += amplitude * np.sin(2 * np.pi * time / 1.2)
    displacements[2, 1] -= amplitude * np.sin(2 * np.pi * time / 1.2)
    displacements[3, 0] += amplitude * np.sin(2 * np.pi * time / 1.2)
#
