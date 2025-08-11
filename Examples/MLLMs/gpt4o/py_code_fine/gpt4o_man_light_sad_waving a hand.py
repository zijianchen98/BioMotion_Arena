
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Joint positions in the example image (relative coordinates)
POINTS = {
    "head": (0, -100),
    "shoulder_center": (0, -70),
    "left_shoulder": (-30, -70),
    "right_shoulder": (30, -70),
    "left_elbow": (-50, -40),
    "right_elbow": (50, -40),
    "left_hand": (-50, -10),
    "right_hand": (50, -10),
    "hip_center": (0, 0),
    "left_hip": (-20, 0),
    "right_hip": (20, 0),
    "left_knee": (-20, 40),
    "right_knee": (20, 40),
    "left_foot": (-20, 80),
    "right_foot": (20, 80),
}

# Function to update hand position for waving motion
def get_waving_motion(base_y, time, amplitude, speed):
    return base_y + amplitude * math.sin(speed * time)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion - Waving Hand")
    clock = pygame.time.Clock()
    
    running = True
    elapsed_time = 0  # tracks the time for animating sine waves
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen with black color
        screen.fill(BLACK)
        
        # Compute the center of the screen
        center_x, center_y = WIDTH // 2, HEIGHT // 2
        
        # Update motion
        elapsed_time += clock.get_time() / 1000  # elapsed time in seconds
        dynamic_points = POINTS.copy()
        dynamic_points["right_hand"] = (
            dynamic_points["right_hand"][0],
            get_waving_motion(dynamic_points["right_hand"][1], elapsed_time, 20, 2)
        )
        
        # Draw points
        for point_name, (x, y) in dynamic_points.items():
            pygame.draw.circle(screen, WHITE, (center_x + x, center_y + y), 5)
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
