
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_COUNT = 15

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sadman Waving Hand - Biological Motion Animation")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = 0

    def update(self, time, hand_center, hand_width, hand_height):
        # Calculate motion based on time to simulate waving hand
        self.angle = (time * 2) % (2 * math.pi)
        
        # Calculate position based on a sinusoidal motion to simulate hand waving
        wave = math.sin(self.angle)
        self.x = hand_center[0] + int(wave * hand_width * 0.5)
        self.y = hand_center[1] + int((self.angle % (2 * math.pi)) * hand_height * 0.05)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    # Create point lights around the hand
    hand_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    hand_width = 200
    hand_height = 100
    lights = [PointLight(hand_center[0], hand_center[1], 5) for _ in range(POINT_COUNT)]

    # Main loop
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Get the current time
        current_time = (pygame.time.get_ticks() - start_time) / 1000.0

        # Update and draw lights
        for light in lights:
            light.update(current_time, hand_center, hand_width, hand_height)
            light.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
