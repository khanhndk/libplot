import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def calc_dist(X, Y):
    normx = np.sum(X**2,axis=0,keepdims=True)
    normy = np.sum(Y**2,axis=0,keepdims=True)
    return np.tile(normx.T,(1,Y.shape[1])) + np.tile(normy,(X.shape[1],1))-2*np.dot(X.T,Y)


def top_l_max(L, X):
    mask = np.ones(X.shape[0],dtype=bool)
    index = np.array(range(X.shape[0]),dtype=int)
    top = np.zeros(L, dtype=int)
    for k in xrange(L):
        top[k] = index[mask][np.argmax(X[mask])]
        mask[top[k]] = False
    return mask

# create data
mean1 = [0, 0]
cov1 = [[5, 0.01], [5, 10]]
mean2 = [20,20]
cov2 = [[5, 5], [0.01, 10]]
x1 = np.random.multivariate_normal(mean1, cov1, 50).T
x2 = np.random.multivariate_normal(mean2, cov2, 50).T
outlier = np.array([[0,25],[35,0]])
# plt.plot(x1, y1, 'o', color='gray')
# plt.plot(x2, y2, 'o', color='gray')
# plt.plot(outlier[:,0], outlier[:,1], 'o', color='gray')
# plt.axis('equal')
# plt.show()

xtrain = np.hstack((x1,x2,outlier))

L = 2
K = 2

centers = xtrain[:,[0,1]]
for loop in xrange(5):
    dist = calc_dist(centers, xtrain)

    mask = top_l_max(L, np.min(dist,axis=0))

    assignments = np.argmin(dist,axis=0)
    assignments[~mask] = -1

    for k in xrange(K):
        centers[:,k] = np.average(xtrain[:,assignments==k],axis=1)

    for k in xrange(K):
        plt.plot(xtrain[0][assignments==k], xtrain[1][assignments==k], '+', color=cm.Paired(float(k)/K))

    plt.plot(xtrain[0][assignments==-1], xtrain[1][assignments==-1], 's', color='black')
    plt.plot(centers[0], centers[1], 'o', color='red')

    plt.axis([-20,50,-20,50],'equal')
    plt.show()

