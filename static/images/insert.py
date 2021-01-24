import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
from datetime import datetime

HOST = "integracio.epsem.upc.edu"
DB = "grupE"
USR = "grupE"
PWD = "z7j+s-ERBj6$4e%g"

def inserta(punt,x,y,z):
    try:
        current_Date = datetime.now()
        timestamp = current_Date.strftime('%Y-%m-%d %H:%M:%S')
        powers = json.dumps({'POS1':punt[0] , 'POS2':punt[1], 'POS3':punt[2], 'POS4':punt[3], 'POS5':punt[4], 'POS6':punt[5], 'POS7':punt[6], 'POS10':punt[7], 'POS11':punt[8], 'POS12':punt[9], 'POS13':punt[10], 'POS14':punt[11], 'POS15':punt[12], 'POS16':punt[13], 'POS17':punt[14], 'POS19':punt[15]})
        query = """INSERT INTO rssi_powers (time, user, device, x, y, z, powers) VALUES ('{}', '{}', '{}', {}, {}, {}, '{}')""".format(timestamp, "Pol", "ESP01", x, y, z, powers)
        print query

        connection = mysql.connector.connect(host=HOST, database=DB, user=USR, password=PWD)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print(cursor.rowcount, "Record inserted successfully")

        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")

    except mysql.connector.Error as error:
        print("Failed to insert record {}".format(error))
