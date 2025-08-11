
import pygame
import math
import sys

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Animation: Man Lying Down")
    clock = pygame.time.Clock()
    
    # Define 15 body points (initial positions when lying flat)
    # Format: [x, y, movement_factor, base_y_offset]
    points = [
        [WIDTH * 0.45, HEIGHT * 0.35, 0.0, 0],       # Head
        [WIDTH * 0.45, HEIGHT * 0.45, 0.5, -5],     # Neck
        [WIDTH * 0.40, HEIGHT * 0.40, 0.8, -5],     # Right shoulder
        [WIDTH * 0.35, HEIGHT * 0.40, 0.0, 0],       # Right elbow
        [WIDTH * 0.30, HEIGHT * 0.40, 0.0, 0],       # Right hand
        [WIDTH * 0.50, HEIGHT * 0.40, 0.8, -5],     # Left shoulder
        [WIDTH * 0.55, HEIGHT * 0.40, 0.0, 0],       # Left elbow
        [WIDTH * 0.60, HEIGHT * 0.40, 0.0, 0],       # Left hand
        [WIDTH * 0.40, HEIGHT * 0.60, 0.2, 10],     # Right hip
        [WIDTH * 0.40, HEIGHT * 0.70, 0.0, 0],       # Right knee
        [WIDTH * 0.40, HEIGHT * 0.80, 0.0, 0],       # Right foot
        [WIDTH * 0.50, HEIGHT * 0.60, 0.2, 10],     # Left hip
        [WIDTH * 0.50, HEIGHT * 0.70, 0.0, 0],       # Left knee
        [WIDTH * 0.50, HEIGHT * 0.80, 0.0, 0],       # Left foot
        [WIDTH * 0.45, HEIGHT * 0.52, 1.0, 5]       # Chest (main breathing point)
    ]
    
    # Animation parameters
    amplitude = 3  # Breathing motion amplitude
    speed = 0.025  # Breathing speed
    
    frame_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Black background
        
        # Update points with breathing motion
        for point in points:
            # Vertical movement with individual phase offsets
            breathing_offset = math.sin(frame_count * speed + point[3] * 0.1)
            point[1] = HEIGHT * 0.5 + point[3] + amplitude * point[2] * breathing_offset
        
        # Draw all points as circles
        for point in points:
            pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 6)
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
        frame_count += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
