
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions for the sad man
# Head, shoulders, elbows, wrists, hips, knees, and feet
positions = [
    np.array([400, 100]),  # head
    np.array([400, 150]),  # shoulder (left)
    np.array([370, 150]),  # elbow (left)
    np.array([340, 150]),  # wrist (left)
    np.array([400, 150]),  # shoulder (right)
    np.array([430, 150]),  # elbow (right)
    np.array([460, 150]),  # wrist (right)
    np.array([400, 200]),  # hip (left)
    np.array([370, 250]),  # knee (left)
    np.array([340, 300]),  # foot (left)
    np.array([400, 200]),  # hip (right)
    np.array([430, 250]),  # knee (right)
    np.array([460, 300]),  # foot (right)
]

# Animation parameters
jump_height = 50
jump_duration = 30
frame_rate = 30

def jump_animation():
    for frame in range(jump_duration):
        # Clear the screen
        screen.fill(BLACK)
        
        # Calculate vertical position for jumping
        jump_offset = np.sin(np.pi * frame / jump_duration) * jump_height
        
        # Draw point-lights
        for pos in positions:
            # Update Y position to create jumping effect
            point_light_pos = pos + np.array([0, -jump_offset])
            pygame.draw.circle(screen, WHITE, point_light_pos.astype(int), 5)
        
        # Update the display
        pygame.display.flip()
        pygame.time.delay(1000 // frame_rate)
        
def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Run the animation
        jump_animation()

    pygame.quit()

if __name__ == "__main__":
    main()
