
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Points representing the body parts
points = [2, 4, 6, 8]

# Function to update the frame of the animation
def update(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    # Move the points up and down to simulate jumping
    y_positions = [frame % 10, (frame+2) % 10, (frame+4) % 10, (frame+6) % 10]
    
    # Draw the stick figure
    ax.plot([1, 1], [y_positions[0], y_positions[1]], color='white', linewidth=3)  # Body
    ax.plot([1, 2], [y_positions[1], y_positions[2]], color='white', linewidth=3)  # Right arm
    ax.plot([1, 0], [y_positions[1], y_positions[3]], color='white', linewidth=3)  # Left arm
    
    # Draw points
    for i in range(4):
        ax.scatter(1, y_positions[i], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), interval=50)

plt.show()
