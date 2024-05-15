# projectile motion project
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def psi_2_V(psi):
    "converts psi to tangential velocity "
    V = .188 * psi + 8.72  # slope of exel graph
    return V


def trig(angle, V):
    "gets horizontal and vertical velocity from tangential"
    angle = np.radians(angle)               # Convert angle to radians
    horizontal_v = np.cos(angle) * V        # calculate horizontal velocity
    vertical_v = np.sin(angle) * V          # calculates vertical velocity
    return horizontal_v, vertical_v         # retrun both

def time(vertical, g=-9.8):
    'gets time'
    coeff = [g / 2, vertical]
    times = np.roots(coeff)
    return max(times)


def calculate_range(time, horizontal):
    'gets range'
    range = time * horizontal*1.09361 # calculate range and covert to yards
    return range


def coordinates(vertical, horizontal, time, timestep=0.1):
    'plots animation'
    # x-coordinate - horizontal
    t = 0
    xs = []                     #list of x vaules
    ys = []                     #list of y vaules
    while t < time:             #loop to get enough points
        x = horizontal * t      #calculate x vaule
        y = vertical * t - 0.5 * 9.8 * (t ** 2)#calculate y vaule
        xs.append(x* 1.09361)   #add x vaule to xs and convert to yards
        ys.append(y* 1.09361)   #add y vaule to ys and convert to yards
        t += timestep           #add to the looper
    #print(xs,"\n", ys)
    plt.plot(xs,ys)     #plot x and y points
    plt.show()                #show graph
    fig, ax = plt.subplots()

    def animate(i):
        'animates x,y vaules'
        ax.clear()                      #clear the point after each frame
        ax.plot(xs[i], ys[i],'ro')      #plot
        ax.set_xlim(0, 120)             #limits
        ax.set_ylim(0, 120)

    ani = animation.FuncAnimation(fig, animate, frames=len(xs) - 1, interval=30, repeat=False)
    plt.show()

def fieldGoal(range, vel):
    'Part 2: Calculates necessary angle and PSI given launch velocity and range to score over a field goal'
    
    psi = (vel-8.72)/0.188 # converts given velocity to psi using excel equation
    d = .8 # desired clearing height above field goal
    h = 0 + d # max projectile height in meters
    r = range/1.09361 # convert yards to meters
    angle = (math.atan(math.sqrt((h*9.8*2)/vel))) # calculate angle
    a = angle*(180/math.pi) # convert from radians to degrees

    return psi, a

def main():
    mode = input("Normal launch or field goal? N/F\n")
    if mode == "N":
        psi = int(input("psi\n"))
        angle = int(input("launch angle\n"))
        tan_V = psi_2_V(psi)
        horizontal, vertical = trig(angle, tan_V)
        t = time(vertical)
        r = calculate_range(t, horizontal)

        print("launch velocity", f"{tan_V}ft/s", "time", f"{t}sec", " range", f"{r} Yards","(",r/1.09361,"meters",")")
        coordinates(vertical, horizontal, t)
    elif mode == "F":
        range = int(input("range\n"))
        vel = int(input("Velocity\n"))
        psi = fieldGoal(range, vel)[0]
        angle = fieldGoal(range, vel)[1]

        print(f"Angle: {angle}, PSI: {psi}")

if __name__ == "__main__":
    main()
