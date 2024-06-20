from flask import Flask, render_template, request, redirect, url_for,session
import os
import sqlite3
from werkzeug.utils import secure_filename

# App Described
app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Set upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to initialize SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY,
            filename TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route To HomePage
@app.route('/')
def home():
   if 'username' in session: 
    # Fetch image filenames from the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT filename FROM images')
    images = [row[0] for row in cursor.fetchall()]  # Extract filenames from the fetched rows
    conn.close()
    return render_template('index.html', images=images)
   else:
       return redirect('/login')
# Route To Upload Page
@app.route('/upload')
def upload():
    return render_template('upload.html')

# Handle image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
       
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
     
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Add image filename to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO images (filename) VALUES (?)', (filename,))
        conn.commit()
        conn.close()
        
        return redirect(url_for('home'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'captain' and password == 'captain00515151':
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


 
@app.route('/delete/<filename>')
def delete(filename):
    try:
        # Remove entry from the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM images WHERE filename=?', (filename,))
        conn.commit()
        conn.close()

        # Delete the image file
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('home'))
    except FileNotFoundError:
        return "File not found."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
