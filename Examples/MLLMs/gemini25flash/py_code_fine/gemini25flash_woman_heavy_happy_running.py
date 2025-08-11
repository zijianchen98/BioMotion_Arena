
import pygame
import math
import sys

# Constants for the Pygame window and drawing
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 5

# Biomechanical parameters (highly simplified for a running gait)
# These values are empirical and aim for a visually plausible animation.
# Adjusting these can change the perceived "gait" or "weight" of the figure.

# Base body dimensions (relative units to define the neutral pose)
# These coordinates are relative to the figure's central origin (0,0).
BODY_SCALE = 0.5  # Overall scale factor for the figure's size
HEAD_Y = 150 * BODY_SCALE
SHOULDER_Y = 110 * BODY_SCALE
SHOULDER_X_OFFSET = 30 * BODY_SCALE
ELBOW_Y = 70 * BODY_SCALE
ELBOW_X_OFFSET = 40 * BODY_SCALE
WRIST_Y = 30 * BODY_SCALE
WRIST_X_OFFSET = 50 * BODY_SCALE
SPINE_Y_UPPER = 90 * BODY_SCALE  # Central Thorax/Upper Spine point
SPINE_Y_LOWER = 50 * BODY_SCALE  # Central Pelvis/Lower Spine point
HIP_Y = 50 * BODY_SCALE
HIP_X_OFFSET = 20 * BODY_SCALE
KNEE_Y = -10 * BODY_SCALE
KNEE_X_OFFSET = 15 * BODY_SCALE
ANKLE_Y = -50 * BODY_SCALE
ANKLE_X_OFFSET = 10 * BODY_SCALE

# Animation parameters
# These control the amplitude and phase of the sinusoidal movements.
RUN_SPEED_MULTIPLIER = 2.0  # Controls the overall speed of the running motion
TIME_SCALE = 0.05 * RUN_SPEED_MULTIPLIER  # How fast the animation progresses over time
VERTICAL_BOB_AMPLITUDE = 10 * BODY_SCALE  # Up-and-down movement of the entire figure
ARM_SWING_AMPLITUDE_X = 60 * BODY_SCALE   # Horizontal swing for arms
ARM_SWING_AMPLITUDE_Y = 20 * BODY_SCALE   # Vertical component for arm swing
LEG_SWING_AMPLITUDE_X = 60 * BODY_SCALE   # Horizontal swing for legs
LEG_KNEE_FLEX_AMPLITUDE = 40 * BODY_SCALE # How much the knee bends
LEG_ANKLE_FLEX_AMPLITUDE = 20 * BODY_SCALE # How much the ankle moves
KNEE_LIFT_AMPLITUDE = 20 * BODY_SCALE     # How much the knee lifts during the swing phase
HEAD_BOB_AMPLITUDE = 5 * BODY_SCALE       # Small up-down movement for the head


