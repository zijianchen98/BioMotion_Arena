
import os
import cv2
import numpy as np

class Animation:
    def __init__(self):
        self.background = np.zeros((1024, 1024, 3), dtype=np.uint8)  # Black background with a size of 1024x1024 px
        self.width = 1024
        self.height = 1024
        self.point_lights = []

    def _add_point_light(self, x, y):
        self.point_lights.append((x, y))

    def _move_point_lights(self, delta_x, delta_y):
        for light in self.point_lights:
            # If it moves out of the screen, wrap it around to opposite side
            new_x = (light[0] + delta_x) % self.width
            new_y = (light[1] + delta_y) % self.height
            self.point_lights.remove(light)
            self.point_lights.append((new_x, new_y))

    def _draw_frame(self):
        # Draw black background
        frame = self.background.copy()
        for light in self.point_lights:
            cv2.circle(frame, light, 2, (255, 255, 255), -1)
        return frame

    def animate(self):
        # Starting positions of point-lights
        start_positions = [
            (250, 250),  # head
            (550, 250),  # head

            (250, 450),  # torso
            (750, 450),
            (250, 650),
            (750, 650)

            (375, 275),  # arms
            (425, 275),
            (575, 275),
            (625, 275),
            (375, 600),
            (425, 600),
            (575, 600),
            (625, 600)

            (375, 300),  # hips & legs
            (425, 300),
            (575, 300),
            (625, 300),

        ]

        for pos in start_positions:
            self._add_point_light(*pos)

        # Animation loop
        for _ in range(60):  # Adjust this for longer animations 
            self._move_point_lights(-2, 1)  # Move lights diagonally to simulate walking
            frame = self._draw_frame()
            cv2.imshow('Animation', frame)
            cv2.waitKey(100)  # Adjust this value to control animation speed
        
        cv2.destroyAllWindows()


# Create and run animation
animation = Animation()
animation.animate()
