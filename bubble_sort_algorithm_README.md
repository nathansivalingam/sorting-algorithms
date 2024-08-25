# Bubble Sort Algorithm
## 1. State the problem clearly. Identify the input & output formats.
Sort the numbers in increasing order.

Input:
- The array of numbers, called 'data'.

Output:
- The array of numbers in increasing order, called 'output'.

## 2. Come up with some example inputs & outputs. Try to cover all edge cases.
Variations:
- Pseudo-randomly ordered array
- Array already in increasing order
- Array in decreasing order
- Array that contains negative numbers

Edge Cases
- Array with duplicate numbers
- Array with one number in it
- Empty array

## 3. Come up with a solution for the problem. State it in plain English.
Bubble Sort

## 4. Implement the solution and test it using example inputs. Fix bugs, if any.
    def bubble_sort_algo(data):
        if len(data) == 0:
            return -1
        else:
            for i in range(1, len(data)):
                for j in range(0, len(data)-1):
                    if data[j] > data[j+1]:
                        tmp = data[j]
                        data[j] = data[j+1]
                        data[j+1] = tmp
            return data

## 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
- Bubble sort has a worst-case time complexity of O(n^2).
- This method of sorting is generally inefficient compared to other sorting algorithms such as merge-sort which has a worst-case time complexity of O (nlog(n)). 

## 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
Next Steps - Improve the program's efficiency by using merge sort.
