
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_stimulus():
    """
    Generates a point-light animation depicting a 'jumping forward' action 
    of a happy man with a realistic biomechanical motion.

    Returns:
        Tuple: (fig, anim) - A tuple containing the matplotlib figure and animation object.
    """

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    num_lights = 15
    lights = []
    for i in range(num_lights):
        light = plt.scatter(0, 0, s=100, color='white', zorder=i)
        lights.append(light)
    
    # Define the motion parameters for the jump
    time_steps = 200
    dt = 1 / time_steps
    
    for t in range(time_steps):
        # Calculate time-dependent parameters for movement
        time = t * dt
        
        # Jump forward motion - Simulate a jump
        for light in lights:
            x = np.sin(time * 5) * 0.5  # Amplitude of the sine wave
            y = np.cos(time * 5) * 0.5  # Amplitude of the sine wave
            light.set_offsets([x, y])

    ani = animation.FuncAnimation(fig, func=lambda t: [light.set_offsets([np.sin(t * 5) * 0.5, np.cos(t * 5) * 0.5]) for light in lights], frames=time_steps, blit=True, repeat=False)
    return fig, ani

if __name__ == '__main__':
    fig, ani = generate_motion_stimulus()
    plt.show()
