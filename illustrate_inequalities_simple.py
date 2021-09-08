from scipy.spatial import HalfspaceIntersection, ConvexHull
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def gen_ineq_str(x1, x2, op, rhs):
    
    ineq_str = ""
    ineq_str += (str(x1) if x1>=0 else '-'+str(x1)) + '$x_1$'
    ineq_str += ('+'+str(x2) if x2>=0 else '-'+str(x2)) + '$x_2$'
    ineq_str += op + str(rhs)
    
    return ineq_str

def illustrate(restrictions, xlim, ylim):

    x_list = np.linspace(xlim[0], xlim[1])
    for (x1, x2, op, rhs) in restrictions:

        # Non-negative solutions
        if (x2 == 0):
            plt.plot([xlim[0], xlim[1]], [0, 0], color='black')
        elif (x1 == 0):
            plt.plot([0, 0], [ylim[0], ylim[1]], color='black' )

        
        else:
            plt.plot(x_list, rhs/x2 - x_list* x1/x2, label=gen_ineq_str(x1, x2, op, rhs))

    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.legend()
    plt.grid(True)
    plt.show()


restrictions = [
    [1, 0, '>=', 0],    # x₁ ≥ 0
    [0, 1, '>=', 0],    # x₂ ≥ 0
    [1, 3, '<=', 6],    # x1 + 3x2 <= 6
    [4, 3, '<=', 12],    # 4x1 + 3x2 ≤ 12
    [4, 1, '<=', 8],    # 4x1 + x2 <= 8
]
xlim = (-1,8)
ylim = (-1,10)

illustrate(restrictions, xlim, ylim)

