# Test-Related Imports
import time
import merge_sort_tests
tests = merge_sort_tests.tests

# Merge Sort Algorithm (O(n log n))
def mergesort(data, left, right): 
    if left < right:
        mid = (left + right) // 2
        mergesort(data, left, mid)
        mergesort(data, mid + 1, right)
        merge(data, left, mid, right)

def merge(data, left, mid, right):
    # UP TO HERE
    return -1

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
        actual_output = mergesort(data, 0, len(data) - 1)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed")
            print(f"     Input: {data}\n     Expected Output: {expected_output}\n     Actual Output: {actual_output}{RESET}")
    
    # End Timer
    end_time = time.time()
    print(f"Test run time: {round(((end_time - start_time) * 1000), 4)} ms")