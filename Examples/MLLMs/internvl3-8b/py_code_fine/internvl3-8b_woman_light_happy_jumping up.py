
import matplotlib.pyplot as plt
import numpy as np
import time

def update_positions(positions):
    # Define the animation steps
    steps = 30
    for step in range(steps):
        time.sleep(steps / 1000.0)  # Adjust the speed of the animation
        positions[0] += 1  # Move subject's right leg
        positions[1] -= (step // 5) + 1  # Move subject's left leg
        positions[2] += (step % 5) * 2  # Move subject's right hand
        positions[3] -= (steps - step) // 5 + 1  # Move subject's left hand
        positions[4] += 3 * (step // 10) % 5  # Move subject's body
        positions[5] += 3 * (steps - step) // 10 % 5  # Move subject's back

        plt.cla()
        # Drawing the woman
        plt.scatter([positions[0]], [positions[1]], s=120, color='white')
        plt.scatter([positions[2]], [positions[3]], s=120, color='white')
        plt.scatter([positions[4]], [positions[5]], s=120, color='white')
        plt.scatter([positions[6]], [positions[7]], s=120, color='white')
        plt.scatter([positions[8]], [positions[9]], s=120, color='white')
        plt.scatter([positions[10]], [positions[11]], s=120, color='white')
        plt.scatter([positions[12]], [positions[13]], s=120, color='white')
        plt.scatter([positions[14]], [positions[15]], s=120, color='white')

        plt.xlim([-5, 15])
        plt.ylim([-5, 15])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.show(block=False)

if __name__ == "__main__":
    initial_positions = np.array([0, 10, 3, 12, 4, 10, 1, 8, 3, 10, 6, 10, 7, 0, 15])
    update_positions(initial_positions)
