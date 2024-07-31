
def boobleSorts (ms):
    n = 1
    while n < len(ms):
        for i in range (len(ms)-n):
            if ms[i] > ms[i+1]:
                ms[i], ms[i+1] = ms[i+1], ms[i]
        n += 1
    return ms
#Test



def BinarySearch (ms,searchInt):
    low = 0;
    hight = len(ms) - 1

    for i in range (len(ms)):
        middle = (low + hight)//2
        ser = ms[middle]
        if ser == searchInt:
            return True;
        if ser > searchInt:
            hight = middle - 1;
        else:
            low = middle + 1;

    return False;

def quickSort (elms):
    if len (elms) <= 1 :
        return elms
    
    elm = elms[0]
    left = list(filter(lambda x: x < elm, elms))
    center = [i for i in elms if i == elm ]
    right = list(filter(lambda x: x > elm, elms))

    return quickSort(left) + center + quickSort(right)


ms = [3,4,1,2,6]
st = quickSort(ms)
print (st)