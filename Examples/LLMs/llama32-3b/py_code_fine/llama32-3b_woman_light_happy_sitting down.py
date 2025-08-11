
import cv2
import numpy as np
import math

# Define constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Define action parameters
ACTION = "sitting_down"

# Define lighting parameters
LIGHT_SIZE = 5
LIGHT_SPACING = 50

# Define animation parameters
ANIMATION_DURATION = 100  # milliseconds

# Define camera parameters
CAMERA_FOV = 60  # degrees

class Light:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def update(self, t):
        self.angle += 0.05 * math.sin(t)

    def get_position(self):
        return (self.x, self.y, self.angle)

def draw_light(img, light):
    x, y, angle = light.get_position()
    light_x = WIDTH // 2 + int(WIDTH // 2 + math.cos(angle) * 200)
    light_y = HEIGHT // 2 + int(HEIGHT // 2 + math.sin(angle) * 200)
    cv2.circle(img, (light_x, light_y), LIGHT_SIZE, WHITE, -1)

def animate(frame):
    global light_positions
    light_positions = []
    for i in range(NUM_LIGHTS):
        angle = i / NUM_LIGHTS * 2 * math.pi
        x = WIDTH // 2 + int(WIDTH // 2 + math.cos(angle) * 200)
        y = HEIGHT // 2 + int(HEIGHT // 2 + math.sin(angle) * 200)
        light_positions.append(Light(x, y, angle))

    for i, light in enumerate(light_positions):
        light.update(frame / 1000)
        draw_light(frame, light)

    return frame

def main():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        raise Exception("Failed to capture video")

    cv2.namedWindow("Point-Light Stimulus", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Point-Light Stimulus", WIDTH, HEIGHT)

    for frame_num in range(ANIMATION_DURATION):
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        frame = animate(frame)

        cv2.imshow("Point-Light Stimulus", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
