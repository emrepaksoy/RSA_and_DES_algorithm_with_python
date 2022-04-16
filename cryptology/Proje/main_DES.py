import random
from utils import *
from Boxes import *
from DES_Algorithm import DES


def _64bits_random_key_generate():
    key = "1"
    for _ in range(1, 64):
        key += str(random.randint(0, 1))
    return key


KEY = _64bits_random_key_generate()
KEY = permutation(KEY, key_per, 56)

left = KEY[:28]
right = KEY[28:]

rounded_keys = []  # rounded keys list

for i in range(16):
    left = shift_left(left, shift_table[i])
    right = shift_left(right, shift_table[i])

    combined_key = left + right

    rounded_key = permutation(combined_key, key_comp, 48)

    rounded_keys.append(rounded_key)

reversed_rounded_keys = rounded_keys[::-1]

des_encrypt = DES(rounded_keys)
des_decrypt = DES(reversed_rounded_keys)


def main():
    print("--------------------------- 64bits message --------------------------")
    text = "you are "  # 64bits text

    binary_text = get_binary_message(text)

    cipher = des_encrypt.encrypt(binary_text)

    print("Encrypted message of 'you are ': ", cipher)

    decrypted_cipher = des_decrypt.encrypt(cipher)

    print("Decrypted message in binary: ", decrypted_cipher)

    print("Decrypted message: ", get_ascii_message(decrypted_cipher))

    print("--------------------------- 3688bits message --------------------------")

    text2 = ""
    with open("text.txt", "r") as t:
        text2 = t.read()

    print(text2)

    binary_text = get_binary_message(text2)

    cipher = des_encrypt.text_encrypt(binary_text)

    print("Encrypted message of 'you are ': ", cipher)

    decrypted_cipher = des_decrypt.text_encrypt(cipher)

    print("Decrypted message in binary: ", decrypted_cipher)

    print("Decrypted message: ", get_ascii_message(decrypted_cipher))


if __name__ == "__main__":
    main()
