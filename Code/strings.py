#!python

def contains(text: str, pattern: str, start=0) -> bool:
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Iterative

    # ! Runtime = O(n), n is len of text. Text must be iterated over. 

    # case: pattern length is greater than text
    if len(pattern) > len(text):
        return False
    # case: pattern is empty
    if pattern == '' or "":
        return True

    # no need to check the rest of text if pattern length exceeds remainder
    for index in range(start, len(text) - len(pattern) + 1):
        # case: check if first letter of pattern exists in text
        if text[index] == pattern[0]:
            # A slice of text that is the length of pattern starting from text[i] to check if the remaining pattern follows after text[i]
            rest = text[index: index + len(pattern)]
            if rest == pattern:
                return True
    # case: pattern not in text
    return False

def find_index(text: str, pattern: str, start=0) -> (int, None):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Iterative

    # ! Runtime = O(n), n is len of text. Text must be iterated over.

    # case: empty string
    if len(pattern) == 0:
        return 0
    
    # case: pattern is text
    if pattern == text:
        return 0

    # case: len pattern > len text
    if len(pattern) > len(text):
        return None

    # case: len pattern >= 1
    for index in range(start, len(text) - len(pattern) + 1):
        if text[index] == pattern[0]:
            rest = text[index: index + len(pattern)]
            if rest == pattern:
                return index
                    
    # case: pattern not in text
    return None

def find_all_indexes(text: str, pattern: str,start=0) -> [int]:
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Recursive

    # Runtime = O(n + m), n being the len of text in find_index and m being the len text in recursive call of find_index 

    # case: pattern = text
    if pattern == text:
        return [0]
    
    # case: pattern is empty
    if pattern == "" or '':
        return [index for index in range(len(text))]

    output = list()
    found_index = find_index(text,pattern)

    # while there is a found_index
    while found_index != None:
        # append found_index
        output.append(found_index)
        # recursion: update found_index by incrementing by 1s
        found_index = find_index(text, pattern, found_index + 1)  
    return output

# def test_string_algorithms(text, pattern):
    # found = contains(text, pattern)
    # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    # index = find_index(text, pattern)
    # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    # print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
    pass


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
