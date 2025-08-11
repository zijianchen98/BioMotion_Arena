
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forward Roll Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FPS control
clock = pygame.time.Clock()
FPS = 30

# Body points in relative coordinates (head, shoulders, elbows, wrists, torso, hips, knees, ankles, feet)
# Belly (torso) is at (0, 0) in relative coordinates
points_rel = [
    (0, -40),    # head
    (-25, -30),  # left shoulder
    (25, -30),   # right shoulder
    (-35, -15),  # left elbow
    (35, -15),   # right elbow
    (-40, 10),   # left wrist
    (40, 10),    # right wrist
    (0, -15),    # upper torso (chest)
    (0, 0),      # torso (belly)
    (-20, 15),   # left hip
    (20, 15),    # right hip
    (-20, 30),   # left knee
    (20, 30),    # right knee
    (-20, 45),   # left ankle
    (20, 45)     # right ankle
]

# Scale factor for visibility
SCALE = 6
# Radius of the point-lights
POINT_RADIUS = 5

# Compute the maximum radius (from belly to farthest point) for the roll
max_radius = 0
for (x, y) in points_rel:
    dist = math.sqrt(x**2 + y**2)
    if dist > max_radius:
        max_radius = dist

# Total displacement during roll (circumference)
total_displacement = 2 * math.pi * max_radius

# Initial positions (centered on screen)
initial_x = WIDTH // 2
initial_y = HEIGHT // 2

# Main animation loop
def main():
    total_frames = 300  # Total frames for animation
    frame = 0
    
    running = True
    while running and frame <= total_frames:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        t = frame / total_frames
        current_points = []
        
        if t < 0.25:  # Transition to tucked
            s = t / 0.25
            # Interpolate to tucked position (scale points closer to belly)
            for (x_rel, y_rel) in points_rel:
                x_tucked = x_rel * (1 - 0.5 * s)
                y_tucked = y_rel * (1 - 0.5 * s)
                # Convert to screen coordinates
                x_screen = initial_x + x_tucked * SCALE
                y_screen = initial_y + y_tucked * SCALE
                current_points.append((x_screen, y_screen))
                
        elif t < 0.75:  # Roll phase
            s = (t - 0.25) / 0.5
            # Angle in radians (360° roll)
            angle = s * 2 * math.pi
            # Calculate forward displacement
            displacement = s * total_displacement * SCALE
            center_x = initial_x + displacement
            
            # Rotate points around belly
            for (x_rel, y_rel) in points_rel:
                x_rot = x_rel * math.cos(angle) - y_rel * math.sin(angle)
                y_rot = x_rel * math.sin(angle) + y_rel * math.cos(angle)
                # Convert to screen coordinates
                x_screen = center_x + x_rot * SCALE
                y_screen = initial_y + y_rot * SCALE
                current_points.append((x_screen, y_screen))
                
        else:  # Transition back to upright
            s = (t - 0.75) / 0.25
            # Calculate total displacement for the end of the roll
            displacement = total_displacement * SCALE
            center_x = initial_x + displacement
            
            # Interpolate from tucked to upright
            for (x_rel, y_rel) in points_rel:
                x_tucked = x_rel * 0.5 * (1 - s)
                y_tucked = y_rel * 0.5 * (1 - s)
                # Convert to screen coordinates
                x_screen = center_x + x_tucked * SCALE
                y_screen = initial_y + y_tucked * SCALE
                current_points.append((x_screen, y_screen))
        
        # Drawing
        screen.fill(BLACK)
        for (x, y) in current_points:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
