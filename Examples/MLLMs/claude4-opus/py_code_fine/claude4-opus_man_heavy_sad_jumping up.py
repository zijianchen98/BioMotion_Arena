
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Heavy Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define 15 point-lights representing human body joints
def create_body_points():
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    points = [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 100, "neck"),
        PointLight(center_x - 20, center_y - 80, "left_shoulder"),
        PointLight(center_x + 20, center_y - 80, "right_shoulder"),
        PointLight(center_x - 35, center_y - 50, "left_elbow"),
        PointLight(center_x + 35, center_y - 50, "right_elbow"),
        PointLight(center_x - 45, center_y - 20, "left_wrist"),
        PointLight(center_x + 45, center_y - 20, "right_wrist"),
        PointLight(center_x, center_y - 60, "torso"),
        PointLight(center_x, center_y - 20, "pelvis"),
        PointLight(center_x - 15, center_y + 20, "left_hip"),
        PointLight(center_x + 15, center_y + 20, "right_hip"),
        PointLight(center_x - 18, center_y + 60, "left_knee"),
        PointLight(center_x + 18, center_y + 60, "right_knee"),
        PointLight(center_x - 20, center_y + 100, "left_ankle"),
        PointLight(center_x + 20, center_y + 100, "right_ankle")
    ]
    return points

def update_jumping_motion(points, frame):
    # Heavy jumping motion with multiple phases
    cycle_length = 120
    t = (frame % cycle_length) / cycle_length
    
    # Jumping phases: preparation, takeoff, flight, landing
    if t < 0.3:  # Preparation phase (crouching down heavily)
        phase = t / 0.3
        crouch_factor = math.sin(phase * math.pi) * 0.4
        
        for point in points:
            if point.joint_name in ["left_knee", "right_knee"]:
                point.y = point.base_y + crouch_factor * 40
            elif point.joint_name in ["left_ankle", "right_ankle"]:
                point.y = point.base_y + crouch_factor * 20
            elif point.joint_name == "pelvis":
                point.y = point.base_y + crouch_factor * 50
            elif point.joint_name in ["torso", "neck", "head"]:
                point.y = point.base_y + crouch_factor * 60
            elif point.joint_name in ["left_shoulder", "right_shoulder"]:
                point.y = point.base_y + crouch_factor * 55
            elif point.joint_name in ["left_elbow", "right_elbow"]:
                point.y = point.base_y + crouch_factor * 45
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * crouch_factor * 15
            elif point.joint_name in ["left_wrist", "right_wrist"]:
                point.y = point.base_y + crouch_factor * 35
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * crouch_factor * 25
            elif point.joint_name in ["left_hip", "right_hip"]:
                point.y = point.base_y + crouch_factor * 45
                
    elif t < 0.5:  # Takeoff phase
        phase = (t - 0.3) / 0.2
        extension = math.sin(phase * math.pi) * 0.8
        
        for point in points:
            if point.joint_name in ["left_knee", "right_knee"]:
                point.y = point.base_y + 16 - extension * 25
            elif point.joint_name in ["left_ankle", "right_ankle"]:
                point.y = point.base_y + 8 - extension * 15
            elif point.joint_name == "pelvis":
                point.y = point.base_y + 20 - extension * 35
            elif point.joint_name in ["torso", "neck", "head"]:
                point.y = point.base_y + 24 - extension * 45
            elif point.joint_name in ["left_elbow", "right_elbow"]:
                point.y = point.base_y + 18 - extension * 40
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * (6 - extension * 20)
            elif point.joint_name in ["left_wrist", "right_wrist"]:
                point.y = point.base_y + 14 - extension * 35
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * (10 - extension * 35)
                
    elif t < 0.8:  # Flight phase (airborne)
        phase = (t - 0.5) / 0.3
        flight_height = math.sin(phase * math.pi) * 60
        
        for point in points:
            point.y = point.base_y - flight_height
            
            # Slight body positioning adjustments during flight
            if point.joint_name in ["left_knee", "right_knee"]:
                point.y += 5
            elif point.joint_name in ["left_ankle", "right_ankle"]:
                point.y += 10
            elif point.joint_name in ["left_elbow", "right_elbow"]:
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * 10
            elif point.joint_name in ["left_wrist", "right_wrist"]:
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * 15
                
    else:  # Landing phase
        phase = (t - 0.8) / 0.2
        landing_impact = math.sin(phase * math.pi) * 0.6
        
        for point in points:
            if point.joint_name in ["left_knee", "right_knee"]:
                point.y = point.base_y + landing_impact * 25
            elif point.joint_name in ["left_ankle", "right_ankle"]:
                point.y = point.base_y + landing_impact * 12
            elif point.joint_name == "pelvis":
                point.y = point.base_y + landing_impact * 35
            elif point.joint_name in ["torso", "neck", "head"]:
                point.y = point.base_y + landing_impact * 40
            elif point.joint_name in ["left_elbow", "right_elbow"]:
                point.y = point.base_y + landing_impact * 30
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * landing_impact * 12
            elif point.joint_name in ["left_wrist", "right_wrist"]:
                point.y = point.base_y + landing_impact * 25
                point.x = point.base_x + (1 if "right" in point.joint_name else -1) * landing_impact * 20

def main():
    points = create_body_points()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Clear screen
        screen.fill(BLACK)
        
        # Update motion
        update_jumping_motion(points, frame)
        
        # Draw point-lights
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), 4)
        
        pygame.display.flip()
        clock.tick(30)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
