# AWS Cloud Management API

![FastAPI](https://img.shields.io/badge/FastAPI-Backend_API-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![AWS](https://img.shields.io/badge/AWS-boto3-orange)
![Status](https://img.shields.io/badge/Project-Learning%20Project-success)

A backend REST API project built using Python, FastAPI and boto3 to interact with AWS services programmatically.

The goal of this project is to integrate:

* AWS services
* boto3 SDK
* FastAPI
* REST API design
* Git workflows
* Cloud resource management

The project currently supports:

* Amazon EC2 instance management
* Amazon S3 bucket and object management

---

# Tech Stack

* Python
* FastAPI
* boto3
* AWS EC2
* AWS S3
* Uvicorn
* Git & GitHub

---

# Features

* EC2 Instance Management APIs
* S3 Bucket & Object Management APIs
* FastAPI based REST architecture
* boto3 integration with AWS
* Modular backend structure
* Request validation using Pydantic
* Swagger/OpenAPI documentation
* Git branch & PR workflow practice

## Current API Overview

### Base APIs

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| GET    | `/`      | Health check endpoint    |
| GET    | `/docs`  | Swagger UI documentation |

---

## EC2 APIs

### 1. Get all instances

```http
GET /instances
```

Returns all EC2 instances.

Example response:

```json
{
  "status": "success",
  "message": [
    {
      "instance_id": "i-0123456789",
      "instance_name": "web-server",
      "instance_state": "running"
    }
  ]
}
```

---

### 2. Launch instance

```http
POST /instances
```

Launches a new EC2 instance using an AWS Launch Template.

Example request body:

```json
{
  "name": "backend-server",
  "launch_template": "my-template"
}
```

---

### 3. Get instances by state

```http
GET /instances/state/{state}
```

Returns EC2 instances filtered by state.

Supported states:

* running
* stopped
* terminated
* pending

Example:

```http
GET /instances/state/running
```

---

### 4. Terminate instances

```http
DELETE /instances
```

Terminates EC2 instances using instance IDs.

Example request body:

```json
{
  "instance_ids": [
    "i-0123456789",
    "i-9876543210"
  ]
}
```

Example response:

```json
{
  "status": "success",
  "message": "Instance with id ['i-0123456789'] terminated"
}
```

---

## S3 APIs

### 1. Create bucket

```http
POST /buckets
```

Creates an S3 bucket.

Example request body:

```json
{
  "name": "my-test-bucket"
}
```

---

### 2. Get all buckets

```http
GET /buckets
```

Returns all S3 buckets.

---

### 3. Get bucket objects

```http
GET /buckets/{bucket_name}
```

Returns all files/objects inside a bucket.

---

### 4. Delete specific bucket

```http
DELETE /buckets/{bucket_name}
```

Deletes a specific bucket.

---

### 5. Empty bucket

```http
DELETE /buckets/{bucket_name}/files
```

Deletes all objects from a bucket.

---

### 6. Delete bucket object

```http
DELETE /buckets/{bucket_name}/files/{file_name}
```

Deletes a specific object from the bucket.

---

# Project Structure

```text
AWS-App/
│
├── ec2/
│   ├── routes.py
│   ├── service.py
│   └── schemas.py
│
├── s3/
│   ├── routes.py
│   ├── service.py
│   └── schemas.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone the repository

```bash
git clone <repository-url>
cd AWS-App
```

---

## 2. Create virtual environment

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure AWS credentials

```bash
aws configure
```

Provide:

* AWS Access Key
* AWS Secret Access Key
* Region
* Output format

---

# Run the Application

```bash
uvicorn main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

---

# Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Example Project Structure Flow

```text
Client/Postman
       ↓
FastAPI Routes
       ↓
Service Layer
       ↓
boto3 SDK
       ↓
AWS Services (EC2 / S3)
```

---

# Practice Goals

This project was created to:

* Demonstrate the usage of AWS programmatically using boto3
* Demonstrate infrastructure automation
* Demonstrate FastAPI development
* Build REST APIs
* Demonstrate Git branching and PR workflow
* Improve backend engineering skills

---

# Current Practice Focus

This project was primarily built to practice:

* AWS SDK interaction using boto3
* Backend API development
* FastAPI fundamentals
* REST API design
* Cloud resource lifecycle management
* Git branching and PR workflow
* Modular backend architecture

---

# Future Improvements

Potential future enhancements:

* Upload/download files to S3
* Presigned URLs
* Better exception handling
* Authentication & authorization
* Logging
* Docker support
* Deployment on EC2
* DynamoDB integration
* Background tasks
* Pagination & filtering

---

# Author

Nikhar Sachdeva
