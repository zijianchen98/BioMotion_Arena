
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize point positions
points = [
    # Body points (6)
    {'pos': (width/2, height/2 - 100)},  # head
    {'pos': (width/2, height/2 - 80)},    # neck
    {'pos': (width/2, height/2 - 60)},    # chest
    {'pos': (width/2, height/2 - 40)},    # waist
    {'pos': (width/2 - 30, height/2 - 20)},  # left hip
    {'pos': (width/2 + 30, height/2 - 20)},  # right hip

    # Right arm (6 points)
    {'pos': (width/2 - 50, height/2 - 60)},  # shoulder
    {'pos': (0, 0)},  # elbow (calculated)
    {'pos': (0, 0)},  # wrist (calculated)
    {'pos': (0, 0)},  # hand 1 (calculated)
    {'pos': (0, 0)},  # hand 2 (calculated)
    {'pos': (0, 0)},  # hand 3 (calculated)

    # Left arm (3 points)
    {'pos': (width/2 + 50, height/2 - 60)},  # shoulder
    {'pos': (width/2 + 50, height/2 - 30)},  # elbow
    {'pos': (width/2 + 50, height/2)}        # wrist
]

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    t = pygame.time.get_ticks() / 1000  # Get time in seconds

    # Update body positions with slight vertical movement
    head_y = height/2 - 100 + 5 * math.sin(t)
    points[0]['pos'] = (width/2, head_y)
    points[1]['pos'] = (width/2, head_y + 20)
    points[2]['pos'] = (width/2, head_y + 40)
    points[3]['pos'] = (width/2, head_y + 60)
    points[4]['pos'] = (width/2 - 30, head_y + 80)
    points[5]['pos'] = (width/2 + 30, head_y + 80)

    # Calculate right arm kinematics
    shoulder_x, shoulder_y = points[6]['pos']
    upper_arm = 50
    lower_arm = 50
    
    # Upper arm movement
    theta = math.radians(90) + 0.5 * math.sin(t * 3)
    elbow_x = shoulder_x + upper_arm * math.cos(theta)
    elbow_y = shoulder_y + upper_arm * math.sin(theta)
    points[7]['pos'] = (elbow_x, elbow_y)
    
    # Lower arm movement
    phi = math.radians(-90) + 0.8 * math.sin(t * 3 + math.pi/2)
    wrist_x = elbow_x + lower_arm * math.cos(phi)
    wrist_y = elbow_y + lower_arm * math.sin(phi)
    points[8]['pos'] = (wrist_x, wrist_y)
    
    # Hand points movement
    hand_radius = 15
    angle = t * 6
    points[9]['pos'] = (wrist_x + hand_radius * math.cos(angle), wrist_y + hand_radius * math.sin(angle))
    points[10]['pos'] = (wrist_x + hand_radius * math.cos(angle + math.pi/2), wrist_y + hand_radius * math.sin(angle + math.pi/2))
    points[11]['pos'] = (wrist_x + hand_radius * math.cos(angle - math.pi/2), wrist_y + hand_radius * math.sin(angle - math.pi/2))

    # Draw all points
    for point in points:
        x, y = point['pos']
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
