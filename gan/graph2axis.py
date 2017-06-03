import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')

exp_folders = ['',
               '']
labels = ['GGM', 'GAN']
colors = ['r', 'b']

fig = plt.figure("KL and Wasserstein metrics")
lines = []
line_labels = []
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

n = 1200
for i, s in enumerate(exp_folders):
    measure_file = "measure_%s.txt" % str(i+1)
    data = np.loadtxt(measure_file, dtype=np.float32,
                      delimiter='\t')
    data = data[:n, :]
    b = data[:, 3] > 0

    data_small = data[b, :]
    epoch = data_small[:, 0]
    KL_sym = (data_small[:, 1]+data_small[:, 2])/2.0
    Ws = data_small[:, 3]
    ax = ax1
    if i > 0:
        ax = ax2

    lns1 = ax.plot(epoch, KL_sym, '%so-' % colors[i], label="Symmetric KL (%s)" % labels[i])
    lns2 = ax.plot(epoch, Ws, '%sx--' % colors[i], label="Wasserstein (%s)" % labels[i])
    line_labels.append("Symmetric KL (%s)" % labels[i])
    line_labels.append("Wasserstein (%s)" % labels[i])
    lines = lines + lns1 + lns2

plt.grid(True)

ax1.set_xlabel("epoch")
ax1.set_ylabel("value")
ax2.set_ylabel("value")

plt.legend(lines, line_labels)
plt.show()
print('Finish')

