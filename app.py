from flask import Flask, render_template, request, redirect
import string
import random

app = app = Flask(__name__, template_folder="templates")
url_database = {}  # Store short URLs and their corresponding long URLs.

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))  # You can adjust the length.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    if long_url in url_database:
        short_url = url_database[long_url]
    else:
        short_url = generate_short_url()
        url_database[long_url] = short_url
    return f"Short URL: {request.host_url}{short_url}"

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_database.values():
        long_url = next(key for key, value in url_database.items() if value == short_url)
        return redirect(long_url)
    else:
        return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)
