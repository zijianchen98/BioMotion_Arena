
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human skeleton:
# Head, Torso, Hips, Shoulders, Elbows, Wrists, Knees, Ankles
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0],   # Torso
    [0, -1],  # Hips
    [-0.5, 0.5],  # Left Shoulder
    [0.5, 0.5],   # Right Shoulder
    [-0.7, -0.5], # Left Elbow
    [0.7, -0.5],  # Right Elbow
    [-0.8, -1.5], # Left Wrist
    [0.8, -1.5],  # Right Wrist
    [-0.5, -2],   # Left Knee
    [0.5, -2],    # Right Knee
    [-0.5, -3],   # Left Ankle
    [0.5, -3],    # Right Ankle
])

# Define the amplitude and phase for each joint's oscillation
amplitudes = np.array([0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.3, 0.3, 0.4, 0.4])
phases = np.linspace(0, np.pi, 13)

# Define the walking cycle period (in seconds)
period = 1.0  # Walking cycle duration

# Function to update the positions of the points over time
def update_points(t):
    # Apply sinusoidal motion to simulate walking
    x = initial_positions[:, 0].copy()
    y = initial_positions[:, 1].copy()
    
    # Add vertical oscillations for a walking gait
    for i in range(len(x)):
        y[i] += amplitudes[i] * np.sin(2 * np.pi * t / period + phases[i])
    
    # Adjust for a "sad" posture: slumped shoulders and slower pace
    y[3:9] -= 0.1  # Lower the upper body (shoulders, elbows, wrists)
    y[9:] -= 0.2   # Lower the legs slightly
    
    return x, y

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Animation function
def animate(frame):
    t = frame / 30.0  # Convert frame number to time (assuming 30 fps)
    x, y = update_points(t)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=33, blit=True)

# Display the animation
plt.show()
