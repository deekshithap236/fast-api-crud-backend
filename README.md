# FastAPI CRUD API with Docker

This project is a simple CRUD (Create, Read, Update, Delete) API built using **FastAPI** and containerized with **Docker**. It allows you to manage a list of items with basic operations.

---

## Features

- **Create**: Add a new item.
- **Read**: Retrieve a single item or all items.
- **Update**: Modify an existing item.
- **Delete**: Remove an item.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional but recommended)

---

## Project Structure

    fastapi-crud-docker/
    │
    ├── app/
    │   ├── __init__.py
    │   └── main.py
    │
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md

---

## Setup and Run

### 1. Clone the Repository

    git clone https://github.com/your-username/fastapi-crud-docker.git
    cd fastapi-crud-docker

### 2. Build and Run with Docker

#### Using Docker Compose (recommended):

    docker-compose up

#### Using Docker directly:

    docker build -t fastapi-crud-docker .
    docker run -d -p 8000:80 fastapi-crud-docker

### 3. Access the API

The API will be running at `http://localhost:8000`.

---

## API Endpoints

### Create an Item
- **POST** `/items/`
- Request Body:

      {
        "id": 1,
        "name": "Laptop",
        "description": "High-end gaming laptop",
        "price": 1500.0
      }

### Read All Items
- **GET** `/items/`

### Read a Single Item
- **GET** `/items/{item_id}`

### Update an Item
- **PUT** `/items/{item_id}`
- Request Body:

      {
        "id": 1,
        "name": "Laptop",
        "description": "High-end gaming laptop with 32GB RAM",
        "price": 1700.0
      }

### Delete an Item
- **DELETE** `/items/{item_id}`

---

## Example Requests

### Create an Item

    curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Laptop", "description": "High-end gaming laptop", "price": 1500.0}'

### Read All Items

    curl "http://localhost:8000/items/"

### Read a Single Item

    curl "http://localhost:8000/items/1"

### Update an Item

    curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Laptop", "description": "High-end gaming laptop with 32GB RAM", "price": 1700.0}'

### Delete an Item

    curl -X DELETE "http://localhost:8000/items/1"

---

## Stopping the Application

### Using Docker Compose:

    docker-compose down

### Using Docker directly:

    docker stop <container_id>

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

Enjoy building and using your FastAPI CRUD API with Docker! 🚀