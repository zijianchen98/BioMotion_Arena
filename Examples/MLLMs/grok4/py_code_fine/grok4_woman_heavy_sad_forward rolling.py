
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate point-light positions
def generate_point_lights(frame):
    # Defines the position of point lights for a sad woman rolling forward.
    # Positions are just illustrative; they must be updated for realism.
    if frame < 30:
        # Start rolling
        y_pos = np.sin(np.linspace(0, np.pi, 15)) * (frame / 30)
    else:
        # Continue and finish rolling
        y_pos = np.sin(np.linspace(0, np.pi, 15))

    # Fixed x positions for the points
    x_pos = np.linspace(-1, 1, 15)

    # Collating points
    return x_pos, y_pos

# Function to update the animation
def update(frame):
    # Clear previous points
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-1.5, 1.5)
    plt.axis('off')  # Hide axes

    # Generate point lights
    x_pos, y_pos = generate_point_lights(frame)
    
    # Draw point lights
    plt.scatter(x_pos, y_pos, color='white', s=100)

# Set up the figure and the axis
fig = plt.figure(figsize=(5, 8), facecolor='black')
plt.title('Point-Light Animation: Sad Woman Forward Rolling', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=100)

# Show the animation
plt.show()
