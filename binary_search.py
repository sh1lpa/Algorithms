from utility import verify, get_list

target = eval(input('Enter a target : '))


def binary_search(l):
    first = 0
    last = len(l)-1
    while first <= last:
        midpoint = (first+last)//2
        if l[midpoint] == target:
            return midpoint
        elif l[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None


verify(binary_search(get_list()))