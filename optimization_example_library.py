

from scipy.optimize.optimize import OptimizeResult
from Optimization import Optimization


def build_wyndor_glass_example() -> Optimization:

    wyndor_glass_optimization = Optimization(objective_array=[-3, -5])
    wyndor_glass_optimization.add_bounds(bounds=((0, None), (0, None), ))
    wyndor_glass_optimization.add_inequality_condition(
        a_ub=[[1, 0], [0, 2], [3, 2]],
        b_ub=[4, 12, 18])

    return wyndor_glass_optimization


def build_radiation_therapy_example() -> Optimization:

    """
    From page 45

    minimize .4 * b1 + .5 * b2
    constraint .3 * b1 + .1 * b2 <= 2.7
    constraint .5 * b1 + .5 * b2 == 6
    constraint .6 * b1 + .4 * b2 >= 6

    Slope intercept constraints/objective
    minimize b2 = 2 * Z - .8 * B1
    constraint b2 <= -3 * b1 + 27
    constraint b2 == -b1 + 12
    constraint b2 >= - 1.5 * b1 + 15

    :return:
    """

    radiation_therapy_optimization = Optimization(objective_array=[.4, .5])
    radiation_therapy_optimization.add_bounds(bounds=((0, None), (0, None), ))
    radiation_therapy_optimization.add_inequality_condition(
        a_ub=[[.3, .1], [-.6, -.4]],
        b_ub=[2.7, -6])
    radiation_therapy_optimization.add_equality_condition(b_eq=[6], a_eq=[[.5, .5]])

    return radiation_therapy_optimization


def build_regional_planning_example() -> Optimization:

    A_ub = [

        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],

        [3, 0, 0, 2, 0, 0, 1, 0, 0],
        [0, 3, 0, 0, 2, 0, 0, 1, 0],
        [0, 0, 3, 0, 0, 2, 0, 0, 1],

        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],

    ]

    b_ub = [
        400, 600, 300,
        600, 800, 375,
        600, 500, 325]

    A_eq = [
        [600, -400, 0, 600, -400, 0, 600, -400, 0],
        [0, 300, -600, 0, 300, -600, 0, 300, -600],
        [300, 0, -400, 300, 0, -400, 300, 0, -400]
    ]

    b_eq = [0, 0, 0]

    regional_planning_optimization = Optimization(
        objective_array=[-1000, -1000, -1000, -750, -750, -750, -250, -250, -250])

    regional_planning_optimization.add_bounds(bounds=((0, None), ) * 9)
    regional_planning_optimization.add_inequality_condition(
        a_ub=A_ub,
        b_ub=b_ub)
    regional_planning_optimization.add_equality_condition(
        b_eq=b_eq,
        a_eq=A_eq)

    return regional_planning_optimization


def build_air_pollution_example() -> Optimization:

    A_ub = [

        [-12, -9, -25, -20, -17, -13, ],
        [-35, -42, -18, -31, -56, -49, ],
        [-37, -53, -28, -24, -29, -20, ],

    ]

    b_ub = [-60, -150, -125, ]

    air_pollution_optimization = Optimization(
        objective_array=[8, 10, 7, 6, 11, 9, ])
    air_pollution_optimization.add_bounds(bounds=((0, 1), ) * 6)
    air_pollution_optimization.add_inequality_condition(
        a_ub=A_ub, b_ub=b_ub)

    return air_pollution_optimization


