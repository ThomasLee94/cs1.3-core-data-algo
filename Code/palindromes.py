#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text: str) -> bool:
   # ! Runtime = O(n/2 + 2m)

    forward = 0
    backward = len(text) - 1

    while forward <= backward:
        # case: char not a letter
        while text[forward] not in string.ascii_letters:
            forward += 1
        # case: char not a letter
        while text[backward] not in string.ascii_letters:
            backward -= 1
        else:
            if text[forward].lower() != text[backward].lower():
                return False
            else:
                # continue loop
                forward += 1
                backward -= 1

    # case: loop completed without text[forward].lower() != text[backward].lower()
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text: str, forward=None, backward=None) -> bool:
    # init forward and backward
    if forward == None and backward == None:
        forward, backward = 0, len(text) - 1

    # case: recursion updates forward past backward
    if forward >= backward:
        return True

    # case: char not a letter
    if text[forward] not in string.ascii_letters:
        return is_palindrome_recursive(text,forward + 1, backward)
    if text[backward] not in string.ascii_letters:
        return is_palindrome_recursive(text, forward, backward - 1)

    if text[forward].lower() != text[backward].lower(): 
        return False
    
    # continue recursion 
    return is_palindrome_recursive(text, forward + 1, backward - 1)

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