class PointLightFigure:
    def __init__(self, center_x, center_y):
        """
        Initializes the PointLightFigure with a central screen position.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.points = {}  # Dictionary to store current {name: (x, y)} for 15 points
        self.base_points = self._define_base_pose()

    def _define_base_pose(self):
        """
        Defines the 15 points for the human figure in a neutral, standing pose.
        The coordinates are relative to the figure's central origin (0,0).
        These points are chosen to represent key joints and body parts,
        matching the common 15-point configuration in biological motion studies
        and roughly corresponding to the provided example image.
        """
        base = {}
        # Torso and Head
        base['Head'] = (0, HEAD_Y)              # 1
        base['Spine_Upper'] = (0, SPINE_Y_UPPER)  # 2 (Central Thorax/Upper Spine)
        base['Spine_Lower'] = (0, SPINE_Y_LOWER)  # 3 (Central Pelvis/Lower Spine)

        # Arms (Shoulder, Elbow, Wrist for Left and Right)
        base['L_Shoulder'] = (-SHOULDER_X_OFFSET, SHOULDER_Y) # 4
        base['R_Shoulder'] = (SHOULDER_X_OFFSET, SHOULDER_Y) # 5
        base['L_Elbow'] = (-ELBOW_X_OFFSET, ELBOW_Y)         # 6
        base['R_Elbow'] = (ELBOW_X_OFFSET, ELBOW_Y)         # 7
        base['L_Wrist'] = (-WRIST_X_OFFSET, WRIST_Y)         # 8
        base['R_Wrist'] = (WRIST_X_OFFSET, WRIST_Y)         # 9

        # Legs (Hip, Knee, Ankle for Left and Right)
        base['L_Hip'] = (-HIP_X_OFFSET, HIP_Y)             # 10
        base['R_Hip'] = (HIP_X_OFFSET, HIP_Y)             # 11
        base['L_Knee'] = (-KNEE_X_OFFSET, KNEE_Y)           # 12
        base['R_Knee'] = (KNEE_X_OFFSET, KNEE_Y)           # 13
        base['L_Ankle'] = (-ANKLE_X_OFFSET, ANKLE_Y)         # 14
        base['R_Ankle'] = (ANKLE_X_OFFSET, ANKLE_Y)         # 15

        if len(base) != 15:
            raise ValueError(f"Expected 15 points, but got {len(base)}. Check base pose definition.")
        return base

    def update(self, time):
        """
        Calculates the new positions of all 15 points based on the current time
        to simulate a running gait. Sinusoidal functions are used to create
        smooth, cyclical motion for different body parts.
        """
        # Overall vertical bobbing for the entire figure, characteristic of running
        vertical_bob = VERTICAL_BOB_AMPLITUDE * math.sin(time * TIME_SCALE * 2)

        # Leg movements (X for swing, Y for flexion/extension)
        # Left leg swings forward and lifts knee, right leg swings backward.
        # Phase difference of pi (half cycle) between left and right legs.
        l_leg_x_swing = LEG_SWING_AMPLITUDE_X * math.sin(time * TIME_SCALE)
        l_knee_y_flex = LEG_KNEE_FLEX_AMPLITUDE * (1 - math.cos(time * TIME_SCALE * 2)) / 2 # Knee flexion (0 to 1 cycle)
        l_ankle_y_flex = LEG_ANKLE_FLEX_AMPLITUDE * (1 - math.cos(time * TIME_SCALE * 2)) / 3 # Ankle flexion
        l_knee_lift_y = KNEE_LIFT_AMPLITUDE * math.sin(time * TIME_SCALE * 2 + math.pi/2) # Additional knee lift during swing

        r_leg_x_swing = LEG_SWING_AMPLITUDE_X * math.sin(time * TIME_SCALE + math.pi)
        r_knee_y_flex = LEG_KNEE_FLEX_AMPLITUDE * (1 - math.cos((time * TIME_SCALE + math.pi) * 2)) / 2
        r_ankle_y_flex = LEG_ANKLE_FLEX_AMPLITUDE * (1 - math.cos((time * TIME_SCALE + math.pi) * 2)) / 3
        r_knee_lift_y = KNEE_LIFT_AMPLITUDE * math.sin((time * TIME_SCALE + math.pi) * 2 + math.pi/2)

        # Arm movements: Counter-swinging to legs (e.g., Right arm swings with Left leg)
        r_arm_swing_x = ARM_SWING_AMPLITUDE_X * math.sin(time * TIME_SCALE)
        r_arm_swing_y = ARM_SWING_AMPLITUDE_Y * math.cos(time * TIME_SCALE)

        l_arm_swing_x = ARM_SWING_AMPLITUDE_X * math.sin(time * TIME_SCALE + math.pi)
        l_arm_swing_y = ARM_SWING_AMPLITUDE_Y * math.cos(time * TIME_SCALE + math.pi)
        
        # Update each point's position
        for name, (bx, by) in self.base_points.items():
            x, y = bx, by # Start with the base (neutral) position

            # Apply overall vertical bob to all points
            y += vertical_bob

            # Apply specific motion based on the point's role
            if name == 'Head':
                x += HEAD_BOB_AMPLITUDE * math.sin(time * TIME_SCALE * 2 + math.pi/2) * 0.5 # Slight horizontal sway
                y += HEAD_BOB_AMPLITUDE * math.cos(time * TIME_SCALE * 2 + math.pi/2) * 0.5 # Slight vertical sway
            elif name == 'Spine_Upper' or name == 'Spine_Lower':
                x += VERTICAL_BOB_AMPLITUDE * math.sin(time * TIME_SCALE * 2) * 0.2 # Slight torso sway
            
            # Arms
            elif name == 'R_Shoulder':
                x += r_arm_swing_x * 0.2
                y += r_arm_swing_y * 0.2
            elif name == 'R_Elbow':
                x += r_arm_swing_x * 0.6
                y += r_arm_swing_y * 0.6
            elif name == 'R_Wrist':
                x += r_arm_swing_x
                y += r_arm_swing_y

            elif name == 'L_Shoulder':
                x += l_arm_swing_x * 0.2
                y += l_arm_swing_y * 0.2
            elif name == 'L_Elbow':
                x += l_arm_swing_x * 0.6
                y += l_arm_swing_y * 0.6
            elif name == 'L_Wrist':
                x += l_arm_swing_x
                y += l_arm_swing_y

            # Legs
            elif name == 'L_Hip':
                x += l_leg_x_swing * 0.1 # Hips move less horizontally
                y += l_knee_lift_y * 0.2 # Slight hip lift
            elif name == 'L_Knee':
                x += l_leg_x_swing * 0.8 # Knee moves significantly horizontally
                y += l_knee_y_flex + l_knee_lift_y
            elif name == 'L_Ankle':
                x += l_leg_x_swing * 1.0 # Ankle follows the full leg swing
                y += l_ankle_y_flex + l_knee_lift_y

            elif name == 'R_Hip':
                x += r_leg_x_swing * 0.1
                y += r_knee_lift_y * 0.2
            elif name == 'R_Knee':
                x += r_leg_x_swing * 0.8
                y += r_knee_y_flex + r_knee_lift_y
            elif name == 'R_Ankle':
                x += r_leg_x_swing * 1.0
                y += r_ankle_y_flex + r_knee_lift_y
            
            # Store the final screen coordinates (Pygame's Y increases downwards)
            self.points[name] = (self.center_x + x, self.center_y - y)

    def draw(self, screen):
        """
        Draws each of the 15 points on the Pygame screen.
        """
        for x, y in self.points.values():
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

def main():
    """
    Main function to initialize Pygame, create the figure, and run the animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion Stimulus: Running Woman")
    clock = pygame.time.Clock()

    # Create the point-light figure instance
    # Position it slightly below the vertical center to give more room for head bobbing
    figure = PointLightFigure(WIDTH // 2, HEIGHT // 2 + 100) 
    
    running = True
    time = 0 # Time variable to drive the animation cycle

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with black background
        screen.fill(BLACK)

        # Update and draw the figure
        figure.update(time)
        figure.draw(screen)

        # Update the display
        pygame.display.flip()

        # Increment time and control frame rate
        time += 1 
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
