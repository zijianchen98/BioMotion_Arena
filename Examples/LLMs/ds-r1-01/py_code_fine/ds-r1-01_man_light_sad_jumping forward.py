
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
initial_y = height // 2
initial_x = width // 4
jump_duration = 100  # Frames per jump cycle
jump_height = 80     # Vertical jump height
jump_distance = 50   # Horizontal distance per jump
points_radius = 5    # Size of point-lights

clock = pygame.time.Clock()
frame_counter = 0
current_initial_x = initial_x

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame and phase
    frame_counter += 1
    phase = frame_counter % jump_duration

    # Reset position when screen edge is reached
    if phase == 0:
        current_initial_x += jump_distance
        if current_initial_x > width - 200:
            current_initial_x = initial_x

    # Calculate vertical position using parabolic trajectory
    if phase < jump_duration / 2:
        vertical_phase = phase / (jump_duration / 2)
        torso_y = initial_y - jump_height * (1 - (1 - vertical_phase)**2)
    else:
        vertical_phase = (phase - jump_duration/2) / (jump_duration / 2)
        torso_y = initial_y - jump_height * (1 - vertical_phase**2)

    # Calculate horizontal position
    torso_x = current_initial_x + (phase / jump_duration) * jump_distance

    # Calculate positions for 15 point-lights
    head = (torso_x, torso_y - 30)
    torso = (torso_x, torso_y)
    left_shoulder = (torso_x - 20, torso_y + 10)
    right_shoulder = (torso_x + 20, torso_y + 10)
    left_elbow = (
        left_shoulder[0] - 10 * math.sin(phase * 0.1),
        left_shoulder[1] + 20
    )
    right_elbow = (
        right_shoulder[0] + 10 * math.sin(phase * 0.1),
        right_shoulder[1] + 20
    )
    left_hand = (
        left_elbow[0] - 10 * math.sin(phase * 0.1 + 0.5),
        left_elbow[1] + 20
    )
    right_hand = (
        right_elbow[0] + 10 * math.sin(phase * 0.1 + 0.5),
        right_elbow[1] + 20
    )
    left_hip = (torso_x - 15, torso_y + 30)
    right_hip = (torso_x + 15, torso_y + 30)
    left_knee = (
        left_hip[0] - 10 * math.sin(phase * 0.1),
        left_hip[1] + 30
    )
    right_knee = (
        right_hip[0] + 10 * math.sin(phase * 0.1),
        right_hip[1] + 30
    )
    left_ankle = (
        left_knee[0] - 10 * math.sin(phase * 0.1 + 0.5),
        left_knee[1] + 30
    )
    right_ankle = (
        right_knee[0] + 10 * math.sin(phase * 0.1 + 0.5),
        right_knee[1] + 30
    )
    left_foot = (left_ankle[0], left_ankle[1] + 15)

    # List of 15 point-light positions
    points = [
        head, torso, left_shoulder, right_shoulder,
        left_elbow, right_elbow, left_hand, right_hand,
        left_hip, right_hip, left_knee, right_knee,
        left_ankle, right_ankle, left_foot
    ]

    # Draw all elements
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, 
                         (int(point[0]), int(point[1])), points_radius)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
