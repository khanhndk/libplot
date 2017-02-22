import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csvfile = open('P:/exp/mkl-np/memory.csv')
reader = csv.DictReader(csvfile)
data = list(reader)
df = pd.DataFrame(data, columns = ['dataset', 'bemkl', 'ufo-mkl', 'mkl-da'])

# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1,figsize=(10,5))

# Set the bar width
bar_width = 0.5

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(df['bemkl']))]

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the pre_score data
        df['bemkl'],
        # set the width
        width=bar_width,
        # with the label pre score
        label='bemkl',
        edgecolor='none',
        # with alpha 0.5
        # alpha=0.5,
        # with color
        color='#2ecc71')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the mid_score data
        np.array(df['ufo-mkl'],dtype=float),
        # set the width
        width=bar_width,
        # with pre_score on the bottom
        bottom=np.array(df['bemkl'],dtype=float),
        # with the label mid score
        label='ufo-mkl',
        edgecolor='none',
        # with alpha 0.5
        # alpha=0.5,
        # with color
        color='#e74c3c')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the post_score data
        df['mkl-da'],
        # set the width
        width=bar_width,
        # with pre_score and mid_score on the bottom
        bottom=np.array(df['bemkl'],dtype=float)+np.array(df['ufo-mkl'],dtype=float),
        # with the label post score
        label='mkl-da',
        edgecolor='none',
        # with alpha 0.5
        # alpha=0.5,
        # with color
        color='#34495e')

# # set the x ticks with names
# plt.xticks(tick_pos, df['Dataset'])
#
# # Set the label and legends
# ax1.set_ylabel("Total Score")
# ax1.set_xlabel("Test Subject")
# plt.legend(loc='upper left')

# Set a buffer around the edge
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.show()