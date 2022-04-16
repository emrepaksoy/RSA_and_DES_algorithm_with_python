import hashlib
from RSA_Algorithm import *
from utils import *

def main_hash():
    print("\n****** digital sign ******")
    while True:
        num_p = int(input("p:"))
        num_q = int(input("q:"))

        if not (is_prime(num_p) and is_prime(num_q)):
            print("enter prime number !")
        elif num_p == num_q:
            print("p and q is not equal")
        else:
            break
    text = input("text :")

    num_n, num_e, num_d = find_numbers(num_p, num_q)

    result = hashlib.md5(text.encode())
    a = result.hexdigest()
    print("hashed text: " + str(a))

    obje1 = RsaAlgorithm()
    digital_signature = obje1.encrypt(a, num_n, num_d)
    print("digital sign :" + str(digital_signature))
    decrypted_signature = obje1.decrypt(digital_signature, num_n, num_e)
    print("decryted digital sign : " + str(decrypted_signature))
    print("hashed text : " + str(a))


main_hash()
