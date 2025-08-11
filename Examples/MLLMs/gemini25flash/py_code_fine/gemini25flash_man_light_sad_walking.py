
import pygame
import math
import sys

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Animation parameters
# The gait cycle duration (in frames) determines the speed of the walk.
# A longer duration makes the walk slower, contributing to the "sadman" feel.
GAIT_CYCLE_DURATION_FRAMES = int(FPS * 2.0)  # 2 seconds per gait cycle

# Base position for the entire figure on the screen.
# Centered horizontally, shifted slightly up vertically to allow full leg movement.
BASE_POS_X = SCREEN_WIDTH // 2
BASE_POS_Y = SCREEN_HEIGHT // 2 + 50 

# Joint data for the 15 point-lights.
# Each entry is a tuple:
# (base_x, base_y, amp_x, amp_y, phase_x, phase_y, freq_mult_x, freq_mult_y)
#
# - base_x, base_y:   Relative static position of the joint from the figure's central reference point (hips).
#                     `base_y` is defined as positive upwards (like a standard Cartesian plane),
#                     which will be inverted for Pygame's y-axis (Y increases downwards).
# - amp_x, amp_y:     Amplitude of sinusoidal movement in the x and y directions.
# - phase_x, phase_y: Phase offset (in radians) for the sinusoidal movements.
#                     This determines the starting point in the sine wave cycle.
#                     e.g., 0 for sin(0)=0 (mid-swing), pi/2 for sin(pi/2)=1 (peak), 3*pi/2 for sin(3*pi/2)=-1 (trough).
# - freq_mult_x, freq_mult_y: Frequency multiplier for the sinusoidal movement.
#                     1 means one full oscillation per gait cycle.
#                     2 means two oscillations per gait cycle (e.g., vertical bounce of torso, two steps per cycle).
#
# Reference for gait cycle phase (time_param from 0 to 2*pi):
# 0 (or 2*pi): Represents the moment of the Right foot's heel strike (right leg is fully extended forward and on ground).
# pi: Represents the moment of the Left foot's heel strike (left leg is fully extended forward and on ground).
JOINT_DATA = {
    # Head: Bobs slightly up/down (twice per gait cycle), minimal horizontal movement.
    'Head':         (  0, 160,   0,   5,   0,           3*math.pi/2, 1, 2), 
    
    # Shoulders: Vertical bounce (2x freq) in sync with head/torso. Horizontal swing (1x freq).
    # Arms swing in opposition to legs: Left arm swings forward when Left leg is forward (and Right leg is back).
    # Right arm swings backward when Right leg is forward (and Left leg is back).
    'L_Shoulder':   (-40, 110,   5,   2,   0,           3*math.pi/2, 1, 2), # Left arm swings forward (phase 0)
    'R_Shoulder':   ( 40, 110,  -5,   2, math.pi,       3*math.pi/2, 1, 2), # Right arm swings backward (phase pi)
    
    # Elbows: More pronounced arm swing.
    'L_Elbow':      (-60,  80,  20,  15,  0,            3*math.pi/2, 1, 1), 
    'R_Elbow':      ( 60,  80, -20,  15, math.pi,       3*math.pi/2, 1, 1), 
    
    # Wrists: Even more pronounced arm swing, following elbow motion.
    'L_Wrist':      (-70,  40,  30,  25,  0,            3*math.pi/2, 1, 1), 
    'R_Wrist':      ( 70,  40, -30,  25, math.pi,       3*math.pi/2, 1, 1), 
    
    # Hips: Slight side-to-side sway (1x freq) and vertical bounce (2x freq) synchronized with body.
    # Hip horizontal movement slightly anticipates leg swing.
    'L_Hip':        (-20,   0,   5,   3, math.pi + math.pi/2, 3*math.pi/2, 1, 2), 
    'R_Hip':        ( 20,   0,  -5,   3, math.pi/2,           3*math.pi/2, 1, 2), 

    # Legs: The core of the walking motion.
    # Right leg (primary phase, starts at angle=0: forward, lowest point for heel strike):
    #   x-motion (forward/backward): Uses phase `pi/2` so `sin(angle + pi/2)` starts at max positive (forward).
    #   y-motion (up/down for stepping): Uses phase `3*pi/2` so `sin(angle + 3*pi/2)` starts at min negative (lowest point).
    'R_Knee':       ( 30, -40, -30,  40, math.pi/2,           3*math.pi/2, 1, 1), 
    'R_Ankle':      ( 30, -80, -40,  60, math.pi/2,           3*math.pi/2, 1, 1), 
    'R_Foot':       ( 30, -100, -50,  70, math.pi/2,           3*math.pi/2, 1, 1), 
    
    # Left leg (180 degrees out of phase from right leg):
    # Its phases are relative to the right leg's cycle (add pi).
    'L_Knee':       (-30, -40,  30,  40, math.pi + math.pi/2, math.pi + 3*math.pi/2, 1, 1),
    'L_Ankle':      (-30, -80,  40,  60, math.pi + math.pi/2, math.pi + 3*math.pi/2, 1, 1),
    'L_Foot':       (-30, -100, 50,  70, math.pi + math.pi/2, math.pi + 3*math.pi/2, 1, 1),
}

