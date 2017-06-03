import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

import pickle

nstep_gogp = 533
nstep_gpy = 5330

dataname_gogp = 'slice.tu.sh2_170313_155751'
report_gogp = pickle.load(open('K:/PyGOGP/log/'+dataname_gogp+'.log.p', "rb"))

dataname_gpy = 'slice.tu.sh2'
report_gpy = pickle.load(open('K:/gpytest/v1/log'+dataname_gpy+'.log.p', 'rb'))

rmse_lst_gogp = report_gogp.rmse_lst
time_gogp = report_gogp.online_time
ngap_gogp = int(len(rmse_lst_gogp) / nstep_gogp)

rmse_lst_gpy = report_gpy['rmse_lst']
time_gpy = report_gpy['onlinetime']
ngap_gpy = int(len(rmse_lst_gpy) / nstep_gpy)

time_gogp_line = np.linspace(0, time_gogp, nstep_gogp)
time_gpy_line = np.linspace(0, time_gpy, nstep_gpy)

rmse_gogp_line = np.array(rmse_lst_gogp)
rmse_gpy_line = np.array(rmse_lst_gpy)

datapoints = np.linspace(10000,5336471,nstep)

print rmse_gogp_line.shape
print rmse_gpy_line.shape
print time_gogp_line.shape
print time_gpy_line.shape

fig, ax = plt.subplots()
ax.grid()

ln1 = ax.plot(time_gogp_line, rmse_gogp_line, label="SGP-SVI")
ln2 = ax.plot(time_gpy_line, rmse_gpy_line, label="GOGP")

lns = ln1+ln2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=4)
ax.set_ylabel('RMSE')
ax.set_xlabel('Time (s)')

ax.plot(time_gogp_line[-1], rmse_gogp_line[-1], marker='o', color='red', markersize=10)
ax.plot(time_gpy_line[-1], rmse_gpy_line[-1], marker='o', color='red', markersize=10)

# plt.xlim(xmax=50873,xmin=0)
ax.set_xscale('log', basex=2)
# ax.set_xlim(xmin=120, xmax=55000)
# plt.ylim(ymax=39.2, ymin=38.3)
# plt.minorticks_on()
# ax.set_xticks((200, ))
# ax.set_xticklabels(('$x_0$', '$y$'))

plt.show()
