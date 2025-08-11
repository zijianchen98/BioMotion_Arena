
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_point_light(subject, action, n_frames=100):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim((-1, 1)
    ax.set_ylim((-1, 1))
    ax.set_aspect('equal')
    ax.axis('off')

    # Background
    ax.imshow(np.zeros((100, 100)), extent=[-1, 1, -1, 1], cmap='Greys', alpha=0.8)

    # Points representing of the subject
    points = np.zeros((n_frames, 15, 2))
    for i in range(n_frames):
        # Generate random points within the bounds of the plot
        points[i] = np.random.rand((15, 2) * 2 - 1
        
        # Update the positions of the points based on the action
        if action == 'waving_hand':
            # Example logic for waving hand motion
            # This is a simple example and can be replaced or expanded as needed
            points[i, 0] += np.sin(i / 20) * 0.1
            points[i, 1] += np.cos(i / 10) * 0.1
            points[i, 6] += np.sin(i / 15) * 0.2
            points[i, 7] += np.cos(i / 15) * 0.2
            
        # Update the scatter plot
        scat.set_offsets(points[i])
        ax.relim()
        ax.autoscale_view()

    ani = FuncAnimation(fig, update, frames=n_frames, blit=True, interval=20)
    plt.show()

animate_point_light('sadwoman', 'waving_hand')
