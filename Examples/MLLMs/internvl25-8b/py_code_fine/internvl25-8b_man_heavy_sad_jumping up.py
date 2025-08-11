
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_sadman():
    # Define positions (15 points for the 12 body parts + 3 head parts + neck)
    positions = np.array([
        [100, 200],  # Head
        [110, 180],  # R eye
        [120, 160],  # L eye
        [60, 180],   # Nose
        [90, 220],   # R ear
        [130, 220],  # L ear
        [50, 180],   # R shoulder
        [150, 180],  # L shoulder
        [90, 280],   # R elbow
        [120, 260],  # L elbow
        [150, 300],  # Right wrist
        [170, 300],  # Left wrist
        [110, 230],  # Right hip
        [120, 240],  # Left hip
        [140, 240],  # Right knee
        [160, 220],  # Left knee
        [130, 210]   # Ankle (neck position if required)
    ])
    return positions

def update_positions(frame, positions):
    # Calculate the movements
    time_frame = frames * 0.01
    jump_height = 120
    jump_speed = 0.8
    
    # Define easing function (simple quadratic model)
    def ease_in(t):
        return (t*t * (2 - t))
    
    def movement(x, y):
        if 0 <= frame < jump_height / 20:
            alpha = ease_in(frame / jump_height)
            delta_y = (alpha * jump_height) / 20
            return [x, y + delta_y]
        elif jump_height / 20 <= frame <= jump_height * 1.5:
            alpha = 1 - ease_in((frame - jump_height / 20) / (jump_height * 1.5))
            delta_y = -(alpha * jump_height) / 20
            return [x, y + delta_y]
        elif frame >= jump_height * 1.5:
            alpha = ease_in((frame - jump_height * 1.5) / (frame - jump_height * 3))
            delta_y = -(alpha * 120) / 100  # Reduce the speed towards final resting position
            return [x, y + delta_y]

    # Update individual points with smooth movement
    return [movement(pos, frame) for pos in positions]

def plot_animation(positions, frames=200, interval=20):
    fig, ax = plt.subplots()
    background = plt.cm.set_color(ax, 'k')
    
    def init():
        ax.clear()
        ax.set_xlim(0, 150)
        ax.set_ylim(0, 350)
        background = plt.cm.set_color(ax, 'k')
        return positions[0], ax.collections
    
    def animate(frame, positions, line):
        line.set_data(positions[:10].T)  # Plot only the lower body for simplicity
        return line,

    positions = create_sadman()
    line, = ax.plot(positions[0][:, 1], positions[0][:, 0], 'o', color='white', markersize=8, marker='o', zorder=1)

    ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, fargs=(positions, line), interval=interval, blit=True)

    plt.savefig('sadman_jumping.gif', dpi=100)
    plt.show()

if __name__ == "__main__":
    plot_animation()

