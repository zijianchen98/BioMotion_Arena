
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Define parameters of walking motion
num_frames = 100
t = np.linspace(0, 2 * np.pi, num_frames)

# Create points representing the biological motion (15 dots)
dots, = ax.plot([], [], 'wo', markersize=8)

def walk_motion(frame):
    angle = 2 * np.pi * frame / num_frames
    
    # Head
    head_x = 0
    head_y = 1.3 + 0.02 * np.sin(2 * angle)
    
    # Shoulders
    shoulder_left_x = -0.3 + 0.02 * np.sin(angle)
    shoulder_left_y = 1.0
    shoulder_right_x = 0.3 + 0.02 * np.cos(angle)
    shoulder_right_y = 1.0
   
    # Elbows
    elbow_left_x = shoulder_left_x - 0.25 * np.sin(angle)
    elbow_left_y = shoulder_left_y - 0.3
    elbow_right_x = shoulder_right_x + 0.25 * np.sin(angle)
    elbow_right_y = shoulder_right_y - 0.3
    
    # Wrists
    wrist_left_x = elbow_left_x - 0.2 * np.sin(angle)
    wrist_left_y = elbow_left_y - 0.3
    wrist_right_x = elbow_right_x + 0.2 * np.sin(angle)
    wrist_right_y = elbow_right_y - 0.3
    
    # Abdomen
    abdomen_x = 0
    abdomen_y = 0.6 + 0.02 * np.sin(2 * angle)
    
    # Hips
    hip_left_x = -0.2 + 0.02 * np.cos(angle)
    hip_left_y = 0.4
    hip_right_x = 0.2 + 0.02 * np.sin(angle)
    hip_right_y = 0.4
    
    # Knees
    knee_left_x = hip_left_x - 0.1 * np.sin(angle)
    knee_left_y = hip_left_y - 0.5 - 0.05 * np.cos(angle)
    knee_right_x = hip_right_x + 0.1 * np.sin(angle)
    knee_right_y = hip_right_y - 0.5 + 0.05 * np.cos(angle)
    
    # Feet
    foot_left_x = knee_left_x - 0.1 * np.sin(angle)
    foot_left_y = knee_left_y - 0.5 + 0.05 * np.cos(angle)
    foot_right_x = knee_right_x + 0.1 * np.sin(angle)
    foot_right_y = knee_right_y - 0.5 - 0.05 * np.cos(angle)
    
    x = [head_x,
         shoulder_left_x, shoulder_right_x,
         elbow_left_x, elbow_right_x,
         wrist_left_x, wrist_right_x,
         abdomen_x,
         hip_left_x, hip_right_x,
         knee_left_x, knee_right_x,
         foot_left_x, foot_right_x]

    y = [head_y,
         shoulder_left_y, shoulder_right_y,
         elbow_left_y, elbow_right_y,
         wrist_left_y, wrist_right_y,
         abdomen_y,
         hip_left_y, hip_right_y,
         knee_left_y, knee_right_y,
         foot_left_y, foot_right_y]

    # add one more dot in the center for the total of exactly 15 dots
    center_x = abdomen_x
    center_y = (abdomen_y + shoulder_left_y) / 2
    x.append(center_x)
    y.append(center_y)

    dots.set_data(x, y)

    return dots,

ani = FuncAnimation(fig, walk_motion, frames=num_frames, interval=50, blit=True)

plt.show()
