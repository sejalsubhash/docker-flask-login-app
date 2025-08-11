

# 🐳 Dockerized Flask Login Application

A simple user login and registration application built with **Flask** and **MySQL**, containerized using **Docker**.
This app demonstrates how to:

* Connect a Flask application to a MySQL database using Docker containers
* Create a user authentication system with registration, login, and password encryption
* Use Docker networks to enable container communication
* Run the full stack with **Docker Compose** for simplified orchestration

---

## 📦 Prerequisites

* Docker installed on your system
* Docker Compose installed
* Git installed

---

## 🚀 Steps to Run

You can run this project in **two ways**:

1. **Manual Docker Commands** (Step-by-step)
2. **Docker Compose** (One command)

---

### **Option 1 — Manual Docker Commands**

#### 1️⃣ Clone the Project

```bash
git clone https://github.com/your-username/docker-flask-login-app.git
cd docker-flask-login-app
```

> Replace `your-username` with your actual GitHub username.

#### 2️⃣ Pull MySQL Docker Image

```bash
sudo docker pull mysql:8.0
```

#### 3️⃣ Create Docker Network

```bash
sudo docker network create <network_name>
```

#### 4️⃣ Run MySQL Container

```bash
sudo docker run -d \
  --name mysql \
  --network <network_name> \
  -e MYSQL_ROOT_PASSWORD=<mysql-password> \
  -e MYSQL_DATABASE=<database_name> \
  -p 3306:3306 \
  mysql:8.0
```

#### 5️⃣ Configure `config.py` in Flask App

```python
DB_HOST = 'mysql'  # MySQL container name
DB_USER = 'root'
DB_PASSWORD = '<mysql-password>'
DB_NAME = '<database_name>'
```

#### 6️⃣ Build Flask App Image

```bash
sudo docker build -t docker-flask-login-app .
```

#### 7️⃣ Run Flask App Container

```bash
sudo docker run -d \
  -p 5000:5000 \
  --network <network_name> \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=<mysql_password> \
  -e MYSQL_DB=<database_name> \
  docker-flask-login-app:latest
```

#### 8️⃣ Access the App

```
http://<your-ec2-public-ip>:5000
```

---

### **Option 2 — Run with Docker Compose** 🐙

#### 1️⃣ Clone the Project

```bash
git clone https://github.com/your-username/docker-flask-login-app.git
cd docker-flask-login-app
```

#### 2️⃣ Ensure `docker-compose.yml` looks like this:

```yaml
version: "3.8"

services:
  mysql:
    container_name: mysql
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: "login_app"
      MYSQL_ROOT_PASSWORD: "root"
    ports:
      - "3306:3306"
    networks:
      - my-network

  flask:
    build:
      context: .
    container_name: dockerized-login-app
    ports:
      - "5000:5000"
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_DB: login_app
    depends_on:
      - mysql
    networks:
      - my-network

networks:
  my-network:
    driver: bridge
```

#### 3️⃣ Start the App

```bash
docker-compose up --build -d
```

#### 4️⃣ Access the App

```
http://localhost:5000
```

---

## 📁 Project Structure

```
docker-flask-login-app/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html

```

---

## 🔐 Login Features

* ✅ Register new users
* 🔐 Secure login with credentials
* 🗃 MySQL database integration for storing user data
* 🔒 Passwords stored securely using hashing (Werkzeug)

---

## 🧹 Cleanup

To stop and remove containers and network:

```bash
docker-compose down
```

Or, if running manually:

```bash
docker stop <container_name_or_id>
docker rm <container_name_or_id>
docker network rm <network_name>
```


