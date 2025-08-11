
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Configuration
NUM_POINTS = 15
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'

# Define positions
init_positions = np.array([
    [250, 450], [300, 250], [350, 150], [400, 50], [450, 150], 
    [500, 250], [550, 450], [600, 550], [570, 400], [540, 250], 
    [520, 150], [500, 50], [480, 150], [460, 250], [440, 450]  
])

def update_position(frame, lines, positions):
    # For simplicity, linear movement along the X-axis
    x_shift = frame * 1.5
    new_positions = init_positions + np.array([x_shift, 0])
    for i, line in enumerate(lines):
        line.set_data(new_positions[i][0], new_positions[i][1])
    return lines

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(100, 900)
ax.set_ylim(100, 700)
lines = [ax.plot([], [], 'o', color=POINT_COLOR)[0] for _ in range(NUM_POINTS)]

ani = animation.FuncAnimation(
    fig, update_position, fargs=(lines, init_positions), 
    frames=100, interval=20, blit=True
)

plt.axis('off')
plt.show()
