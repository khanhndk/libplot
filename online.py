import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

import pickle
data1 = pd.read_csv('P:/vudata/out.2008.txt.csv')

rmse1 = np.array(data1['RMSE'])

nstep = 533
ngap = int(rmse1.shape[0] / nstep)

nstep1 = 5330
ngap1 = int(rmse1.shape[0] / nstep1)

INPUT_FOLDER='P:/vudata/Airline/f4/'
# result_id = '2008__160520_1622005'
#
# f = open(INPUT_FOLDER+result_id+'.pickle')
# learner = pickle.load(f)
# f.close()
# rmse2 = learner.rmse_arr[:533]
# time2 = np.linspace(ngap, learner.train_time, nstep)

data2 = pd.read_csv(INPUT_FOLDER+'2008__160520_1622005.csv')
rmse2 = np.array(data2['RMSE'])[:nstep]
time2 = np.linspace(0, 1973.26999998, nstep)





rmse1 = rmse1[ngap1:rmse1.shape[0]:ngap1]
time1 = np.linspace(0, 50873.24, nstep1)
# time = time[1:(time.shape[0])]
print rmse1.shape
print time1.shape


datapoints = np.linspace(10000,5336471,nstep)

print rmse2.shape
print time2.shape

fig, ax = plt.subplots()

ax.grid()

ln1 = ax.plot(time1, rmse1, label="SGP-SVI")
ln2 = ax.plot(time2, rmse2, label="GOGP")

lns = ln1+ln2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=4)
ax.set_ylabel('RMSE')
ax.set_xlabel('Time (s)')

ax.plot(time1[time1.shape[0]-1],rmse1[time1.shape[0]-1],marker='o',color='red',markersize=10)
ax.plot(time2[time2.shape[0]-1],rmse2[time2.shape[0]-1],marker='o',color='red',markersize=10)

# plt.xlim(xmax=50873,xmin=0)
ax.set_xscale('log',basex=2)
ax.set_xlim(xmin=120,xmax=55000)
plt.ylim(ymax=39.2,ymin=38.3)
# plt.minorticks_on()
# ax.set_xticks((200, ))
# ax.set_xticklabels(('$x_0$', '$y$'))


plt.show()
