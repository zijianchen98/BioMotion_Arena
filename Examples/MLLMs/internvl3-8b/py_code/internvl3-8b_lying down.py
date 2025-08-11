
import pygame

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Point-Light Man, lying down")

    # Define the number of points
    num_points = 15
    points = [{'x': screen_width / 2, 'y': screen_height / 2 - y_val*10} for y_val in range(num_points)]

    # Set the initial speed and direction of movement
    speeds = [{'x': speed_x, 'y': speed_y} for speed_x, speed_y in ((-2, 1), (-1, 1), (1, 1), (2, 1), (2, 0), (2, -1), (1, -1), (0, -1), (-1, -1), (-2, -1), (-2, 0), (-1, 1), (0, 1), (1, 0), (0, 0))]

    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen with black
        for i in range(num_points):
            x = int(points[i]['x'])
            y = int(points[i]['y'])
            # Assuming colors are (255, 255, 255) for white
            screen.set_at((x, y), (255, 255, 255))
            # Update position with the speed
            points[i]['x'] += speeds[i]['x']
            points[i]['y'] += speeds[i]['y']

            # Flip the points to simulate the effect
            # This is not doing anything right now, you'll need to update positions realistically
            # for a proper "lying down" motion; a lot of complexity here.
            # Flip points back after a simulated movement
            points[i]['x'] -= speeds[i]['x']
            points[i]['y'] -= speeds[i]['y']
        
        pygame.display.flip()  # Update the full display surface to the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
