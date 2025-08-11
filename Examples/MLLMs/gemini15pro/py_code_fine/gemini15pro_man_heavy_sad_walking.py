
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a list of its x and y coordinates over time
num_frames = 60  # Number of frames in the animation

# Example coordinates for head, shoulders, elbows, wrists, hips, knees, ankles
head_x = np.linspace(100, 110, num_frames) + 5*np.sin(np.linspace(0, 2*np.pi, num_frames))  # Subtle head bob
head_y = np.ones(num_frames) * 200

shoulder_left_x = np.linspace(90, 100, num_frames)
shoulder_left_y = np.ones(num_frames) * 180

shoulder_right_x = np.linspace(110, 120, num_frames)
shoulder_right_y = np.ones(num_frames) * 180



elbow_left_x = shoulder_left_x + 10*np.cos(np.linspace(0, np.pi/2, num_frames)) 
elbow_left_y = shoulder_left_y - 20

elbow_right_x = shoulder_right_x - 10*np.cos(np.linspace(0, np.pi/2, num_frames)) 
elbow_right_y = shoulder_right_y - 20


wrist_left_x = shoulder_left_x - 20 + 10*np.sin(np.linspace(0, np.pi, num_frames))
wrist_left_y = shoulder_left_y - 30

wrist_right_x = shoulder_right_x + 20 - 10*np.sin(np.linspace(0, np.pi, num_frames))
wrist_right_y = shoulder_right_y - 30


hips_center_x = np.linspace(100, 110, num_frames) + 5 * np.sin(np.linspace(0, np.pi/2, num_frames))
hips_center_y = np.ones(num_frames) * 120

knee_left_x = hips_center_x - 10 
knee_left_y = hips_center_y - 30


knee_right_x = hips_center_x + 10
knee_right_y = hips_center_y - 30


ankle_left_x = hips_center_x - 15
ankle_left_y = knee_left_y - 30 + 10*np.cos(np.linspace(0, np.pi, num_frames))

ankle_right_x = hips_center_x + 15
ankle_right_y = knee_right_y - 30 -10*np.cos(np.linspace(0, np.pi, num_frames))


#... define similar arrays for other 15 point lights


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([50, 150]) # adjust based on point coordinates
ax.set_ylim([0, 250])
ax.set_aspect('equal')  # Ensures proper aspect ratio for human form
ax.set_facecolor('black')  # Set background to black
scatter = ax.scatter([], [], s=20, c='white')  # Initialize scatter plot


# Animation update function
def animate(i):
    x_coords = [head_x[i], shoulder_left_x[i], shoulder_right_x[i], elbow_left_x[i],elbow_right_x[i],wrist_left_x[i],wrist_right_x[i],hips_center_x[i],knee_left_x[i],knee_right_x[i],ankle_left_x[i],ankle_right_x[i]]
    y_coords = [head_y[i],shoulder_left_y[i], shoulder_right_y[i], elbow_left_y[i],elbow_right_y[i],wrist_left_y[i],wrist_right_y[i],hips_center_y[i],knee_left_y[i],knee_right_y[i],ankle_left_y[i],ankle_right_y[i]]

    scatter.set_offsets(np.c_[x_coords, y_coords]) # Update point positions
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=40, blit=True) # interval controls speed

#To display the animation
plt.show()

#To save the animation
# ani.save('walking_animation.gif', writer='imagemagick') # Requires imagemagick

