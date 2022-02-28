def mergeSort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list 

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    combine: Merge the sorted sublist created in previous step

    Takes overall O(n log n) time
    """

    if len(list) <= 1:
        return list

    left_half , right_half = split(list)
    left = mergeSort(left_half)
    right = mergeSort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merge 2 lists (arrays), sorting them in the process
    Returns a new merged list

    Takes in overall O(n) time
    """

    l = []
    # left indexes
    i = 0
    # right indexes
    j = 0

    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verifySorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verifySorted(list[1:])


samLists = [22,3,44,6,45,87,90,34,65,12]
l = mergeSort(samLists)
print(verifySorted(l))
print(verifySorted(samLists))