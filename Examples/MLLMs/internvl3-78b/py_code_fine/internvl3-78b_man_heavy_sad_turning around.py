
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
# These positions are static and will animate as described in 3
points = [
    [2, 10],
    [2.5, 9],
    [3, 8],
    [3.5, 9],
    [4, 10],
    [4.5, 9],
    [5, 8],
    [5.5, 9],
    [6, 10],
    [6.5, 9.5],
    [4, 6],
    [6, 6],
    [1, 3],
    [5, 3],
    [9, 3]
]

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set(facecolor='black', xlim=(0, 10), ylim=(0, 15), aspect='equal', xticks=[])
ax.grid(False)

# Function to animate
def update(frame):
    ax.clear()
    ax.set(facecolor='black', xlim=(0, 10), ylim=(0, 15), aspect='equal', xticks=[])
    
    for i in range(len(points)):
        x, y = points[i]
        ax.plot(x + frame/10, y, 'o', color='white')

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(101), interval=25, repeat=False)

# Show the plot
plt.show()
