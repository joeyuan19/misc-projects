import matplotlib as mpl
from matplotlib import pyplot
from matplotlib import animation as ani
import numpy as np
import time
from scipy.ndimage import convolve

fig = pyplot.figure()
ax = fig.add_subplot(111)


def life(grid):
    """     The idea here is to use a convolution
    to work out whether or not a cell is alive or dead
    in the next evolution and then output the new
    populated grid     """
    weights = np.array([[1,1,1],[1,0,1],[1,1,1]]);
    A = convolve(grid,weights);
    n = grid.shape[0];
    m = grid.shape[1];
    grid1 = np.zeros((n,m),dtype=np.int);
    for j in range(n):
        for k in range(m):
            if grid[j,k] in [1,2]:
                if A[j,k] in [2,3]:
                    grid1[j,k] = 1;
            else:
                if A[j,k] in [3,10]:
                    grid1[j,k] = 1;
    return grid1

n,m = 100,100;

# Make grid of random 0's and 1's
grid0 = np.random.randint(0,2,(n,m));

def update(frame_number):
    global ax
    global grid0
    ax.cla()
    grid = life(grid0)
    ax.imshow(grid)
    grid0 = grid

# Make map characteristics
"""cmap = mpl.colors.ListedColormap(['black','red'])
bounds = [-0.5,0.5,1.5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# Make initial image
img = pyplot.imshow(grid, interpolation='nearest', cmap = cmap, norm = norm)
f = pyplot.figure()
f.show()

print grid
print life(grid)"""

a = ani.FuncAnimation(fig,update,frames=100,interval=300)

pyplot.show()

# grid1 = life(grid0)

'''def life2(grid):
    """     The idea here is to use a convolution
    to work out whether or not a cell is alive or dead
    in the next evolution and then output the new
    populated grid     """
    weights = np.array([[1,1,1],[1,0,1],[1,1,1]]);
    A = convolve(grid,weights)
    return A

print grid0
print life2(grid0)
print life(grid0)'''



