
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 4)
ax.set_facecolor('black')
plt.axis('off')

# Define initial point-light locations (upright standing)
points = np.array([
    [0, 3.5],          # head
    [-0.4, 3.1], [0, 3.1], [0.4, 3.1],    # shoulders
    [-0.6, 2.7], [-0.2, 2.7], [0.2, 2.7], [0.6, 2.7],  # hips and mid-body
    [-0.6, 2.0], [-0.2, 2.0], [0.2, 2.0], [0.6, 2.0],  # lower hips/knees
    [-0.4, 1.3], [0.4, 1.3],             # ankles
    [-0.2, 0.7], [0.2, 0.7]              # feet
])

scat = ax.scatter(points[:,0], points[:,1], c='white', s=80)

# Define animation frames for sitting down motion
def animate(i):
    t = min(i / 100, 1)
    new_points = points.copy()
    
    # sitting down vertical motion (lower body and center of mass down)
    displacement = np.array([0, -1.2 * (t**2)])
    hip_disp = np.array([0, -1.2 * (t**1.8)])
    knee_disp = np.array([0, -0.8 * (t**1.5)])
    foot_disp = np.zeros((2,))
    
    # head slightly forward and downward 
    new_points[0] += displacement * 0.5  
    
    # shoulders move slightly forward and downward
    new_points[1:4] += displacement * 0.6  
    
    # mid-body forward and downward
    new_points[4:8] += displacement * 0.8  
    
    # hips and knees downward, hips more downward
    new_points[8:12] += hip_disp  
    
    # ankles move slightly back and small upward (to represent knees flexing)
    new_points[12:14] += knee_disp + np.array([-0.2*t, 0])  
    
    # feet stationary or slight backward
    new_points[14:] += foot_disp + np.array([-0.1*t, 0])  
    
    scat.set_offsets(new_points)

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, repeat=False)

plt.show()
