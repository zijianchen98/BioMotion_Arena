
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration for animation
POINT_COLOR = 'white'  # Color of the points
BG_COLOR = 'black'     # Background color
POINT_SIZE = 20        # Size of the points
FPS = 30               # Frames per second
DURATION = 5           # Duration in seconds
NUM_POINTS = 15        # Number of points for the skeleton

# Generate biomechanically plausible motion (running of a sad woman)
def generate_running_motion(num_frames, num_points):
    t = np.linspace(0, 2 * np.pi, num_frames)
    
    # Define motion for each point (x, y) coordinates
    motion_data = np.zeros((num_frames, num_points, 2))
    
    motion_data[:, 0, :] = np.array([0.3 * np.sin(t), 0.5 + 0.05 * np.cos(t)]).T  # Head
    motion_data[:, 1, :] = np.array([0.3 * np.sin(2 * t), 0.4 + 0.05 * np.sin(t)]).T  # Left shoulder
    motion_data[:, 2, :] = np.array([0.3 * np.sin(2 * t) + 0.1, 0.4 - 0.05 * np.sin(t)]).T  # Right shoulder
    motion_data[:, 3, :] = np.array([0.3 * np.sin(t), 0.25 + 0.03 * np.cos(t)]).T  # Torso 1
    motion_data[:, 4, :] = np.array([0.3 * np.sin(t), 0.1 + 0.02 * np.sin(t)]).T  # Torso 2

    # Arms
    motion_data[:, 5, :] = np.array([0.25 * np.sin(2 * t), 0.4 + 0.15 * np.sin(t)]).T  # Left elbow
    motion_data[:, 6, :] = np.array([0.35 * np.sin(2 * t), 0.3 + 0.2 * np.sin(t)]).T  # Left hand
    motion_data[:, 7, :] = np.array([0.25 * np.sin(2 * t) + 0.1, 0.4 + 0.15 * np.sin(t)]).T  # Right elbow
    motion_data[:, 8, :] = np.array([0.35 * np.sin(2 * t) + 0.1, 0.3 + 0.2 * np.sin(t)]).T  # Right hand

    # Legs
    motion_data[:, 9, :] = np.array([0.15 * np.sin(t), -0.05 + 0.1 * np.cos(t)]).T  # Left thigh
    motion_data[:, 10, :] = np.array([0.15 * np.sin(t), -0.2 + 0.15 * np.cos(t)]).T  # Left knee
    motion_data[:, 11, :] = np.array([0.15 * np.sin(t), -0.35 + 0.1 * np.cos(t)]).T  # Left foot

    motion_data[:, 12, :] = np.array([0.15 * np.sin(t) - 0.1, -0.05 + 0.1 * np.cos(t)]).T  # Right thigh
    motion_data[:, 13, :] = np.array([0.15 * np.sin(t) - 0.1, -0.2 - 0.15 * np.cos(t)]).T  # Right knee
    motion_data[:, 14, :] = np.array([0.15 * np.sin(t) - 0.1, -0.35 - 0.1 * np.cos(t)]).T  # Right foot
    
    return motion_data


# Create animation
def create_animation():
    num_frames = FPS * DURATION
    motion_data = generate_running_motion(num_frames, NUM_POINTS)

    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.6)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    scatter = ax.scatter([], [], s=POINT_SIZE, c=POINT_COLOR)

    def update(frame):
        scatter.set_offsets(motion_data[frame])
        return scatter,

    ani = animation.FuncAnimation(
        fig, update, frames=num_frames, interval=1000 // FPS, blit=True
    )

    plt.show()


if __name__ == "__main__":
    create_animation()
