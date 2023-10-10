import keyring

from cryptography.fernet import Fernet
# key = b'8uwIxhzc4Sre887Y0w4j_jNoKpU_ZyVLIcJHSr9lm0k='

#keyring.set_password('auth_key','Key','8uwIxhzc4Sre887Y0w4j_jNoKpU_ZyVLIcJHSr9lm0k=')

auth_key = keyring.get_password('auth_key', 'Key')

print(auth_key)

cipher_suite = Fernet(str(auth_key))

with open('./mssqltip_bytes.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = (cipher_suite.decrypt(encryptedpwd))

plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string

print(plain_text_encryptedpassword)