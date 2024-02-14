def duplicate_list():
    '''
    This function is to filter duplicate elements without using builtin function
    '''
    list_1 = [1,2,1,2,3,4,5,6]
    list_2 = []
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    print(list_2)

def using_set():
    '''
    This function is to filter duplicate elements using set
    '''
    list_1 = [1,2,1,2,3,4,5,6]
    set_1 = set(list_1)
    print(set_1)

if __name__ == '__main__':
    duplicate_list()
    using_set()