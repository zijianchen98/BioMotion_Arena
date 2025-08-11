
import pygame
import math

def main():
    """
    This program displays a point-light animation of a person waving.
    The animation consists of 15 white points on a black background,
    simulating biological motion capture data.
    """
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    width, height = 600, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Biological Motion: Waving Hand")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Animation parameters
    clock = pygame.time.Clock()
    frame_count = 0
    running = True
    point_radius = 6

    # Define the 15 points for the skeleton's base pose.
    # The skeleton is modeled to represent a person waving with their right arm.
    # The right side of the body corresponds to the left side of the screen.
    # Indices map to body parts:
    # 0: Head, 1: Shoulder Center, 2: R Shoulder, 3: R Elbow, 4: R Wrist,
    # 5: L Shoulder, 6: L Elbow, 7: L Wrist, 8: Pelvis Center,
    # 9: R Hip, 10: R Knee, 11: R Ankle, 12: L Hip, 13: L Knee, 14: L Ankle
    base_points = [
        [300, 150],  # 0 Head
        [300, 225],  # 1 Shoulder Center
        [250, 225],  # 2 Right Shoulder (pivot)
        [270, 165],  # 3 Right Elbow (base position)
        [230, 115],  # 4 Right Wrist (wave start)
        [350, 225],  # 5 Left Shoulder
        [370, 305],  # 6 Left Elbow
        [390, 385],  # 7 Left Wrist
        [300, 400],  # 8 Pelvis Center
        [265, 400],  # 9 Right Hip
        [265, 540],  # 10 Right Knee
        [265, 680],  # 11 Right Ankle
        [335, 400],  # 12 Left Hip
        [335, 540],  # 13 Left Knee
        [335, 680],  # 14 Left Ankle
    ]

    # Define keyframe targets for the waving motion
    # The wrist will move between its base position and this target position
    wrist_start_pos = base_points[4]
    wrist_end_pos = [310, 115]

    # The elbow moves slightly for a more natural effect
    elbow_start_pos = base_points[3]
    elbow_end_pos = [270, 175]

    # Main animation loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Update Animation State ---
        frame_count += 1
        
        # Create a fresh copy of points for the current frame
        current_points = [list(p) for p in base_points]

        # 1. Add a subtle vertical bob to the whole body to simulate breathing/sway
        bob_offset = math.sin(frame_count * 0.04) * 3
        for i in range(len(current_points)):
            current_points[i][1] += bob_offset
            
        # 2. Animate the waving arm using sinusoidal interpolation
        # The wave_factor smoothly transitions from 0 to 1 and back to 0
        wave_factor = (math.sin(frame_count * 0.08) + 1) / 2.0
        
        # Interpolate Right Wrist (point 4) position
        current_points[4][0] = wrist_start_pos[0] * (1 - wave_factor) + wrist_end_pos[0] * wave_factor
        current_points[4][1] = wrist_start_pos[1] * (1 - wave_factor) + wrist_end_pos[1] * wave_factor

        # Interpolate Right Elbow (point 3) position for secondary motion
        current_points[3][0] = elbow_start_pos[0] * (1 - wave_factor) + elbow_end_pos[0] * wave_factor
        current_points[3][1] = elbow_start_pos[1] * (1 - wave_factor) + elbow_end_pos[1] * wave_factor

        # --- Render Frame ---
        screen.fill(BLACK)

        # Draw the 15 points
        for point in current_points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), point_radius)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main()
