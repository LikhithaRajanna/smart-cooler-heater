from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
import cv2
from recognition import Recognise, status
from serial_test import Send
from dataset import create_dataset
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            Temp TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        Temp = request.form['temp']
        password = request.form['password']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute("insert into users values (NULL,?,?,?,?,?)", [name, phone, email, Temp, password])
        connection.commit()

        last_id = str(cursor.lastrowid)
        create_dataset(last_id)

    return render_template('adduser.html')

@app.route('/recognition')
def recognition():
    return render_template('recognition.html')

@app.route('/video_feed')
def video_feed():
    return Response(Recognise(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def get_status():
    return jsonify(status)

# same commands as manual.py, plus Stop -> 'X'
COMMANDS = {'heater1': 'A', 'heater2': 'B', 'cooler': 'C', 'stop': 'D'}

@app.route('/send/<cmd>', methods=['POST'])
def send_cmd(cmd):
    if cmd not in COMMANDS:
        return jsonify({'ok': False, 'error': 'invalid command'}), 400
    Send(COMMANDS[cmd])
    return jsonify({'ok': True, 'sent': COMMANDS[cmd]})

@app.route('/stop_feed')
def stop_feed():
    f = open('stream.txt', 'w')
    f.write('stop')
    f.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
