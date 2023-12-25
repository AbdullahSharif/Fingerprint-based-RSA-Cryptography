import cv2

from utils import hash_data, gcd, encrypt, decrypt, normalize_fingerprint_image, multiplicative_inverse, generate_key_pair





if __name__ == "__main__":
    print(" ")


   

    while True:
        print("Choose the operation you want to perform:")
        print("1 - Generate Public & Private key pair")
        print("2 - Perform encryption using reciever's Public key")
        print("3 - Perform Decryption using your Private key")
        print("4 - To exit.")

        choice = int(input())

        if choice == 1:
            path_of_p = input("Enter the path of fingerprint image for p: ")
            path_of_q = input("Enter the path of fingerprint image for q: ")

            image_p = cv2.imread(path_of_p)
            image_q = cv2.imread(path_of_q)

            normalize_fingerprint_image_p = normalize_fingerprint_image(image_p)
            normalize_fingerprint_image_q = normalize_fingerprint_image(image_q)

            p = hash_data(normalize_fingerprint_image_p)
            q = hash_data(normalize_fingerprint_image_q)

            print(" - Generating your public / private key-pairs now . . .")

            public, private = generate_key_pair(p, q)


            with open("private_key.txt", 'w') as file:
                file.write(str(private))
            with open("public_key.txt", 'w') as file:
                file.write(str(public))

            print("Saved your public and private key to public_key.txt and private_key.txt respectively.\n")
        
        elif choice == 2:

            pub_key_file = input("Enter the path of your public key file: ")

            # read the key pair.

            with open(pub_key_file, 'r') as file:
                pub_key = file.read()
                pub_key = eval(pub_key)

            plain_text_file = input("Enter the file that you want to encrypt: ")

            with open(plain_text_file, 'r') as file:
                plain_text = file.read()

            encrypted_file = input("Enter the name you want to give to your encrypted file: ")
            encrypted_msg = encrypt(pub_key, plain_text)

            with open(encrypted_file, "w") as file:
                file.write(str(encrypted_msg))

            print("Encryption done successfully.\n")


        elif choice == 3:
            priv_key_file = input("Enter the path of your private key file: ")

            with open(priv_key_file, 'r') as file:
                priv_key = file.read()
                priv_key = eval(priv_key)

            cipher_text_file = input("Enter the file that you want to decrypt: ")

            with open(cipher_text_file, "r") as file:
                cipher_text = file.read()
                cipher_text = eval(cipher_text)
                # cipher_text = [int(x) for x in cipher_text]

            decrypted_file = input("What would you like to call your decrypted file: ")

            decrypted_msg = decrypt(priv_key, cipher_text)

            with open(decrypted_file, 'w') as file:
                file.write(decrypted_msg)

            print("Successfully decrypted your file.\n")

        elif choice == 4:
            print(" ")

            exit()
        else:
            print("No such option exist.\n")



