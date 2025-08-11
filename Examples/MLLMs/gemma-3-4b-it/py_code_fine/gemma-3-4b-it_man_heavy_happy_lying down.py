
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_animation(duration=10, fps=30):
    """
    Generates a point-light animation representing a "lying down" action 
    for a "happyman" figure.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second of the animation.
    """

    # Define the number of points in the light emission
    num_lights = 15

    # Generate random positions for the lights (representing body parts)
    # These positions will be slightly offset and rotated to create a more natural look
    light_positions = np.random.rand(num_lights, 2) * 0.5 - 0.25  # Center around (0, 0)
    light_colors = 'white'

    # Define the animation function
    def animate(frame):
        # Update light positions based on a simple, biomechanically plausible motion
        # This is a simplified representation of a lying down motion.
        for i in range(num_lights):
            # Simulate movement downwards and slightly to the sides
            light_positions[i, 1] += 0.01 * np.sin(frame * 2) #Movement down
            light_positions[i, 0] += 0.005 * np.cos(frame * 3) # Movement to the sides
            
        # Convert positions to image format
        image = np.zeros((1080, 1920), dtype=np.uint8)  # 1080x1920 canvas
        for pos in light_positions:
            image[int(pos[1] * 540), int(pos[0] * 960)] = 255

        return image

    # Create the animation
    ani = animation.FuncAnimation(plt.figure(), animate, frames=int(duration * fps), blit=True, repeat=True)

    # Save the animation as a GIF
    ani.save('lying_down_motion.gif', writer='pillow') # Use Pillow for GIF export

    plt.close() # Close the figure to prevent it from displaying

if __name__ == '__main__':
    generate_motion_animation()
