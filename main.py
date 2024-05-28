
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/preferences')
def preferences():
    return render_template('preferences.html')

@app.route('/newsfeed')
def newsfeed():
    connection = sqlite3.connect('news.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    connection.close()
    return jsonify(articles)

@app.route('/customization', methods=['POST'])
def customization():
    connection = sqlite3.connect('news.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE preferences SET interests=?, topics=? WHERE user_id=?', (request.form['interests'], request.form['topics'], request.form['user_id']))
    connection.commit()
    connection.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()
