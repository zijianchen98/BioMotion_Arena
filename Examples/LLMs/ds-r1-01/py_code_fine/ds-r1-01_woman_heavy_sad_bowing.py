
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
SPEED = 0.5  # Slower speed for heavy movement
AMPLITUDE = 80  # Forward bending amplitude
SWAY = 20  # Side-to-side body sway

# Body points configuration (15 points)
class BodyPoints:
    def __init__(self):
        self.base_points = {
            'head': (0, -120),
            'shoulder_l': (-40, -90),
            'shoulder_r': (40, -90),
            'elbow_l': (-60, -60),
            'elbow_r': (60, -60),
            'hand_l': (-70, -30),
            'hand_r': (70, -30),
            'torso_upper': (0, -75),
            'torso_mid': (0, -40),
            'torso_lower': (0, -5),
            'hip_l': (-30, 20),
            'hip_r': (30, 20),
            'knee_l': (-20, 50),
            'knee_r': (20, 50),
            'foot_l': (-25, 100),
            'foot_r': (25, 100)
        }

    def get_positions(self, time):
        # Calculate motion parameters
        bow = math.sin(time * SPEED) * AMPLITUDE
        sway = math.sin(time * SPEED * 0.7) * SWAY
        arm_swing = math.sin(time * SPEED * 1.2) * 30
        knee_bend = abs(math.sin(time * SPEED)) * 20

        # Calculate point positions
        points = {}
        
        # Head and upper body
        points['head'] = (sway*0.5, -120 + bow*0.7)
        points['shoulder_l'] = (-40 - sway*0.3, -90 + bow*0.5)
        points['shoulder_r'] = (40 - sway*0.3, -90 + bow*0.5)
        
        # Arms
        points['elbow_l'] = (-60 + arm_swing*0.5, -60 + bow*0.3)
        points['elbow_r'] = (60 - arm_swing*0.5, -60 + bow*0.3)
        points['hand_l'] = (-70 + arm_swing, -30 + bow*0.2)
        points['hand_r'] = (70 - arm_swing, -30 + bow*0.2)
        
        # Torso
        points['torso_upper'] = (sway*0.3, -75 + bow*0.6)
        points['torso_mid'] = (sway*0.4, -40 + bow*0.4)
        points['torso_lower'] = (sway*0.5, -5 + bow*0.2)
        
        # Lower body
        points['hip_l'] = (-30 + sway*0.2, 20 - bow*0.1)
        points['hip_r'] = (30 + sway*0.2, 20 - bow*0.1)
        points['knee_l'] = (-20, 50 + knee_bend)
        points['knee_r'] = (20, 50 + knee_bend)
        points['foot_l'] = (-25, 100 + knee_bend*0.5)
        points['foot_r'] = (25, 100 + knee_bend*0.5)

        return points

def main():
    body = BodyPoints()
    time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        
        # Get current positions
        points = body.get_positions(time)
        
        # Draw all points
        for key in points:
            x = points[key][0] + WIDTH//2
            y = points[key][1] + HEIGHT//2
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 8)

        pygame.display.flip()
        time += 0.1
        clock.tick(FPS)

if __name__ == "__main__":
    main()
