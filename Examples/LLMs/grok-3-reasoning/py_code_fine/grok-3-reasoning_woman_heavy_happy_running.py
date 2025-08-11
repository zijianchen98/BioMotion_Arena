
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define parameters
T = 100  # number of frames per cycle
base_x = [0, 0, -0.2, 0.2, -0.3, 0.3, -0.4, 0.4, 0, -0.1, 0.1, -0.1, 0.1, -0.1, 0.1]
base_y = [1.5, 1.3, 1.2, 1.2, 1.0, 1.0, 0.8, 0.8, 0, -0.5, -0.5, -1.0, -1.0, -1.1, -1.1]
body_points = [0,1,2,3,8]  # head, neck, L shoulder, R shoulder, hip

# Define motion parameters for limb points
b = [0]*15
phi = [0]*15
d = [0.1 if i in body_points else 0.05 for i in range(15)]
psi = [0]*15

# Set parameters for left side limbs
for i in [4,6,9,11,13]:  # L elbow, L wrist, L knee, L ankle, L foot
    b[i] = 0.3 if i in [4,6] else 0.5
    phi[i] = math.pi if i in [4,6] else 0
    d[i] = 0.05 if i in [4,6] else 0.3
    psi[i] = 0 if i in [4,6] else math.pi / 2

# Set parameters for right side limbs
for i in [5,7,10,12,14]:  # R elbow, R wrist, R knee, R ankle, R foot
    b[i] = 0.3 if i in [5,7] else 0.5
    phi[i] = 0 if i in [5,7] else math.pi
    d[i] = 0.05 if i in [5,7] else 0.3
    psi[i] = 0 if i in [5,7] else math.pi / 2

# Set up the figure
fig = plt.figure(facecolor='black')
ax = plt.axes(xlim=(-1.5,1.5), ylim=(-1.5,2.0))
ax.set_facecolor('black')
points = ax.scatter([0]*15, [0]*15, c='white', s=10)

def update(frame):
    t = frame % T
    x = []
    y = []
    for i in range(15):
        if i in body_points:
            x.append(base_x[i])
            y.append(base_y[i] + 0.1 * math.sin(4*math.pi*t/T))
        else:
            x.append(base_x[i] + b[i] * math.sin(2*math.pi*t/T + phi[i]))
            y.append(base_y[i] + d[i] * math.sin(2*math.pi*t/T + psi[i]))
    points.set_offsets(list(zip(x,y)))
    return points,

anim = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.axis('off')
plt.show()
