
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Walker Animation")

# Define constants
x_torso = 400
y0 = 300
A = 5  # Amplitude for torso vertical motion
B = math.pi / 6  # Hip angle amplitude
D = math.pi / 4  # Knee angle amplitude
E = math.pi / 9  # Shoulder angle amplitude
F = math.pi / 18  # Elbow angle
upper_arm_length = 40
lower_arm_length = 40
hand_length = 10
upper_leg_length = 50
lower_leg_length = 50
head_offset = 60
shoulder_width = 20
hip_width = 20
torso_height = 80

# Main loop
t = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Compute torso vertical position
    y_torso = y0 + A * math.cos(2 * t)

    # Define positions
    head = (x_torso, y_torso + head_offset)
    left_shoulder = (x_torso - shoulder.day, y_torso + torso_height / 2)
    right_shoulder = (x_torso + shoulder_width, y_torso + torso_height / 2)
    left_hip = (x_torso - hip_width, y_torso - torso_height / 2)
    right_hip = (x_torso + hip_width, y_torso - torso_height / 2)

    # Left arm
    θ_shoulder_left = -E * math.sin(t)
    left_elbow = (left_shoulder[0] + upper_arm_length * math.sin(θ_shoulder_left),
                  left_shoulder[1] - upper_arm_length * math.cos(θ_shoulder_left))
    left_wrist = (left_elbow[0] + lower_arm_length * math.sin(θ_shoulder_left + F),
                  left_elbow[1] - lower_arm_length * math.cos(θ_shoulder_left + F))
    left_hand = (left_wrist[0] + hand_length * math.sin(θ_shoulder_left + F),
                 left_wrist[1] - hand_length * math.cos(θ_shoulder_left + F))

    # Right arm
    θ_shoulder_right = E * math.sin(t)
    right_elbow = (right_shoulder[0] + upper_arm_length * math.sin(θ_shoulder_right),
                   right_shoulder[1] - upper_arm_length * math.cos(θ_shoulder_right))
    right_wrist = (right_elbow[0] + lower_arm_length * math.sin(θ_shoulder_right + F),
                   right_elbow[1] - lower_arm_length * math.cos(θ_shoulder_right + F))
    right_hand = (right_wrist[0] + hand_length * math.sin(θ_shoulder_right + F),
                  right_wrist[1] - hand_length * math.cos(θ_shoulder_right + F))

    # Left leg
    θ_hip_left = B * math.sin(t)
    θ_knee_left = D * max(0, math.sin(t))
    left_knee = (left_hip[0] + upper_leg_length * math.sin(θ_hip_left),
                 left_hip[1] - upper_leg_length * math.cos(θ_hip_left))
    left_ankle = (left_knee[0] + lower_leg_length * math.sin(θ_hip_left + θ_knee_left),
                  left_knee[1] - lower_leg_length * math.cos(θ_hip_left + θ_knee_left))

    # Right leg
    θ_hip_right = -B * math.sin(t)
    θ_knee_right = D * max(0, -math.sin(t))
    right_knee = (right_hip[0] + upper_leg_length * math.sin(θ_hip_right),
                  right_hip[1] - upper_leg_length * math.cos(θ_hip_right))
    right_ankle = (right_knee[0] + lower_leg_length * math.sin(θ_hip_right + θ_knee_right),
                   right_knee[1] - lower_leg_length * math.cos(θ_hip_right + θ_knee_right))

    # Collect all points
    points = [head, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist,
              left_hand, right_hand, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle]

    # Transform y-coordinates for Pygame (y increases downwards)
    screen_points = [(x, height - y) for (x, y) in points]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the points
    for point in screen_points:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 3)

    # Update the display
    pygame.display.flip()

    # Increment time
    t += math.pi / 60
    if t > 2 * math.pi:
        t -= 2 * math.pi

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
