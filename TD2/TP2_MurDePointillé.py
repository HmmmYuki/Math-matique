from pylab import *
xlim(0,20)
ylim(0,30)

for i in range(10, 20):
    y=i
    for u in range(5, 15):
        x=u
        plot(x,y,'*')

show()
