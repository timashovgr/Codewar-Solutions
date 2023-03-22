# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst