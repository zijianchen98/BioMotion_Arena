
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point light source
class PointLight:
    def __init__(self, x, y, z, intensity=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity

    def get_direction(self):
        return np.array([0, 0, 1])

    def get_direction_vector(self):
        return np.array([self.x - self.z, self.y - self.z, self.z - self.x])

# Define the camera
class Camera:
    def __init__(self, x, y, z, focal_length=10.0):
        self.x = x
        self.y = y
        self.z = z
        self.focal_length = focal_length

    def get_direction(self):
        return np.array([0, 0, 1])

    def get_direction_vector(self):
        return np.array([self.x - self.z, self.y - self.z, self.z - self.x])

# Define the subject
class Subject:
    def __init__(self):
        self.position = np.array([0, 0, 0])
        self.direction = np.array([0, 0, 1])
        self.weight = 1.0

    def move(self, x, y, z):
        self.position = np.array([x, y, z])
        self.direction = np.array([0, 0, 1])

# Define the action
class Action:
    def __init__(self):
        self.subject = Subject()
        self.weight = 1.0
        self.direction = np.array([0, 0, 1])

    def move(self, x, y, z):
        self.subject.weight += 0.1
        self.subject.direction = np.array([0, 0, 1])

# Create the point lights
point_lights = [PointLight(0, 0, 0, intensity=1.0) for _ in range(15)]

# Create the camera
camera = Camera(5, 5, 5, focal_length=10.0)

# Create the subject and action
subject = Subject()
action = Action()

# Initialize the plot
fig, ax = plt.subplots()

# Function to update the plot
def update(frame):
    global point_lights, camera, subject, action
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    # Move the point lights
    for light in point_lights:
        light.x += np.random.uniform(-0.01, 0.01)
        light.y += np.random.uniform(-0.01, 0.01)
        light.z += np.random.uniform(-0.01, 0.01)
        light.intensity = np.clip(light.intensity, 0, 10)

    # Move the subject and action
    subject.position += np.random.uniform(-0.01, 0.01, size=3)
    subject.direction = np.random.uniform(-0.01, 0.01, size=3)
    action.subject.weight += np.random.uniform(-0.01, 0.01)
    action.subject.direction = np.random.uniform(-0.01, 0.01)

    # Move the camera
    camera.x += np.random.uniform(-0.01, 0.01)
    camera.y += np.random.uniform(-0.01, 0.01)
    camera.z += np.random.uniform(-0.01, 0.01)

    # Plot the point lights
    for light in point_lights:
        ax.scatter(light.x, light.y, light.z, c=light.intensity, s=0.1, alpha=0.5)

    # Plot the subject and action
    ax.scatter(subject.position[0], subject.position[1], subject.position[2], c=subject.weight, s=0.1, alpha=0.5)
    ax.quiver(subject.position[0], subject.position[1], subject.position[2], subject.direction[0], subject.direction[1], subject.direction[2], color='red', alpha=0.5)

    # Plot the camera
    ax.quiver(camera.x, camera.y, camera.z, camera.direction[0], camera.direction[1], camera.direction[2], color='green', alpha=0.5)

    # Update the plot
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    plt.draw()
    plt.pause(0.01)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
