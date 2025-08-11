
import pygame
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 6

CYCLE_SPEED = 0.04
HORIZONTAL_SPEED = 0.8

SCALE = 2.5
TORSO_LENGTH = 35 * SCALE
NECK_LENGTH = 15 * SCALE
HEAD_RADIUS = 10 * SCALE
SHOULDER_WIDTH = 20 * SCALE
HIP_WIDTH = 18 * SCALE
UPPER_ARM_LENGTH = 28 * SCALE
LOWER_ARM_LENGTH = 28 * SCALE
THIGH_LENGTH = 38 * SCALE
SHIN_LENGTH = 35 * SCALE

SLUMP_AMOUNT = 15 * SCALE
HEAD_TILT = 20 * SCALE
VERTICAL_BOB = 2 * SCALE
ARM_SWING = math.radians(15)
LEG_LIFT = math.radians(25)
KNEE_BEND = math.radians(60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Walk")
clock = pygame.time.Clock()

def get_joint_positions(t, center_x):
    points = {}

    bob = VERTICAL_BOB * math.sin(2 * t)
    
    pelvis_y = SCREEN_HEIGHT / 2 - bob + 50 
    pelvis_x = center_x
    
    sternum_x = pelvis_x + SLUMP_AMOUNT
    sternum_y = pelvis_y - TORSO_LENGTH
    
    head_x = sternum_x + HEAD_TILT
    head_y = sternum_y - NECK_LENGTH
    
    points['pelvis'] = (pelvis_x, pelvis_y)
    points['sternum'] = (sternum_x, sternum_y)
    points['head'] = (head_x, head_y)

    shoulder_y = sternum_y + 10
    points['l_shoulder'] = (sternum_x - SHOULDER_WIDTH / 2, shoulder_y)
    points['r_shoulder'] = (sternum_x + SHOULDER_WIDTH / 2, shoulder_y)

    points['l_hip'] = (pelvis_x - HIP_WIDTH / 2, pelvis_y)
    points['r_hip'] = (pelvis_x + HIP_WIDTH / 2, pelvis_y)

    thigh_angle_r = LEG_LIFT * math.sin(t)
    knee_bend_r = KNEE_BEND * max(0, math.sin(t - math.pi / 4))
    
    r_hip_pos = points['r_hip']
    r_knee_x = r_hip_pos[0] + THIGH_LENGTH * math.sin(thigh_angle_r)
    r_knee_y = r_hip_pos[1] + THIGH_LENGTH * math.cos(thigh_angle_r)
    points['r_knee'] = (r_knee_x, r_knee_y)
    
    r_ankle_x = r_knee_x + SHIN_LENGTH * math.sin(thigh_angle_r - knee_bend_r)
    r_ankle_y = r_knee_y + SHIN_LENGTH * math.cos(thigh_angle_r - knee_bend_r)
    points['r_ankle'] = (r_ankle_x, r_ankle_y)

    thigh_angle_l = LEG_LIFT * math.sin(t + math.pi)
    knee_bend_l = KNEE_BEND * max(0, math.sin(t + math.pi - math.pi / 4))

    l_hip_pos = points['l_hip']
    l_knee_x = l_hip_pos[0] + THIGH_LENGTH * math.sin(thigh_angle_l)
    l_knee_y = l_hip_pos[1] + THIGH_LENGTH * math.cos(thigh_angle_l)
    points['l_knee'] = (l_knee_x, l_knee_y)
    
    l_ankle_x = l_knee_x + SHIN_LENGTH * math.sin(thigh_angle_l - knee_bend_l)
    l_ankle_y = l_knee_y + SHIN_LENGTH * math.cos(thigh_angle_l - knee_bend_l)
    points['l_ankle'] = (l_ankle_x, l_ankle_y)

    arm_angle_r = ARM_SWING * math.sin(t + math.pi)
    elbow_bend_r = math.radians(10)
    
    r_shoulder_pos = points['r_shoulder']
    r_elbow_x = r_shoulder_pos[0] + UPPER_ARM_LENGTH * math.sin(arm_angle_r)
    r_elbow_y = r_shoulder_pos[1] + UPPER_ARM_LENGTH * math.cos(arm_angle_r)
    points['r_elbow'] = (r_elbow_x, r_elbow_y)
    
    r_wrist_x = r_elbow_x + LOWER_ARM_LENGTH * math.sin(arm_angle_r + elbow_bend_r)
    r_wrist_y = r_elbow_y + LOWER_ARM_LENGTH * math.cos(arm_angle_r + elbow_bend_r)
    points['r_wrist'] = (r_wrist_x, r_wrist_y)

    arm_angle_l = ARM_SWING * math.sin(t)
    elbow_bend_l = math.radians(10)

    l_shoulder_pos = points['l_shoulder']
    l_elbow_x = l_shoulder_pos[0] + UPPER_ARM_LENGTH * math.sin(arm_angle_l)
    l_elbow_y = l_shoulder_pos[1] + UPPER_ARM_LENGTH * math.cos(arm_angle_l)
    points['l_elbow'] = (l_elbow_x, l_elbow_y)
    
    l_wrist_x = l_elbow_x + LOWER_ARM_LENGTH * math.sin(arm_angle_l + elbow_bend_l)
    l_wrist_y = l_elbow_y + LOWER_ARM_LENGTH * math.cos(arm_angle_l + elbow_bend_l)
    points['l_wrist'] = (l_wrist_x, l_wrist_y)

    ordered_points = [
        points['head'], points['sternum'], points['pelvis'],
        points['l_shoulder'], points['r_shoulder'],
        points['l_hip'], points['r_hip'],
        points['l_elbow'], points['r_elbow'],
        points['l_knee'], points['r_knee'],
        points['l_wrist'], points['r_wrist'],
        points['l_ankle'], points['r_ankle']
    ]
    
    return [(int(p[0]), int(p[1])) for p in ordered_points]

def main():
    running = True
    t = 0
    x_offset = SCREEN_WIDTH + 150

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        t += CYCLE_SPEED
        x_offset -= HORIZONTAL_SPEED
        
        if x_offset < -200:
            x_offset = SCREEN_WIDTH + 150

        points_to_draw = get_joint_positions(t, x_offset)

        screen.fill(BLACK)
        
        for point in points_to_draw:
            pygame.draw.circle(screen, WHITE, point, POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
