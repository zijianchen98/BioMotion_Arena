
import pygame
import math

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 6

# Animation settings
ANIMATION_DURATION_SECONDS = 7  # Slower turn for "heavy" feel
TOTAL_FRAMES = FPS * ANIMATION_DURATION_SECONDS

# 3D Projection settings
ZOOM = 2.0
PERSPECTIVE = 0.004

# --- 3D Model Data ---
# 15 joints representing a human figure.
# The origin (0,0,0) is at the Pelvis.
# Y is up, X is right, Z is towards the viewer.
# The pose is designed to be slumped and hunched, as if sad or carrying weight.
BASE_POSE_3D = [
    (0, 95, -5),   # 0: Head (slumped forward and down)
    (0, 70, -10),  # 1: Sternum (hunched)
    (20, 68, -8),  # 2: Right Shoulder
    (-20, 68, -8), # 3: Left Shoulder
    (28, 40, 0),   # 4: Right Elbow (arms slightly out)
    (-28, 40, 0),  # 5: Left Elbow
    (32, 15, 5),   # 6: Right Wrist
    (-32, 15, 5),  # 7: Left Wrist
    (0, 0, 0),     # 8: Pelvis
    (12, -2, 0),   # 9: Right Hip
    (-12, -2, 0),  # 10: Left Hip
    (15, -45, -5), # 11: Right Knee (bent)
    (-15, -45, -5),# 12: Left Knee (bent)
    (15, -90, 0),  # 13: Right Ankle
    (-15, -90, 0), # 14: Left Ankle
]

# --- Core Functions ---

def rotate_y(p, angle_rad):
    """Rotates a 3D point (x, y, z) around the Y axis."""
    x, y, z = p
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    new_x = x * cos_a + z * sin_a
    new_z = -x * sin_a + z * cos_a
    return new_x, y, new_z

def project_3d_to_2d(p):
    """Projects a 3D point to 2D screen coordinates with perspective."""
    x, y, z = p
    
    # Perspective scaling factor
    scale = 1 / (1 + z * PERSPECTIVE + 1e-6)
    
    # Apply zoom and center on screen
    screen_x = SCREEN_WIDTH / 2 + x * scale * ZOOM
    # Pygame's Y-axis is inverted (0 is at the top)
    screen_y = SCREEN_HEIGHT / 2 - y * scale * ZOOM
    
    # Adjust point radius based on depth for a 3D effect
    radius = max(2, POINT_RADIUS * scale * ZOOM * 0.8)
    
    return int(screen_x), int(screen_y), int(radius)

def get_animation_frame(frame_index):
    """
    Calculates the 3D coordinates for all points for a given animation frame.
    The motion combines a primary rotation with secondary motions (bobbing, shuffling)
    to create the impression of a sad, heavy person turning around.
    """
    progress = frame_index / TOTAL_FRAMES
    
    # 1. Primary Motion: Full 360-degree turn
    body_angle = progress * 2 * math.pi
    
    # 2. Secondary Motions for "Sad/Heavy" feel
    
    # Slow vertical bobbing from heavy steps
    bob_freq = 2 * math.pi * 2  # Two "steps" per rotation cycle
    bob_amp = 4                 # How much the body moves down with each step
    vertical_bob = -abs(math.sin(progress * bob_freq)) * bob_amp

    # Shuffling motion for feet
    shuffle_freq = 2 * math.pi * 4  # Four shuffles per rotation
    shuffle_amp_z = 10              # Forward/backward shuffle distance
    shuffle_amp_y = 5               # Vertical lift for shuffle

    # Use phase-shifted sine waves for alternating left/right foot shuffles
    l_shuffle_phase = progress * shuffle_freq
    r_shuffle_phase = progress * shuffle_freq + math.pi
    
    l_foot_shuffle_z = math.sin(l_shuffle_phase) * shuffle_amp_z
    l_foot_shuffle_y = max(0, math.cos(l_shuffle_phase)) * shuffle_amp_y 

    r_foot_shuffle_z = math.sin(r_shuffle_phase) * shuffle_amp_z
    r_foot_shuffle_y = max(0, math.cos(r_shuffle_phase)) * shuffle_amp_y

    current_points = []
    for i, p_base in enumerate(BASE_POSE_3D):
        x, y, z = p_base
        
        # Apply body bob to all points except the feet
        if i not in [13, 14]:
            y += vertical_bob
        
        # Apply shuffling motion to the leg chain (ankles and knees)
        if i == 14:  # Left Ankle
            z += l_foot_shuffle_z
            y += l_foot_shuffle_y
        elif i == 13:  # Right Ankle
            z += r_foot_shuffle_z
            y += r_foot_shuffle_y
        elif i == 12:  # Left Knee
            # Knee follows the ankle's motion, but less intensely
            z += l_foot_shuffle_z * 0.6
            y += l_foot_shuffle_y * 0.5
        elif i == 11:  # Right Knee
            z += r_foot_shuffle_z * 0.6
            y += r_foot_shuffle_y * 0.5
            
        p_modified = (x, y, z)
        
        # Apply overall rotation to the modified point
        p_rotated = rotate_y(p_modified, body_angle)
        
        current_points.append(p_rotated)
        
    return current_points

# --- Main Application ---
def main():
    """Initializes Pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Man with Heavy Weight Turning Around")
    clock = pygame.time.Clock()
    
    frame_index = 0
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Update animation state
        frame_index = (frame_index + 1) % TOTAL_FRAMES
        points_3d = get_animation_frame(frame_index)
        
        # Drawing
        screen.fill(BACKGROUND_COLOR)
        
        for p3d in points_3d:
            x, y, radius = project_3d_to_2d(p3d)
            pygame.draw.circle(screen, POINT_COLOR, (x, y), radius)
            
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()
