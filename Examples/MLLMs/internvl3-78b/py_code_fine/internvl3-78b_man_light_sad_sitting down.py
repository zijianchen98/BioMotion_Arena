
import pygame
import numpy as np

# Constants
WINDOW_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

N_POINTS = 15
DURATION_FRAMES = 150  # Duration in frames for a single animation cycle
FPS = 60  # Frames per second

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sad Man Sitting Down Animation")
clock = pygame.time.Clock()

# Define points positions for different frames
# Here we use 5 animation phases and then we interpolate to get the desired number of frames.
initial_positions = np.array(
    [[400, 200], [420, 200], [440, 200], [460, 200], [480, 200], 
     [400, 240], [420, 240], [440, 240], [460, 240], [480, 240],
     [400, 300], [420, 300], [440, 300], [460, 300], [480, 300]])

# Coordinates for initial sitting down motion
positions_phase_1 = np.array(
    [[400, 250], [420, 250], [440, 250], [460, 250], [480, 250], 
     [400, 290], [420, 290], [440, 290], [460, 290], [480, 290],
     [400, 350], [420, 350], [440, 350], [460, 350], [480, 350]])

# Coordinates for midway sitting motion
positions_phase_2 = np.array(
    [[400, 250], [420, 255], [440, 260], [460, 265], [480, 270], 
     [400, 290], [420, 300], [440, 310], [460, 320], [480, 330],
     [400, 350], [420, 360], [440, 370], [460, 380], [480, 390]])

# Coordinates for halfway motion
positions_phase_3 = np.array(
    [[400, 260], [420, 270], [440, 280], [460, 290], [480, 300], 
     [400, 300], [420, 310], [440, 320], [460, 330], [480, 340],
     [400, 350], [420, 360], [440, 370], [460, 380], [480, 390]])

# Coordinates for sitting down motion
positions_phase_4 = np.array(
    [[400, 270], [420, 280], [440, 290], [460, 300], [480, 310], 
     [400, 310], [420, 320], [440, 330], [460, 340], [480, 350],
     [400, 360], [420, 370], [440, 380], [460, 390], [480, 400]])

# Coordinates for completed sitting motion
final_positions = np.array(
    [[400, 280], [420, 290], [440, 300], [460, 310], [480, 320], 
     [400, 320], [420, 330], [440, 340], [460, 350], [480, 360],
     [400, 370], [420, 380], [440, 390], [460, 400], [480, 410]])

# Generate frame positions via interpolation
all_positions = []
keyframes = [initial_positions, positions_phase_1, positions_phase_2, positions_phase_3, positions_phase_4, final_positions]

for i in range(DURATION_FRAMES):
    x_key = np.interp(i, [0, DURATION_FRAMES / 5, DURATION_FRAMES * 2 / 5, DURATION_FRAMES * 3 / 5, DURATION_FRAMES * 4 / 5, DURATION_FRAMES], [0, 1, 2, 3, 4, 5])
    current_positions = keyframes[int(x_key)]
    all_positions.append(current_positions)

# Start of the animation loop
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for point in all_positions[frame]:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    frame = (frame + 1) % DURATION_FRAMES
    clock.tick(FPS)

pygame.quit()
