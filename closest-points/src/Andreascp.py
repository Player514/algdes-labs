import sys
import math


def parse_stdin(): 
    points = []
    for line in sys.stdin:
        line = line.strip()

        point_match = re.search('^\s*(?P<first>\w+)\s*(?P<second>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))\s*(?P<third>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))$', line)
        if point_match: 
            name = point_match.group("first")
            x = float(point_match.group("second"))
            y = float(point_match.group("third"))
            point = (name, x, y)
            points.append(point)
    return points

def ClosestPair(points,closest1):
#    print("---------------")
#    print("Called ClosestPair")
#    print(points)
#    print("---------------")
    closest = closest1
    if(len(points) > 2):
        part1,part2,middle = Split(points)
        maybeclosest = ClosestPair(part1,closest1)
#        print(points)
        if(maybeclosest < closest):
            closest = maybeclosest
        maybeclosest = ClosestPair(part2,closest1)
        if(maybeclosest < closest):
            closest = maybeclosest

        #DO BAR THING
        #if item between middle+bar/2 and middle-bar/2
        inbar = []
        for i in points:
            if(i[0] < middle+closest and i[0] > middle-closest):
                inbar.append(i)
#        print("inbar: " + str(len(inbar)))
        if(len(inbar) <= 1):
            pass #only 1 inside
        elif(len(inbar) < 4):
#            print("---------------")
#            print("Called Bar")
#            print(inbar)
#            print("---------------")
            maybeclosest = findClosest(inbar)
            if(maybeclosest < closest):
                closest = maybeclosest
        else:
            maybeclosest = ClosestPair(inbar,closest)
            if(maybeclosest < closest):
                closest = maybeclosest
        return closest
    elif(len(points) <= 1):
        return closest
    else: #2
        if(len(points) != 2):
            print("Error points don't eqaul 2")
        maybeclosest = findClosest(points)
        if(maybeclosest < closest):
            closest = maybeclosest
        return closest


def findClosest(points):
    if(len(points) == 2):
        distance1 = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
        print(distance1)
        return distance1
    elif(len(points) == 3):
        distance1 = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
        distance2 = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
        distance3 = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)
        print(distance1)
        print(distance2)
        print(distance3)
        return min(distance1,distance2,distance3)
    else:
        print("Error " + str(len(points)) + " != 2 or 3")
        print(points)

def Split(points):
    sortbyx = sorted(points, key=lambda x: x[0])
    
    sbxmiddle = int(len(sortbyx)/2)
    
    sbxpart1 = sortbyx[:sbxmiddle]
    sbxpart2 = sortbyx[sbxmiddle:]  
    
    #plt.plot([sbxmiddle, sbxmiddle], [0, 250], 'k-', lw=2)
    #plt.scatter(x,y)
    #plt.show()
    
    return sbxpart1, sbxpart2, sbxmiddle


points = parse_input()
ClosestPair(points,sys.maxsize)
    

'''
Sort points according to their x-coordinates.
Split the set of points into two equal-sized subsets by a vertical line x=xmid.
Solve the problem recursively in the left and right subsets. This yields the left-side and right-side minimum distances dLmin and dRmin, respectively.
Find the minimal distance dLRmin among the set of pairs of points in which one point lies on the left of the dividing vertical and the other point lies to the right.
The final answer is the minimum among dLmin, dRmin, and dLRmin.
'''