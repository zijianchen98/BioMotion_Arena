
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Animation of Sitting Down")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Define the positions for each point in the three keyframes
# Each point has positions for standing, intermediate, and sitting
points = [
    # head
    [(200, 50), (200, 100), (200, 150)],
    # left shoulder
    [(180, 100), (180, 150), (180, 200)],
    # right shoulder
    [(220, 100), (220, 150), (220, 200)],
    # left elbow
    [(180, 150), (180, 200), (180, 250)],
    # right elbow
    [(220, 150), (220, 200), (220, 250)],
    # left wrist
    [(180, 200), (180, 250), (180, 300)],
    # right wrist
    [(220, 200), (220, 250), (220, 300)],
    # left hip
    [(190, 200), (190, 250), (190, 300)],
    # right hip
    [(210, 200), (210, 250), (210, 300)],
    # left knee
    [(190, 275), (165, 287.5), (140, 300)],
    # right knee
    [(210, 275), (235, 287.5), (260, 300)],
    # left ankle
    [(190, 350), (165, 350), (140, 350)],
    # right ankle
    [(210, 350), (235, 350), (260, 350)],
    # left foot
    [(185, 355), (160, 355), (135, 355)],
    # right foot
    [(215, 355), (240, 355), (265, 355)],
]

# Function to calculate the position of a point at a given frame t
def get_position(t, pos1, pos2, pos3, segment_frames=45):
    if t <= segment_frames:
        ratio = t / segment_frames
        x = pos1[0] + (pos2[0] - pos1[0]) * ratio
        y = pos1[1] + (pos2[1] - pos1[1]) * ratio
    else:
        ratio = (t - segment_frames) / segment_frames
        x = pos2[0] + (pos3[0] - pos2[0]) * ratio
        y = pos2[1] + (pos3[1] - pos2[1]) * ratio
    return (int(x), int(y))

# Main animation loop
running = True
t = 0
total_frames = 90  # Total frames for the animation

while running and t <= total_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw each point
    for point in points:
        pos1, pos2, pos3 = point
        pos = get_position(t, pos1, pos2, pos3)
        pygame.draw.circle(screen, (255, 255, 255), pos, 5)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # 30 frames per second

    # Increment the frame counter
    t += 1

# Quit Pygame
pygame.quit()
