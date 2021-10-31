

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy import optimize


class Optimization:

    def __init__(self, objective_array: list, ):
        self.__objective_array = objective_array

        self.__a_eq = None
        self.__b_eq = None

        self.__b_ub = None
        self.__a_ub = None

        self.__bounds = None

    def add_equality_condition(self, b_eq: list, a_eq: list) -> None:
        self.__a_eq = a_eq
        self.__b_eq = b_eq

    def add_inequality_condition(self, a_ub: list, b_ub: list) -> None:
        self.__b_ub = b_ub
        self.__a_ub = a_ub

    def add_bounds(self, bounds: tuple) -> None:
        self.__bounds = bounds

    def plot(self):

        ax = plt.axes(projection='3d')

        line_segment_blank = np.linspace(0, 10, 10)
        x, z = np.meshgrid(line_segment_blank, line_segment_blank)

        zeros = np.zeros(10)

        # TODO:
        constraint_1 = x * -3 + 27
        constraint_2 = x * -1 + 12
        constraint_3 = x * -1.5 + 15

        ax.plot_surface(
            x, constraint_1, z, color='gray', alpha=.3,
            linewidth=0, antialiased=False)
        ax.plot_surface(
            x, constraint_2, z, color='gray', alpha=.3,
            linewidth=0, antialiased=False)
        ax.plot_surface(
            x, constraint_3, z, color='gray', alpha=.3,
            linewidth=0, antialiased=False)

        x, y = np.meshgrid(line_segment_blank, line_segment_blank)
        objective = x * .4 + y * .5

        ax.plot_surface(
            x, y, objective, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)

        plt.show()

    def optimize(self):
        return optimize.linprog(
            c=self.__objective_array, bounds=self.__bounds,
            A_ub=self.__a_ub, b_ub=self.__b_ub, A_eq=self.__a_eq, b_eq=self.__b_eq)
