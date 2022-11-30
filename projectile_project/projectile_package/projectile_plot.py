import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(t, y)
ax1.set_ylabel("y (m)")

ax2.plot(t, vy)
ax2.set_ylabel("dy/dx (m/s)")
ax2.set_xlabel("t (s)")

plt.show()