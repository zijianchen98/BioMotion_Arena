
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Generate the skeleton points of the happyman
# Points represent coordinates (x, y) in a normalized space
def create_frame(t):
    # Time-dependent values for running motion animation
    speed = 2 * np.pi / 30
    angle = t * speed
    
    # Base positions for body parts (simulating running animation)
    head = (0, 0.8 + 0.05 * np.sin(angle))
    torso = (0, 0.6)

    # Left arm and right arm
    left_arm = (-0.3 + 0.1 * np.sin(angle), 0.7)
    right_arm = (0.3 - 0.1 * np.sin(angle), 0.7)

    # Left leg and right leg
    left_leg = (-0.2 + 0.1 * np.sin(angle + np.pi), 0.4)
    right_leg = (0.2 - 0.1 * np.sin(angle + np.pi), 0.4)

    # Knees moving dynamically
    left_knee = (-0.1 + 0.15 * np.sin(angle), 0.25)
    right_knee = (0.1 - 0.15 * np.sin(angle), 0.25)

    # Feet dynamically moving (to simulate running effect)
    left_foot = (-0.2 + 0.2 * np.sin(angle), 0.1)
    right_foot = (0.2 - 0.2 * np.sin(angle), 0.1)

    # Shoulders moving slightly for biomechanical plausibility
    left_shoulder = (-0.15 + 0.05 * np.sin(angle), 0.65)
    right_shoulder = (0.15 - 0.05 * np.sin(angle), 0.65)

    # Elbows moving dynamically
    left_elbow = (-0.2 + 0.1 * np.sin(angle + np.pi / 2), 0.6)
    right_elbow = (0.2 - 0.1 * np.sin(angle + np.pi / 2), 0.6)

    # Combine all points in order
    return np.array([
        head, torso, left_arm, right_arm, left_shoulder, right_shoulder,
        left_leg, right_leg, left_knee, right_knee, left_foot, right_foot,
        left_elbow, right_elbow
    ])

# Animation function
def animate(t):
    points = create_frame(t)
    scat.set_offsets(points)
    return (scat,)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1)
ax.set_facecolor("black")
ax.axis("off")

# Create scatter plot for 15 white points
scat = ax.scatter([], [], s=100, c="white")

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=50, blit=True)

# Show animation
plt.show()
