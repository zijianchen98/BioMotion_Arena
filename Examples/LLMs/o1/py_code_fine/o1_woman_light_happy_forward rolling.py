import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_forward_roll_frames(num_frames=60):
    """
    Generate a sequence of 2D coordinates (x, y) for 15 points mimicking
    a forward roll. Each element of the returned array corresponds to one
    animation frame. The shape of the returned array is (num_frames, 15, 2).
    
    This is a simplified, approximate version of a forward roll biological motion.
    It arranges 15 'joints' in a plausible rolling arc. You can refine or replace
    these coordinates for more biomechanical realism.
    """
    frames = np.zeros((num_frames, 15, 2))
    
    # Time array for parameterizing motion
    t = np.linspace(0, 2*np.pi, num_frames, endpoint=False)
    
    # Primary radius for the "main body circle"
    body_radius = 0.5
    
    # We'll move the overall center to simulate a rolling translation
    # Let's create a horizontal movement from left to right
    # while rotating the body in a forward flipping motion.
    
    center_x_movement = np.linspace(-3, 3, num_frames)
    center_y_base = 0  # baseline
    # For a bit of vertical variation to simulate a gentle arc
    center_y_movement = 0.2 * np.sin(t)
    
    # We'll define 15 points. Indices might correspond to
    # 0) head, 1) neck, 2) r_shoulder, 3) r_elbow, 4) r_wrist,
    # 5) l_shoulder, 6) l_elbow, 7) l_wrist,
    # 8) r_hip, 9) r_knee, 10) r_ankle,
    # 11) l_hip, 12) l_knee, 13) l_ankle,
    # 14) mid-torso or root
    #
    # For each frame, we rotate these points around an axis
    # while translating the center from left to right.
    
    # Relative angles for each point around the center:
    # (arranged roughly in a circle or with mild offsets)
    point_angles = np.array([
        0.0,           # head
        0.4,           # neck
        0.8,           # right shoulder
        1.2,           # right elbow
        1.6,           # right wrist
        -0.8,          # left shoulder
        -1.2,          # left elbow
        -1.6,          # left wrist
        2.4,           # right hip
        2.8,           # right knee
        3.2,           # right ankle
        -2.4,          # left hip
        -2.8,          # left knee
        -3.2,          # left ankle
        np.pi          # torso center (slightly behind the head)
    ])
    
    # Radii for each of the 15 points (distance from body center)
    point_radii = np.array([
        0.35,  # head
        0.25,  # neck
        0.25,  # right shoulder
        0.3,   # right elbow
        0.35,  # right wrist
        0.25,  # left shoulder
        0.3,   # left elbow
        0.35,  # left wrist
        0.25,  # right hip
        0.3,   # right knee
        0.35,  # right ankle
        0.25,  # left hip
        0.3,   # left knee
        0.35,  # left ankle
        0.1    # torso center
    ])
    
    for i in range(num_frames):
        # Compute rotation angle for the forward roll (full 2*pi flip across num_frames)
        roll_angle = (2*np.pi * i / num_frames)
        
        # Center of the body
        cx = center_x_movement[i]
        cy = center_y_base + center_y_movement[i]
        
        # For each of 15 points, rotate by roll_angle around (cx, cy)
        for p in range(15):
            px = cx + point_radii[p] * np.cos(point_angles[p] + roll_angle)
            py = cy + point_radii[p] * np.sin(point_angles[p] + roll_angle)
            frames[i, p, 0] = px
            frames[i, p, 1] = py
    
    return frames

def update_animation(frame_idx, scatter_plot, data):
    """ Update function for FuncAnimation: sets new positions for each of the 15 point-lights. """
    scatter_plot.set_offsets(data[frame_idx])
    return (scatter_plot,)

def main():
    # Generate frames
    data = generate_forward_roll_frames(num_frames=60)
    
    # Create plotting context
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')  # Black background for the figure
    ax.set_facecolor('black')         # Black background for the plot area
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes for a clean stimulus-like presentation
    
    # Initial scatter plot (15 white points)
    scatter_plot = ax.scatter(data[0, :, 0], data[0, :, 1],
                              color='white', s=40, marker='o')
    
    # Create animation using FuncAnimation
    ani = animation.FuncAnimation(
        fig,
        update_animation,
        frames=len(data),
        fargs=(scatter_plot, data),
        interval=50,  # delay between frames in ms
        blit=True,
        repeat=True
    )
    
    # Show the animation
    plt.show()

if __name__ == '__main__':
    main()