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

# Brute Force Position (For Loop)
def locate_position_iterative(data, number):
    print(data, number)
    for i in data:
        if i == number:
            return data[i]
    return -1

# BST SEARCH FUNCTION
def locate_position(data, number):
    
    pass

# MAIN FUNCTION
if __name__ == "__main__":
    for i in tests:
        data = i['input']['data']
        number = i['input']['number']
        expected_output = i['output']
        actual_output = locate_position_iterative(data, number)

        if expected_output == actual_output:
            print('Test Passed')
        else:
            print('Test Failed')