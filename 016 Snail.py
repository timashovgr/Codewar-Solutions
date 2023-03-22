#Snail Sort
#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

def snail(snail_map):
    snail_road = []
    n1 = 0
    n = len(snail_map)
    if snail_map == [[]]:
        return [] 
    for k in range(n-1):
        for j in range(n1, n-1-n1):
            i = n1
            snail_road.append(snail_map[i][j])
        for i in range(n1, n-1-n1):
            j = n-1-n1
            snail_road.append(snail_map[i][j])
        for j in range(n-1-n1, n1, -1):
            i = n-1-n1
            snail_road.append(snail_map[i][j])
        for i in range(n-1-n1, n1, -1):
            j = n1
            snail_road.append(snail_map[i][j])
        n1 += 1
    if n%2 != 0:
        snail_road.append(snail_map[n//2][n//2]) 
    return snail_road