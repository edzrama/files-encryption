from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self,key_path, file_list ):
        self.key_path = key_path
        self.file_list = file_list

    def encrypt_files(self):
        # read .key file
        try:
            with open(self.key_path, "rb") as secret_key:
                key = secret_key.read()
            # when file exist but is empty, assert error
            assert key != b''
        except (FileNotFoundError, AssertionError):
            # update/create key file when empty or not exist
            with open(self.key_path, "wb") as secret_key:
                # generate the key
                key = Fernet.generate_key()
                secret_key.write(key)
        finally:
            # encrypt all the files in chosen directory
            for file in self.file_list:
                with open(file, "rb") as file_to_encrypt:
                    contents = file_to_encrypt.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as file_to_encrypt:
                    file_to_encrypt.write(contents_encrypted)
            print('Files has been encrypted')