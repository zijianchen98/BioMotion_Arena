
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
num_points = 15
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_facecolor('black')

# Initialize point positions
points, = ax.plot([], [], 'wo', markersize=8)

# Define jumping motion (adjust parameters for different styles)
def jump_motion(t):
    x = np.zeros((num_points, len(t)))
    y = np.zeros((num_points, len(t)))
    
    # Example coordinates - adjust to match the provided image and jumping action
    coords = np.array([
        [0, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [2, 2], [2,-2], [-2,2], [-2,-2],
        [0.5, 2], [-0.5, 2], [0.5, -2], [-0.5, -2], [0,3], [0, -3]
    ])


    #Jumping Motion Simulation
    for i in range(num_points):
        amplitude = 2  # Adjust the jump height
        frequency = 0.5 # Adjust the jump speed

        x[i,:] = coords[i,0] + 0.5*np.sin(2 * np.pi * frequency * t + i*0.2)
        y[i,:] = coords[i,1] + amplitude * np.sin(2 * np.pi * frequency * t)


    return x,y




# Animation function
def animate(i):
    t = np.linspace(0, i / 30, 30) # Adjust speed here
    x, y = jump_motion(t)
    points.set_data(x[:, -1], y[:, -1])  # Update only last frame
    return points,


# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Save or display animation (comment out one option)
ani.save('jumping_man.gif', writer='imagemagick', fps=30) # requires imagemagick
#plt.show()

