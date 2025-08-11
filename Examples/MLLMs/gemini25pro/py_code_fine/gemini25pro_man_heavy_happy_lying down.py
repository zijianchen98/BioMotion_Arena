
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_animation_data():
    """
    Generates the full sequence of coordinates for the 15 points over time.
    It defines keyframes for the "lying down" motion and interpolates between them.
    """
    # Joint map (15 points):
    # 0: Head, 1: Neck, 2: L_Shoulder, 3: R_Shoulder, 4: L_Elbow, 5: R_Elbow,
    # 6: L_Wrist, 7: R_Wrist, 8: Pelvis, 9: L_Hip, 10: R_Hip, 11: L_Knee,
    # 12: R_Knee, 13: L_Ankle, 14: R_Ankle

    keyframes = [
        # Keyframe 0: Standing hunched, as if holding a heavy weight. Knees are bent.
        [
            (1, 38), (1, 28), (-7, 25), (9, 25), (-5, 15), (7, 15),
            (-2, 8), (4, 8), (0, 0), (-5, 0), (5, 0), (-6, -20),
            (6, -20), (-7, -40), (7, -40)
        ],
        # Keyframe 1: Deep crouch, lowering the "weight". Torso leans forward.
        [
            (0, 15), (0, 5), (-10, 2), (5, 2), (-8, -8), (7, -8),
            (-5, -25), (2, -25), (-10, -25), (-15, -25), (-5, -25),
            (-12, -35), (8, -35), (-7, -40), (7, -40)
        ],
        # Keyframe 2: Hips land on the ground. Hands are released and start moving back for support.
        [
            (-15, 0), (-18, -10), (-25, -12), (-15, -12), (-20, -20),
            (-10, -20), (-25, -30), (-5, -30), (-20, -38), (-25, -38),
            (-15, -38), (-5, -30), (10, -30), (5, -40), (20, -40)
        ],
        # Keyframe 3: Leaning back, supported by elbows on the ground.
        [
            (-28, -5), (-25, -15), (-30, -18), (-20, -18), (-35, -40),
            (-15, -40), (-38, -30), (-12, -30), (-20, -38), (-24, -38),
            (-15, -38), (0, -25), (15, -25), (10, -40), (25, -40)
        ],
        # Keyframe 4: Fully lying down. Back, shoulders, and head are on the ground.
        [
            (-45, -35), (-38, -35), (-35, -34), (-25, -34), (-40, -38),
            (-20, -38), (-45, -40), (-15, -40), (-25, -38), (-29, -38),
            (-20, -38), (0, -38), (15, -38), (20, -40), (35, -40)
        ]
    ]
    # Add a final keyframe to hold the last pose for a moment.
    keyframes.append(keyframes[-1])

    # Durations define the number of frames for each transition between keyframes.
    durations = [40, 50, 40, 40, 30]

    all_frames_data = []
    for i in range(len(keyframes) - 1):
        start_pose = np.array(keyframes[i])
        end_pose = np.array(keyframes[i+1])
        num_frames = durations[i]
        
        # We need to generate num_frames points, so we use num_frames in linspace.
        # To avoid duplicating endpoints, we iterate range(num_frames).
        for frame_num in range(num_frames):
            # Use cubic easing for smoother start and end of movements
            t = frame_num / (num_frames -1) if num_frames > 1 else 1.0
            t_eased = t * t * (3.0 - 2.0 * t)
            current_pose = start_pose * (1 - t_eased) + end_pose * t_eased
            all_frames_data.append(current_pose)
            
    return np.array(all_frames_data)

# Generate all the frame data for the animation
animation_data = generate_animation_data()

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Remove axes, ticks, and spines for a clean look
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Calculate the plot limits from the data to ensure the whole animation is visible
margin = 10
x_min = animation_data[:, :, 0].min() - margin
x_max = animation_data[:, :, 0].max() + margin
y_min = animation_data[:, :, 1].min() - margin
y_max = animation_data[:, :, 1].max() + margin
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Create the scatter plot object that will be updated each frame
scatter = ax.scatter([], [], c='white', s=70)

def init():
    """Initializes the animation."""
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

def update(frame):
    """Updates the animation for each frame."""
    # Get the coordinates for the current frame
    data = animation_data[frame]
    # Update the positions of the points
    scatter.set_offsets(data)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(animation_data),
    init_func=init,
    blit=True,
    interval=33  # Corresponds to ~30 FPS
)

# Show the plot
plt.show()
