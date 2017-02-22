import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 0.35*x**2 - 2*x + 5

x = np.linspace(0, 10, 100)
y = func(x)

a = 1
b = 7
alpha = 0.7
fa = func(a)

fb = func(b)
ab = np.linspace(0,10,100)

m = a + (1-alpha)*(b-a)
fm = func(m)

right_hand = alpha*fa + (1-alpha)*fb

ymin = 0
ymax = 10
fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.plot([a,a,b,b],[ymin,fa,fb,ymin],'bo--',linewidth=1)
plt.plot([a,a,b,b],[ymin,fa,fb,ymin],'bo--',linewidth=1)
plt.plot([m,m],[ymin,right_hand],'mo--',linewidth=1)
plt.plot([m,m],[ymin,fm],'go--',linewidth=1)
plt.ylim(ymax=ymax,ymin=ymin)

plt.annotate('$f(x)$',xy=(a,fa),xytext=(a,fa+0.5))
plt.annotate('$f(y)$',xy=(b,fb),xytext=(b-0.5,fb))
plt.annotate('$f(\\alpha x+(1-\\alpha)y)$',xy=(m,fm),xytext=(m+0.1,fm-0.3))
plt.annotate('$\\alpha f(x)+(1-\\alpha)f(y)$',xy=(m,right_hand),xytext=(m+0.2,right_hand-0.2))
plt.annotate('$\\geq 0$',xy=(m,fm+1),xytext=(m,fm+1))

ax.set_xticks((a, m, b))
ax.set_xticklabels(('$x$', '$\\alpha x+(1-\\alpha)y$' , '$y$'))
ax.set_yticks([])

plt.show()