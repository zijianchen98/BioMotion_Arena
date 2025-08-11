
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Running")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
speed = 0.08
torso_amplitude = 15
leg_amplitude = 40
arm_amplitude = 30
knee_amplitude = 25
ankle_amplitude = 15

def get_positions(t):
    # Base positions relative to center
    base = {
        'head': (0, -120),
        'shoulders': [(-40, -80), (40, -80)],
        'elbows': [(-60, -60), (60, -60)],
        'hands': [(-80, -40), (80, -40)],
        'hips': [(-30, 0), (30, 0)],
        'knees': [(-20, 30), (20, 30)],
        'ankles': [(-20, 60), (20, 60)],
        'torso_center': (0, -40),
        'mid_hip': (0, 0)
    }
    
    # Calculate dynamic offsets
    torso_dy = -torso_amplitude * math.sin(t)
    arm_phase = math.pi  # Arms opposite to legs
    
    positions = []
    
    # Head (slight vertical movement)
    positions.append((
        base['head'][0],
        base['head'][1] + torso_dy//2
    ))
    
    # Shoulders (move with torso)
    for x, y in base['shoulders']:
        positions.append((x, y + torso_dy))
    
    # Arms (opposite phase to legs)
    for i, (x, y) in enumerate(base['elbows']):
        dx = arm_amplitude * math.sin(t + arm_phase if i == 0 else t + arm_phase + math.pi)
        positions.append((x + dx, y + torso_dy))
    
    # Hands follow elbows
    for i, (x, y) in enumerate(base['hands']):
        dx = arm_amplitude * 1.2 * math.sin(t + arm_phase if i == 0 else t + arm_phase + math.pi)
        positions.append((x + dx, y + torso_dy))
    
    # Hips (move with torso)
    for x, y in base['hips']:
        positions.append((x, y + torso_dy))
    
    # Legs (alternating phase)
    for i, (x, y) in enumerate(base['knees']):
        dx = leg_amplitude * math.sin(t if i == 1 else t + math.pi)
        dy = -knee_amplitude * math.sin(t if i == 1 else t + math.pi)
        positions.append((x + dx, y + dy + torso_dy))
    
    # Ankles follow knees
    for i, (x, y) in enumerate(base['ankles']):
        dx = leg_amplitude * 1.2 * math.sin(t if i == 1 else t + math.pi)
        dy = -ankle_amplitude * math.sin(t if i == 1 else t + math.pi)
        positions.append((x + dx, y + dy + torso_dy))
    
    # Torso and mid-hip
    positions.append((base['torso_center'][0], base['torso_center'][1] + torso_dy))
    positions.append(base['mid_hip'])
    
    return positions

# Main animation loop
t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    # Get current positions
    points = get_positions(t)
    
    # Draw points (convert to screen coordinates)
    for x, y in points:
        pygame.draw.circle(screen, WHITE, 
                         (int(width/2 + x), int(height/2 + y)), 6)
    
    pygame.display.flip()
    clock.tick(30)
    t += speed

pygame.quit()
sys.exit()
