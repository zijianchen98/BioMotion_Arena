
import pygame
import sys
import numpy as np

# Assuming we have a function to load and parse BVH data
# This is a placeholder for the actual data loading logic
def load_motion_data():
    # Example: return a list of frames, each frame is a list of 15 (x, y) tuples
    # For demonstration, we'll use dummy data
    num_frames = 100
    points_per_frame = 15
    motion_data = []
    for frame in range(num_frames):
        frame_data = []
        for point in range(points_per_frame):
            # Simulate movement: points move downwards to simulate sitting
            x = point * 40 + 100  # Spread points horizontally
            y = 100 + frame * 2   # Move points downwards over time
            frame_data.append((x, y))
        motion_data.append(frame_data)
    return motion_data

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    motion_data = load_motion_data()
    num_frames = len(motion_data)
    current_frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Black background

        # Draw the 15 points for the current frame
        for point in motion_data[current_frame]:
            pygame.draw.circle(screen, (255, 255, 255), point, 5)  # White points

        pygame.display.flip()
        clock.tick(30)  # 30 FPS

        current_frame = (current_frame + 1) % num_frames

if __name__ == "__main__":
    main()
