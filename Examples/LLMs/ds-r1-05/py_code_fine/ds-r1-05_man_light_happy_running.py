
import pygame
import math
import time

def main():
    # Initialize pygame
    pygame.init()
    
    # Screen dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Running Point-Light Display")
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Time parameters
    clock = pygame.time.Clock()
    t = 0.0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Core body parameters
        core_x = width // 2
        core_y = height // 2 + 20 * math.sin(2 * math.pi * 1.5 * t)
        
        # Head
        head_y = core_y - 90
        
        # Shoulders
        shoulder_offset = 35
        shoulder_phase = 0.3 * math.sin(3 * math.pi * t)
        l_shoulder_x = core_x - shoulder_offset + 7 * math.sin(2.2 * t)
        r_shoulder_x = core_x + shoulder_offset + 7 * math.sin(2.2 * t + 0.5)
        l_shoulder_y = core_y - 70 + 3 * math.sin(3 * t)
        r_shoulder_y = core_y - 70 + 3 * math.sin(3 * t + 0.5)
        
        # Elbows
        arm_phase = 0.8 * math.sin(4 * math.pi * t)
        l_elbow_x = l_shoulder_x - 35 * math.sin(1.5 * arm_phase + math.pi)
        l_elbow_y = l_shoulder_y + 35 * math.cos(1.5 * arm_phase + math.pi)
        r_elbow_x = r_shoulder_x - 35 * math.sin(1.5 * arm_phase)
        r_elbow_y = r_shoulder_y + 35 * math.cos(1.5 * arm_phase)
        
        # Wrists
        l_wrist_x = l_elbow_x - 25 * math.sin(2.0 * arm_phase + math.pi)
        l_wrist_y = l_elbow_y + 25 * math.cos(2.0 * arm_phase + math.pi)
        r_wrist_x = r_elbow_x - 25 * math.sin(2.0 * arm_phase)
        r_wrist_y = r_elbow_y + 25 * math.cos(2.0 * arm_phase)
        
        # Hips
        hip_sway = 8 * math.sin(3 * math.pi * t + math.pi)
        l_hip_x = core_x - 22 + hip_sway
        r_hip_x = core_x + 22 + hip_sway
        l_hip_y = core_y + 5
        r_hip_y = core_y + 5
        
        # Knees
        leg_phase = 0.8 * math.sin(4 * math.pi * t)
        l_knee_x = l_hip_x - 30 * math.sin(1.5 * leg_phase + math.pi)
        l_knee_y = l_hip_y + 40 * math.cos(1.5 * leg_phase + math.pi)
        r_knee_x = r_hip_x - 30 * math.sin(1.5 * leg_phase)
        r_knee_y = r_hip_y + 40 * math.cos(1.5 * leg_phase)
        
        # Ankles
        ankle_spring = 0.4 * math.sin(8 * math.pi * t)
        l_ankle_x = l_knee_x - 40 * math.sin(1.5 * (leg_phase + ankle_spring) + math.pi)
        l_ankle_y = l_knee_y + 40 * math.cos(1.5 * (leg_phase + ankle_spring) + math.pi)
        r_ankle_x = r_knee_x - 40 * math.sin(1.5 * (leg_phase + ankle_spring))
        r_ankle_y = r_knee_y + 40 * math.cos(1.5 * (leg_phase + ankle_spring))
        
        # Feet
        l_foot_x = l_ankle_x - 25
        l_foot_y = l_ankle_y + 3
        r_foot_x = r_ankle_x - 25
        r_foot_y = r_ankle_y + 3
        
        # Body points: head, shoulders, elbows, wrists, hips, knees, ankles, feet
        points = [
            (core_x, head_y),            # Head
            (l_shoulder_x, l_shoulder_y), # Left shoulder
            (r_shoulder_x, r_shoulder_y), # Right shoulder
            (l_elbow_x, l_elbow_y),       # Left elbow
            (r_elbow_x, r_elbow_y),       # Right elbow
            (l_wrist_x, l_wrist_y),       # Left wrist
            (r_wrist_x, r_wrist_y),       # Right wrist
            (l_hip_x, l_hip_y),           # Left hip
            (r_hip_x, r_hip_y),           # Right hip
            (l_knee_x, l_knee_y),         # Left knee
            (r_knee_x, r_knee_y),         # Right knee
            (l_ankle_x, l_ankle_y),       # Left ankle
            (r_ankle_x, r_ankle_y),       # Right ankle
            (l_foot_x, l_foot_y),         # Left foot
            (r_foot_x, r_foot_y)          # Right foot
        ]
        
        # Draw all points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 7)
        
        # Update display
        pygame.display.flip()
        
        # Update time
        t += 0.016  # Increment time (approx 60 FPS)
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
