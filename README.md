# 📘 Book CRUD Microservice (FastAPI + Docker)

---

## 📌 Project Overview

This project is a **CRUD (Create, Read, Update, Delete) Microservice** built using **FastAPI** and containerized using **Docker**.

It provides REST APIs to manage Book records and includes:

✔ REST API implementation
✔ Swagger UI documentation
✔ Docker containerization
✔ Docker Hub image push
✔ GitHub repository integration

---

# 🗂️ Project Structure

```
CURD_API/
│
├── app/
│   ├── main.py
│   └── models.py
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

# ⚙️ Technologies Used

* Python 3.11
* FastAPI
* Uvicorn
* Docker

---

# 🚀 RUN APPLICATION LOCALLY (WITHOUT DOCKER)

## Step 1: Create Virtual Environment

```
python -m venv .venv
```

## Step 2: Activate Virtual Environment

Windows:

```
.venv\Scripts\activate
```

## Step 3: Install Dependencies

```
pip install -r requirements.txt
```

## Step 4: Run Application

```
uvicorn app.main:app --reload --port 8000
```

## Step 5: Open in Browser

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 DOCKERIZATION STEPS

## Step 1: Build Docker Image

(Execute from project root where Dockerfile exists)

```
docker build -t aswininigidaaveer/book-crud-api:1.0 .
```

## Step 2: Run Docker Container

```
docker run -d -p 8000:8000 aswininigidaaveer/book-crud-api:1.0
```

## Step 3: Access Application

```
http://localhost:8000/docs
```

---

# 📷 API OUTPUT (Swagger UI)

After running the application successfully, the Swagger UI displays all CRUD endpoints as shown below:

### Available Endpoints:

* GET  /        → Root
* GET  /books   → Get All Books
* POST /books   → Create Book
* GET  /books/{book_id} → Get Book by ID
* PUT  /books/{book_id} → Update Book
* DELETE /books/{book_id} → Delete Book

---

## 📌 Swagger UI Screenshot

Below is the output of the running application:

![Swagger UI Output](Screenshot%202026-03-04%20091623.png)

> This screenshot shows successful execution of the FastAPI application with all CRUD endpoints visible.

---

# 🔁 API ENDPOINTS DETAILS

## 1️⃣ Create Book

POST /books

Sample Request Body:

```
{
  "id": 1,
  "title": "Docker Basics",
  "author": "John"
}
```

---

## 2️⃣ Get All Books

GET /books

---

## 3️⃣ Get Book by ID

GET /books/1

---

## 4️⃣ Update Book

PUT /books/1

Sample Body:

```
{
  "id": 1,
  "title": "Updated Title",
  "author": "John"
}
```

---

## 5️⃣ Delete Book

DELETE /books/1

---

# 🌐 PUSH TO GITHUB

If remote repository already exists:

```
git pull origin main --allow-unrelated-histories
git push origin main
```

Initial setup:

```
git init
git add .
git commit -m "Initial commit - CRUD microservice with Docker"
git remote add origin https://github.com/yourusername/CURD_API.git
git push -u origin main
```

---

# 🌍 PUSH IMAGE TO DOCKER HUB

Login:

```
docker login
```

Push Image:

```
docker push aswininigidaaveer/book-crud-api:1.0
```

---

# 🔧 Useful Docker Commands

List containers:

```
docker ps
```

Stop container:

```
docker stop <container_id>
```

Remove container:

```
docker rm <container_id>
```

View logs:

```
docker logs <container_id>
```

---

# ✅ Final Output Verification

✔ Application runs successfully
✔ Swagger UI accessible
✔ All CRUD endpoints working
✔ Docker container running
✔ Image pushed to Docker Hub
✔ Code pushed to GitHub
✔ Screenshot of API output attached

---

# 👩‍💻 Author

Ashwini Gidaveer

---
