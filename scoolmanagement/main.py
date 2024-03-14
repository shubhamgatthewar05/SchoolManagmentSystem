from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['school']
collection = db['student']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student_data = {
            'name': request.form['name'],
            'class': request.form['class'],
            'medium': request.form['medium'],
            'dob': request.form['dob'],
            'admission_year': request.form['admission-year'],
            'registration_number': request.form['registration-number']
        }

        # Save the photo file to a folder and store its path in the database
        photo_file = request.files['photo']
        photo_path = f"static/uploads/{photo_file.filename}"
        photo_file.save(photo_path)
        student_data['photo_path'] = photo_path
        
        # Insert student data into MongoDB
        collection.insert_one(student_data)

        flash('Data submitted successfully!', 'success')  # Flash success message
        return redirect(url_for('index'))

@app.route('/students')
def students():
    students_data = collection.find()  # Retrieve all student data
    return render_template('students.html', students=students_data)

@app.route('/student/<student_id>')
def student_detail(student_id):
    student = collection.find_one({'_id': student_id})
    return render_template('student_detail.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
