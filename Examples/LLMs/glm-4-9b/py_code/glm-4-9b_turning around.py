
import tkinter as tk
import math
import time

# Constants
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
NUM_LIGHTS = 15
 ANIMATION_CYCLE = 10  # seconds for a full cycle

class Light:
    def __init__(self, canvas, x, y, radius=5, color='white'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color)

    def move(self, new_x, new_y):
        self.canvas.move(self.id, new_x - self.x, new_y - self.y)
        self.x, self.y = new_x, new_y

class Animation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.lights = []
        self.create_lights()
        self.start_animation()

    def create_lights(self):
        angle_step = 360 / NUM_LIGHTS
        for i in range(NUM_LIGHTS):
            angle = math.radians(i * angle_step)
            x = CENTER_X + 100 * math.cos(angle)
            y = CENTER_Y + 100 * math.sin(angle)
            self.lights.append(Light(self.canvas, x, y))

    def start_animation(self):
        self.animate()
        self.root.after(50, self.start_animation)

    def animate(self):
        for i, light in enumerate(self.lights):
            angle = math.radians((time.time() * 36) % 360 + (i * 360 / NUM_LIGHTS))
            x = CENTER_X + 100 * math.cos(angle)
            y = CENTER_Y + 100 * math.sin(angle)
            light.move(x, y)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Point-Light Stimulus Animation")
    app = Animation(root)
    root.mainloop()
