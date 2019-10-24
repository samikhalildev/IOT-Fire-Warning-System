import sqlite3

connection = sqlite3.connect("sensors.db") 
crsr = connection.cursor() 

create_command = """
CREATE TABLE sensor(id INTEGER PRIMARY KEY AUTOINCREMENT, temperature DOUBLE, pressure DOUBLE,  date TEXT, time TEXT);
"""
crsr.execute("""drop table if exists sensor""")
crsr.execute(create_command)

connection.commit()
connection.close()
