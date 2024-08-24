## 1. State the problem clearly. Identify the input & output formats.
Find the position of a given number in a list of numbers arranged by decreasing order. The list must be accessed a minimum number of times.

Input: 
- An array of data arranged in decreasing order.
- A number in the array whose position needs to be determined.

Output:
- The position in the array where the input number was being kept.

## 2. Come up with some example inputs & outputs. Try to cover all edge cases.
Variations:
- The number is the in the middle of the array.
- The number is the first element in the array.
- The number is the last element in the array.

Edge Cases:
- The array is just one element.
- The array does not contain the number.
- The array is empty.
- The array contains duplicate numbers. 
- The number occurs at more than one position in the array (repeating numbers).

## 3. Come up with a solution for the problem. State it in plain English.
Brute Force Solution
- Start at the first element.
- Loop through the entire array.
- Print the position of the number once it has been found in the array.

## 4. Implement the solution and test it using example inputs. Fix bugs, if any.
### Brute Force Linear Search Function (O(n))
    def linear_search_algo(data, number):
        i = 0
        while i < len(data):
            if data[i] == number:
                return i
            i+=1
        return -1

## 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
The linear search algorithm has a time complexity of O(n).
By using a binary search algorithm, the time complexity can be reduced to O(log n).

## 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
### Binary Search Tree Function (O(log n))
    def bst_search_algo(data, number):
        left = 0
        right = len(data) - 1

        while (left <= right):
            mid = (right + left) // 2
            if data[mid] == number:
                return mid
            elif data[mid] > number:
                left = mid + 1
            else:
                right = mid - 1
        return -1