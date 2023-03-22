#Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
#All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

def ips_between(start, end):
    start, end, diff = start.split('.'), end.split('.'), []
    for i in range(4):
        diff.append(int(end[i])-int(start[i]))
    difference = diff[0]*256**3+diff[1]*256**2+diff[2]*256**1+diff[3]*256**0
    return difference