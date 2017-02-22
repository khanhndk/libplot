# import numpy as np
# import matplotlib.pyplot as plt
#
# circle1 = plt.Circle((200, 200), 100, color='r', alpha=0.5)
#
# plt.axis([0,400,0,400])
# fig = plt.gcf()
# ax = fig.gca()
#
# ax.add_artist(circle1)
# plt.axes().set_aspect('equal')
# plt.show()

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-2.0, 2.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = Z1
N = x.shape[0]
for i in xrange(N):
    for j in xrange(N):
        Z[i,j]=-((x[i]-0)**2 + (y[j]-0)**2 - 1**2)
        Z[i,j]= (1+np.exp(-Z[i,j]))**-1




# Create a simple contour plot with labels using default colors.  The
# inline argument to clabel will control whether the labels are draw
# over the line segments of the contour, removing the lines beneath
# the label



plt.figure()
plt.axes().set_aspect('equal')
fig = plt.gcf()
ax = fig.gca()
circle1 = plt.Circle((0,0), 1, color='r', alpha=0.25)
ax.add_artist(circle1)
CS = plt.contour(X, Y, Z, 7,
                 linestyles=['dashed','dashed','dashed','dashed','solid','dashed','dashed'],
                 cmap=cm.PuRd,
                 linewidths=[2,2,2,2,2,2,],
                 )
plt.clabel(CS, inline=0.3, fontsize=10)
plt.title('Simplest default with labels')
plt.savefig('P:/a.png', dpi=600)
plt.show()