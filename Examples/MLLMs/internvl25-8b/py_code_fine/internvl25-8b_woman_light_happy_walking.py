
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from copy import deepcopy

# Constants
num_points = 15
background_color = 'black'
line_style ='solid'
vertex_numbers = ['hip', 'elbow','shoulder', 'elbow', 'wrist', 
                  'ankle', 'floor', 'ankle', 'knee', 'thigh', 
                  'hip','shoulder', 'elbow', 'wrist', 'floor']

def walk_animation():
    animation = np.zeros((100, 400, 3))

    for step in range(100):  # 100 steps
        positions = get_walking_positions(step = step)
        for idx, (x, y) in enumerate(positions):
            animation[step, idx, :] = (1, 1, 1)  # Draw white points

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.set_aspect('datalim', 'box')
    ax.set_xlim(2000, -2000)  # Expand x limits
    ax.set_ylim(2000, -2000)  # Expand y limits
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.autoscale(False)

    for idx, labels in enumerate(vertex_numbers):
        ax.add_patch(PathPatch(PathPatch(
            deepcopy({'left': positions[idx][0], 
                      'bottom': positions[idx][1],
                      'right': positions[idx][2],
                      'top': positions[idx][3]}))),
                facecolor='white',
                linewidth=1,
                edgecolor='black',
                label=labels,
                clip_on=False,  # This makes the lines clip
                linewidth=1,
                capstyle='round'))

    plt.savefig('point_light_stimulus.gif', format='GIF', dpi=100, transparent=True)
    plt.close(fig)

def get_walking_positions(step=0):
    # Here we use a simple animation cycle for demonstration
    # Replace with a more complex motion if needed
    if step == 0:
        return [(-2000, 0), (2000, 0), (2000, 0), (2000, 0), (2000, 0),
                (-2000, 0), (0, 0), (-2000, 0), (0, 0), (0, 0),
                (-2000, 0), (2000, 0), (2000, 0), (2000, 0), (2000, 0)]
    elif step == 1:
        return [(1800, -500), (2000, 500), (1600, 650), (1200, 650), (1000, 650),
                '(1000, 800)', (1400, 1200), '(-1000, 800)', '(1000, 800)',
                '(-1000, 500)', '(-1000, 300)', '(-1200, 500)', '(-1600, 500), (1600, 500)', (1800, -500)]
    elif step == 2:
        return [(2000, 0), (1600, 500), (1400, 600), (1400, 700), (1400, 800),
                '(1200, 500), (1200, 800), (-800, 700), '(800, 700), (1100, 500)',
                '(1100, 500), (800, 300), `(1000, 500), (1400, 500), (1600, 500)]
    elif step == 3:
        return [(-2000, 0), (1600, 500), (1200, 600), (1200, 700), (1200, 800),
                '(1000, 600), (1050, 800), (-800, 800), '(800, 700), (1200, 500)',
                '(1200, 550), (1000, 550), `(800, 300), (1100, 500), (1400, 500)]
    elif step == 4:
        return [(0, 0), (1400, 0), (1400, 250), (1300, 290), (1300, 320),
                '(-1000, 330), (1000, 0), (1300, 250), (-800, 250), (-800, 260),
                '(1000, 330), (1400, 250), (1400, 100), (1800, 250)]
    elif step == 5:
        return [(1500, 500), (1800, 0), (1650, 250), (1500, 250), (1500, 300),
                '(1400, 250), (1400, 350), (-600, 350), '(600, 350), (1000, 250),
                '(900, 250), (1100, 250), '(900, 150), (1050, 250), (1100, 250)]
    elif step == 6:
        return [(2000, 0), (1600, 300), (1600, 350), (1600, 390), (1600, 450),
                '(1800, 0), (1600, 200), (-600, 300), '(600, 300), (1000, 250),
                '(600, 250), (800, 250), '(400, 100), (600, 250), (800, 300)]
    elif step == 7:
        return [(2400, 0), (2400, 400), (2250, 500), (2200, 470), (2200, 450),
                '(2250, 400), (2300, 300), (-400, 400), '(400, 320), (1800, 300),
                '(1200, 400), (1100, 450), '(800, 450), (900, 450), (2100, 350)]
    elif step == 8:
        return [(2000, 450), (1100, 250), (1000, 270), (1000, 310), (1000, 360),
                '(800, 250), (900, 300), (-200, 450), '(200, 330), (1000, 250),
                '(800, 290), (700, 250), '(900, 100), (700, 420), (1600, 500)]

    return [(0, 0)] * num_points

walk_animation()
