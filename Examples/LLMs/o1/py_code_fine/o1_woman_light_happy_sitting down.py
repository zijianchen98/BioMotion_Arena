import pygame
import sys

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Sitting Down")

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define 15 points for standing (x, y) and sitting (x, y) postures
# These coordinates are just approximations for demonstration.
# The 15 points might represent (head, shoulders, elbows, wrists, hips, knees, ankles, etc.)
standing_points = [
    (400, 200),  # Head
    (400, 220),  # Neck
    (385, 240),  # Left Shoulder
    (415, 240),  # Right Shoulder
    (370, 270),  # Left Elbow
    (430, 270),  # Right Elbow
    (360, 300),  # Left Wrist
    (440, 300),  # Right Wrist
    (395, 300),  # Left Hip
    (405, 300),  # Right Hip
    (390, 350),  # Left Knee
    (410, 350),  # Right Knee
    (390, 400),  # Left Ankle
    (410, 400),  # Right Ankle
    (400, 310)   # Torso midpoint
]

sitting_points = [
    (400, 210),  # Head
    (400, 230),  # Neck
    (385, 250),  # Left Shoulder
    (415, 250),  # Right Shoulder
    (370, 290),  # Left Elbow
    (430, 290),  # Right Elbow
    (360, 320),  # Left Wrist
    (440, 320),  # Right Wrist
    (395, 360),  # Left Hip
    (405, 360),  # Right Hip
    (390, 380),  # Left Knee
    (410, 380),  # Right Knee
    (390, 400),  # Left Ankle
    (410, 400),  # Right Ankle
    (400, 340)   # Torso midpoint
]

# Function to linearly interpolate between standing and sitting
def interpolate_points(p1, p2, t):
    return [(p1[i][0] + (p2[i][0] - p1[i][0]) * t,
             p1[i][1] + (p2[i][1] - p1[i][1]) * t) for i in range(len(p1))]

# Variables to control the sitting-down animation
t = 0.0        # Interpolation parameter between 0 and 1
speed = 0.01   # How quickly to move from standing to sitting
direction = 1  # 1 means going toward sitting, -1 means returning to standing

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update interpolation parameter
    t += direction * speed
    if t > 1.0:
        t = 1.0
        direction = -1  # Once fully sitting, reverse direction (stand up again)
    elif t < 0.0:
        t = 0.0
        direction = 1   # Once standing again, switch direction

    # Interpolate between standing and sitting
    current_points = interpolate_points(standing_points, sitting_points, t)

    # Draw the 15 white circles
    for (x, y) in current_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()