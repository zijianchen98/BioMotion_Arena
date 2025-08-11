
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_dot_positions(frame):
    # Simplified model to simulate turning around using 15 points
    angles = np.linspace(0, 2 * np.pi, 15, endpoint=False)
    radius = 0.4 + 0.2 * np.sin(frame * np.pi / 30)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    # Add more complexity to simulate body parts
    x += 0.1 * np.sin(frame * np.pi / 15)
    y += 0.1 * np.cos(frame * np.pi / 15)
    
    # Add head movement
    head_angle = frame * np.pi / 30
    x_head = 0.2 * np.cos(head_angle)
    y_head = 0.2 * np.sin(head_angle)
    
    positions = np.vstack((x, y))
    positions = np.hstack((positions, np.array([[x_head], [y_head]])))
    
    return positions

def update(frame):
    plt.clf()
    plt.axis('off')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    
    positions = generate_dot_positions(frame)
    plt.scatter(positions[0], positions[1], color='white')

fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=60, interval=50)

plt.show()
