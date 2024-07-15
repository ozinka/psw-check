from flask import Flask, render_template, request
import search

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    lines = []
    results = []
    password = ''
    search_time = ''
    if request.method == 'POST':
        password = request.form['password']
        print(password)

    if password:
        lines, results, search_time = search.search(password)

    return render_template('index.html', lines=lines, results=results, search_time=search_time)


if __name__ == '__main__':
    app.run(debug=True)
