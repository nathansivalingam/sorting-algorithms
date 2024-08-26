# Test-Related Imports
import time
import bubble_sort_tests
tests = bubble_sort_tests.tests

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

    # Begin Timer
    start_time = time.time()
    
    # Test Iterations
    for test in tests:
        data = test['input']
        expected_output = test['output']
        actual_output = bubble_sort_algo(data)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed{RESET}")
    
    # End Timer
    end_time = time.time()
    print(f"Test run time: {round(((end_time - start_time) * 1000), 4)} ms")