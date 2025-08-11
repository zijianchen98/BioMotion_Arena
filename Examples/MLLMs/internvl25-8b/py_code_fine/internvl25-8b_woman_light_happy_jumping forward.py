
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def update(frame, points):
    x = np.sin(frame * points['speed'] + points['phase'])
    y = np.cos(frame * points['speed'] + points['phase'])
    points['set'][:] = x * points['amplitude']
    points['center'][:] = y * points['amplitude']
    return points['set'], points['center']

def main():
    fig = plt.figure(facecolor='black')
    ax = fig.add_subplot(111)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    points = {
       'set': np.zeros(15),
        'center': np.zeros(15),
       'speed': 0.05,
        'amplitude': 1,
        'phase': 0.0,
       'set_initial': np.sin(np.linspace(0, 2 * np.pi, 15)),
        'center_initial': np.cos(np.linspace(0, 2 * np.pi, 15))
    }
    scat, = ax.plot([], [], 'o', color='white', markersize=10)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=np.linspace(0, 100, 200),
        fargs=(points,),
        init_func=lambda: (points['set_initial'], points['center_initial']),
        blit=True,
        interval=50
    )
    plt.show()

if __name__ == '__main__':
    main()
