import json
from flask import Flask, request
from .connectToDatabase import connectDB
from .rowLimiter import rowLimiter

app = Flask(__name__)

@app.post('/database')
def database():
    try:
        connection, cursor = connectDB()

        toReturn = cursor.execute(request.get_json()['input']).fetchall()
        connection.close()

        print(request.get_json())
        return {
            "ok": True,
            "data": toReturn
        }
    except:
        connection.close()
        return {
            "ok": False,
            "data": "wrong input"
        }

@app.route('/linefollower', methods=[ 'POST', 'GET' ])
def lineFolower():
    connection, cursor = connectDB()

    if request.method == "POST":
        try:
            data = request.get_json()

            cursor.execute("""INSERT INTO linefollower (
                temperature,
                sens1,
                sens2,
                sens3,
                sens4,
                sens5,
                sens6
            ) VALUES(?,?,?,?,?,?,?);""", [
                data['temperature'],
                data['sens1'],
                data['sens2'],
                data['sens3'],
                data['sens4'],
                data['sens5'],
                data['sens6']
            ])

            rowLimiter(cursor)

            connection.commit()
            connection.close()
            return {
                "ok": True
            }

        except:
            connection.close()
            return {
                'ok': False
            }

    elif request.method == "GET":

        toReturn = cursor.execute("SELECT * FROM linefollower;").fetchall()

        rowLimiter(cursor)

        connection.close()
        return {
            "ok": True,
            "data": toReturn
        }

@app.get('/test')
def testGet():
    return {"data": "test"}

@app.post('/test')
def testPost():
    print(request.get_json())

    return "Data Received"

if __name__ == '__main__':
    app.run(debug=True)