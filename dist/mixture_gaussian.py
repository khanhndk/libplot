import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data1 = np.random.multivariate_normal(mean, cov, 200)
data2 = np.random.multivariate_normal([3,0], [[0.8,1],[-0.8,1]], size=500)

df1 = pd.DataFrame(data1, columns=["x", "y"])

df2 = pd.DataFrame(data2, columns=["x", "y"])


g1 = sns.JointGrid(x='x', y='y', data=df1)
g1 = g1.plot_joint(sns.kdeplot, color='r', alpha=0.5, shade=True, cmap='Blues')
g1.plot_marginals(sns.kdeplot, shade=True)

l1 = len(g1.ax_joint.collections)
g1.x = df2.x
g1.y = df2.y
g1.ax_joint.collections[0].set_alpha(0)


g1 = g1.plot_joint(sns.kdeplot, color='g', alpha=0.5, shade=True, cmap='Reds')
g1.ax_joint.collections[l1].set_alpha(0)
g1.plot_marginals(sns.kdeplot, color='r', shade=True)


plt.show()
