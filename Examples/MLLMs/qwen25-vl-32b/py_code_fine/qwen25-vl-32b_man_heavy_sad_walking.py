
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.25],
    'right_elbow': [1, 0.25],
    'left_hand': [-1.5, -0.25],
    'right_hand': [1.5, -0.25],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_ankle': [-1.5, -1.5],
    'right_ankle': [1.5, -1.5],
    'left_foot': [-1.5, -2],
    'right_foot': [1.5, -2]
}

# Convert the dictionary to a list of positions
initial_positions_list = [
    initial_positions['head'],
    initial_positions['torso'],
    initial_positions['left_shoulder'],
    initial_positions['right_shoulder'],
    initial_positions['left_elbow'],
    initial_positions['right_elbow'],
    initial_positions['left_hand'],
    initial_positions['right_hand'],
    initial_positions['left_hip'],
    initial_positions['right_hip'],
    initial_positions['left_knee'],
    initial_positions['right_knee'],
    initial_positions['left_ankle'],
    initial_positions['right_ankle'],
    initial_positions['left_foot'],
    initial_positions['right_foot']
]

# Function to update the positions for each frame
def update_positions(frame):
    # Define the walking cycle parameters
    amplitude = 0.5  # Amplitude of the walking motion
    frequency = 0.1  # Frequency of the walking cycle
    
    # Calculate the phase for the current frame
    phase = frame / num_frames * 2 * np.pi
    
    # Update the positions of the legs (simulating walking)
    left_leg_phase = phase
    right_leg_phase = phase + np.pi  # Opposite phase for the other leg
    
    # Update the left leg
    initial_positions['left_hip'][1] = -0.5 + amplitude * np.sin(left_leg_phase)
    initial_positions['left_knee'][1] = -1 + amplitude * np.sin(left_leg_phase + np.pi / 2)
    initial_positions['left_ankle'][1] = -1.5 + amplitude * np.sin(left_leg_phase + np.pi)
    initial_positions['left_foot'][1] = -2 + amplitude * np.sin(left_leg_phase + 3 * np.pi / 2)
    
    # Update the right leg
    initial_positions['right_hip'][1] = -0.5 + amplitude * np.sin(right_leg_phase)
    initial_positions['right_knee'][1] = -1 + amplitude * np.sin(right_leg_phase + np.pi / 2)
    initial_positions['right_ankle'][1] = -1.5 + amplitude * np.sin(right_leg_phase + np.pi)
    initial_positions['right_foot'][1] = -2 + amplitude * np.sin(right_leg_phase + 3 * np.pi / 2)
    
    # Update the torso (slight sway)
    initial_positions['torso'][0] = 0.1 * np.sin(phase)
    
    # Convert the updated dictionary to a list
    updated_positions_list = [
        initial_positions['head'],
        initial_positions['torso'],
        initial_positions['left_shoulder'],
        initial_positions['right_shoulder'],
        initial_positions['left_elbow'],
        initial_positions['right_elbow'],
        initial_positions['left_hand'],
        initial_positions['right_hand'],
        initial_positions['left_hip'],
        initial_positions['right_hip'],
        initial_positions['left_knee'],
        initial_positions['right_knee'],
        initial_positions['left_ankle'],
        initial_positions['right_ankle'],
        initial_positions['left_foot'],
        initial_positions['right_foot']
    ]
    
    return updated_positions_list

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Hide the axes
ax.set_facecolor('black')  # Set background to black

# Initialize the scatter plot
scatter = ax.scatter([], [], color='white', s=20)

# Animation function
def animate(frame):
    updated_positions = update_positions(frame)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=num_frames,
    interval=50,  # 50 ms per frame (20 FPS)
    blit=True
)

# Display the animation
plt.show()
