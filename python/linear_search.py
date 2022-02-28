def linearSearch(list, target):
    """
        Returns the index position of the target if found, else returns None
    """
    # 
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Targe found in index: ', index)
    else:
        print('Target not found')

number = [1,2,3,4,5,6,7,8,9,10]
result = linearSearch(number, 12)
verify(result)

number = [1,2,3,4,5,6,7,8,9,10]
result = linearSearch(number, 6)
verify(result)