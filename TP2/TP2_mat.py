from pylab import *
def f(x):
    y=x**2
    return y

pas=1
listex=[]
listey=[]
for i in range(0,20) : 
    x=-10+i*pas
    y=f(x)
    listex.append(x)
    listey.append(y)

    plot(listex,listey, '--*')

xlim(-5,10)
ylim(3,13)
axis("equal")

plot (x,y,'--r*')
plot (x,y,linewidth=5)

show()
