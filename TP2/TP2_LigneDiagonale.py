from pylab import *
xlim(0,50)
ylim(0,50)


listex = []
listey = []

for x in range(10, 41):
    listex.append(x)
    listey.append(x)

plot(listex, listey, '*b')
show()