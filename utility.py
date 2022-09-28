
def verify(index):
    if index is not None:
        print(f'target is found at {index}')
    else:
        print('Target Not found')

def get_list():
    l = [int(x) for x in input('Enter the list : ').split(' ')]
    return l


