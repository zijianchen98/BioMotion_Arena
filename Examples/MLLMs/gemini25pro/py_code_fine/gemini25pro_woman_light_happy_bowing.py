
import pygame
import math

def solve_ik_2bone(root_pos, target_pos, len1, len2, bend_positive):
    """
    Solves a 2-bone Inverse Kinematics problem to find the middle joint's position.
    This is used to calculate the position of the knee given the hip and ankle.

    :param root_pos: pygame.math.Vector2, the start of the chain (hip).
    :param target_pos: pygame.math.Vector2, the end of the chain (ankle).
    :param len1: float, length of the first bone (upper leg).
    :param len2: float, length of the second bone (lower leg).
    :param bend_positive: bool, determines the bend direction. False for the typical backward knee bend.
    :return: pygame.math.Vector2, the position of the middle joint (knee).
    """
    root_to_target = target_pos - root_pos
    dist = root_to_target.length()

    # Handle cases where the target is not reachable
    if dist > len1 + len2:
        return root_pos + root_to_target.normalize() * len1
    if dist < abs(len1 - len2):
        return root_pos + root_to_target.normalize() * len1

    # Use the law of cosines to find the angle at the root joint
    # Clamp the value to avoid math domain errors from floating point inaccuracies
    cos_angle_val = (dist**2 + len1**2 - len2**2) / (2 * dist * len1)
    cos_angle_val = max(-1.0, min(1.0, cos_angle_val))
    angle_at_root = math.acos(cos_angle_val)

    # The angle of the vector from the root to the target
    base_angle = math.atan2(root_to_target.y, root_to_target.x)

    # Determine the final angle for the first bone based on the desired bend direction
    if bend_positive:
        final_angle = base_angle + angle_at_root
    else:
        final_angle = base_angle - angle_at_root

    # Calculate the middle joint's position
    middle_joint_pos = root_pos + pygame.math.Vector2(math.cos(final_angle), math.sin(final_angle)) * len1
    
    return middle_joint_pos

