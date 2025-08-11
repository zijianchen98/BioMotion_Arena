
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Waving Hand")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 point-lights for a human figure
def create_human_points():
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    
    points = [
        PointLight(center_x, center_y - 120, "head"),           # 0
        PointLight(center_x, center_y - 90, "neck"),            # 1
        PointLight(center_x - 30, center_y - 70, "left_shoulder"), # 2
        PointLight(center_x + 30, center_y - 70, "right_shoulder"), # 3
        PointLight(center_x - 50, center_y - 30, "left_elbow"),  # 4
        PointLight(center_x + 50, center_y - 30, "right_elbow"), # 5
        PointLight(center_x - 70, center_y + 10, "left_hand"),   # 6
        PointLight(center_x + 70, center_y + 10, "right_hand"),  # 7
        PointLight(center_x, center_y - 30, "spine_upper"),      # 8
        PointLight(center_x, center_y + 20, "spine_lower"),      # 9
        PointLight(center_x - 20, center_y + 70, "left_hip"),    # 10
        PointLight(center_x + 20, center_y + 70, "right_hip"),   # 11
        PointLight(center_x - 25, center_y + 140, "left_knee"),  # 12
        PointLight(center_x + 25, center_y + 140, "right_knee"), # 13
        PointLight(center_x - 30, center_y + 210, "left_foot"),  # 14
        PointLight(center_x + 30, center_y + 210, "right_foot")  # 15
    ]
    
    return points[:15]  # Ensure exactly 15 points

def update_animation(points, frame):
    # Hand waving animation - focusing on right hand movement
    wave_amplitude = 40
    wave_frequency = 0.15
    
    # Slight body sway for sadness
    sad_sway = math.sin(frame * 0.05) * 3
    
    for i, point in enumerate(points):
        # Reset to base position
        point.x = point.base_x + sad_sway
        point.y = point.base_y
        
        # Right hand waving motion (more prominent)
        if point.joint_name == "right_hand":
            wave_motion = math.sin(frame * wave_frequency) * wave_amplitude
            point.x = point.base_x + wave_motion + 20
            point.y = point.base_y - abs(wave_motion) * 0.3
            
        # Right elbow follows hand motion (reduced)
        elif point.joint_name == "right_elbow":
            wave_motion = math.sin(frame * wave_frequency) * (wave_amplitude * 0.4)
            point.x = point.base_x + wave_motion + 10
            point.y = point.base_y - abs(wave_motion) * 0.2
            
        # Right shoulder slight movement
        elif point.joint_name == "right_shoulder":
            wave_motion = math.sin(frame * wave_frequency) * 5
            point.x = point.base_x + wave_motion + sad_sway
            point.y = point.base_y - abs(wave_motion) * 0.1
            
        # Head slight nodding for sadness
        elif point.joint_name == "head":
            nod = math.sin(frame * 0.08) * 2
            point.y = point.base_y + nod + sad_sway * 0.5
            
        # Subtle breathing motion for torso
        elif point.joint_name in ["neck", "spine_upper", "spine_lower"]:
            breath = math.sin(frame * 0.12) * 1
            point.y = point.base_y + breath
            
        # Left hand slight movement (less active, showing sadness)
        elif point.joint_name == "left_hand":
            subtle_motion = math.sin(frame * 0.07) * 5
            point.y = point.base_y + subtle_motion
            
        # Weight shifting for sad posture
        elif point.joint_name in ["left_hip", "right_hip", "left_knee", "right_knee", "left_foot", "right_foot"]:
            weight_shift = math.sin(frame * 0.04) * 2
            point.x = point.base_x + weight_shift + sad_sway * 0.7

def draw_points(screen, points):
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), POINT_RADIUS)

def main():
    points = create_human_points()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        update_animation(points, frame)
        draw_points(screen, points)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
