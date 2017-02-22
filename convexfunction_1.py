import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 0.35*x**2 - 2*x + 5


def grad_func(x):
    return 2*0.35*x-2

x = np.linspace(0, 10, 100)
y = func(x)

a = 4
b = 7
fa = func(a)
gfax = grad_func(a)*(x-a)+fa

fb = func(b)
gfbx = grad_func(a)*(b-a)+fa
# ab = np.linspace(0,10,100)
#
# m = a + (1-alpha)*(b-a)
# fm = func(m)
#
# right_hand = alpha*fa + (1-alpha)*fb

ymin = 0
ymax = 10
fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.plot(x, gfax, 'b')
plt.plot([b,b],[0,fb],'go--',linewidth=1)
plt.plot([b,b],[0,gfbx],'bo--',linewidth=1)
plt.plot([a,a],[0,fa],'bo--',linewidth=1)
# plt.plot([a,a,b,b],[ymin,fa,fb,ymin],'bo--',linewidth=1)
# plt.plot([m,m],[ymin,right_hand],'mo--',linewidth=1)
# plt.plot([m,m],[ymin,fm],'go--',linewidth=1)
plt.ylim(ymax=ymax,ymin=ymin)

plt.annotate('$f(y)$',xy=(b,fb),xytext=(b+0.2,fb))
plt.annotate('$g^T(x_0)(y-x_0)+f(x_0)$',xy=(b,gfbx),xytext=(b+0.5,gfbx-0.1))
plt.annotate('$\\geq 0$',xy=(b,fb-1),xytext=(b,fb-1.5))
# plt.annotate('$f(y)$',xy=(b,fb),xytext=(b-0.5,fb))
# plt.annotate('$f(\\alpha x+(1-\\alpha)y)$',xy=(m,fm),xytext=(m+0.1,fm-0.3))
# plt.annotate('$\\alpha f(x)+(1-\\alpha)f(y)$',xy=(m,right_hand),xytext=(m+0.2,right_hand-0.2))
#
ax.set_xticks((a, b))
ax.set_xticklabels(('$x_0$', '$y$'))
ax.set_yticks([])

plt.show()