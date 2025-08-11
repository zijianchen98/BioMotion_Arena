
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_bowing_woman():
    """
    Generates a point-light animation depicting a happy woman bowing.
    """

    # Define the number of lights
    num_lights = 15

    # Generate random coordinates for the lights
    lights = np.random.rand(num_lights, 2) * 0.5  # Scale coordinates to 0-0.5 for size

    # Define the bowing motion parameters (adjust for realism)
    time_scale = 1.0  # Adjust to control the speed of the animation
    bow_amplitude = 0.2
    bow_frequency = 3.0
    twist_amplitude = 0.05
    twist_frequency = 5.0
    
    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Create the light objects
    lights_plot = ax.scatter(lights[:, 0], lights[:, 1], s=50, c='white')

    # Animation function
    def animate(frame):
        for i in range(num_lights):
            # Bowing motion
            lights[i, 0] = np.sin(frame * bow_amplitude * bow_frequency) * 0.3 + 0.15
            lights[i, 1] = np.sin(frame * bow_amplitude * bow_frequency) * 0.3 + 0.15

            # Twist motion
            lights[i, 0] += np.sin(frame * twist_amplitude * twist_frequency) * 0.02
            lights[i, 1] += np.cos(frame * twist_amplitude * twist_frequency) * 0.02
            
        lights_plot.set_offsets(lights)
        return lights_plot

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=100, blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("bowing_woman.gif", writer='pillow', fps=30) 

    plt.show()

if __name__ == '__main__':
    animate_bowing_woman()
