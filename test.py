import unittest
from couch import Couch
from rabbit import Rabbit
from postgres_service import Postgres
from rethink import Rethink

class TestSuite(unittest.TestCase):

    def test_couch(self):
        couch = Couch()
        couch.populate()
        things = couch.count()
        self.failIf(things != 5)

    def test_rabbit(self):
        rabbit = Rabbit()
        rabbit.sendMessage()
        things = rabbit.relayMessage()
        self.failIf(things != "Hello World!")

    def test_postgres(self):
        pg = Postgres()
        pg.populate()
        count = pg.read()
        self.failIf(count != 5)
        pg.disconnect()

    def test_rethink(self):
        rethink = Rethink()
        rethink.populate()
        things = rethink.count()
        self.failIf(things != 5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
