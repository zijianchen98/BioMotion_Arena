
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_bio_motion_sequence(frame_count, frequency=1):
    """
    Simulates a biomechanical walking motion for a sadwoman as point-light animation.
    This generates the (x, y) coordinates for the 15 points over time.
    
    :param frame_count: Total number of frames for the animation.
    :param frequency: Controls the speed of the walking motion.
    :return: A list of frames where each frame contains the (x, y) positions of the 15 points.
    """
    # Define point characteristics for a walking figure (approximated).
    # Each point represents: head, shoulders, hips, knees, feet, and arms.
    initial_positions = np.array([
        [0, 10],  # Head
        [-2, 8], [2, 8],  # Left and Right Shoulders
        [-2, 6], [2, 6],  # Left and Right Hips
        [-2, 4], [2, 4],  # Left and Right Knees
        [-2, 2], [2, 2],  # Left and Right Feet
        [-4, 7], [-4, 5],  # Left Arm Joints
        [4, 7], [4, 5],  # Right Arm Joints
        [-3, 7], [3, 7]   # Left and Right Hand Points
    ])

    frames = []
    for t in range(frame_count):
        frame = initial_positions.copy()
        # Add biomechanical motion (sinusoidal patterns for limbs, mimic walking)
        # Frequency adjusts alternating limb movement speeds (walking pace).
        swing = np.sin((2 * np.pi * frequency * t / frame_count))
        
        # Legs: Knees bounce vertically
        frame[5, 1] += swing  # Left Knee
        frame[6, 1] -= swing  # Right Knee
        frame[7, 1] += swing  # Left Foot
        frame[8, 1] -= swing  # Right Foot

        # Arms: Hand positions swing horizontally
        frame[10, 0] += swing  # Left Hand 
                  
        
