
import pyglet
import pyglet.gl as gl
import numpy as np

window_width = 600
window_height = 600
frame_rate = 30

class PointLight(pyglet.text.Label):
    def __init__(self, x, y):
        super().__init__(text='.', x=x, y=y, font_size=10, color=(255, 255, 255, 255))

class BiologicalMotionAnimation:
    def __init__(self):
        self.positions = np.zeros((15, 2))
        self.initial_pos = np.array([
            [window_width // 2, window_height - 50],
            [window_width // 2 - 10, window_height - 60],
            [window_width // 2 + 10, window_height - 60],
            [window_width // 2 - 20, window_height - 70],
            [window_width // 2 + 20, window_height - 70],
            [window_width // 2 - 30, window_height - 80],
            [window_width // 2 - 10, window_height - 80],
            [window_width // 2 + 10, window_height - 80],
            [window_width // 2 + 30, window_height - 80],
            [window_width // 2 - 40, window_height - 90],
            [window_width // 2 - 20, window_height - 90],
            [window_width // 2, window_height - 90],
            [window_width // 2 + 20, window_height - 90],
            [window_width // 2 + 40, window_height - 90],
            [window_width // 2, window_height - 100]
        ])
        self.positions = self.initial_pos.copy()

    def update(self):
        self.positions += np.random.normal(0, 0.5, size=(15, 2))
        for i in range(15):
            if self.positions[i][0] < 0 or self.positions[i][0] > window_width:
                self.positions[i][0] = window_width - self.positions[i][0]
            if self.positions[i][1] < 0 or self.positions[i][1] > window_height:
                self.positions[i][1] = window_height - self.positions[i][1]

    def draw(self):
        gl.glPointSize(5)
        gl.glColor3f(1.0, 1.0, 1.0)
        gl.glBegin(gl.GL_POINTS)
        for pos in self.positions:
            gl.glVertex2f(pos[0], pos[1])
        gl.glEnd()

window = pyglet.window.Window(window_width, window_height)
gl.glClearColor(0, 0, 0, 1)

motion = BiologicalMotionAnimation()

@window.event
def on_draw():
    window.clear()
    motion.draw()

def update(dt):
    motion.update()

pyglet.clock.schedule_interval(update, 1/frame_rate)
pyglet.app.run()
