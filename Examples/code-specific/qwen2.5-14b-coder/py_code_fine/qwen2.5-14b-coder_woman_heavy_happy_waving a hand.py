
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5

# Happy woman waving hand parameters
HAND_START_ANGLE = math.radians(90)
HAND_END_ANGLE = math.radians(45)
WAVE_DURATION = 2000  # milliseconds

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Happy Woman Waving Hand")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def draw_point_light(x, y):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), LIGHT_RADIUS)

def get_hand_position(angle, arm_length=100):
    x = SCREEN_WIDTH // 2 + arm_length * math.cos(angle)
    y = SCREEN_HEIGHT // 2 + arm_length * math.sin(angle)
    return x, y

def main():
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time

        if elapsed_time > WAVE_DURATION:
            start_time = current_time  # Reset the start time for the next wave

        # Calculate the angle of the hand based on elapsed time
        progress = min(elapsed_time / WAVE_DURATION, 1)
        hand_angle = HAND_START_ANGLE + (HAND_END_ANGLE - HAND_START_ANGLE) * progress

        # Calculate positions of the point lights
        lights_positions = []
        for i in range(NUM_LIGHTS):
            angle_offset = (i / (NUM_LIGHTS - 1)) * math.pi / 4
            light_angle = hand_angle + angle_offset
            light_x, light_y = get_hand_position(light_angle)
            lights_positions.append((light_x, light_y))

        # Draw the background
        screen.fill(BLACK)

        # Draw the point lights
        for x, y in lights_positions:
            draw_point_light(x, y)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
