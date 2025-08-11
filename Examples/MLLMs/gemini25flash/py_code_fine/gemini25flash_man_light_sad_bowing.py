
import pygame
import math

# --- Configuration ---
WIDTH, HEIGHT = 600, 800  # Window dimensions (portrait, similar to example image)
FPS = 30                      # Frames per second for smooth animation
DURATION_SECONDS = 3          # Total duration for one complete bow cycle (down and up)
POINT_RADIUS = 5              # Size of each white point-light
WHITE = (255, 255, 255)       # Color for the point-lights
BLACK = (0, 0, 0)             # Background color

# Number of point-lights required
NUM_POINTS = 15

# Normalized coordinates (0-1 range) for the initial standing pose.
# These represent a human figure's key joints/points, carefully chosen
# to match the visual style and proportions hinted by the example image.
# The y-axis is inverted for Pygame (0 at top, increasing downwards).
start_coords_norm = [
    (0.50, 0.10), # 0: Head
    (0.50, 0.18), # 1: Neck (Cervical Spine region)
    (0.42, 0.25), # 2: Left Shoulder (Acromion)
    (0.58, 0.25), # 3: Right Shoulder (Acromion)
    (0.40, 0.40), # 4: Left Elbow
    (0.60, 0.40), # 5: Right Elbow
    (0.38, 0.55), # 6: Left Wrist
    (0.62, 0.55), # 7: Right Wrist
    (0.50, 0.35), # 8: Mid-Torso (lower sternum/upper abdomen area)
    (0.45, 0.55), # 9: Left Hip (Greater Trochanter)
    (0.55, 0.55), # 10: Right Hip (Greater Trochanter)
    (0.47, 0.70), # 11: Left Knee
    (0.53, 0.70), # 12: Right Knee
    (0.47, 0.85), # 13: Left Ankle
    (0.53, 0.85), # 14: Right Ankle
]

# Normalized coordinates (0-1 range) for the final bowed pose.
# The bowing action is primarily a bend at the hips.
# - Head, Neck, Shoulders, Mid-Torso points move downwards and forwards.
# - Elbows and Wrists follow the shoulders, simulating naturally hanging arms.
# - Hip points act as the approximate pivot, showing minimal change.
# - Knee and Ankle points remain largely stationary, consistent with a formal bow.
end_coords_norm = [
    (0.50, 0.55), # 0: Head - moves significantly down for a deep bow
    (0.50, 0.50), # 1: Neck
    (0.42, 0.45), # 2: Left Shoulder
    (0.58, 0.45), # 3: Right Shoulder
    (0.40, 0.55), # 4: Left Elbow - arms hang more vertically/forward
    (0.60, 0.55), # 5: Right Elbow
    (0.38, 0.65), # 6: Left Wrist
    (0.62, 0.65), # 7: Right Wrist
    (0.50, 0.45), # 8: Mid-Torso
    (0.45, 0.55), # 9: Left Hip - minimal change (pivot)
    (0.55, 0.55), # 10: Right Hip - minimal change (pivot)
    (0.47, 0.70), # 11: Left Knee - stationary
    (0.53, 0.70), # 12: Right Knee - stationary
    (0.47, 0.85), # 13: Left Ankle - stationary
    (0.53, 0.85), # 14: Right Ankle - stationary
]

# --- Helper Function ---
# Converts normalized coordinates to pixel coordinates based on window size.
def to_pixels(coords_norm, width, height):
    return [(int(x * width), int(y * height)) for x, y in coords_norm]

# Convert the normalized start and end coordinates to pixel values
start_coords_pixels = to_pixels(start_coords_norm, WIDTH, HEIGHT)
end_coords_pixels = to_pixels(end_coords_norm, WIDTH, HEIGHT)

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Bowing")
clock = pygame.time.Clock()

# --- Animation Control Variables ---
# FRAMES_PER_PHASE defines the number of frames for one direction of the animation
# (e.g., from standing to bowed, or from bowed to standing).
FRAMES_PER_PHASE = int(FPS * DURATION_SECONDS / 2)

current_frame_in_phase = 0  # Counter for the current frame within the active phase
bowing_down = True          # Boolean flag: True for standing -> bowed, False for bowed -> standing

running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Drawing Background ---
    screen.fill(BLACK) # Ensures a solid black background for each frame

    # --- Animation Logic ---
    # Calculate 't_linear': a linear interpolation factor from 0.0 to 1.0 (or 1.0 to 0.0).
    # It represents the progress through the current animation phase.
    if bowing_down:
        t_linear = current_frame_in_phase / (FRAMES_PER_PHASE - 1)
    else:
        # If standing up, 't_linear' progresses from 1.0 down to 0.0
        t_linear = 1.0 - (current_frame_in_phase / (FRAMES_PER_PHASE - 1))
    
    # Apply easing function (cosine easing) for smoother motion.
    # This makes the animation start and end slowly, providing a more natural feel.
    t_eased = 0.5 - 0.5 * math.cos(t_linear * math.pi)

    # --- Draw Point-Lights ---
    for i in range(NUM_POINTS):
        start_x, start_y = start_coords_pixels[i]
        end_x, end_y = end_coords_pixels[i]

        # Interpolate each point's position based on the eased 't' value
        interp_x = start_x + (end_x - start_x) * t_eased
        interp_y = start_y + (end_y - start_y) * t_eased
        
        # Draw a white circle for each point
        pygame.draw.circle(screen, WHITE, (int(interp_x), int(interp_y)), POINT_RADIUS)

    # --- Update Animation State ---
    current_frame_in_phase += 1
    if current_frame_in_phase >= FRAMES_PER_PHASE:
        # If the current phase is complete, reset frame counter and toggle direction
        current_frame_in_phase = 0
        bowing_down = not bowing_down

    # --- Update Display and Control Frame Rate ---
    pygame.display.flip()  # Update the full display Surface to the screen
    clock.tick(FPS)        # Limit the frame rate to FPS

# --- Pygame Quit ---
pygame.quit()
