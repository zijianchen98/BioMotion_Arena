
import tkinter as tk
import math
import time

# Constants
WIDTH, HEIGHT = 800, 600  # Canvas width and height
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2  # Center of the canvas
POINT_LIGTH_COUNT = 15  # Number of points
GRAVITY = 9.8  # Acceleration due to gravity
JUMP_SPEED = 5  # Initial upward speed
ANIMATION_INTERVAL = 20  # Milliseconds

# Calculate the radius of the ellipse according to the count of point-lights
ELLIPSE_RADIUS_X, ELLIPSE_RADIUS_Y = WIDTH * 0.3, HEIGHT * 0.2


class PointLightAnimation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.point_lights = [(canvas.create_oval(CENTER_X - 3, CENTER_Y - 3, CENTER_X + 3,
                                                  CENTER_Y + 3, fill='white', outline='white')) for _ in range(POINT_LIGTH_COUNT)]
        self.y_position = CENTER_Y
        self.jump_velocity = JUMP_SPEED
        self.time_step = 0.1
        self.time = 0

    def update(self):
        # Calculate new position based on a simple parabolic motion
        self.time += self.time_step
        self.jump_velocity -= GRAVITY * self.time_step
        new_y_position = self.y_position + self.jump_velocity * self.time_step

        # Change x and y positions of the point-lights
        for i, point_light in enumerate(self.point_lights):
            angle = 2 * math.pi * i / POINT_LIGTH_COUNT
            x_offset = math.cos(angle) * ELLIPSE_RADIUS_X
            y_offset = math.sin(angle) * ELLIPSE_RADIUS_Y
            x = CENTER_X + x_offset
            y = new_y_position + y_offset
            self.canvas.coords(point_light, x - 3, y - 3, x + 3, y + 3)

        # Check for bottom boundary
        if new_y_position >= HEIGHT - ELLIPSE_RADIUS_Y:
            new_y_position = HEIGHT - ELLIPSE_RADIUS_Y
            self.jump_velocity *= -0.5  # Bounce with energy loss

        self.y_position = new_y_position

        # Schedule the update method to be called again after ANIMATION_INTERVAL milliseconds
        self.canvas.after(ANIMATION_INTERVAL, self.update)


def main():
    # Create main window
    window = tk.Tk()
    window.title("Jumping Forward Point-Light Animation")

    # Create canvas
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='black')
    canvas.pack()

    # Create the animation
    animation = PointLightAnimation(canvas)

    # Start the animation
    animation.update()

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
