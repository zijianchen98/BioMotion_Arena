
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define joint indices
joints = {
    'head': 0,
    'shoulder1': 1,
    'shoulder2': 2,
    'elbow1': 3,
    'elbow2': 4,
    'hand1': 5,
    'hand2': 6,
    'hip1': 7,
    'hip2': 8,
    'knee1': 9,
    'knee2': 10,
    'foot1': 11,
    'foot2': 12,
    'torso': 13,
    'waist': 14
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initial coordinates for the joints
initial_coords = np.array([
    [0.5, 0.8],  # head
    [0.4, 0.7],  # shoulder1
    [0.6, 0.7],  # shoulder2
    [0.35, 0.6],  # elbow1
    [0.65, 0.6],  # elbow2
    [0.3, 0.5],  # hand1
    [0.7, 0.5],  # hand2
    [0.45, 0.4],  # hip1
    [0.55, 0.4],  # hip2
    [0.42, 0.3],  # knee1
    [0.58, 0.3],  # knee2
    [0.38, 0.2],  # foot1
    [0.62, 0.2],  # foot2
    [0.5, 0.55],  # torso
    [0.5, 0.45]   # waist
])

# Create point lights
point_lights, = ax.plot([], [], 'w.', markersize=10)

def init():
    point_lights.set_data([], [])
    return point_lights,

def update(frame):
    amplitude = 0.1
    freq = 0.05
    offset = np.sin(frame * freq) * amplitude

    coords = initial_coords.copy()
    
    # Animate the upper body
    coords[joints['head']] += [0, offset]
    coords[joints['shoulder1']] += [0, offset]
    coords[joints['shoulder2']] += [0, offset]
    coords[joints['elbow1']] += [0, offset]
    coords[joints['elbow2']] += [0, offset]
    coords[joints['hand1']] += [0, offset]
    coords[joints['hand2']] += [0, offset]

    # Animate the lower body
    coords[joints['hip1']] += [0, offset]
    coords[joints['hip2']] += [0, offset]
    coords[joints['knee1']] += [0, offset * 1.5]
    coords[joints['knee2']] += [0, offset * 1.5]
    coords[joints['foot1']] += [0, offset * 2]
    coords[joints['foot2']] += [0, offset * 2]

    # Update torso and waist
    coords[joints['torso']] += [0, offset * 0.8]
    coords[joints['waist']] += [0, offset * 0.7]

    # Move the body forward
    coords += [0.005 * frame, 0]

    point_lights.set_data(coords[:, 0], coords[:, 1])
    return point_lights,

ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)
plt.axis('off')
plt.show()
