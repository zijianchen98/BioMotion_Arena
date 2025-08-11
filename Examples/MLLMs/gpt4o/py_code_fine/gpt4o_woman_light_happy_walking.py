
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Frame Rate
clock = pygame.time.Clock()
FPS = 60

# Define point-light positions relative to walking motion (2D coordinates)
# These positions are based on a biomechanically plausible model for walking
points = [
    {"joint": "Head", "base_x": 0, "base_y": -100},
    {"joint": "Left Shoulder", "base_x": -40, "base_y": -60},
    {"joint": "Right Shoulder", "base_x": 40, "base_y": -60},
    {"joint": "Left Elbow", "base_x": -70, "base_y": -40},
    {"joint": "Right Elbow", "base_x": 70, "base_y": -40},
    {"joint": "Left Hip", "base_x": -30, "base_y": 0},
    {"joint": "Right Hip", "base_x": 30, "base_y": 0},
    {"joint": "Left Knee", "base_x": -30, "base_y": 70},
    {"joint": "Right Knee", "base_x": 30, "base_y": 70},
    {"joint": "Left Ankle", "base_x": -30, "base_y": 140},
    {"joint": "Right Ankle", "base_x": 30, "base_y": 140},
    {"joint": "Left Hand", "base_x": -90, "base_y": -20},
    {"joint": "Right Hand", "base_x": 90, "base_y": -20},
    {"joint": "Left Foot", "base_x": -30, "base_y": 170},
    {"joint": "Right Foot", "base_x": 30, "base_y": 170},
]

# Animation parameters
time_elapsed = 0
WALK_CYCLE_PERIOD = 2000  # Milliseconds to complete one walk cycle

def update_points(frame_time):
    """Update the positions of 15 points to simulate walking motion."""
    global time_elapsed
    # Increment time elapsed
    time_elapsed += frame_time

    # Calculate the phase of walking motion
    phase = (time_elapsed % WALK_CYCLE_PERIOD) / WALK_CYCLE_PERIOD * 2 * math.pi

    # Update each point's position
    updated_points = []
    for point in points:
        # Apply sinusoidal motion for legs, arms and other joints
        if "Hip" in point["joint"]:
            offset_x = math.sin(phase) * 15 if "Left" in point["joint"] else -math.sin(phase) * 15
            offset_y = 0
        elif "Knee" in point["joint"]:
            offset_x = math.sin(phase + math.pi / 2) * 15 if "Left" in point["joint"] else -math.sin(phase + math.pi / 2) * 15
            offset_y = math.sin(phase) * 20
        elif "Ankle" in point["joint"] or "Foot" in point["joint"]:
            offset_x = math.sin(phase) * 5 if "Left" in point["joint"] else -math.sin(phase) * 5
            offset_y = math.sin(phase) * 30
        elif "Elbow" in point["joint"]:
            offset_x = math.sin(phase + math.pi / 6) * 20 if "Left" in point["joint"] else -math.sin(phase + math.pi / 6) * 20
            offset_y = -math.sin(phase) * 10
        elif "Hand" in point["joint"]:
            offset_x = math.sin(phase + math.pi / 4) * 30 if "Left" in point["joint"] else -math.sin(phase + math.pi / 4) * 30
            offset_y = -math.sin(phase) * 20
        else:  # Static points (e.g., Head)
            offset_x = 0
            offset_y = 0
        
        # Update position
        updated_points.append((WIDTH // 2 + point["base_x"] + offset_x,
                               HEIGHT // 3 + point["base_y"] + offset_y))
    return updated_points

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation
    frame_time = clock.tick(FPS)
    positions = update_points(frame_time)

    # Draw the scene
    screen.fill(BLACK)  # Set background to black
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, 4)  # Draw point-lights (radius = 4)
    pygame.display.flip()  # Update the display

pygame.quit()
