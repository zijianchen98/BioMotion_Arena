
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of points and their labels
NUM_POINTS = 15
POINT_RADIUS = 4
POINT_LABELS = ["head", "neck", "shoulder_r", "shoulder_l", "elbow_r", "elbow_l", 
                "wrist_r", "wrist_l", "chest", "hip_r", "hip_l", "knee_r", 
                "knee_l", "ankle_r", "ankle_l"]

# Center of the animation
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
GROUND_Y = CENTER_Y + 150

# Biomechanical parameters
BODY_HEIGHT = 200  # Height in pixels
ARM_LENGTH = 0.4 * BODY_HEIGHT
LEG_LENGTH = 0.5 * BODY_HEIGHT
UPPER_ARM = 0.45 * ARM_LENGTH
LOWER_ARM = 0.55 * ARM_LENGTH
THIGH = 0.4 * LEG_LENGTH
CALF = 0.4 * LEG_LENGTH
FOOT = 0.2 * LEG_LENGTH

# Forward roll animation parameters
ROLL_RADIUS = 0.3 * BODY_HEIGHT
SPINE_CURVATURE = 0.2
PHASE_DURATION = 250  # milliseconds per phase

def get_point_positions(animation_progress):
    """Calculate the positions of all 15 points during the animation"""
    # Calculate the main body position (center of gravity)
    t = animation_progress
    body_x = CENTER_X
    body_y = GROUND_Y
    
    # Head position
    head_x = body_x
    head_y = body_y - 0.9 * BODY_HEIGHT
    
    # Calculate rolling movement (sigmoid progression)
    roll_angle = 4 * t
    roll_distance = (math.sin(roll_angle - math.pi/2) + 1) / 2 * ROLL_RADIUS * 2
    if animation_progress > 0.5:
        roll_offset = ROLL_RADIUS * (4 * animation_progress - 2)
    else:
        roll_offset = 0
    
    # Determine body tilt and roll position
    body_tilt = 0
    head_tilt = 0
    if animation_progress < 0.25:  # Initiation phase
        body_tilt = animation_progress * 3.2
        head_tilt = animation_progress * 1.8
        roll_offset = animation_progress * ROLL_RADIUS * 2
    elif animation_progress < 0.75:  # Rolling phase
        body_tilt = 0.8 + animation_progress * 2
        head_tilt = 0.45 + animation_progress * 2.2
    else:  # Recovery phase
        body_tilt = 2.8 - (animation_progress - 0.75) * 3.2
        head_tilt = 2.4 - (animation_progress - 0.75) * 1.8
        roll_offset = ROLL_RADIUS * 2 - (animation_progress - 0.5) * ROLL_RADIUS * 2
    
    # Apply forward roll movement to the body
    body_y = GROUND_Y - roll_distance
    body_x = CENTER_X + roll_offset
    head_x = body_x - math.sin(head_tilt) * 0.4 * BODY_HEIGHT
    head_y = body_y - math.cos(head_tilt) * 0.8 * BODY_HEIGHT
    
    # Calculate spine curvature for more natural movement
    spine_curve = math.sin(animation_progress * 4) * SPINE_CURVATURE * BODY_HEIGHT
    
    # Calculate positions of all points
    points = {}
    
    # Head and neck
    points["head"] = (head_x, head_y)
    points["neck"] = (
        head_x + math.sin(head_tilt + 0.4) * 0.1 * BODY_HEIGHT,
        head_y + math.cos(head_tilt + 0.4) * 0.1 * BODY_HEIGHT
    )
    
    # Shoulders and chest
    points["shoulder_r"] = (
        body_x + math.sin(body_tilt) * 0.2 * BODY_HEIGHT,
        body_y + math.cos(body_tilt) * 0.25 * BODY_HEIGHT
    )
    points["shoulder_l"] = (
        body_x - math.sin(body_tilt) * 0.2 * BODY_HEIGHT,
        body_y + math.cos(body_tilt) * 0.25 * BODY_HEIGHT
    )
    points["chest"] = (body_x, body_y)
    
    # Arms (right)
    points["elbow_r"] = (
        points["shoulder_r"][0] + math.sin(body_tilt + 1.0) * UPPER_ARM,
        points["shoulder_r"][1] + math.cos(body_tilt + 1.0) * UPPER_ARM
    )
    points["wrist_r"] = (
        points["elbow_r"][0] + math.sin(body_tilt + 1.2) * LOWER_ARM,
        points["elbow_r"][1] + math.cos(body_tilt + 1.2) * LOWER_ARM
    )
    
    # Arms (left)
    points["elbow_l"] = (
        points["shoulder_l"][0] + math.sin(body_tilt - 0.6) * UPPER_ARM,
        points["shoulder_l"][1] + math.cos(body_tilt - 0.6) * UPPER_ARM
    )
    points["wrist_l"] = (
        points["elbow_l"][0] + math.sin(body_tilt - 0.8) * LOWER_ARM,
        points["elbow_l"][1] + math.cos(body_tilt - 0.8) * LOWER_ARM
    )
    
    # Hips
    points["hip_r"] = (
        body_x + math.sin(body_tilt - 0.3) * 0.2 * BODY_HEIGHT - spine_curve * 0.4,
        body_y + math.cos(body_tilt - 0.3) * 0.25 * BODY_HEIGHT
    )
    points["hip_l"] = (
        body_x - math.sin(body_tilt - 0.3) * 0.2 * BODY_HEIGHT - spine_curve * 0.4,
        body_y + math.cos(body_tilt - 0.3) * 0.25 * BODY_HEIGHT
    )
    
    # Legs (right)
    points["knee_r"] = (
        points["hip_r"][0] + math.sin(body_tilt + 0.2) * THIGH,
        points["hip_r"][1] + math.cos(body_tilt + 0.2) * THIGH
    )
    points["ankle_r"] = (
        points["knee_r"][0] + math.sin(body_tilt + 0.5) * CALF,
        points["knee_r"][1] + math.cos(body_tilt + 0.5) * CALF
    )
    
    # Legs (left)
    points["knee_l"] = (
        points["hip_l"][0] + math.sin(body_tilt - 0.5) * THIGH,
        points["hip_l"][1] + math.cos(body_tilt - 0.5) * THIGH
    )
    points["ankle_l"] = (
        points["knee_l"][0] + math.sin(body_tilt - 0.2) * CALF,
        points["knee_l"][1] + math.cos(body_tilt - 0.2) * CALF
    )
    
    return points

def main():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BLACK)
        
        # Calculate animation progress (0 to 1, looped)
        elapsed = pygame.time.get_ticks() - start_time
        animation_progress = (elapsed % PHASE_DURATION) / PHASE_DURATION
        
        # Get current point positions
        points = get_point_positions(animation_progress)
        
        # Draw all 15 points
        for label in POINT_LABELS:
            x, y = points[label]
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

if __name__ == "__main__":
    main()
