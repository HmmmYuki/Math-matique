from pylab import *
xlim(0,25)
ylim(0,45)

listex = []
listey = []
listew = []
listec = []

for x in range(0, 21):
    listex.append(x)
    listey.append(2*x)
    listew.append(x)
    listec.append(x/2)


    plot(listex, listey, 'dr')
    plot(listex, listew, 'ob')
    plot(listex, listec, '*g')

show()