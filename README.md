# 📘 Book CRUD Microservice (FastAPI + Docker)

## 📌 Project Overview

This project is a CRUD (Create, Read, Update, Delete) Microservice built using **FastAPI** and containerized using **Docker**.
It provides REST APIs to manage Book records and is fully configurable using environment variables.

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
docker build -t aswininigidaveer/book-crud-api:1.0 .
```

## Step 2: Run Docker Container (Default Port 8000)

```
docker run -d -p 8000:8000 aswininigidaveer/book-crud-api:1.0
```

Open in browser:

```
http://localhost:8000/docs
```

---

## Run on Custom Port (Example: 9000)

```
docker run -d -p 9000:9000 -e PORT=9000 aswininigidaveer/book-crud-api:1.0
```

Open:

```
http://localhost:9000/docs
```

---

# 🌐 PUSH IMAGE TO DOCKER HUB

## Login

```
docker login
```

## Push Image

```
docker push aswininigidaveer/book-crud-api:1.0
```

## Pull Image Anywhere

```
docker pull aswininigidaveer/book-crud-api:1.0
```

---

# 📦 EXPORT DOCKER IMAGE (ALTERNATIVE SUBMISSION)

## Save Image

```
docker save -o book-crud-api.tar aswininigidaveer/book-crud-api:1.0
```

## Load Image

```
docker load -i book-crud-api.tar
```

---

# 🔁 API ENDPOINTS

## 1. Create Book

POST /books

Sample Body:

```
{
  "id": 1,
  "title": "Docker Basics",
  "author": "John"
}
```

## 2. Get All Books

GET /books

## 3. Get Book by ID

GET /books/1

## 4. Update Book

PUT /books/1

Sample Body:

```
{
  "id": 1,
  "title": "Updated Title",
  "author": "John"
}
```

## 5. Delete Book

DELETE /books/1

---

# 🔧 Useful Docker Commands

List running containers:

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

# 🌍 GITHUB COMMANDS

Initialize repository:

```
git init
git add .
git commit -m "Initial commit - CRUD microservice with Docker"
```

Connect to GitHub:

```
git remote add origin https://github.com/yourusername/CURD_API.git
```

If repository already contains files:

```
git pull origin main --allow-unrelated-histories
```

Push to GitHub:

```
git push origin main
```

---

# ✅ Checklist

✔ CRUD operations implemented
✔ Proper folder structure
✔ requirements.txt used
✔ Environment variable configuration
✔ Dockerfile created
✔ Docker image built
✔ Container running successfully
✔ Image pushed to Docker Hub
✔ README with complete execution steps included

---

# 👩‍💻 Author

Ashwini Gidaveer
