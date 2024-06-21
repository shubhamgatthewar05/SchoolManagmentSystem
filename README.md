# SchoolManagmentSystem



# School Management System

This project is a web-based school management system built using Flask and MongoDB. It allows managing students, teachers, library transactions, and non-teaching staff.

## Features

- Dashboard displaying total counts and student information
- Adding and displaying student details
- Adding and displaying teacher details
- Adding and displaying library transactions
- Adding and displaying non-teaching staff details

## Requirements

- Python 3.8+
- Flask
- pymongo
- gridfs

## Installation

### Clone the Repository

Download or clone the repository to your local machine.

```bash
git clone <repository_url>
cd school-management-system
```

### Set Up the Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python packages:

```bash
pip install flask pymongo gridfs
```

### Set Up MongoDB

Make sure MongoDB is installed and running on your machine. You can download and install MongoDB from [here](https://www.mongodb.com/try/download/community).

Create the necessary database and collections:

1. Connect to the MongoDB server:

    ```bash
    mongo
    ```

2. Create the database and collections:

    ```javascript
    use school
    db.createCollection("student")
    db.createCollection("teachers")
    db.createCollection("transactions")
    db.createCollection("non_teaching_staff")
    ```

### Configure the Application

Set your secret key and MongoDB URI in the `main.py` file:

```python
app.secret_key = "your_secret_key"
client = MongoClient('mongodb://localhost:27017/')
```

You can change `your_secret_key` to any random string of your choice.

## Running the Application

Run the Flask application:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

1. **Dashboard**: Open `http://127.0.0.1:5000/` to view the dashboard displaying total counts of students, teachers, library transactions, and non-teaching staff.
2. **Add Students**: Navigate to `http://127.0.0.1:5000/index` to add student details.
3. **View Students**: Navigate to `http://127.0.0.1:5000/studentdisplay` to view all student details.
4. **Add Teachers**: Navigate to `http://127.0.0.1:5000/teacher` to add teacher details.
5. **View Teachers**: Navigate to `http://127.0.0.1:5000/teacher_list` to view all teacher details.
6. **Add Library Transactions**: Navigate to `http://127.0.0.1:5000/li` to add library transaction details.
7. **View Library Transactions**: Navigate to `http://127.0.0.1:5000/library_list` to view all library transaction details.
8. **Add Non-Teaching Staff**: Navigate to `http://127.0.0.1:5000/non` to add non-teaching staff details.
9. **View Non-Teaching Staff**: Navigate to `http://127.0.0.1:5000/non_teaching_staff_list` to view all non-teaching staff details.

## Project Structure

```
school-management-system/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── student.html
│   ├── studentdisplay.html
│   ├── teacherform.html
│   ├── teacher_list.html
│   ├── library.html
│   ├── library_list.html
│   ├── nonteach.html
│   ├── nontechlist.html
```

- `main.py`: The main application file containing routes and logic.
- `templates/`: HTML templates for rendering web pages.

## Contributing

Feel free to make suggestions or improvements to the project. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
```

This `README.md` should cover the basics of your project and help others set it up and use it effectively.
