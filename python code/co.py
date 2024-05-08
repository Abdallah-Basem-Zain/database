from flask import Flask, render_template, request, jsonify
import mysql.connector
import file4m
import databaseConnection as dbc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch student data from MySQL and render student.html with data
@app.route('/student')
def student():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Student")
            data = cursor.fetchall()
            return render_template('student.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()




# Route to fetch student data from MySQL and render student.html with data
@app.route('/instructor')
def instructor():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT IID , first_name , last_name , age , email FROM Instructor")
            data = cursor.fetchall()
            return render_template('instructor.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Route to fetch student data from MySQL and render student.html with data
@app.route('/program')
def program():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Program")
            data = cursor.fetchall()
            return render_template('program.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/license')
def license():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT ID , type , expiration_date , cost , p.name AS program_name FROM mainschema.license l JOIN mainschema.program p ON l.Program_ID_FK = p.PID;")
            data = cursor.fetchall()
            return render_template('license.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/aiu')
def aiu():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM AIUCourse")
            data = cursor.fetchall()
            return render_template('aiuCourses.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


@app.route('/coursera')
def coursera():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM CourseraCourse")
            data = cursor.fetchall()
            return render_template('coursera.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)