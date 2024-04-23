import numpy as np


def psi_2_V(psi):
    V=.188*psi+8.72     #slope of exel graph
    return V
def trig(angle,V):
    horizontal_v=np.cos(angle)*V
    vertical_v=np.sin(angle)*V
    return [horizontal_v,vertical_v]

def main():
    psi=int(input("psi\n"))
    angle=int(input("launch angle\n"))
    tan_V=psi_2_V(psi)
    horizontal,vertical=trig(angle,tan_V)

if __name__ == "__main__":
        main()
