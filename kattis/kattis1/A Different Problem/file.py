import sys

def binary(endsorted, x):

    low = 0
    high = x

    while low <= high:
        mid = (low + high) // 2
        if endsorted[mid][1] <= endsorted[x][0]:
            if endsorted[mid + 1][1] <= endsorted[x][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return None

l = []
for n,i in enumerate(sys.stdin):
    if(n == 0):
        x = int(i)
    else:
        ab = i.split()
        start = int(ab[0])
        end = int(ab[1])
        weight = int(ab[2])
        l.append((start,end,weight))
    
endsorted = sorted(l, key=lambda tup: tup[1],reverse = True)
# print(endsorted)

endsorted.sort(key=lambda x: x[1])

x = len(endsorted)

profit = [None] * x
profit[0] = endsorted[0][2]

#print(profit)
for i in range(1, x):
    index = binary(endsorted, i)
    incl = endsorted[i][2]
    if index != None:
        incl += profit[index]
    profit[i] = max(incl, profit[i - 1])
#    print(profit)
print(profit[x - 1])
