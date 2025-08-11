
import pygame
import math
import sys

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Point-Light Running Animation")

    clock = pygame.time.Clock()
    FPS = 30
    duration = 5
    frames = duration * FPS
    frame_count = 0

    point_color = (255, 255, 255)
    background_color = (0, 0, 0)

    cycle_length = 30
    bounce_amplitude = 20
    shoulder_amplitude = 35
    hip_amplitude = 40
    knee_amplitude = 65

    while frame_count < frames:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        t = frame_count % cycle_length
        progress = 2 * math.pi * t / cycle_length
        bounce = bounce_amplitude * math.sin(progress)
        root_x = 400
        root_y = 300 + bounce

        neck_length = 20
        head_radius = 15
        neck_x = root_x
        neck_y = root_y - neck_length
        head_x = root_x
        head_y = neck_y - head_radius

        shoulder_width = 40
        left_shoulder_x = neck_x - shoulder_width / 2
        left_shoulder_y = neck_y
        right_shoulder_x = neck_x + shoulder_width / 2
        right_shoulder_y = neck_y

        upper_arm_length = 40
        left_shoulder_angle = 90 + shoulder_amplitude * math.sin(progress)
        left_elbow_x = left_shoulder_x + math.cos(math.radians(left_shoulder_angle)) * upper_arm_length
        left_elbow_y = left_shoulder_y + math.sin(math.radians(left_shoulder_angle)) * upper_arm_length

        forearm_length = 30
        elbow_angle_offset = 45
        left_forearm_angle = left_shoulder_angle - elbow_angle_offset
        left_wrist_x = left_elbow_x + math.cos(math.radians(left_forearm_angle)) * forearm_length
        left_wrist_y = left_elbow_y + math.sin(math.radians(left_forearm_angle)) * forearm_length

        right_shoulder_angle = 90 - shoulder_amplitude * math.sin(progress)
        right_elbow_x = right_shoulder_x + math.cos(math.radians(right_shoulder_angle)) * upper_arm_length
        right_elbow_y = right_shoulder_y + math.sin(math.radians(right_shoulder_angle)) * upper_arm_length

        right_forearm_angle = right_shoulder_angle - elbow_angle_offset
        right_wrist_x = right_elbow_x + math.cos(math.radians(right_forearm_angle)) * forearm_length
        right_wrist_y = right_elbow_y + math.sin(math.radians(right_forearm_angle)) * forearm_length

        hip_width = 40
        left_hip_x = root_x - hip_width / 2
        left_hip_y = root_y
        right_hip_x = root_x + hip_width / 2
        right_hip_y = root_y

        thigh_length = 40
        calf_length = 40
        left_hip_angle = 90 - hip_amplitude * math.sin(progress)
        left_knee_x = left_hip_x + math.cos(math.radians(left_hip_angle)) * thigh_length
        left_knee_y = left_hip_y + math.sin(math.radians(left_hip_angle)) * thigh_length

        if left_hip_angle < 90:
            knee_angle_factor = (90 - left_hip_angle) / hip_amplitude
            knee_angle = knee_amplitude * knee_angle_factor
        else:
            knee_angle = 0
        left_ankle_x = left_knee_x + math.cos(math.radians(left_hip_angle + knee_angle - 180)) * calf_length
        left_ankle_y = left_knee_y + math.sin(math.radians(left_hip_angle + knee_angle - 180)) * calf_length

        right_hip_angle = 90 + hip_amplitude * math.sin(progress)
        right_knee_x = right_hip_x + math.cos(math.radians(right_hip_angle)) * thigh_length
        right_knee_y = right_hip_y + math.sin(math.radians(right_hip_angle)) * thigh_length

        if right_hip_angle < 90:
            knee_angle_factor = (90 - right_hip_angle) / hip_amplitude
            knee_angle = knee_amplitude * knee_angle_factor
        else:
            knee_angle = 0
        right_ankle_x = right_knee_x + math.cos(math.radians(right_hip_angle + knee_angle - 180)) * calf_length
        right_ankle_y = right_knee_y + math.sin(math.radians(right_hip_angle + knee_angle - 180)) * calf_length

        points = [
            (head_x, head_y),
            (neck_x, neck_y),
            (left_shoulder_x, left_shoulder_y),
            (right_shoulder_x, right_shoulder_y),
            (left_elbow_x, left_elbow_y),
            (right_elbow_x, right_elbow_y),
            (left_wrist_x, left_wrist_y),
            (right_wrist_x, right_wrist_y),
            (root_x, root_y),
            (left_hip_x, left_hip_y),
            (right_hip_x, right_hip_y),
            (left_knee_x, left_knee_y),
            (right_knee_x, right_knee_y),
            (left_ankle_x, left_ankle_y),
            (right_ankle_x, right_ankle_y)
        ]

        screen.fill(background_color)
        for point in points:
            pygame.draw.circle(screen, point_color, (int(point[0]), int(point[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
