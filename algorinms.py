
def boobleSorts (ms):
    n = 1
    while n < len(ms):
        for i in range (len(ms)-n):
            if ms[i] > ms[i+1]:
                ms[i], ms[i+1] = ms[i+1], ms[i]
        n += 1
    return ms
#Test
ms = [3,4,1,2,6]
print(boobleSorts(ms))