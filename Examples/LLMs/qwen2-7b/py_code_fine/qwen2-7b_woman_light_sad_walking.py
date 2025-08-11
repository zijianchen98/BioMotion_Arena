
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_walking(num_frames, duration=10):
    fig = plt.figure(figsize=(6, 6))
    ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
    ax.set_facecolor('black')
    
    # Define the sad woman's position
    woman_pos = [0, 0]
    
    def update(frame):
        # Update the woman's position based on her walking motion
        dx = 0.05 * np.sin(((frame / duration) * 2 * np.pi)
        dy = -0.04 * np.cos((frame / duration) * 2 * np.pi)
        woman_pos[0] += dx
        woman_pos[1] += dy
        
        # Ensure she stays within the frame
        if woman_pos[0] > 1:
            woman_pos[0] = 1
        elif woman_pos[0] < -1:
            woman_pos[0] = -1
        if woman_pos[1] > 1:
            woman_pos[1] = 1
        elif woman_pos[1] < -1:
            woman_pos[1] = -1
            
        # Plot the point lights representing the woman
        ax.clear()
        ax.set_facecolor('black')
        ax.plot(woman_pos[0], woman_pos[1], 'w.', markersize=10)
        
        # Plot additional 14 white point-lights
        for i in range((-1, 2):
            ax.plot(0.5 * np.sin((i / 2) * 2 * np.pi), 0.8 * np.cos((i / 2) * 2 * np.pi), 'w.', markersize=10)
        
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.axis('off')

    ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000//num_frames)
    plt.show()

# Run the function with 15 frames
sad_woman_walking(15)
