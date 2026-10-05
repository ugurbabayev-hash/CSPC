import numpy as np
import matplotlib.pyplot as plt

traj_data = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1)
t = traj_data[:, 0]
x = traj_data[:, 1]
y = traj_data[:, 2]

v_x = np.gradient(x, t)
v_y = np.gradient(y, t)
speed = np.sqrt(v_x**2 + v_y**2)
fig, (ax_path, ax_speed) = plt.subplots(1, 2, figsize=(12, 5))
ax_path.plot(x, y, label='Trajectory', color='purple')
ax_path.set_xlabel('X position (m)')
ax_path.set_ylabel('Y position (m)')
ax_path.set_title('2D Tracked Trajectory')
ax_path.grid(True)
ax_path.legend()

ax_speed.plot(t, speed, label='Speed', color='teal')
ax_speed.set_xlabel('Time (s)')
ax_speed.set_ylabel('Speed (m/s)')
ax_speed.set_title('Speed over Time')
ax_speed.grid(True)
ax_speed.legend()

plt.tight_layout()
plt.savefig('bonus_motion.png')
plt.show()