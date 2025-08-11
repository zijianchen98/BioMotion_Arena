import pygame
import math
import sys

def main():
    # Initialize Pygame
    pygame.init()
    
    # Screen dimensions
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Point-Light Biological Motion: Happy Woman Lying Down")
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Frames per second
    clock = pygame.time.Clock()
    fps = 30
    
    # Define base positions for 15 points (lying horizontally).
    # (x, y) coordinates relative to screen center.
    # A simple arrangement with torso in the middle, arms and legs extended.
    #               1. Head
    #               2. Neck
    #               3. Right Shoulder
    #               4. Right Elbow
    #               5. Right Hand
    #               6. Left Shoulder
    #               7. Left Elbow
    #               8. Left Hand
    #               9. Hip Center
    #              10. Right Hip
    #              11. Right Knee
    #              12. Right Foot
    #              13. Left Hip
    #              14. Left Knee
    #              15. Left Foot
    base_points = [
        (0, -70),   # Head
        (0, -50),   # Neck
        (20, -50),  # Right Shoulder
        (40, -50),  # Right Elbow
        (60, -50),  # Right Hand
        (-20, -50), # Left Shoulder
        (-40, -50), # Left Elbow
        (-60, -50), # Left Hand
        (0, 0),     # Hip Center
        (15, 0),    # Right Hip
        (25, 30),   # Right Knee
        (25, 60),   # Right Foot
        (-15, 0),   # Left Hip
        (-25, 30),  # Left Knee
        (-25, 60),  # Left Foot
    ]
    
    # Shift to screen center
    def shift_to_screen_center(points):
        shifted = []
        for (x, y) in points:
            shifted.append((x + screen_width // 2, y + screen_height // 2))
        return shifted
    
    # Generate updated positions for realistic, subtle "breathing" and slight limb adjustments
    # t is time in seconds
    def get_points(t):
        # We'll gently oscillate the torso and limbs
        # For a "lying down" breath-like motion:
        #   - Chest region (neck to hips) moves slightly up/down
        #   - Arms and legs sway gently as if at rest
        
        # Breathing amplitude and frequency
        breath_amp = 5.0
        breath_freq = 1.0
        
        # Limb sway amplitude and frequency
        limb_amp = 10.0
        limb_freq = 0.5
        
        # Time-based offsets
        breath_offset = breath_amp * math.sin(2 * math.pi * breath_freq * t)
        limb_offset = limb_amp * math.sin(2 * math.pi * limb_freq * t)
        
        updated = []
        
        # We'll define which points should move with "breathing" vs. limb sway:
        #   torso_indices = [1, 2, 3, 6, 9]  # neck, shoulders, hip center
        #   arms_indices_right = [3, 4, 5]
        #   arms_indices_left = [6, 7, 8]
        #   legs_indices_right = [10, 11, 12]
        #   legs_indices_left = [13, 14, 15]
        # We'll just apply partial offsets for each region.
        
        for i, (bx, by) in enumerate(base_points, start=1):
            # Torso region: slight vertical offset
            if i in [1, 2, 3, 6, 9]:
                px = bx
                py = by + breath_offset
            # Right arm region
            elif i in [4, 5]:
                px = bx
                py = by + 0.3 * limb_offset
            # Left arm region
            elif i in [7, 8]:
                px = bx
                py = by - 0.3 * limb_offset
            # Right leg region
            elif i in [10, 11, 12]:
                px = bx
                py = by + 0.2 * limb_offset
            # Left leg region
            elif i in [13, 14, 15]:
                px = bx
                py = by - 0.2 * limb_offset
            else:
                px, py = bx, by
            
            updated.append((px, py))
        
        return shift_to_screen_center(updated)
    
    running = True
    start_ticks = pygame.time.get_ticks()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        # Calculate elapsed time in seconds
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        t = elapsed_ms / 1000.0
        
        # Fill screen with black
        screen.fill(BLACK)
        
        # Fetch updated points
        points_to_draw = get_points(t)
        
        # Draw 15 white point-lights
        for (x, y) in points_to_draw:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(fps)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()