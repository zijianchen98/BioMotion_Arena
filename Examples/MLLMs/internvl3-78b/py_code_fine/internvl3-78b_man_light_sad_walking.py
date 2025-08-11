
import pyglet
import pyglet.gl as gl

class PointLightAnimation(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(PointLightAnimation, self).__init__(*args, **kwargs)
        self.frames_per_second = 60
        self.width = 800
        self.height = 600
        self.circles = [
            # Define the initial positions of the circles. Modify these as desired.
            (400, 300, 3), (410, 290, 2), (430, 270, 2), (450, 250, 2), (470, 230, 2),
            (490, 230, 2), (510, 250, 2), (530, 270, 2), (550, 290, 2), (560, 300, 2),
            (540, 320, 2), (520, 340, 2), (500, 360, 2), (480, 380, 2), (460, 400, 2)
        ]
        self.set_caption("Sadman Walking Animation")
        self.set_visible(True)

    def on_draw(self):
        self.clear()
        gl.glColor3f(1, 1, 1)  # white color
        for x, y, radius in self.circles:
            self.draw_circle(x, y, radius)

    def draw_circle(self, x, y, radius):
        iterations = 20
        s = gl.glSin(2 * gl.pi / iterations)
        c = gl.glCos(2 * gl.pi / iterations)

        dx, dy = radius, 0.0
        gl.glBegin(gl.GL_TRIANGLE_FAN)  
        gl.glVertex2f(x, y)
        for i in range(iterations + 1):
            gl.glVertex2f(x + dx, y + dy)
            dx, dy = (dx * c + dy * s) - (dx * s + dy * c)
        gl.glEnd()

    def update(self, dt):
        self.move_points()

    def move_points(self):
        step = 1
        for i, (x, y, _) in enumerate(self.circles):
            # Simple pattern movement. Modify based on desired animation.
            self.circles[i] = (x, y + step, 3)
            if y + step > self.height - 20 or y + step < 20:
                step = -step

if __name__ == '__main__':
    window = PointLightAnimation(caption='Point Light Animation', width=800, height=600, vsync=True)
    pyglet.clock.schedule_interval(window.update, 1.0 / window.frames_per_second)
    pyglet.app.run()
