
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point stimulus properties
POINT_RADIUS = 5
NUM_POINTS = 15  # Required number of points

# Animation parameters
FPS = 60
ROLL_SPEED_X_PIXELS_PER_SEC = 100  # Horizontal speed of the rolling figure
ROLL_ANGULAR_SPEED_RAD_PER_SEC = 2.0 * math.pi / 1.5  # One full 360-degree roll in 1.5 seconds

# Initial figure position (center of screen, adjusted for continuous motion)
INITIAL_CENTER_X = WIDTH // 4  # Start the figure somewhat to the left
INITIAL_CENTER_Y = HEIGHT // 2  # Vertical center for the average height of the figure

# Base point definitions relative to the figure's central point (torso)
# These coordinates define the 'extended' or 'neutral' pose of the figure.
# (x, y) coordinates relative to the torso's center (0,0). Y-axis positive down in Pygame.
BASE_POINTS = {
    'head': (0, -100),
    'neck': (0, -70),
    'left_shoulder': (-45, -50), 'right_shoulder': (45, -50),
    'left_elbow': (-60, 0), 'right_elbow': (60, 0),
    'left_wrist': (-75, 50), 'right_wrist': (75, 50),
    'torso': (0, 0),  # This is the central point for overall rotation
    'left_hip': (-35, 30), 'right_hip': (35, 30),
    'left_knee': (-50, 80), 'right_knee': (50, 80),
    'left_ankle': (-65, 130), 'right_ankle': (65, 130)
}

# Ensure we have exactly 15 points as per requirements
assert len(BASE_POINTS) == NUM_POINTS, f"Error: Expected {NUM_POINTS} points, but defined {len(BASE_POINTS)}."

# Animation state variables
current_x = INITIAL_CENTER_X
current_angle = 0.0  # Current rotation angle of the figure in radians

# Amplitude for vertical undulation during roll (representing CoM movement)
# This makes the figure "bob" up and down as it rolls, simulating lifting off and landing.
Y_UNDULATION_AMPLITUDE = 60 

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate delta time for frame-rate independent motion
    dt = clock.tick(FPS) / 1000.0  # seconds since last frame

    # Update global position and rotation of the figure
    current_x += ROLL_SPEED_X_PIXELS_PER_SEC * dt
    current_angle += ROLL_ANGULAR_SPEED_RAD_PER_SEC * dt

    # Loop the figure around the screen horizontally
    # When it moves fully off the right side, reset it to the left side
    if current_x > WIDTH + 150:  # Add a buffer to allow the figure to fully exit
        current_x = -150  # Reset to left off-screen with a similar buffer

    # Calculate vertical undulation for the rolling motion.
    # The center of mass (CoM) is lowest when the figure is 'standing' or 'inverted' (angle ~0 or pi),
    # and highest when it's transitioning (e.g., body horizontal, angle ~pi/2 or 3pi/2),
    # as if pushing off the ground. This contributes to the "light weight" and "agile" feel.
    # -math.cos(current_angle) oscillates between -1 and 1.
    # When current_angle is 0 (upright), -cos(0) = -1, lowest Y.
    # When current_angle is pi/2 (horizontal), -cos(pi/2) = 0, mid Y.
    # When current_angle is pi (inverted), -cos(pi) = 1, highest Y.
    current_y = INITIAL_CENTER_Y + Y_UNDULATION_AMPLITUDE * (-math.cos(current_angle))

    # Clear screen to black
    SCREEN.fill(BLACK)

    # Calculate and draw each point based on current animation state
    for point_name, (base_rel_x, base_rel_y) in BASE_POINTS.items():
        # The 'tuck_factor' simulates limb bending and tucking during the roll.
        # It's high (limbs tucked) when the body is roughly horizontal (angle ~pi/2, 3pi/2),
        # and low (limbs extended) when the body is vertical (angle ~0, pi).
        # (1 - cos(2*theta)) / 2 is equivalent to sin^2(theta), oscillating between 0 and 1 twice per cycle.
        tuck_factor = (1 - math.cos(current_angle * 2)) / 2.0
        
        # Start with the base relative position
        adjusted_rel_x, adjusted_rel_y = base_rel_x, base_rel_y

        # Define how strongly different body parts tuck in
        arm_tuck_strength = 0.6
        leg_tuck_strength = 0.8
        head_neck_tuck_strength = 0.4

        # Apply tucking adjustments based on `tuck_factor`
        # Limbs pull inwards towards the torso's central point (0,0)
        if 'shoulder' in point_name or 'elbow' in point_name or 'wrist' in point_name:
            # Arms pull in, reducing their horizontal and vertical extension from the torso
            adjusted_rel_x *= (1 - tuck_factor * arm_tuck_strength)
            adjusted_rel_y *= (1 - tuck_factor * arm_tuck_strength * 0.5) 
        elif 'hip' in point_name or 'knee' in point_name or 'ankle' in point_name:
            # Legs bend significantly, pulling knees/ankles closer to the torso
            # Reducing positive Y values brings them 'up' towards the torso center.
            adjusted_rel_x *= (1 - tuck_factor * leg_tuck_strength)
            adjusted_rel_y *= (1 - tuck_factor * leg_tuck_strength) 
        elif point_name == 'head' or point_name == 'neck':
            # Head and neck pull closer to the torso (reducing negative Y value)
            adjusted_rel_y *= (1 - tuck_factor * head_neck_tuck_strength) 
            adjusted_rel_x *= (1 - tuck_factor * head_neck_tuck_strength * 0.5)

        # Apply the overall rotation of the figure to the adjusted point position
        cos_a = math.cos(current_angle)
        sin_a = math.sin(current_angle)

        rotated_x = adjusted_rel_x * cos_a - adjusted_rel_y * sin_a
        rotated_y = adjusted_rel_x * sin_a + adjusted_rel_y * cos_a

        # Apply the global translation (current_x, current_y) to get screen coordinates
        screen_x = int(rotated_x + current_x)
        screen_y = int(rotated_y + current_y)

        # Draw the white point-light stimulus
        pygame.draw.circle(SCREEN, WHITE, (screen_x, screen_y), POINT_RADIUS)

    # Update the entire display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
