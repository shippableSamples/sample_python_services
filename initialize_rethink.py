import rethinkdb as r

def main():
    r.connect(host = 'localhost', port = 28015).repl()
    r.db_create('test').run()

if __name__ == "__main__":
    main()
