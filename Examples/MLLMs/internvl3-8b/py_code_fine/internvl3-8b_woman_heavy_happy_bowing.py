
import pygame

def animate_happy_woman():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    pygame.key.set_repeat(1, 100)
    clock = pygame.time.Clock()

    # Define the initial positions of the 15 points
    points = [
        (100, 100), (110, 100), (120, 90), (125, 110), (115, 125),
        (110, 120), (130, 130), (140, 125), (150, 130), (155, 125),
        (140, 110), (135, 100), (130, 80), (125, 70), (140, 70)
    ]

    # Define the velocities for each point
    velocities = [(-1, -1), (-1, -2), (3, -1), (-1, -1), (2, -3),
                  (2, 0), (1, -3), (-2, 2), (-3, -4), (3, 2),
                  (1, -2), (2, 1), (1, 0), (-1, 1), (-3, 2)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the positions of the points
        new_points = []
        for p, v in zip(points, velocities):
            new_p = (p[0] + v[0], p[1] + v[1])
            new_points.append(new_p)

        # Wrap around the edges
        for i in range(len(new_points)):
            p = new_points[i]
            if p[0] < 0:
                new_points[i] = (width, p[1])
            if p[0] > width:
                new_points[i] = (0, p[1])
            if p[1] < 0:
                new_points[i] = (p[0], height)
            if p[1] > height:
                new_points[i] = (p[0], 0)

        # Draw the points
        screen.fill((0, 0, 0))
        for point in new_points:
            pygame.draw.circle(screen, (255, 255, 255), point, 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

animate_happy_woman()
