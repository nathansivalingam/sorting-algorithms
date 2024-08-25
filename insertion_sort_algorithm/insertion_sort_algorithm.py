# Test-Related Imports
import insertion_sort_tests
tests = insertion_sort_tests.tests

# Bubble Sort Algorithm (O(n^2))
def insertion_sort_algo(data):
    pass

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
        actual_output = insertion_sort_algo(data)

        if expected_output == actual_output:
            print(f"{GREEN} Test Passed{RESET}")
        else:
            print(f"{RED} Test Failed{RESET}")