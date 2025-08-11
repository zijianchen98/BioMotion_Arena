
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions for the sad woman with a heavy weight
# Each point represents a joint in the body
point_lights = {
    'head': [WIDTH // 2, HEIGHT // 2 - 100],
    'left_shoulder': [WIDTH // 2 - 50, HEIGHT // 2 - 50],
    'right_shoulder': [WIDTH // 2 + 50, HEIGHT // 2 - 50],
    'left_elbow': [WIDTH // 2 - 100, HEIGHT // 2],
    'right_elbow': [WIDTH // 2 + 100, HEIGHT // 2],
    'left_hand': [WIDTH // 2 - 150, HEIGHT // 2 + 50],
    'right_hand': [WIDTH // 2 + 150, HEIGHT // 2 + 50],
    'left_hip': [WIDTH // 2 - 50, HEIGHT // 2 + 100],
    'right_hip': [WIDTH // 2 + 50, HEIGHT // 2 + 100],
    'left_knee': [WIDTH // 2 - 50, HEIGHT // 2 + 150],
    'right_knee': [WIDTH // 2 + 50, HEIGHT // 2 + 150],
    'left_ankle': [WIDTH // 2 - 50, HEIGHT // 2 + 200],
    'right_ankle': [WIDTH // 2 + 50, HEIGHT // 2 + 200],
    'weight': [WIDTH // 2, HEIGHT // 2 + 250],
   'sad_face': [WIDTH // 2, HEIGHT // 2 - 120],
}

# Animation parameters
jump_height = 100
jump_duration = 1000  # milliseconds
frame_rate = 60

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation loop
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Calculate jump position
    current_time = pygame.time.get_ticks() - start_time
    if current_time < jump_duration:
        jump_progress = current_time / jump_duration
        jump_offset = jump_height * math.sin(2 * math.pi * jump_progress)
    else:
        jump_offset = 0

    # Draw point-lights
    for point, position in point_lights.items():
        if point == 'weight':
            # Weight is being carried, so it moves with the body
            adjusted_position = [position[0], position[1] - jump_offset]
        elif point =='sad_face':
            # Sad face is a fixed point on the head
            adjusted_position = [position[0], position[1] - jump_offset]
        elif point in ['head', 'left_shoulder', 'right_shoulder']:
            # Upper body moves with the jump
            adjusted_position = [position[0], position[1] - jump_offset]
        elif point in ['left_elbow', 'right_elbow', 'left_hand', 'right_hand']:
            # Arms move with the upper body
            adjusted_position = [position[0], position[1] - jump_offset]
        elif point in ['left_hip', 'right_hip']:
            # Hips move with the lower body
            adjusted_position = [position[0], position[1] + jump_offset / 2]
        elif point in ['left_knee', 'right_knee']:
            # Knees move with the lower body
            adjusted_position = [position[0], position[1] + jump_offset / 2]
        elif point in ['left_ankle', 'right_ankle']:
            # Ankles move with the lower body
            adjusted_position = [position[0], position[1] + jump_offset / 2]
        else:
            # Other points remain stationary
            adjusted_position = position

        # Draw point-light
        pygame.draw.circle(screen, (255, 255, 255), adjusted_position, 5)

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(frame_rate)

# Quit Pygame
pygame.quit()
