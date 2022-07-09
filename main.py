import os
from encrypt import Encrypt
from decrypt import Decrypt

file_paths = []
secret_phrase = "[SECRET_PHRASE_FOR_DECRYPTION]"
# Make sure to try it on a test folder first, I'm not responsible if you end up losing your files during encryption
path = "[DIRECTORY_OF_FILES_TO_ENCRYPT]\\"
key_file = f"{path}binary_key.key"

# get all files inside the directory and subdirectories
for subdir, dirs, files in os.walk(path):
    for file in files:
        if os.path.join(subdir, file) == key_file:
            continue
        file_paths.append(os.path.join(subdir, file))
encrypt = Encrypt(key_path=key_file, file_list=file_paths)
decrypt = Decrypt(key_path=key_file,file_list=file_paths,secret=secret_phrase)

run_it = True
while run_it:
    answer = input('What do you want to do? (Encrypt/ Decrypt/ Exit)\n').lower()
    if answer == "encrypt":
        encrypt.encrypt_files()
    elif answer == "decrypt":
        decrypt.decrypt_files()
    elif answer == "exit":
        run_it = False
    else:
        print("Wrong Input")









