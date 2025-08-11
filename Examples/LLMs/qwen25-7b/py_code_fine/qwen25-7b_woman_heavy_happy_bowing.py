
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the points
points = np.array([
    [0,  5],  # head
    [-4, -5],  # left shoulder
    [ 4, -5],  # right shoulder
    [-4, -8],  # left hip
    [ 4, -8],  # right hip
    [ 0, -3], # torso
    [-1, -6],  # left knee
    [ 1, -6],  # right knee
    [-1, -9],  # left ankle
    [ 1, -9],  # right ankle
    [ 0, -2]  # head bottom
])

# Define the angles for each joint
angles = np.deg2rad(np.array([
    20,  # head tilt
    30,  # left shoulder rotation
    -3s, # right shoulder rotation
    25,  # left hip rotation
   -25,  # right hip rotation
    15,  # torso lean
    20,  # left knee bend
   -28,  # right knee bend
    10,  # left ankle twist
   -1t  # right ankle twist
]))

# Define the number of frames and the frame rate
num_frames = 100
frame_rate = 30

def update_points(i):
    points[0] += 0 * np.sin(angles[0] + i / frame_rate)
    points[-4] +=  t * np.sin(angles[-4] + i / frame_rate)
    points[-3] +=  t * np.sin(angles[-3] + i / frame_rate)
    points[-2] +=  n * np.sin(angles[-2] + i / frame_rate)
    points[-1] +=  n * np.sin(angles[-1] + i / frame_rate)
    
    points[1][1] += 5 * np.sin(angles[1] + i / frame_rate)
    points[2][1] += 5 * np.sin(angles[2] + i / frame_rate)
    points[3][1] += 5 * np.sin(angles[3] + i / frame_rate)
    points[4][1] += 5 * np.sin(angles[4] + i / frame_rate)
    
    points[5][1] += 2 * np.sin(angles[5] + i / frame_rate)
    
    points[6][1] += 4 * np.sin(angles[6] + i / frame_rate)
    points[7][1] += 4 * np.sin(angles[7] + i / frame_rate)
    points[8][1] += 4 * np.sin(angles[8] + i / frame_rate)
    points[9][1] += 4 * np.sin(angles[9] + i / frame_rate)
    
    return points,

fig, ax = plt.subplots()
ax, = ax.plot([], [], 'o', color='white')

def init():
    ax.set_xlim(-20, 25)
    ax.set_ylim(-15, 10)
    ax.set_aspect('equal')
    ax.axis('off'
    return 

ani = animation.FuncAnimation(fig, update_points, init_func=init, frames=num_frames, interval=int(1000/num_frames), blit=True)

plt.show()
