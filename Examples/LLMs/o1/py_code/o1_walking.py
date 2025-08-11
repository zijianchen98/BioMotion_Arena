import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, pi

# Number of frames in one walking cycle
FRAMES_PER_CYCLE = 50
# Total frames (two walk cycles in this example)
TOTAL_FRAMES = FRAMES_PER_CYCLE * 2
# Amplitude of arm and leg swing (in radians)
ARM_SWING = pi / 6
LEG_SWING = pi / 4

# Define segment lengths
TORSO_LENGTH = 0.4
ARM_UPPER = 0.3
ARM_LOWER = 0.3
LEG_UPPER = 0.4
LEG_LOWER = 0.4

# Vertical base positions
HIP_HEIGHT = 0.8
SHOULDER_HEIGHT = HIP_HEIGHT + TORSO_LENGTH
HEAD_HEIGHT = SHOULDER_HEIGHT + 0.3

# Horizontal offsets
HIP_OFFSET = 0.1
SHOULDER_OFFSET = 0.2

def get_points(frame):
    """Return (x,y) coordinates for 15 point-lights representing a walking human."""
    # Time parameter for the walking cycle (0 to 2*pi)
    t = 2 * pi * (frame % FRAMES_PER_CYCLE) / FRAMES_PER_CYCLE

    # Angles for right arm/leg (and left out of phase by pi)
    rightArmAngle = ARM_SWING * sin(t)
    leftArmAngle = ARM_SWING * sin(t + pi)
    rightLegAngle = LEG_SWING * sin(t)
    leftLegAngle = LEG_SWING * sin(t + pi)

    # Define elbow/knee bending as smaller angles for a more lifelike motion
    rightElbowAngle = 0.5 * rightArmAngle
    leftElbowAngle = 0.5 * leftArmAngle
    rightKneeAngle = 0.5 * rightLegAngle
    leftKneeAngle = 0.5 * leftLegAngle

    points = []

    # 1) Head
    points.append((0.0, HEAD_HEIGHT))

    # 2) Neck
    neck = (0.0, SHOULDER_HEIGHT + 0.1 * (HEAD_HEIGHT - SHOULDER_HEIGHT))
    points.append(neck)

    # 3) Right Shoulder
    rShoulder = (SHOULDER_OFFSET, SHOULDER_HEIGHT)
    points.append(rShoulder)

    # 4) Right Elbow
    rElbowX = rShoulder[0] + ARM_UPPER * sin(rightArmAngle)
    rElbowY = rShoulder[1] - ARM_UPPER * cos(rightArmAngle)
    points.append((rElbowX, rElbowY))

    # 5) Right Wrist
    rWristX = rElbowX + ARM_LOWER * sin(rightArmAngle + rightElbowAngle)
    rWristY = rElbowY - ARM_LOWER * cos(rightArmAngle + rightElbowAngle)
    points.append((rWristX, rWristY))

    # 6) Left Shoulder
    lShoulder = (-SHOULDER_OFFSET, SHOULDER_HEIGHT)
    points.append(lShoulder)

    # 7) Left Elbow
    lElbowX = lShoulder[0] + ARM_UPPER * sin(leftArmAngle)
    lElbowY = lShoulder[1] - ARM_UPPER * cos(leftArmAngle)
    points.append((lElbowX, lElbowY))

    # 8) Left Wrist
    lWristX = lElbowX + ARM_LOWER * sin(leftArmAngle + leftElbowAngle)
    lWristY = lElbowY - ARM_LOWER * cos(leftArmAngle + leftElbowAngle)
    points.append((lWristX, lWristY))

    # 9) Mid-Hip (center)
    midHip = (0.0, HIP_HEIGHT)
    points.append(midHip)

    # 10) Right Hip
    rHip = (HIP_OFFSET, HIP_HEIGHT)
    points.append(rHip)

    # 11) Right Knee
    rKneeX = rHip[0] + LEG_UPPER * sin(rightLegAngle)
    rKneeY = rHip[1] - LEG_UPPER * cos(rightLegAngle)
    points.append((rKneeX, rKneeY))

    # 12) Right Ankle
    rAnkleX = rKneeX + LEG_LOWER * sin(rightLegAngle + rightKneeAngle)
    rAnkleY = rKneeY - LEG_LOWER * cos(rightLegAngle + rightKneeAngle)
    points.append((rAnkleX, rAnkleY))

    # 13) Left Hip
    lHip = (-HIP_OFFSET, HIP_HEIGHT)
    points.append(lHip)

    # 14) Left Knee
    lKneeX = lHip[0] + LEG_UPPER * sin(leftLegAngle)
    lKneeY = lHip[1] - LEG_UPPER * cos(leftLegAngle)
    points.append((lKneeX, lKneeY))

    # 15) Left Ankle
    lAnkleX = lKneeX + LEG_LOWER * sin(leftLegAngle + leftKneeAngle)
    lAnkleY = lKneeY - LEG_LOWER * cos(leftLegAngle + leftKneeAngle)
    points.append((lAnkleX, lAnkleY))

    return np.array(points)

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter with 15 points
initial_positions = get_points(0)
scatter = ax.scatter(initial_positions[:,0], initial_positions[:,1], 
                     c='white', s=20)

def update(frame):
    coords = get_points(frame)
    scatter.set_offsets(coords)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=50, blit=True)
plt.show()