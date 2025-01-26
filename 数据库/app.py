from flask import Flask, render_template, request, jsonify,redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), 'olympics.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/home')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT text FROM feedback')
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('home.html', feedbacks=feedbacks)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/athletes2.html')
def athletes2():
    return render_template('athletes2.html')

@app.route('/athletes.html')
def athletes():
    return render_template('athletes.html')

@app.route('/dataset/athletes')
def get_athletes_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            NOC as country, discipline, COUNT(*) as athlete_count
        FROM 
            athletes
        GROUP BY 
            NOC, discipline
    ''')
    rows = cursor.fetchall()
    conn.close()
    data = [dict(row) for row in rows]
    return jsonify(data)

@app.route('/medals.html')
def medals():
    return render_template('medals.html')

@app.route('/colors.html')
def colors():
    return render_template('colors.html')

@app.route('/colors2.html')
def colors2():
    return render_template('colors2.html')

@app.route('/year-selection.html')
def dishes():
    return render_template('year-selection.html')

@app.route('/dishes/<int:year>')
def get_dishes(year):
    conn = sqlite3.connect('olympics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SignatureDishes WHERE year=?", (year,))
    result = cursor.fetchone()
    conn.close()

    if result:
        year, city, cuisine, dishes = result
        return jsonify({
            'year': year,
            'city': city,
            'cuisine': cuisine,
            'dishes': dishes
        })
    else:
        return jsonify({'error': '未找到该年份的奥运会信息'})


@app.route('/submit_interest', methods=['POST'])
def submit_interest():
    interest = request.form['interest']
     # You can store this information in the database or process it as needed.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (text) VALUES (?)', (interest,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,port=5001)

