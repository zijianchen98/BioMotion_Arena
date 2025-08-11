

    # import matplotlib.pyplot as plt

    # import matplotlib.animation as animation

    # import numpy as np

    # num_frames = 60

    # def get_positions(t):

    #     s = np.sin(np.pi * t / 30)

    #     positions = np.array([

    #         [0, 85],  # head

    #         [-12, 65],  # left shoulder

    #         [12, 65],  # right shoulder

    #         [-12, 55],  # left elbow

    #         [12 + 1*s, 55 + 5*s],  # right elbow

    #         [-12, 35],  # left wrist

    #         [12 + 3*s, 35 + 10*s],  # right wrist

    #         [12 + 3*s + 2*s, 35 + 10*s - 5*(1-s)],  # right hand1

    #         [12 + 3*s + 4*s, 35 + 10*s - 10*(1-s)],  # right hand2

    #         [-5, 50],  # left hip

    #         [5, 50],  # right hip

    #         [-10, 25],  # left knee

    #         [10, 25],  # right knee

    #         [-10, 0],  # left ankle

    #         [10, 0]   # right ankle

    #     ])

    #     return positions

    # fig, ax = plt.subplots()

    # ax.set_facecolor('black')

    # ax.set_xlim(-20, 20)

    # ax.set_ylim(0, 90)

    # ax.set_aspect('equal')

    # ax.set_axis_off()

    # positions = get_positions(0)

    # scat = ax.scatter(positions[:,0], positions[:,1], c='white', s=20)

    # def update(t):

    #     positions = get_positions(t)

    #     scat.set_offsets(positions)

    #     return scat,

    # anim = animation.FuncAnimation(fig, update, frames=num_frames, interval=33, blit=True)

    # plt.show()

    # 