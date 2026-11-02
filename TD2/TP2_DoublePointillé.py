from pylab import *
xlim(0,20)
ylim(0,6.0)

y=3
y2=5

for i in range(5, 15):
    x=i
    plot(x,y,'*')

for u in range(5, 15):
    x=u
    plot(x,y2,'*')

show()
