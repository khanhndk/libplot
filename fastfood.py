import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report_dir = 'P:/OFOC/x64/Debug/'

dataname1 = 'rf'
dataname2 = 'ff'

suffix = '_0.100000_128'

data_rf = pd.read_csv(report_dir+dataname1+suffix+'.txt', sep='\t', engine='python', header=None)
data_ff = pd.read_csv(report_dir+dataname2+suffix+'.txt', sep='\t', engine='python', header=None)

rf = np.array(data_rf.values[0])
# for i in xrange(1, data_rf.ndim):
#     rf = np.vstack((rf, np.array(data_rf.values[i])))

print rf.shape

ff = np.array(data_ff.values[0])
# for i in xrange(1, data_ff.ndim):
#     ff = np.vstack((ff, np.array(data_ff.values[i])))

print ff.shape

# rf = np.average(rf, axis=0)
# ff = np.average(ff, axis=0)

print ff.shape

fig, ax = plt.subplots()
ln1 = ax.plot(rf[:], color='blue')
ln2 = ax.plot(ff[:], color='red')

plt.show()

