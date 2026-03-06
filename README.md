# Book Notes API (FastAPI Backend)

## Overview

This project is a simple backend API built using FastAPI.
It allows users to manage a collection of books by performing basic CRUD operations (Create, Read, Update, Delete).

The API stores book data in a SQLite database using SQLAlchemy ORM and validates request data using Pydantic schemas.

---

## Features

* Create a new book
* View all books
* View a specific book by ID
* Update book details
* Delete a book
* Data validation using Pydantic
* Persistent storage using SQLite database

---

## Technologies Used

* FastAPI – Backend framework
* Pydantic – Data validation
* SQLAlchemy – ORM for database interaction
* SQLite – Lightweight database

---

## Project Structure

book-project
│
├── main.py – FastAPI application entry point
├── database.py – Database connection setup
├── models.py – Database table definitions
├── schemas.py – Request and response schemas
└── routers/
    └── books.py – Book-related API routes

---

## Installation

1. Clone the repository or download the project.

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment:

Windows:
venv\Scripts\activate

4. Install dependencies:

pip install fastapi uvicorn sqlalchemy

---

## Run the Server

Start the FastAPI server using:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

---

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

---

## API Endpoints

| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| GET    | /books      | Get all books       |
| GET    | /books/{id} | Get a specific book |
| POST   | /books      | Add a new book      |
| PUT    | /books/{id} | Update a book       |
| DELETE | /books/{id} | Delete a book       |

---

## Future Improvements

* User authentication using JWT
* User accounts with personal book collections
* Pagination for large datasets
* Docker containerization
* Integration with React frontend

---

## Author

Bhagyasree Muni
