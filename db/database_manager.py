import os.path
import sqlite3

from constants.constant import (
    QUERY_INSERT_TABLE_USER,
    QUERY_INSERT_TABLE_WORD,
    QUERY_TABLE_PARAMETER_USER,
    QUERY_TABLE_PARAMETER_WORD, QUERY_FIND_USER, QUERY_FIND_SENTENCE,
)
from constants.error_messages import ERROR_MESSAGE_DB_ALREADY_EXISTS
from exceptions.DB_already_exists_error import DBAlreadyExistsError


def open_db(json_name):
    con = sqlite3.connect(os.path.join("data", f"{json_name}.db"))
    # attiva la modalità di autocommit
    con.isolation_level = None
    return con


def initialize_db(json_name, on_db_conflict_delete):
    if os.path.exists(os.path.join("data", f"{json_name}.db")):
        if on_db_conflict_delete:
            os.remove(os.path.join("data", f"{json_name}.db"))
        else:
            raise DBAlreadyExistsError(
                ERROR_MESSAGE_DB_ALREADY_EXISTS.format(json_name)
            )
    con = open_db(json_name)
    cur = con.cursor()
    cur.execute(QUERY_INSERT_TABLE_USER)
    cur.execute(QUERY_INSERT_TABLE_WORD)


def insert_user(json_name, id_user, name):
    con = open_db(json_name)
    cur = con.cursor()

    cur.execute(
        f"INSERT OR IGNORE INTO user ({QUERY_TABLE_PARAMETER_USER}) \
        VALUES('{id_user}','{name}')"
    )


def bulk_insert_users(json_name, users):
    con = open_db(json_name)
    cur = con.cursor()
    cur.executemany(
        f"INSERT OR IGNORE INTO user ({QUERY_TABLE_PARAMETER_USER}) \
        VALUES(?,?)",
        users,
    )


def insert_sentence(json_name, value, date, id_user):
    con = open_db(json_name)
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO sentence ({QUERY_TABLE_PARAMETER_WORD}) \
        VALUES('{value}',{date},'{id_user}')"
    )


def bulk_insert_sentences(json_name, sentences):
    con = open_db(json_name)
    cur = con.cursor()
    cur.executemany(
        f"INSERT INTO sentence ({QUERY_TABLE_PARAMETER_WORD}) \
        VALUES(?,?,?)",
        sentences,
    )


def search_user(json_name, user_input):
    con = open_db(json_name)
    cur = con.cursor()

    return cur.execute(
        QUERY_FIND_USER.format(user_input)
    )


def search_sentence(json_name, user_input):
    con = open_db(json_name)
    cur = con.cursor()

    return cur.execute(
        QUERY_FIND_SENTENCE.format(user_input)
    )
