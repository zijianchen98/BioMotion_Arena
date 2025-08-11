
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Walking Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters for the walking animation
FPS = 60
TOTAL_FRAMES = 600  # Total frames for a complete walking cycle
PARTICLE_COUNT = 15

# Body segment lengths (proportions)
SEGMENT_LENGTHS = [0.3, 0.25, 0.2, 0.2, 0.15]  # Head, thigh, lower leg, upper arm, lower arm

# Base position of the model
BASE_X, BASE_Y = WIDTH // 2, HEIGHT * 3 // 4

# Function to calculate joint positions for walking
def calculate_positions(frame):
   walking_angle = (frame / TOTAL_FRAMES) * 2 * math.pi
    
    # Head position (relative to upper body)
    neck_angle = math.pi / 8 * math.sin(walking_angle * 1.5)
    neck_x = 0
    neck_y = -SEGMENT_LENGTHS[0] * math.cos(neck_angle)
    head_x = neck_x
    head_y = neck_y - SEGMENT_LENGTHS[0] * math.cos(neck_angle)
    
    # Upper body
    torso_angle = math.pi / 16 * math.sin(walking_angle * 2)
    torso_x = SEGMENT_LENGTHS[0] * math.sin(neck_angle)
    torso_y = SEGMENT_LENGTHS[0] * math.cos(neck_angle)
    upper_body_x = torso_x + SEGMENT_LENGTHS[1] * math.sin(torso_angle)
    upper_body_y = torso_y + SEGMENT_LENGTHS[1] * math.cos(torso_angle)
    
    # Left leg
    left_hip_angle = walking_angle
    left_thigh_x = upper_body_x + SEGMENT_LENGTHS[1] * math.sin(left_hip_angle)
    left_thigh_y = upper_body_y + SEGMENT_LENGTHS[1] * math.cos(left_hip_angle)
    
    left_knee_angle = left_hip_angle + math.pi / 4
    left_lower_leg_x = left_thigh_x + SEGMENT_LENGTHS[2] * math.sin(left_knee_angle)
    left_lower_leg_y = left_thigh_y + SEGMENT_LENGTHS[2] * math.cos(left_knee_angle)
    
    # Right leg
    right_hip_angle = walking_angle - math.pi
    right_thigh_x = upper_body_x + SEGMENT_LENGTHS[1] * math.sin(right_hip_angle)
    right_thigh_y = upper_body_y + SEGMENT_LENGTHS[1] * math.cos(right_hip_angle)
    
    right_knee_angle = right_hip_angle + math.pi / 4
    right_lower_leg_x = right_thigh_x + SEGMENT_LENGTHS[2] * math.sin(right_knee_angle)
    right_lower_leg_y = right_thigh_y + SEGMENT_LENGTHS[2] * math.cos(right_knee_angle)
    
    # Left arm
    left_shoulder_angle = walking_angle * 1.2
    left_upper_arm_x = upper_body_x - SEGMENT_LENGTHS[1] * math.sin(torso_angle)
    left_upper_arm_y = upper_body_y + SEGMENT_LENGTHS[1] * math.cos(torso_angle)
    
    left_elbow_angle = left_shoulder_angle + math.pi / 4
    left_lower_arm_x = left_upper_arm_x + SEGMENT_LENGTHS[3] * math.sin(left_elbow_angle)
    left_lower_arm_y = left_upper_arm_y + SEGMENT_LENGTHS[3] * math.cos(left_elbow_angle)
    
    # Right arm
    right_shoulder_angle = walking_angle * 1.2
    right_upper_arm_x = upper_body_x - SEGMENT_LENGTHS[1] * math.sin(torso_angle)
    right_upper_arm_y = upper_body_y + SEGMENT_LENGTHS[1] * math.cos(torso_angle)
    
    right_elbow_angle = right_shoulder_angle + math.pi / 4
    right_lower_arm_x = right_upper_arm_x + SEGMENT_LENGTHS[3] * math.sin(right_elbow_angle)
    right_lower_arm_y = right_upper_arm_y + SEGMENT_LENGTHS[3] * math.cos(right_elbow_angle)
    
    # Return all joint positions
    positions = [
        (BASE_X, BASE_Y),  # Base
        (torso_x, torso_y),  # Upper body
        (left_thigh_x, left_thigh_y),  # Left thigh
        (left_lower_leg_x, left_lower_leg_y),  # Left lower leg
        (right_thigh_x, right_thigh_y),  # Right thigh
        (right_lower_leg_x, right_lower_leg_y),  # Right lower leg
        (left_upper_arm_x, left_upper_arm_y),  # Left upper arm
        (left_lower_arm_x, left_lower_arm_y),  # Left lower arm
        (right_upper_arm_x, right_upper_arm_y),  # Right upper arm
        (right_lower_arm_x, right_lower_arm_y),  # Right lower arm
        (head_x, head_y)  # Head
    ]
    
    return positions

# Function to generate particles around joint positions
def generate_particles(positions, frame):
    particles = []
    walking_phase = (frame % TOTAL_FRAMES) / TOTAL_FRAMES
    
    for i in range(len(positions) - 1):
        start_pos = positions[i]
        end_pos = positions[i+1]
        
        # Number of particles per segment
        particles_per_segment = 5
        
        for j in range(particles_per_segment):
            t = j / particles_per_segment
            
            # Add some random offset to make the particles move
            offset = 5 * math.sin(t * math.pi + walking_phase * 2 * math.pi)
            angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
            
            particle_x = start_pos[0] + t * (end_pos[0] - start_pos[0]) + offset * math.sin(angle)
            particle_y = start_pos[1] + t * (end_pos[1] - start_pos[1]) + offset * math.cos(angle)
            
            # Vary particle size slightly
            size = 2 + 1 * math.sin(t * math.pi)
            
            particles.append((particle_x, particle_y, size))
    
    return particles

# Main loop
clock = pygame.time.Clock()
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with black
    screen.fill(BLACK)
    
    # Calculate joint positions for current frame
    positions = calculate_positions(frame)
    
    # Generate particles around the joint positions
    particles = generate_particles(positions, frame)
    
    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, WHITE, (int(particle[0]), int(particle[1])), int(particle[2]))
    
    # Update display
    pygame.display.flip()
    
    # Increment frame
    frame += 1
    if frame >= TOTAL_FRAMES:
        frame = 0
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
