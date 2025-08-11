
import pygame
import math

# --- Program Configuration ---
# Screen and Animation settings
WIDTH, HEIGHT = 800, 600
FPS = 60
DOT_RADIUS = 5
ANIMATION_SECONDS = 4.0  # Duration for one full bow and return cycle

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Point-Light Model Definition ---
# The model consists of 15 points representing the major joints.
POINT_NAMES = [
    'head', 'neck_base', 'pelvis_center',
    'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow',
    'l_wrist', 'r_wrist', 'l_hip', 'r_hip',
    'l_knee', 'r_knee', 'l_ankle', 'r_ankle'
]

# --- Keyframe Poses ---
# The animation is created by interpolating between two keyframes.

# Keyframe 1: Standing "sad" pose.
# Posture is defined by slumped shoulders and a slightly lowered head.
BASE_POSE = {
    # Central axis points
    'head': (400, 190),
    'neck_base': (400, 240),
    'pelvis_center': (400, 360),
    # Left and Right Limbs
    'l_ankle': (370, 520),
    'r_ankle': (430, 520),
    'l_knee': (375, 440),
    'r_knee': (425, 440),
    'l_hip': (370, 360),
    'r_hip': (430, 360),
    'l_shoulder': (350, 250), # Slumped inward and downward
    'r_shoulder': (450, 250),
    'l_elbow': (340, 320),
    'r_elbow': (460, 320),
    'l_wrist': (335, 380),
    'r_wrist': (465, 380),
}

# Keyframe 2: Full "bow" pose.
# The upper body is bent forward, and the knees are slightly bent for balance.
BOW_POSE = {
    # Central axis moves down as the body bends
    'head': (400, 390),
    'neck_base': (400, 350),
    'pelvis_center': (400, 370),
    # Legs bend slightly, lowering the hips
    'l_ankle': (370, 520), # Feet are stationary anchors
    'r_ankle': (430, 520),
    'l_knee': (375, 450),
    'r_knee': (425, 450),
    'l_hip': (370, 370),
    'r_hip': (430, 370),
    # Upper body folds down, shoulders move closer
    'l_shoulder': (375, 355),
    'r_shoulder': (425, 355),
    # Arms hang down from the new shoulder positions
    'l_elbow': (370, 415),
    'r_elbow': (430, 415),
    'l_wrist': (365, 470),
    'r_wrist': (435, 470),
}

def interpolate(p1, p2, factor):
    """
    Linearly interpolates between two 2D points (p1 and p2)
    based on a factor (0.0 to 1.0).
    """
    x = p1[0] + (p2[0] - p1[0]) * factor
    y = p1[1] + (p2[1] - p1[1]) * factor
    return (x, y)

def main():
    """
    Initializes Pygame and runs the main animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Bowing")
    clock = pygame.time.Clock()

    start_ticks = pygame.time.get_ticks()
    running = True

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Animation Timing ---
        # Calculate time progress within the animation cycle
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        cycle_progress = (elapsed_ms / (1000.0 * ANIMATION_SECONDS)) % 1.0

        # Use a smooth easing function (cosine wave) that moves from 0 to 1 and back to 0.
        # This creates a natural acceleration and deceleration for the motion.
        eased_factor = (1 - math.cos(cycle_progress * 2 * math.pi)) / 2.0

        # --- Update Point Positions ---
        # Calculate the current position of each point by interpolating between
        # the base pose and the bow pose using the eased factor.
        current_points = {}
        for name in POINT_NAMES:
            start_pos = BASE_POSE[name]
            end_pos = BOW_POSE[name]
            current_points[name] = interpolate(start_pos, end_pos, eased_factor)

        # --- Drawing ---
        screen.fill(BLACK)

        for name in POINT_NAMES:
            pos = current_points[name]
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), DOT_RADIUS)

        pygame.display.flip()

        # --- Frame Rate Control ---
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
