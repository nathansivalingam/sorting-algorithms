nums = [-1, 0, 1, 4, 5]
target = 0

# Binary Search Algo
def binary_search_func(nums, target):
  left = 0
  right = len(nums) - 1
  while (left <= right):
    mid = (left + right) // 2

    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return 'number is not in array'

if __name__ == '__main__':
  value = binary_search_func(nums, target)
  print(value)