
import cv2
import numpy as np
import time

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPAWN_RATE = 10  # milliseconds

# Create a window
cv2.namedWindow("Point Light Stimulus", cv2.WINDOW_NORMAL)

# Define the initial positions of the lights
lights = np.random.choice([-LIGHT_RADIUS, LIGHT_RADIUS], size=NUM_LIGHTS, replace=False)

# Define the action sequence
action_sequence = [
    {"action": "sit_down", "time": 0},  # initial pose
    {"action": "lower_left_knee", "time": 100},  # lower left knee
    {"action": "lower_right_knee", "time": 150},  # lower right knee
    {"action": "lower_left_hip", "time": 200},  # lower left hip
    {"action": "lower_right_hip", "time": 250},  # lower right hip
    {"action": "lower_back", "time": 300},  # lower back
    {"action": "lower_left_leg", "time": 350},  # lower left leg
    {"action": "lower_right_leg", "time": 400},  # lower right leg
    {"action": "lower_left_foot", "time": 450},  # lower left foot
    {"action": "lower_right_foot", "time": 500},  # lower right foot
    {"action": "lower_back", "time": 550},  # lower back
    {"action": "lower_left_hip", "time": 600},  # lower left hip
    {"action": "lower_right_hip", "time": 650},  # lower right hip
    {"action": "lower_left_knee", "time": 700},  # lower left knee
    {"action": "lower_right_knee", "time": 750},  # lower right knee
]

# Define the animation function
def animate(action):
    global lights
    cv2.imshow("Point Light Stimulus", create_image())
    cv2.waitKey(1000 // 60)  # 60 FPS
    if action["action"] == "sit_down":
        lights = np.array([LIGHT_RADIUS if i == 0 else -LIGHT_RADIUS for i in range(NUM_LIGHTS)])
    elif action["action"] == "lower_left_knee":
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = LIGHT_RADIUS
        lights[3] = LIGHT_RADIUS
        lights[4] = LIGHT_RADIUS
    elif action["action"] == "lower_right_knee":
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = LIGHT_RADIUS
        lights[8] = LIGHT_RADIUS
        lights[9] = LIGHT_RADIUS
    elif action["action"] == "lower_left_hip":
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = -LIGHT_RADIUS
        lights[3] = -LIGHT_RADIUS
        lights[4] = -LIGHT_RADIUS
    elif action["action"] == "lower_right_hip":
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = -LIGHT_RADIUS
        lights[8] = -LIGHT_RADIUS
        lights[9] = -LIGHT_RADIUS
    elif action["action"] == "lower_back":
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = -LIGHT_RADIUS
        lights[3] = -LIGHT_RADIUS
        lights[4] = -LIGHT_RADIUS
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = -LIGHT_RADIUS
        lights[8] = -LIGHT_RADIUS
        lights[9] = -LIGHT_RADIUS
    elif action["action"] == "lower_left_leg":
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = -LIGHT_RADIUS
        lights[3] = -LIGHT_RADIUS
        lights[4] = -LIGHT_RADIUS
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = -LIGHT_RADIUS
        lights[8] = -LIGHT_RADIUS
        lights[9] = LIGHT_RADIUS
    elif action["action"] == "lower_right_leg":
        lights[10] = -LIGHT_RADIUS
        lights[11] = -LIGHT_RADIUS
        lights[12] = -LIGHT_RADIUS
        lights[13] = -LIGHT_RADIUS
        lights[14] = -LIGHT_RADIUS
        lights[15] = -LIGHT_RADIUS
    elif action["action"] == "lower_left_foot":
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = -LIGHT_RADIUS
        lights[3] = -LIGHT_RADIUS
        lights[4] = -LIGHT_RADIUS
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = -LIGHT_RADIUS
        lights[8] = -LIGHT_RADIUS
        lights[9] = LIGHT_RADIUS
        lights[10] = LIGHT_RADIUS
        lights[11] = LIGHT_RADIUS
        lights[12] = LIGHT_RADIUS
        lights[13] = LIGHT_RADIUS
        lights[14] = LIGHT_RADIUS
    elif action["action"] == "lower_right_foot":
        lights[10] = -LIGHT_RADIUS
        lights[11] = -LIGHT_RADIUS
        lights[12] = -LIGHT_RADIUS
        lights[13] = -LIGHT_RADIUS
        lights[14] = -LIGHT_RADIUS
        lights[15] = -LIGHT_RADIUS
        lights[0] = -LIGHT_RADIUS
        lights[1] = -LIGHT_RADIUS
        lights[2] = -LIGHT_RADIUS
        lights[3] = -LIGHT_RADIUS
        lights[4] = -LIGHT_RADIUS
        lights[5] = -LIGHT_RADIUS
        lights[6] = -LIGHT_RADIUS
        lights[7] = -LIGHT_RADIUS
        lights[8] = -LIGHT_RADIUS
        lights[9] = LIGHT_RADIUS

# Define the image creation function
def create_image():
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    for i, light in enumerate(lights):
        x = int(i % 15 * 40)
        y = int(i // 15 * 40)
        cv2.circle(image, (x, y), LIGHT_RADIUS, WHITE, -1)
    return image

# Start the animation
start_time = time.time()
for action in action_sequence:
    animate(action)
    cv2.waitKey(1000 // 60)  # 60 FPS
    if time.time() - start_time > action["time"]:
        break

# Close the window
cv2.destroyAllWindows()
