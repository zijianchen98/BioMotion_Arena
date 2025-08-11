
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points (approximate human figure)
initial_positions = np.array([
    [0, 4],      # Head
    [-1, 3],     # Left Shoulder
    [1, 3],      # Right Shoulder
    [-2, 2],     # Left Elbow
    [2, 2],      # Right Elbow
    [-2.5, 1],   # Left Wrist
    [2.5, 1],    # Right Wrist
    [0, 2],      # Torso center
    [-1, 0],     # Left Hip
    [1, 0],      # Right Hip
    [-1.5, -2],   # Left Knee
    [1.5, -2],   # Right Knee
    [-1.5, -4],   # Left Ankle
    [1.5, -4],   # Right Ankle
    [0, -1]     # waist
])

# Define the animation function
def animate(i):
    # Define the jumping motion
    jump_height = 1.0
    jump_frequency = 0.1
    vertical_displacement = jump_height * np.sin(2 * np.pi * jump_frequency * i)

    # Define arm swinging motion
    arm_swing = 0.5
    arm_frequency = 0.2
    left_arm_x_displacement = arm_swing * np.sin(2 * np.pi * arm_frequency * i)
    right_arm_x_displacement = -arm_swing * np.sin(2 * np.pi * arm_frequency * i)
    left_arm_y_displacement = arm_swing * np.cos(2 * np.pi * arm_frequency * i)
    right_arm_y_displacement = arm_swing * np.cos(2 * np.pi * arm_frequency * i)

    # Update the positions of the points based on the jumping and arm swinging motions
    x_data = initial_positions[:, 0].copy()
    y_data = initial_positions[:, 1].copy()

    y_data += vertical_displacement
    
    # Simulate a slight wobble effect
    wobble_amplitude = 0.1  # Adjust for less or more wobble
    x_wobble = np.sin(i * 0.5) * wobble_amplitude

    # Modify arm points to create swinging movement
    x_data[3] += left_arm_x_displacement
    x_data[5] += left_arm_x_displacement * 1.5  # Greater wrist movement
    y_data[3] += left_arm_y_displacement
    y_data[5] += left_arm_y_displacement * 1.5

    x_data[4] += right_arm_x_displacement
    x_data[6] += right_arm_x_displacement * 1.5  # Greater wrist movement
    y_data[4] += right_arm_y_displacement
    y_data[6] += right_arm_y_displacement * 1.5
    
    x_data[8] += x_wobble # hips
    x_data[9] += -x_wobble # hips
    
    x_data[10] += x_wobble # knees
    x_data[11] += -x_wobble # knees

    x_data[12] += x_wobble # ankles
    x_data[13] += -x_wobble # ankles
    
    x_data[7] += x_wobble # torso
    
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Show the animation
plt.show()
