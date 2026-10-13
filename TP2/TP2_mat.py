from pylab import *
def f(x):
    y=2
    return y

pas=1
listex=[]
listey=[]
for i in range(0,20) : 
    x=10
    y=f(x)
    listex.append(x)
    listey.append(y)

    plot(listex,listey, '*')

xlim(5,3)
ylim(14,14)
axis("equal")

plot (x,y,linewidth=3,*'r')

show()
