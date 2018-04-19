# -*-coding:utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt


# 定义一个欧拉算法的类，从而实现不同步长的引用.


class Euler:
    # y_list = []  # 定义一个空列表来实现y值的存储

    def __init__(self, h,  y0):  # 初始化Euler类的方法
        self.h = h
        self.y0 = y0
        self.y = y0
        self.n = 1 / self.h
        self.x = 0

    def euler(self):  # 定义Euler算法的过程
        # x = 0
        #  y = self.y0
        # n = 1 / self.h
        for i in range(int(self.n + 1)):
            y_dere = 1 + math.log(self.x + 1)
            self.y += self.h * y_dere
            self.y_list = Euler_y_list.append("%.10f" % self.y)
            self.x += self.h
        # print(Euler.y_list,)
        return np.linspace(0, 1, self.n + 1, dtype=float), Euler_y_list  # 为了引用结果列表，从而返回两个列表


# 定义一个实现龙格库塔方法
class RungeKutta:

    def __init__(self, h, y0=1):
        self.h = h
        self.y0 = y0

    def make_ks(self, x_k, y_k):
        def y_ders(x_k):
            y_der = 1 + math.log(x_k + 1)
            return y_der

        # 计算K1,K2,K3,K4
        k1 = y_ders(x_k)
        k2 = y_ders(x_k + self.h / 2)
        k3 = y_ders(x_k + (self.h / 2))
        k4 = y_ders(x_k + self.h)
        y_k = y_k + self.h / 6 * (k1 + (2 - math.sqrt(2)) * k2 + (2 + math.sqrt(2)) * k3 + k4)
        return x_k, y_k

    def make(self):
        n = int(1 / self.h)
        y_k = self.y0
        x_k = 0
        for i in range(n):  # 用循环遍历来实现y值的计算
            x_k, y_k = self.make_ks(x_k, y_k)
            x_k += self.h
            RungeKutta_y_list.append(y_k)

        return np.linspace(0, 1, n+1, endpoint=True,dtype=float), RungeKutta_y_list


class Plots:
    def __init__(self, x, y, title):
        self.x = list(x)
        self.y = list(y)
        self.title = title

    def plots(self):
        plt.figure(figsize=(8, 4))
        plt.scatter(self.x, self.y, label="y'=1+ln(x+1),\ny0=1\n(0<x<=1) ", color="red", linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(self.title)
      #  plt.ylim(min(self.y), max(self.y))
        plt.ylim()
        plt.legend()
        plt.show()


if __name__ == "__main__":
     while True:
        name = input("本程序提供Euler算法和Rungekutta算法\n选择算法时输入exit退出\n请输入需要的算法名：")
        try:
             a = float(input("请输入所需要的h值："))
             if  a =="exit" or a=="Exit":
                 break
        except ValueError as ve:
            print(ve)
        if name == "Euler":
            Euler_y_list =[]
            l1 = Euler(h=a, y0=1)
            l1x, l1y = l1.euler()
            with open("Euler.txt","a+") as f:
                f.write("h=%s\n" % l1.h)
                f.write("x值--------------y值\n")
                for i in range(len(l1x)):
                     print("x是：%.5f  y是：%.10f" % (float(l1x[i]),float(l1y[i])))
                     a,b = str(l1x[i]),str(l1y[i])
                     f.write(a+" "*6+b+"\n")
            l1p = Plots(l1x, l1y, name)
            l1p.plots()
            print("请储存好你的x值，和y值")
            del l1, l1p, l1x, l1y
            Euler.y_list = []
        elif name == "Rungekutta":
            RungeKutta_y_list = [0]
            l2 = RungeKutta(h=a)
            l2x, l2y = l2.make()
            with open("Rungekutta.txt", "a+") as f:
                f.write("h=%s\n" % l2.h)
                f.write("x值--------------y值\n")
                for i in range(len(l2x)):
                     print("x是：%.5f  y是：%.10f" % (l2x[i], l2y[i]))
                     a, b = str(l2x[i]), str(l2y[i])
                     f.write(a + " " * 6 + b + "\n")
            l2p = Plots(l2x, l2y, name)
            l2p.plots()
            print("请储存好你的x值，和y值")
            del l2, l2p
        elif name =="exit":
            break
        else:
            print("请输入正确的算法名!!!!")

