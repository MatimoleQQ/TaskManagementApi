# Task Manager API 🚀

![Python](https://img.shields.io/badge/Python-3.11-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.101.0-blue)
![SQLite](https://img.shields.io/badge/SQLite-lightgrey)
![JWT](https://img.shields.io/badge/JWT-auth-orange)

**A REST API for managing tasks with secure user authentication. Built with FastAPI, JWT, and SQLite. Perfect for a junior backend developer portfolio.**

---

## ✨ Features
- JWT-based **User Authentication**
- **Create, Read, Delete** Tasks
- Secure password hashing (**bcrypt**)
- SQLite database (can switch to PostgreSQL)
- Auto-generated API docs (/docs)

---

## 🚀 Demo
- Local API: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠 Installation

```bash
git clone <repo-url>
cd FastApi
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
echo SECRET_KEY=your_super_secret_key > .env
python -m uvicorn app.main:app --reload
```

---

## 🔗 API Endpoints

**Users**  
- `POST /users/` – Register new user  
- `POST /login` – Login and get JWT token  

**Tasks**  
- `GET /tasks/` – Get tasks  
- `POST /tasks/` – Create task  
- `DELETE /tasks/{task_id}` – Delete task  

---

## 💻 Example Requests

**Register User**
```bash
curl -X POST http://127.0.0.1:8000/users/ \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "mypassword"}'
```

**Login**
```bash
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=user@example.com&password=mypassword"
```

**Get Tasks**
```bash
curl -X GET http://127.0.0.1:8000/tasks/ \
-H "Authorization: Bearer <your_access_token>"
```

---

## 📁 Project Structure

```plaintext
app/
├── main.py        # FastAPI app and routes
├── auth.py        # JWT and auth logic
├── crud.py        # DB operations
├── database.py    # DB connection
├── models.py      # ORM models
├── schemas.py     # Request/response schemas
```

---

## ⚠️ Notes
- Keep `SECRET_KEY` private  
- Passwords are hashed with bcrypt  
- SQLite can be replaced with PostgreSQL in production
- API docs available at `/docs` (Swagger) and `/redoc` (ReDoc)
