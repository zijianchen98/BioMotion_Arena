
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_jump_frames():
    frames = []
    points = [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7)]
    for i in range(15):
        # Simulate a jump motion (simple vertical movement)
        for point in points:
            new_y = 7 + i
            if new_y > 7:
                frames.append(((point[0], new_y),))
    return frames

def animate_scatter(frames):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    points = []
    for point_size in [1]*len([y for y in range(10, 20)]):
        points.append(plt.scatter([], [], s=point_size))
    
    anim = animation.FuncAnimation(
        fig, 
        update_points, 
        frames=frames,
        fargs=(points,),
        interval=100,
        blit=True
    )
    plt.show()
    
def update_points(frame, points):
    for point, scatter in zip(frame, points):
        scatter.set_offsets([point])

animate_scatter(sadman_jump_frames())
