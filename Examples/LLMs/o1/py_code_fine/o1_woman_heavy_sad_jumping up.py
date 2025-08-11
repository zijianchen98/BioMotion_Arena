#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_biological_motion_frames(num_frames=60):
    """
    Generate a list of frames for a 2D point-light display (15 points) simulating
    a 'sad woman with heavy weight' performing a jump.

    Each frame is a numpy array of shape (15, 2) representing the (x, y) coordinates
    of the 15 point-lights. The frame sequence attempts to depict a slightly stooped,
    heavy posture transitioning into a jump and landing.
    """
    # Define 15 distinct points corresponding to typical body markers:
    #  0: Head
    #  1: Neck
    #  2: Right Shoulder
    #  3: Right Elbow
    #  4: Right Wrist
    #  5: Left Shoulder
    #  6: Left Elbow
    #  7: Left Wrist
    #  8: Torso (center)
    #  9: Right Hip
    # 10: Right Knee
    # 11: Right Ankle
    # 12: Left Hip
    # 13: Left Knee
    # 14: Left Ankle
    #
    # For a "sad" posture, the shoulders and head will be tilted forward.
    # For a "heavy" feel, the movement is somewhat slow and with limited jump height.

    frames = []

    # We'll define a simple motion timeline:
    #  - 0% to ~20%: slight crouch (preparing to jump)
    #  - ~20% to ~40%: upward motion (jump takeoff)
    #  - ~40% to ~60%: peak and descending
    #  - ~60% to ~80%: landing
    #  - ~80% to 100%: return to some stance

    for i in range(num_frames):
        t = i / (num_frames - 1)  # normalize time 0 to 1

        # Start with baseline stance (x ~ 0 for center, y ~ 0 to -some_value)
        # We'll offset y for each joint. We'll incorporate changes over time for the jump.

        # Base positions for a somewhat stooped stance:
        # These are rough approximations, just to create a plausible posture.
        base_positions = np.array([
            [ 0.0,  2.0],  # Head
            [ 0.0,  1.6],  # Neck
            [ 0.4,  1.6],  # Right Shoulder
            [ 0.6,  1.2],  # Right Elbow
            [ 0.7,  0.8],  # Right Wrist
            [-0.4,  1.6],  # Left Shoulder
            [-0.6,  1.2],  # Left Elbow
            [-0.7,  0.8],  # Left Wrist
            [ 0.0,  1.0],  # Torso Center
            [ 0.2,  0.8],  # Right Hip
            [ 0.2,  0.4],  # Right Knee
            [ 0.2,  0.0],  # Right Ankle
            [-0.2,  0.8],  # Left Hip
            [-0.2,  0.4],  # Left Knee
            [-0.2,  0.0],  # Left Ankle
        ])

        # The woman is "sad and heavy": we tilt the head/shoulders slightly forward
        # and keep the stance a bit wide. We'll add a mild forward shift to the top joints.
        forward_tilt = 0.1
        base_positions[:5, 0] += forward_tilt  # tilt head to right
        base_positions[5:8, 0] -= forward_tilt  # tilt left side in opposite direction

        # Let's define a jump amplitude curve. We'll keep it small (she's "heavy"), so amplitude is small.
        # We can define phases:
        #   - crouch: slight downward
        #   - jump up: moderate upward
        #   - land: come back down
        # We'll define a piecewise function to shape the jump.

        if t < 0.2:
            # Crouch (positions go slightly lower)
            factor = t / 0.2
            y_offset = -0.3 * factor  # crouch down a bit
        elif t < 0.4:
            # Jump up from crouch
            factor = (t - 0.2) / 0.2
            y_offset = -0.3 + 1.0 * factor  # move from -0.3 to +0.7
        elif t < 0.6:
            # Descend from jump
            factor = (t - 0.4) / 0.2
            y_offset = 0.7 - 0.7 * factor  # move from +0.7 to 0
        elif t < 0.8:
            # Land: overshoot slightly negative, then come back
            factor = (t - 0.6) / 0.2
            y_offset = 0.0 - 0.2 * factor  # move from 0 to -0.2
        else:
            # Return: stand up again
            factor = (t - 0.8) / 0.2
            y_offset = -0.2 + 0.2 * factor  # move from -0.2 back to 0

        # Apply the offset to y
        current_frame = base_positions.copy()
        current_frame[:, 1] += y_offset

        # Store in frames
        frames.append(current_frame)

    return frames


def main():
    # Generate frames for the animation
    frames = generate_biological_motion_frames(num_frames=60)

    fig, ax = plt.subplots()
    fig.set_facecolor("black")
    ax.set_facecolor("black")

    # Set up the scatter plot (15 points). We'll use white color for the lights.
    scatter = ax.scatter([], [], c="white", s=50)

    # To keep the figure stable, fix the axis limits around what we expect.
    ax.set_xlim(-1.5, 2.0)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")

    def init():
        scatter.set_offsets([])
        return (scatter,)

    def update(frame_index):
        # Update the scatter plot with the new frame
        data = frames[frame_index]
        scatter.set_offsets(data)
        return (scatter,)

    # Create an animation
    ani = animation.FuncAnimation(
        fig, update, frames=len(frames), init_func=init, interval=100, blit=True
    )

    # Show the animation
    plt.show()


if __name__ == "__main__":
    main()