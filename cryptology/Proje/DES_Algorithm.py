
from utils import *
from Boxes import *
from utils import _4bits_binary


class DES:
    def __init__(self, keys):
        self.keys = keys

    def encrypt(self, _64bits_message):

        message = permutation(_64bits_message, initial_perm, 64)

        left = message[:32]
        right = message[32:]

        for idx in range(16):
            expanded_right = permutation(right, exp_d, 48)

            xor_right = xor(expanded_right, self.keys[idx])

            s_box_output = ""

            j = 0
            for i in range(0, len(xor_right), 6):
                row = xor_right[i] + xor_right[i+5]
                column = xor_right[i+1: i+5]
                row = int("0b" + row, 2)
                column = int("0b" + column, 2)

                s_box_out = s_boxes[j][row][column]

                j += 1

                s_box_out = bin(s_box_out)[2:]
                s_box_out = _4bits_binary(s_box_out)

                s_box_output += s_box_out

            s_box_output = permutation(s_box_output, per, 32)

            left = xor(left, s_box_output)

            if idx != 15:
                left, right = right, left

        combined_cipher = left + right

        cipher = permutation(combined_cipher, final_perm, 64)

        return cipher

    def text_encrypt(self, text):

        _64bits_text_list = []

        for idx in range(0, len(text), 64):
            txt = text[idx: idx+64]
            if len(txt) == 64:
                _64bits_text_list.append(txt)
            else:
                txt = txt + "0"*(64 - len(txt))
                _64bits_text_list.append(txt)

        cipher = ""

        for _64bits_text in _64bits_text_list:
            cipher += self.encrypt(_64bits_text)

        return cipher
