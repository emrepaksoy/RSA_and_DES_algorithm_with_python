import random

def permutation(inp, permutation_box, length):
    """
        :param inp:str: value to be permuted
        :param permutation_box:list: permutation value list
        :param length:int: length of the permuted inp

        :return permuted:str: permuted inp
    """
    permuted = ""
    for i in range(0, length):
        permuted = permuted + inp[permutation_box[i] - 1]

    return permuted


def shift_left(key, shift_value):
    """
      :param key:str: The key value that will be shifted
      :param shift_value:int: how much will it be shifted to the left

      :return shifted_key:str: left shifted key value
    """
    return key[shift_value:] + key[0: shift_value]


def xor(value1, value2):
    output = ""
    for idx in range(len(value1)):
        output += str(int(value1[idx] != value2[idx]))

    return output


def ascii2bin(char):
    """
        :param char: character
        :return binary_value:str: binary equal of the char
    """
    ascii_number = ord(char)
    binary_value = bin(ascii_number)
    return binary_value[2:]


def _8bits_binary(binary_value):
    """
        :param binary_value:str
        :return: the 8 bits binary value
    """
    return "0" * (8 - len(binary_value)) + binary_value


def _4bits_binary(binary_value):
    """
        :param binary_value:str
        :return: the 4 bits binary value
    """
    return "0" * (4 - len(binary_value)) + binary_value


def binary2ascii(binary_value):
    if binary_value == "0" * 8:
        return ""
    return chr(int("0b" + binary_value, 2))


def get_binary_message(message):
    """
        :param message: string or text
        :return: binary equal of the message
    """
    binary_message = ""

    for i in message:
        binary = ascii2bin(i)
        binary = _8bits_binary(binary)

        binary_message += binary

    return binary_message


def get_ascii_message(binary):
    message = ""
    for idx in range(0, len(binary), 8):
        char = binary2ascii(binary[idx: idx + 8])
        message += char

    return message


def coprime(number1, number2):
    if number1 < number2:
        small = number1
    else:
        small = number2
    for i in range(2, small + 1):
        if number1 % i == 0 and number2 % i == 0:
            return False
    return True


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5)):
        if num % i == 0:
            return False
    return True


def find_the_number_e(phi):
    counter = 0
    e_numbers = []

    for i in range(2, phi):
        if coprime(i, phi):
            counter += 1
            e_numbers.append(i)
        if counter == 15:
            break
    e = random.choice(e_numbers)
    return e


def find_numbers(p_prime, q_prime):
    n = p_prime * q_prime
    fi = (p_prime - 1) * (q_prime - 1)
    e = find_the_number_e(fi)
    d = 1
    while True:
        if (e * d - 1) % fi == 0:
            break
        d += 1

    print("n :" + str(n))
    print("fi : " + str(fi))
    print("e public key  :" + str(e))
    print("d private key :" + str(d))

    return n, e, d

