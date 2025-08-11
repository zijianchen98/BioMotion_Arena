
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set up the point light
point_light = pygame.rect.Rect((0, 0, 10, 10))
velocity = pygame.math.Vector2(2, 2)

def draw_point_light():
    pygame.draw.rect(screen, (255, 255, 255), point_light)

def move_point_light():
    point_light.move_ip(velocity)

    # Bounce the point light off the edges of the screen
    if point_light.left < 0 or point_light.right > WIDTH:
        velocity[0] *= -1
    if point_light.top < 0 or point_light.bottom > HEIGHT:
        velocity[1] *= -1

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        move_point_light()
        draw_point_light()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
