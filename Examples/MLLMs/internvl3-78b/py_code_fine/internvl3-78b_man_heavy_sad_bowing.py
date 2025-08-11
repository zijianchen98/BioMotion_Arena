
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Sadman Bowing Animation")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the frame rate
clock = pygame.time.Clock()
fps = 30

# Set up the points
points = [
    (200, 100), (180, 150), (220, 150), (160, 200), (240, 200), (200, 250), 
    (170, 250), (230, 250), (140, 300), (260, 300), (200, 350), (180, 350), 
    (220, 350), (160, 400), (240, 400)
]

# Animation parameters
frame_count = 0
bowing_frames = 30

def draw_points(points):
    for point in points:
        pygame.draw.circle(screen, white, point, 5)

def update_points(points, frame_count):
    new_points = []
    for x, y in points:
        amplitude = 20
        frequency = 0.5
        wave = (amplitude * pygame.math.Vector2(0, 1).rotate(frame_count * frequency)).y
        new_y = y + wave
        new_points.append((x, int(new_y)))
    return new_points

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    points = update_points(points, frame_count % bowing_frames)
    draw_points(points)
    pygame.display.flip()

    frame_count += 1
    clock.tick(fps)

pygame.quit()
sys.exit()
