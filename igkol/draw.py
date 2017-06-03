import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

import pickle

dataname = 'svmguide1'
report_igkol = pickle.load(open('igkol.'+dataname+'.log.p', "rb"))

report_dsgd = pickle.load(open('dsgd.'+dataname+'.log.p', "rb"))

metric = 'train_loss'

obj_func_igkol = np.array(report_igkol[metric])
obj_func_dsgd = np.array(report_dsgd[metric])

len_igkol = len(obj_func_igkol)
len_dsgd = len(obj_func_dsgd)
print(obj_func_igkol.shape)
print(obj_func_igkol.shape)

max_len = np.maximum(len_dsgd, len_igkol)

x_igkol = np.linspace(0, max_len, len_igkol)
x_dsgd = np.linspace(0, max_len, len_dsgd)


fig, ax = plt.subplots()
ax.grid()

ln1 = ax.plot(x_igkol, obj_func_igkol, label="DualIGD")
ln2 = ax.plot(x_dsgd, obj_func_dsgd, label="DualSGD")

lns = ln1+ln2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
# ax.set_ylabel('RMSE')
ax.set_xlabel('Epoches')
#
# ax.plot(time_gogp_line[-1], rmse_gogp_line[-1], marker='o', color='red', markersize=10)
# ax.plot(time_gpy_line[-1], rmse_gpy_line[-1], marker='o', color='red', markersize=10)
#
# # plt.xlim(xmax=50873,xmin=0)
# ax.set_xscale('log', basex=2)
# # ax.set_xlim(xmin=120, xmax=55000)
# # plt.ylim(ymax=39.2, ymin=38.3)
# # plt.minorticks_on()
# # ax.set_xticks((200, ))
# # ax.set_xticklabels(('$x_0$', '$y$'))
#
plt.show()
