
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Hand Waving")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, radius=4):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.radius = radius

# Define the 15 key points for human body (simplified)
def create_body_points():
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    
    points = [
        PointLight(center_x, center_y - 150),  # 0: Head
        PointLight(center_x, center_y - 120), # 1: Neck
        PointLight(center_x - 40, center_y - 90),  # 2: Left shoulder
        PointLight(center_x + 40, center_y - 90),  # 3: Right shoulder
        PointLight(center_x - 50, center_y - 40),  # 4: Left elbow
        PointLight(center_x + 50, center_y - 40),  # 5: Right elbow
        PointLight(center_x - 60, center_y + 10),  # 6: Left hand
        PointLight(center_x + 60, center_y + 10),  # 7: Right hand (waving)
        PointLight(center_x, center_y - 50),       # 8: Chest
        PointLight(center_x, center_y + 20),       # 9: Waist
        PointLight(center_x - 20, center_y + 80),  # 10: Left hip
        PointLight(center_x + 20, center_y + 80),  # 11: Right hip
        PointLight(center_x - 25, center_y + 140), # 12: Left knee
        PointLight(center_x + 25, center_y + 140), # 13: Right knee
        PointLight(center_x - 30, center_y + 200), # 14: Left foot
    ]
    
    # Add right foot as 15th point
    points.append(PointLight(center_x + 30, center_y + 200))  # 15: Right foot
    
    return points[:15]  # Ensure exactly 15 points

def update_waving_motion(points, time):
    # Hand waving parameters
    wave_amplitude = 40
    wave_frequency = 0.1
    wave_speed = 0.15
    
    # Heavy weight effect - slightly slower, more deliberate motion
    heavy_factor = 0.8
    
    # Calculate wave motion
    wave_offset = math.sin(time * wave_speed * heavy_factor) * wave_amplitude
    vertical_wave = math.sin(time * wave_speed * heavy_factor * 1.5) * 15
    
    # Right hand waving motion (point 7)
    points[7].x = points[7].base_x + wave_offset
    points[7].y = points[7].base_y + vertical_wave
    
    # Right elbow follows hand motion but dampened
    elbow_damping = 0.4
    points[5].x = points[5].base_x + wave_offset * elbow_damping
    points[5].y = points[5].base_y + vertical_wave * elbow_damping
    
    # Right shoulder subtle movement
    shoulder_damping = 0.2
    points[3].x = points[3].base_x + wave_offset * shoulder_damping
    points[3].y = points[3].base_y + vertical_wave * shoulder_damping
    
    # Body sway due to heavy weight
    body_sway = math.sin(time * wave_speed * 0.5) * 5
    
    # Apply subtle body movement to show weight
    for i in [0, 1, 8, 9]:  # Head, neck, chest, waist
        points[i].x = points[i].base_x + body_sway
    
    # Leg stability with slight weight shift
    leg_shift = math.sin(time * wave_speed * 0.3) * 3
    for i in [10, 12, 14]:  # Left leg points
        points[i].x = points[i].base_x - leg_shift
    for i in [11, 13, 15]:  # Right leg points (if exists)
        if i < len(points):
            points[i].x = points[i].base_x + leg_shift
    
    # Left arm subtle counter-movement
    left_counter = wave_offset * -0.1
    points[4].x = points[4].base_x + left_counter  # Left elbow
    points[6].x = points[6].base_x + left_counter  # Left hand
    
    # Breathing effect on chest
    breathing = math.sin(time * 0.05) * 2
    points[8].y = points[8].base_y + breathing

def main():
    points = create_body_points()
    time = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update animation
        update_waving_motion(points, time)
        time += 1
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), point.radius)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
