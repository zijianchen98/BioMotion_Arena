
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame, points, angle_end):
    point_size = 200
    center = np.array([480, 350])
    
    body = []

    body.append(np.array([center[0] + 80 * np.cos(np.radians(frame - angle_end)), 
                          center[1] - 100 * np.sin(np.radians(frame - angle_end))]))
    
    body.append(np.array([center[0] + 110 * np.cos(np.radians(frame - angle_end)), 
                          center[1] - 130 * np.sin(np.radians(frame - angle_end))]))

    body.append(np.array([center[0] + 90 * np.cos(np.radians(frame - angle_end)), 
                          center[1] - 90 * np.sin(np.radians(frame - angle_end))]))

    body.append(np.array([center[0] + 180 * np.cos(np.radians(frame - angle_end)), 
                          center[1] + 100 * np.sin(np.radians(frame - angle_end))]))

    body.append(np.array([center[0] + 80 * np.cos(np.radians(frame - angle_end)), 
                          center[1] + 90 * np.sin(np.radians(frame - angle_end))]))

    for i in range(15):
        points[i].set_data([body[0][0] + (body[i][0] - body[0][0]) / 4 * (i - 0) / 14,
                            body[0][1] + (body[i][1] - body[0][1]) / 4 * (i - 0) / 14])
                            
    return points

angle_end = 0

points = [plt.Circle(0, 0, color="white", lw=0) for _ in range(15)]
body = [np.array([480, 350]), np.array([480 + 80, 350 - 100]), np.array([480 + 90, 350 - 90]),
        np.array([480 + 180, 350 + 100]), np.array([480 + 80, 350 + 90])]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(400, 570)
ax.set_ylim(300, 440)
ax.set_axis_off()  # Hide axes
ani = animation.FuncAnimation(fig, update, frames=range(0, 180, 2), fargs=(points, angle_end),
                              interval=50, blit=True)
plt.show()
