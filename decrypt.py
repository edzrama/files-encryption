import os
from cryptography.fernet import Fernet


class Decrypt:
    def __init__(self, key_path, file_list, secret):
        self.key_path = key_path
        self.file_list = file_list
        self.secret = secret

    def decrypt_files(self):
        # read the binary key
        with open(self.key_path, "rb") as secret_key:
            binary_key = secret_key.read()
            user_input = None
        # check if secret phrase match the user input
        while self.secret != user_input:
            user_input = input("Input the secret phrase to decrypt files:\n")
            if self.secret == user_input:
                # decrypt all the files in chosen directory
                for file in self.file_list:
                    with open(file, "rb") as file_to_decrypt:
                        contents = file_to_decrypt.read()
                    contents_decrypted = Fernet(binary_key).decrypt(contents)
                    with open(file, "wb") as file_to_decrypt:
                        file_to_decrypt.write(contents_decrypted.strip())
                print("Files has been decrypted successfully")
            else:
                print("Wrong Phrase, try again!")
