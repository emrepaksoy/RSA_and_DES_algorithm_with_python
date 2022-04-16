import random


class RsaAlgorithm:
    def __init__(self):
        self.L_clear = 0
        self.L_cipher = 0

    def encrypt(self, message, num_n, num_e):

        self.L_clear = self.find_the_number_of_digits(num_n) - 1
        self.L_cipher = self.find_the_number_of_digits(num_n)
        ascii_message = []

        for i in message:
            ascii_message.append(self.ascii(i))

        for i in range(0, len(ascii_message)):
            ascii_message[i] = self.set_zero(str(ascii_message[i]), 3)

        message_with_zero = ""

        for i in range(0, len(ascii_message)):
            message_with_zero += ascii_message[i]

        blocks_list = self.text_shredding(message_with_zero)

        encryted_text = []

        for i in blocks_list:
            encryted_text.append(pow(int(i), num_e) % num_n)

        for i in range(0, len(encryted_text)):
            encryted_text[i] = self.set_zero(encryted_text[i], self.L_cipher)

        text = ""
        for i in encryted_text:
            text += i

        return text

    def decrypt(self, enrcypted_text, num_n, num_d):
        print("******************")
        blocks = []
        text_blocks = ""
        counter = 0

        for i in range(0, len(enrcypted_text)):
            if counter != self.L_cipher:
                text_blocks += enrcypted_text[i]
                counter += 1
            if counter == self.L_cipher:
                blocks.append(text_blocks)
                counter = 0
                text_blocks = ""

        for i in range(0, len(blocks)):
            blocks[i] = pow(int(blocks[i]) % num_n, num_d) % num_n

        for i in range(0, len(blocks)):
            blocks[i] = self.set_zero(blocks[i], self.L_clear)

        txt = ""

        for i in blocks:
            txt += i

        decrypted_text_blocks = []
        txt_block = ""

        for i in range(0, len(txt)):
            if counter != 3:
                txt_block += txt[i]
                counter += 1
            if counter == 3:
                decrypted_text_blocks.append(txt_block)
                counter = 0
                txt_block = ""

        for i in range(0, len(decrypted_text_blocks)):
            decrypted_text_blocks[i] = chr(int(decrypted_text_blocks[i]))

        decrypted_text = ""

        for i in decrypted_text_blocks:
            decrypted_text += i

        return decrypted_text

    def text_shredding(self, encryted_text):
        blocks = []
        text = ""
        counter = 0

        for i in range(0, len(encryted_text)):
            if counter != self.L_clear:
                text += encryted_text[i]
                counter += 1
                if counter == self.L_clear:
                    blocks.append(text)
                    counter = 0
                    text = ""

        if len(text) != 0 and len(text) < self.L_clear:
            blocks.append(text)
        counter2 = len(blocks[-1])
        while counter2 != self.L_clear:
            blocks[-1] += "0"
            counter2 += 1
        return blocks

    def set_zero(self, ascii_char, number_of_digits):
        num = str(ascii_char)
        while self.find_the_number_of_digits(ascii_char) < number_of_digits:
            num = "0" + str(num)
            number_of_digits -= 1
        return num

    def ascii(self, char):
        ascii_code = ord(char)
        return ascii_code

    def find_the_number_of_digits(self, number):
        numberofdigits = 1
        x = 1
        while int(int(number) / x) > 9:
            x *= 10
            numberofdigits += 1
        return numberofdigits



