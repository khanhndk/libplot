import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import seaborn as sns
exp_folder = ''
x_gen_file = '%sdatagen00000400.npz' % exp_folder
x_data_file = '%sdata.npz' % exp_folder

data = np.load(x_gen_file)
x_gen = data['x_gen']
idx = np.random.permutation(x_gen.shape[0])
idx = idx[:10000]
x_gen = x_gen[idx, :]

data = np.load(x_data_file)
x_data = data['data']


df1 = pd.DataFrame(x_data, columns=["x", "y"])
df2 = pd.DataFrame(x_gen, columns=["x", "y"])

g1 = sns.JointGrid(x='x', y='y', data=df2, xlim=[-1.2, 1.2], ylim=[-0.8, 0.8])

levels = [0.5,1,2,3,4,6,50]
n_levels = len(levels);
idx_lst = list(range(1,n_levels))
colors = [cm.Reds(float(i) / n_levels) for i in idx_lst]

g1 = g1.plot_joint(sns.kdeplot, n_levels=levels,
                   alpha=0.8, shade=True,
                   cmap = None,
                   colors=colors,
                   normed=True)
g1.plot_marginals(sns.kdeplot, color='r', shade=True)


g1.x = df1.x
g1.y = df1.y
# g1.ax_joint.collections[0].set_alpha(0)
g1 = g1.plot_joint(sns.kdeplot, color='r', alpha=0.5, shade=True, cmap='Blues')
g1.plot_marginals(sns.kdeplot, shade=True)
l1 = len(g1.ax_joint.collections)
# g1.ax_joint.collections[l1].set_alpha(0)

plt.show()
