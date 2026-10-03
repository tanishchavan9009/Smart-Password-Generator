from flask import Flask, render_template, request
import random
import string
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create database
def create_database():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS generated_passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            difficulty TEXT,
            length INTEGER,
            password TEXT,
            created_at TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_database()


def generate_password(length, letters, numbers, special):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}"

    chars = ""

    if letters:
        chars += lowercase + uppercase

    if numbers:
        chars += digits

    if special:
        chars += symbols

    if not chars:
        return "Please select at least one option"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password(level, length, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO generated_passwords (difficulty, length, password, created_at)
        VALUES (?, ?, ?, ?)
    ''', (level, length, password, str(datetime.now())))

    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""

    if request.method == 'POST':
        length = int(request.form['length'])

        letters = 'include_letters' in request.form
        numbers = 'include_numbers' in request.form
        special = 'include_special' in request.form

        difficulty = "custom"

        password = generate_password(length, letters, numbers, special)
        save_password(difficulty, length, password)

    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)