
import pygame
import math
import sys

def calculate_positions(t):
    points = []
    # Vertical center with jump motion (sine wave)
    y_center = 300 + 50 * math.sin(t * 0.12)
    
    # Head (1)
    points.append((400, y_center - 60))
    
    # Shoulders (2)
    shoulder_phase = math.sin(t * 0.15)
    points.append((400 - 35 - shoulder_phase*8, y_center - 30))
    points.append((400 + 35 + shoulder_phase*8, y_center - 30))
    
    # Arms (4: elbows and hands)
    arm_phase = math.sin(t * 0.18 + 0.5)
    points.append((400 - 50 - arm_phase*25, y_center - 20 + abs(arm_phase)*30))  # Left elbow
    points.append((400 + 50 + arm_phase*25, y_center - 20 + abs(arm_phase)*30))  # Right elbow
    points.append((400 - 65 - arm_phase*40, y_center + 10 + arm_phase*30))       # Left hand
    points.append((400 + 65 + arm_phase*40, y_center + 10 + arm_phase*30))       # Right hand
    
    # Hips (2)
    points.append((400 - 25, y_center + 20))
    points.append((400 + 25, y_center + 20))
    
    # Legs (6: knees, ankles, feet)
    leg_phase = math.sin(t * 0.12 + math.pi/1.8)
    knee_offset = 25 * leg_phase
    ankle_offset = 40 * leg_phase
    points.append((400 - 25, y_center + 60 + knee_offset))   # Left knee
    points.append((400 + 25, y_center + 60 + knee_offset))   # Right knee
    points.append((400 - 30, y_center + 100 + ankle_offset)) # Left ankle
    points.append((400 + 30, y_center + 100 + ankle_offset)) # Right ankle
    points.append((400 - 35, y_center + 120 + ankle_offset)) # Left foot
    points.append((400 + 35, y_center + 120 + ankle_offset)) # Right foot
    
    return points

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Biological Motion - Jumping Woman")
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        t = pygame.time.get_ticks() / 85  # Time parameter for animation
        screen.fill((0, 0, 0))
        
        # Get and draw all points
        for x, y in calculate_positions(t):
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 6)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
