
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (standing position)
points_data = {
    'head': [0, 4],
    'shoulder_l': [-1, 3],
    'shoulder_r': [1, 3],
    'elbow_l': [-2, 2],
    'elbow_r': [2, 2],
    'wrist_l': [-3, 1],
    'wrist_r': [3, 1],
    'hip_l': [-0.5, 1],
    'hip_r': [0.5, 1],
    'knee_l': [-0.5, -1],
    'knee_r': [0.5, -1],
    'ankle_l': [-1, -3],
    'ankle_r': [1, -3],
    'foot_l': [-1.5, -3.5],
    'foot_r': [1.5, -3.5],
}

points_coords = np.array(list(points_data.values()))

# Define the animation function
def update_points(num, points, scatter):
    # Simulate lying down motion
    x_offset = 0
    y_offset = -num * 0.05 # Gradual move down
    rotation = np.radians(num * 0.2) # Gradual rotation
    
    # Translation matrix
    translation_matrix = np.array([[1, 0, x_offset], [0, 1, y_offset], [0, 0, 1]])
    
    # Rotation matrix
    rotation_matrix = np.array([[np.cos(rotation), -np.sin(rotation), 0], [np.sin(rotation), np.cos(rotation), 0], [0, 0, 1]])
    
    new_coords = points_coords.copy()
    
    # Apply rotation and translation
    for i in range(len(new_coords)):
        point = np.array([new_coords[i][0], new_coords[i][1], 1])
        rotated_point = np.dot(rotation_matrix, point)
        translated_point = np.dot(translation_matrix, rotated_point)
        new_coords[i][0] = translated_point[0]
        new_coords[i][1] = translated_point[1]
        
    # Modify positions to show arm movement (simplified)
    new_coords[3][0] = new_coords[3][0] - np.sin(num * 0.1) * 0.3  # elbow_l
    new_coords[4][0] = new_coords[4][0] + np.sin(num * 0.1) * 0.3  # elbow_r
    new_coords[5][0] = new_coords[5][0] - np.sin(num * 0.1) * 0.5  # wrist_l
    new_coords[6][0] = new_coords[6][0] + np.sin(num * 0.1) * 0.5  # wrist_r
    
    scatter.set_offsets(new_coords)
    return scatter,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # background black
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off') # remove axis

# Create the scatter plot
scatter = ax.scatter(points_coords[:, 0], points_coords[:, 1], color='white', s=20) # s = size

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points_coords, scatter), blit=False, repeat=True, frames=100)

plt.show()
