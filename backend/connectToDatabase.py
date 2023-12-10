import sqlite3


def connectDB() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect('db/sql.db')
    cursor = connection.cursor()

    return [ connection, cursor ]
