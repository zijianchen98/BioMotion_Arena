
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the action: a happy woman with heavy weight doing a forward roll
# We'll simulate the motion of 15 points representing joints or markers on the body

# Define key points on the body (simplified for animation)
# These are approximate positions of joints or markers on a human body
# We will simulate a forward roll motion

# Define a function to generate a realistic forward roll motion
def generate_forward_roll_motion(num_points=15, duration=5, sampling_rate=30):
    t = np.linspace(0, duration, duration * sampling_rate)
    positions = []

    # Define body points (approximate joint positions)
    body_points = {
        'head': np.array([0, 0]),
        'neck': np.array([0, 0.2]),
        'shoulder_left': np.array([-0.3, 0.3]),
        'shoulder_right': np.array([0.3, 0.3]),
        'elbow_left': np.array([-0.5, 0.1]),
        'elbow_right': np.array([0.5, 0.1]),
        'hip_left': np.array([-0.3, -0.3]),
        'hip_right': np.array([0.3, -0.3]),
        'knee_left': np.array([-0.5, -0.5]),
        'knee_right': np.array([0.5, -0.5]),
        'ankle_left': np.array([-0.6, -0.7]),
        'ankle_right': np.array([0.6, -0.7]),
        'spine': np.array([0, -0.1]),
        'pelvis': np.array([0, -0.2]),
        'shoulder_center': np.array([0, 0.4]),
    }

    # Define a function to simulate forward roll motion
    def forward_roll(t):
        # Simulate rotation around the spine
        angle = (np.sin(t * 2 * np.pi / 2) * 0.5)  # Sine wave for rolling motion
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
        # Apply rotation to body points
        rotated_points = {}
        for point, pos in body_points.items():
            rotated = rotation_matrix @ pos
            rotated_points[point] = rotated
        return rotated_points

    # Generate positions for each time step
    for time in t:
        positions.append(forward_roll(time))

    # Convert to numpy array
    positions = np.array(positions)

    # Select 15 points for the animation (choose a subset)
    selected_points = ['head', 'neck', 'shoulder_left', 'elbow_left', 'hip_left', 'knee_left', 'ankle_left',
                       'shoulder_right', 'elbow_right', 'hip_right', 'knee_right', 'ankle_right', 'spine',
                       'pelvis', 'shoulder_center']

    # Extract the positions of the selected points
    selected_positions = []
    for i in range(len(positions)):
        selected = np.array([positions[i][point] for point in selected_points])
        selected_positions.append(selected)

    return selected_positions

# Generate the motion data
motion_data = generate_forward_roll_motion()

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create a list of circles for the point lights
points = [Circle((0, 0), 0.03, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(i):
    for j, point in enumerate(points):
        x, y = motion_data[i][j]
        point.set_center((x, y))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(motion_data), interval=1000 / 30, blit=False)

# Show the animation
plt.show()
