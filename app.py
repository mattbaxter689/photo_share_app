from flask import Flask , render_template, request, redirect, url_for

'''
- Need input for user to select photo from their computer
- Then need to create button to download this picutre to a database
- Each photo will be given a new id and the date they were posted
- photos will then all be displayed on the home page when it loads
- Will be allowed to add caption to photos
- user can select a photo to view one specific photo in another page
- they could even be allowed to update the caption of the photo
- then need to update the styling of the page
'''

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