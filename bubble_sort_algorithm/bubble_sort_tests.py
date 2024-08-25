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