import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rcParams.update({'font.size': 12})

dataname = 'a9a'
var_name = '.ub'
filename = 'K:/odsm/v15/'+dataname+var_name+'.delta.35.14h.txt'
csv_file = pd.read_csv(filename, sep="\t| ", engine='python', header=None)

df_mean = csv_file.groupby(1, sort=False).mean()

print df_mean[3]
print np.array(df_mean[21])

index = range(0, df_mean.shape[0], 1)

acc = np.array(df_mean[7])[index] * 100
modesize = np.array(df_mean[21])[index]
delta = np.array(df_mean[35])[index] # 29, 35

# acc_err = np.array(df_err['acc_oc:'])[index] * 100
# modesize_err = np.array(df_err['train:'])[index] * 1000

fig = plt.figure()
ax1 = fig.add_subplot(111)

# lns1 = ax1.errorbar(delta, acc, yerr=acc_err, label='accuracy', marker='s')
lns1 = ax1.plot(delta, acc, marker='s', color='b')
ax2 = ax1.twinx()
# lns2 = ax2.errorbar(delta, modesize, yerr=modesize_err, label='modesize', marker='o', color='r')
lns2 = ax2.plot(delta, modesize, marker='o', color='r')
# added these three lines
lns = lns1+lns2
labs = ["accuracy", "model size"]
ax1.legend(lns, labs, loc=0)

ax1.grid()
ax1.set_xlabel("$\delta$",fontsize=17)
ax1.set_ylabel("accuracy (%)")
ax2.set_ylabel("model size")
ax1.set_xlim(1, 20)
ax1.set_ylim(60, 90)
# ax.set_ylim(-20,100)
plt.show()
