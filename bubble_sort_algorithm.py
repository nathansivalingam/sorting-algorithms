# TESTS
tests = []

# Pseudo-randomly ordered array
tests.append ({
    'input': [2, 8, 5, 3, 9, 4, 1],
    'output': [1, 2, 3, 4, 5, 8, 9]
})

# Array already in increasing order
tests.append ({
    'input': [1, 2, 3, 4, 5, 8, 9],
    'output': [1, 2, 3, 4, 5, 8, 9]
})

# Array in decreasing order
tests.append ({
    'input': [9, 8, 5, 4, 3, 2, 1],
    'output': [1, 2, 3, 4, 5, 8, 9]
})

# Array that contains negative numbers
tests.append ({
    'input': [2, -8, 5, 3, 9, 4, 1],
    'output': [-8, 1, 2, 3, 4, 5, 9]
})

# Array with duplicate numbers
tests.append ({
    'input': [2, 8, 5, 3, 9, 3, 1],
    'output': [1, 2, 3, 3, 5, 8, 9]
})

# Array with one number in it
tests.append ({
    'input': [2],
    'output': [2]
})

# Empty array
tests.append ({
    'input': [],
    'output': -1
})

# Bubble Sort Algorithm (O(n^2))
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

# Main Function 
if __name__ == "__main__":
    
    # Coloured Text Presets
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    
    # Test Iterations
    for test in tests:
        data = test['input']
        expected_output = test['output']
        actual_output = bubble_sort_algo(data)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed{RESET}")