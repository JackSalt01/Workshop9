import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(x)
ax1.set_ylabel("y (m)")

ax2.plot(y)
ax2.set_ylabel("dy/dx (m/s)")
ax2.set_xlabel("t (s)")

plt.show()