# Define the precise order of points to ensure exactly 15 are used.
# This order also corresponds to standard biological motion marker sets.
POINT_ORDER = [
    'Head', 'L_Shoulder', 'R_Shoulder', 'L_Elbow', 'R_Elbow', 'L_Wrist', 'R_Wrist',
    'L_Hip', 'R_Hip', 'L_Knee', 'R_Knee', 'L_Ankle', 'R_Ankle', 'L_Foot', 'R_Foot'
]

# Assertion to ensure the strict requirement of 15 points is met.
assert len(POINT_ORDER) == 15, "The number of points must be exactly 15."

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Walking Sadman")
clock = pygame.time.Clock()

# --- Animation Loop ---
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear the screen with black background each frame

    # Calculate the current phase of the gait cycle (from 0 to 2*pi radians).
    # `frame_count % GAIT_CYCLE_DURATION_FRAMES` ensures a continuous, looping animation.
    time_param = (frame_count % GAIT_CYCLE_DURATION_FRAMES) / GAIT_CYCLE_DURATION_FRAMES * (2 * math.pi)

    # Calculate and draw each point's position for the current frame.
    for point_name in POINT_ORDER:
        # Retrieve motion parameters for the current point
        base_x, base_y, amp_x, amp_y, phase_x, phase_y, freq_mult_x, freq_mult_y = JOINT_DATA[point_name]

        # Calculate animated offsets using sinusoidal functions.
        # The `freq_mult` determines how many cycles the point completes within one gait cycle.
        # The `phase` shifts the start of the sine wave.
        anim_x = amp_x * math.sin(time_param * freq_mult_x + phase_x)
        anim_y = amp_y * math.sin(time_param * freq_mult_y + phase_y)

        # Calculate the final screen position for the point.
        # `BASE_POS_X` centers the figure horizontally.
        # `BASE_POS_Y - (base_y + anim_y)` is used because Pygame's Y-axis increases downwards,
        # while our `base_y` and `anim_y` are defined as positive values for upward movement.
        pos_x = int(BASE_POS_X + base_x + anim_x)
        pos_y = int(BASE_POS_Y - (base_y + anim_y))
        
        # Draw the point as a white circle on the screen.
        pygame.draw.circle(screen, WHITE, (pos_x, pos_y), POINT_RADIUS)

    pygame.display.flip() # Update the entire screen to show the newly drawn points

    frame_count += 1 # Increment frame counter for animation progression
    clock.tick(FPS) # Control the frame rate to ensure consistent speed

pygame.quit() # Uninitialize Pygame modules
sys.exit() # Exit the program cleanly
