
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy woman
point_lights = np.array([
    [0.1, 0.5],  # Head
    [0.2, 0.6],  # Right shoulder
    [0.8, 0.6],  # Left shoulder
    [0.3, 0.7],  # Right elbow
    [0.7, 0.7],  # Left elbow
    [0.4, 0.8],  # Right hand
    [0.6, 0.8],  # Left hand
    [0.5, 0.4],  # Hip
    [0.3, 0.3],  # Right knee
    [0.7, 0.3],  # Left knee
    [0.2, 0.2],  # Right ankle
    [0.8, 0.2],  # Left ankle
    [0.4, 0.5],  # Right foot
    [0.6, 0.5],  # Left foot
    [0.5, 0.1]   # Torso
])

# Define the movement patterns for each point-light
def move_head(t):
    return np.array([0.1 + 0.05 * np.sin(t), 0.5 + 0.05 * np.cos(t)])

def move_shoulders(t):
    return np.array([
        [0.2 + 0.05 * np.sin(t + np.pi/2), 0.6 + 0.05 * np.cos(t + np.pi/2)],
        [0.8 + 0.05 * np.sin(t + np.pi/2), 0.6 + 0.05 * np.cos(t + np.pi/2)]
    ])

def move_elbows(t):
    return np.array([
        [0.3 + 0.05 * np.sin(t + np.pi), 0.7 + 0.05 * np.cos(t + np.pi)],
        [0.7 + 0.05 * np.sin(t + np.pi), 0.7 + 0.05 * np.cos(t + np.pi)]
    ])

def move_hands(t):
    return np.array([
        [0.4 + 0.05 * np.sin(t + 3*np.pi/2), 0.8 + 0.05 * np.cos(t + 3*np.pi/2)],
        [0.6 + 0.05 * np.sin(t + 3*np.pi/2), 0.8 + 0.05 * np.cos(t + 3*np.pi/2)]
    ])

def move_hip(t):
    return np.array([0.5 + 0.05 * np.sin(t), 0.4 + 0.05 * np.cos(t)])

def move_knees(t):
    return np.array([
        [0.3 + 0.05 * np.sin(t + np.pi), 0.3 + 0.05 * np.cos(t + np.pi)],
        [0.7 + 0.05 * np.sin(t + np.pi), 0.3 + 0.05 * np.cos(t + np.pi)]
    ])

def move_ankles(t):
    return np.array([
        [0.2 + 0.05 * np.sin(t + 3*np.pi/2), 0.2 + 0.05 * np.cos(t + 3*np.pi/2)],
        [0.8 + 0.05 * np.sin(t + 3*np.pi/2), 0.2 + 0.05 * np.cos(t + 3*np.pi/2)]
    ])

def move_feet(t):
    return np.array([
        [0.4 + 0.05 * np.sin(t + np.pi/2), 0.5 + 0.05 * np.cos(t + np.pi/2)],
        [0.6 + 0.05 * np.sin(t + np.pi/2), 0.5 + 0.05 * np.cos(t + np.pi/2)]
    ])

def move_torso(t):
    return np.array([0.5 + 0.05 * np.sin(t), 0.1 + 0.05 * np.cos(t)])

# Define the animation function
def animate(t):
    fig.clear()
    fig.set_facecolor('black')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Update point-light locations
    head = move_head(t)
    shoulders = move_shoulders(t)
    elbows = move_elbows(t)
    hands = move_hands(t)
    hip = move_hip(t)
    knees = move_knees(t)
    ankles = move_ankles(t)
    feet = move_feet(t)
    torso = move_torso(t)
    
    # Draw the point-lights
    ax.plot(head[0], head[1], 'wo')
    ax.plot(shoulders[:, 0], shoulders[:, 1], 'wo')
    ax.plot(elbows[:, 0], elbows[:, 1], 'wo')
    ax.plot(hands[:, 0], hands[:, 1], 'wo')
    ax.plot(hip[0], hip[1], 'wo')
    ax.plot(knees[:, 0], knees[:, 1], 'wo')
    ax.plot(ankles[:, 0], ankles[:, 1], 'wo')
    ax.plot(feet[:, 0], feet[:, 1], 'wo')
    ax.plot(torso[0], torso[1], 'wo')
    
    # Draw the jumping motion
    if t < np.pi:
        ax.plot([head[0], shoulders[0, 0]], [head[1], shoulders[0, 1]], 'w-')
        ax.plot([head[0], shoulders[1, 0]], [head[1], shoulders[1, 1]], 'w-')
        ax.plot([shoulders[0, 0], elbows[0, 0]], [shoulders[0, 1], elbows[0, 1]], 'w-')
        ax.plot([shoulders[1, 0], elbows[1, 0]], [shoulders[1, 1], elbows[1, 1]], 'w-')
        ax.plot([elbows[0, 0], hands[0, 0]], [elbows[0, 1], hands[0, 1]], 'w-')
        ax.plot([elbows[1, 0], hands[1, 0]], [elbows[1, 1], hands[1, 1]], 'w-')
        ax.plot([hip[0], knees[0, 0]], [hip[1], knees[0, 1]], 'w-')
        ax.plot([hip[0], knees[1, 0]], [hip[1], knees[1, 1]], 'w-')
        ax.plot([knees[0, 0], ankles[0, 0]], [knees[0, 1], ankles[0, 1]], 'w-')
        ax.plot([knees[1, 0], ankles[1, 0]], [knees[1, 1], ankles[1, 1]], 'w-')
        ax.plot([ankles[0, 0], feet[0, 0]], [ankles[0, 1], feet[0, 1]], 'w-')
        ax.plot([ankles[1, 0], feet[1, 0]], [ankles[1, 1], feet[1, 1]], 'w-')
    else:
        ax.plot([head[0], shoulders[0, 0]], [head[1] + 0.1 * np.sin(t - np.pi), shoulders[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([head[0], shoulders[1, 0]], [head[1] + 0.1 * np.sin(t - np.pi), shoulders[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([shoulders[0, 0], elbows[0, 0]], [shoulders[0, 1] + 0.1 * np.sin(t - np.pi), elbows[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([shoulders[1, 0], elbows[1, 0]], [shoulders[1, 1] + 0.1 * np.sin(t - np.pi), elbows[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([elbows[0, 0], hands[0, 0]], [elbows[0, 1] + 0.1 * np.sin(t - np.pi), hands[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([elbows[1, 0], hands[1, 0]], [elbows[1, 1] + 0.1 * np.sin(t - np.pi), hands[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([hip[0], knees[0, 0]], [hip[1] + 0.1 * np.sin(t - np.pi), knees[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([hip[0], knees[1, 0]], [hip[1] + 0.1 * np.sin(t - np.pi), knees[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([knees[0, 0], ankles[0, 0]], [knees[0, 1] + 0.1 * np.sin(t - np.pi), ankles[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([knees[1, 0], ankles[1, 0]], [knees[1, 1] + 0.1 * np.sin(t - np.pi), ankles[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([ankles[0, 0], feet[0, 0]], [ankles[0, 1] + 0.1 * np.sin(t - np.pi), feet[0, 1] + 0.1 * np.sin(t - np.pi)], 'w-')
        ax.plot([ankles[1, 0], feet[1, 0]], [ankles[1, 1] + 0.1 * np.sin(t - np.pi), feet[1, 1] + 0.1 * np.sin(t - np.pi)], 'w-')

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 128), interval=50)

plt.show()
