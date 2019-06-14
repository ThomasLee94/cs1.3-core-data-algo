#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
# string.printable = '0123456789abcdefghijklmnopqrstuvwxyz'

def decode(digits: str, base: int) -> int:
    '''
    DIGITS IN GIVEN BASE -> DIGITS IN BASE10
    '''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    power = len(digits)
    output = 0
    for digit in digits:
        # INDEX() GIVES BACK INDEX OF THE DIGIT ACCORDING TO STRING.PRINTABLE
        power -= 1
        value_of_digit = string.printable.index(digit)
        output += (base ** power) * value_of_digit
    return output

def encode(number: int, base: int) -> str:
    '''
    GIVEN NUMBER (BASE10) -> DIGITS IN GIVEN BASE
    '''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    
    
    output = ""
    while number > 0:
        remainder = number % base
        # VALUE BY INDEX: 0 => '0', 1 => '1', 13 => 'd'
        digit_for_value = string.printable[remainder]
        # output = output + digit_for_value  # append new digit to right side of output string
        output = digit_for_value + output  # prepend new digit to left side of output string
        # ROUNDED DIVISION
        number = number // base
    return output

def convert(bits: str, base1: int, base2: int) -> str:
    '''
    GIVEN DIGITS IN BASE1 -> DIGITS IN BASE2
    '''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    # DECODE TO BASE1 - RETURNS BASE10 NUM
    decoded = decode(bits, base1)
    # ENCODE BASE10 NUM TO BASE2
    encoded = encode(decoded, base2)
    return encoded

def main():
    '''Read command-line arguments and convert given digits between bases.'''
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
    decode('c9',16)