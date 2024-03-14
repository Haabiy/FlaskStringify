from simple_python.src import remove_null, reverse_substrings, find_missing_number

def test_remove_null():
    """This function tests the remove_null function with various test cases.
    
    It checks if the function correctly removes 'NULL' values from comma-separated strings.
    """
    try:
        # Test cases having NULL at different indices
        assert remove_null('2076,3B,19C,138D,NULL,NULL') == '2076,3B,19C,138D'
        assert remove_null('2076,3B,NULL,19C,138D,NULL') == '2076,3B,19C,138D'
        assert remove_null('NULL,2076,3B,19C,138D') == '2076,3B,19C,138D'
        assert remove_null('2076,3B,19C,138D,NULL') == '2076,3B,19C,138D'
        assert remove_null('2076,3B,19C,138D') == '2076,3B,19C,138D'
        assert remove_null('') == ''
        print("All test cases passed!")
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

def test_reverse_substrings():
    """This function tests the reverse_substrings function with various test cases.
    
    It checks if the function correctly reverses the order of substrings in a comma-separated string.
    """
    try: 
        # Test case 1: Basic test with non-empty string
        assert reverse_substrings('2076,3B,19C,138D') == '138D,19C,3B,2076'
        # Test case 2: String with multiple substrings
        assert reverse_substrings('A,B,C,D,E,F') == 'F,E,D,C,B,A'
        # Test case 3: String with one substring
        assert reverse_substrings('SingleSubstring') == 'SingleSubstring'
        # Test case 4: Empty string
        assert reverse_substrings('') == ''
        # Test case 5: String with empty substrings
        assert reverse_substrings(',,,') == ',,,'
        print("All test cases passed!")
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def test_find_missing_number():
    """This function tests the find_missing_number function with various test cases.
    
    It checks if the function correctly identifies the missing number in a list of consecutive numbers.
    """
    try:
        # Test case 1: Basic test with one missing number
        assert find_missing_number([8, 6, 3, 4, 2, 7, 1]) == 5
        # Test case 2: Basic test with one missing number (different order)
        assert find_missing_number([3, 1, 2, 5]) == 4
        # Test case 3: List with no missing numbers
        assert find_missing_number([1, 2, 3, 4, 5]) == 6
        # Test case 4: Empty list
        assert find_missing_number([]) == 1
        # Test case 5: List with all numbers missing
        assert find_missing_number([5, 4, 3, 2, 1]) == 6
        print("All test cases passed!")
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    test_remove_null()
    test_reverse_substrings()
    test_find_missing_number()