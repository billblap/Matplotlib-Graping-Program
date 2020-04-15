import matplotlib.pyplot as plt
#([x axis],[y axis],color and linetype)
plt.plot([1, 2, 3 ,4],[1,3,2,4], 'ro')
#([xmin, xmax, ymin, ymax]) (.axis)
plt.axis([0,6,0,20])
plt.ylabel("some numbers")
plt.show()
