
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255255)

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define 15 point-lights representing key body joints
point_lights = [
    PointLight(400, 150, "head"),           # 1. Head
    PointLight(400, 200, "neck"),           # 2. Neck
    PointLight(380, 230, "l_shoulder"),     # 3. Left shoulder
    PointLight(420, 230, "r_shoulder"),     # 4. Right shoulder
    PointLight(370, 280, "l_elbow"),        # 5. Left elbow
    PointLight(430, 280, "r_elbow"),        # 6. Right elbow
    PointLight(365, 320, "l_wrist"),        # 7. Left wrist  
    PointLight(435, 320, "r_wrist"),        # 8. Right wrist
    PointLight(400, 300, "torso"),          # 9. Torso/spine
    PointLight(385, 380, "l_hip"),          # 10. Left hip
    PointLight(415, 380, "r_hip"),          # 11. Right hip
    PointLight(380, 450, "l_knee"),         # 12. Left knee
    PointLight(420, 450, "r_knee"),         # 13. Right knee
    PointLight(375, 520, "l_ankle"),        # 14. Left ankle
    PointLight(425, 520, "r_ankle")         # 15. Right ankle
]

def update_jumping_motion(frame, point_lights):
    # Jumping cycle parameters
    cycle_length = 120  # frames for complete jump cycle
    t = (frame % cycle_length) / cycle_length
    
    # Heavy, sad woman characteristics - slower, more labored movement
    jump_height = 40  # Reduced jump height due to heavy weight
    crouch_depth = 25  # How much she crouches before jumping
    
    # Phase-based motion
    if t < 0.3:  # Preparation/crouch phase (longer due to heaviness)
        phase = t / 0.3
        vertical_offset = -crouch_depth * math.sin(phase * math.pi / 2)
        arm_swing = -15 * phase
        knee_bend = 20 * phase
    elif t < 0.5:  # Takeoff phase
        phase = (t - 0.3) / 0.2
        vertical_offset = -crouch_depth + (crouch_depth + jump_height) * phase
        arm_swing = -15 + 30 * phase
        knee_bend = 20 * (1 - phase)
    elif t < 0.7:  # Peak/flight phase
        phase = (t - 0.5) / 0.2
        vertical_offset = jump_height * (1 - phase * 0.3)
        arm_swing = 15 - 20 * phase
        knee_bend = 0
    else:  # Landing phase (extended due to weight)
        phase = (t - 0.7) / 0.3
        vertical_offset = jump_height * 0.7 * (1 - phase) - crouch_depth * 0.5 * phase
        arm_swing = -5 * phase
        knee_bend = 15 * phase
    
    # Update each point light
    for light in point_lights:
        # Reset to base position
        light.x = light.base_x
        light.y = light.base_y
        
        # Apply vertical movement (jumping)
        if light.joint_name != "l_ankle" and light.joint_name != "r_ankle":
            light.y += vertical_offset
        
        # Joint-specific movements
        if light.joint_name == "head":
            light.y += vertical_offset * 1.1  # Head leads slightly
            light.y += math.sin(t * 6.28) * 2  # Slight bobbing
            
        elif light.joint_name in ["l_shoulder", "r_shoulder"]:
            # Shoulders move with torso and slight rotation
            shoulder_sway = math.sin(t * 6.28 * 2) * 3
            if light.joint_name == "l_shoulder":
                light.x += shoulder_sway
            else:
                light.x -= shoulder_sway
                
        elif light.joint_name in ["l_elbow", "r_elbow"]:
            # Arms swing during jump
            if light.joint_name == "l_elbow":
                light.x += arm_swing
                light.y += arm_swing * 0.3
            else:
                light.x -= arm_swing
                light.y += arm_swing * 0.3
                
        elif light.joint_name in ["l_wrist", "r_wrist"]:
            # Wrists follow elbows with additional swing
            if light.joint_name == "l_wrist":
                light.x += arm_swing * 1.5
                light.y += arm_swing * 0.5
            else:
                light.x -= arm_swing * 1.5
                light.y += arm_swing * 0.5
                
        elif light.joint_name in ["l_knee", "r_knee"]:
            # Knee bending during crouch and landing
            light.y += knee_bend
            # Slight inward movement when bending
            if light.joint_name == "l_knee":
                light.x += knee_bend * 0.3
            else:
                light.x -= knee_bend * 0.3
                
        elif light.joint_name in ["l_hip", "r_hip"]:
            # Hips move with slight rotation
            hip_rotation = math.sin(t * 6.28) * 2
            if light.joint_name == "l_hip":
                light.x += hip_rotation
            else:
                light.x -= hip_rotation
                
        elif light.joint_name in ["l_ankle", "r_ankle"]:
            # Ankles stay on ground longer, lift later
            if t < 0.4 or t > 0.75:  # On ground
                ankle_lift = 0
            else:  # In air
                ankle_lift = vertical_offset * 0.8
            light.y += ankle_lift
            
            # Slight foot positioning adjustment
            if light.joint_name == "l_ankle":
                light.x += knee_bend * 0.2
            else:
                light.x -= knee_bend * 0.2

def main():
    running = True
    frame = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Update motion
        update_jumping_motion(frame, point_lights)
        
        # Draw point lights
        for light in point_lights:
            pygame.draw.circle(screen, WHITE, (int(light.x), int(light.y)), 4)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()

if __name__ == "__main__":
    main()
