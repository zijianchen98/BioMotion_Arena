
import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Setup display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
fps = 60
clock = pygame.time.Clock()

# Keypoint structure representing lying down motion (simplified example)
# Coordinates are normalized positions of joints in 2D space relative to the center
keypoints = np.array([
    [0, -100],  # Head
    [-50, -50], [50, -50],  # Shoulders
    [-70, 0], [70, 0],  # Elbows
    [-50, 50], [50, 50],  # Wrists
    [-30, 100], [30, 100],  # Hips
    [-70, 150], [70, 150],  # Knees
    [-50, 200], [50, 200],  # Ankles
    [-20, 250], [20, 250]   # Feet
])

# Motion parameters
animation_speed = 0.1  # Speed multiplier
motion_amplitude = 10  # Amount of oscillation

# Generate biomechanically plausible motion pattern
def update_keypoints(frame_count, keypoints):
    updated_keypoints = keypoints.copy()
    for i in range(len(updated_keypoints)):
        # Oscillate joints to simulate natural motion
        if i > 1:  # Skip head and shoulders for lying down action
            offset = motion_amplitude * np.sin(frame_count * animation_speed + i)
            updated_keypoints[i][1] += offset  # Apply Y-axis motion
    return updated_keypoints

# Draw points on the screen
def draw_keypoints(screen, keypoints, center):
    for point in keypoints:
        x = center[0] + point[0]
        y = center[1] + point[1]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

# Animation loop
def main():
    center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen
    frame_count = 0
    
    while True:
        screen.fill(BLACK)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update keypoints for animation
        animated_keypoints = update_keypoints(frame_count, keypoints)
        
        # Draw the keypoints
        draw_keypoints(screen, animated_keypoints, center)
        
        # Update the display
        pygame.display.flip()
        
        # Increment frame counter and maintain frame rate
        frame_count += 1
        clock.tick(fps)

if __name__ == "__main__":
    main()
