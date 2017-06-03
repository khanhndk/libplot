import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')

exp_folders = ['',
               '']
labels = ['GGM', 'GAN']
colors = ['r', 'b']

plt.figure("KL and Wasserstein metrics")
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
    plt.plot(epoch, KL_sym, '%so-' % colors[i], label="Symmetric KL (%s)" % labels[i])
    plt.plot(epoch, Ws, '%sx--' % colors[i], label="Wasserstein (%s)" % labels[i])

    print('abc')
plt.grid(True)
plt.xlabel('epoch')
plt.ylabel('value')
plt.legend()
plt.show()
print('Finish')

