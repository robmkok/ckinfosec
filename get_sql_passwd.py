#######################################
#
#  Filename :  get_sql_passwd.py
#  Date: 2023-10-09
#
#  Get symmetric key from credential manager and decrypt password from file
#  Prerequisite:
#  - install cryptography library
#  - install keyring module
#
#  This script must be incorperated in the SQL script to access the password.
#  The symmetric key which is used to encrypt the password is stored in a keyring and is only accessible by the user who creates the symmetric key
#
#######################################

# Import Fernet from Crypthography library, keyring and getpass
from cryptography.fernet import Fernet
import keyring

#Get the symmetric key from the keyring
sym_key = keyring.get_password("SQLService","SymKey")
#print(sym_key)

#Encode the symmetric key
sym_key = sym_key.encode()

#print(sym_key)
#Define the Fernet cipher suite with the symmetric key
cipher_suite = Fernet(sym_key)

#Get the password from the binary file
with open('./mssql_pw_bytes.bin', 'rb') as file_object:
    for line in file_object:
        encrypted_passwd = line

#print(encrypted_passwd)

#Decrypt the password with the symmetric key
uncipher_text = (cipher_suite.decrypt(encrypted_passwd))
#print(uncipher_text)

#Decode the password
sql_passwd = bytes(uncipher_text).decode("utf-8")

#print(sql_passwd)
#Password can now be used in the SQL-code