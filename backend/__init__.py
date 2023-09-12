from flask import Flask, request
import sqlite3, json

app = Flask(__name__)

def connectDB():
    connection = sqlite3.connect('db/sql.db')
    return connection

@app.post('/database')
def database():
    try:
        connection = connectDB()
        cursor = connection.cursor()

        toReturn = cursor.execute(request.get_json()['input']).fetchall()
        connection.commit()
        connection.close()

        print(toReturn)
        
        print(request.get_json())
        return {
            "ok": True,
            "data": toReturn
        }
    except:
        return {
            "ok": False,
            "data": "wrong input"
        }

@app.get('/test')
def testGet():
    return {"data": "test"}

@app.post('/test')
def testPost():
    print(request.data.decode('utf-8'))

    global var
    var = request.data.decode('utf-8')
    return "Data Received"

if __name__ == '__main__':
    app.run(debug=True)