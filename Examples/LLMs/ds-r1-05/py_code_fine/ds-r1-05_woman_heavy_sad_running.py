
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

def get_positions(t):
    positions = []
    torso_x = WIDTH // 2
    torso_y = HEIGHT // 2 + 30 * math.sin(t * 0.4)  # Heavy vertical movement

    # Head and neck
    head_x, head_y = torso_x, torso_y - 60
    neck_x, neck_y = torso_x, torso_y - 40

    # Shoulders
    shoulder_lx, shoulder_ly = torso_x - 35, torso_y - 25
    shoulder_rx, shoulder_ry = torso_x + 35, torso_y - 25

    # Hips
    hip_lx, hip_ly = torso_x - 25, torso_y + 45
    hip_rx, hip_ry = torso_x + 25, torso_y + 45

    # Leg motion parameters
    leg_speed = 2.2  # Slower speed for heavy movement
    phase_left = (t * leg_speed) % (2 * math.pi)
    phase_right = phase_left + math.pi

    # Left leg calculations
    if phase_left < math.pi:
        foot_lx = hip_lx + 55 * (1 - math.cos(phase_left)) / 2
        foot_ly = hip_ly - 80 * math.sin(phase_left)
    else:
        foot_lx = hip_lx - 50 * (phase_left - math.pi) / math.pi
        foot_ly = hip_ly
    knee_lx = (hip_lx + foot_lx)/2
    knee_ly = (hip_ly + foot_ly)/2 - 25

    # Right leg calculations
    if phase_right < math.pi:
        foot_rx = hip_rx + 55 * (1 - math.cos(phase_right)) / 2
        foot_ry = hip_ry - 80 * math.sin(phase_right)
    else:
        foot_rx = hip_rx - 50 * (phase_right - math.pi) / math.pi
        foot_ry = hip_ry
    knee_rx = (hip_rx + foot_rx)/2
    knee_ry = (hip_ry + foot_ry)/2 - 25

    # Arm motion parameters (opposite phase to legs)
    arm_phase_left = phase_left + math.pi
    arm_phase_right = phase_right + math.pi

    # Left arm calculations
    elbow_lx = shoulder_lx - 40 * (1 - math.cos(arm_phase_left)) / 2
    elbow_ly = shoulder_ly + 50 * math.sin(arm_phase_left)
    hand_lx = elbow_lx - 25
    hand_ly = elbow_ly + 40

    # Right arm calculations
    elbow_rx = shoulder_rx + 40 * (1 - math.cos(arm_phase_right)) / 2
    elbow_ry = shoulder_ry + 50 * math.sin(arm_phase_right)
    hand_rx = elbow_rx + 25
    hand_ry = elbow_ry + 40

    positions = [
        (head_x, head_y), (neck_x, neck_y),
        (shoulder_lx, shoulder_ly), (shoulder_rx, shoulder_ry),
        (elbow_lx, elbow_ly), (elbow_rx, elbow_ry),
        (hand_lx, hand_ly), (hand_rx, hand_ry),
        (torso_x, torso_y), (hip_lx, hip_ly),
        (hip_rx, hip_ry), (knee_lx, knee_ly),
        (knee_rx, knee_ry), (foot_lx, foot_ly),
        (foot_rx, foot_ry)
    ]
    return positions

running = True
t = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    positions = get_positions(t)
    
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)
    
    pygame.display.flip()
    clock.tick(FPS)
    t += 1/FPS

pygame.quit()
sys.exit()
