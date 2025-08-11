#!/usr/bin/env python3
import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman (Heavy Weight) Forward Rolling")

CLOCK = pygame.time.Clock()
FPS = 60

# Define 7 keyframes, each with 15 points (x,y). 
# The points are arranged as:
# 0: Head
# 1: Neck
# 2: LShoulder
# 3: RShoulder
# 4: LElbow
# 5: RElbow
# 6: LWrist
# 7: RWrist
# 8: TorsoCenter
# 9: LHip
# 10: RHip
# 11: LKnee
# 12: RKnee
# 13: LAnkle
# 14: RAnkle

frames = [
    [  # Frame 0 (Standing, slumped)
        (400,230),(400,240),(385,245),(415,245),
        (380,265),(420,265),(375,285),(425,285),
        (400,265),(390,280),(410,280),(390,320),
        (410,320),(390,360),(410,360)
    ],
    [  # Frame 1 (Slightly crouched)
        (400,235),(400,245),(385,250),(415,250),
        (380,270),(420,270),(377,290),(423,290),
        (400,270),(390,285),(410,285),(390,325),
        (410,325),(390,365),(410,365)
    ],
    [  # Frame 2 (Hands on ground)
        (400,245),(400,255),(385,255),(415,255),
        (380,275),(420,275),(375,295),(425,295),
        (400,280),(395,295),(405,295),(395,330),
        (405,330),(395,365),(405,365)
    ],
    [  # Frame 3 (Mid-roll, inverted)
        (420,250),(420,260),(405,265),(435,265),
        (400,280),(440,280),(395,300),(445,300),
        (420,280),(410,295),(430,295),(410,325),
        (430,325),(410,355),(430,355)
    ],
    [  # Frame 4 (Continuing roll)
        (440,240),(440,250),(425,255),(455,255),
        (420,270),(460,270),(415,290),(465,290),
        (440,270),(430,285),(450,285),(430,320),
        (450,320),(430,355),(450,355)
    ],
    [  # Frame 5 (Almost done)
        (460,235),(460,245),(445,250),(475,250),
        (440,270),(480,270),(435,290),(485,290),
        (460,270),(450,285),(470,285),(450,325),
        (470,325),(450,365),(470,365)
    ],
    [  # Frame 6 (Final standing)
        (480,230),(480,240),(465,245),(495,245),
        (460,265),(500,265),(455,285),(505,285),
        (480,265),(470,280),(490,280),(470,320),
        (490,320),(470,360),(490,360)
    ]
]

# Function to linearly interpolate between two points
def lerp(a, b, fraction):
    return (a[0] + (b[0] - a[0]) * fraction,
            a[1] + (b[1] - a[1]) * fraction)

# Given a continuous float t, return a list of 15 (x,y) points for the skeleton.
def get_skeleton_positions(t):
    # We cycle through frames 0..6, then loop
    n_frames = len(frames)
    base_idx = int(t) % n_frames
    frac = t - int(t)
    next_idx = (base_idx + 1) % n_frames
    
    # Interpolate between frames[base_idx] and frames[next_idx]
    interpolated = []
    for i in range(15):
        p1 = frames[base_idx][i]
        p2 = frames[next_idx][i]
        interpolated.append(lerp(p1, p2, frac))
    return interpolated

def main():
    t = 0.0
    running = True
    
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        # Increase t slowly to simulate heavy/slow rolling
        t += 0.02
        
        SCREEN.fill((0, 0, 0))  # Black background
        
        # Get current positions of the 15 points
        points = get_skeleton_positions(t)
        
        # Draw the points as white circles
        for (x, y) in points:
            pygame.draw.circle(SCREEN, (255,255,255), (int(x), int(y)), 5)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()