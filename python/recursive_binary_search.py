def recursiveBinarySearch(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) //2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursiveBinarySearch(list[midpoint+1:], target)
            else:
                return recursiveBinarySearch(list[:midpoint-1], target)

def verify(result):
    print('Target Found : ', result)

number = [1,2,3,4,5,6,7,8,9,10]
result = recursiveBinarySearch(number, 10)
verify(result)