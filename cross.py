import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    filename = 'H:/f02/svm/a1a~3.cross.txt'
    option = 2
    option_log_scale = 2
    attr = 'em_error'
    df = pd.read_csv(filename)

    X = np.array(df['c'])
    Y = np.array(df['gamma'])
    Z = np.array(df[attr])
    print Z

    if option == 1:
        fig = plt.figure()
        ax = fig.gca(projection = '3d')
        surf = ax.plot_trisurf(X, Y, Z, cmap=cm.jet, linewidth=0.02)
        plt.show()
    elif option == 2:
        X = np.unique(X)
        np.sort(X)
        Y = np.unique(Y)
        np.sort(Y)
        xmesh, ymesh = np.meshgrid(np.log2(X),np.log2(Y))
        # xmesh, ymesh = np.meshgrid(X,Y)
        data = np.zeros((X.shape[0],Y.shape[0]))
        seq = np.zeros((X.shape[0],Y.shape[0]))
        for index, row in df.iterrows():
            idx = np.where(X==float(row['c']))[0][0]
            idy = np.where(Y==float(row['gamma']))[0][0]
            if option_log_scale == 1 :
                data[idx,idy] += np.log10(row[attr])
            elif option_log_scale == 2:
                data[idx,idy] += np.log10(row[attr] / float(X[idx]))
            else:
                data[idx,idy] = row[attr]
            seq[idx,idy] += 1
        data = data / seq
        # # extract subset data
        # data = data[:100,:]
        # X = X[:100]
        # xmesh, ymesh = np.meshgrid(np.log2(X),np.log2(Y))
        # # end extract
        print np.max(data)
        plt.pcolor(xmesh, ymesh, data, cmap=cm.jet)
        plt.colorbar()
        plt.show()

