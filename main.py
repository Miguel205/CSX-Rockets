# projectile motion project
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def psi_2_V(psi):
    V = .188 * psi + 8.72                    # slope of exel graph
    return V


def trig(angle, V):
    angle = np.radians(int(angle))            #converts angle to radians
    horizontal_v = round(np.cos(angle)) * V   #horzontal component
    vertical_v = np.sin(angle) * V            #vertical component
    return [horizontal_v, vertical_v]


def time(vertical, g=-10):                    
    coeff = [g / 2, vertical]                  #
    times = np.roots(coeff)                    #
    return max(times)


def range(time, horizontal):
    range = time * horizontal    
    return range


def coordinates(vertical, horizontal, time, timestep=0.05):
    # x-coordinate - horizontal
    t = 0
    xs = []            #array of x vaules
    ys = []            #array of y vaules
    while t < time:
        x = horizontal * t                    
        y = vertical * t - 5 * (t ** 2)
        xs.append(x)
        ys.append(y)
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

    ani = animation.FuncAnimation(fig, animate, frames=len(xs) - 1, interval=40)
    plt.show()




def main():
    psi = int(input("psi\n"))
    angle = int(input("launch angle\n"))
    tan_V = psi_2_V(psi)
    horizontal, vertical = trig(angle, tan_V)
    t = time(vertical)
    r = range(t, horizontal)

    print("launch velocity", f"{tan_V}ft/s", "time", f"{t}sec", " range", f"{r}ft")
    coordinates(vertical, horizontal, t)


if __name__ == "__main__":
    main()
