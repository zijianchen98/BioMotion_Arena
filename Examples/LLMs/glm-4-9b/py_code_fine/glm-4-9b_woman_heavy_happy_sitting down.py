
import tkinter as tk
import math

class PointMotion:
    def __init__(self, canvas):
        self.canvas = canvas
        self.points = []
        self.init_points()
        self.time = 0

    def init_points(self):
        # Initialize the positions of the 15 points in a way that
        # represents the silhouette of a woman sitting down.
        # The positions are randomized to simulate the weight.
        for _ in range(15):
            x = math.sin(math.radians(self.time)) * 100 + 150
            y = math.cos(math.radians(self.time)) * 50 + 100
            point = self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='white', outline='white')
            self.points.append(point)

    def update(self):
        # Update the positions of the points to simulate the movement
        self.canvas.delete('all')
        self.time += 0.1
        for i, point in enumerate(self.points):
            angle = math.radians(self.time + i * (360 / 15))
            x = math.sin(angle) * 100 + 150
            y = math.cos(angle) * (50 - i * 0.5) + 100  # Decreases in height to simulate sitting
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='white', outline='white')

def main():
    root = tk.Tk()
    root.configure(background='black')
    canvas = tk.Canvas(root, width=300, height=200, background='black')
    canvas.pack()
    animation = PointMotion(canvas)
    def animate():
        animation.update()
        root.after(50, animate)
    animate()
    root.mainloop()

if __name__ == '__main__':
    main()
