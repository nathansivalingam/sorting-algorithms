# Selection Sort Algorithm
## 1. State the problem clearly. Identify the input & output formats.
Sort an array of data to be in increasing order. The algorithm must have a worst-case time complexity of O(n^2)

Input:
- Array of numbers.

Output
- The same array of numbers organised into increasing order.

## 2. Come up with some example inputs & outputs. Try to cover all edge cases.
Expected Case:
- Pseudo-randomly ordered array
- Array already in increasing order
- Array in decreasing order
- Array containing negative numbers
- Array containing non-integer numbers

Edge Cases:
- Empty array
- Array with one element
- Array with duplicate numbers

## 3. Come up with a solution for the problem. State it in plain English.
Selection Sort

## 4. Implement the solution and test it using example inputs. Fix bugs, if any.
    def selection_sort_algo(data):
        if len(data) == 0:
            return -1
        else:
            i = 0
            while i < len(data):
                
                cur_min = i
                cur_item = i
                while cur_item < len(data):
                    if data[cur_item] < data[cur_min]:
                        cur_min = cur_item        
                    cur_item+=1 # 1
                
                # Swaps
                tmp = data[i]
                data[i] = data[cur_min]
                data[cur_min] = tmp

                i+=1
            return data

## 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
- The worst-case time complexity of insertion sort is O(n^2).
- Other sorting algorithms such as merge sort are more efficient, however, this sorting algorithm runs well for on small amounts of data.

## 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
Next steps:
- Try and create a visualizer to help others understand selection sort.
- Maybe it would highlight which lines of code are being run adjacents to a visual aid.