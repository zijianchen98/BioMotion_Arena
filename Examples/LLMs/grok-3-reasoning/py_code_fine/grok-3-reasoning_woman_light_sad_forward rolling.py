
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 points in order: head, Lshoulder, Rshoulder, Lelbow, Relbow, Lwrist, Rwrist, Lhand, Rhand, Lhip, Rhip, Lknee, Rknee, Lfoot, Rfoot
key_frames = [
    # t=0: Standing at x=200
    [
        (200, 160),  # head
        (190, 140),  # Lshoulder
        (210, 140),  # Rshoulder
        (190, 110),  # Lelbow
        (210, 110),  # Relbow
        (190, 80),   # Lwrist
        (210, 80),   # Rwrist
        (190, 70),   # Lhand
        (210, 70),   # Rhand
        (190, 90),   # Lhip
        (210, 90),   # Rhip
        (190, 50),   # Lknee
        (210, 50),   # Rknee
        (190, 0),    # Lfoot
        (210, 0),    # Rfoot
    ],
    # t=1: Bent forward
    [
        (200, 80),   # head
        (190, 100),  # Lshoulder
        (210, 100),  # Rshoulder
        (170, 80),   # Lelbow
        (230, 80),   # Relbow
        (150, 60),   # Lwrist
        (250, 60),   # Rwrist
        (140, 50),   # Lhand
        (260, 50),   # Rhand
        (190, 90),   # Lhip
        (210, 90),   # Rhip
        (190, 50),   # Lknee
        (210, 50),   # Rknee
        (190, 0),    # Lfoot
        (210, 0),    # Rfoot
    ],
    # t=2: Tucked position at x=400
    [
        (400, 60),   # head
        (390, 50),   # Lshoulder
        (410, 50),   # Rshoulder
        (380, 60),   # Lelbow
        (420, 60),   # Relbow
        (370, 70),   # Lwrist
        (430, 70),   # Rwrist
        (360, 80),   # Lhand
        (440, 80),   # Rhand
        (390, 70),   # Lhip
        (410, 70),   # Rhip
        (400, 60),   # Lknee
        (400, 60),   # Rknee
        (400, 80),   # Lfoot
        (400, 80),   # Rfoot
    ],
    # t=3: Crouched position at x=500
    [
        (500, 120),  # head
        (490, 100),  # Lshoulder
        (510, 100),  # Rshoulder
        (490, 80),   # Lelbow
        (510, 80),   # Relbow
        (490, 60),   # Lwrist
        (510, 60),   # Rwrist
        (490, 50),   # Lhand
        (510, 50),   # Rhand
        (490, 70),   # Lhip
        (510, 70),   # Rhip
        (490, 40),   # Lknee
        (510, 40),   # Rknee
        (490, 0),    # Lfoot
        (510, 0),    # Rfoot
    ],
    # t=4: Standing at x=600
    [
        (600, 160),  # head
        (590, 140),  # Lshoulder
        (610, 140),  # Rshoulder
        (590, 110),  # Lelbow
        (610, 110),  # Relbow
        (590, 80),   # Lwrist
        (610, 80),   # Rwrist
        (590, 70),   # Lhand
        (610, 70),   # Rhand
        (590, 90),   # Lhip
        (610, 90),   # Rhip
        (590, 50),   # Lknee
        (610, 50),   # Rknee
        (590, 0),    # Lfoot
        (610, 0),    # Rfoot
    ],
]

# Animation settings
fps = 60
total_time = 4  # seconds
total_frames = fps * total_time
clock = pygame.time.Clock()

# Function to interpolate positions
def interpolate(pos1, pos2, alpha):
    x1, y1 = pos1
    x2, y2 = pos2
    return (x1 + alpha * (x2 - x1), y1 + alpha * (y2 - y1))

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Compute current time t in seconds
    t = frame / fps

    if t > total_time:
        running = False
        continue

    # Find the appropriate key frames to interpolate between
    key_frame_index = int(t)
    if key_frame_index >= len(key_frames) - 1:
        key_frame_index = len(key_frames) - 2

    # Compute alpha for interpolation
    alpha = t - key_frame_index

    # Interpolate positions
    current_positions = []
    for i in range(15):
        pos1 = key_frames[key_frame_index][i]
        pos2 = key_frames[key_frame_index + 1][i]
        current_pos = interpolate(pos1, pos2, alpha)
        current_positions.append(current_pos)

    # Draw the points
    for pos in current_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(height - pos[1])), 5)

    # Update the display
    pygame.display.flip()

    # Increment frame
    frame += 1
    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()
