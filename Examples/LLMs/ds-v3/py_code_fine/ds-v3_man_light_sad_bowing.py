
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of points and frames
num_points = 15
num_frames = 100

# Define the points for the stick figure (head, shoulders, elbows, hands, hips, knees, feet)
points = np.zeros((num_frames, num_points, 2))

# Generate the motion: a person bowing
for t in range(num_frames):
    # Time parameter (0 to 2pi)
    theta = 2 * np.pi * t / num_frames
    
    # Head (stationary)
    points[t, 0, :] = [0, 1.2]
    
    # Shoulders (slightly moving forward when bowing)
    shoulder_y = 0.9
    shoulder_forward = 0.2 * np.sin(theta - np.pi/2)  # Forward motion
    points[t, 1, :] = [-0.4, shoulder_y + 0.05 * shoulder_forward]  # Left shoulder
    points[t, 2, :] = [0.4, shoulder_y + 0.05 * shoulder_forward]   # Right shoulder
    
    # Elbows (move backward when bowing)
    elbow_angle = 0.3 * np.sin(theta - np.pi/2)
    points[t, 3, :] = [-0.5, 0.7 + 0.1 * np.sin(theta)]  # Left elbow
    points[t, 4, :] = [0.5, 0.7 + 0.1 * np.sin(theta)]   # Right elbow
    
    # Hands (follow elbows with some lag)
    points[t, 5, :] = [-0.6, 0.5 + 0.1 * np.sin(theta + 0.2)]  # Left hand
    points[t, 6, :] = [0.6, 0.5 + 0.1 * np.sin(theta + 0.2)]   # Right hand
    
    # Hips (stationary)
    hip_y = 0.5
    points[t, 7, :] = [-0.3, hip_y]  # Left hip
    points[t, 8, :] = [0.3, hip_y]   # Right hip
    
    # Knees (bend slightly when bowing)
    knee_bend = 0.2 * np.sin(theta - np.pi/2)
    points[t, 9, :] = [-0.3, 0.2 + knee_bend]   # Left knee
    points[t, 10, :] = [0.3, 0.2 + knee_bend]   # Right knee
    
    # Feet (stationary)
    points[t, 11, :] = [-0.3, 0.0]   # Left foot
    points[t, 12, :] = [0.3, 0.0]    # Right foot
    
    # Additional points for smoother motion (e.g., spine, mid-limbs)
    # Spine (midpoint between shoulders and hips)
    points[t, 13, :] = [0, 0.7 + 0.05 * shoulder_forward]
    # Mid-arm points (for smoother arm motion)
    points[t, 14, :] = [0, 0.3 + 0.05 * np.sin(theta)]

# Create a scatter plot for the points
scat = ax.scatter([], [], color='white', s=50)

# Create line segments for the stick figure (optional, for better visualization)
lines = LineCollection([], colors='white', linewidths=1)
ax.add_collection(lines)

def update(frame):
    # Update the scatter plot
    scat.set_offsets(points[frame])
    
    # Update the lines (optional)
    segments = [
        [points[frame, 0], points[frame, 13]],  # Head to spine
        [points[frame, 13], points[frame, 1]],  # Spine to left shoulder
        [points[frame, 13], points[frame, 2]],  # Spine to right shoulder
        [points[frame, 1], points[frame, 3]],   # Left shoulder to left elbow
        [points[frame, 3], points[frame, 5]],   # Left elbow to left hand
        [points[frame, 2], points[frame, 4]],   # Right shoulder to right elbow
        [points[frame, 4], points[frame, 6]],   # Right elbow to right hand
        [points[frame, 13], points[frame, 7]],  # Spine to left hip
        [points[frame, 13], points[frame, 8]],  # Spine to right hip
        [points[frame, 7], points[frame, 9]],   # Left hip to left knee
        [points[frame, 9], points[frame, 11]],  # Left knee to left foot
        [points[frame, 8], points[frame, 10]], # Right hip to right knee
        [points[frame, 10], points[frame, 12]]  # Right knee to right foot
    ]
    lines.set_segments(segments)
    return scat, lines

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
