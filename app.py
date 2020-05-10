from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

#the 2 following routes are for buttons that allow users to move to the "Photos" tab, and back to the home page
@app.route('/to_photos/', methods=['POST'])
def to_photos():
    return redirect(url_for('photos'))

@app.route('/to_home/', methods=['POST'])
def to_home():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)