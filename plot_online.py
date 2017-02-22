import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report_dir1 = 'H:/f03/amm_online/'
report_dir2 = 'H:/f03/sammex1/v12/'
dataname1 = 'a9a@'
dataname2 = 'a9a.274f_1'


data1 = pd.read_csv(report_dir1+dataname1+'.txt',sep='\t|:',engine='python',header=None)
data2 = pd.read_csv(report_dir2+dataname2+'.txt',sep='\t|:',engine='python',header=None)

index1 = 13
index2 = 12
st_array1 = np.array(data1.values[0][index1].split('|'))[:][:-1]
st_array2 = np.array(data2.values[0][index2].split('|'))[:-1]

x1 = st_array1.astype(np.float)
N1 = len(x1)
x1 = x1[51:N1-1]
N1 = len(x1)
print N1


x2 = st_array2.astype(np.float)
N2 = len(x2)
print N2

fig, ax = plt.subplots()
ln1 = ax.plot(x1)
ln2 = ax.plot(x2)

plt.show()
