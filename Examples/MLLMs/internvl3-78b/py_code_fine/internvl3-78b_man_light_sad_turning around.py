
import tkinter as tk
import math

# Animation parameters
WIDTH, HEIGHT = 400, 400
DOT_RADIUS = 3
FPS = 60
FRAME_DELAY = 1000 // FPS
N_DOTS = 15

class PointLightAnimation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.dots = []
        self.init_dots()
        self.animate()

    def init_dots(self):
        angles = [i * (2 * math.pi) / N_DOTS for i in range(N_DOTS)]
        for angle in angles:
            x = WIDTH // 2 + math.cos(angle) * 100
            y = HEIGHT // 2 + math.sin(angle) * 100
            dot = self.canvas.create_oval(x - DOT_RADIUS, y - DOT_RADIUS,
                                          x + DOT_RADIUS, y + DOT_RADIUS,
                                          fill="white")
            self.dots.append((dot, angle))

    def animate(self):
        for dot, angle in self.dots:
            angle += 0.05
            angle %= 2 * math.pi
            x = WIDTH // 2 + math.cos(angle) * 100
            y = HEIGHT // 2 + math.sin(angle) * 100
            self.canvas.coords(dot, x - DOT_RADIUS, y - DOT_RADIUS,
                               x + DOT_RADIUS, y + DOT_RADIUS)
        self.canvas.after(FRAME_DELAY, self.animate)

# Create the main window
root = tk.Tk()
root.title("Biological Motion Animation")

# Create the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Start the animation
animation = PointLightAnimation(canvas)

# Run the main loop
root.mainloop()
