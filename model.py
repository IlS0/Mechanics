import numpy
import matplotlib.pyplot as plt
from math import sqrt

#определение констант
g = 9.80665
k = 380.653 #коэф. сжатия резинки
spoon_weight = 0.06
bullet_weight = 0.04504 #скорей всего задавать на инпуте
loaded_h = 0.14
shot_h = 0.2
delta_x = 0.05


def dymics():
    return sqrt((k*(delta_x**2)- 2 *(spoon_weight+bullet_weight)*g*(shot_h-loaded_h))/((2*spoon_weight+bullet_weight)))
    

def main():
    starting_speed = dymics()
    print(starting_speed)


if __name__ == "__main__":
    main()