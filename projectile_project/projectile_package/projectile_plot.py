import matplotlib.pyplot as plt

def plot_xy(x,y):

    fig, ax = plt.subplots(sharex=True)

    ax.plot(x, y)
    ax.set_ylabel("x")
    ax.set_ylabel("y")
    ax.set_title("2D Projectile")
    
plt.show()