
import matplotlib.pyplot as plt

points = [(1,2),(3,4),(5,6),(5,3),(21,42),(31,4),(5,64),(6.2,7.1)]

x = []
y = []
for i in points:
    x.append(i[0])
    y.append(i[1])

plt.scatter(x,y)
plt.show()

def closestpoints(points):
    sortbyx = sorted(points, key=lambda x: x[0])
    
    sbxmiddle = int(len(sortbyx)/2)
    
    sbxpart1 = sortbyx[:sbxmiddle]
    sbxpart2 = sortbyx[sbxmiddle:]
    
    print(sbxpart1)
    print(sbxpart2)
    
    
    
    
closestpoints(points)



'''
Sort points according to their x-coordinates.
Split the set of points into two equal-sized subsets by a vertical line x=xmid.
Solve the problem recursively in the left and right subsets. This yields the left-side and right-side minimum distances dLmin and dRmin, respectively.
Find the minimal distance dLRmin among the set of pairs of points in which one point lies on the left of the dividing vertical and the other point lies to the right.
The final answer is the minimum among dLmin, dRmin, and dLRmin.
'''