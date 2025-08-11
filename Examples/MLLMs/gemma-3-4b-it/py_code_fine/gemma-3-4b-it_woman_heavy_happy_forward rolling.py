
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_motion_animation():
    """Generates a point-light animation representing a happy woman performing a forward roll."""

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Create the point lights
    lights = []
    for i in range(15):
        light = plt.scatter(0, 0, s=50, c='white')
        lights.append(light)

    # Define the roll motion parameters
    frame_rate = 10  # Frames per second
    num_frames = 240  # Number of frames in the animation
    
    # Motion trajectory (simplified for demonstration)
    x = np.linspace(0, 1, num_frames)
    y = np.linspace(0, 1, num_frames)
    z = np.linspace(0, 1, num_frames)

    # Roll motion - simple sinusoidal wave
    roll_angle = np.linspace(0, 2 * np.pi, num_frames)

    # Update the positions of the lights in each frame
    def update(frame):
        for i in range(len(lights)):
            # Calculate the angle of the light based on the frame number
            angle = roll_angle[frame]
            
            # Simplified roll motion - x and y change with the angle
            x_pos = np.cos(angle)
            y_pos = np.sin(angle)
            
            # Random z-position variation to make it look more natural
            z_pos = 0.5 + 0.3 * np.random.rand()  # Slightly random z-position
            
            lights[i].set_offsets([x_pos, y_pos, z_pos])
        return lights

    ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)
    
    plt.show()

if __name__ == '__main__':
    generate_motion_animation()
