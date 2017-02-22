import pandas as pd
import numpy as np
from matplotlib.pylab import *
import matplotlib.cm as cm

xl_file = pd.ExcelFile('P:/Dropbox/TrungVu/GaussianProcessSGD/Airline/airline_results_gpy.xlsx')

dfs = {sheet_name: xl_file.parse(sheet_name)
          for sheet_name in xl_file.sheet_names}

u = np.array(dfs['vary_u_2008']['u'])
time = np.array(dfs['vary_u_2008']['time'])
test_rmse = np.array(dfs['vary_u_2008']['test_rmse'])

colors = ["#3498db", "#e74c3c", "#2ecc71"]

fig, ax1 = plt.subplots()
fig.set_size_inches(18.5, 3.5)
ax = fig.gca()
#ax1.set_xticks(np.arange(min(D), max(D), (max(D) - min(D)/20)))
#ax1.set_yticks(np.arange(min(time), max(time), (max(time) - min(time)/20)))
#ax1.grid()
r2 = 2753.61500001

lns1 = ax1.plot(u, time, label="Time of SGP-SVI", marker='o', color=colors[0])
#ax1.errorbar(D, time, yerr=terr, fmt='b')
ax1.set_xlabel('u')
# Make the y-axis label and tick labels match the line color.

ax1_ytick = ax1.get_yticks()
ax1_ylabel = ax1.get_yticklabels()

#ax1_ylabel[0] = '120'
ax1.set_yticks((2000,r2,4000,6000,8000,10000,12000,14000))
#ax.set_yticklabels(ax1_ylabel)

ax1.set_ylabel('Time (s)', color=colors[0])
for tl in ax1.get_yticklabels():
    tl.set_color(colors[0])

for i in xrange(7):
    x = i*100+200
    y = i*2000+2000
    ax1.plot([x,x],[0,14000],':',linewidth=1, color='black')
    ax1.plot([100,800],[y,y],':',linewidth=1, color='black')

ax2 = ax1.twinx()
r1 = 37.64
ax2.plot([120,120],[0,r1],'go--',linewidth=1, color='black')
ax2.plot([800,120],[r1,r1],'+--',linewidth=1, color='black')


lns2 = ax2.plot(u, test_rmse, label="RMSE of SGP-SVI", marker='o', color=colors[1])
lns3 = ax2.plot(120, r1, label="RMSE of GOGP", marker='s',color=colors[1])
# lns3b = ax2.plot(120, 34.7602, label="RMSE of GOGP", marker='s', markersize=15,color=colors[1])


ax1.plot([120,100],[r2,r2],'+--',linewidth=1, color='black')
lns4 = ax1.plot(120, r2, label="Time of GOGP", marker='s',color=colors[0])
# lns4b = ax1.plot(120, 331, label="Time of GOGP", marker='s', markersize=15,color=colors[0])

ax2_ytick = ax2.get_yticks()
ax2_ylabel = ax2.get_yticklabels()
np.insert(ax2_ytick,1,r1)
#ax1_ylabel[0] = '120'
ax2.set_yticks((30,32,34,36,r1,38,40))

ax2.set_xticks((100, 120, 200, 300, 400, 500, 600, 700, 800))
ax2.set_xticklabels(('', '120', '200', '300', '400', '500', '600', '700', '800'))
# ax1.set_yscale('log')

#ax2.errorbar(D, acc, yerr=aerr, fmt='r')
ax2.set_ylabel('RMSE', color=colors[1])
ax2.set_ylim(30,40)
for tl in ax2.get_yticklabels():
    tl.set_color(colors[1])



lns = lns1+lns4+lns2+lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=4)

#plt.savefig('Dvaried_uspst.pdf', bbox_inches='tight')

plt.show()