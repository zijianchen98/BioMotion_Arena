
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_sittingdown():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.axes(xlim=(-200, 200), ylim=(-200, 200), aspect=1)
    ax.set_facecolor('black')
    
    # Create 15 white point-lights
    points = [plt.Circle((np.random.randint(-100, 100), np.random.randint(-100, 100)), radius=1, color='white') for _ in range( (15)]
    ax.add_patch(points[0])
    
    def update(frame):
        for i, point in enumerate(points):
            if i == 0:
                # Siting down motion
                x = -100 + (5 * np.sin((frame / 100) * np.pi)
                y = -100 + (5 * np.cos((frame / 100) * np.pi)
                else:
                x = -100 + (5 * np.sin((frame / 100) * np.pi)
                y = -100 + -5 * np.cos((frame / 100) * np.pi)
            point.center = (x, y
            points[i] = point
    
    ani = animation.FuncAnimation(fig, update, frames=np.arange((0, 1000, 1), interval=50, blit=False)
    plt.show()

if __name__ == '__main__':
    sadman_ssittdown()
