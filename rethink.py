import rethinkdb as r


class Rethink():
    def __init__(self):
        self.client = r.connect(host = 'localhost', port = 28015).repl()
        r.db_drop('test').run()
        r.db_create('test').run()
        self.db = r.db('test')

    def populate(self):
        self.db.table_create('table').run()
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.db.table('table').insert(things).run()

    def count(self):
        return self.db.table('table').count().run()

if __name__ == "__main__":
    rethink = Rethink()
    rethink.populate()
    print(mongo.count())
