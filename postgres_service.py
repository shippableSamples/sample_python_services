import psycopg2 as pg


class Postgres():
    def __init__(self):
        self.conn_string = "host='127.0.0.1' dbname='test' user='postgres' password=''"
        self.conn = pg.connect(self.conn_string)
        self.cursor = self.conn.cursor()

    def populate(self):
        self.cursor.execute("DROP TABLE IF EXISTS things;")
        self.cursor.execute("CREATE TABLE things (name varchar(20));")
        self.cursor.execute("INSERT INTO things(name) VALUES('Dre');")
        self.cursor.execute("INSERT INTO things(name) VALUES('Smalls');")
        self.cursor.execute("INSERT INTO things(name) VALUES('West');")
        self.cursor.execute("INSERT INTO things(name) VALUES('Combs');")
        self.cursor.execute("INSERT INTO things(name) VALUES('Flame');")

    def read(self):
        self.cursor.execute("SELECT * FROM things;")
        count = self.cursor.fetchall()
        return len(count)

    def disconnect(self):
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    postgres = Postgres()
    postgres.populate()
    postgres.read()
    postgres.disconnect()
