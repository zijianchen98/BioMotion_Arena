
import cv2
import numpy as np
import math
import random

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COUNT = 15
LIGHT_RADIUS = 10

# Define class for point-light stimulus
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.1, 0.5)

    def update(self):
        self.angle += self.speed
        self.x = WIDTH // 2 + math.cos(self.angle) * 200
        self.y = HEIGHT // 2 + math.sin(self.angle) * 200

# Define function to draw point-lights
def draw_point_lights(frame, lights):
    for light in lights:
        cv2.circle(frame, (int(light.x), int(light.y)), LIGHT_RADIUS, WHITE, -1)

# Define function to generate animation
def generate_animation():
    cap = cv2.VideoCapture(0)
    clock = cv2.getTickFrequency()
    fps = 60

    # Create a list of point-lights
    lights = [PointLight(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(LIGHT_COUNT)]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Draw point-lights on the frame
        draw_point_lights(frame, lights)

        # Update point-lights
        for light in lights:
            light.update()

        # Display the frame
        cv2.imshow('Point-Light Stimulus', frame)

        # Calculate frame rate
        frame_time = clock() / fps
        if frame_time > 0.0167:  # 60 FPS
            break

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Call the function to generate animation
generate_animation()
