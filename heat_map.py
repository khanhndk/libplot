import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

dataname = 'seismicbin1'
var_name = '.heatDB'
xl_file = pd.ExcelFile('K:/ofoc/report/'+dataname+var_name+'.xlsx')

df = xl_file.parse('311_2a1a')

df_mean = df.groupby('testid:', sort=False).mean()
# df_err = df.groupby('testid:', sort=False).std()

df_pivot = df_mean.pivot('dim_rf:', 'batch_size', 'acc_oc:')

print df_pivot

ax = sns.heatmap(df_pivot)
ax.invert_yaxis()
plt.yticks(rotation=0)
plt.show()

