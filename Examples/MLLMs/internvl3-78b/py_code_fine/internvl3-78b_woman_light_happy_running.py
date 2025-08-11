
import cv2
import numpy as np
import sys

def draw_frame(frame, points, frame_size):
    # Create a black background
    img = np.zeros((frame_size, frame_size, 3), dtype="uint8")

    # Draw white points
    for point in points:
        cv2.circle(img, (int(point[0]), int(point[1])), 2, (255, 255, 255), -1)
    
    # Display the frame
    window_name = "Point-light Animation"
    cv2.imshow(window_name, img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        sys.exit()

def main():
    frame_size = 600
    num_points = 15
    points = np.random.rand(num_points, 2) * frame_size
    velocity = np.random.rand(num_points, 2) * 5 - 2.5

    while True:
        draw_frame(0, points, frame_size)
        points += velocity

        # Keep points within the frame
        for i in range(num_points):
            if points[i][0] <= 0 or points[i][0] >= frame_size:
                velocity[i][0] *= -1
            if points[i][1] <= 0 or points[i][1] >= frame_size:
                velocity[i][1] *= -1

if __name__ == "__main__":
    main()
