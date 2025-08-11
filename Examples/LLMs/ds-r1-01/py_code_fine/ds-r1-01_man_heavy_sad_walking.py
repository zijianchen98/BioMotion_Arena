
import pygame
import math
import sys

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Sad Walk")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuration parameters
dt = 0.03  # Slower speed for heavy movement
vertical_amplitude = 30  # Increased body vertical movement
hip_width = 35
shoulder_width = 40
torso_height = 60
head_radius = 8

# Limb movement parameters (adjusted for heavy weight)
leg_amplitude_x = 40  # Shorter stride
leg_amplitude_y = 40  # Higher knee lift
arm_amplitude_x = 15  # Reduced arm swing
arm_amplitude_y = 10

def calculate_positions(t):
    center_x, center_y = width//2, height//2 + 50  # Lower center for slumped posture
    
    # Vertical body movement
    body_vertical = vertical_amplitude * math.sin(t*0.7)
    
    # Head (subtle nodding)
    head_pos = (center_x, center_y - torso_height - head_radius + body_vertical - 10)
    
    # Shoulders (slightly hunched)
    left_shoulder = (center_x - shoulder_width, center_y - torso_height + body_vertical - 5)
    right_shoulder = (center_x + shoulder_width, center_y - torso_height + body_vertical - 5)
    
    # Hips (wider stance)
    left_hip = (center_x - hip_width, center_y + body_vertical + 10)
    right_hip = (center_x + hip_width, center_y + body_vertical + 10)
    
    # Legs (exaggerated knee bend)
    left_ankle = (
        left_hip[0] + leg_amplitude_x * math.sin(t),
        left_hip[1] + leg_amplitude_y * math.sin(t + math.pi/2) + 20
    )
    left_knee = (
        (left_hip[0] + left_ankle[0])/2,
        (left_hip[1] + left_ankle[1])/2 - 35  # Deep knee bend
    )
    
    right_ankle = (
        right_hip[0] - leg_amplitude_x * math.sin(t),
        right_hip[1] + leg_amplitude_y * math.sin(t + math.pi/2) + 20
    )
    right_knee = (
        (right_hip[0] + right_ankle[0])/2,
        (right_hip[1] + right_ankle[1])/2 - 35
    )
    
    # Arms (limited swing, forward lean)
    left_wrist = (
        left_shoulder[0] - arm_amplitude_x * math.sin(t + math.pi),
        left_shoulder[1] + arm_amplitude_y * math.sin(t + math.pi/2) + 30
    )
    left_elbow = (
        (left_shoulder[0] + left_wrist[0])/2 - 5,
        (left_shoulder[1] + left_wrist[1])/2 + 15
    )
    
    right_wrist = (
        right_shoulder[0] + arm_amplitude_x * math.sin(t + math.pi),
        right_shoulder[1] + arm_amplitude_y * math.sin(t + math.pi/2) + 30
    )
    right_elbow = (
        (right_shoulder[0] + right_wrist[0])/2 + 5,
        (right_shoulder[1] + right_wrist[1])/2 + 15
    )
    
    # Feet (flat contact pattern)
    left_foot = (left_ankle[0], left_ankle[1] + 25)
    right_foot = (right_ankle[0], right_ankle[1] + 25)
    
    return [
        head_pos, left_shoulder, right_shoulder,
        left_elbow, right_elbow, left_wrist, right_wrist,
        left_hip, right_hip, left_knee, right_knee,
        left_ankle, right_ankle, left_foot, right_foot
    ]

# Main animation loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BLACK)
    points = calculate_positions(t)
    
    # Draw all 15 points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)
    t += dt
