
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the frame rate and animation timing
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Initial positions for the joints (in black dots)
joints = {
    'top': [0.0, 0.0],
   'shoulder': [0.0, 0.1],
    'elbow': [0.0, 0.25],
    'hand': [0.04, 0.4],
    'head': [0.05, 0.05],
    'hip': [-0.07, 0.3],
    'knee': [-0.1, 0.35],
    'ankle': [-0.15, 0.36],
    'foot': [-0.02, 0.4]
}

# Convert joints to start positions
points = list(joints.values())
point_set = np.array(points)

# Array to store points for the legs and arms
points_list = [
    point_set[-3],  # Right foot
    point_set[-2],  # Right ankle
    point_set[-1],  # Right knee
    point_set[-4],  # Left foot
    point_set[-5],  # Left ankle
    point_set[-6],  # Left knee
    point_set[-7],  # Right hand
    point_set[-8],  # Right elbow
    point_set[-9]   # Right shoulder
]

# Function to animate points with given velocity and acceleration
def animate(dot, velocity=None, acceleration=None):
    if velocity is not None:
        dot[0] += velocity[0]
    if acceleration is not None:
        dot[0] += acceleration[0]

# Main animation function
def run():
    # Total number of point lights
    num_points = 15
    # Create an empty list to store all points
    dot_list = [[j for j in joints.values()] + [joints['shoulder']] + [
        joints['head']
    ]]

    # Create animation figure
    def init():
        ax.set_aspect('equal')
        return ax

    def update(frame):
        # Create a list to store all moving points.
        points = []

        # Move the points
        dot = np.array(dot_list[0])
        for i in range(len(dot_list)):
            points.append(plt.scatter(dot_list[i][0], dot_list[i][1], color='white'))
            dot_list[i][0] +=.01
            dot_list[i][1] +=.01

        if motion['type'] in ['Running', 'Standing']:
            dots = []
            for point in points:
                dots.append(point)

            # Update motion for each point
            # This part needs to define more complex motion and acceleration
            # Here we use very simple velocity, adjusting in loops
            velocity = {
                'foot': (0.1, -0.1),
                'ankle': (0.6, 0.1),
                'knee': (0.1, 0.05),
                'hand': (0.2, -0.2),
                'elbow': (0.05, 0.1),
               'shoulder': (0.04, 0.0),
                'head': (0.03, -0.02)
            }

            # Apply velocity and acceleration
            for idx, part in enumerate(dots):
                acc = {
                    'foot': (0.0, 0.05),
                    'ankle': (0.0, -0.01),
                    'knee': (-0.03, 0.0),
                    'hand': (0.0, 0.03),
                    'elbow': (0.0, -0.01),
                   'shoulder': (0.0, 0.01),
                    'head': (-0.02, 0.0)
                }
                velocity_idx = idx // 3
                points_list[velocity_idx][1] += 0.01  # Increase position of joint to maintain upright
                dot = np.array(dot_list[velocity_idx])
                if idx >= 3 and idx < 6:
                    animate(dot, velocity[velocity_idx], acc[velocity_idx])
                    points_list[velocity_idx][1] += dot[1]

            ax = plt.gca()
            ax.cla()
            for point in points:
                point.remove()
            for point in dots:
                point.set_position(np.array(point.get_position()))
                ax.add_artist(point)

        return [dot for dot in points]

    frame_times = 200
    animation = animation.FuncAnimation(
        fig, update, frames=frame_times, init_func=init, interval=50, blit=True)

    plt.show()

# Define the motion type, e.g., Running or Standing
motion = {'type': 'Running'}
run()
