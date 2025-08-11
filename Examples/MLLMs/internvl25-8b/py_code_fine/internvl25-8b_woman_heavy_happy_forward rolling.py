
import time
import os
import numpy as np
import cv2

def draw_points(points):
    for point in points:
        cv2.circle(frame, point, 1, (255, 255, 255), -1)

def main():
    # Initialize the frame dimensions
    frame_width = 800
    frame_height = 600

    # Initialize the background to pure black
    frame = np.zeros((frame_height, frame_width, 3), dtype="uint8")
    
    # Define the number of bodies and points
    num_bodies = 15
    points = []

    # Define the initial positions in a specific arrangement
    initial_positions = [
        (100, 50),
        (120, 50),
        (140, 50),
        (160, 30),
        (180, 30),
        (200, 30),
        (220, 30),
        (240, 50),
        (260, 50),
        (280, 50),
        (300, 50),
        (320, 30),
        (240, 170),
        (160, 130),
        (80, 120)
    ]
    
    # Populate points with the initial positions
    for pos in initial_positions:
        points.append(pos)

    while True:
        # Clear frame with black
        frame[:] = 0
        
        # Draw the points
        draw_points(points)

        # Display the frame
        window_name = "Pointlights animation"
        cv2.imshow(window_name, frame)
        
        # Check for the 'q' key to exit the simulation
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
            
        # Transition frames
        points = [(p[0] + 2, p[1] + 2) if (p[0] < frame_width and p[1] < frame_height) else (p[0] - 2, p[1] - 2) for p in points]

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
