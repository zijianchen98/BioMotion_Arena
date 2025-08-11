
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Helper function to map the biomechanical motion
def biomechanical_motion(frame, amplitude, frequency, phase_shift):
    """Generate smooth, natural motion based on sine waves for animation."""
    return amplitude * math.sin(frequency * frame + phase_shift)

# Define point-light positions relative to the `happyman` structure
# Joint positions (e.g., head, shoulders, elbows, wrists, hips, knees, ankles)
original_positions = [
    (300, 200),  # Head
    (250, 300), (350, 300),  # Shoulders
    (200, 400), (400, 400),  # Elbows
    (150, 500), (450, 500),  # Wrists
    (260, 500), (340, 500),  # Hips
    (230, 600), (370, 600),  # Knees
    (200, 700), (400, 700),  # Ankles
    (300, 750),  # Left Foot
    (320, 750)   # Right Foot
]

# Amplitude and frequency settings for the motion
head_amplitude = 20
head_frequency = 0.1
leg_amplitude = 40
leg_frequency = 0.2
arm_amplitude = 25
arm_frequency = 0.15

def animate_positions(frame):
    """Update positions of the points based on the biomechanical motion."""
    updated_positions = []
    for i, pos in enumerate(original_positions):
        x, y = pos
        # Apply biomechanical motion to different parts
        if i == 0:  # Head
            y += biomechanical_motion(frame, head_amplitude, head_frequency, 0)
        elif i in [3, 4]:  # Elbows
            x += biomechanical_motion(frame, arm_amplitude, arm_frequency, math.pi / 2)
        elif i in [5, 6]:  # Wrists
            x += biomechanical_motion(frame, arm_amplitude, arm_frequency, 0)
        elif i in [9, 10]:  # Knees
            y += biomechanical_motion(frame, leg_amplitude, leg_frequency, math.pi / 2)
        elif i in [11, 12]:  # Ankles
            y += biomechanical_motion(frame, leg_amplitude, leg_frequency, 0)
        elif i in [13, 14]:  # Feet
            y += biomechanical_motion(frame, leg_amplitude / 2, leg_frequency, math.pi / 2)
        updated_positions.append((x, y))
    return updated_positions

# Main animation loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen background
    screen.fill(BLACK)

    # Animate the positions
    new_positions = animate_positions(frame)

    # Draw the point-lights
    for pos in new_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update the display to show the new frame
    pygame.display.flip()

    # Increment frame counter
    frame += 1

    # Control frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
