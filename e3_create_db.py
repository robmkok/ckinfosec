##
##
import configparser
import mysql.connector
from getpass import getpass
import keyring

config_file = '/Volumes/Hub/CKInfoSec/E3/connect.ini'
vault = 'mariadb_vault'

def  read_config(section='development'):
     print(section)
     cp = configparser.ConfigParser()
     cp.read(config_file)
     if not cp.has_section(section):
         raise Exception("No configuration found for '{}'".format(section))

     return cp[section]

def main():
     try:
          db = read_config()
          #print(db['password'])
          #print(db['vault1'])
          print(db)
          #password = keyring.get_password(vault, db['user'])
          conn = mysql.connector.connect(**db, password=keyring.get_password(vault, db['user']))
     
     except mysql.connector.Error as e:
          print("MySQL exception: ", e)
          return
     except Exception as e: 
          print("Other exception", e); 
          return

 #    print ("Connected:", conn )

     cursor = conn.cursor()
     cursor.execute("SELECT * FROM Incidents")

     rows = cursor.fetchall()
     
     print(len(rows))
     for row in rows:
          print(row)

 #    while True:
 #         row = cursor.fetchone()
 #         if not row:
 #              break
 #         print (row)

     cursor.close()
     conn.close()

if __name__ == "__main__":
     main()


