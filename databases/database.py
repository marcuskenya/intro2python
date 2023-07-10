from peewee import *
from os import path

# creating my 1st database.
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Marcus.db"))


# Creating table inside db
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Student(Model):
    name = CharField()
    number = IntegerField()
    age = IntegerField()
    gender = CharField()
    studentcode = IntegerField()

    class Meta:
        database = db


User.create_table(fail_silently=True)
Student.create_table(fail_silently=True)
