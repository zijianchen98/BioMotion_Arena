
import pygame
import math

# Constants for the Pygame window and drawing
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5  # Size of each point-light
WHITE = (255, 255, 255)  # Color for the point-lights
BLACK = (0, 0, 0)      # Color for the background

# Joint indices for the 15 points, defining the human figure's structure.
# These indices map to specific elements in the 'self.points' list.
HEAD = 0
NECK = 1
L_SHOULDER = 2
R_SHOULDER = 3
L_ELBOW = 4
R_ELBOW = 5
MID_TORSO = 6  # Represents the center of the spine, roughly chest level
L_WRIST = 7
R_WRIST = 8
L_HIP = 9
R_HIP = 10
L_KNEE = 11
R_KNEE = 12
L_ANKLE = 13
R_ANKLE = 14

class Person:
    """
    Represents a human figure as a collection of 15 point-lights and
    animates it to simulate a running motion.
    """
    def __init__(self, start_x, start_y):
        """
        Initializes the Person object.

        Args:
            start_x (int): The initial X coordinate for the center of the person.
            start_y (int): The initial Y coordinate for the center of the person.
        """
        self.start_x = start_x
        self.start_y = start_y
        self.points = [(0, 0) for _ in range(15)]  # List to store (x, y) coordinates for each point
        self.time = 0.0  # Accumulator for animation time

        # Animation speed and horizontal movement
        self.speed = 1.0  # Overall animation speed factor
        self.running_speed_horiz = 80  # Horizontal speed of the figure in pixels per second

        # Biomechanical parameters, tuned to represent a "sadwoman with light weight".
        # This involves slightly smaller proportions, less energetic movements,
        # and a more subdued posture.
        self.body_height_scale = 0.9  # Makes the figure slightly shorter/lighter build
        self.torso_height = 80 * self.body_height_scale
        self.shoulder_width = 30 * self.body_height_scale
        self.arm_length_upper = 40 * self.body_height_scale
        self.arm_length_lower = 40 * self.body_height_scale
        self.leg_length_upper = 70 * self.body_height_scale
        self.leg_length_lower = 70 * self.body_height_scale

        # Motion amplitudes and frequencies for running
        self.vertical_bob_amplitude = 8 * self.body_height_scale  # Vertical bounce (reduced for 'light weight')
        self.bob_freq = 3.5  # Cycles per second for the running gait

        self.arm_swing_amplitude = math.radians(20)  # Max angle for arm swing (reduced for 'sad')
        self.leg_swing_amplitude = math.radians(30)  # Max angle for leg swing (reduced for 'light weight')
        self.knee_bend_amplitude = math.radians(60)  # Max knee bend during swing from a straight leg position

        # "Sad" posture adjustments
        self.head_down_angle_offset = math.radians(10)  # Additional angle for head tilt downwards
        self.torso_forward_lean_angle = math.radians(5)  # Overall slight forward lean for the torso

    def update(self, dt):
        """
        Updates the position of all 15 point-lights based on the running animation.

        Args:
            dt (float): Time elapsed since the last frame in seconds.
        """
        self.time += dt * self.speed

        # Calculate the base position for the entire figure, which moves horizontally
        # and bobs vertically (to simulate running gait).
        main_x = self.start_x + (self.time * self.running_speed_horiz) % SCREEN_WIDTH
        main_y = self.start_y + self.vertical_bob_amplitude * math.sin(self.time * self.bob_freq)

        # Apply overall forward lean to the torso and head.
        # This shifts the upper body points slightly forward and down relative to the hips.
        # These offsets are used for the fixed body parts (torso, neck, head).
        lean_x_offset_torso = self.torso_height * math.sin(self.torso_forward_lean_angle)
        lean_y_offset_torso = self.torso_height * (1 - math.cos(self.torso_forward_lean_angle))

        # MID_TORSO is the central anchor point for the upper body.
        self.points[MID_TORSO] = (main_x, main_y)

        # Neck and Head positions relative to MID_TORSO, incorporating the forward lean.
        neck_rel_y = -self.torso_height / 2 + lean_y_offset_torso
        neck_rel_x = lean_x_offset_torso
        self.points[NECK] = (self.points[MID_TORSO][0] + neck_rel_x, self.points[MID_TORSO][1] + neck_rel_y)

        # Head position relative to Neck, with an additional "sad" tilt downwards.
        head_len_from_neck = 20 * self.body_height_scale
        # Calculate the base angle of the neck from vertical due to torso's lean.
        base_neck_angle = -self.torso_forward_lean_angle  # Negative as it's leaning forward (left rotation on Cartesian plane)
        head_final_angle = base_neck_angle + self.head_down_angle_offset # Add the "sad" tilt
        self.points[HEAD] = (self.points[NECK][0] + head_len_from_neck * math.sin(head_final_angle),
                             self.points[NECK][1] - head_len_from_neck * math.cos(head_final_angle)) # Y decreases upwards, so -cos for head above neck

        # Shoulders position relative to MID_TORSO, following the torso's lean.
        shoulder_y_offset = neck_rel_y + 10 * self.body_height_scale
        self.points[L_SHOULDER] = (self.points[MID_TORSO][0] + neck_rel_x - self.shoulder_width, self.points[MID_TORSO][1] + shoulder_y_offset)
        self.points[R_SHOULDER] = (self.points[MID_TORSO][0] + neck_rel_x + self.shoulder_width, self.points[MID_TORSO][1] + shoulder_y_offset)

        # Hips position relative to MID_TORSO, following the torso's lean.
        hip_y_offset = self.torso_height / 2 + lean_y_offset_torso
        hip_x_offset = lean_x_offset_torso
        self.points[L_HIP] = (self.points[MID_TORSO][0] + hip_x_offset - self.shoulder_width / 2, self.points[MID_TORSO][1] + hip_y_offset)
        self.points[R_HIP] = (self.points[MID_TORSO][0] + hip_x_offset + self.shoulder_width / 2, self.points[MID_TORSO][1] + hip_y_offset)


        # Arm motion calculations
        # Arms swing in opposition to legs. A phase offset makes them look natural.
        arm_swing_offset_phase = self.time * self.bob_freq
        arm_angle_left = self.arm_swing_amplitude * math.sin(arm_swing_offset_phase + math.pi / 2) # Starts slightly forward
        arm_angle_right = self.arm_swing_amplitude * math.sin(arm_swing_offset_phase - math.pi / 2) # Starts slightly backward

        # Left Arm: Elbow and Wrist positions
        sx, sy = self.points[L_SHOULDER]
        el_x = sx + self.arm_length_upper * math.sin(arm_angle_left)
        el_y = sy + self.arm_length_upper * math.cos(arm_angle_left)
        self.points[L_ELBOW] = (el_x, el_y)
        # Wrist rotates around elbow with a constant bend (forearm_bend_angle).
        forearm_bend_angle = math.radians(20) 
        wrist_angle_left = arm_angle_left + forearm_bend_angle
        wx = el_x + self.arm_length_lower * math.sin(wrist_angle_left)
        wy = el_y + self.arm_length_lower * math.cos(wrist_angle_left)
        self.points[L_WRIST] = (wx, wy)

        # Right Arm: Elbow and Wrist positions (mirrored from left arm)
        sx, sy = self.points[R_SHOULDER]
        el_x = sx + self.arm_length_upper * math.sin(arm_angle_right)
        el_y = sy + self.arm_length_upper * math.cos(arm_angle_right)
        self.points[R_ELBOW] = (el_x, el_y)
        wrist_angle_right = arm_angle_right + forearm_bend_angle
        wx = el_x + self.arm_length_lower * math.sin(wrist_angle_right)
        wy = el_y + self.arm_length_lower * math.cos(wrist_angle_right)
        self.points[R_WRIST] = (wx, wy)


        # Leg motion calculations
        leg_swing_offset_phase = self.time * self.bob_freq
        # Thigh angle relative to vertical. Left leg forward when right leg is back.
        thigh_angle_left = self.leg_swing_amplitude * math.sin(leg_swing_offset_phase)
        thigh_angle_right = self.leg_swing_amplitude * math.sin(leg_swing_offset_phase + math.pi)

        # Knee bend factor: Knee bends most when leg is under the body (mid-swing/mid-stance).
        # This uses a doubled frequency cosine wave, peaking at 1 (max bend) and dipping at 0 (min bend).
        knee_bend_factor = 0.5 + 0.5 * math.cos(leg_swing_offset_phase * 2)

        # Left Leg: Knee and Ankle positions
        hx, hy = self.points[L_HIP]
        # Knee: rotates around hip
        k_x = hx + self.leg_length_upper * math.sin(thigh_angle_left)
        k_y = hy + self.leg_length_upper * math.cos(thigh_angle_left)
        self.points[L_KNEE] = (k_x, k_y)
        # Ankle: lower leg angle relative to thigh, adjusted by knee bend.
        # (math.pi - current_knee_bend) makes the lower leg segment angle from the upper leg segment.
        current_knee_bend_left = self.knee_bend_amplitude * knee_bend_factor
        ankle_angle_from_vertical_left = thigh_angle_left + (math.pi - current_knee_bend_left)
        ax = k_x + self.leg_length_lower * math.sin(ankle_angle_from_vertical_left)
        ay = k_y + self.leg_length_lower * math.cos(ankle_angle_from_vertical_left)
        self.points[L_ANKLE] = (ax, ay)

        # Right Leg: Knee and Ankle positions (opposite phase to left leg)
        hx, hy = self.points[R_HIP]
        k_x = hx + self.leg_length_upper * math.sin(thigh_angle_right)
        k_y = hy + self.leg_length_upper * math.cos(thigh_angle_right)
        self.points[R_KNEE] = (k_x, k_y)
        current_knee_bend_right = self.knee_bend_amplitude * (0.5 + 0.5 * math.cos(leg_swing_offset_phase * 2 + math.pi)) # Opposing knee bend factor
        ankle_angle_from_vertical_right = thigh_angle_right + (math.pi - current_knee_bend_right)
        ax = k_x + self.leg_length_lower * math.sin(ankle_angle_from_vertical_right)
        ay = k_y + self.leg_length_lower * math.cos(ankle_angle_from_vertical_right)
        self.points[R_ANKLE] = (ax, ay)

    def draw(self, screen):
        """
        Draws the 15 point-lights on the Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame surface to draw on.
        """
        for x, y in self.points:
            # Draw each point as a white circle on the black background
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)


def main():
    """
    Main function to initialize Pygame, create the animation, and run the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion Stimulus - Running Sadwoman")
    clock = pygame.time.Clock()

    # Create the Person object, starting in the center of the screen, slightly lower.
    person = Person(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)

    running = True
    while running:
        # Calculate time elapsed since last frame for smooth, frame-rate independent animation.
        dt = clock.tick(FPS) / 1000.0  # dt in seconds

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the person's position for the current frame
        person.update(dt)

        # Drawing
        screen.fill(BLACK)  # Fill the background with solid black
        person.draw(screen)  # Draw the point-light figure
        pygame.display.flip()  # Update the full display surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()
