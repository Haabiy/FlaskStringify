def remove_null(cat_string):
    """This function takes a string of comma-separated values (cat_string) and removes any occurrences of 'NULL'.
    
    Parameters:
    cat_string (str): A string containing comma-separated values.
    
    Returns:
    str: A string with 'NULL' values removed, joined by commas.
    """
    # Split the input cat_string into a list of substrings using the comma as a delimiter
    substrings = cat_string.split(',')
    # Create a new list containing only the substrings that are not equal to 'NULL'
    filtered_substrings = [sub for sub in substrings if sub != 'NULL']
    # Join the filtered substrings back into a single string using the comma as a delimiter
    removed_null = ','.join(filtered_substrings)
    return removed_null

def reverse_substrings(cat_string):
    """This function takes a string of comma-separated values (cat_string) and reverses the order of substrings.
    
    Parameters:
    cat_string (str): A string containing comma-separated values.
    
    Returns:
    str: A string with substrings reversed, joined by commas.
    """
    substrings = cat_string.split(',')
    reversed_substrings = reversed(substrings)
    reversed_str = ','.join(reversed_substrings)
    return reversed_str

def find_missing_number(l):
    """This function finds the missing number in a list of consecutive numbers from 1 to n.
    
    Parameters:
    l (list): A list of consecutive numbers with one missing number.
    
    Returns:
    int: The missing number in the list.
    """
    # Calculate the expected sum of numbers from 1 to n
    n = len(l) + 1
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of numbers in the list
    actual_sum = sum(l)
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    return missing_number

