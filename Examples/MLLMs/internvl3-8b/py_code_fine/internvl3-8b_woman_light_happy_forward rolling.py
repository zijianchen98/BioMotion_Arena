
import cv2
import numpy as np

def draw_point_light(img, x, y):
    """
    Draws a point light at the specified coordinates in the provided image.
    """
    center = int(x * img.shape[1]), int(y * img.shape[0])
    cv2.circle(img, center, 2, (255, 255, 255), -1)

# Constants
n_points = 15
height, width = 512, 512

# Initialize the frame
frame = np.zeros((height, width, 3), dtype=np.uint8)

# Define initial positions
positions = [(0.1 + i * 0.06, 0.7 + i * 0.06) for i in range(15)]

# Open a video capture object for saving the animation
out = cv2.VideoWriter('point_light_animation.mp4', cv2.Video_fourcc(*'mp4v'), 15.0, (width, height))

# Draw positions
for pos in positions:
    draw_point_light(frame, *pos)
out.write(frame)

# Define the forward rolling motion
def forward_rolling_animation(positions, duration=100):
    """
    Animates the positions of the points to depict a forward rolling for a certain duration.
    """
    step_1 = [(0.1, 0.7), (0.11, 0.71), (0.12, 0.72), (0.13, 0.73), (0.14, 0.74), 
              (0.15, 0.75), (0.16, 0.76), (0.17, 0.77), (0.18, 0.78), (0.19, 0.79),
              (0.20, 0.80), (0.19, 0.81), (0.18, 0.82), (0.17, 0.83), (0.16, 0.84)]
    step_2 = [(0.16 + i * 0.04, 0.84) for i in range(15)]
    total_steps = 250  # duration of the animation
    step_size = total_steps // 20

    for t in range(total_steps):
        # Move to step 1
        if t < step_size:
            frame_idx = t
        # In step 1
        elif t < 2 * step_size:
            frame_idx = t - step_size
        # Move to step 2
        elif t < 3 * step_size:
            frame_idx = 2 * step_size + (t - 2 * step_size) * (15 - 1) / step_size
        # In step 2
        else:
            frame_idx = 2 * step_size + 15 * ((t - 3 * step_size) / step_size)
        x, y = step_1[frame_idx]
        draw_point_light(frame, x, y)
        out.write(np.copy(frame))

# Run the animation
forward_rolling_animation(positions)
out.release()
