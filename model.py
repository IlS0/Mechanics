import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi
import argparse

# учесть ситуацию со слишком большим весом
# интерфейс?

# определение констант
g = 9.80665
k = 380.653  # коэф. сжатия резинки
spoon_weight = 0.06
bullet_weight = 0.04504  # дефолт - 0. задавать на инпуте
loaded_h = 0.14
shot_h = 0.2
delta_x = 0.05
angle = 30 * pi / 180  # перевод в радианы


def consoleParser():
    parser = argparse.ArgumentParser(description='Args:')
    parser.add_argument("-weight", type=float, help="Weight of a bullet in kg.", default=0.04504)
    return parser.parse_args()


def dynamics():
    return sqrt((k * (delta_x ** 2) - 2 * (spoon_weight + bullet_weight) * g * (shot_h - loaded_h)) /
                (2 * spoon_weight + bullet_weight))


def kinematics(starting_speed):
<<<<<<< HEAD
    time_interval = np.arange(0,1,step=0.001)
=======
    time_interval = np.arange(0, 1, step=0.001)
    print(time_interval)
>>>>>>> 618e26a0d7c966c558b0d052b5edcb62db3ab715

    def spaceX(t):
        return starting_speed * cos(angle) * t

    def spaceY(t):
<<<<<<< HEAD
        return shot_h+starting_speed*sin(angle)*t - 0.5*g*(t**2)

    ys = list(map(spaceY,time_interval))
    ys = [n for n in ys if n>0]
    xs = list(map(spaceX,time_interval))
    xs = xs[:len(ys)]
    plt.plot(xs,ys)
=======
        return shot_h + starting_speed * sin(angle) * t - ((g * (t ** 2)) / 2)

    y = list(map(spaceY, time_interval))
    ys = [n for n in y if n >= 0]
    x = list(map(spaceX, time_interval))
    xs = x[:len(ys)]
    plt.plot(xs, ys)
>>>>>>> 618e26a0d7c966c558b0d052b5edcb62db3ab715
    plt.show()


if __name__ == "__main__":
    args = consoleParser()
    bullet_weight = args.weight
    starting_speed = dynamics()
    kinematics(starting_speed)
    print(starting_speed)
