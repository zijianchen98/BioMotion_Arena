
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
DURATION = 60  # seconds
FPS = 30
STiffness = 10
mass = 80
angle = 0.1
time_step = 1/FPS
max_speed = 1.5
max_force = 0.5

def simulate_walking():
    # Initial conditions
    positions = [np.random.rand() * 400 for _ in range(NUM_POINTS)]
    velocities = [0 for _ in range(NUM_POINTS)]
    accelerations = [0 for _ in range(NUM_POINTS)]

    fig, ax = plt.subplots()
    ax.set_xlim((-400, 400)
    ax.set_ylim((-200, 200))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    line_points, = ax.plot(positions, 0, 'o', color='white')

    def update(frame):
        global angle
        forces = []
        for i in range(NUM_POINTS - 1):
            force = -(positions[i] - positions[i+1]) / stiffness
            forces.append(force)
        net_force = sum(forces)

        if abs(net_force) > max_force:
            net_force = np.sign(net_force) * max_force

        accelerace = net_force / mass
        for i in range(NUM_POINTS):
            velocities[i] += accelerace[i] * time_step
            positions[i] += velocities[i] * time_step

        if positions[0] > 400 or positions[0] < -400:
            angle += 0.01
            for i in range(NUM_POINTS):
                positions[i] *= np.cos(angle)
                velocities[i] *= np.cos(angle)

        if abs(velocities[0]) < max_speed:
            for i in range(NUM_POINTS):
                positions[i] -= velocities[i] * time_step
            velocities[i] = 0

        for i in range(NUM_POINTS):
            x = positions[i]
            y = 0
            if i == 0:
                x = 400 * np.cos(angle)
                y = 400 * np.sin(angle)

            if i == NUM_POINTS - 1:
                x = -400 * np.cos(angle)
                y = -400 * np.sin(angle)

            if i > 0 and i < NUM_POINTS - 1:
                x = ( (positions[i-1] + positions[i+1]) / 2

            line_points.set_data(x, y)

        return line_points,

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, DURATION*time_step, time_step),
                                interval=int(1000/FPS), blit=True)

    plt.show()

simulate_walking()
