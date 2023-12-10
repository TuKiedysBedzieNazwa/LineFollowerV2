import sqlite3


def rowLimiter(cursor: sqlite3.Cursor) -> None:
    rowLen = cursor.execute("SELECT count(*) FROM linefollower").fetchall()[0][0]

    if rowLen > 100:
        cursor.execute("DELETE FROM linefollower WHERE id=(SELECT MIN(id) FROM linefollower)")