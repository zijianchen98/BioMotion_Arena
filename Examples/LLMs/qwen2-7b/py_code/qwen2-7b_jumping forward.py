
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_point_light(action='jumping forward', num_points=15, duration=50):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
    ax.set_xlim(-20, 20), ax.set_ylim(-20, 20)
    
    # Man class to handle the subject's's motion
    class Man:
        def __init__(self, x=0, y=0, radius=2):
            self.x = x
            self.y = y
            self.radius = radius
            self.action = 'jumping forward'
            self.direction = 90 # Initial direction in degrees
            
        def move(self):
            if self.action == 'jumping forward':
                # Calculate new position based on direction and time elapsed
                self.x += np.cos(np.deg2rad(self.direction)) * speed * dt
                self.y += np.sin(np.deg2rad(self.direction)) * speed * dt
                # Ensure the man stays within the plot boundaries
                self.x = max(-20, min(20, self.x)
                self.y = max(-20, min(20, self.y)
                
        def draw(self):
            circle = plt.Circle((self.x, self.y), self.radius, color='white')
            ax.add_patch(circle)
            
    man = Man()
    speed = 0.5 # Speed of the man
    dt = 0.01 # Time step for animation
    
    # Initialize points list
    points = []
    
    # Create initial points for the man
    for _ in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = 10 * np.cos(angle)
        y = 10 * np.sin(angle)
        points.append([x, y])
        
    # Create animation
    def update(frame):
        man.move()
        for i, point in enumerate(points):
            x, y = point
            points[i] = [man.x, man.y]
            circle = plt.Circle((x, y), 2, color='white')
            ax.add_patch(circle)
            
    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, duration*dt, dt),
                                   interval=30, blit=False)
    
    plt.show()

animate_point_light()
