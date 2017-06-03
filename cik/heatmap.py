import scipy.io as sio
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors


mat_container_bank = sio.loadmat('gram.bank.gauss2d.v6a.mat')
gram_bank = np.log(np.maximum(1e-8, mat_container_bank['gram'].T / 1100))

mat_container_cik = sio.loadmat('gram.cik.gauss2d.v6a.mat')
gram_cik = np.log(np.maximum(1e-8, mat_container_cik['gram'].T / 1100))
print(gram_bank.shape)
print(gram_cik.shape)

fig, (ax1, ax2, axcb) = plt.subplots(
    1, 3, gridspec_kw={'width_ratios': [1, 1, 0.08]})
ax1.get_shared_y_axes().join(ax2)


cmap = sns.cubehelix_palette(dark=0.2, light=1.0, as_cmap=True)

ax1 = sns.heatmap(
    gram_cik, cmap=cmap, ax=ax1, cbar=False
)

ax2 = sns.heatmap(
    gram_bank, cmap=cmap, ax=ax2, cbar_ax=axcb
)

ax1.invert_yaxis()
ax1.set(yticks=[])
ax1.set(xticks=[])
ax1.set_aspect("equal")
ax1.set_xlabel('CIK')

ax2.invert_yaxis()
ax2.set(yticks=[])
ax2.set(xticks=[])
ax2.set_aspect("equal")
ax2.set_xlabel('BaNK')

# fig.colorbar(pcm, ax=ax[0], extend='max')

plt.show()
