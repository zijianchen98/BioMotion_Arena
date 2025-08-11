
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HUMAN_SIZE = 0.5

# Define the subject and action
subject = {
    'x': 0,
    'y': HEIGHT // 2,
    'vx': 0,
    'vy': 0,
    'weight': 200
}

def animate(i):
    global subject
    subject['x'] += subject['vx'] * i / 100
    subject['y'] += subject['vy'] * i / 100
    
    # Check if subject is on the ground
    if subject['y'] + HUMAN_SIZE // 2 > HEIGHT:
        subject['y'] = HEIGHT - HUMAN_SIZE // 2
        subject['vy'] = -1.5
    
    # Move point lights
    for light in lights:
        light['x'] += light['dx'] * i / 100
        light['y'] += light['dy'] * i / 100
        
        # Check if light is out of bounds
        if light['x'] < -WIDTH // 2 or light['x'] > WIDTH // 2:
            light['x'] = WIDTH // 2
            light['y'] = -light['y'] * 2
        
        # Check if light is on the subject
        if light['x'] < subject['x'] + HUMAN_SIZE // 2 and light['x'] + HUMAN_SIZE // 2 > subject['x'] - HUMAN_SIZE // 2:
            light['y'] = subject['y'] + HUMAN_SIZE // 2
    
    return subject, lights

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point lights
lights = []
for i in range(15):
    dx = np.random.uniform(-WIDTH // 4, WIDTH // 4)
    dy = np.random.uniform(-HEIGHT // 4, HEIGHT // 4)
    light = {
        'x': dx,
        'y': dy,
        'dx': dx / 10,
        'dy': dy / 10,
        'vy': 0,
        'weight': 200
    }
    lights.append(light)

# Set the axis limits and aspect ratio
ax.set_xlim(-WIDTH // 2, WIDTH // 2)
ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)
ax.set_aspect('equal')

# Set the axis limits for the subject
ax.set_xlim(subject['x'] - HUMAN_SIZE // 2 - 10, subject['x'] + HUMAN_SIZE // 2 + 10)
ax.set_ylim(subject['y'] - HUMAN_SIZE // 2 - 10, subject['y'] + HUMAN_SIZE // 2 + 10)

# Initialize the subject
subject = {
    'x': 0,
    'y': HEIGHT // 2,
    'vx': 0,
    'vy': 0,
    'weight': 200
}

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=20, blit=True)

# Show the animation
plt.show()
