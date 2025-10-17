def parity_multiplication(list_of_nums):
    '''
    Multiply values in a list of numbers based on their parity.

    Args:
    list_of_nums(list): A list containing numbers which are idealy whole.

    Returns:
    result(list): A list containing multiplied numbers.
    '''
    return [num * 2 if num % 2 == 0 else num * 3 for num in list_of_nums]  # Checks the remainder to see if the number is even or odd

def mixed_case_concatenation(list_of_words):
    '''
    Make a mixed case sentence where words length five or more are upper case and rest are lower case.

    Args:
    list_of_words(list): A list containing words/strings.

    Returns:
    phrase.strip(string): A long string which is a large mixed case sentence.
    '''
    phrase = ""
    try:
        new_list = [word.upper() + " " if len(word) > 5 else word.lower() + " " for word in list_of_words]  # Makes words all upper or lower case based on their length
        for word in new_list:
            phrase += word
    except TypeError:
        print(f"Your list must contain String values only")
    return phrase.strip()


def script_logic():
    '''
    Test the functions parity_multiplication and mixed_case_concatenation.

    Retruns:
    Two print statements.
    '''
    number_list = [1, 2, 3, 4, 5, 6, 7]
    fruit_list = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    print(f"Processed Numbers: {parity_multiplication(number_list)}")
    print(f"Processed Strings: {mixed_case_concatenation(fruit_list)}")


if __name__ == "__main__":
    script_logic()
