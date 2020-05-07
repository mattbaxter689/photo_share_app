from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/to_photos/', methods=['POST'])
def to_photos():
    return render_template('photos.html')

@app.route('/to_home/', methods=['POST'])
def to_home():
    return render_template('index.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

if __name__ == "__main__":
    app.run(debug=True)