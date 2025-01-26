from flask import Flask, render_template, jsonify,redirect, url_for
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'olympics.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

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
    print(data)
    return jsonify(data)

get_athletes_data()
