
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_jumping_man():
    """
    Generates an animation of a "happyman" jumping up with 15 point-lights.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

    # Point-light parameters
    num_lights = 15
    light_radius = 0.05
    light_color = 'white'

    # Create the lights
    lights = []
    for _ in range(num_lights):
        light = plt.Circle((np.random.rand() * 1.2, np.random.rand() * 1.2), 
                            light_radius, color=light_color)
        lights.append(light)
        ax.add_patch(light)

    # Animation data - simulate jumping motion
    frames = 24
    x_data = np.linspace(0, 2, frames)
    y_data = np.linspace(1, 0.5, frames)  # Initial height, descending
    z_data = np.linspace(0, 1, frames)  # Simulate vertical jump
    
    for i in range(frames):
        for light in lights:
            light.center = (x_data[i], y_data[i])
            light.set_height(z_data[i] * light_radius)
        
    ani = animation.FuncAnimation(fig, func=lambda frame: [light.set_props(dict(scale=z_data[frame] * light_radius)) for light in lights], frames=frames, repeat=False)

    plt.show()

if __name__ == '__main__':
    animate_jumping_man()
