
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Number of points
num_points = 15

# Define initial positions of point-lights representing the body joints
initial_positions = np.array([
    [0, 1],    # Head
    [-0.5, 0.5],   # Left Shoulder
    [0.5, 0.5],    # Right Shoulder
    [-0.5, 0],   # Left Elbow
    [0.5, 0],    # Right Elbow
    [-0.5, -0.5],  # Left Hip
    [0.5, -0.5],   # Right Hip
    [-0.6, -1],  # Left Knee
    [0.6, -1],   # Right Knee
    [-0.4, -1.5],  # Left Ankle
    [0.4, -1.5],  # Right Ankle
    [0, 0.3],   # Spine
    [-0.3, 0],  # Left Hand
    [0.3, 0],   # Right Hand
    [0, -0.7],  # Mobile part
    [0, -0.1]   # Central point for coordination
])

def update(frame):
    plt.clf()  # Clear the current frame
    t = frame / 10.0  # Time factor for smoothness
    # Update positions to simulate running motion
    displacement = np.array([0, 0])
    for i in range(num_points):
        # Simulating some vertical motion and lateral movement
        displacement[0] = np.sin(t + i) * 0.1  # Simulating side-to-side motion
        displacement[1] = (-1 if i % 2 == 0 else 1) * np.abs(np.cos(t + i) * 0.5)  # Vertical oscillation
        plt.scatter(initial_positions[i, 0] + displacement[0], 
                    initial_positions[i, 1] + displacement[1], 
                    color='white', s=100)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axis('off')  # Hides the axes

fig = plt.figure()
plt.style.use('dark_background')
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