def main():
    """
    Main function to run the biological motion animation.
    """
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Biological Motion: Happy Woman Bowing")
    clock = pygame.time.Clock()

    # --- Style and Colors ---
    BG_COLOR = (0, 0, 0)
    POINT_COLOR = (255, 255, 255)
    POINT_RADIUS = 7

    # --- Figure Proportions (in pixels) ---
    torso_len = 100
    head_rad = 25
    shoulder_width = 75
    hip_width = 60
    upper_arm_len = 65
    lower_arm_len = 60
    upper_leg_len = 85
    lower_leg_len = 75

    # --- Animation Parameters ---
    animation_speed = 0.025
    max_bow_angle = math.radians(75)    # How deep the bow is
    max_nod_angle = math.radians(45)    # How much the head nods
    arm_swing_back = math.radians(20)   # How much arms swing backward
    happy_bounce_amp = 2.5              # Amplitude of the subtle bounce
    happy_bounce_speed = 2              # Speed of the bounce cycle
    hip_shift_x = 55                    # How much hips shift back for balance
    hip_shift_y = 30                    # How much hips sink down

    # --- Positioning ---
    center_x = screen_width // 2
    base_y = screen_height - 100

    # --- Point-light data structure (15 points) ---
    points = [pygame.math.Vector2(0, 0) for _ in range(15)]
    HEAD, NECK, PELVIS = 0, 1, 2
    L_SHOULDER, R_SHOULDER = 3, 4
    L_ELBOW, R_ELBOW = 5, 6
    L_WRIST, R_WRIST = 7, 8
    L_HIP, R_HIP = 9, 10
    L_KNEE, R_KNEE = 11, 12
    L_ANKLE, R_ANKLE = 13, 14

    running = True
    time_step = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time_step += 1
        phase = time_step * animation_speed
        # bow_cycle smoothly transitions from 0 (upright) to 1 (full bow) and back to 0
        bow_cycle = 0.5 * (1 - math.cos(phase))

        # --- KINEMATICS CALCULATIONS ---

        # 1. Base: Ankles are the anchor points.
        points[L_ANKLE].x = center_x - hip_width / 2
        points[L_ANKLE].y = base_y
        points[R_ANKLE].x = center_x + hip_width / 2
        points[R_ANKLE].y = base_y

        # 2. Hips: Shift backward and down to maintain balance during the bow.
        current_hip_shift_x = -hip_shift_x * bow_cycle
        current_hip_shift_y = hip_shift_y * bow_cycle
        initial_hip_y = base_y - lower_leg_len - upper_leg_len
        
        # Add a subtle "happy" bounce.
        bounce = happy_bounce_amp * math.cos(phase * happy_bounce_speed)

        points[L_HIP].x = center_x - hip_width / 2 + current_hip_shift_x
        points[L_HIP].y = initial_hip_y + current_hip_shift_y + bounce
        points[R_HIP].x = center_x + hip_width / 2 + current_hip_shift_x
        points[R_HIP].y = initial_hip_y + current_hip_shift_y + bounce
        
        # 3. Knees: Calculated using Inverse Kinematics for a natural leg bend.
        points[L_KNEE] = solve_ik_2bone(points[L_HIP], points[L_ANKLE], upper_leg_len, lower_leg_len, False)
        points[R_KNEE] = solve_ik_2bone(points[R_HIP], points[R_ANKLE], upper_leg_len, lower_leg_len, False)

        # 4. Torso: Pivots at the pelvis (midpoint of hips).
        points[PELVIS] = (points[L_HIP] + points[R_HIP]) / 2.0
        
        # A positive angle results in a counter-clockwise rotation (bending left).
        torso_angle = max_bow_angle * bow_cycle
        
        neck_vec = pygame.math.Vector2(0, -torso_len).rotate_rad(torso_angle)
        points[NECK] = points[PELVIS] + neck_vec

        # 5. Head: Rotates with the torso and adds an extra nod.
        head_nod_angle = max_nod_angle * bow_cycle
        head_angle = torso_angle + head_nod_angle
        head_vec = pygame.math.Vector2(0, -head_rad).rotate_rad(head_angle)
        points[HEAD] = points[NECK] + head_vec

        # 6. Shoulders: Attached to the neck and rotate with the torso.
        shoulder_vec_l = pygame.math.Vector2(-shoulder_width / 2, 0).rotate_rad(torso_angle)
        points[L_SHOULDER] = points[NECK] + shoulder_vec_l
        shoulder_vec_r = pygame.math.Vector2(shoulder_width / 2, 0).rotate_rad(torso_angle)
        points[R_SHOULDER] = points[NECK] + shoulder_vec_r
        
        # 7. Arms: Hang from shoulders and swing slightly backward.
        # A negative angle results in a clockwise rotation (swinging backward relative to the figure).
        arm_angle_abs = -arm_swing_back * bow_cycle
        
        l_elbow_vec = pygame.math.Vector2(0, upper_arm_len).rotate_rad(arm_angle_abs)
        points[L_ELBOW] = points[L_SHOULDER] + l_elbow_vec
        l_wrist_vec = pygame.math.Vector2(0, lower_arm_len).rotate_rad(arm_angle_abs)
        points[L_WRIST] = points[L_ELBOW] + l_wrist_vec
        
        r_elbow_vec = pygame.math.Vector2(0, upper_arm_len).rotate_rad(arm_angle_abs)
        points[R_ELBOW] = points[R_SHOULDER] + r_elbow_vec
        r_wrist_vec = pygame.math.Vector2(0, lower_arm_len).rotate_rad(arm_angle_abs)
        points[R_WRIST] = points[R_ELBOW] + r_wrist_vec

        # --- DRAWING ---
        screen.fill(BG_COLOR)
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point.x), int(point.y)), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
