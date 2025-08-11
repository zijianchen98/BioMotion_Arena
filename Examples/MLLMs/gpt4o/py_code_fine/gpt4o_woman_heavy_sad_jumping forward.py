
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion - Sadwoman Jumping Forward")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the points for a human figure
# These represent different body parts: head, shoulders, elbows, wrists, hips, knees, ankles
points = {
    "head": [0, -100],
    "shoulder_left": [-40, -80],
    "shoulder_right": [40, -80],
    "elbow_left": [-60, -50],
    "elbow_right": [60, -50],
    "wrist_left": [-70, -20],
    "wrist_right": [70, -20],
    "hip_left": [-30, 0],
    "hip_right": [30, 0],
    "knee_left": [-30, 50],
    "knee_right": [30, 50],
    "ankle_left": [-30, 100],
    "ankle_right": [30, 100],
    "center_torso": [0, -40],
    "pelvis": [0, 20]
}

# Function to animate the points to simulate "jumping forward"
def animate(frame):
    jump_height = 40  # Adjust jump height
    jump_period = 60  # Frames per jump

    # Calculate vertical motion (sinusoidal) and forward motion
    dy = -math.sin(math.pi * frame / jump_period) * jump_height
    dx = math.cos(math.pi * frame / jump_period) * 5  # Simulate forward movement

    animated_points = {}
    for name, (x, y) in points.items():
        # Add slight pendulum motion for non-centered points
        if "shoulder" in name or "elbow" in name or "wrist" in name:
            swing = math.sin(math.pi * frame / jump_period) * 10
            x += swing if "right" in name else -swing
        elif "knee" in name or "ankle" in name:
            swing = math.sin(math.pi * frame / jump_period) * 15
            x += swing if "right" in name else -swing

        animated_points[name] = [x + dx, y + dy]

    return animated_points

# Main loop
def main():
    frame = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Animate the points
        animated_points = animate(frame)

        # Draw the points (scaled and centered on screen)
        for x, y in animated_points.values():
            pygame.draw.circle(screen, WHITE, (int(x + WIDTH // 2), int(y + HEIGHT // 2)), 5)

        # Update the frame
        frame += 1
        if frame > 60:  # Reset after one jump cycle
            frame = 0
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 30 FPS
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
