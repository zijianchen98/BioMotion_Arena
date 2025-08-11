
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Define the positions and connections of point-lights
POINT_LIGHTS = {
    "head": (0, -200),
    "shoulder_left": (-50, -150),
    "shoulder_right": (50, -150),
    "elbow_left": (-75, -100),
    "elbow_right": (75, -100),
    "hand_left": (-100, -50),
    "hand_right": (100, -50),
    "hip": (0, -50),
    "knee_left": (-50, 50),
    "knee_right": (50, 50),
    "foot_left": (-75, 200),
    "foot_right": (75, 200),
}

CONNECTIONS = [
    ("head", "shoulder_left"),
    ("head", "shoulder_right"),
    ("shoulder_left", "elbow_left"),
    ("shoulder_right", "elbow_right"),
    ("elbow_left", "hand_left"),
    ("elbow_right", "hand_right"),
    ("shoulder_left", "hip"),
    ("shoulder_right", "hip"),
    ("hip", "knee_left"),
    ("hip", "knee_right"),
    ("knee_left", "foot_left"),
    ("knee_right", "foot_right"),
]

# Function to apply smooth jumping animation
def animate_motion(base_points, t):
    animated_points = {}
    jump_amplitude = 150  # Amplitude of the jump
    jump_frequency = 2  # Frequency of the jump

    for key, (x, y) in base_points.items():
        # Vertical jumping motion
        y_offset = jump_amplitude * math.sin(math.radians(t * jump_frequency))

        # Add biomechanical vertical and horizontal sway for realism
        sway_x = 20 * math.sin(math.radians(t * jump_frequency * 0.5 + x * 0.01))
        sway_y = 10 * math.sin(math.radians(t * jump_frequency * 0.5 + y * 0.02))

        animated_points[key] = (x + sway_x + WIDTH // 2, y + sway_y + HEIGHT // 2 + y_offset)

    return animated_points

def draw_point_lights(points, connections):
    # Draw points
    for key, (x, y) in points.items():
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Draw connections
    for p1, p2 in connections:
        pygame.draw.line(screen, WHITE, points[p1], points[p2], 2)

def main():
    t = 0  # Time variable for animation
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Animate motion and render
        animated_points = animate_motion(POINT_LIGHTS, t)
        draw_point_lights(animated_points, CONNECTIONS)

        pygame.display.flip()
        clock.tick(60)

        t += 1  # Increment time for smooth animation

# Run the program
main()
