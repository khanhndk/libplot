import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

font = {'family': 'normal',
        # 'weight': 'bold',
        'size': 14}
matplotlib.rc('font', **font)

dataname = 'KDD'
var_name = '.report'
xl_file = pd.ExcelFile('K:/ofoc/report/'+dataname+var_name+'.xlsx')

df = xl_file.parse('Sheet1')
alg = np.array(df['alg'])
time = np.array(df['time'])
acc = np.array(df['acc'])
print time
print alg
print acc

N = len(alg)

mid_point = 3
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
index = np.array([1.5, 5])
bar_width = (mid_point - 0.5) / N
opacity = 0.8

bar_list = []
for n in xrange(N):
    mybar2 = ax2.bar(index[1] + n * bar_width, np.array([acc[n]]), bar_width,
                     # alpha=opacity,
                     color=cm.Accent(float(n) / N),
                     label=alg[n])
    bar_list.append(mybar2)
    mybar1 = ax1.bar(index[0] + n*bar_width, np.array([time[n]]), bar_width,
                     # alpha=opacity,
                     color=cm.Accent(float(n)/N),
                     label=alg[n])

mylegend = ax2.legend(bar_list, alg, loc=4)
mylegend.set_zorder(20)
ax1.set_yscale('log', basey=10)
ax1.set_xticks(np.array([2.8, 6.35]))
ax1.set_xticklabels(np.array(['Time', 'Accuracy']))
ax1.set_ylabel("Time (s)")
ax2.set_ylabel("Accuracy (%)")
ax2.set_ylim([80,100])
plt.tight_layout()
plt.show()
fig.savefig('P:/'+dataname+'.pdf', dpi=800)
exit()

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
#
# # lns1 = ax1.errorbar(dim, acc, yerr=acc_err, label='accuracy', marker='s')
# lns1 = ax1.plot(dim, acc, marker='s', color='b', markersize=10, linewidth=1.5)
# ax2 = ax1.twinx()
# # lns2 = ax2.errorbar(dim, time, yerr=time_err, label='time', marker='o', color='r')
# lns2 = ax2.plot(dim, time, marker='o', color='r', markersize=10, linewidth=1.5)
# # added these three lines
# lns = lns1+lns2
# labs = ["accuracy", "time"]
# ax1.legend(lns, labs, loc=4)
#
# ax1.grid()
# ax1.set_xlabel("D")
# ax1.set_ylabel("accuracy (%)")
# ax2.set_ylabel("training time (ms)")
# ax1.set_ylim(85, 100)
# # ax.set_ylim(-20,100)
# plt.tight_layout(pad=0.2)
# plt.show()
#
# fig.set_size_inches(8, 6)
# fig.savefig('P:/'+dataname+'.pdf', dpi=600)