# Test-Related Imports
import time
import selection_sort_tests
tests = selection_sort_tests.tests

# Selection Sort Algorithm (O(n^2))
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
                cur_item+=1
            
            # Swaps
            tmp = data[i]
            data[i] = data[cur_min]
            data[cur_min] = tmp

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
        actual_output = selection_sort_algo(data)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed")
            print(f"     Input: {data}\n     Expected Output: {expected_output}\n     Actual Output: {actual_output}{RESET}")
    
    # End Timer
    end_time = time.time()
    print(f"Test run time: {round(((end_time - start_time) * 1000), 4)} ms")