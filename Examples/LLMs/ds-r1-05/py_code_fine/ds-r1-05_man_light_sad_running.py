
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
SPEED = 0.08
AMPLITUDE = 35

def calculate_positions(t):
    """Calculate positions of 15 body points based on time"""
    positions = []
    center_x, center_y = WIDTH//2, HEIGHT//2
    
    # Head (1 point)
    positions.append((center_x, center_y - 90 + 5 * math.sin(t * 0.8)))
    
    # Shoulders (2 points)
    positions.append((center_x - 40, center_y - 50 + 8 * math.sin(t + 5 * math.sin(t * 2))))
    positions.append((center_x + 40, center_y - 50 - 8 * math.sin(t) + 5 * math.sin(t * 2))))
    
    # Elbows (2 points)
    elbow_angle = t * 3
    positions.append((
        center_x - 40 - 30 * math.cos(elbow_angle),
        center_y - 50 + 30 * math.sin(elbow_angle)
    ))
    positions.append((
        center_x + 40 + 30 * math.cos(elbow_angle),
        center_y - 50 + 30 * math.sin(elbow_angle)
    ))
    
    # Hands (2 points)
    hand_angle = t * 3 + math.pi/1.7
    positions.append((
        positions[2][0] - 25 * math.cos(hand_angle),
        positions[2][1] + 25 * math.sin(hand_angle)
    ))
    positions.append((
        positions[3][0] + 25 * math.cos(hand_angle),
        positions[3][1] + 25 * math.sin(hand_angle)
    ))
    
    # Hips (2 points)
    hip_osc = 15 * math.sin(t * 1.2)
    positions.append((center_x - 25, center_y + 10 + hip_osc))
    positions.append((center_x + 25, center_y + 10 - hip_osc))
    
    # Knees (2 points)
    knee_angle = t * 4
    positions.append((
        positions[6][0] + 20 * math.cos(knee_angle),
        positions[6][1] + 40 * math.sin(knee_angle)
    ))
    positions.append((
        positions[7][0] - 20 * math.cos(knee_angle),
        positions[7][1] + 40 * math.sin(knee_angle)
    ))
    
    # Ankles (2 points)
    ankle_angle = t * 4 + math.pi/2
    positions.append((
        positions[8][0] + 15 * math.cos(ankle_angle),
        positions[8][1] + 30 * math.sin(ankle_angle)
    ))
    positions.append((
        positions[9][0] - 15 * math.cos(ankle_angle),
        positions[9][1] + 30 * math.sin(ankle_angle)
    ))
    
    # Feet (2 points)
    foot_angle = t * 4 + math.pi
    positions.append((
        positions[10][0] + 10 * math.cos(foot_angle),
        positions[10][1] + 10 * math.sin(foot_angle)
    ))
    positions.append((
        positions[11][0] - 10 * math.cos(foot_angle),
        positions[11][1] + 10 * math.sin(foot_angle)
    ))
    
    return positions

def main():
    clock = pygame.time.Clock()
    t = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        
        # Get current positions
        points = calculate_positions(t)
        
        # Draw all points
        for pos in points:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 6)
        
        pygame.display.flip()
        clock.tick(FPS)
        t += SPEED

if __name__ == "__main__":
    main()
