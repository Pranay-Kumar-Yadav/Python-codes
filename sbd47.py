#database programming
import sqlite3

class person:

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.excute("""
        INSERT INTO persons VALUES
        ({}, {}, {}, {})
        """.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()

p1 = person(7, "Alex", "Robbins", 30)

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("Select * FROM persons")
results = cursor.fetcha11()
print(results)

connection.close()