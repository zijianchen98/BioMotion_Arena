
import matplotlib.pyplot as plt
import time

# Define the positions of the lights for the woman (these positions mimic the motion)
light_positions = [
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
    (3, 5), (4, 5), (6, 5), (2, 6), (6, 6),
    (2, 7), (6, 7)
]

number_of_frames = 50  # The number of frames in the animation

for i in range(number_of_frames):
    if i % 10 == 0:  # Change color when one frame is done
        light_colors = ['white' for _ in light_positions]
    else:
        light_colors = ['white' for _ in light_positions]
        
    # Calculate new positions (this would depend on the physics of the forward roll)
    for idx, (x, y) in enumerate(light_positions):
        if i < number_of_frames // 3:
            # Simulate rolling motion
            if x != 5 and y != 3:
                light_positions[idx] = (x-1, y+1)
        elif i < 2 * number_of_frames // 3:
            x, y = (x+1, y+1) if (idx & 1) else (x-1, y)
            light_positions[idx] = (x, y)
        else:
            # Final recovery phase
            x, y = (5, 1) if y == 7 else (x + i % 3 - 1, y)
            light_positions[idx] = (x, y if x == 2 or x == 6 else y+2*i)
        
    plt.figure(figsize=(8, 10))
    for (x, y), color in zip(light_positions, light_colors):
        plt.scatter(x, y, color=color, s=100)
    plt.xlim(0, 7)
    plt.ylim(0, 8)
    plt.axis('off')
    plt.ion()
    plt.show()
    time.sleep(0.1)  # Adjust this to change the speed of the animation
    
    # Check for a full cycle to stop
    if i == number_of_frames - 1:
        plt.close()
        break