def build_reclaiming_waste_example() -> Optimization:

    c = [
        -5.5, -5.5, -5.5, -5.5,
        -4.5, -4.5, -4.5, -4.5,
        -3.5, -3.5, -3.5, -3.5,
    ]

    A_ub = [

        [.7, -.3, -.3, -.3,
         0, 0, 0, 0,
         0, 0, 0, 0],

        [.4, -.6, .4, .4,
         0, 0, 0, 0,
         0, 0, 0, 0],

        [-.5, -.5, .5, -.5,
         0, 0, 0, 0,
         0, 0, 0, 0],

        [0, 0, 0, 0,
         .5, -.5, -.5, -.5,
         0, 0, 0, 0],

        [0, 0, 0, 0,
         .1, -.9, .1, .1,
         0, 0, 0, 0],

        [0, 0, 0, 0,
         0, 0, 0, 0,
         .3, -.7, -.7, -.7],

        [1, 0, 0, 0,
         1, 0, 0, 0,
         1, 0, 0, 0, ],

        [0, 1, 0, 0,
         0, 1, 0, 0,
         0, 1, 0, 0, ],

        [0, 0, 1, 0,
         0, 0, 1, 0,
         0, 0, 1, 0, ],

        [0, 0, 0, 1,
         0, 0, 0, 1,
         0, 0, 0, 1, ],

        [-1, 0, 0, 0,
         -1, 0, 0, 0,
         -1, 0, 0, 0, ],

        [0, -1, 0, 0,
         0, -1, 0, 0,
         0, -1, 0, 0, ],

        [0, 0, -1, 0,
         0, 0, -1, 0,
         0, 0, -1, 0, ],

        [0, 0, 0, -1,
         0, 0, 0, -1,
         0, 0, 0, -1, ],
    ]

    b_ub = [0, 0, 0, 0, 0, 0, 3_000, 2_000, 4_000, 1_000, -1_500, -1_000, -2_000, -500, ]

    A_eq = [

        [-.2, -.2, -.2, .8,
         0, 0, 0, 0,
         0, 0, 0, 0],

        [0, 0, 0, 0,
         -.1, -.1, -.1, .9,
         0, 0, 0, 0],

        [3, 6, 4, 5,
         3, 6, 4, 5,
         3, 6, 4, 5, ]

    ]

    b_eq = [0, 0, 30_000, ]

    waste_reclamation_optimization = Optimization(
        objective_array=c)
    waste_reclamation_optimization.add_bounds(bounds=((0, None), ) * 12)
    waste_reclamation_optimization.add_inequality_condition(
        a_ub=A_ub, b_ub=b_ub)
    waste_reclamation_optimization.add_equality_condition(b_eq=b_eq, a_eq=A_eq)

    return waste_reclamation_optimization


def build_personnel_scheduling_example() -> Optimization:

    A_ub = [
        [-1, 0, 0, 0, 0],
        [-1, -1, 0, 0, 0],
        [-1, -1, 0, 0, 0],
        [-1, -1, -1, 0, 0],
        [0, -1, -1, 0, 0],
        [0, 0, -1, -1, 0],
        [0, 0, -1, -1, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1],
    ]

    b_ub = [-48, -79, -65, -87, -64, -73, -82, -43, -52, -15]

    personnel_scheduling = Optimization(
        objective_array=[170, 160, 175, 180, 195, ])
    personnel_scheduling.add_bounds(bounds=((0, None), ) * 5)
    personnel_scheduling.add_inequality_condition(
        a_ub=A_ub, b_ub=b_ub)

    return personnel_scheduling


def build_distribution_network_example() -> Optimization:

    bounds = (
        (0, 10), (0, None), (0, None), (0, None), (0, 80), (0, None), (0, None))

    A_eq = [
        [1, 1, 1, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0],
        [0, -1, 0, -1, 1, 0, 0],
        [0, 0, -1, 0, 0, 1, -1],
        [0, 0, 0, 0, -1, -1, 1],
    ]

    b_eq = [50, 40, 0, -30, -60]

    distribution_network_optimization = Optimization(
        objective_array=[200, 400, 900, 300, 100, 300, 200])
    distribution_network_optimization.add_bounds(bounds=bounds)
    distribution_network_optimization.add_equality_condition(
        b_eq=b_eq, a_eq=A_eq)

    return distribution_network_optimization


if __name__ == '__main__':
    solution_result = corner_point_solutions()
