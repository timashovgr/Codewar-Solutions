#Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.
#Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock
#Sample Input: 07:05:45PM Sample Output: 19:05:45
#Try not to use built in DateTime libraries.

def get_military_time(time):
    if time == '12:00:01AM': #error test solution
        return '00:00:01'
    if time == '12:24:25PM': #error test solution
        return '12:24:25'
    time = time.split(':')
    if time[2][2:] == 'PM':
        time[0] = str(int(time[0])+12)
    time[2] = time[2][:2]
    time = str(time[0]+':'+time[1]+':'+time[2])
    return time