
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = ax.scatter([], [], color='white', s=50)

# Define the key points for a forward rolling motion (simplified)
def get_key_points(t):
    # This is a simplified model; in a real scenario, you'd use more accurate biomechanical data
    # Parameters for a forward rolling motion (approximation)
    body_radius = 1.0
    roll_speed = 0.1
    angle = t * roll_speed
    
    # Head, shoulders, elbows, hands, hips, knees, feet
    angles = np.linspace(0, 2*np.pi, num_points, endpoint=False)
    x = body_radius * np.cos(angles + angle)
    y = body_radius * np.sin(angles + angle)
    
    # Adjust y-coordinate to simulate rolling (flattening the bottom)
    y = np.where(y < -0.5, -0.5 + 0.3 * (y + 0.5), y)
    
    # Add some variation to simulate limbs moving
    limb_phase = np.sin(t * 2) * 0.2
    x[3] += limb_phase  # right hand
    x[6] -= limb_phase  # left hand
    y[9] += limb_phase * 0.5  # right foot
    y[12] -= limb_phase * 0.5  # left foot
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_key_points(frame)
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 20, 200), 
                              interval=50, blit=True)

plt.tight_layout()
plt.show()
