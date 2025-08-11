
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Creating a biomechanical simulation for bowing motion
def generate_bowing_motion():
    """
    A function to simulate the bowing motion of a sad woman. 
    This generates the realistic movement of 15 point-lights (key joints: head, shoulders, elbows, hands, hips, knees, feet).
    """
    num_frames = 100  # Number of animation frames
    num_points = 15  # Number of key points in the human model
    
    # Joints coordinates for bowing animation (initial position)
    joints = np.array([
        [0, 10],  # head
        [-2, 8],  # left shoulder
        [2, 8],   # right shoulder
        [-3, 6],  # left elbow
        [3, 6],   # right elbow
        [-4, 4],  # left hand
        [4, 4],   # right hand
        [-2, 4],  # left hip
        [2, 4],   # right hip
        [-2.5, 2],  # left knee
        [2.5, 2],   # right knee
        [-3, 0],  # left foot
        [3, 0],   # right foot
        [0, 7],  # spine midpoint (upper)
        [0, 5]   # spine midpoint (lower)
    ])
    
    # Generate frames for bowing motion
    frames = []
    for frame in range(num_frames):
        angle = np.sin(frame / num_frames * 2 * np.pi) * 30  # Bow angle oscillation between -30 and 30 degrees
        rotation_matrix = np.array([
            [np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
            [np.sin(np.radians(angle)), np.cos(np.radians(angle))]
        ])
        
        # Apply rotation to upper body points (head, shoulders, elbows, spine upper/lower)
        upper_body_indices = [0, 1, 2, 13, 14, 3, 4]
        rotated_joints = joints.copy()
        for index in upper_body_indices:
            rotated_joints[index] = np.dot(rotation_matrix, joints[index] - joints[8]) + joints[8]
        
        frames.append(rotated_joints)
    
    return np.array(frames)

# Animation setup
def animate(i, scatter, frames):
    scatter.set_offsets(frames[i])
    return scatter,

def main():
    # Generate motion data
    frames = generate_bowing_motion()
    
    # Setup plot
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-1, 12)
    ax.set_facecolor('black')  # Set background to black
    ax.axis('off')

    # Scatter plot for the animation
    scatter = ax.scatter([], [], s=50, color='white')  # White point-lights

    # Animation
    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=len(frames),
        fargs=(scatter, frames),
        interval=50  # Controls the speed of the animation
    )

    plt.show()

if __name__ == "__main__":
    main()
