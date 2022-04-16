from RSA_Algorithm import *
from utils import *


def main():
    print("********** RSA *********")
    while True:
        p = int(input("p:"))
        q = int(input("q:"))

        if not (is_prime(p) and is_prime(q)):
            print("enter prime number !")
        elif p == q:
            print("p and q is not equal")
        else:
            break

    txt = input("key :")

    n, e, d = find_numbers(p, q)

    obje = RsaAlgorithm()
    encrypted_text = obje.encrypt(txt, n, e)
    print("encryted key : " + str(encrypted_text))
    decrypted_text = obje.decrypt(encrypted_text, n, d)
    print("decryted key : " + str(decrypted_text))


main()
