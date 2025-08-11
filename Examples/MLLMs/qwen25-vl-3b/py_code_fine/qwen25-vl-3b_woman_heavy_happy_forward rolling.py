
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Generate random positions for the points
points = np.random.rand(num_points, 2)

# Define the forward rolling action
def forward_roll(points):
    # Rotate the points around their center
    rotation_matrix = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                                [np.sin(np.pi/4), np.cos(np.pi/4)]])
    rotated_points = np.dot(points, rotation_matrix)
    
    # Translate the points to simulate forward rolling
    translation_vector = np.array([0.1, 0.1])  # Adjust these values for better visual effect
    translated_points = rotated_points + translation_vector
    
    return translated_points

# Apply the forward roll action
points = forward_roll(points)

# Plot the points
plt.figure(figsize=(6, 6))
for point in points:
    plt.plot(point[0], point[1], 'o', markersize=5, color='white')
plt.axis('equal')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
