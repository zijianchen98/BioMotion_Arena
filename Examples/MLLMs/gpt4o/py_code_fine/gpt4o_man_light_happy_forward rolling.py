
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_forward_rolling_motion(frame_num, num_points=15):
    """
    Generate the coordinates for a forward rolling motion of a humanoid.
    Parameters:
        frame_num (int): The current frame number in the animation.
        num_points (int): Number of points (lights) in the motion.
    Returns:
        np.array: An array of (x, y) coordinates for the points.
    """
    # Define circular rolling motion parameters
    radius = 0.5
    angular_speed = 0.2  # radians per frame
    phase_offset = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    
    # Center of the rolling motion (moving forward)
    roll_center_x = frame_num * 0.05  # Forward motion per frame
    roll_center_y = 0.3  # Fixed height for rolling
    
    # Calculate positions dynamically for the current frame
    angles = angular_speed * frame_num + phase_offset
    x_coords = roll_center_x + radius * np.cos(angles)
    y_coords = roll_center_y + radius * np.sin(angles)
    
    return np.column_stack((x_coords, y_coords))

# Set up the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize points
num_points = 15
point_lights, = ax.plot([], [], 'wo', ms=4)  # 'wo' means white dots

def init_scene():
    point_lights.set_data([], [])
    return point_lights,

def animate(frame):
    points = generate_forward_rolling_motion(frame, num_points)
    point_lights.set_data(points[:, 0], points[:, 1])
    return point_lights,

ani = animation.FuncAnimation(
    fig, animate, init_func=init_scene, frames=200, interval=50, blit=True
)

plt.show()
