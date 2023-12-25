import os
import hashlib
import sympy
import random
import cv2

def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    hash_digest = sha256.digest()
    hash_int = int.from_bytes(hash_digest, byteorder='big')
    
    next_prime = sympy.nextprime(hash_int)

    return next_prime


def normalize_fingerprint_image(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(grayscale_image, (5,5), 0)
    thresholded_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)[1]
    return thresholded_image



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def generate_key_pair(p, q):
    if not (sympy.isprime(p) and sympy.isprime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
   
    cipher = [pow(ord(char), key, n) for char in plaintext]
    
    return cipher


def decrypt(pk, ciphertext):
    
    key, n = pk
    
    aux = [str(pow(int(char), key, n)) for char in ciphertext]

    # print(aux)

    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)