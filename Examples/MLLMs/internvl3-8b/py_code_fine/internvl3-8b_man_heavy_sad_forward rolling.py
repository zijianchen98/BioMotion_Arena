
import time
from termcolor import colored

# Initialize the screen size
width, height = 80, 25

# Position of the point-light (representing the 'sadman')
position = [40, 12]  # x, y

# Define the motion function
def move_sadman():
    global position
    position[0] -= 1  # Move left
    if position[0] < 0:
        position[0] = width-1  # Move back to right end when reaching the left end
    
    # Clear the screen
    print("\x1b[H\x1b[J")
    
    # Create an empty map
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Draw the sadman
    for x in range(max(0, position[0]-5), min(width, position[0]+5)):
        for y in range(max(0, position[1]-3), min(height, position[1]+3)):
            if ((x - position[0])**2 + (y - position[1])**2) <= 16:  # Circle with diameter 4
                if (x - position[0] + (y - position[1]) * 1j) % 2 == 0:
                    screen[y][x] = colored('.', 'white')

    # Print the screen
    for row in screen:
        print(''.join(row))

# Run the animation
while True:
    move_sadman()
    time.sleep(0.1)
