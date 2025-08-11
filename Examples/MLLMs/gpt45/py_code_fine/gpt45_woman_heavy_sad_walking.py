
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters for the figure
fig, ax = plt.subplots()
fig.set_size_inches(5, 7)
ax.set_xlim(-2, 2)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_facecolor('black')

# Initialize the 15 points for a human walker: head, shoulders, arms, hips, knees, feet
points, = ax.plot([], [], 'wo', markersize=8)

# Define positions for each point of the figure in the neutral posture
body_part_positions = {
    'head': np.array([0, 6]),
    'shoulder_right': np.array([0.5, 5.5]),
    'shoulder_left': np.array([-0.5, 5.5]),
    'elbow_right': np.array([1.0, 4.5]),
    'elbow_left': np.array([-1.0, 4.5]),
    'hand_right': np.array([1.0, 3.5]),
    'hand_left': np.array([-1.0, 3.5]),
    'hip_right': np.array([0.3, 4.0]),
    'hip_left': np.array([-0.3, 4.0]),
    'knee_right': np.array([0.4, 2.7]),
    'knee_left': np.array([-0.4, 2.7]),
    'ankle_right': np.array([0.4, 1.4]),
    'ankle_left': np.array([-0.4, 1.4]),
    'foot_right': np.array([0.5, 0.2]),
    'foot_left': np.array([-0.5, 0.2])
}

# Define the animation update function for walking
def update(t):
    dt = 0.05
    walk_cycle_frequency = 2
    amplitude = 0.3

    # Swaying arms
    arm_swing = amplitude * np.sin(2 * np.pi * walk_cycle_frequency * t)
    
    # Legs alternate swinging forward and backward
    leg_swing = amplitude * np.sin(2 * np.pi * walk_cycle_frequency * t)
    
    # Slight body vertical bobbing
    bobbing = 0.1 * np.abs(np.sin(4 * np.pi * walk_cycle_frequency * t))
    
    updated_positions = []
    
    updated_positions.append(body_part_positions['head'] + [0, bobbing])
    updated_positions.append(body_part_positions['shoulder_right'] + [0, bobbing])
    updated_positions.append(body_part_positions['shoulder_left'] + [0, bobbing])
    updated_positions.append(body_part_positions['elbow_right'] + [arm_swing, bobbing])
    updated_positions.append(body_part_positions['elbow_left'] - [arm_swing, -bobbing])
    updated_positions.append(body_part_positions['hand_right'] + [arm_swing, 0])
    updated_positions.append(body_part_positions['hand_left'] - [arm_swing, 0])
    updated_positions.append(body_part_positions['hip_right'] + [0, bobbing])
    updated_positions.append(body_part_positions['hip_left'] + [0, bobbing])
    updated_positions.append(body_part_positions['knee_right'] - [leg_swing, 0])
    updated_positions.append(body_part_positions['knee_left'] + [leg_swing, 0])
    updated_positions.append(body_part_positions['ankle_right'] - [leg_swing, 0])
    updated_positions.append(body_part_positions['ankle_left'] + [leg_swing, 0])
    updated_positions.append(body_part_positions['foot_right'] - [leg_swing, 0])
    updated_positions.append(body_part_positions['foot_left'] + [leg_swing, 0])
    
    # Update the plot data
    updated_positions = np.array(updated_positions)
    points.set_data(updated_positions[:,0], updated_positions[:,1])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True)

# Show animation
plt.show()
