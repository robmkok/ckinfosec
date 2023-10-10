import mysql.connector as database

def main():
     try:
           conn = database.connect (
             host = 'localhost',
             database = 'dlp_db',
             port = '3306',
             user = 'rob',
             password = 'G@4itn@ow')
     except mysql.connector.Error as e:
          print("MySQL exception: ", e)
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


