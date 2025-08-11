
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define key points of a jumping forward motion
key_points = [
    [(30, 10), (40, 15), (50, 5), (60, 15)],  # Head, Left Shoulder, Spine, Right Shoulder
    [(40, 10), (50, 15), (60, 5), (70, 15)],  # Chest, Left Elbow, Elbow, Right Elbow
    [(50, 10), (60, 15), (70, 5), (80, 15)],  # Waist, Left Wrist, Wrist, Right Wrist
    [(60, 10), (70, 15), (80, 5), (90, 15)],  # Hip, Left Knee, Knee, Right Knee
    [(70, 10), (80, 15), (90, 5), (100, 15)]  # Knee, Left Ankle, Ankle, Right Ankle
]

def update_biological_motion(frame):
    for i, (x, y) in enumerate(key_points[-1][frame]):
        plt.scatter(x, y, color='white', s=20, marker='o')
    plt.xlim(0, 120)
    plt.ylim(0, 20)
    plt.gca().set_aspect('equal', adjustable='box')

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_biological_motion, frames=range(5), interval=200, blit=False)
plt.scatter([], [], color='white', s=20, marker='o')
plt.show()
