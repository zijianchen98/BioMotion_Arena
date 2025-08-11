
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 30
JUMP_DURATION = 2  # seconds
GRAVITY = 0.5  # Adjusted for visual realism

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Initial positions
start_x = WIDTH * 0.2
start_y = HEIGHT * 0.7
jump_distance = WIDTH * 0.4
jump_height = HEIGHT * 0.2

def calculate_positions(t_normalized):
    base_x = start_x + jump_distance * t_normalized
    base_y = start_y - 4 * jump_height * t_normalized * (1 - t_normalized)
    
    points = []
    
    # Head
    points.append((base_x, base_y - 40))
    
    # Shoulders
    shoulder_offset = 25 + 10 * math.sin(2 * math.pi * t_normalized)
    points.append((base_x - shoulder_offset, base_y - 30))
    points.append((base_x + shoulder_offset, base_y - 30))
    
    # Arms
    arm_phase = math.pi * t_normalized
    left_elbow_y = base_y - 20 + 30 * math.sin(arm_phase)
    right_elbow_y = base_y - 20 + 30 * math.sin(arm_phase)
    points.append((base_x - 45, left_elbow_y))
    points.append((base_x + 45, right_elbow_y))
    
    # Hands
    hand_phase = arm_phase + math.pi/2
    points.append((base_x - 60, base_y - 20 + 40 * math.sin(hand_phase)))
    points.append((base_x + 60, base_y - 20 + 40 * math.sin(hand_phase)))
    
    # Hips
    points.append((base_x, base_y))
    points.append((base_x - 15, base_y))
    points.append((base_x + 15, base_y))
    
    # Legs
    leg_phase = 2 * math.pi * t_normalized
    knee_bend = 25 * (1 + math.sin(leg_phase))
    points.append((base_x - 15, base_y + knee_bend))
    points.append((base_x + 15, base_y + knee_bend))
    
    # Ankles
    ankle_phase = leg_phase + math.pi/2
    points.append((base_x - 15, base_y + 50 + 20 * math.sin(ankle_phase)))
    points.append((base_x + 15, base_y + 50 + 20 * math.sin(ankle_phase)))
    
    # Torso midpoint
    points.append((base_x, base_y - 15))
    
    return points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BACKGROUND_COLOR)
    
    current_time = pygame.time.get_ticks() / 1000
    t_normalized = (current_time % JUMP_DURATION) / JUMP_DURATION
    
    points = calculate_positions(t_normalized)
    
    for x, y in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
