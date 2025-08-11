
import pygame
import math

# Constants
WIDTH, HEIGHT = 600, 600
BG_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Fixed positions
fixed_positions = {
    'left_hip': (280, 300),
    'right_hip': (320, 300),
    'left_knee': (280, 450),
    'right_knee': (320, 450),
    'hip_center': (300, 300),
}

# Hierarchy with parents and offsets
hierarchy = {
    'lower_spine': ('hip_center', (0, -50)),
    'middle_spine': ('lower_spine', (0, -50)),
    'upper_spine': ('middle_spine', (0, -50)),
    'neck': ('upper_spine', (0, -50)),
    'head': ('neck', (0, -50)),
    'left_shoulder': ('upper_spine', (-50, 0)),
    'right_shoulder': ('upper_spine', (50, 0)),
    'left_elbow': ('left_shoulder', (0, 100)),
    'right_elbow': ('right_shoulder', (0, 100)),
    'left_wrist': ('left_elbow', (0, 100)),
    'right_wrist': ('right_elbow', (0, 100)),
}

# Points to draw
points_to_draw = ['head', 'neck', 'upper_spine', 'middle_spine', 'lower_spine',
                  'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
                  'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee']

# Function to compute position based on hierarchy and rotation
def get_position(point, theta, cache):
    if point in fixed_positions:
        return fixed_positions[point]
    if point in cache:
        return cache[point]
    parent, offset = hierarchy[point]
    parent_pos = get_position(parent, theta, cache)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    rotated_offset = (offset[0] * cos_theta + offset[1] * sin_theta,
                      -offset[0] * sin_theta + offset[1] * cos_theta)
    position = (parent_pos[0] + rotated_offset[0], parent_pos[1] + rotated_offset[1])
    cache[point] = position
    return position

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    t = 0
    T = 2000  # Period in milliseconds
    theta_max = math.radians(11.25)  # Maximum rotation angle per segment

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute theta for the current time
        theta = theta_max * (1 - math.cos(2 * math.pi * t / T)) / 2

        # Compute positions
        cache = {}
        positions = {point: get_position(point, theta, cache) for point in points_to_draw}

        # Draw
        screen.fill(BG_COLOR)
        for pos in positions.values():
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)
        pygame.display.flip()

        # Update time
        t = (t + clock.tick(60)) % T

    pygame.quit()

if __name__ == '__main__':
    main()
