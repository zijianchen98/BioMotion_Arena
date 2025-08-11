
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, facecolor='black')
ax.set_aspect('equal')
ax.set_xlim(-2, 8)
ax.set_ylim(-2, 4)
points, = ax.plot([], [], 'wo', markersize=8)

# Animation parameters
num_points = 15
T = 2.0  # Jump cycle duration
A = 1.2  # Jump height
vx = 1.5  # Horizontal speed
t = np.linspace(0, T, 100)

# Initialize coordinates
x = np.zeros(num_points)
y = np.zeros(num_points)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t_total = frame * 0.05
    t_in_cycle = t_total % T
    phase = 2 * np.pi * t_in_cycle / T
    
    # Center of mass trajectory (parabola)
    center_x = vx * t_total
    center_y = A * (1 - (2*(t_in_cycle/T) - 1)**2)
    
    # Body parts positions
    # Head (0)
    x[0], y[0] = center_x, center_y + 0.6
    
    # Shoulders (1,2)
    x[1], y[1] = center_x - 0.4, center_y + 0.3
    x[2], y[2] = center_x + 0.4, center_y + 0.3
    
    # Arms (3-6)
    arm_ang = np.sin(phase) * 0.8
    x[3] = x[1] + 0.3*np.cos(arm_ang)
    y[3] = y[1] + 0.3*np.sin(arm_ang)
    x[4] = x[2] + 0.3*np.cos(-arm_ang)
    y[4] = y[2] + 0.3*np.sin(-arm_ang)
    x[5] = x[3] + 0.25*np.cos(arm_ang-0.5)
    y[5] = y[3] + 0.25*np.sin(arm_ang-0.5)
    x[6] = x[4] + 0.25*np.cos(-arm_ang-0.5)
    y[6] = y[4] + 0.25*np.sin(-arm_ang-0.5)
    
    # Hips (7,8)
    x[7], y[7] = center_x - 0.3, center_y - 0.2
    x[8], y[8] = center_x + 0.3, center_y - 0.2
    
    # Legs (9-14)
    leg_ang = np.sin(phase + np.pi) * 0.6
    x[9] = x[7] + 0.4*np.cos(leg_ang)
    y[9] = y[7] + 0.4*np.sin(leg_ang)
    x[10] = x[8] + 0.4*np.cos(-leg_ang)
    y[10] = y[8] + 0.4*np.sin(-leg_ang)
    x[11] = x[9] + 0.35*np.cos(leg_ang-0.3)
    y[11] = y[9] + 0.35*np.sin(leg_ang-0.3)
    x[12] = x[10] + 0.35*np.cos(-leg_ang-0.3)
    y[12] = y[10] + 0.35*np.sin(-leg_ang-0.3)
    x[13] = x[11] + 0.2*np.cos(leg_ang-0.6)
    y[13] = y[11] + 0.2*np.sin(leg_ang-0.6)
    x[14] = x[12] + 0.2*np.cos(-leg_ang-0.6)
    y[14] = y[12] + 0.2*np.sin(-leg_ang-0.6)
    
    # Update plot limits
    ax.set_xlim(center_x-3, center_x+3)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=200, interval=20, blit=True)
plt.show()
