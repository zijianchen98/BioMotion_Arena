
import pygame
import sys

# Screen dimensions
WIDTH, HEIGHT = 800, 600
# Point properties
POINT_COLOR = (255, 255, 255)
BACKGROUND = (0, 0, 0)
POINT_RADIUS = 5
FPS = 30

# Keyframes for the bowing motion (5 keyframes)
keyframes = [
    # Standing upright
    [
        (400, 150), (400, 200), (360, 210), (320, 250), (300, 300),
        (440, 210), (480, 250), (500, 300), (400, 320),
        (380, 370), (380, 450), (380, 530),
        (420, 370), (420, 450), (420, 530)
    ],
    # Start of bow: slight lean
    [
        (400, 180), (400, 230), (360, 240), (320, 280), (300, 320),
        (440, 240), (480, 280), (500, 320), (400, 340),
        (380, 380), (380, 450), (380, 530),
        (420, 380), (420, 450), (420, 530)
    ],
    # Mid bow: deeper bend
    [
        (400, 220), (400, 270), (360, 280), (320, 320), (300, 360),
        (440, 280), (480, 320), (500, 360), (400, 380),
        (380, 390), (380, 450), (380, 530),
        (420, 390), (420, 450), (420, 530)
    ],
    # Full bow: maximum bend
    [
        (400, 280), (400, 330), (360, 340), (320, 380), (300, 420),
        (440, 340), (480, 380), (500, 420), (400, 420),
        (380, 400), (380, 450), (380, 530),
        (420, 400), (420, 450), (420, 530)
    ],
    # Return to mid bow
    [
        (400, 220), (400, 270), (360, 280), (320, 320), (300, 360),
        (440, 280), (480, 320), (500, 360), (400, 380),
        (380, 390), (380, 450), (380, 530),
        (420, 390), (420, 450), (420, 530)
    ]
]

# Generate intermediate frames
frames = []
INTERMEDIATE_STEPS = 15
for i in range(len(keyframes)):
    start_frame = keyframes[i]
    end_frame = keyframes[(i + 1) % len(keyframes)]
    for step in range(INTERMEDIATE_STEPS):
        alpha = step / INTERMEDIATE_STEPS
        current_frame = []
        for j in range(len(start_frame)):
            x1, y1 = start_frame[j]
            x2, y2 = end_frame[j]
            x = x1 + (x2 - x1) * alpha
            y = y1 + (y2 - y1) * alpha
            current_frame.append((x, y))
        frames.append(current_frame)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing")
clock = pygame.time.Clock()

# Main animation loop
current_frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BACKGROUND)
    
    # Draw all 15 points
    for x, y in frames[current_frame_index]:
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)
    
    pygame.display.flip()
    clock.tick(FPS)
    current_frame_index = (current_frame_index + 1) % len(frames)

pygame.quit()
sys.exit()
