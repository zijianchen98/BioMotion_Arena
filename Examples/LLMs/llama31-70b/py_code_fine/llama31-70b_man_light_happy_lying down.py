
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
lights = [
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Head
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Neck
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Shoulder
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Elbow
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Wrist
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Shoulder
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Elbow
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Wrist
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Hip
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Knee
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Right Ankle
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Hip
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Knee
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])},  # Left Ankle
    {'x': np.array([0]), 'y': np.array([0]), 'dx': np.array([0]), 'dy': np.array([0])}  # Torso
]

# Define the animation frames
frames = 100

# Define the motion for each point-light
for i in range(frames):
    # Head
    lights[0]['x'] = np.append(lights[0]['x'], 0)
    lights[0]['y'] = np.append(lights[0]['y'], 0)
    
    # Neck
    lights[1]['x'] = np.append(lights[1]['x'], 0)
    lights[1]['y'] = np.append(lights[1]['y'], -5)
    
    # Right Shoulder
    lights[2]['x'] = np.append(lights[2]['x'], 10 * np.sin(i / 10.0))
    lights[2]['y'] = np.append(lights[2]['y'], -10)
    
    # Right Elbow
    lights[3]['x'] = np.append(lights[3]['x'], 15 * np.sin(i / 10.0))
    lights[3]['y'] = np.append(lights[3]['y'], -15)
    
    # Right Wrist
    lights[4]['x'] = np.append(lights[4]['x'], 20 * np.sin(i / 10.0))
    lights[4]['y'] = np.append(lights[4]['y'], -20)
    
    # Left Shoulder
    lights[5]['x'] = np.append(lights[5]['x'], -10 * np.sin(i / 10.0))
    lights[5]['y'] = np.append(lights[5]['y'], -10)
    
    # Left Elbow
    lights[6]['x'] = np.append(lights[6]['x'], -15 * np.sin(i / 10.0))
    lights[6]['y'] = np.append(lights[6]['y'], -15)
    
    # Left Wrist
    lights[7]['x'] = np.append(lights[7]['x'], -20 * np.sin(i / 10.0))
    lights[7]['y'] = np.append(lights[7]['y'], -20)
    
    # Right Hip
    lights[8]['x'] = np.append(lights[8]['x'], 10 * np.sin(i / 10.0))
    lights[8]['y'] = np.append(lights[8]['y'], -30)
    
    # Right Knee
    lights[9]['x'] = np.append(lights[9]['x'], 10 * np.sin(i / 10.0))
    lights[9]['y'] = np.append(lights[9]['y'], -40)
    
    # Right Ankle
    lights[10]['x'] = np.append(lights[10]['x'], 10 * np.sin(i / 10.0))
    lights[10]['y'] = np.append(lights[10]['y'], -50)
    
    # Left Hip
    lights[11]['x'] = np.append(lights[11]['x'], -10 * np.sin(i / 10.0))
    lights[11]['y'] = np.append(lights[11]['y'], -30)
    
    # Left Knee
    lights[12]['x'] = np.append(lights[12]['x'], -10 * np.sin(i / 10.0))
    lights[12]['y'] = np.append(lights[12]['y'], -40)
    
    # Left Ankle
    lights[13]['x'] = np.append(lights[13]['x'], -10 * np.sin(i / 10.0))
    lights[13]['y'] = np.append(lights[13]['y'], -50)
    
    # Torso
    lights[14]['x'] = np.append(lights[14]['x'], 0)
    lights[14]['y'] = np.append(lights[14]['y'], -20)

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Set the limits of the axes
ax.set_xlim(-50, 50)
ax.set_ylim(-70, 30)

# Initialize the plot with the first frame
for i in range(len(lights)):
    ax.plot(lights[i]['x'][0], lights[i]['y'][0], 'wo')

# Define the function to update the plot for each frame
def update(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.set_xlim(-50, 50)
    ax.set_ylim(-70, 30)
    for j in range(len(lights)):
        ax.plot(lights[j]['x'][i], lights[j]['y'][i], 'wo')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
