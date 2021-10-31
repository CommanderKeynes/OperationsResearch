

import numpy as np


def simplex() -> None:

    c = [-3, -5]
    A_ub = [[1, 0], [0, 2], [3, 2]]
    b_ub = [4, 12, 18]

    c = c + [0] * len(b_ub)
    c = np.array(c)

    A_ub = np.array(A_ub)

    pass