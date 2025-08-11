
import numpy as np
import cv2

# Define the parameters for the animation
num_points = 15
point_radius = 5
fps = 30
duration = 10  # seconds

# Define the points for the happy woman with heavy weight rolling forward
points = np.array([
    [100, 100],  # Head
    [150, 120],  # Left shoulder
    [200, 150],  # Left elbow
    [250, 180],  # Left wrist
    [300, 200],  # Left hand
    [350, 220],  # Right hand
    [400, 200],  # Right wrist
    [450, 180],  # Right elbow
    [500, 150],  # Right shoulder
    [550, 120],  # Right hip
    [600, 100],  # Right knee
    [650, 80],   # Right ankle
    [700, 100],  # Left ankle
    [750, 80],   # Left knee
    [800, 120],  # Left hip
])

# Define the motion for each point
motion = np.array([
    [0, 0],  # Head
    [10, 0],  # Left shoulder
    [20, 0],  # Left elbow
    [30, 0],  # Left wrist
    [40, 0],  # Left hand
    [-40, 0],  # Right hand
    [-30, 0],  # Right wrist
    [-20, 0],  # Right elbow
    [-10, 0],  # Right shoulder
    [0, 0],  # Right hip
    [10, 0],  # Right knee
    [10, 0],  # Right ankle
    [-10, 0],  # Left ankle
    [-10, 0],  # Left knee
    [0, 0],  # Left hip
])

# Define the rotation and scaling for each point
rotation = np.array([
    [0, 0],  # Head
    [0, 0],  # Left shoulder
    [0, 0],  # Left elbow
    [0, 0],  # Left wrist
    [0, 0],  # Left hand
    [0, 0],  # Right hand
    [0, 0],  # Right wrist
    [0, 0],  # Right elbow
    [0, 0],  # Right shoulder
    [0, 0],  # Right hip
    [0, 0],  # Right knee
    [0, 0],  # Right ankle
    [0, 0],  # Left ankle
    [0, 0],  # Left knee
    [0, 0],  # Left hip
])

scaling = np.array([
    [1, 1],  # Head
    [1, 1],  # Left shoulder
    [1, 1],  # Left elbow
    [1, 1],  # Left wrist
    [1, 1],  # Left hand
    [1, 1],  # Right hand
    [1, 1],  # Right wrist
    [1, 1],  # Right elbow
    [1, 1],  # Right shoulder
    [1, 1],  # Right hip
    [1, 1],  # Right knee
    [1, 1],  # Right ankle
    [1, 1],  # Left ankle
    [1, 1],  # Left knee
    [1, 1],  # Left hip
])

# Create a window to display the animation
cv2.namedWindow('Animation', cv2.WINDOW_NORMAL)

# Create a black background
background = np.zeros((600, 800, 3), dtype=np.uint8)

# Main loop for the animation
for frame in range(int(fps * duration)):
    # Clear the background
    cv2.rectangle(background, (0, 0), (800, 600), (0, 0, 0), -1)

    # Draw the points
    for i in range(num_points):
        point = points[i] + motion[i]
        point = (int(point[0]), int(point[1]))
        cv2.circle(background, point, point_radius, (255, 255, 255), -1)

    # Display the frame
    cv2.imshow('Animation', background)

    # Wait for a short period
    cv2.waitKey(1000 // fps)

# Close the window
cv2.destroyAllWindows()
