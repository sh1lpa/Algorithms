from utility import get_list, verify

target = eval(input('Enter a target : '))

def linear_search(list):
    '''
    Returns the index position of target element if found else returns None
    '''
    for i,val in enumerate(list):
        if val == target:
            return i
    return None

verify(linear_search(get_list()))