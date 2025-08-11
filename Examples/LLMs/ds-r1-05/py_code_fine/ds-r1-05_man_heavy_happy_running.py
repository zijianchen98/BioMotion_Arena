
import pygame
import math
import sys

def main():
    # Initialize Pygame
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Point-Light Running Animation")
    clock = pygame.time.Clock()
    
    # Animation parameters
    fps = 30
    period = 1.0  # seconds per cycle
    cycle_frames = int(fps * period)
    
    # Point-light configuration: 15 points [head, neck, shoulders, elbows, hands, torso, hips, knees, ankles]
    points_info = [
        # Head
        {'x0': 0.0, 'y0': -0.6, 'A_x': 0.0, 'phase_x': 0.0, 'A_y': 0.2, 'phase_y': 0.0},
        # Neck
        {'x0': 0.0, 'y0': -0.4, 'A_x': 0.0, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Left shoulder
        {'x0': -0.2, 'y0': -0.4, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Right shoulder
        {'x0': 0.2, 'y0': -0.4, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Left elbow
        {'x0': -0.4, 'y0': -0.2, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Right elbow
        {'x0': 0.4, 'y0': -0.2, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Left hand
        {'x0': -0.6, 'y0': -0.4, 'A_x': 0.3, 'phase_x': 0.0, 'A_y': 0.2, 'phase_y': 0.0},
        # Right hand
        {'x0': 0.6, 'y0': -0.4, 'A_x': 0.3, 'phase_x': 0.5, 'A_y': 0.2, 'phase_y': 0.5},
        # Torso center (chest)
        {'x0': 0.0, 'y0': -0.2, 'A_x': 0.0, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Left hip
        {'x0': -0.2, 'y0': 0.0, 'A_x': 0.1, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Right hip
        {'x0': 0.2, 'y0': 0.0, 'A_x': 0.1, 'phase_x': 0.0, 'A_y': 0.15, 'phase_y': 0.0},
        # Left knee
        {'x0': -0.2, 'y0': 0.3, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.3, 'phase_y': 0.0},
        # Right knee
        {'x0': 0.2, 'y0': 0.3, 'A_x': 0.15, 'phase_x': 0.5, 'A_y': 0.3, 'phase_y': 0.5},
        # Left ankle
        {'x0': -0.2, 'y0': 0.6, 'A_x': 0.15, 'phase_x': 0.0, 'A_y': 0.5, 'phase_y': 0.0},
        # Right ankle
        {'x0': 0.2, 'y0': 0.6, 'A_x': 0.15, 'phase_x': 0.5, 'A_y': 0.5, 'phase_y': 0.5}
    ]
    
    # Main animation loop
    frame_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Black background
        
        t = frame_count % cycle_frames
        t_frac = t / cycle_frames
        
        # Compute and draw each point-light
        for info in points_info:
            x = info['x0'] + info['A_x'] * math.sin(2 * math.pi * (t_frac + info['phase_x']))
            y = info['y0'] + info['A_y'] * math.sin(2 * math.pi * (t_frac + info['phase_y']))
            
            # Convert to screen coordinates
            screen_x = int(screen_width / 2 + x * screen_width / 3)
            screen_y = int(screen_height / 2 + y * screen_width / 3)
            
            pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 5)
        
        pygame.display.flip()
        clock.tick(fps)
        frame_count += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
