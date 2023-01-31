# Code for iterative algorithm:
def binary_search(data, el):

    first = 0  #value of first index
    last = len(data) - 1  #value of last index
    found = False  #target el not initially found

    while first <= last and not found:
        mid = (first + last) // 2  #We use the '//' division operator so an integer value is returned; if we used '/', a floating point value would be returned.

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# Test code:
lst = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(lst, 12))
print(binary_search(lst, 11))
print(binary_search(lst, 5))