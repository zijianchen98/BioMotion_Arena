
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define key poses
key_poses = [
    # Pose 1: Standing upright
    [(0, 1.8), (-0.15, 1.4), (0.15, 1.4), (-0.15, 1.0), (0.15, 1.0), (-0.15, 0.6), (0.15, 0.6), (-0.1, 1.0), (0.1, 1.0), (-0.1, 0.5), (0.1, 0.5), (-0.1, 0.1), (0.1, 0.1), (-0.1, 0.0), (0.1, 0.0)],
    # Pose 2: Squatting down, hands on the ground
    [(0, 1.3), (-0.15, 0.9), (0.15, 0.9), (-0.2, 0.5), (0.2, 0.5), (-0.2, 0.0), (0.2, 0.0), (-0.1, 0.5), (0.1, 0.5), (-0.1, 0.3), (0.1, 0.3), (-0.1, 0.1), (0.1, 0.1), (-0.1, 0.0), (0.1, 0.0)],
    # Pose 3: Starting to roll, head tucked, shoulders on the ground
    [(0.5, 0.2), (0.4, 0.0), (0.6, 0.0), (0.4, 0.3), (0.6, 0.3), (0.4, 0.5), (0.6, 0.5), (0.5, 0.7), (0.5, 0.7), (0.5, 1.0), (0.5, 1.0), (0.5, 1.2), (0.5, 1.2), (0.5, 1.4), (0.5, 1.4)],
    # Pose 4: Mid-roll, with back on the ground
    [(1.0, 0.6), (0.9, 0.2), (1.1, 0.2), (0.8, 0.4), (1.2, 0.4), (0.7, 0.6), (1.3, 0.6), (0.9, 0.1), (1.1, 0.1), (0.9, 0.3), (1.1, 0.3), (0.9, 0.5), (1.1, 0.5), (0.9, 0.7), (1.1, 0.7)],
    # Pose 5: Standing up again
    [(1.5, 1.8), (1.35, 1.4), (1.65, 1.4), (1.35, 1.0), (1.65, 1.0), (1.35, 0.6), (1.65, 0.6), (1.4, 1.0), (1.6, 1.0), (1.4, 0.5), (1.6, 0.5), (1.4, 0.1), (1.6, 0.1), (1.4, 0.0), (1.6, 0.0)],
]

num_segments = len(key_poses) - 1
num_frames_per_segment = 15
total_frames = num_segments * num_frames_per_segment

# Scale and offset for screen coordinates
scale = 200
offset_x = 100
offset_y = 550  # so that y=0 is at screen_y=550

# Main loop
clock = pygame.time.Clock()
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Compute current frame index for looping
    current_frame = frame % total_frames
    segment = current_frame // num_frames_per_segment
    t = (current_frame % num_frames_per_segment) / num_frames_per_segment

    # Compute interpolated positions
    positions = []
    for k in range(15):
        pos1 = key_poses[segment][k]
        pos2 = key_poses[segment + 1][k]
        x = pos1[0] + t * (pos2[0] - pos1[0])
        y = pos1[1] + t * (pos2[1] - pos1[1])
        screen_x = offset_x + x * scale
        screen_y = offset_y - y * scale
        positions.append((screen_x, screen_y))

    # Clear the screen
    screen.fill(BLACK)

    # Draw the point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update the display
    pygame.display.flip()

    # Wait for next frame
    clock.tick(30)  # 30 fps
    frame += 1

pygame.quit()
sys.exit()
