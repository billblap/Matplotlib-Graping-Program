import matplotlib.pyplot as plt
print ("coords go as x -> y")
print ("type plot at any point after typing in BOTH x and y COORDS")
print ("the coords will be sorted")
print ("bill barg 2020 :)")
print ("")
global xcoords
xcoords = []
global ycoords
ycoords = []
def start():
    global xcoords
    global ycoords
    x = input ("x coord..")
    x = int(x)
    xcoords.append(x)
    y = input ("y coord..")
    y = int(y)
    ycoords.append(y)
    print (xcoords,ycoords)
    z = input ("continue plotting? y/n")
    if z == "y":
        start()
    else:
        plot()

def plot():
    
    print ("xcoords are",xcoords)
    print ("ycoords are",ycoords)
    global maxx
    maxx = max(xcoords)
    global maxy
    maxy = max(ycoords)
    print ("max x value is",maxx)
    print ("max y value is",maxy)
    maxx = maxx + 10
    maxy = maxy + 10
    graph()

    

def graph():
    global xcoords
    global ycoords
    global maxx
    global maxy
    plt.plot(xcoords,ycoords)
    plt.xlim(0,maxx)
    plt.ylim(0,maxy)
    plt.show()

    


start()
