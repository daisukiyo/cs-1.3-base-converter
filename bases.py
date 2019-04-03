#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)

    if base == 2:
        listed_digits = list(map(int, digits))
        sum = 0
        power = len(listed_digits) - 1
        for i in listed_digits:
            sum += (i * (2 ** power))
            power -= 1
        return(sum)

    # TODO: Decode digits from hexadecimal (base 16)
    elif base == 16:
        listed_digits = list(digits)
        sum = 0
        power = len(listed_digits) - 1
        for i in listed_digits:
            sum += (string.hexdigits.index(i) * (16 ** power))
            power -= 1
        return(sum)

    # TODO: Decode digits from any base (2 up to 36)
    else: 
        listed_digits = list(digits)
        sum = 0
        power = len(listed_digits) - 1
        for i in listed_digits:
            sum += (string.printable.index(i) * (base ** power))
            power -= 1
        return(sum)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # TODO: Encode number in binary (base 2)
    if base == 2: 
        int_num = int(number)
        split_encoding = []
        while int_num >= 1:
            split_encoding.append(int(int_num % 2))
            int_num = int_num/2
        merge_list = ("".join(map(str, split_encoding)))
        print(split_encoding)
        print("merge")
        print(merge_list)
        return((merge_list)[::-1])
            
    # TODO: Encode number in hexadecimal (base 16)
    elif base == 16: 
        int_num = int(number)
        split_encoding = []
        while int_num >= 1: 
            if int(int_num % 16) >= 10:
                split_encoding.append(string.hexdigits[int(int_num % 16)])
            else:
                split_encoding.append(int(int_num % 16))
            int_num = int_num/16
        converted_encoding = (list(map(str, split_encoding)))
        return("".join(converted_encoding[::-1]))

    # TODO: Encode number in any base (2 up to 36)
    else:
        int_num = int(number)
        split_encoding = []
        while int_num >= 1: 
            if int(int_num % base) >= 10:
                split_encoding.append(string.printable[int(int_num % base)])
            else:
                split_encoding.append(int(int_num % base))
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
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    if base1 == 2 and base2 == 16:
        return(encode(decode(digits, 2), 16))
    elif base1 == 16 and base2 == 2:
        return(encode(decode(digits, 16), 2))
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    elif base1 == 2 and base2 == 10:
        return(str(decode(digits, 2)))
    elif base1 == 10 and base2 == 2:
        return(encode(int(digits), 2))
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    elif base1 == 10 and base2 == 16:
        return(encode(int(digits), 16))
    elif base1 == 16 and base2 == 10:
        return(str(decode(digits, 16)))
    # TODO: Convert digits from any base to any base (2 up to 36)
    else:
        return(encode(decode(digits, base1), base2))


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