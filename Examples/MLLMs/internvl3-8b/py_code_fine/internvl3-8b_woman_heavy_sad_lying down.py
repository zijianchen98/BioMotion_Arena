
import matplotlib.pyplot as plt

colors = ['white'] * 15
positions = [(400, 300), (400, 250), (200, 200), (400, 150), (600, 200), (200, 100), (400, 50), (600, 150), (200, 50), (400, 400), (600, 400)]

x = [pos[0] for pos in positions]
y = [pos[1] for pos in positions]

fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=colors)
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])

for i in range(100):
    for j in range(9):
        x[j] = positions[j][0] + (1 - i / 100) * 20
        y[j] = positions[j][1] + (1 - i / 100) * 20
    scatter.set_offsets(list(zip(x, y)))
    plt.pause(0.001)

plt.show()
