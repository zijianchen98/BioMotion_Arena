
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Frame rate
FPS = 30

class PointLightFigure:
    def __init__(self, start_x, start_y):
        """
        Initializes the point-light figure.
        :param start_x: The initial X-coordinate for the figure's pelvis (root point).
        :param start_y: The initial Y-coordinate for the figure's pelvis (root point).
        """
        self.start_x = start_x 
        self.start_y = start_y 

        self.initial_relative_points = {}
        self.define_initial_pose() # Sets up the 15 points in a standing pose, relative to pelvis (0,0)

        self.animation_frames = []
        self.current_frame_idx = 0
        self.total_frames_in_animation = FPS * 4 # 4 seconds for one complete roll cycle

        # Generate all animation frames upfront for smooth playback
        self.generate_forward_roll_animation(self.total_frames_in_animation)

    def define_initial_pose(self):
        """
        Defines the initial standing pose of the 15 point-lights relative to the 'pelvis' point (0,0).
        These points represent major human joints and body parts, designed to mimic the example image.
        """
        self.initial_relative_points = {
            'head': (0, -100),       # Top of the head
            'neck': (0, -80),        # Base of the neck
            'l_shoulder': (-30, -60),  # Left shoulder
            'r_shoulder': (30, -60),   # Right shoulder
            'l_elbow': (-45, -20),     # Left elbow (slightly bent, arms forward)
            'r_elbow': (45, -20),      # Right elbow
            'l_wrist': (-40, 20),      # Left wrist (hanging slightly below pelvis level)
            'r_wrist': (40, 20),       # Right wrist
            'pelvis': (0, 0),          # Central point, acts as the root
            'l_hip': (-20, 0),         # Left hip
            'r_hip': (20, 0),          # Right hip
            'l_knee': (-15, 50),       # Left knee
            'r_knee': (15, 50),        # Right knee
            'l_ankle': (-10, 100),     # Left ankle
            'r_ankle': (10, 100)       # Right ankle
        }

    def generate_forward_roll_animation(self, total_frames):
        """
        Generates the keyframes for the forward roll animation.
        The animation is broken down into phases (bend, roll, unroll) and uses
        mathematical easing functions to ensure smooth transitions.
        """
        frames = []
        
        # Define overall motion parameters
        roll_distance_x = 400  # Total horizontal distance the figure travels during the roll
        max_dip_y = 150        # Maximum vertical dip of the figure's pelvis during the roll
        max_bend_angle = 90    # Max forward bend angle of torso/head (in degrees)
        max_knee_bend_factor = 0.7 # Factor for how much legs 'tuck in' (0.0 to 1.0)
        total_body_roll_angle = math.radians(360) # Total full body rotation during the roll phase (360 degrees)

        for i in range(total_frames):
            p = i / (total_frames - 1) # Overall animation progress (0.0 to 1.0)

            # Use a smoothed progress for primary movements (ease-in-out)
            # This makes the acceleration and deceleration natural.
            p_eased = 0.5 - 0.5 * math.cos(math.pi * p) 

            current_frame_points = {}
            
            # 1. Overall Translation of the Figure (Pelvis's absolute position)
            # Horizontal motion: moves from start_x to start_x + roll_distance_x
            current_pelvis_x = self.start_x + roll_distance_x * p_eased 
            
            # Vertical motion: pelvis dips down and then rises back up (a smooth arc)
            current_pelvis_y = self.start_y + max_dip_y * math.sin(math.pi * p) 
            
            # --- Limb Poses Relative to Pelvis and Global Rotation ---
            
            # Head/Torso bend forward and back (using sin wave for smooth bending and unbending)
            bend_angle = math.radians(max_bend_angle * math.sin(math.pi * p)) 
            
            # Leg bend/tuck factor (0.0 to 1.0 then back to 0.0)
            knee_bend_factor = max_knee_bend_factor * math.sin(math.pi * p) 

            # Arm tuck factor (0.0 to 1.0 then back to 0.0)
            arm_tuck_factor = math.sin(math.pi * p) 
            
            # Body rotation during the actual rolling phase
            # This rotation primarily occurs when the figure is tucked and moving over the ground.
            current_roll_angle = 0.0
            roll_phase_start = 0.2
            roll_phase_end = 0.8
            if p > roll_phase_start and p < roll_phase_end:
                # Normalize progress within the active rolling phase
                roll_sub_progress = (p - roll_phase_start) / (roll_phase_end - roll_phase_start)
                # Apply easing to the roll sub-progress for smooth rotation speed
                roll_sub_progress_eased = 0.5 - 0.5 * math.cos(math.pi * roll_sub_progress)
                current_roll_angle = total_body_roll_angle * roll_sub_progress_eased

            # Define the pivot point for the overall body rotation during the roll.
            # This point represents the contact point with the ground (e.g., lower back/shoulders).
            # It moves dynamically with the pelvis.
            roll_pivot_rel_y_offset = 50 # Relative to pelvis, typically on the lower back
            roll_pivot_x = current_pelvis_x + self.initial_relative_points['pelvis'][0]
            roll_pivot_y = current_pelvis_y + roll_pivot_rel_y_offset 

            for name, (initial_rel_x, initial_rel_y) in self.initial_relative_points.items():
                current_rel_x, current_rel_y = initial_rel_x, initial_rel_y

                # Apply bending to upper body (head, neck, shoulders, arms) around the pelvis
                if name in ['head', 'neck', 'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow', 'l_wrist', 'r_wrist']:
                    # Calculate position relative to the pelvis (its current relative (0,0))
                    temp_x = current_rel_x - self.initial_relative_points['pelvis'][0]
                    temp_y = current_rel_y - self.initial_relative_points['pelvis'][1]
                    
                    # Rotate these points forward based on bend_angle
                    rotated_x = temp_x * math.cos(bend_angle) - temp_y * math.sin(bend_angle)
                    rotated_y = temp_x * math.sin(bend_angle) + temp_y * math.cos(bend_angle)
                    
                    # Translate back relative to pelvis
                    current_rel_x = rotated_x + self.initial_relative_points['pelvis'][0]
                    current_rel_y = rotated_y + self.initial_relative_points['pelvis'][1]
                    
                    # Arms tuck in specifically (e.g., crossing body)
                    if 'elbow' in name or 'wrist' in name:
                        # Interpolate between current position and a tucked position
                        tucked_x = initial_rel_x * (1 - arm_tuck_factor * 0.7) # Move 70% towards center x
                        tucked_y = initial_rel_y + 10 * arm_tuck_factor # Move slightly down when tucking
                        
                        current_rel_x = current_rel_x * (1 - arm_tuck_factor) + tucked_x * arm_tuck_factor
                        current_rel_y = current_rel_y * (1 - arm_tuck_factor) + tucked_y * arm_tuck_factor
                        
                # Apply leg bending/tucking for knees and ankles
                elif 'knee' in name or 'ankle' in name:
                    # Legs shorten and pull in as they bend/tuck
                    current_rel_y = initial_rel_y * (1 - knee_bend_factor) # Vertical compression
                    current_rel_x = initial_rel_x * (1 - knee_bend_factor * 0.5) # Horizontal tucking towards center
                    
                    # Ankles tuck in even more than knees
                    if 'ankle' in name:
                        current_rel_y = initial_rel_y * (1 - knee_bend_factor * 1.5) 
                        current_rel_x = initial_rel_x * (1 - knee_bend_factor * 1.5)

                # Apply the overall body rotation (the "roll") around the roll_pivot
                # First, get the point's position relative to the current roll_pivot
                point_from_pivot_x = (current_pelvis_x + current_rel_x) - roll_pivot_x
                point_from_pivot_y = (current_pelvis_y + current_rel_y) - roll_pivot_y

                # Rotate this relative point
                rotated_x_global = point_from_pivot_x * math.cos(current_roll_angle) - point_from_pivot_y * math.sin(current_roll_angle)
                rotated_y_global = point_from_pivot_x * math.sin(current_roll_angle) + point_from_pivot_y * math.cos(current_roll_angle)

                # Translate back to absolute screen coordinates
                current_frame_points[name] = (roll_pivot_x + rotated_x_global, roll_pivot_y + rotated_y_global)
            
            frames.append(current_frame_points)
        
        self.animation_frames = frames

    def update(self):
        """
        Updates the figure's points to the next frame in the animation sequence.
        Loops back to the beginning after the last frame.
        """
        if not self.animation_frames:
            return

        self.points = self.animation_frames[self.current_frame_idx]
        self.current_frame_idx = (self.current_frame_idx + 1) % len(self.animation_frames)

    def draw(self, screen):
        """
        Draws the current positions of the point-lights on the screen.
        """
        for point_pos in self.points.values():
            pygame.draw.circle(screen, WHITE, (int(point_pos[0]), int(point_pos[1])), POINT_RADIUS)

# --- Main Program Execution ---
if __name__ == "__main__":
    # Create the point-light figure
    # Initial position set slightly to the left and centered vertically
    # to allow space for the figure to roll across the screen.
    figure = PointLightFigure(WIDTH // 2 - 200, HEIGHT // 2 + 50) 

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Allow ESC to quit
                    running = False

        # Clear the screen to black
        SCREEN.fill(BLACK)

        # Update the figure's animation frame
        figure.update()
        # Draw the figure's point-lights
        figure.draw(SCREEN)

        # Update the full display surface to the screen
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    # Quit Pygame and exit the program
    pygame.quit()
    sys.exit()
