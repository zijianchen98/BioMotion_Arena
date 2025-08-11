
    # import pygame
    # import math

    # # Constants
    # WIDTH, HEIGHT = 800, 600
    # FPS = 60
    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # scale = 300  # pixels per unit

    # # Bone lengths
    # thigh_length = 0.4
    # calf_length = 0.4
    # torso_length = 0.2
    # head_length = 0.1
    # upper_arm_length = 0.3
    # forearm_length = 0.3
    # shoulder_offset = 0.1
    # hip_offset = 0.05

    # # Motion parameters
    # T = 1.0  # period in seconds
    # A_hip = math.radians(30)
    # B_knee = math.radians(60)
    # A_arm = math.radians(20)
    # theta_elbow = math.radians(45)
    # theta_torso = math.radians(10)
    # A_vertical = 0.05

    # # Initialize Pygame
    # pygame.init()
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # clock = pygame.time.Clock()
    # running = True
    # start_time = pygame.time.get_ticks() / 1000.0

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    #     # Get current time
    #     current_time = pygame.time.get_ticks() / 1000.0 - start_time
    #     t = current_time % T

    #     # Calculate angles
    #     theta_left_hip = A_hip * math.sin(2 * math.pi * t / T)
    #     theta_right_hip = A_hip * math.sin(2 * math.pi * t / T + math.pi)
    #     theta_left_knee = B_knee * (1 - math.cos(2 * math.pi * t / T))
    #     theta_right_knee = B_knee * (1 - math.cos(2 * math.pi * t / T + math.pi))
    #     theta_left_shoulder = -A_arm * math.sin(2 * math.pi * t / T)
    #     theta_right_shoulder = A_arm * math.sin(2 * math.pi * t / T)

    #     # Calculate center_hip_model
    #     center_hip_model_y = A_vertical * math.sin(4 * math.pi * t / T)
    #     center_hip_model = (0, center_hip_model_y)

    #     # Torso
    #     torso_model = (center_hip_model[0] + torso_length * math.sin(theta_torso), center_hip_model[1] + torso_length * math.cos(theta_torso))

    #     # Head
    #     head_model = (torso_model[0] + head_length * math.sin(theta_torso), torso_model[1] + head_length * math.cos(theta_torso))

    #     # Shoulders
    #     left_shoulder_model = (torso_model[0] - shoulder_offset * math.cos(theta_torso), torso_model[1] + shoulder_offset * math.sin(theta_torso))
    #     right_shoulder_model = (torso_model[0] + shoulder_offset * math.cos(theta_torso), torso_model[1] - shoulder_offset * math.sin(theta_torso))

    #     # Elbows
    #     left_elbow_model = (left_shoulder_model[0] + upper_arm_length * math.sin(theta_left_shoulder), left_shoulder_model[1] - upper_arm_length * math.cos(theta_left_shoulder))
    #     right_elbow_model = (right_shoulder_model[0] + upper_arm_length * math.sin(theta_right_shoulder), right_shoulder_model[1] - upper_arm_length * math.cos(theta_right_shoulder))

    #     # Wrists
    #     left_wrist_model = (left_elbow_model[0] + forearm_length * math.sin(theta_left_shoulder + theta_elbow), left_elbow_model[1] - forearm_length * math.cos(theta_left_shoulder + theta_elbow))
    #     right_wrist_model = (right_elbow_model[0] + forearm_length * math.sin(theta_right_shoulder + theta_elbow), right_elbow_model[1] - forearm_length * math.cos(theta_right_shoulder + theta_elbow))

    #     # Hips
    #     left_hip_model = (center_hip_model[0] - hip_offset, center_hip_model[1])
    #     right_hip_model = (center_hip_model[0] + hip_offset, center_hip_model[1])

    #     # Knees
    #     left_knee_model = (left_hip_model[0] + thigh_length * math.sin(theta_left_hip), left_hip_model[1] - thigh_length * math.cos(theta_left_hip))
    #     right_knee_model = (right_hip_model[0] + thigh_length * math.sin(theta_right_hip), right_hip_model[1] - thigh_length * math.cos(theta_right_hip))

    #     # Ankles
    #     left_ankle_model = (left_knee_model[0] + calf_length * math.sin(theta_left_hip + theta_left_knee), left_knee_model[1] - calf_length * math.cos(theta_left_hip + theta_left_knee))
    #     right_ankle_model = (right_knee_model[0] + calf_length * math.sin(theta_right_hip + theta_right_knee), right_knee_model[1] - calf_length * math.cos(theta_right_hip + theta_right_knee))

    #     # List of all points in model coordinates
    #     points_model = [
    #         center_hip_model,
    #         torso_model,
    #         head_model,
    #         left_shoulder_model,
    #         right_shoulder_model,
    #         left_elbow_model,
    #         right_elbow_model,
    #         left_wrist_model,
    #         right_wrist_model,
    #         left_hip_model,
    #         right_hip_model,
    #         left_knee_model,
    #         right_knee_model,
    #         left_ankle_model,
    #         right_ankle_model
    #     ]

    #     # Convert to screen coordinates
    #     points_screen = [(WIDTH / 2 + scale * p[0], HEIGHT / 2 - scale * p[1]) for p in points_model]

    #     # Clear screen
    #     screen.fill(BLACK)

    #     # Draw points
    #     for point in points_screen:
    #         pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    #     # Update display
    #     pygame.display.flip()

    #     # Tick clock
    #     clock.tick(FPS)

    # # Quit Pygame
    # pygame.quit()
    # 