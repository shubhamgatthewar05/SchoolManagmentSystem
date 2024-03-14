from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from gridfs import GridFS
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['school']
collection = db['student']
collection1 = db['teachers']
collection2 = db['transactions']
collection3 = db['non_teaching_staff']
fs = GridFS(db)

@app.route('/index')
def index():
    return render_template('student.html')

@app.route('/li')
def li():
    return render_template('library.html')

@app.route('/')
def dashboard():
    total_students = collection.count_documents({})
    total_teachers=collection1.count_documents({})
    total_li=collection2.count_documents({})
    students_data = collection.find()
    total_non=collection3.count_documents({})
    return render_template('index.html', total_students=total_students,total_teachers=total_teachers,total_li=total_li,students=students_data,total_non=total_non)

@app.route('/teacher')
def teacher():
    return render_template('teacherform.html')

@app.route('/non')
def non():
    return render_template('nonteach.html')

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

        # Save the photo file to GridFS
       
        
        # Insert student data into MongoDB
        collection.insert_one(student_data)
        flash('Data submitted successfully!', 'success') 
        return redirect(url_for('index'))

@app.route('/studentdisplay')
def studentdisplay():
    students_data = collection.find()  # Retrieve all student data
    return render_template('studentdisplay.html', students=students_data)

@app.route('/submit_teacher', methods=['POST'])
def submit_teacher():
    if request.method == 'POST':
        teacher_data = {
            'teacherName': request.form['teacherName'],
            'qualification': request.form['qualification'],
            'subject': request.form['subject'],
            'medium': request.form['medium'],
            'class': request.form['class'],
            'registrationNumber': request.form['registrationNumber'],
            'joiningYear': request.form['joiningYear'],
            'experience': request.form['experience'],
            'salary': request.form['salary']
        }
        
        # Insert teacher data into MongoDB
        collection1.insert_one(teacher_data)

        flash('Teacher information submitted successfully!', 'success')  # Flash success message
        return redirect(url_for('teacher'))

@app.route('/submit_library', methods=['POST'])
def submit_library():
    if request.method == 'POST':
        library_data = {
            'book': request.form['book'],
            'studentName': request.form['studentName'],
            'libraryId': request.form['libraryId'],
            'date': request.form['date'],
            'returnDate': request.form['returnDate']
        }
        
        # Insert library data into MongoDB
        collection2.insert_one(library_data)

        flash('Library information submitted successfully!', 'success')  # Flash success message
        return redirect(url_for('li'))



@app.route('/submit_non_teaching_staff', methods=['POST'])
def submit_non_teaching_staff():
    if request.method == 'POST':
        non_teaching_staff_data = {
            'position': request.form['position'],
            'name': request.form['name'],
            'age': int(request.form['age']),
            'register_id': request.form['register_id'],
            'joining_year': int(request.form['joining_year']),
            'salary': float(request.form['salary'])
        }
        
        # Insert non-teaching staff data into MongoDB
        collection3.insert_one(non_teaching_staff_data)

        flash('Non-Teaching Staff information submitted successfully!', 'success')  # Flash success message
        return redirect(url_for('non'))


@app.route('/teacher_list')
def teacher_list():
    teachers_data = collection1.find()  # Retrieve all teacher data
    return render_template('teacher_list.html', teachers=teachers_data)

@app.route('/library_list')
def library_list():
    library_data = collection2.find() # Retrieve all library data
    return render_template('library_list.html', library=library_data)

@app.route('/non_teaching_staff_list')
def non_teaching_staff_list():
    non_teaching_staff_data = collection3.find()  # Retrieve all non-teaching staff data
    return render_template('nontechlist.html', non_teaching_staff=non_teaching_staff_data)



if __name__ == '__main__':
    app.run(debug=True)
