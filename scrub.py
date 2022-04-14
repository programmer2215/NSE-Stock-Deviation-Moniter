import database as db

with open("stocks.txt") as f:
    for i in f:
        stock = i.strip()
        a = db.connect_to_sqlite(db.get_last_date, stock)