# Student Management REST API

A simple REST API built using **FastAPI**, **SQLAlchemy**, and **SQLite** to perform CRUD (Create, Read, Update, Delete) operations on student records.

## 📌 Features

- Create a new student
- View all students
- View a student by ID
- Update student details
- Delete a student
- SQLite database integration
- Input validation using Pydantic
- Automatic Swagger API documentation
- Proper HTTP status codes and error handling

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

## 📂 Project Structure

```
StudentAPI/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── README.md
└── student.db
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/StudentAPI.git
```

### 2. Open the project

```bash
cd StudentAPI
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 Swagger Documentation

After starting the server, open:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all endpoints directly from your browser.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Create a new student |
| GET | /students | Retrieve all students |
| GET | /students/{id} | Retrieve a student by ID |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |

---

## 📝 Sample Request

### POST /students

```json
{
  "name": "Vishnu",
  "age": 22,
  "course": "Computer Science"
}
```

### Sample Response

```json
{
  "id": 1,
  "name": "Vishnu",
  "age": 22,
  "course": "Computer Science"
}
```

---

## ✅ HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | OK |
| 201 | Created |
| 404 | Student Not Found |
| 422 | Validation Error |

---

## 🧪 Testing

The API endpoints were successfully tested using **Thunder Client** in Visual Studio Code.

The following endpoints were tested:

- POST /students
- GET /students
- GET /students/{id}
- PUT /students/{id}
- DELETE /students/{id}

---

## 💾 Database

This project uses **SQLite** as the local database.

Database file:

```
student.db
```

---

## 👨‍💻 Author

**Vishnu Gurrapusala**

B.Tech – Computer Science Engineering
