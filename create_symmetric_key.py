#######################################
#
#  Create symmetric key and store the key in credential manager
#  Prerequisite:
#  - install cryptography library
#  - install keyring module
#
#  Date: 2023-10-09
#
#######################################

# Import Fernet from Crypthography library, keyring and getpass
from cryptography.fernet import Fernet
import keyring
from getpass import getpass

#Create symmetric key and store in a keyring
sym_key = Fernet.generate_key()
keyring.set_password('SQLService','SymKey', sym_key.decode())
#print(sym_key)

# Request SQL password and encode
sql_password = getpass().encode()

#Encrypt the password with the symmetric key and store in a file
cipher_suite = Fernet(sym_key)
ciphered_text = cipher_suite.encrypt(sql_password)
with open('./mssql_pw_bytes.bin', 'wb') as file_object:  file_object.write(ciphered_text)
