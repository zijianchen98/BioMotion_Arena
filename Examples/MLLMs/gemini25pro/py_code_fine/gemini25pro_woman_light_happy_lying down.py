
import pygame
import math

def main():
    """
    This program displays a point-light stimulus animation of a person lying down.
    The animation is created by interpolating between a series of keyframes.
    """
    # --- Pygame Setup ---
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()

    # --- Visual Style ---
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    POINT_RADIUS = 6
    NUM_POINTS = 15

    # --- Joint Indices ---
    # For clarity when defining keyframe coordinates.
    HEAD, STERNUM, PELVIS = 0, 1, 2
    L_SHOULDER, R_SHOULDER = 3, 4
    L_ELBOW, R_ELBOW = 5, 6
    L_WRIST, R_WRIST = 7, 8
    L_HIP, R_HIP = 9, 10
    L_KNEE, R_KNEE = 11, 12
    L_ANKLE, R_ANKLE = 13, 14

    # --- Animation Timing ---
    PAUSE_START_FRAMES = 30
    TRANSITION_FRAMES = 70
    PAUSE_END_FRAMES = 90

    # --- Keyframe Data ---
    # A list of poses. Each pose is a list of 15 (x, y) coordinates.
    # The animation shows a person from a profile view (facing right) lying down.
    keyframes = []

    # Keyframe 0: Standing upright
    kf0 = [(0, 0)] * NUM_POINTS
    kf0[PELVIS] = (400, 400); kf0[STERNUM] = (400, 320); kf0[HEAD] = (400, 260)
    kf0[L_HIP] = (395, 400); kf0[R_HIP] = (405, 400)
    kf0[L_SHOULDER] = (395, 320); kf0[R_SHOULDER] = (405, 320)
    kf0[L_KNEE] = (395, 480); kf0[R_KNEE] = (405, 480)
    kf0[L_ANKLE] = (395, 560); kf0[R_ANKLE] = (405, 560)
    kf0[L_ELBOW] = (395, 380); kf0[R_ELBOW] = (405, 380)
    kf0[L_WRIST] = (395, 440); kf0[R_WRIST] = (405, 440)
    keyframes.append(kf0)

    # Keyframe 1: Crouching down to kneel
    kf1 = [(0, 0)] * NUM_POINTS
    kf1[PELVIS] = (460, 470); kf1[STERNUM] = (480, 390); kf1[HEAD] = (490, 330)
    kf1[L_HIP] = (455, 470); kf1[R_HIP] = (465, 470)
    kf1[L_SHOULDER] = (475, 390); kf1[R_SHOULDER] = (485, 390)
    kf1[L_KNEE] = (470, 560); kf1[R_KNEE] = (480, 560)
    kf1[L_ANKLE] = (420, 560); kf1[R_ANKLE] = (430, 560)
    kf1[L_ELBOW] = (490, 450); kf1[R_ELBOW] = (500, 450)
    kf1[L_WRIST] = (510, 520); kf1[R_WRIST] = (520, 520)
    keyframes.append(kf1)

    # Keyframe 2: Sitting back on heels, preparing to shift weight to the side
    kf2 = [(0, 0)] * NUM_POINTS
    kf2[PELVIS] = (440, 520); kf2[STERNUM] = (460, 440); kf2[HEAD] = (470, 380)
    kf2[L_HIP] = (435, 520); kf2[R_HIP] = (445, 520)
    kf2[L_SHOULDER] = (455, 440); kf2[R_SHOULDER] = (465, 440)
    kf2[L_KNEE] = (480, 540); kf2[R_KNEE] = (490, 540)
    kf2[L_ANKLE] = (430, 560); kf2[R_ANKLE] = (440, 560)
    kf2[L_ELBOW] = (410, 460); kf2[R_ELBOW] = (420, 460)
    kf2[L_WRIST] = (390, 520); kf2[R_WRIST] = (400, 520)
    keyframes.append(kf2)

    # Keyframe 3: Lying on side, supported by elbow
    kf3 = [(0, 0)] * NUM_POINTS
    kf3[PELVIS] = (380, 540); kf3[STERNUM] = (460, 530); kf3[HEAD] = (520, 520)
    kf3[L_HIP] = (380, 545); kf3[R_HIP] = (380, 535)
    kf3[L_SHOULDER] = (460, 535); kf3[R_SHOULDER] = (460, 525)
    kf3[L_KNEE] = (350, 520); kf3[R_KNEE] = (350, 510)
    kf3[L_ANKLE] = (320, 520); kf3[R_ANKLE] = (320, 510)
    kf3[L_ELBOW] = (480, 500); kf3[R_ELBOW] = (450, 495)
    kf3[L_WRIST] = (510, 490); kf3[R_WRIST] = (420, 485)
    keyframes.append(kf3)

    # Keyframe 4: Fully relaxed, lying on side
    kf4 = [(0, 0)] * NUM_POINTS
    kf4[PELVIS] = (360, 550); kf4[STERNUM] = (440, 540); kf4[HEAD] = (500, 530)
    kf4[L_HIP] = (360, 555); kf4[R_HIP] = (360, 545)
    kf4[L_SHOULDER] = (440, 545); kf4[R_SHOULDER] = (440, 535)
    kf4[L_KNEE] = (320, 560); kf4[R_KNEE] = (320, 550)
    kf4[L_ANKLE] = (260, 560); kf4[R_ANKLE] = (260, 550)
    kf4[L_ELBOW] = (470, 535); kf4[R_ELBOW] = (420, 525)
    kf4[L_WRIST] = (500, 530); kf4[R_WRIST] = (390, 540)
    keyframes.append(kf4)

    TOTAL_TRANSITIONS = len(keyframes) - 1
    TOTAL_MOTION_FRAMES = TOTAL_TRANSITIONS * TRANSITION_FRAMES
    TOTAL_FRAMES_IN_CYCLE = PAUSE_START_FRAMES + TOTAL_MOTION_FRAMES + PAUSE_END_FRAMES

    # --- Helper Functions ---
    def ease_in_out_sine(t):
        return -(math.cos(math.pi * t) - 1) / 2

    def lerp(a, b, t):
        return a + (b - a) * t

    def lerp_point(p1, p2, t):
        x = lerp(p1[0], p2[0], t)
        y = lerp(p1[1], p2[1], t)
        return (x, y)

    def get_current_pose(frame_count):
        frame_in_cycle = frame_count % TOTAL_FRAMES_IN_CYCLE
        
        if frame_in_cycle < PAUSE_START_FRAMES:
            return keyframes[0]
        
        if frame_in_cycle >= PAUSE_START_FRAMES + TOTAL_MOTION_FRAMES:
            return keyframes[-1]

        motion_frame = frame_in_cycle - PAUSE_START_FRAMES
        transition_index = motion_frame // TRANSITION_FRAMES
        frame_in_transition = motion_frame % TRANSITION_FRAMES
        
        if TRANSITION_FRAMES == 1:
            t = 1.0
        else:
            t = frame_in_transition / (TRANSITION_FRAMES - 1)
        eased_t = ease_in_out_sine(t)
        
        start_pose = keyframes[transition_index]
        end_pose = keyframes[transition_index + 1]
        
        current_pose = [lerp_point(start_pose[i], end_pose[i], eased_t) for i in range(NUM_POINTS)]
        return current_pose

    # --- Main Loop ---
    frame_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        pose = get_current_pose(frame_count)

        screen.fill(BLACK)
        for point in pose:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()
        frame_count += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
