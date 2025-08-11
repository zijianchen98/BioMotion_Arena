import pygame
import math
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Sadman Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 30

# Number of point-lights
NUM_POINTS = 15

# A simple function to create a running gait cycle with a "sad" posture.
# t in [0, 1) represents one full cycle (stride).
# Returns a list of (x, y) positions for 15 joints in screen coordinates.
def get_biomotion_points(t):
    # Scale and center for the figure on the screen
    scale = 80
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 50  # slight downward shift

    # Running frequency specifics
    # t: normalized from 0 to 1 over a full stride
    # We'll define angles for arms/legs with typical ~180 deg out of phase
    # "Sad" posture means forward-leaning torso, lowered head, minimal arm swing.
    leg_phase = 2 * math.pi * t
    arm_phase = leg_phase + math.pi  # arms out of phase with legs

    # Vertical bounce to simulate weight (more pronounced bounce for heavier feel):
    # We'll make the center move up/down ~ a small fraction of the scale
    bounce = math.sin(leg_phase * 2) * (scale * 0.10)

    # Torso lean forward angle (slight)
    torso_angle = 20  # degrees

    def rotate(x, y, deg):
        # rotate (x, y) around (0, 0) by deg degrees
        rad = math.radians(deg)
        xr = x * math.cos(rad) - y * math.sin(rad)
        yr = x * math.sin(rad) + y * math.cos(rad)
        return xr, yr

    # Base body layout (t = 0 posture), roughly
    # We'll define local coordinates for each joint, then apply transformations:
    # (x, y) in "body" space, aiming for a running stance in 2D side-view.
    # This is a very rough skeleton approximation:
    #  0: Head
    #  1: Left Shoulder
    #  2: Right Shoulder
    #  3: Left Elbow
    #  4: Right Elbow
    #  5: Left Wrist
    #  6: Right Wrist
    #  7: Hip Center
    #  8: Left Hip
    #  9: Right Hip
    # 10: Left Knee
    # 11: Right Knee
    # 12: Left Ankle
    # 13: Right Ankle
    # 14: Chest (just an extra point in the torso)
    base_points = [
        (0, -15),   # Head
        (-6,  -5),  # L Shoulder
        ( 6,  -5),  # R Shoulder
        (-9,   0),  # L Elbow
        ( 9,   0),  # R Elbow
        (-11,  5),  # L Wrist
        ( 11,  5),  # R Wrist
        (0,   5),   # Hip Center
        (-4,  5),   # L Hip
        ( 4,  5),   # R Hip
        (-4, 14),   # L Knee
        ( 4, 14),   # R Knee
        (-4, 23),   # L Ankle
        ( 4, 23),   # R Ankle
        (0,  -10),  # Chest
    ]

    # We'll add dynamic offsets for arms/legs, making them swing.
    # For a running motion, we can approximate:
    # Leg angle: ~40*sin(leg_phase) for each leg out of phase
    # Arm angle: ~30*sin(arm_phase) for each arm out of phase
    # We'll shift left vs right with +/-. We also mod the elbow and knee to add bend.

    # For sadness, we reduce arm swing amplitude and shift head downward more:
    arm_swing_amplitude = 20
    leg_swing_amplitude = 40
    head_drop = 5  # additional downward shift for "sad" posture

    # angles for left/right arms, legs:
    left_leg_angle =  leg_swing_amplitude * math.sin(leg_phase)
    right_leg_angle = -leg_swing_amplitude * math.sin(leg_phase)
    left_arm_angle =  arm_swing_amplitude * math.sin(arm_phase)
    right_arm_angle = -arm_swing_amplitude * math.sin(arm_phase)

    # Knees and elbows bend: we just offset them along the swing
    # We'll do a small sinus offset in y direction
    left_knee_bend = 3 * math.sin(leg_phase + math.pi)
    right_knee_bend = 3 * math.sin(leg_phase)
    left_elbow_bend = 2 * math.sin(arm_phase + math.pi)
    right_elbow_bend = 2 * math.sin(arm_phase)

    # Modify the base points to create a frame:
    # We'll build a new list with dynamic offsets.
    dynamic_points = list(base_points)

    # Head droop
    hx, hy = dynamic_points[0]
    hy += head_drop
    dynamic_points[0] = (hx, hy)

    # Shoulders rotate a bit with torso angle
    # We'll rotate all points about the hip center local position (0,5).
    # Then we add some extra rotation for sadness. We'll do it once after we do arms/legs.

    # Left arm chain: (Shoulder->Elbow->Wrist)
    # We'll rotate the entire chain around the shoulder by left_arm_angle
    # 1: L Shoulder, 3: L Elbow, 5: L Wrist
    lsx, lsy = dynamic_points[1]
    lex, ley = dynamic_points[3]
    lwx, lwy = dynamic_points[5]
    # rotate elbow and wrist around the shoulder:
    # shift first so that shoulder is origin, rotate, shift back
    def rotate_around(px, py, cx, cy, angle):
        px -= cx
        py -= cy
        rx, ry = rotate(px, py, angle)
        rx += cx
        ry += cy
        return rx, ry

    # left arm rotation
    lex, ley = rotate_around(lex, ley, lsx, lsy, left_arm_angle)
    lwx, lwy = rotate_around(lwx, lwy, lsx, lsy, left_arm_angle)

    # add elbow bend
    # We'll shift elbow a bit in y, relative to shoulder->elbow direction
    edx = 0
    edy = left_elbow_bend
    lex += edx
    ley += edy
    # apply again the wrist rotation around the newly moved elbow:
    lwx, lwy = rotate_around(lwx, lwy, lex, ley, left_arm_angle * 0.5)

    dynamic_points[3] = (lex, ley)
    dynamic_points[5] = (lwx, lwy)

    # Right arm chain: (Shoulder->Elbow->Wrist)
    rsx, rsy = dynamic_points[2]
    rex, rey = dynamic_points[4]
    rwx, rwy = dynamic_points[6]

    # right arm rotation
    rex, rey = rotate_around(rex, rey, rsx, rsy, right_arm_angle)
    rwx, rwy = rotate_around(rwx, rwy, rsx, rsy, right_arm_angle)

    # add elbow bend
    edx = 0
    edy = right_elbow_bend
    rex += edx
    rey += edy
    # apply again the wrist rotation around the newly moved elbow:
    rwx, rwy = rotate_around(rwx, rwy, rex, rey, right_arm_angle * 0.5)

    dynamic_points[4] = (rex, rey)
    dynamic_points[6] = (rwx, rwy)

    # Left leg chain: (Hip->Knee->Ankle)
    lhx, lhy = dynamic_points[8]
    lkx, lky = dynamic_points[10]
    lax, lay = dynamic_points[12]

    # Rotate around the hip
    lkx, lky = rotate_around(lkx, lky, lhx, lhy, left_leg_angle)
    lax, lay = rotate_around(lax, lay, lhx, lhy, left_leg_angle)

    # add knee bend
    lkx += 0
    lky += left_knee_bend
    # apply again the ankle rotation around the newly moved knee
    lax, lay = rotate_around(lax, lay, lkx, lky, left_leg_angle * 0.3)

    dynamic_points[10] = (lkx, lky)
    dynamic_points[12] = (lax, lay)

    # Right leg chain: (Hip->Knee->Ankle)
    rhx, rhy = dynamic_points[9]
    rkx, rky = dynamic_points[11]
    rax, ray = dynamic_points[13]

    # Rotate around the hip
    rkx, rky = rotate_around(rkx, rky, rhx, rhy, right_leg_angle)
    rax, ray = rotate_around(rax, ray, rhx, rhy, right_leg_angle)

    # add knee bend
    rkx += 0
    rky += right_knee_bend
    # apply again the ankle rotation around the newly moved knee
    rax, ray = rotate_around(rax, ray, rkx, rky, right_leg_angle * 0.3)

    dynamic_points[11] = (rkx, rky)
    dynamic_points[13] = (rax, ray)

    # Now rotate entire figure around hip center to add forward lean
    # We'll do so around dynamic_points[7] (Hip Center)
    hcx, hcy = dynamic_points[7]
    for i in range(len(dynamic_points)):
        if i == 7:
            continue
        px, py = dynamic_points[i]
        px, py = rotate_around(px, py, hcx, hcy, torso_angle)
        dynamic_points[i] = (px, py)

    # Add vertical bounce
    for i in range(len(dynamic_points)):
        px, py = dynamic_points[i]
        py += bounce
        dynamic_points[i] = (px, py)

    # Convert local coords to screen coords
    # then multiply by scale
    screen_points = []
    for px, py in dynamic_points:
        sx = center_x + px * (scale / 20.0)
        sy = center_y + py * (scale / 20.0)
        screen_points.append((sx, sy))

    return screen_points

def main():
    running = True
    time_pos = 0.0

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Update normalized time in [0, 1)
        time_pos += 1.0 / (FPS * 1.0)  # 1 second for one full cycle
        if time_pos >= 1.0:
            time_pos -= 1.0

        points = get_biomotion_points(time_pos)

        # Draw the points
        for x, y in points:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()