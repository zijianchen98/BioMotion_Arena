
import sys
import pygame

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions are defined for each frame
frames = [
    [(200, 100), (210, 110), (220, 120), (230, 130), (240, 140),
     (260, 150), (250, 160), (270, 170), (280, 180), (200, 190), (220, 190), (250, 190), (280, 190), (180, 200), (300, 190)],

    [(200, 110), (210, 120), (220, 130), (230, 140), (240, 150),
     (260, 160), (250, 170), (270, 180), (280, 190), (200, 200), (220, 200), (250, 200), (280, 200), (180, 210), (300, 200)],

    # More frames with point-light positions over here - similar pattern
    # ...

    [(200, 580), (210, 590), (220, 600), (230, 610), (240, 620),
     (260, 630), (250, 640), (270, 650), (280, 660), (200, 670), (220, 670), (250, 670), (280, 670), (180, 680), (300, 670)]
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    frame_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point in frames[frame_index]:
            pygame.draw.circle(screen, WHITE, point, 5)

        pygame.display.flip()
        frame_index = (frame_index + 1) % len(frames)
        clock.tick(30)  # Adjust for smoother animation

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
