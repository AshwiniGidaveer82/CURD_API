# Python Microservice (FastAPI + MongoDB + Docker + Kubernetes)

## Overview

This project implements a **containerized Python microservice** using FastAPI, providing RESTful CRUD operations backed by MongoDB.
The service is designed following **microservices architecture principles** and deployed using Docker and Kubernetes.

It demonstrates:

* API development with FastAPI
* Database integration using MongoDB
* Containerization using Docker
* Orchestration using Kubernetes

---

## API Preview

<img width="1870" height="628" alt="Screenshot 2026-04-11 084641" src="https://github.com/user-attachments/assets/b52eacbf-dcc4-446b-b223-98632ddf4558" />

---

## Architecture Diagram

```
Client (Browser / Postman)
            │
            ▼
     Kubernetes Service (NodePort)
            │
            ▼
   Python Microservice (FastAPI Pod)
            │
            ▼
        MongoDB Pod
            │
            ▼
        Data Storage
```

---

## Execution Flow

1. Client sends HTTP request (GET, POST, PUT, DELETE)
2. Request is routed via Kubernetes Service
3. FastAPI application processes the request
4. Data is stored/retrieved from MongoDB
5. Response is returned to the client

---

## Tech Stack

* FastAPI (Backend Framework)
* MongoDB (Database)
* Docker (Containerization)
* Kubernetes (Orchestration)
* GitHub (Version Control)

---

## Project Structure

```
python-microservice/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── mongodb-deployment.yaml
├── mongodb-service.yaml
├── python-deployment.yaml
├── python-service.yaml
│
├── Screenshot 2026-04-11 084641.png
└── README.md
```

---

## Running the Application

### Local Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Access:
http://localhost:8000/docs

---

### Docker Setup

```bash
docker-compose up --build
```

---

### Kubernetes Deployment

```bash
kubectl apply -f mongodb-deployment.yaml
kubectl apply -f mongodb-service.yaml
kubectl apply -f python-deployment.yaml
kubectl apply -f python-service.yaml
```

Verify:

```bash
kubectl get pods
kubectl get svc
```

Access:

```
http://localhost:<nodeport>/docs
```

---

## API Endpoints

| Method | Endpoint    | Description        |
| ------ | ----------- | ------------------ |
| GET    | /           | Health check       |
| GET    | /items      | Retrieve all items |
| POST   | /items      | Create item        |
| GET    | /items/{id} | Retrieve item      |
| PUT    | /items/{id} | Update item        |
| DELETE | /items/{id} | Delete item        |

---

## Example Request

```json
{
  "name": "Laptop",
  "price": 50000
}
```

---

## Key Features

* RESTful API design
* Full CRUD operations
* Containerized microservice
* Kubernetes-based deployment
* Service-to-service communication
* Interactive API interface

---

## Common Issues

**Image not found in Kubernetes**

```bash
docker build -t python-microservice:latest .
```

**NodePort already in use**

* Update `nodePort` in `python-service.yaml`

**MongoDB connection issue**

```
mongodb://mongodb:27017/
```

---

## Future Enhancements

* CI/CD pipeline using GitHub Actions
* API Gateway integration
* Authentication (JWT)
* Cloud deployment (AWS / GCP)

---

## Author

Ashwini Gidaveer

---
