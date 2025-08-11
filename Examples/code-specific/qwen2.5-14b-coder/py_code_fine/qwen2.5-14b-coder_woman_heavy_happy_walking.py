
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Woman Walking Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point-light properties
num_lights = 15
lights = []

# Initial positions and velocities for the point-lights
for i in range(num_lights):
    x = width // 2 + (i - num_lights // 2) * 10
    y = height // 2
    lights.append({'x': x, 'y': y, 'vx': 0, 'vy': 0})

# Animation parameters
frame_rate = 60
clock = pygame.time.Clock()
running = True

def update_positions(lights, dt):
    # Update positions based on velocities
    for light in lights:
        light['x'] += light['vx'] * dt
        light['y'] += light['vy'] * dt

def apply_gravity(lights, dt):
    # Simple gravity effect
    for light in lights:
        light['vy'] += 9.8 * dt

def apply_friction(lights, friction):
    # Apply friction to slow down the movement
    for light in lights:
        light['vx'] *= friction
        light['vy'] *= friction

def calculate_velocity(lights, target_x, target_y, speed):
    # Calculate velocity to move towards the target position
    for light in lights:
        dx = target_x - light['x']
        dy = target_y - light['y']
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 0:
            light['vx'] = (dx / distance) * speed
            light['vy'] = (dy / distance) * speed

def animate():
    global running
    frame_count = 0
    step = 0
    steps_per_cycle = 100
    cycle_length = 10  # seconds
    speed = 200  # pixels per second
    friction = 0.98

    while running:
        dt = clock.get_time() / 1000.0
        screen.fill(black)

        # Calculate target position for the current step
        target_x = width // 2 + (step - steps_per_cycle // 2) * 10
        target_y = height // 2 + 50 * math.sin(step / 10.0)

        # Update velocities
        calculate_velocity(lights, target_x, target_y, speed)

        # Apply gravity and friction
        apply_gravity(lights, dt)
        apply_friction(lights, friction)

        # Update positions
        update_positions(lights, dt)

        # Draw point-lights
        for light in lights:
            pygame.draw.circle(screen, white, (int(light['x']), int(light['y'])), 5)

        pygame.display.flip()
        clock.tick(frame_rate)

        # Increment step and handle cycling
        step += 1
        if step >= steps_per_cycle:
            step = 0

        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    animate()
    pygame.quit()
