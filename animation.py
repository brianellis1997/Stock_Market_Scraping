import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
# from scraper import companies
import pandas as pd

# Animation setup
style.use('fivethirtyeight')
fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2, figsize=(10, 8))
axes = [ax1, ax2, ax3, ax4]

def animate(i):
    df = pd.read_csv('real time stock data.csv')
    for j, ax in enumerate(axes):
        ys = df.iloc[:, j + 1].values  # Adjusting column indexing
        xs = list(range(1, len(ys) + 1))
        ax.clear()
        ax.plot(xs, ys)
        ax.set_title('h', fontsize=12)

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
plt.show()