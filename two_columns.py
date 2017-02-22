import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

font = {'family': 'normal',
        # 'weight': 'bold',
        'size': 22}

matplotlib.rc('font', **font)

dataname = 'shuttlebin1'
var_name = '.Dvaried'
xl_file = pd.ExcelFile('K:/ofoc/report/'+dataname+var_name+'.xlsx')

df = xl_file.parse('312_2a1')

df_mean = df.groupby('testid:', sort=False).mean()
df_err = df.groupby('testid:', sort=False).std()

index = range(0, 40, 1)

acc = np.array(df_mean['acc_oc:'])[index] * 100
time = np.array(df_mean['train:'])[index] * 1000
dim = np.array(df_mean['dim_rf:'])[index]

acc_err = np.array(df_err['acc_oc:'])[index] * 100
time_err = np.array(df_err['train:'])[index] * 1000

fig = plt.figure()
ax1 = fig.add_subplot(111)

# lns1 = ax1.errorbar(dim, acc, yerr=acc_err, label='accuracy', marker='s')
lns1 = ax1.plot(dim, acc, marker='s', color='b', markersize=10, linewidth=1.5)
ax2 = ax1.twinx()
# lns2 = ax2.errorbar(dim, time, yerr=time_err, label='time', marker='o', color='r')
lns2 = ax2.plot(dim, time, marker='o', color='r', markersize=10, linewidth=1.5)
# added these three lines
lns = lns1+lns2
labs = ["accuracy", "time"]
ax1.legend(lns, labs, loc=4)

ax1.grid()
ax1.set_xlabel("D")
ax1.set_ylabel("accuracy (%)")
ax2.set_ylabel("training time (ms)")
ax1.set_ylim(85, 100)
# ax.set_ylim(-20,100)
plt.tight_layout(pad=0.2)
plt.show()

fig.set_size_inches(8, 6)
fig.savefig('P:/'+dataname+'.pdf', dpi=600)