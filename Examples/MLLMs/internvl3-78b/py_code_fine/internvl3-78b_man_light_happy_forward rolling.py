
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a new figure with a black background
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)

# Function to update the animation frame
def update(frame):
    ax.clear()
  
    # Define the positions of the 15 point-lights
    x = [
        0.2 + (frame / 1000) % 1,
        0.4 + (frame / 1000) % 1,
        0.6 + (frame / 1000) % 1,
        0.8 + (frame / 1000) % 1,
        1.0 + (frame / 1000) % 1,
        1.2 + (frame / 1000) % 1,
        1.4 + (frame / 1000) % 1,
        1.6 + (frame / 1000) % 1,
        1.8 + (frame / 1000) % 1,
        2.0 + (frame / 1000) % 1,
        2.2 + (frame / 1000) % 1,
        2.4 + (frame / 1000) % 1,
        2.6 + (frame / 1000) % 1,
        2.8 + (frame / 1000) % 1,
        3.0 + (frame / 1000) % 1
    ]
    y = [0.5 for _ in range(15)]
  
    ax.scatter(x, y, color='white', s=50)
    ax.set_xlim(0.1, 3.1)
    ax.set_ylim(0.4, 0.6)
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100000), interval=10)

# Display the animation
plt.show()
