import numpy as np

def psi_2_V(psi):
    V=.188*psi+8.72     #slope of exel graph
    return V

def trig(angle,V):
    angle = np.radians(int(angle))
    horizontal_v=round(np.cos(angle))*V
    vertical_v=np.sin(angle)*V
    return [horizontal_v,vertical_v]

def main():
    psi=int(input("psi\n"))
    angle=int(input("launch angle\n"))
    tan_V=psi_2_V(psi)
    horizontal,vertical=trig(angle,tan_V)
    t = time(vertical)
    r = range(t, horizontal)

    print("launch velocity", f"{tan_V}ft/s", "time", f"{t}sec", " range", f"{r}ft")
    

def time(vertical, g=-10):
    coeff = [g/2, vertical]
    times = np.roots(coeff)
    return max(times)

def range(time, horizontal):
    range = time*horizontal
    return range
     

if __name__ == "__main__":
        main()
