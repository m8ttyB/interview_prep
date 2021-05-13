#!/usr/bin/env python


# recursive binary search using array slices
def binary_search_with_slices(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search_with_slices(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx + 1:]
    result = binary_search_with_slices(right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1


# recursive binary search using pointers
def binary_search_with_pointers(sorted_list, left_pointer, right_pointer, target):
    # indicates an empty sub-list
    if left_pointer >= right_pointer:
        return "value not found"

    # calculate the mid point using the pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # if value is to the left of mid_idx
        return binary_search_with_pointers(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # if value is to the right of mid_idx
        return binary_search_with_pointers(sorted_list, mid_idx + 1, right_pointer, target)
    

# For testing:
line = '-' * 5

# binary search using array slices
print(line + ' binary search using array slices ' + line)
sorted_values = [13, 14, 15, 16, 17]
print(binary_search_with_slices(sorted_values, 16))

sorted_values = [1, 11, 13, 15, 16, 19, 100]
print(binary_search_with_slices(sorted_values, 2))

# binary search using pointers
print(line + ' binary search using pointers ' + line)
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search_with_pointers(values, start_of_values, end_of_values, 288)
print("element {0} is located at index {1}".format(288, result))

result = binary_search_with_pointers(values, start_of_values, end_of_values, 1500)
print(result)

# binary search with while loop, using pointers
def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list) - 1

  while left_pointer <= right_pointer:
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if target < mid_val:
        right_pointer = mid_idx - 1
    if target > mid_val:
        left_pointer = mid_idx + 1
  
  return "Value not found"
  
print(line + ' binary search with while loop ' + line)
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))