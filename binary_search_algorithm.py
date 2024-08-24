# TESTS
tests = []
# Middle of the array
tests.append ({
    'input': {
        'data': [8, 7, 6, 5, 4, 3, 2, 1, 0],
        'number': 4
    },
    'output': 4
})

# Start of the array
tests.append ({
    'input': {
        'data': [8, 7, 6, 5, 4, 3, 2, 1, 0],
        'number': 8
    },
    'output': 0
})

# End of the array
tests.append ({
    'input': {
        'data': [8, 7, 6, 5, 4, 3, 2, 1, 0],
        'number': 0
    },
    'output': 8
})

# Single Element Array
tests.append ({
    'input': {
        'data': [7],
        'number': 7
    },
    'output': 0
})

# Array does not contain the number
tests.append ({
    'input': {
        'data': [8, 7, 6, 5, 4, 3, 2, 1, 0],
        'number': 9
    },
    'output': -1
})

# Empty Array
tests.append ({
    'input': {
        'data': [],
        'number': 4
    },
    'output': -1
})

# Array Contains Duplicate Numbers 
tests.append ({
    'input': {
        'data': [8, 7, 7, 5, 4, 4, 2, 1, 0],
        'number': 5
    },
    'output': 3
})

# The number appears in more than one position 
tests.append ({
    'input': {
        'data': [8, 7, 6, 5, 4, 4, 2, 1, 0],
        'number': 4
    },
    'output': 4 # Returns First Occurence of the Number
})

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
        
        # Binary Search Tree Function
        bst_actual_output = bst_search_algo(data, number)
        
        if expected_output == bst_actual_output:
            print(f"{GREEN} BST Test Passed{RESET}")
        else:
            print(f"{RED} BST Test Failed{RESET}")
