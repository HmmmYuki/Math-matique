from pylab import *

def f(x):
    y = 1/x
    return y

pas = 10/499
listex = []
listey = []

for i in range(0, 500):
    x = -5 + i*pas
    y = f(x)
    listex.append(x)
    listey.append(y)

plot(listex, listey, 'or')
ylim(-10, 10)
show()