# projectile motion project
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def psi_2_V(psi):
    V = .188 * psi + 8.72  # slope of exel graph
    return V


def trig(angle, V):
    angle = np.radians(angle)  # Convert angle to radians
    horizontal_v = np.cos(angle) * V
    vertical_v = np.sin(angle) * V
    return horizontal_v, vertical_v

def main():
    psi = int(input("psi\n"))
    angle = int(input("launch angle\n"))
    tan_V = psi_2_V(psi)
    horizontal, vertical = trig(angle, tan_V)
    t = time(vertical)
    r = calculate_range(t, horizontal)

    print("launch velocity", f"{tan_V}ft/s", "time", f"{t}sec", " range", f"{r}Yards","(",r/1.09361,"meters",")")
    coordinates(vertical, horizontal, t)


def time(vertical, g=-9.8):
    coeff = [g / 2, vertical]
    times = np.roots(coeff)
    return max(times)


def calculate_range(time, horizontal):
    range = time * horizontal*1.09361# convert to yards
    return range


def coordinates(vertical, horizontal, time, timestep=0.1):
    # x-coordinate - horizontal
    t = 0
    xs = []
    ys = []
    while t < time:
        x = horizontal * t
        y = vertical * t - 0.5 * 9.8 * (t ** 2)
        xs.append(x* 1.09361)
        ys.append(y* 1.09361)
        t += timestep
    print(xs,"\n", ys)
    plt.plot(xs,ys)
    plt.show()
    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        ax.plot(xs[i], ys[i],'ro')
        ax.set_xlim(0, 120)
        ax.set_ylim(0, 120)


    ani = animation.FuncAnimation(fig, animate, frames=len(xs) - 1, interval=30, repeat=False)
    plt.show()
"have to convert meters to feet"
if __name__ == "__main__":
    main()
