
import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
POINT_COLOR = (255, 255, 255)  # White point-lights
FPS = 30

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")

# Define a class for the point-light stimulus
class PointLight:
    def __init__(self, start_pos, end_pos, duration):
        self.start_pos = np.array(start_pos, dtype=float)
        self.end_pos = np.array(end_pos, dtype=float)
        self.current_pos = np.array(start_pos, dtype=float)
        self.duration = duration
        self.elapsed_time = 0

    def update(self, dt):
        self.elapsed_time += dt
        t = min(self.elapsed_time / self.duration, 1)  # Progress between 0 and 1
        self.current_pos = self.start_pos + t * (self.end_pos - self.start_pos)

# Generate point-light positions for "sitting down"
def generate_sitting_down_animation():
    points = []
    
    # Initial positions of body joints (standing frame)
    initial_positions = [
        (400, 100),  # Head
        (380, 150), (420, 150),  # Shoulders
        (360, 200), (440, 200),  # Elbows
        (340, 250), (460, 250),  # Hands
        (380, 300), (420, 300),  # Hips
        (370, 350), (430, 350),  # Knees
        (360, 450), (440, 450),  # Feet
        (380, 500), (420, 500),  # Floor projection for sitting
    ]
    
    # Final positions (sitting frame)
    final_positions = [
        (400, 150),  # Head moves slightly down
        (380, 200), (420, 200),  # Shoulders lower
        (360, 250), (440, 250),  # Elbows lower
        (340, 300), (460, 300),  # Hands lower
        (380, 400), (420, 400),  # Hips move closer to knees
        (370, 450), (430, 450),  # Knees bend
        (360, 500), (440, 500),  # Feet shift slightly forward
        (380, 500), (420, 500),  # Floor projection remains in place for sitting
    ]
    
    duration = 2.0  # Animation duration in seconds
    
    for start, end in zip(initial_positions, final_positions):
        points.append(PointLight(start, end, duration))
    
    return points

# Main loop
def main():
    clock = pygame.time.Clock()
    points = generate_sitting_down_animation()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update points
        dt = clock.get_time() / 1000  # Time elapsed in seconds
        for point in points:
            point.update(dt)
        
        # Draw the scene
        screen.fill(BACKGROUND_COLOR)
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, point.current_pos.astype(int), 5)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
