
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Woman Jumping Forward")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 point-lights for major body joints
def create_point_lights():
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    
    return [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 80, "neck"),
        PointLight(center_x - 30, center_y - 60, "left_shoulder"),
        PointLight(center_x + 30, center_y - 60, "right_shoulder"),
        PointLight(center_x - 45, center_y - 20, "left_elbow"),
        PointLight(center_x + 45, center_y - 20, "right_elbow"),
        PointLight(center_x - 50, center_y + 20, "left_wrist"),
        PointLight(center_x + 50, center_y + 20, "right_wrist"),
        PointLight(center_x, center_y - 40, "spine"),
        PointLight(center_x - 20, center_y + 20, "left_hip"),
        PointLight(center_x + 20, center_y + 20, "right_hip"),
        PointLight(center_x - 25, center_y + 80, "left_knee"),
        PointLight(center_x + 25, center_y + 80, "right_knee"),
        PointLight(center_x - 30, center_y + 140, "left_ankle"),
        PointLight(center_x + 30, center_y + 140, "right_ankle")
    ]

def update_jumping_motion(points, frame):
    # Jumping cycle parameters
    jump_duration = 90  # frames for complete jump cycle
    phase = (frame % jump_duration) / jump_duration
    
    # Create different phases of jumping
    if phase < 0.2:  # Preparation/crouch
        crouch_factor = 1 - (phase / 0.2) * 0.3
        vertical_offset = 0
        forward_offset = 0
        arm_swing = 0
    elif phase < 0.4:  # Takeoff
        crouch_factor = 0.7 + ((phase - 0.2) / 0.2) * 0.6
        vertical_offset = -((phase - 0.2) / 0.2) * 80
        forward_offset = ((phase - 0.2) / 0.2) * 50
        arm_swing = ((phase - 0.2) / 0.2) * 30
    elif phase < 0.7:  # Flight
        crouch_factor = 1.3
        flight_phase = (phase - 0.4) / 0.3
        vertical_offset = -80 + math.sin(flight_phase * math.pi) * 40
        forward_offset = 50 + flight_phase * 30
        arm_swing = 30 - flight_phase * 15
    else:  # Landing
        landing_phase = (phase - 0.7) / 0.3
        crouch_factor = 1.3 - landing_phase * 0.6
        vertical_offset = -40 + landing_phase * 40
        forward_offset = 80 - landing_phase * 20
        arm_swing = 15 - landing_phase * 15
    
    # Apply transformations to each point
    for point in points:
        # Reset to base position
        x, y = point.base_x, point.base_y
        
        # Apply forward movement
        x += forward_offset
        
        # Apply vertical movement and body compression
        if point.joint_name == "head":
            y += vertical_offset + (1 - crouch_factor) * 10
        elif point.joint_name == "neck":
            y += vertical_offset + (1 - crouch_factor) * 15
        elif point.joint_name in ["left_shoulder", "right_shoulder"]:
            y += vertical_offset + (1 - crouch_factor) * 20
        elif point.joint_name in ["left_elbow", "right_elbow"]:
            y += vertical_offset + (1 - crouch_factor) * 25
            # Arm swing
            if point.joint_name == "left_elbow":
                x -= arm_swing
            else:
                x += arm_swing
        elif point.joint_name in ["left_wrist", "right_wrist"]:
            y += vertical_offset + (1 - crouch_factor) * 30
            # Arm swing
            if point.joint_name == "left_wrist":
                x -= arm_swing * 1.5
            else:
                x += arm_swing * 1.5
        elif point.joint_name == "spine":
            y += vertical_offset + (1 - crouch_factor) * 20
        elif point.joint_name in ["left_hip", "right_hip"]:
            y += vertical_offset + (1 - crouch_factor) * 25
        elif point.joint_name in ["left_knee", "right_knee"]:
            y += vertical_offset + (1 - crouch_factor) * 40
            # Knee bend during crouch and landing
            if phase < 0.2 or phase > 0.7:
                y -= (1 - crouch_factor) * 15
        elif point.joint_name in ["left_ankle", "right_ankle"]:
            y += vertical_offset + (1 - crouch_factor) * 50
            # Ankle position during jump
            if phase < 0.2 or phase > 0.7:
                y -= (1 - crouch_factor) * 20
        
        # Add slight happiness bounce (subtle up-down motion)
        happiness_bounce = math.sin(frame * 0.3) * 2
        y += happiness_bounce
        
        # Add weight effect (slightly more pronounced movements)
        if point.joint_name in ["left_hip", "right_hip", "left_knee", "right_knee"]:
            weight_effect = math.sin(frame * 0.2) * 1.5
            y += weight_effect
        
        point.x = x
        point.y = y

def main():
    points = create_point_lights()
    frame = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update point positions
        update_jumping_motion(points, frame)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw point lights
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), 4)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
