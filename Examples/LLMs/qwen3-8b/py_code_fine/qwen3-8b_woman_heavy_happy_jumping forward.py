
import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Jumping Forward - Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define a joint structure for the human body
JOINTS = [
    ("hips", (400, 300)),
    ("left_knee", (350, 350)),
    ("left_ankle", (320, 400)),
    ("right_knee", (450, 350)),
    ("right_ankle", (480, 400)),
    ("torso", (400, 250)),
    ("left_shoulder", (340, 200)),
    ("left_elbow", (310, 150)),
    ("left_wrist", (280, 100)),
    ("right_shoulder", (460, 200)),
    ("right_elbow", (490, 150)),
    ("right_wrist", (520, 100)),
    ("neck", (400, 200)),
    ("head", (400, 150)),
    ("left_eye", (390, 130)),
    ("right_eye", (410, 130)),
]

# Create a list of point-light positions
point_lights = [pygame.Vector2(x, y) for (name, (x, y)) in JOINTS]

# Define a function to simulate realistic motion
def animate_body():
    # Jumping forward motion
    # Simulate a smooth jump and forward motion
    # This is a simplified biomechanical model
    for joint in JOINTS:
        if joint[0] == "hips":
            # Hips move forward and up
            point_lights[0] += pygame.Vector2(0.5, -0.5)
        elif joint[0] == "torso":
            # Torso moves forward and up
            point_lights[5] += pygame.Vector2(0.5, -0.5)
        elif joint[0] == "neck":
            # Neck moves forward and up
            point_lights[13] += pygame.Vector2(0.5, -0.5)
        elif joint[0] == "head":
            # Head moves forward and up
            point_lights[14] += pygame.Vector2(0.5, -0.5)
        elif joint[0] == "left_shoulder":
            # Left shoulder moves forward
            point_lights[7] += pygame.Vector2(0.3, 0)
        elif joint[0] == "right_shoulder":
            # Right shoulder moves forward
            point_lights[10] += pygame.Vector2(0.3, 0)
        elif joint[0] == "left_knee":
            # Left knee moves forward and down
            point_lights[1] += pygame.Vector2(0.4, 0.5)
        elif joint[0] == "right_knee":
            # Right knee moves forward and down
            point_lights[4] += pygame.Vector2(0.4, 0.5)
        elif joint[0] == "left_ankle":
            # Left ankle moves forward
            point_lights[2] += pygame.Vector2(0.3, 0)
        elif joint[0] == "right_ankle":
            # Right ankle moves forward
            point_lights[5] += pygame.Vector2(0.3, 0)
        elif joint[0] == "left_elbow":
            # Left elbow moves forward
            point_lights[8] += pygame.Vector2(0.3, 0)
        elif joint[0] == "right_elbow":
            # Right elbow moves forward
            point_lights[11] += pygame.Vector2(0.3, 0)
        elif joint[0] == "left_wrist":
            # Left wrist moves forward
            point_lights[9] += pygame.Vector2(0.3, 0)
        elif joint[0] == "right_wrist":
            # Right wrist moves forward
            point_lights[12] += pygame.Vector2(0.3, 0)
        elif joint[0] == "left_eye":
            # Left eye moves forward slightly
            point_lights[15] += pygame.Vector2(0.1, 0)
        elif joint[0] == "right_eye":
            # Right eye moves forward slightly
            point_lights[16] += pygame.Vector2(0.1, 0)

    # Reset positions when they go out of bounds
    for i in range(len(point_lights)):
        if point_lights[i].x > WIDTH:
            point_lights[i] = pygame.Vector2(0, point_lights[i].y)
        elif point_lights[i].x < 0:
            point_lights[i] = pygame.Vector2(WIDTH, point_lights[i].y)
        elif point_lights[i].y > HEIGHT:
            point_lights[i] = pygame.Vector2(point_lights[i].x, 0)
        elif point_lights[i].y < 0:
            point_lights[i] = pygame.Vector2(point_lights[i].x, HEIGHT)

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    animate_body()

    # Draw point-lights
    for light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(light.x), int(light.y)), 5)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
