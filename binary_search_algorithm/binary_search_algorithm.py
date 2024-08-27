# Test-Related Imports
import binary_search_tests
tests = binary_search_tests.tests

# Brute Force Linear Search Function (O(n))
def linear_search_algo(data, number):
    i = 0
    while i < len(data):
        if data[i] == number:
            return i
        i+=1
    return -1

# Binary Search Tree Function (O(log n))
def bst_search_algo(data, number):
    
    left = 0
    right = len(data) - 1

    while (left <= right):
        mid = (right + left) // 2
        if data[mid] == number:
            return mid
        elif data[mid] > number:        # To deal with increasing arrays, flip the sign
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary Search Tree Function Recursive
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

# Main Function
if __name__ == "__main__":
    
    # Coloured Text Presets
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    
    # Test Iterations 
    for i in tests:
        data = i['input']['data']
        number = i['input']['number']
        expected_output = i['output']
        
        # Brute Force Linear Search Function
        lpi_actual_output = linear_search_algo(data, number)

        if expected_output == lpi_actual_output:
            print(f"{GREEN} LPI Test Passed{RESET}")
        else:
            print(f"{RED} LPI Test Failed{RESET}")
        
        # Binary Search Tree Function (Iterative)
        bst_actual_output = bst_search_algo(data, number)
        
        if expected_output == bst_actual_output:
            print(f"{GREEN} BST Test Passed{RESET}")
        else:
            print(f"{RED} BST Test Failed{RESET}")

        # Binary Search Tree Function (Recursive)
        bstr_actual_output = bstr_search_algo(data, 0, len(data) - 1, number)
        
        if expected_output == bstr_actual_output:
            print(f"{GREEN} BSTR Test Passed{RESET}")
        else:
            print(f"{RED} BSTR Test Failed{RESET}")
