import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rcParams.update({'font.size': 12})

vary_name = 'n'
vary_item = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
acc = np.array([[0.0901, 0.0619, 0.0604, 0.0838, 0.0686, 0.0647, 0.0621, 0.0623, 0.0644, 0.0666],
               [0.0903, 0.0726, 0.0721, 0.0571, 0.0856, 0.0896, 0.0672, 0.1187, 0.0750, 0.0614],
               [0.0628, 0.0736, 0.0825, 0.0631, 0.0641, 0.1006, 0.1752, 0.0850, 0.0800, 0.0994],
               [0.0744, 0.0747, 0.0807, 0.0684, 0.0731, 0.0612, 0.0738, 0.0641, 0.0671, 0.0650]])
time = np.array([[35.5306, 31.6088, 29.9526, 29.0464, 28.9994, 28.7964, 28.3745, 28.3276, 28.2182, 28.6401]])
acc = np.mean(acc, axis=0)
time = np.mean(time, axis=0)

# vary_name = 'm'
# vary_item = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# acc = np.array([[0.0698, 0.1015, 0.0620, 0.0654, 0.0597, 0.1197, 0.0815, 0.0607, 0.0797, 0.0684],
#                 [0.0580, 0.0823, 0.0858, 0.0671, 0.0677, 0.0612, 0.0654, 0.0687, 0.0673, 0.0676]])
# time = np.array([[42.5633, 58.1280, 73.3086, 85.4432, 98.4146, 111.1124, 122.5783, 130.4868, 141.0395, 147.2317],
#                 [41.0965, 54.4569, 68.0817, 80.7114, 91.9022, 103.8027, 115.8047, 124.5819, 132.1573, 137.3724]])
# acc = np.mean(acc, axis=0)
# time = np.mean(time, axis=0)

# vary_name = 'n'
# vary_item = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# acc = np.array([[0.0183, 0.0150, 0.0150, 0.0137, 0.0146, 0.0171, 0.0133, 0.0146, 0.0160, 0.0185],
#                [0.0141, 0.0143, 0.0173, 0.0143, 0.0152, 0.0170, 0.0151, 0.0153, 0.0159, 0.0156]])
# time = np.array([[78.4960, 70.3331, 74.2539, 70.6328, 70.5513, 69.5153, 64.8156, 66.1520, 41.3430, 41.0461],
#                 [81.5807, 74.8255, 75.7580, 70.7545, 69.9799, 71.4190, 68.1939, 69.0222, 41.8898, 41.5149]])
# acc = np.mean(acc, axis=0)
# time = np.mean(time, axis=0)

# vary_name = 'm'
# vary_item = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# acc = np.array([[0.0153, 0.0167, 0.0266, 0.0165, 0.0164, 0.0172, 0.0198, 0.0179, 0.0198, 0.0198],
#                 [0.0179, 0.0251, 0.0164, 0.0188, 0.0168, 0.0188, 0.0194, 0.0191, 0.0145, 0.0174]
#                 ])
# time = np.array([[87.5538, 114.8865, 143.2446, 176.7813, 189.8437, 209.5002, 212.7129, 223.0154, 254.9375, 258.3233],
#                  [86.6131, 114.0230, 133.7088, 155.4281, 178.4497, 187.1532, 219.3188, 233.8764, 272.6903, 355.6027]
#                  ])
# acc = np.mean(acc, axis=0)
# time = np.mean(time, axis=0)

idx_remove = np.array([], dtype=int)
mask_remove = np.ones(len(vary_item), dtype=bool)
mask_remove[idx_remove] = False

vary_item = vary_item[mask_remove]
acc = acc[mask_remove]
time = time[mask_remove]

acc = (1-acc) * 100

# acc_err = np.array(df_err['acc_oc:'])[index] * 100
# modesize_err = np.array(df_err['train:'])[index] * 1000

fig = plt.figure()
ax1 = fig.add_subplot(111)

# lns1 = ax1.errorbar(delta, acc, yerr=acc_err, label='accuracy', marker='s')
lns1 = ax1.plot(vary_item, acc, marker='s', color='b', linewidth=3, markersize=10)
ax2 = ax1.twinx()
# lns2 = ax2.errorbar(delta, modesize, yerr=modesize_err, label='modesize', marker='o', color='r')
lns2 = ax2.plot(vary_item, time, marker='o', color='r', linewidth=3, markersize=10)
# added these three lines
lns = lns1+lns2
labs = ["Accuracy", "Time"]
ax1.legend(lns, labs, loc=4)

ax1.grid()
# ax1.set_xlabel("$\delta$", fontsize=17)
ax1.set_xlabel(vary_name)
ax1.set_ylabel("Accuracy (%)")
ax2.set_ylabel("Time (s)")
# ax1.set_xlim(1, 20)
ax1.set_ylim(60, 100)
plt.xticks([100, 300, 500, 700, 900])
ax2.set_ylim(20, 50)
# ax.set_ylim(-20,100)
fig.set_size_inches(4, 3)
plt.tight_layout(pad=0.2)

plt.show()
