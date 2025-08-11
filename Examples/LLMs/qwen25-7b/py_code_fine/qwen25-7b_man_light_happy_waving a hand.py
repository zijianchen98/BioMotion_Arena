
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the hand-waving man
positions = [
    [0_x, th_x, fh_x, ll_x, lr_x, rl_x, rr_x, fl_x, fr_x, t_x, m_x, b_x, wl_x, wr_x]
]

def update_points(num, points, line):
    # Update the positions of the points
    new_positions = []
    for i in range(15):
        new_positions.append([positions[num][i_x], positions[num][th_x], positions[num][fh_x],
                              positions[num][ll_x], positions[num][lr_x], positions[num][rl_x],
                              positions[num][rr_x], positions[num][fl_x], positions[num][fr_x],
                              positions[num][t_x], positions[num][m_x], positions[num][b_x],
                              positions[num][wl_x], positions[num][wr_x]])
    
    # Update the points' positions
    for i in range(15):
        line.set_data(new_positions[i])
    return line,

def init():
    line.set_data([], [])
    return line,

# Initial positions of the points
positions.append([
    0_x = 0_x + 0_x * np.cos(2 * np.pi * num / 15),
    th_x =  th_x +  th_x * np.cos(2 * np.pi * num / 15),
    fh_x =  fh_x +  fh_x * np.cos(2 * np.pi * num / 15),
    ll_x =  ll_x +  ll_x * np.cos(2 * np.pi * num / 15),
    lr_x =  lr_x +  lr_x * np.cos(2 * np.pi * num / 15),
    rl_x =  rl_x +  rl_x * np.cos(2 * np.pi * num / 15),
    rr_x =  rr_x +  rr_x * np.cos(2 * np.pi * num / 15),
    fl_x =  fl_x +  fl_x * np.cos(2 * np.pi * num / 15),
    fr_x =  fr_x +  fr_x * np.cos(2 * np.pi * num / 15),
    t_x =  t_x +  t_x * np.cos(2 * np.pi * num / 15),
    m_x =  m_x +  m_x * np.cos(2 * np.pi * num / 15),
    b_x =  b_x +  b_x * np.cos(2 * np.pi * num / 15),
    wl_x =  wl_x +  wl_x * np.cos(2 * np.pi * num / 15),
    wr_x =  wr_x +  wr_x * np.cos(2 * np.pi * num / 15)
])

fig, ax = plt.subplots()
ax_x = ax.scatter([], [], c='white')
 th_x = ax.scatter([], [], c='white')
 fh_x = ax.scatter([], [], c='white')
 ll_x = ax.scatter([], [], c='white')
 lr_x = ax.scatter([], [], c='white')
 rl_x = ax.scatter([], [], c='white')
 rr_x = ax.scatter([], [], c='white')
 fl_x = ax.scatter([], [], c='white')
 fr_x = ax.scatter([], [], c='white')
 t_x = ax.scatter([], [], c='white')
 m_x = ax.scatter([], [], c='white')
 b_x = ax.scatter([], [], c='white')
 wl_x = ax.scatter([], [], c='white')
 wr_x = ax.scatter([], [], c='white')

line = [ll_x, lr_x, rl_x, rr_x, fl_x, fr_x, t_x, m_x, b_x, wl_x, wr_x

ax_x = ax.add_collection(line)
 ax.set_xlim(-1, 1)
 ax.set_ylim(-1, 1)
 ax.set_aspect('equal'
 ax.axis('off

ani = init
 ani = animation.FuncAnimation(fig, update_points, frames=15, fargs=(positions, line), init_func=init, blit=True)

plt.show()
