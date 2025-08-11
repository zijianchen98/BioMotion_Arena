
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

def calculate_positions(t):
    """Calculate positions of 15 body points based on time t"""
    body_x = 400 + (t * 1.5) % width  # Body center with horizontal movement
    body_y = 300 + 8 * math.sin(t * 0.08)  # Vertical oscillation

    # Head
    head = (body_x, body_y - 50)

    # Shoulders
    shoulders = [
        (body_x - 30, body_y - 25),  # Left shoulder
        (body_x + 30, body_y - 25)   # Right shoulder
    ]

    # Arms
    arm_phase = t * 0.25
    arm_swing = 45 * math.sin(arm_phase)
    left_elbow = (
        shoulders[0][0] + arm_swing * math.sin(arm_phase + math.pi),
        shoulders[0][1] + 30 * math.cos(arm_phase)
    )
    right_elbow = (
        shoulders[1][0] + arm_swing * math.sin(arm_phase),
        shoulders[1][1] + 30 * math.cos(arm_phase + math.pi)
    )
    hands = [
        (left_elbow[0] + 25 * math.sin(arm_phase + math.pi), left_elbow[1] + 15),
        (right_elbow[0] + 25 * math.sin(arm_phase), right_elbow[1] + 15)
    ]

    # Hips
    hips = [
        (body_x - 20, body_y + 10),  # Left hip
        (body_x + 20, body_y + 10)   # Right hip
    ]

    # Legs with heavier movement
    leg_phase = t * 0.3
    leg_swing = 60 * math.sin(leg_phase)
    vertical_lift = 40 * abs(math.sin(leg_phase))  # Enhanced vertical movement

    left_knee = (
        hips[0][0] + leg_swing * math.sin(leg_phase + math.pi),
        hips[0][1] + vertical_lift
    )
    right_knee = (
        hips[1][0] + leg_swing * math.sin(leg_phase),
        hips[1][1] + vertical_lift
    )

    # Ankles and feet with weighted movement
    ankle_phase = leg_phase + 0.5
    ankle_swing = 50 * math.sin(ankle_phase)
    left_ankle = (
        left_knee[0] + ankle_swing * math.sin(ankle_phase + math.pi),
        left_knee[1] + 50
    )
    right_ankle = (
        right_knee[0] + ankle_swing * math.sin(ankle_phase),
        right_knee[1] + 50
    )

    feet = [
        (left_ankle[0], left_ankle[1] + 20),  # Left foot
        (right_ankle[0], right_ankle[1] + 20) # Right foot
    ]

    return [head] + shoulders + [left_elbow, right_elbow] + hands + hips + [left_knee, right_knee] + [left_ankle, right_ankle] + feet

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Get current time in seconds
    current_time = pygame.time.get_ticks() / 1000
    
    # Calculate all point positions
    points = calculate_positions(current_time)
    
    # Draw all points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
