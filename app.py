from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    conn = mysql.connector.connect(
        host = '',
        user = 'root',
        password = '',
        database = 'db'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students = students)


if __name__ == '__main__':
    app.run()
