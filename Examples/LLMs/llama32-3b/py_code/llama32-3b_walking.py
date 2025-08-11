
import cv2
import numpy as np
import time

# Define the walking cycle parameters
gait_cycle_length = 2  # seconds
gait_cycle_duration = gait_cycle_length * 10  # seconds
stride_length = 0.8  # meters
stride_duration = 0.1  # seconds
frame_rate = 30  # Hz
frame_duration = 1 / frame_rate  # seconds

# Define the camera parameters
camera_fov = 60  # degrees
camera_height = 500  # pixels

# Define the point-light parameters
num_point_lights = 15
point_light_size = 10  # pixels

# Define the walking cycle phases
phases = [
    {"phase": 0, "stride": 0, "leg_position": (0, 0), "arm_position": (0, 0)},
    {"phase": 0, "stride": 1, "leg_position": (1, 0), "arm_position": (0, 0)},
    {"phase": 0, "stride": 2, "leg_position": (2, 0), "arm_position": (0, 0)},
    {"phase": 0, "stride": 3, "leg_position": (3, 0), "arm_position": (0, 0)},
    {"phase": 0, "stride": 4, "leg_position": (0, 1), "arm_position": (0, 0)},
    {"phase": 0, "stride": 5, "leg_position": (0, 2), "arm_position": (0, 0)},
    {"phase": 0, "stride": 6, "leg_position": (0, 3), "arm_position": (0, 0)},
    {"phase": 0, "stride": 7, "leg_position": (0, 4), "arm_position": (0, 0)},
    {"phase": 0, "stride": 8, "leg_position": (0, 5), "arm_position": (0, 0)},
    {"phase": 0, "stride": 9, "leg_position": (0, 6), "arm_position": (0, 0)},
    {"phase": 0, "stride": 10, "leg_position": (0, 7), "arm_position": (0, 0)},
    {"phase": 0, "stride": 11, "leg_position": (0, 8), "arm_position": (0, 0)},
    {"phase": 0, "stride": 12, "leg_position": (0, 9), "arm_position": (0, 0)},
    {"phase": 0, "stride": 13, "leg_position": (0, 10), "arm_position": (0, 0)},
    {"phase": 0, "stride": 14, "leg_position": (0, 11), "arm_position": (0, 0)},
    {"phase": 0, "stride": 15, "leg_position": (0, 12), "arm_position": (0, 0)},
    {"phase": 1, "stride": 0, "leg_position": (1, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 1, "leg_position": (2, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 2, "leg_position": (3, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 3, "leg_position": (4, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 4, "leg_position": (5, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 5, "leg_position": (6, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 6, "leg_position": (7, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 7, "leg_position": (8, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 8, "leg_position": (9, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 9, "leg_position": (10, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 10, "leg_position": (11, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 11, "leg_position": (12, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 12, "leg_position": (13, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 13, "leg_position": (14, 0), "arm_position": (0, 0)},
    {"phase": 1, "stride": 14, "leg_position": (0, 1), "arm_position": (0, 0)},
    {"phase": 1, "stride": 15, "leg_position": (0, 2), "arm_position": (0, 0)},
]

# Initialize the OpenCV window
cv2.namedWindow("Walking Cycle", cv2.WINDOW_NORMAL)

# Initialize the frame counter
frame_counter = 0

while True:
    # Clear the frame
    frame = np.zeros((camera_height, camera_height, 3), dtype=np.uint8)

    # Draw the walking cycle
    for i, phase in enumerate(phases):
        # Calculate the leg position
        leg_x = int(phase["stride"] * stride_length * np.sin(2 * np.pi * (i / 15)))
        leg_y = int(phase["stride"] * stride_length * np.cos(2 * np.pi * (i / 15)))
        arm_x = int(phase["stride"] * stride_length * np.sin(2 * np.pi * (i / 15) + np.pi / 2))
        arm_y = int(phase["stride"] * stride_length * np.cos(2 * np.pi * (i / 15) + np.pi / 2))

        # Draw the point-lights
        for j in range(num_point_lights):
            point_light_x = int(leg_x + j * 2)
            point_light_y = int(leg_y + j * 2)
            cv2.circle(frame, (point_light_x, point_light_y), point_light_size, (255, 255, 255), -1)

        # Draw the leg and arm
        cv2.line(frame, (leg_x, leg_y), (leg_x + 10, leg_y), (255, 255, 255), 2)
        cv2.line(frame, (arm_x, arm_y), (arm_x + 10, arm_y), (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Walking Cycle", frame)

    # Check for the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()
