
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Generate random positions for the points
points = np.random.rand(num_points, 2)

# Set the background color to black
plt.figure(figsize=(6, 6))
plt.gca().set_axis_off()
plt.scatter(points[:, 0], points[:, 1], s=100, c='white')

# Display the plot
plt.show()
