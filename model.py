import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi

# определение констант
g = 9.80665
k = 475.32  # коэф. сжатия резинки
spoon_weight = 0.06
loaded_h = 0.14
shot_h = 0.2
delta_x = 0.05
angle = pi / 3  # в радианах

# изменяемые величины
starting_speed = 0
bullet_weight = 0


def dynamics():
    return sqrt((k * (delta_x ** 2) - 2 * (spoon_weight + bullet_weight) * g * (shot_h - loaded_h)) /
                (2 * spoon_weight + bullet_weight))


def kinematics():
    time_interval = np.arange(0, 1, step=0.001)

    def spaceX(t):
        return starting_speed * cos(angle) * t

    def spaceY(t):
        return shot_h + starting_speed * sin(angle) * t - 0.5 * g * (t ** 2)

    ys = list(map(spaceY, time_interval))
    ys = [n for n in ys if n > 0]
    xs = list(map(spaceX, time_interval))
    xs = xs[:len(ys)]
    plt.plot(xs, ys)
    plt.title("График траектории полёта снаряда")
    plt.xlabel('Расстояние, x (м)')
    plt.ylabel('Расстояние, y (м)')
    plt.show()


if __name__ == "__main__":
    from tkinter import *
    from tkinter import messagebox


    def isValidWeight():
        if bullet_weight > 0.94:
            messagebox.showinfo("Ошибка", "Слишком большое значение массы!")
            return False
        if bullet_weight <= 0:
            messagebox.showinfo("Ошибка", "Отрицательное или нулевое значение массы!")
            return False
        return True


    def updateData():
        if txt_inp.get() == "":
            messagebox.showinfo("Пустое поле", "Введите значение массы!")
            return False
        global bullet_weight, starting_speed
        try:
            bullet_weight = float(txt_inp.get())
        except ValueError:
            bullet_weight = 0
            messagebox.showinfo("Ошибка", "Некорректное значение массы!")
            return False
        if not isValidWeight():
            return False
        starting_speed = dynamics()
        return True


    def dyn_clicked():
        if updateData():
            lbl_speed.configure(
                text="Начальная скорость при заданных\nпараметрах массы равна: {:.3f} м/с".format(starting_speed),
                state="active")


    def kin_clicked():
        if updateData():
            kinematics()


    def close():
        plt.ion()
        plt.close("all")
        window.destroy()


    plt.grid()
    window = Tk()
    window.title("Mechanical system model")
    window.geometry("560x170")

    lbl = Label(window, text="Введите значение массы груза в килограммах: ", font=("Arial Bold", 15))
    lbl.grid(column=0, row=0)
    lbl_speed = Label(window, font=("Arial Bold", 15), state="disabled")
    lbl_speed.place(x=200, y=30)

    txt_inp = Entry(window, width=10, font=("Arial Bold", 15))
    txt_inp.grid(column=1, row=0)
    txt_inp.focus()

    btn_dyn = Button(window, text="Динамический\nрасчёт", font=("Arial Bold", 15), command=dyn_clicked)
    btn_dyn.place(x=5, y=30)
    btn_kin = Button(window, text="Кинематичесий\nрасчёт", font=("Arial Bold", 15), command=kin_clicked)
    btn_kin.place(x=5, y=100)

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
