from peewee import *

db = SqliteDatabase('books.db')


class Book(Model):
    id = AutoField(primary_key=True)
    title = CharField()
    author = CharField()
    genre = CharField()
    year_published = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author}"


db.create_tables([Book])
