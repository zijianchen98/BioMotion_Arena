
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Sad Woman Walking")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
fps = 30
clock = pygame.time.Clock()
period = 2.5  # Slower period for heavy movement
hip_amplitude_x = 20
hip_amplitude_y = 15
leg_amplitude = 60
arm_amplitude = 40
head_offset = -45  # Slightly slouched

def get_positions(t):
    hip_x = width/2 + hip_amplitude_x * math.sin(2 * math.pi * t / period)
    hip_y = height/2 + 50 + hip_amplitude_y * math.sin(4 * math.pi * t / period)
    
    head = (hip_x, hip_y + head_offset)
    
    # Shoulders
    shoulder_l = (hip_x - 40, hip_y - 20)
    shoulder_r = (hip_x + 40, hip_y - 20)
    
    # Arms (opposite phase to legs)
    arm_phase = math.pi
    arm_angle = arm_amplitude * math.sin(2 * math.pi * t / period + arm_phase)
    elbow_l = (shoulder_l[0] - arm_angle, shoulder_l[1] + 40)
    elbow_r = (shoulder_r[0] + arm_angle, shoulder_r[1] + 40)
    hand_l = (elbow_l[0] - arm_angle*0.7, elbow_l[1] + 40)
    hand_r = (elbow_r[0] + arm_angle*0.7, elbow_r[1] + 40)
    
    # Legs
    leg_angle = leg_amplitude * math.sin(2 * math.pi * t / period)
    knee_l = (hip_x - 25 + leg_angle, hip_y + 50 - abs(30 * math.sin(2 * math.pi * t / period)))
    knee_r = (hip_x + 25 - leg_angle, hip_y + 50 - abs(30 * math.sin(2 * math.pi * t / period + math.pi)))
    
    ankle_l = (knee_l[0] + leg_angle, knee_l[1] + 50 + 10 * math.sin(2 * math.pi * t / period))
    ankle_r = (knee_r[0] - leg_angle, knee_r[1] + 50 + 10 * math.sin(2 * math.pi * t / period + math.pi))
    
    foot_l = (ankle_l[0], ankle_l[1] + 15)
    foot_r = (ankle_r[0], ankle_r[1] + 15)
    
    return [
        head, shoulder_l, shoulder_r, elbow_l, elbow_r,
        hand_l, hand_r, (hip_x-15, hip_y+10), (hip_x+15, hip_y+10),
        knee_l, knee_r, ankle_l, ankle_r, foot_l, foot_r
    ]

# Main loop
t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    points = get_positions(t)
    
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    t += 1/fps
    clock.tick(fps)

pygame.quit()
sys.exit()
