#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_skeleton_data(num_frames=60):
    """
    Generate 2D coordinates for 15 point-lights to depict a simplified, stylized
    forward jump ("sad woman" pose with slight slump, then a small jump).
    This data is entirely procedural, intended to mimic a realistic jumping motion.
    """

    # Each frame will contain (15, 2) = (number_of_points, x_and_y)
    skeleton = np.zeros((num_frames, 15, 2))

    # Body model reference:
    #  0: Head
    #  1: Neck
    #  2: Right Shoulder
    #  3: Right Elbow
    #  4: Right Wrist
    #  5: Left Shoulder
    #  6: Left Elbow
    #  7: Left Wrist
    #  8: Chest (upper torso)
    #  9: Right Hip
    # 10: Right Knee
    # 11: Right Ankle
    # 12: Left Hip
    # 13: Left Knee
    # 14: Left Ankle

    # Times
    t = np.linspace(0, 1, num_frames)  # 0 to 1 for the entire sequence

    # -------------------------------------------------------------------------
    # Global / center-of-mass motion (simple ballistic arc for the jump)
    # We'll define the jump from about t=0.3 to t=0.6 in a simplified manner.
    # The subject starts slightly crouched, goes up, and lands. We'll move forward
    # in x direction from x=0 to x=1 body-length total.
    # -------------------------------------------------------------------------
    # Horizontal movement (simplified)
    x_start = 0.0
    x_end = 1.0
    # Vertical offset baseline (standing on ground near y=0)
    y_baseline = 0.0

    # We create a piecewise function for vertical:
    # - until t=0.3: subject is bending knees (slightly dropping)
    # - t in [0.3, 0.35]: pushing off
    # - t in [0.35, 0.55]: in flight with ballistic arc
    # - t in [0.55, 0.6]: landing
    # - t in [0.6, 1.0]: recovery to baseline

    def center_of_mass_x(tt):
        return x_start + (x_end - x_start) * tt

    def center_of_mass_y(tt):
        # For vertical position, define piecewise arcs
        if tt < 0.3:
            # Slight bend
            return y_baseline - 0.05 * (tt / 0.3)
        elif 0.3 <= tt < 0.35:
            # Push off up to ground + 0.3
            alpha = (tt - 0.3) / 0.05  # 0..1
            return (y_baseline - 0.05) + 0.35 * alpha
        elif 0.35 <= tt < 0.55:
            # Mid-flight (ballistic top ~ y= +0.3)
            alpha = (tt - 0.35) / 0.20  # 0..1
            # Simple parabola from 0.3 to 0.3 again
            # Let apex be around alpha=0.5 => +0.45
            # We'll treat amplitude as a small arc
            return y_baseline + 0.30 - 0.15 * (2 * alpha - 1) ** 2
        elif 0.55 <= tt < 0.6:
            # Landing from mid-air
            alpha = (tt - 0.55) / 0.05  # 0..1
            # End at baseline
            # Start from y ~ 0.30
            return (y_baseline + 0.30) * (1 - alpha)
        else:
            # Recovery, stand upright at baseline
            return y_baseline

    # -------------------------------------------------------------------------
    # Limbs and head positions relative to center-of-mass ("COM")
    # We'll define simple offsets that shift as the subject moves through the jump.
    # -------------------------------------------------------------------------
    # We define a default neutral stance (standing) offsets from COM:
    # x is horizontal, y is vertical (relative to COM).
    # Dimensions are approximate to look "human-like" in 2D.
    # Head above COM, arms slightly out, legs below, etc.

    # Neutral offsets (standing) - approximate skeleton
    neutral_offsets = np.array([
        [0.0,  0.70],  # Head
        [0.0,  0.50],  # Neck
        [0.15, 0.45],  # Right Shoulder
        [0.23, 0.25],  # Right Elbow
        [0.25, 0.05],  # Right Wrist
        [-0.15, 0.45], # Left Shoulder
        [-0.23, 0.25], # Left Elbow
        [-0.25, 0.05], # Left Wrist
        [0.0,  0.45],  # Chest (upper torso)
        [0.10, 0.0],   # Right Hip
        [0.10, -0.30], # Right Knee
        [0.10, -0.55], # Right Ankle
        [-0.10, 0.0],  # Left Hip
        [-0.10, -0.30],# Left Knee
        [-0.10, -0.55] # Left Ankle
    ])

    # We'll define some "sag" for the "sad" posture: slight slump of shoulders and head.
    # Also define how arms and legs bend more as t progresses into a squat.
    def compute_offsets(tt):
        # Start with a copy of neutral offsets
        offs = neutral_offsets.copy()

        # "Sad" slump factor:
        # The head and neck shift forward slightly more than neutral
        slump_factor = 0.12
        offs[0, 0] += slump_factor  # Head
        offs[1, 0] += slump_factor / 2.0  # Neck

        # Bending timeline:
        #   0 -> 0.3: bend knees/hips/arms for jump prep
        #   0.3 -> 0.35: arms swing, legs extend for push off
        #   0.35 -> 0.55: arms up, legs extended in flight
        #   0.55 -> 0.6: arms begin to lower, legs ready for landing
        #   0.6 -> 1.0: recovery to neutral
        # We'll define simple joint angle transitions.

        # A helper for blending 0..1 factor in specific intervals
        def blend(a, b, x, y):
            # For t in [x, y], returns normalized param in [0,1]. Else 0 or 1 outside range.
            if tt < x:
                return 0.0
            elif tt > y:
                return 1.0
            else:
                return (tt - x) / (y - x)

        # Knees bend from 0..0.3
        squat_bend = blend(0.0, 0.3, 0.0, 0.3)  # 0..1
        # Then they push off from 0.3..0.35
        push_off = blend(0.3, 0.35, 0.0, 0.35)  # 0..1
        # In flight, legs are fairly extended
        flight = blend(0.35, 0.55, 0.0, 0.55)  
        # Landing and recovery
        landing = blend(0.55, 0.6, 0.0, 0.6)
        done = blend(0.6, 1.0, 0.6, 1.0)

        # We'll define a net "bend factor" for knees based on these intervals
        # so the knees can bend up to ~0.2 m
        knee_bend = 0.2 * squat_bend * (1 - push_off)  # squat deeper
        # Extend during push off
        knee_extend = 0.2 * push_off
        # In flight, largely extended
        mid_air_extend = 0.15 * flight
        # Landing bend
        landing_bend = 0.15 * landing
        # Recovery
        recov = 0.2 * done

        # Combine them to get net knee offset
        net_knee_offset = - (knee_bend - knee_extend + mid_air_extend - landing_bend + recov)
        # Adjust right knee, left knee
        offs[10, 1] += net_knee_offset
        offs[13, 1] += net_knee_offset

        # Move ankles down/up accordingly
        # We'll keep ankles below knee about the same distance => 0.25
        # So if knee is at -0.30 + net_knee_offset, ankle is about -0.55 + some portion
        delta_knee_to_ankle = 0.25
        offs[11, 1] = offs[10, 1] - delta_knee_to_ankle
        offs[14, 1] = offs[13, 1] - delta_knee_to_ankle

        # Arms: We'll have arms swing back, then up in flight
        # Right elbow/wrist offsets
        swing_back = 0.15 * squat_bend
        swing_up = 0.20 * push_off + 0.20 * flight

        # Right elbow: originally (0.23, 0.25), shift it
        offs[3, 0] += -swing_back + swing_up
        offs[3, 1] += swing_up * 0.1
        # Right wrist
        offs[4, 0] += -swing_back * 1.2 + swing_up * 1.3
        offs[4, 1] += swing_up * 0.2

        # Left elbow/wrist do something similar
        offs[6, 0] += swing_back - swing_up
        offs[6, 1] += swing_up * 0.1
        offs[7, 0] += swing_back * 1.2 - swing_up * 1.3
        offs[7, 1] += swing_up * 0.2

        # Slight posture changes in torso/chest
        # e.g., leaning torso more forward when prepping the jump
        torso_lean = 0.08 * squat_bend - 0.12 * flight
        offs[8, 0] += torso_lean

        return offs

    # Fill skeleton matrix for each frame
    for i in range(num_frames):
        tt = t[i]
        # Center of mass
        com_x = center_of_mass_x(tt)
        com_y = center_of_mass_y(tt)
        # Offsets
        off = compute_offsets(tt)
        # Final positions
        skeleton[i, :, 0] = com_x + off[:, 0]
        skeleton[i, :, 1] = com_y + off[:, 1]

    return skeleton

def main():
    # Generate skeleton data
    num_frames = 60
    skel_data = generate_skeleton_data(num_frames=num_frames)

    # Set up the figure and the axis
    fig, ax = plt.subplots()
    fig.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(-0.5, 1.5)  # Enough space for the forward jump
    ax.set_ylim(-1.0, 1.0)  # Enough space for the jump height
    ax.set_aspect('equal')
    ax.axis('off')

    # Plot 15 white point-lights
    scatter_plot = ax.scatter([], [], color='white', s=50)

    # Initialization function for FuncAnimation
    def init():
        scatter_plot.set_offsets([])
        return (scatter_plot,)

    # Update function
    def update(frame):
        points = skel_data[frame]
        scatter_plot.set_offsets(points)
        return (scatter_plot,)

    # Create animation
    ani = FuncAnimation(
        fig, update, frames=num_frames, init_func=init, blit=True, interval=50
    )

    plt.show()

if __name__ == "__main__":
    main()