
import pygame
import math

# Constants for screen and drawing
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Scaling factors for the human figure
# The figure will be centered on the screen.
# FIGURE_SCALE determines the overall size of the point-light figure.
FIGURE_SCALE = 200 # pixels per relative unit
OFFSET_X = SCREEN_WIDTH / 2
OFFSET_Y = SCREEN_HEIGHT / 2

# Relative coordinates for 15 points, representing a person lying down on their back.
# The origin (0,0) is set to be roughly the center of the torso.
# The figure is oriented horizontally: head is towards the left (negative X),
# and feet are towards the right (positive X).
# Y-coordinates: Negative values represent points on the person's right side (visually "below" on screen).
#                Positive values represent points on the person's left side (visually "above" on screen).
initial_relative_points = {
    # Head and Torso (3 points)
    'head': (-0.6, 0.0),    # Head is furthest to the left
    'neck': (-0.5, 0.0),
    'torso': (0.0, 0.0),    # Mid-torso/center of gravity
    
    # Right Arm (from the person's perspective, visually "below" on screen) - 3 points
    'r_shoulder': (-0.4, -0.15),
    'r_elbow': (-0.25, -0.3),  # Arm slightly bent and extended outwards
    'r_wrist': (-0.05, -0.4),

    # Left Arm (from the person's perspective, visually "above" on screen) - 3 points
    'l_shoulder': (-0.4, 0.15),
    'l_elbow': (-0.25, 0.3),
    'l_wrist': (-0.05, 0.4),

    # Right Leg (from the person's perspective, visually "below" on screen) - 3 points
    'r_hip': (0.1, -0.1),
    'r_knee': (0.3, -0.2),  # Leg slightly bent at the knee
    'r_ankle': (0.5, -0.25),

    # Left Leg (from the person's perspective, visually "above" on screen) - 3 points
    'l_hip': (0.1, 0.1),
    'l_knee': (0.3, 0.2),
    'l_ankle': (0.5, 0.25),
}

# Verify that exactly 15 points are defined, as per the requirement.
assert len(initial_relative_points) == 15, f"Expected 15 points, but got {len(initial_relative_points)}"

# Points that will be affected by the subtle "breathing" animation.
# These points represent the torso and connected limbs, which would show slight movement during breathing.
BREATHING_AFFECTED_POINTS = [
    'head', 'neck', 'torso',
    'r_shoulder', 'l_shoulder',
    'r_hip', 'l_hip',
]

# Breathing animation parameters
# BREATHING_AMPLITUDE: Maximum vertical movement (in pixels) of the affected points.
# BREATHING_FREQUENCY: Speed of oscillation (in radians per millisecond). A smaller value means slower breathing.
BREATHING_AMPLITUDE = 4.0 # A slightly larger amplitude for "heavy weight" woman
BREATHING_FREQUENCY = 0.003 # A slightly slower frequency for "heavy weight" woman

def transform_point(relative_x, relative_y, breathing_offset_y=0):
    """
    Transforms relative coordinates (0-1 range) to screen pixel coordinates,
    applying a vertical offset for breathing animation.
    """
    # Scale relative coordinates to pixel size and apply screen offset to center the figure.
    screen_x = int(relative_x * FIGURE_SCALE + OFFSET_X)
    # Pygame's Y-axis increases downwards. To simulate a "rising chest" (moving visually up on screen),
    # the Y-coordinate needs to decrease. Hence, we subtract the breathing offset.
    screen_y = int(relative_y * FIGURE_SCALE + OFFSET_Y - breathing_offset_y)
    return (screen_x, screen_y)

def main():
    """
    Main function to initialize Pygame, set up the display, and run the animation loop.
    """
    pygame.init() # Initialize all the Pygame modules

    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Lying Down (Point-Light)")

    clock = pygame.time.Clock() # Create a clock object to control the frame rate

    running = True
    start_time = pygame.time.get_ticks() # Get the initial time in milliseconds for animation timing

    # Main animation loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Exit the loop if the user closes the window

        # Calculate elapsed time for smooth animation using a sine wave
        current_time = pygame.time.get_ticks()
        elapsed_time_ms = current_time - start_time

        # Calculate the breathing offset based on a sine wave.
        # This creates a smooth, oscillating vertical movement.
        breathing_offset = BREATHING_AMPLITUDE * math.sin(elapsed_time_ms * BREATHING_FREQUENCY)

        # Drawing operations
        screen.fill(BLACK) # Fill the background with black

        # Draw each of the 15 point-lights
        for point_name, (rel_x, rel_y) in initial_relative_points.items():
            current_breathing_offset_y = 0
            # Apply breathing animation only to the specified points (torso, head, shoulders, hips)
            if point_name in BREATHING_AFFECTED_POINTS:
                current_breathing_offset_y = breathing_offset
            
            # Get the final screen coordinates for the current point, including animation offset
            x, y = transform_point(rel_x, rel_y, current_breathing_offset_y)
            
            # Draw a white circle (point-light) at the calculated position
            pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

        pygame.display.flip() # Update the full display Surface to the screen

        clock.tick(FPS) # Control the frame rate to ensure consistent animation speed

    pygame.quit() # Uninitialize Pygame modules when the loop ends

if __name__ == "__main__":
    main()
