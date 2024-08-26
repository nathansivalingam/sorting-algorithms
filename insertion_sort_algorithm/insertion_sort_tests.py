# TESTS
tests = []

# Pseudo-randomly ordered array
tests.append ({
    'input': [2, 8, 5, 3, 9, 4],
    'output': [2, 3, 4, 5, 8, 9]
})

# Array already in increasing order
tests.append ({
    'input': [2, 3, 4, 5, 8, 9],
    'output': [2, 3, 4, 5, 8, 9]
})

# Array in decreasing order
tests.append ({
    'input': [9, 8, 5, 4, 3, 2],
    'output': [2, 3, 4, 5, 8, 9]
})

# Array containing negative numbers
tests.append ({
    'input': [2, 8, 5, -3, 9, 4],
    'output': [-3, 2, 4, 5, 8, 9]
})

# Array containing non-integer numbers
tests.append ({
    'input': [2, 8.5, 5, 3, 9, 4],
    'output': [2, 3, 4, 5, 8.5, 9]
})

# Empty array
tests.append ({
    'input': [],
    'output': -1
})

# Array with one element
tests.append ({
    'input': [2],
    'output': [2]
})

# Array with duplicate numbers
tests.append ({
    'input': [2, 5, 5, 3, 5, 4],
    'output': [2, 3, 4, 5, 5, 5]
})