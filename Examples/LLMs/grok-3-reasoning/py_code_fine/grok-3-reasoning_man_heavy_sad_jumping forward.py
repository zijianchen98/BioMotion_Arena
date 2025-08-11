
import pygame

# Initialize Pygame
pygame.init()

# Set up window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_title("Point-Light Stimulus Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Frame rate
fps = 60
clock = pygame.time.Clock()

# Define key postures
# Standing posture at x=0
points_standing = [
    (0, 1.0),  # head
    (0, 0.95),  # neck
    (0, 0.7),  # torso_center
    (-0.1, 0.9),  # left_shoulder
    (0.1, 0.9),  # right_shoulder
    (-0.1, 0.6),  # left_elbow
    (0.1, 0.6),  # right_elbow
    (-0.1, 0.3),  # left_wrist
    (0.1, 0.3),  # right_wrist
    (-0.05, 0.5),  # left_hip
    (0.05, 0.5),  # right_hip
    (-0.05, 0.25),  # left_knee
    (0.05, 0.25),  # right_knee
    (-0.05, 0),  # left_ankle
    (0.05, 0),  # right_ankle
]

# Crouched posture at x=0
points_crouched = [
    (0, 0.8),  # head
    (0, 0.75),  # neck
    (0, 0.5),  # torso_center
    (-	            # left_shoulder
    (-0.1, 0.7),  # left_shoulder
    (0.1, 0.7),  # right_shoulder
    (-0.1, 0.5),  # left_elbow
    (0.1, 0.5),  # right_elbow
    (-0.1, 0.3),  # left_wrist
    (0.1, 0.3),  # right_wrist
    (-0.05, 0.3),  # left_hip
    (0.05, 0.3),  # right_hip
    (-0.05, 0.1),  # left_knee
    (0.05, 0.1),  # right_knee
    (-0.05, 0),  # left_ankle
    (0.05, 0),  # right_ankle
]

# Flight posture offsets from torso_center
flight_offsets = [
    (0, 0.3),  # head
    (0, 0.25),  # neck
    (0, 0),  # torso_center
    (-0.1, 0.2),  # left_shoulder
    (0.1, 0.2),  # right_shoulder
    (-0.15, 0.1),  # left_elbow
    (0.15, 0.1),  # right_elbow
    (-0.2, 0.05),  # left_wrist
    (0.2, 0.05),  # right_wrist
    (-0.05, -0.2),  # left_hip
    (0.05, -0.2),  # right_hip
    (-0.1, -0.3),  # left_knee
    (0.1, -0.3),  # right_knee
    (-0.15, -0.4),  # left_ankle
    (0.15, -0.4),  # right_ankle
]

# Function to convert (x,y) to pixel coordinates
def to_pixels(x, y):
    px = 100 + x * 600
    py = 550 - y * 375
    return int(px), int(py)

# Function to get positions at time t
def get_positions(t):
    if t < 0.2:
        # Standing
        return points_standing
    elif t < 0.4:
        # Interpolate between standing and crouched
        alpha = (t - 0.2) / 0.2
        positions = []
        for p1, p2 in zip(points_standing, points_crouched):
            x = p1[0] * (1 - alpha) + p2[0] * alpha
            y = p1[1] * (1 - alpha) + p2[1] * alpha
            positions.append((x, y))
        return positions
    elif t < 0.6:
        # Interpolate between crouched and standing (takeoff)
        alpha = (t - 0.4) / 0.2
        positions = []
        for p1, p2 in zip(points_crouched, points_standing):
            x = p1[0] * (1 - alpha) + p2[0] * alpha
            y = p1[1] * (1 - alpha) + p2[1] * alpha
            positions.append((x, y))
        # Shift x by 0.1 * alpha
        dx = 0.1 * alpha
        positions = [(x + dx, y) for x, y in positions]
        return positions
    elif t < 1.4:
        # Flight
        dt = t - 0.6
        x_torso = 0.1 + 1.0 * dt
        y_torso = 0.7 + 1.0 * dt - 0.5 * 2.5 * dt**2
        positions = []
        for dx, dy in flight_offsets:
            positions.append((x_torso + dx, y_torso + dy))
        return positions
    elif t < 1.6:
        # Interpolate between flight at t=1.4 and crouched at x=0.9
        dt = 1.4 - 0.6
        x_torso_flight = 0.1 + 1.0 * dt
        y_torso_flight = 0.7 + 1.0 * dt - 0.5 * 2.5 * dt**2
        positions_flight = [(x_torso_flight + dx, y_torso_flight + dy) for dx, dy in flight_offsets]
        # Crouched posture at x=0.9
        points_crouched_landed = [(x + 0.9, y) for x, y in points_crouched]
        alpha = (t - 1.4) / 0.2
        positions = []
        for p1, p2 in zip(positions_flight, points_crouched_landed):
            x = p1[0] * (1 - alpha) + p2[0] * alpha
            y = p1[1] * (1 - alpha) + p2[1] * alpha
            positions.append((x, y))
        return positions
    else:
        # Standing at x=1.0
        points_standing_final = [(x + 1.0, y) for x, y in points_standing]
        return points_standing_final

# Main loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Get positions
    positions = get_positions(t)

    # Draw points
    for x, y in positions:
        px, py = to_pixels(x, y)
        pygame.draw.circle(screen, white, (px, py), 5)

    # Update display
    pygame.display.flip()

    # Advance time
    t += 1 / fps
    if t > 2.0:
        t = 0  # Loop the animation

    # Wait for next frame
    clock.tick(fps)

pygame.quit()
