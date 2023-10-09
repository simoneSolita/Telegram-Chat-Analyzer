import os.path
import sqlite3

from constants.constant import FILE_DB_NAME, QUERY_INSERT_TABLE_USER, QUERY_INSERT_TABLE_WORD, \
    QUERY_TABLE_PARAMETER_USER, QUERY_TABLE_PARAMETER_WORD


def open_db(group_name):
    con = sqlite3.connect(os.path.join("data", f"{FILE_DB_NAME}{group_name}.db"))
    # attiva la modalità di autocommit
    con.isolation_level = None
    return con


def initialize_db(group_name):
    con = open_db(group_name)
    cur = con.cursor()
    cur.execute(QUERY_INSERT_TABLE_USER)
    cur.execute(QUERY_INSERT_TABLE_WORD)


def insert_user(group_name, id_user, name):
    con = open_db(group_name)
    cur = con.cursor()

    cur.execute(f"INSERT OR IGNORE INTO user ({QUERY_TABLE_PARAMETER_USER}) \
        VALUES('{id_user}','{name}')")


def insert_sentence(group_name, value, date, id_user):
    con = open_db(group_name)
    cur = con.cursor()
    cur.execute(f"INSERT INTO sentence ({QUERY_TABLE_PARAMETER_WORD}) \
        VALUES('{value}',{date},'{id_user}')")
