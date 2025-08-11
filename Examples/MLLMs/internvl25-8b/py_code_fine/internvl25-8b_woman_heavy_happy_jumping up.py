
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
background_color = 'black'
light_color = 'white'
interval = 30  # ms

# Initial positions of the lights
positions = np.array([[250, 300], [340, 350], [460, 330], [600, 310], [700, 330], [840, 300], [960, 340],
                     [1040, 390], [1000, 450], [880, 480], [730, 500], [630, 500], [530, 470], [430, 510], [390, 550]])

# Function to update the animation
def update(i):
    fig, ax = plt.subplots()
    ax.set_facecolor(background_color)
    
    # Update positions for the animation
    positions[:, 1] = np.sin(0.5 * np.pi * np.linspace(0, (i * interval) / 1000, 30))
    
    # Display static lights
    for pos in positions[:5]:
        circle = plt.Circle(pos, 5, color=light_color)
        ax.add_artist(circle)
    
    # Show moving lights
    for pos in positions[5:]:
        circle = plt.Circle(pos, 5, color=light_color)
        circle.set_edgecolor('black')
        ax.add_artist(circle)
    
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.xlim(200, 1000)
    plt.ylim(300, 550)
    return (fig,)

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update, frames=60, interval=interval)

# Show the animation
plt.show()
