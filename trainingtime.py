import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

data = pd.read_csv('P:/exp/mkl-np/time.csv')
alg_name = ['MKL-DA', 'BEMKL', 'UFO-MKL']
x_label = 'dataset'
padding = 0.4


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

N = len(alg_name)
M = np.array(data[alg_name[0]]).shape[0]
ind = np.arange(M)  # the x locations for the groups
width = (1.0-padding)/N
bar_list = []
matplotlib.rcParams.update({'font.size': 16})

fig, ax = plt.subplots()
for i in xrange(N):
    bar = ax.bar(padding/2+ind+width*i, np.array(data[alg_name[i]]), width, color=cm.Accent(float(i)/N))
    # autolabel(bar)
    bar_list.append(bar)

# add some text for labels, title and axes ticks
ax.set_ylabel('Training time (seconds)')
ax.set_yscale('log')
ax.set_xticks(ind + width)
ax.set_xticklabels(np.array(data[x_label]))

locs, labels = plt.xticks()
plt.setp(labels, rotation=45)
plt.gcf().subplots_adjust(bottom=0.18,right=0.99)

ax.legend(bar_list, alg_name,loc=4)

fig.set_size_inches(8, 6)
fig.savefig('P:/exp/mkl-np/time6.pdf', dpi=600)

plt.show()