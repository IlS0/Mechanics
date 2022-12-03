import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,cos,sin,pi
import argparse

#учесть ситуацию со слишком большим весом 
#интерфейс?

#определение констант
g = 9.80665
k = 380.653 #коэф. сжатия резинки
spoon_weight = 0.06
bullet_weight = 0.04504 # дефолт - 0. задавать на инпуте
loaded_h = 0.14
shot_h = 0.2
delta_x = 0.05
angle = 30*pi/180 #перевод в радианы


def consoleParser():
	parser = argparse.ArgumentParser(description='Args:')
	parser.add_argument("weight", type=float, help="Weight of a bullet in kg.")
	return parser.parse_args()


def dymics():
    return sqrt((k*(delta_x**2)- 2 *(spoon_weight+bullet_weight)*g*(shot_h-loaded_h))/((2*spoon_weight+bullet_weight)))


def kinematics(starting_speed):
    time_interval = np.arange(0,1,step=0.05)
    print(time_interval)

    def spaceX(t):
        return starting_speed * cos(angle) * t

    def spaceY(t):
        return shot_h+starting_speed*sin(angle)*t - ((g*(t**2))/2)

    xs = np.array(list(map(spaceX,time_interval)))
    ys = np.array(list(map(spaceY,time_interval)))
    plt.plot(xs,ys)
    plt.show()


def main():
    global bullet_weight
    args = consoleParser()
    #bullet_weight = args.weight
    starting_speed = dymics()
    kinematics(starting_speed)
    print(starting_speed)


if __name__ == "__main__":
    main()