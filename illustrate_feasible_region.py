from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection, ConvexHull
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np



def find_feasible_region(halfspaces, feasible_point, xlim, ylim, direction):
    colors = ["blue", "orange", "red", "yellow"]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, aspect='equal')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    x = np.linspace(xlim[0], xlim[1], 100)

    hs = HalfspaceIntersection(halfspaces, feasible_point)

    for (h, dir) in zip(halfspaces, direction):

        if (h[1] == 0):
            ax.axvline(-h[2]/h[0], color=colors[0]) 
            xi = np.linspace(xlim[dir], -h[2]/h[0], 100)
            ax.fill_between(xi, ylim[0], ylim[1], color=colors[0], alpha = 0.9)

        else:
            ax.plot(x, (-h[2]-h[0]*x)/h[1], color=colors[0])

            ax.fill_between(x, (-h[2]-h[0]*x)/h[1], ylim[dir], color=None, alpha = 0.5)
        
        colors = colors[1:]
    
    x,y = zip(*hs.intersections)

    ax.plot(x, y, 'o', color='red')
    plt.show()




halfspaces = np.array([[-1, 0., 0.],
                       [0., -1., 0.],
                       [1., 3., -6.],
                       [4., 3., -12.]])


feasible_point = np.array([0.5, 0.5])

xlim, ylim = (-1, 6), (-1, 10)

# 0 means "less than", -1 means "larger than"
direction = [-1, -1, 0, 0]

find_feasible_region(halfspaces, feasible_point, xlim, ylim, direction)


