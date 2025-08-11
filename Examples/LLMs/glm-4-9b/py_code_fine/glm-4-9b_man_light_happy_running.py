
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

class HappyManMotion:
    def __init__(self, num_lights=15):
        self.num_lights = num_lights
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 5)
        self.ax.set_facecolor('black')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Create initial point lights
        self point lights = [self.ax.plot([], [], 'o', color='white', markersize=6)[0] for _ in range(num_lights)]
        
        # Initialize happyman figure
        self.happyman = self.draw_happyman()
        
    def draw_happyman(self):
        # Simple representation of a happy man (circle head with smile, rectangle body)
        head = patches.Circle((0.5, 4), 0.4, color='white')
        body = patches.Rectangle((0.4, 3.6), 0.2, 1.5, color='white')
        left_arm = patches.Rectangle((0.4, 3.8), 1.2, 0.1, color='white')
        right_arm = patches.Rectangle((0.4, 3.8), -1.2, 0.1, color='white')
        left_leg = patches.Rectangle((0.4, 2.9), 0.1, 1.7, color='white')
        right_leg = patches.Rectangle((0.5, 2.9), 0.1, 1.7, color='white')
        
        self.ax.add_patch(head)
        self.ax.add_patch(body)
        self.ax.add_patch(left_arm)
        self.ax.add_patch(right_arm)
        self.ax.add_patch(left_leg)
        self.ax.add_patch(right_leg)
        
        # Add smile
        smile = patches.Arc((0.5, 4.1), 0.3, 0.1, theta1=-40, theta2=40, color='black')
        self.ax.add_patch(smile)
        
        return [head, body, left_arm, right_arm, left_leg, right_leg]
    
    def init_animation(self):
        for point in self.point_lights:
            point.set_data([], [])
        return self.point_lights
    
    def update_animation(self, frame):
        # Remove previous happyman
        for patch in self.happyman:
            patch.remove()
        self.happyman = self.draw_happyman()
        
        # Running motion parameters
        t = frame / 50  # time in seconds
        x0, y0 = 0.5, 3.0
        period = 2.0  # period of running cycle in seconds
        
        # Define positions for 15 point lights based on running motion
        for i, point in enumerate(self.point_lights):
            # Vary the motion based on body part and individual variation
            freq_offset = 0.5 + 0.2 * np.sin(i / 5)
            
            # Different body parts move with different phases
            if i < 5:  # upper body (5 lights)
                x = x0 + 0.8 * np.sin(2 * np.pi * freq_offset * t)
                y = y0 + 0.3 * np.cos(2 * np.pi * freq_offset * t)
            else:  # lower body (10 lights)
                x = x0 + 1.5 * np.sin(2 * np.pi * freq_offset * t)
                y = y0 - 1.0 * np.cos(2 * np.pi * freq_offset * t)
                
            point.set_data(x, y)
        
        return self.point_lights

    def animate(self):
        anim = FuncAnimation(self.fig, self.update_animation, frames=500,
                             init_func=self.init_animation, blit=False, interval=20)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    happy_man = HappyManMotion()
    happy_man.animate()
