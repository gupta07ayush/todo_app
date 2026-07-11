# ✅ Todo List App

A simple, clean and persistent Todo List web application built with **Flask** and **SQLite**.

Your tasks are automatically saved and remain available even after you close the browser or restart the application.

## ✨ Features

- Add new tasks quickly
- Mark tasks as complete / incomplete
- Delete tasks
- Clean and responsive UI
- Data persistence using SQLite
- Docker support
- Ready for deployment on Azure App Service

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML + CSS + Jinja2 Templates
- **Production Server**: Gunicorn
- **Containerization**: Docker

## 📁 Project Structure
todo-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .gitignore
├── .dockerignore
├── todos.db               # SQLite database (auto-created)
├── static/
│   └── style.css
└── templates/
└── index.html


## 🚀 Quick Start

### Option 1: Run Locally (Without Docker)

1. Clone the repository:
   git clone https://github.com/gupta07ayush/todo_app.git
   cd todo_app


Create and activate virtual environment:Bashpython -m venv venv
venv\Scripts\activate          # For Windows
# source venv/bin/activate     # For Linux / Mac
Install dependencies:Bashpip install -r requirements.txt
Run the application:Bashpython app.py
Open your browser and visit: http://127.0.0.1:5000


### Option 2: Run with Docker

Build the image:Bashdocker build -t todo-app:latest .
Run the container:Bashdocker run -p 8080:80 -v todo_data:/app todo-app:latest
Open browser: http://localhost:8080


###🐳 Docker Commands

Build Image: docker build -t todo-app:latest .
Run Container: docker run -p 8080:80 todo-app:latest
Stop All Containers: docker stop $(docker ps -q)


### 🚀 Deployment
This project is configured for deployment on Azure App Service using Docker.
Main Steps:

### Push code to GitHub
Build & push Docker image to Azure Container Registry (ACR)
Deploy from ACR to Azure App Service



### 🔮 Future Enhancements

User login & multiple user support
Due dates for tasks
Task categories and priorities
Search functionality
Dark mode support
Export todos as JSON/CSV


📸 Screenshots
<img width="629" height="365" alt="image" src="https://github.com/user-attachments/assets/754cf4a8-53b5-4db6-8a1a-cc5c74f48651" />


### 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the project and submit a Pull Request.

📄 License
This project is licensed under the MIT License.

Made with ❤️ while learning Flask
