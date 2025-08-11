
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1.0, 1.0, 1.0)
BLACK_COLOR = (0.0, 0.0, 0.0)

# Define the subject and action
SUBJECT = {'x': 0.0, 'y': 0.0, 'z': 0.0}
ACTION = {'x': 0.0, 'y': 0.0, 'z': 0.0}

# Define the point-light source parameters
POINT_LIGHT_SIZE = 0.1
POINT_LIGHT_COLOR = WHITE_COLOR

# Function to create a 3D plot
def create_3d_plot(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a 3D line plot
    ax.plot3D(x, y, z, 'b-')

    # Set axis limits
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_zlim(-HEIGHT / 2, HEIGHT / 2)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set axis title
    ax.set_title(f'Subject: {SUBJECT["x"]}, Action: {ACTION["x"]}')

    plt.show()

# Main function
def main():
    # Create a 3D plot
    create_3d_plot(SUBJECT['x'], SUBJECT['y'], SUBJECT['z'])

    # Define the point-light source positions
    LIGHTS = 15
    LIGHTS_PER_ROW = 3
    LIGHTS_PER_COL = 5

    # Create an array to hold the point-light positions
    point_light_positions = np.zeros((LIGHTS, LIGHTS_PER_ROW, LIGHTS_PER_COL))

    # Define the light source colors
    LIGHT_COLORS = [POINT_LIGHT_COLOR] * LIGHTS

    # Create a 3D plot for each light source
    for i in range(LIGHTS):
        row = i // LIGHTS_PER_ROW
        col = i % LIGHTS_PER_ROW

        # Calculate the light source position
        x = WIDTH / 2 + col * (WIDTH / LIGHTS_PER_ROW)
        y = HEIGHT / 2 + row * (HEIGHT / LIGHTS_PER_COL)

        # Set the light source position
        point_light_positions[i] = np.array([x, y, 0])

        # Set the light source color
        point_light_positions[i] = np.array([LIGHT_COLORS[i], LIGHT_COLORS[i], LIGHT_COLORS[i]])

    # Create a 3D plot for the point-light source
    create_3d_plot(np.mean(point_light_positions, axis=0), np.mean(point_light_positions, axis=1), 0)

    # Display the plot
    plt.show()

# Run the main function
main()
