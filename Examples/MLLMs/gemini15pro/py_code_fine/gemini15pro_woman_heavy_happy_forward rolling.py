
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a list of its x and y coordinates over time
num_frames = 60
points = []

# Example point - head (adjust values for realistic rolling motion)
head_x = np.linspace(100, 300, num_frames) + 20 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
head_y = np.linspace(400, 400, num_frames) + 50 * np.cos(np.linspace(0, np.pi, num_frames)) * np.cos(np.linspace(0, np.pi, num_frames))
points.append([head_x, head_y])

# Example point (add more points for the rest of the body)
shoulder_x = head_x + 20 * np.cos(np.linspace(0, 2 * np.pi, num_frames))
shoulder_y = head_y + 30 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
points.append([shoulder_x, shoulder_y])

# Simulate rolling by changing y coordinates relative to a rolling center
center_x = head_x
center_y = head_y - 50

def create_rolling_point(offset_x, offset_y):
    angle = np.linspace(0, 2 * np.pi, num_frames)
    x = center_x + offset_x * np.cos(angle) - offset_y * np.sin(angle)
    y = center_y + offset_x * np.sin(angle) + offset_y * np.cos(angle)
    return x,y


for i in range(13):
    offset_x = (i % 7) * 20 - 50
    offset_y = (i // 7) * 40 - 40
    x, y = create_rolling_point(offset_x, offset_y)
    points.append([x, y])




# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light scatter plot
scat = ax.scatter([], [], s=50, c='white')


# Update function for the animation
def update(frame):
    x_coords = [point[0][frame] for point in points]
    y_coords = [point[1][frame] for point in points]

    scat.set_offsets(np.c_[x_coords, y_coords])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)


# Save the animation (optional)
# ani.save('rolling_animation.gif', writer='pillow')

# Show the animation
plt.show()



