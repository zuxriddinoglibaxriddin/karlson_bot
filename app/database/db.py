# create_part

from datetime import datetime
import time
import sqlite3
from os.path import exists as path_exists
from typing import List

sqlite = 'app/database/sqlite.db'
# sqlite = 'sqlite.db'

while not path_exists(sqlite):
    print(datetime.now(), "=> SQLite file is not found")
    time.sleep(1)

connection = sqlite3.connect(sqlite)
cursor = connection.cursor()

create_table_orders = """
   create table if not exists orders(

        id integer primary key autoincrement,
        created_at text default current_timestamp,
        phone_number varchar(25),
        product_title varchar(25),
        product_kilo varchar(25),
        product_count varchar(25),
        telegram_id integer(15),
        username varchar(25)

   ) 
"""


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        connection.commit()
        return result

    return wrapper


@commit
def create_table():
    cursor.execute(create_table_orders)


@commit
def new_order(phone_number, product_title, product_kilo, product_count, telegram_id, username):
    inser_into_order = """
        insert into orders (phone_number,product_title,product_kilo,product_count,telegram_id,username) values (?,?,?,?,?,?)
    """

    params = (phone_number, product_title, product_kilo, product_count, telegram_id, username)
    cursor.execute(inser_into_order, params)


@commit
def select_telegram_id():
    select_id = """
        select telegram_id from orders
    """
    telegram_id = cursor.execute(select_id).fetchall()
    return telegram_id


@commit
def select_all_users():
    select_users = """
        select * from orders
    """

    users = cursor.execute(select_users).fetchall()
    return users


def init():
    create_table()

# init()
