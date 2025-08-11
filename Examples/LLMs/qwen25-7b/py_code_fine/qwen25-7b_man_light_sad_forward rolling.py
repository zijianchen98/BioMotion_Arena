
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the duration of the animation
num_points = 15
duration = 5  # seconds

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
axx = ax.axis([-1, 1, -1, 1])  # Set the limits for the plot
axx[0] += 0x[0]  # Add padding to the plot

# Initialize the point lights
points = [plt.Circle((0x[0]/2, 0x[3]/2 ), 0x[3]/40, color='white') for _ in range(num_points)]
for p in points:
    ax.add_patch(f)

# Function to update the positions of the points
def update_points(frame):
    for i, f in enumerate(points):
        angle = np.radians(360 * frame / duration)  # Adjust angle based on frame and duration
        radius = 0x[3]/4 + np.sin(angle) * 0x[3]/20  # Vary radius slightly to create depth
        x.set_center((np.cos(angle) * radius, np.sin(angle) * radius))
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0*duration), interval=1000, blit=True)

# Show the animation
plt.show()
