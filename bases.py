import string

# REFACTORED FUNCTION TO SUBMIT
def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    listed_digits = list(digits)
    # initialize the decoded value at 0
    decoded_value = 0
    # calculate the power of the rightmost digit
    power = len(listed_digits) - 1
    for i in listed_digits:
        # individual digit multiplied by the base to the digit's power
        decoded_digit = (string.printable.index(i) * (base ** power))
        # decoded digit is summation of each digit decoded
        decoded_value += decoded_digit
        # move to the digit on the right thus decreasing the power
        power -= 1
    # return
    return(decoded_value)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # convert the number of type string to an integer type
    int_num = int(number)
    # create an array to store each individual digit of the encoded vlaue
    split_encoding = []
    while int_num >= 1: 
        encoded_remainder = int(int_num % base)
        if encoded_remainder >= 10:
            string_constant_value = string.printable[encoded_remainder]
            split_encoding.append(string_constant_value)
        else:
            split_encoding.append(encoded_remainder)
        int_num = int_num/base
    converted_encoding = (list(map(str, split_encoding)))
    return("".join(converted_encoding[::-1]))


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # decoded the initial value
    decoded_digit = decode(digits, base1)
    # encode the decoded value to the expected base
    converted_value = encode(decoded_digit, base2)
    # return the converted value
    return(converted_value)


def main():
    """Read command-line arguments and convert given digits between bases."""
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