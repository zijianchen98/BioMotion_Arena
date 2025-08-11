
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
waving_amplitude = 0.2
speed = 0.1

# Define the initial positions of the point lights
# Here, I'm creating a simple structure to represent a person
body = np.array([
    [0, 0],   # center
    [0, 0.5], # head
    [-0.1, 0.4], [0.1, 0.4], # shoulders
    [-0.1, 0.3], [0.1, 0.3], # arms (rest)
    [-0.1, 0], [0.1, 0],     # legs
])

# Function to update the points for each frame
def update(frame):
    plt.clf()  # Clear the previous frame
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('off')  # Turn off the axes

    # Calculate new positions for the waving action (vertical movement for the hand)
    hand_wave = np.array([
        [-0.1, 0.3 + waving_amplitude * np.sin(frame * speed)], # left hand
        [0.1, 0.3 + waving_amplitude * np.sin(frame * speed)]   # right hand
    ])
    
    # Combine body and waving hands
    positions = np.vstack([body, hand_wave])
    
    # Extract x and y coordinates
    x, y = positions[:, 0], positions[:, 1]
    
    # Plot the points
    plt.scatter(x, y, color='white')
    plt.gca().set_facecolor('black')

# Create the figure and animate
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# To save the animation, you can uncomment the following line:
# ani.save('waving_hand_animation.mp4', writer='ffmpeg', fps=30)

plt.show()
