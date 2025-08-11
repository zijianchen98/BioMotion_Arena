
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_jumping_man():
    """
    Generates an animation of a "jumping up" man with point lights.

    The animation shows a simplified man figure with 15 white point lights 
    moving against a black background, simulating a jump.  The motion is 
    designed to be biomechanically plausible.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 2)
    ax.set_aspect('equal')

    # Create the man figure (simplified)
    man = plt.plot([-0.5, 0.5], [0, 1], 'w-', lw=2)[0]  # Simple stick figure

    # Create the point lights
    lights = []
    for i in range(15):
        light = plt.scatter(0, 0, s=50, color='w')
        lights.append(light)
    
    # Define the jump trajectory (simplified)
    def jump_trajectory(t):
        # Simulate a jump up, starting at y=0
        y = 2 * (t**2) 
        x = t  #  simplified x movement
        return x, y

    # Animation function
    def animate(frame):
        x_coord = jump_trajectory(frame/100.0)[0]
        y_coord = jump_trajectory(frame/100.0)[1]

        man.set_data(x_coord, y_coord)

        for light in lights:
            light.set_data(x_coord, y_coord)

        return lights + [man]

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

    plt.title("Jumping Man with Point Lights")
    plt.show()


if __name__ == '__main__':
    animate_jumping_man()
