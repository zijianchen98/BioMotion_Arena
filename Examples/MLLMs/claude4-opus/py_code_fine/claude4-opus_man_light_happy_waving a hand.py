
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_RADIUS = 8

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Hand Waving")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 body points for a human figure
def create_body_points():
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    
    points = [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 80, "neck"),
        PointLight(center_x - 30, center_y - 60, "left_shoulder"),
        PointLight(center_x + 30, center_y - 60, "right_shoulder"),
        PointLight(center_x - 50, center_y - 30, "left_elbow"),
        PointLight(center_x + 50, center_y - 30, "right_elbow"),
        PointLight(center_x - 70, center_y, "left_wrist"),
        PointLight(center_x + 70, center_y, "right_wrist"),
        PointLight(center_x, center_y - 40, "spine_upper"),
        PointLight(center_x, center_y, "spine_mid"),
        PointLight(center_x, center_y + 40, "hip_center"),
        PointLight(center_x - 20, center_y + 80, "left_knee"),
        PointLight(center_x + 20, center_y + 80, "right_knee"),
        PointLight(center_x - 25, center_y + 120, "left_foot"),
        PointLight(center_x + 25, center_y + 120, "right_foot")
    ]
    
    return points

def update_hand_wave_animation(points, frame):
    # Reset all points to base positions
    for point in points:
        point.x = point.base_x
        point.y = point.base_y
    
    # Calculate wave motion
    wave_angle = (frame * 0.3) % (2 * math.pi)
    wave_amplitude = 40
    
    # Add subtle body sway
    body_sway = math.sin(frame * 0.1) * 5
    
    # Apply body sway to torso points
    torso_joints = ["head", "neck", "left_shoulder", "right_shoulder", 
                   "spine_upper", "spine_mid"]
    
    for point in points:
        if point.joint_name in torso_joints:
            point.x += body_sway
    
    # Animate right arm waving (main motion)
    for point in points:
        if point.joint_name == "right_shoulder":
            # Shoulder moves slightly with wave
            point.y += math.sin(wave_angle) * 15
            
        elif point.joint_name == "right_elbow":
            # Elbow creates the main waving arc
            point.x = point.base_x + math.sin(wave_angle) * wave_amplitude
            point.y = point.base_y + math.cos(wave_angle) * 20 - 10
            
        elif point.joint_name == "right_wrist":
            # Wrist follows elbow with extended motion
            elbow_offset_x = math.sin(wave_angle) * wave_amplitude
            elbow_offset_y = math.cos(wave_angle) * 20 - 10
            
            # Additional wrist extension
            wrist_extension = math.sin(wave_angle * 1.5) * 25
            point.x = point.base_x + elbow_offset_x + wrist_extension
            point.y = point.base_y + elbow_offset_y + math.cos(wave_angle * 1.2) * 15
    
    # Add subtle left arm counter-movement for balance
    for point in points:
        if point.joint_name == "left_elbow":
            point.x += math.sin(wave_angle + math.pi) * 8
            
        elif point.joint_name == "left_wrist":
            point.x += math.sin(wave_angle + math.pi) * 12
    
    # Add slight head movement following the wave
    for point in points:
        if point.joint_name == "head":
            point.x += math.sin(wave_angle * 0.5) * 8
            point.y += math.cos(wave_angle * 0.3) * 5

def main():
    points = create_body_points()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update animation
        update_hand_wave_animation(points, frame)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
