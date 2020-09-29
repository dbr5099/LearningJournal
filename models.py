import datetime
from peewee import IntegerField, TextField, DateField, SqliteDatabase, Model


DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_id = IntegerField(primary_key=True)
    title = TextField()
    timespent = IntegerField(null=False)
    learned = TextField(null=False)
    resources= TextField(null=False)
    date = DateField(default=datetime.datetime.now().strftime("%B %d, %Y"))

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, title, timespent, learned, resources, date):
        with DATABASE.transaction():
            cls.create(title=title, timespent=timespent,
                       learned=learned, resources=resources, date=date)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)


def view_all():
    """A function when you run models.py that allows you to view all entries"""
    query = Entry.select().dicts()

    for item in query:
        print(item)


if __name__ == '__main__':
    initialize()
    view_all()