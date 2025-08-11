
import pygame
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Jumping")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
PERIOD = 2.5  # Jump cycle duration in seconds
JUMP_HEIGHT = 80  # Vertical displacement
GROUND_LEVEL = height - 150  # Base vertical position

def get_jump_position(t):
    phase = (t % PERIOD) / PERIOD
    y = GROUND_LEVEL - JUMP_HEIGHT * (4 * (phase - 0.5)**2)
    return y

def main():
    running = True
    time_elapsed = 0.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        dt = clock.tick(60) / 1000.0
        time_elapsed += dt

        # Calculate central hip position
        hip_y = get_jump_position(time_elapsed)
        hip_x = width // 2

        # Generate point positions
        points = []

        # Head
        points.append((hip_x, hip_y - 50))

        # Shoulders
        points.append((hip_x - 30, hip_y - 30))
        points.append((hip_x + 30, hip_y - 30))

        # Elbows with dynamic swing
        arm_phase = math.sin(2 * math.pi * time_elapsed / PERIOD)
        points.append((hip_x - 50 - arm_phase*20, hip_y - 10))
        points.append((hip_x + 50 + arm_phase*20, hip_y - 10))

        # Hands with follow-through motion
        hand_phase = math.sin(2 * math.pi * time_elapsed / PERIOD + math.pi/2)
        points.append((hip_x - 70 - arm_phase*15, hip_y + 20 + hand_phase*25))
        points.append((hip_x + 70 + arm_phase*15, hip_y + 20 + hand_phase*25))

        # Hips
        points.append((hip_x, hip_y))

        # Knees with bending motion
        knee_phase = math.sin(2 * math.pi * time_elapsed / PERIOD)
        points.append((hip_x - 20, hip_y + 50 + knee_phase*30))
        points.append((hip_x + 20, hip_y + 50 + knee_phase*30))

        # Ankles
        points.append((hip_x - 20, hip_y + 100))
        points.append((hip_x + 20, hip_y + 100))

        # Feet with push-off/lift motion
        foot_phase = math.sin(2 * math.pi * time_elapsed / PERIOD + math.pi)
        points.append((hip_x - 30, hip_y + 120 + foot_phase*20))
        points.append((hip_x + 30, hip_y + 120 + foot_phase*20))

        # Torso midpoint
        points.append((hip_x, hip_y - 15))

        # Draw all points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
