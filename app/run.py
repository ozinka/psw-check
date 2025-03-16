"""
File Name: search.py
Description: Flask application allows to go through the big (hundreds of GB) TXT file with sorted lines and
             does search for specific string (password)

Created by: Vitaliy Osidach
Date Created: 2024.07.16

Version: 1.0

Usage:
    run:
    set DATA_DIR=C:\path\to\folder
    set PASSWORD_FILE=filename.txt
    python3.exe run.py

p.s. Environment variables DATA_DIR and PASSWORD_FILE can be set in .env file
"""
from flask import Flask, render_template, request
import search
from dotenv import load_dotenv

load_dotenv(override=False)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    lines = []
    results = []
    password = ''
    search_time = ''
    if request.method == 'POST':
        password = request.form['password']

    if password:
        lines, results, search_time = search.search(password)

    return render_template('index.html', lines=lines, results=results, search_time=search_time)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
