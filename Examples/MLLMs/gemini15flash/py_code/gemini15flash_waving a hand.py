
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
positions = np.array([
    [0, 0],  # Shoulder
    [0, 1],  # Elbow
    [1, 2],  # Wrist
    [-1, 2], # Wrist
    [0, 3],  # Hand
    [0.5, 0.5], #Shoulder
    [-0.5, 0.5], #Shoulder
    [0.5, 1.5], #Elbow
    [-0.5, 1.5], #Elbow
    [0.5, 2.5], #Wrist
    [-0.5, 2.5], #Wrist
    [0, 4],  # Head
    [0, -1], #Hip
    [0.5, -1.5], # Knee
    [-0.5, -1.5]  #Knee

])

# Function to update the positions of the point lights for each frame
def update(frame):
    global positions
    # Simulate waving hand motion.  This is a simplified example; 
    # more complex biomechanical models could be used for greater realism.

    #Waving motion for right hand
    wave_amplitude = 0.5 * np.sin(frame * 0.1)
    positions[2, 0] += wave_amplitude
    positions[2,1] += 0.2 *np.sin(frame*0.1)
    #Waving motion for left hand
    positions[3, 0] -= wave_amplitude
    positions[3,1] += 0.2 * np.sin(frame * 0.1)

    #Update hand position
    positions[4,0] = (positions[2,0]+positions[3,0])/2 + 0.1 * np.sin(frame*0.05)
    positions[4,1] = (positions[2,1] + positions[3,1])/2 + 0.1 * np.sin(frame*0.05)


    #Clear previous plot
    ln.set_offsets(positions)

    return ln,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the point light scatter plot
ln, = ax.plot([], [], 'wo', markersize=8)



# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)

# Show the animation
plt.show()

