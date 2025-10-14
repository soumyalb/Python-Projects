# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?
  
# low, high, mid
# low = 0
# high = n-1
# low<= high
# low+high/2  = mid
# list(mid) = target


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    
    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return f"Value {sorted_list[mid]} Found at index {mid}"
        
        if sorted_list[mid] < target:
            low = low + 1
        else:
            high = high - 1
            
    return "Not Found"

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11

result = binary_search(sorted_list, target)
print(result)
    
