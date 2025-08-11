
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100
fps = 30
dt = 1/fps

# Define joint angles (simplified for walking motion)
def get_joint_angles(time):
    angle = 10 * np.sin(time)
    return angle

# Define leg motion
def get_leg_positions(angle, length=1.0):
    hip_x = 0
    hip_y = 0
    knee_x = length * np.cos(angle)
    knee_y = length * np.sin(angle)
    ankle_x = knee_x
    ankle_y = knee_y - 0.2*length
    return hip_x, hip_y, knee_x, knee_y, ankle_x, ankle_y

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the lights
lights = []
for _ in range(num_lights):
    light = ax.scatter([], [], s=50, c='white')
    lights.append(light)

# Animation function
def animate(frame):
    for i in range(num_lights):
        # Generate random angles
        angle = np.random.uniform(-np.pi/2, np.pi/2) 

        # Get leg positions
        hip_x, hip_y, knee_x, knee_y, ankle_x, ankle_y = get_leg_positions(angle)
        
        # Update light positions
        lights[i].set_offsets([ankle_x, ankle_y])

    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration*fps, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("sadman_walking.gif", writer='pillow', fps=fps)

plt.show()
