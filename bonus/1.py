# Code for recursive algorithm
def recursive_bsearch(lst, el):

    #Check if the list is empty; if it is, return False
    if len(lst) == 0:
        return False

    else:
        #Define a variable called mid and set it equal to the index of the middle element in the list
        mid = len(lst) // 2

        #Check if the middle element's value is equal to the desired value; if it is, return True
        if lst[mid] == el:
            return True

        else:
            #Check if the desired value is less than the middle element's value; if it is, call the function again
            if el < lst[mid]:
                return recursive_bsearch(lst[:mid], el)
            else:
                return recursive_bsearch(lst[mid + 1], el)


# Test code:
test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(recursive_bsearch(test_list, 1))
print(recursive_bsearch(test_list, 5))
print(recursive_bsearch(test_list, 0))