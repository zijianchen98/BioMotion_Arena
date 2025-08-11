
import pygame
import sys
import math

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping")
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
base_y = height // 2
jump_height = 60
phase = 0.0
phase_increment = 0.02

# Body dimensions
body_points = {
    'head': (0, -50),
    'neck': (0, -30),
    'l_shoulder': (-40, -30),
    'r_shoulder': (40, -30),
    'l_elbow': (-40, 0),
    'r_elbow': (40, 0),
    'l_wrist': (-40, 30),
    'r_wrist': (40, 30),
    'torso': (0, 0),
    'l_hip': (-30, 30),
    'r_hip': (30, 30),
    'l_knee': (-30, 70),
    'r_knee': (30, 70),
    'l_ankle': (-30, 110),
    'r_ankle': (30, 110)
}

def calculate_positions(phase):
    torso_y = base_y - jump_height * 4 * phase * (1 - phase)
    arm_angle = math.sin(phase * 2 * math.pi) * math.pi/3
    leg_angle = math.sin(phase * 2 * math.pi + math.pi) * math.pi/4

    points = []
    
    # Upper body
    points.append((width//2 + body_points['head'][0], torso_y + body_points['head'][1]))
    points.append((width//2 + body_points['neck'][0], torso_y + body_points['neck'][1]))
    
    # Arms
    l_shoulder = (width//2 + body_points['l_shoulder'][0], torso_y + body_points['l_shoulder'][1])
    r_shoulder = (width//2 + body_points['r_shoulder'][0], torso_y + body_points['r_shoulder'][1])
    
    points.append(l_shoulder)
    points.append(r_shoulder)
    
    l_elbow = (l_shoulder[0] + 50 * math.cos(arm_angle),
               l_shoulder[1] + 50 * math.sin(arm_angle))
    r_elbow = (r_shoulder[0] - 50 * math.cos(arm_angle),
               r_shoulder[1] + 50 * math.sin(arm_angle))
    
    points.append(l_elbow)
    points.append(r_elbow)
    
    points.append((l_elbow[0] + 40 * math.cos(arm_angle - math.pi/2),
                   l_elbow[1] + 40 * math.sin(arm_angle - math.pi/2)))
    points.append((r_elbow[0] - 40 * math.cos(arm_angle - math.pi/2),
                   r_elbow[1] + 40 * math.sin(arm_angle - math.pi/2)))
    
    # Torso
    points.append((width//2, torso_y))
    
    # Legs
    l_hip = (width//2 + body_points['l_hip'][0], torso_y + body_points['l_hip'][1])
    r_hip = (width//2 + body_points['r_hip'][0], torso_y + body_points['r_hip'][1])
    
    points.append(l_hip)
    points.append(r_hip)
    
    l_knee = (l_hip[0] + 60 * math.cos(leg_angle),
              l_hip[1] + 60 * math.sin(leg_angle))
    r_knee = (r_hip[0] - 60 * math.cos(leg_angle),
              r_hip[1] + 60 * math.sin(leg_angle))
    
    points.append(l_knee)
    points.append(r_knee)
    
    points.append((l_knee[0] + 60 * math.cos(leg_angle - math.pi/2),
                   l_knee[1] + 60 * math.sin(leg_angle - math.pi/2)))
    points.append((r_knee[0] - 60 * math.cos(leg_angle - math.pi/2),
                   r_knee[1] + 60 * math.sin(leg_angle - math.pi/2)))
    
    return points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Update animation phase
    phase += phase_increment
    if phase >= 1.0:
        phase -= 1.0
    
    # Get current frame points
    points = calculate_positions(phase)
    
    # Draw points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
