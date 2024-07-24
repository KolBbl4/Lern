
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

ms = [3,4,1,2,6]
sortMs = boobleSorts(ms)
resul = BinarySearch(sortMs,5)
if resul:
    print('Есть такое число')
else:
    print('НЕТ')