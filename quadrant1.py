import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Ellipse, Circle
from matplotlib.transforms import ScaledTranslation
from matplotlib import rc, patches
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch

def circle(xy, radius, fig, ax, kwargs=None):
    """Create circle on figure with axes of different sizes.

    Plots a circle on the current axes using `plt.Circle`, taking into account
    the figure size and the axes units.

    It is done by plotting in the figure coordinate system, taking the aspect
    ratio into account. In this way, the data dimensions do not matter.
    However, if you adjust `xlim` or `ylim` after plotting `circle`, it will
    screw them up; set `plt.axis` before calling `circle`.

    Parameters
    ----------
    xy, radius, kwars :
        As required for `plt.Circle`.

    """

    # Get current figure and axis

    # Calculate figure dimension ratio width/height
    pr = fig.get_figwidth()/fig.get_figheight()

    # Get the transScale (important if one of the axis is in log-scale)
    tscale = ax.transScale + (ax.transLimits + ax.transAxes)
    ctscale = tscale.transform_point(xy)
    cfig = fig.transFigure.inverted().transform(ctscale)

    # Create circle
    if kwargs == None:
        circ = patches.Ellipse(cfig, radius, radius*pr,
                transform=fig.transFigure)
    else:
        circ = patches.Ellipse(cfig, radius, radius*pr,
                transform=fig.transFigure, **kwargs)

    # Draw circle
    ax.add_artist(circ)


class AnyObject(object):
    def __init__(self, color=None, marker=None):
        self.color = color
        self.marker = marker

class MarkerObject(object):
    def __init__(self, marker='s'):
        self.marker = marker

class AnyObjectHandler(object):
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        if orig_handle.color != None:
            patch = mpatches.Rectangle([x0, y0], width, height, facecolor=orig_handle.color,
                                       edgecolor=orig_handle.color,
                                       transform=handlebox.get_transform())
        elif orig_handle.marker == 's':
            patch = mpatches.Rectangle([x0+width/2-height/2, y0], height, height, facecolor='white',
                                       edgecolor='black',
                                       transform=handlebox.get_transform())
        elif orig_handle.marker == 'o':
            patch = mpatches.Circle([x0+width/2, y0+height/2], height/2, facecolor='white',
                           edgecolor='black',
                           transform=handlebox.get_transform())
        elif orig_handle.marker == '^':
            patch = mpatches.Polygon([[x0+width/2-height/2,y0],
                                      [x0+width/2, y0+height],[x0+width/2+height/2,y0]], facecolor='white',
                           edgecolor='black',
                           transform=handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch

class MarkerObjectHandler(object):
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle([x0, y0], width, height, facecolor=orig_handle.color,
                                   edgecolor=orig_handle.color,
                                   transform=handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch

class HandlerEllipse(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse(xy=center, width=width + xdescent,
                             height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]

fig = plt.figure()
ax = fig.add_subplot(111)

data = pd.read_csv('P:/exp/mkl-np/online.csv')
time = np.array(data['time'])
acc = np.array(data['acc'])
alg = np.array(data['alg'])
name = np.array(data['dataset'])

alg_name, tmp = np.unique(alg, return_inverse=True)
marker = {}
marker[alg_name[0]] = 's'
marker[alg_name[1]] = 'o'
marker[alg_name[2]] = '^'

color = {}
dataset_name, tmp = np.unique(name, return_inverse=True)
for i in xrange(dataset_name.shape[0]):
    color[dataset_name[i]] = cm.Accent(float(i)/4)

N = time.shape[0]

ax.set_xscale('log')
plt.gca().invert_yaxis()
plt.ylim((100,70))
plt.xlim((10**0,10**7))
x,y = 70,0

# circ_offset = ScaledTranslation(x,y,ax.transScale)
# circ_tform = circ_offset + ax.transLimits + ax.transAxes
# circ = plt.Circle((0,100),x,color='r',alpha=0.5,transform=ax.transAxes)
# ax.add_artist(circ)
#
# # plot a circle with dashes
# x0, y0 = ax.transAxes.transform((0, 0)) # lower left in pixels
# x1, y1 = ax.transAxes.transform((1, 1)) # upper right in pixes
# ax.add_artist(Ellipse((0, 100), 1000, 30, fill=False, linestyle='dashed'))

for i in xrange(9):
    circle((1,100),0.2*(i+1), fig, ax, {'color':'0.75', 'fill' : False, 'linestyle':'dashed'})
# circle((1,100),0.7, fig, ax, {'color':'r', 'fill' : False, 'linestyle':'dashed'})
# circle((1,100),0.5, fig, ax, {'color':'r', 'fill' : False, 'linestyle':'dashed'})
# ax.add_artist(c)

p = []
for i in xrange(N):
    t = ax.plot(time[i],acc[i], marker=marker[alg[i]],ms=20,color=color[name[i]])
    # p.append(t)

for i in xrange(dataset_name.shape[0]):
    p.append(AnyObject(color=color[dataset_name[i]]))
for i in xrange(alg_name.shape[0]):
    p.append(AnyObject(marker=marker[alg_name[i]]))

lst_name = np.concatenate((dataset_name,alg_name))

plt.legend(p,lst_name,
           handler_map={AnyObject: AnyObjectHandler()},loc=2)
ax.set_xlabel('Running time (seconds)')
ax.set_ylabel('Accuracy (%)')
plt.show()