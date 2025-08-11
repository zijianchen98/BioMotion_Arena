
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the point-light stimulus
class PointLight:
    def __init__(self, position, color):
        self.position = np.array(position)
        self.color = np.array(color)

    def __str__(self):
        return f"PointLight(position={self.position}, color={self.color})"

# Define the subject and action
class Subject:
    def __init__(self, position, color):
        self.position = np.array(position)
        self.color = np.array(color)

    def __str__(self):
        return f"Subject(position={self.position}, color={self.color})"

class Action:
    def __init__(self, subject, direction):
        self.subject = subject
        self.direction = np.array(direction)

    def __str__(self):
        return f"Action(subject={self.subject}, direction={self.direction})"

# Define the bowing action
class BowingAction(Action):
    def __init__(self, subject, direction):
        super().__init__(subject, direction)

    def calculate_motion(self, time_step):
        # Calculate the distance from the point-light to the subject
        distance = np.linalg.norm(self.subject.position - self.direction)

        # Calculate the acceleration based on the distance
        acceleration = 0.1 * (1 - distance**2 / 100)

        # Calculate the velocity based on the acceleration and time step
        velocity = acceleration * time_step

        # Calculate the position based on the velocity and time step
        position = self.subject.position + velocity * time_step

        return position

# Define the parameters
subject_position = np.array([0, 0, 0])
subject_color = np.array([1, 1, 1])
bowing_direction = np.array([1, 0, 0])  # right

# Create a list to store the positions of the point-lights
point_lights = []

# Create the point-lights
for i in range(15):
    point_light = PointLight([i * 10, 0, 0], [1, 1, 1])  # green
    point_lights.append(point_light)

# Create the subject and action
subject = Subject(subject_position, subject_color)
action = BowingAction(subject, bowing_direction)

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Calculate the positions of the point-lights
for point_light in point_lights:
    position = action.calculate_motion(0.01)
    ax.scatter(position[0], position[1], position[2], c='w', marker='o', s=50)

# Set the limits and aspect ratio of the axis
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_aspect('equal')

# Show the plot
plt.show()
