
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body parts and their corresponding points
BODY_PARTS = {
    'head': (0, -50),
    'left_shoulder': (-50, -25),
    'left_elbow': (-50, 25),
    'left_hand': (-50, 75),
    'right_shoulder': (50, -25),
    'right_elbow': (50, 25),
    'right_hand': (50, 75),
    'left_hip': (-50, 25),
    'left_knee': (-50, 100),
    'left_foot': (-50, 150),
    'right_hip': (50, 25),
    'right_knee': (50, 100),
    'right_foot': (50, 150)
}

# Angles and movement speed
angle = 0
speed = 0.1

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Running the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Calculate the position of each body part
    head_x = WIDTH / 2 + 50 * math.sin(angle)
    head_y = HEIGHT / 2 + 50 * math.cos(angle)
    left_shoulder_x = head_x + 50 * math.sin(angle)
    left_shoulder_y = head_y + 50 * math.cos(angle)
    left_elbow_x = left_shoulder_x + 50 * math.sin(angle)
    left_elbow_y = left_shoulder_y + 50 * math.cos(angle)
    left_hand_x = left_elbow_x + 50 * math.sin(angle)
    left_hand_y = left_elbow_y + 50 * math.cos(angle)
    right_shoulder_x = head_x - 50 * math.sin(angle)
    right_shoulder_y = head_y - 50 * math.cos(angle)
    right_elbow_x = right_shoulder_x - 50 * math.sin(angle)
    right_elbow_y = right_shoulder_y - 50 * math.cos(angle)
    right_hand_x = right_elbow_x - 50 * math.sin(angle)
    right_hand_y = right_elbow_y - 50 * math.cos(angle)
    left_hip_x = left_hand_x
    left_hip_y = left_hand_y + 100
    left_knee_x = left_hip_x + 50 * math.sin(angle)
    left_knee_y = left_hip_y + 50 * math.cos(angle)
    left_foot_x = left_knee_x + 50 * math.sin(angle)
    left_foot_y = left_knee_y + 50 * math.cos(angle)
    right_hip_x = right_hand_x
    right_hip_y = right_hand_y + 100
    right_knee_x = right_hip_x - 50 * math.sin(angle)
    right_knee_y = right_hip_y - 50 * math.cos(angle)
    right_foot_x = right_knee_x - 50 * math.sin(angle)
    right_foot_y = right_knee_y - 50 * math.cos(angle)

    # Draw each body part as a white circle
    for part, (x, y) in BODY_PARTS.items():
        if part in ['head', 'left_hand', 'right_hand', 'left_foot', 'right_foot']:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
        else:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 10)

    # Update the angle for the next frame
    angle += speed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
