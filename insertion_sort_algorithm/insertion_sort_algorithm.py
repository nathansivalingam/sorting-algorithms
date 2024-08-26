# Test-Related Imports
import time
import insertion_sort_tests
tests = insertion_sort_tests.tests

# Bubble Sort Algorithm (O(n^2))
def insertion_sort_algo(data):
    if len(data) == 0:
        return -1
    else:
        i = 1
        while i < len(data):
            j = i
            while j > 0 and data[j-1] > data[j]:
                tmp = data[j]
                data[j] = data[j-1]
                data[j-1] = tmp
                j-=1
            i+=1
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
        actual_output = insertion_sort_algo(data)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed")
            print(f"     Input: {data}\n     Expected Output: {expected_output}\n     Actual Output: {actual_output}{RESET}")
    
    # End Timer
    end_time = time.time()
    print(f"Test run time: {round(((end_time - start_time) * 1000), 4)} ms")