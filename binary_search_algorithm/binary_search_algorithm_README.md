# Binary Search Tree Algorithm
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

## 3. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
Using a recursive binary search tree algorithm has the same time complexity of O(log n).
However, while the resursive bst is easier to code/understand, it is less space efficient than the iterative bst algorithm.

    def bstr_search_algo(data, left, right, number):

        if left > right:
            return -1

        mid = (right + left) // 2

        if data[mid] == number:
            return mid
        elif data[mid] < number:
            return bstr_search_algo(data, left, mid - 1, number)
        else:
            return bstr_search_algo(data, mid + 1, right, number)

Resource: https://stackoverflow.com/questions/57481997/recursive-and-iterative-binary-search-which-one-is-more-efficient-and-why#:~:text=Focusing%20on%20space%20complexity%2C%20the,O(log%20n)%20space.&text=There%20is%20no%20different%20w.r.t%20Big%20O%20analysis%20between%20these%20two%20versions.

Next Steps:
- Finish up the merge sort algorithm and get to testing.