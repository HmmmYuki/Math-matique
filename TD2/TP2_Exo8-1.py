from pylab import *

def f(x):
    y = x**3
    return y

pas = 0.06 # 6 divisée par 100
listex = []
listey = []

for i in range(0, 100):
    x = -3 + i*pas
    y = f(x)
    listex.append(x)
    listey.append(y)

plot(listex, listey, '.b')
show()