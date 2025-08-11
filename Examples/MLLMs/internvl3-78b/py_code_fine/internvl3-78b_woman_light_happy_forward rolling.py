
import random
import time

# define the number of point-lights
num_points = 15

# define the size of the frame
frame_size = 50

# define the position of the point-lights
points = [(random.uniform(0, frame_size), random.uniform(0, frame_size)) for _ in range(num_points)]

# define the velocity of the point-lights
velocities = [(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)) for _ in range(num_points)]

# define the function to update the positions of the point-lights
def update_points(points, velocities):
    for i in range(len(points)):
        points[i] = (points[i][0] + velocities[i][0], points[i][1] + velocities[i][1])
        
        # if the point-light hits the edge of the frame, reverse its velocity
        if points[i][0] < 0 or points[i][0] > frame_size:
            velocities[i] = (-velocities[i][0], velocities[i][1])
        if points[i][1] < 0 or points[i][1] > frame_size:
            velocities[i] = (velocities[i][0], -velocities[i][1])
            
    return points, velocities

# define the function to draw the point-lights
def draw_points(points):
    for point in points:
        # print the point-light
        print("-", end="")
        for _ in range(int(point[0]) - 1):
            print(" ", end="")
        print("○")
        
        for _ in range(int(point[1]) - 1):
            print(" ", end="")
        print("-")

    print("
")
    
# animate the point-lights
while True:
    points, velocities = update_points(points, velocities)
    draw_points(points)
    time.sleep(0.1)  # pause for 0.1 seconds between frames
