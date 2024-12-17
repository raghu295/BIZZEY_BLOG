# BIZZEY_BLOG
# BIZZEY_BLOG

This repository contains the code for the BIZZEY_BLOG project.

## Project Description

BIZZEY_BLOG is a blogging platform where users can create, read, update, and delete blog posts. It also includes a contact form for users to send messages.

## Technologies Used

- Python 3
  - Used for the backend programming language
- Django
  - Used for the backend framework
- Django REST Framework
  - Used for API development, serialization, and validation
- SQLite
  - Used for the database
- Git
  - Used for version control
- Docker
  - Used for containerization
- Swagger
  - Used for API documentation

## Features

- User authentication
- Create, read, update, and delete blog posts
- Contact form for users to send messages
- API documentation with Swagger

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Docker (optional)

### Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd BIZZEY_BLOG

2. Create a virtual environment:
   python3 -m venv venv

3. Activate the virtual environment:
   On Windows:
venv\Scripts\activate
   On macOS/Linux:
source venv/bin/activate

4. Install the requirements:
   pip install -r requirements.txt

5. Apply the migrations:
   python manage.py migrate

6. Run the server:
   python manage.py runserver

### Running with Docker

1. Build the Docker image:
   docker build -t bizzy_blog .

2. Run the Docker container:
   docker run -p 8000:8000 bizzy_blog

### Usage

Access the application at http://localhost:8000
Access the admin panel at http://localhost:8000/admin
Access the API documentation at http://localhost:8000/swagger/

### Contributing

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature-branch)
Open a pull request
