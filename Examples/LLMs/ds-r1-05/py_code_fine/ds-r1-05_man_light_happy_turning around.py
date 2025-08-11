
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi, sin, cos, exp

# Initialize plot with dark background
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Biomechanical model parameters
num_points = 15
shoulder_width = 0.8
hip_width = 0.6
height = 1.6
arm_swing = 0.5
foot_lift = 0.3
turning_speed = pi / 60  # Angular velocity (radians per frame)

# Initialize scatter plot for points
scatter = ax.scatter([], [], s=50, c='white', edgecolors='white')

# Function to calculate positions based on biomechanical model
def update_positions(t):
    positions = np.zeros((num_points, 2))
    
    # Core body rotation (smooth sinusoidal)
    body_angle = t * turning_speed
    sin_body = sin(body_angle)
    cos_body = cos(body_angle)
    
    # Head (subtle up-down movement)
    positions[0] = (0, height + 0.05 * sin(2 * body_angle))
    
    # Shoulders and neck (natural rotation kinematics)
    positions[1] = (-shoulder_width * 0.5, height * 0.8)
    positions[2] = (shoulder_width * 0.5, height * 0.8)
    positions[3] = (0, height * 0.9)  # Neck
    
    # Arms (realistic pendulum motion)
    arm_phase = pi + pi * sin(2 * t * turning_speed)
    positions[4] = (positions[1][0] - 0.2 * sin(arm_phase), 
                    positions[1][1] - 0.2 * abs(sin(arm_phase)))
    positions[5] = (positions[2][0] + 0.2 * sin(arm_phase), 
                    positions[2][1] - 0.2 * abs(sin(arm_phase)))
    positions[6] = (positions[4][0] - 0.25 * sin(arm_phase), 
                    positions[4][1] - 0.25 * abs(sin(arm_phase)))
    positions[7] = (positions[5][0] + 0.25 * sin(arm_phase), 
                    positions[5][1] - 0.25 * abs(sin(arm_phase)))
    
    # Hips and spine (body tilt synchronized with turn)
    positions[8] = (0, height * 0.3)
    positions[9] = (-hip_width * 0.5, height * 0.3)
    positions[10] = (hip_width * 0.5, height * 0.3)
    
    # Legs and feet (gait dynamics with foot liftoff)
    leg_phase = 0.5 * arm_phase
    foot_phase = exp(-2 * sin(t * turning_speed)**2)
    
    positions[11] = (positions[9][0], height * 0.15 - 0.15 * sin(leg_phase))
    positions[12] = (positions[10][0], height * 0.15 + 0.15 * sin(leg_phase))
    positions[13] = (positions[11][0], positions[11][1] - foot_lift * foot_phase)
    positions[14] = (positions[12][0], positions[12][1] - foot_lift)
    
    # Apply rotational transformation
    for i in range(num_points):
        x, y = positions[i]
        positions[i] = (x * cos_body - y * sin_body, 
                        x * sin_body + y * cos_body)
    
    return positions

# Animation update function
def update(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=120,  # About 4 seconds at 30 FPS
    interval=33,  # ~30 frames per second
    blit=True
)

plt.tight_layout()
plt.show()
