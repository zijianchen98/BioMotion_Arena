
import pygame
import sys
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 6

# --- Animation Data ---
# 15 points representing a sad woman with heavy weight jumping up.
# The motion is characterized by a slouched posture, a slow and deep preparation,
# a low-effort jump, and a heavy landing with a slow recovery.
#
# Point order:
# 0: Head, 1: Neck, 2: L Shoulder, 3: R Shoulder, 4: L Elbow, 5: R Elbow,
# 6: L Wrist, 7: R Wrist, 8: Pelvis, 9: L Hip, 10: R Hip, 11: L Knee,
# 12: R Knee, 13: L Ankle, 14: R Ankle

ANIMATION_DURATION = 3200  # in milliseconds

KEYFRAMES = [
    {
        "time": 0,  # 0. Initial sad stance
        "coords": [
            (400, 230), (400, 270), (360, 280), (440, 280), (350, 350),
            (450, 350), (345, 410), (455, 410), (400, 380), (370, 385),
            (430, 385), (360, 465), (440, 465), (370, 550), (430, 550)
        ]
    },
    {
        "time": 1000, # 1. Deep crouch (preparation)
        "coords": [
            (400, 330), (400, 370), (350, 380), (450, 380), (320, 420),
            (480, 420), (300, 450), (500, 450), (400, 450), (370, 455),
            (430, 455), (330, 500), (470, 500), (370, 550), (430, 550)
        ]
    },
    {
        "time": 1300, # 2. Takeoff (extension)
        "coords": [
            (400, 200), (400, 240), (360, 250), (440, 250), (330, 290),
            (470, 290), (310, 340), (490, 340), (400, 350), (370, 355),
            (430, 355), (365, 450), (435, 450), (370, 550), (430, 550)
        ]
    },
    {
        "time": 1600, # 3. Peak of the jump (low height)
        "coords": [
            (400, 180), (400, 220), (360, 230), (440, 230), (340, 290),
            (460, 290), (330, 350), (470, 350), (400, 320), (370, 325),
            (430, 325), (360, 400), (440, 400), (370, 480), (430, 480)
        ]
    },
    {
        "time": 1900, # 4. Heavy landing (impact absorption)
        "coords": [
            (400, 330), (400, 370), (350, 380), (450, 380), (280, 390),
            (520, 390), (230, 400), (570, 400), (400, 450), (370, 455),
            (430, 455), (330, 500), (470, 500), (370, 550), (430, 550)
        ]
    },
    {
        "time": 3200, # 5. Return to sad stance (slow recovery)
        "coords": [
            (400, 230), (400, 270), (360, 280), (440, 280), (350, 350),
            (450, 350), (345, 410), (455, 410), (400, 380), (370, 385),
            (430, 385), (360, 465), (440, 465), (370, 550), (430, 550)
        ]
    }
]

def smoothstep(t):
    """A smooth interpolation function (hermite interpolation)."""
    return t * t * (3.0 - 2.0 * t)

def lerp(p1, p2, t):
    """Linear interpolation between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return x1 + (x2 - x1) * t, y1 + (y2 - y1) * t

def get_current_pose(time):
    """Calculates the pose at a specific time by interpolating between keyframes."""
    
    # Find the segment of the animation we are in
    start_frame = None
    end_frame = None
    for i in range(len(KEYFRAMES) - 1):
        if KEYFRAMES[i]["time"] <= time < KEYFRAMES[i+1]["time"]:
            start_frame = KEYFRAMES[i]
            end_frame = KEYFRAMES[i+1]
            break
    
    if start_frame is None or end_frame is None:
        return KEYFRAMES[0]["coords"] # Default to the first frame

    # Calculate the progress (t) within the current segment
    segment_duration = end_frame["time"] - start_frame["time"]
    time_in_segment = time - start_frame["time"]
    
    if segment_duration == 0:
        t = 0
    else:
        t = time_in_segment / segment_duration
    
    # Apply smoothing function for more natural movement
    eased_t = smoothstep(t)
    
    # Interpolate each point's position
    current_coords = []
    for i in range(len(start_frame["coords"])):
        p1 = start_frame["coords"][i]
        p2 = end_frame["coords"][i]
        current_coords.append(lerp(p1, p2, eased_t))
        
    return current_coords

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Jumping Up (Heavy)")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Get the current time in the animation cycle
        current_time_ms = pygame.time.get_ticks()
        cycle_time = current_time_ms % ANIMATION_DURATION

        # Calculate the current pose
        pose_to_draw = get_current_pose(cycle_time)

        # --- Drawing ---
        screen.fill(BLACK)
        
        for point in pose_to_draw:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
