
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAMES = 200
FPS = 30
FIGSIZE = (8, 8)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
lights = [plt.Circle((0, 0), 0.01, color='white') for _ in range(NUM_LIGHTS)]
for light in lights:
    ax.add_patch(light)

# Animation function
def animate(frame):
    t = frame / FPS
    
    # Sine wave for smooth motion
    def sine_wave(x, freq, amp, phase):
        return amp * np.sin(freq * x + phase)
    
    # Head position
    head_x = sine_wave(t, 4, 0.1, np.pi/2)
    head_y = sine_wave(t, 4, 0.1, np.pi)
    
    # Torso position
    torso_x = sine_wave(t, 3, 0.2, 0)
    torso_y = sine_wave(t, 3, 0.2, np.pi/2)
    
    # Arm positions
    arm_length = 0.2
    left_arm_angle = sine_wave(t, 6, np.pi/4, np.pi/2)
    right_arm_angle = sine_wave(t, 6, np.pi/4, 0)
    
    left_arm_x = torso_x + arm_length * np.cos(left_arm_angle)
    left_arm_y = torso_y + arm_length * np.sin(left_arm_angle)
    
    right_arm_x = torso_x + arm_length * np.cos(right_arm_angle)
    right_arm_y = torso_y + arm_length * np.sin(right_arm_angle)
    
    # Leg positions
    leg_length = 0.3
    left_leg_angle = sine_wave(t, 6, -np.pi/4, np.pi/2)
    right_leg_angle = sine_wave(t, 6, -np.pi/4, 0)
    
    left_leg_x = torso_x + leg_length * np.cos(left_leg_angle)
    left_leg_y = torso_y + leg_length * np.sin(left_leg_angle)
    
    right_leg_x = torso_x + leg_length * np.cos(right_leg_angle)
    right_leg_y = torso_y + leg_length * np.sin(right_leg_angle)
    
    # Assign positions to lights
    positions = [
        (head_x, head_y),
        (torso_x, torso_y),
        (left_arm_x, left_arm_y),
        (right_arm_x, right_arm_y),
        (left_leg_x, left_leg_y),
        (right_leg_x, right_leg_y),
        # Add more points for a total of 15
        (torso_x + 0.1, torso_y + 0.1),
        (torso_x - 0.1, torso_y + 0.1),
        (torso_x + 0.1, torso_y - 0.1),
        (torso_x - 0.1, torso_y - 0.1),
        (left_arm_x + 0.05, left_arm_y),
        (right_arm_x + 0.05, right_arm_y),
        (left_leg_x + 0.05, left_leg_y),
        (right_leg_x + 0.05, right_leg_y),
        (torso_x, torso_y + 0.15)
    ]
    
    for i, (x, y) in enumerate(positions):
        lights[i].center = (x, y)
    
    return lights

# Create animation
ani = FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
