# 🐳 Dockerized Flask Login Application

A simple user login and registration application built with **Flask** and **MySQL**, containerized using **Docker**. This app demonstrates how to:

- Connect a Flask application to a MySQL database using Docker containers
- Create a user authentication system with registration, login, and password encryption
- Use Docker networks to enable container communication

---

## 📦 Prerequisites

- Docker installed on your system
- Git installed

---

## 🚀 Steps to Run

### 1. 📥 Clone the Project

```bash
git clone https://github.com/your-username/docker-flask-login-app.git
cd docker-flask-login-app
````

> Replace `your-username` with your actual GitHub username or use the correct repository URL.

---

### 2. 🐬 Pull the MySQL Docker Image

```bash
sudo docker pull mysql:8.0
```

---

### 3. 🌐 Create Docker Network

Create a custom Docker bridge network so that both containers can communicate easily:

```bash
sudo docker network create <network_name>
```

---

### 4. 🛠️ Run MySQL Container

```bash
sudo docker run -d \
  --name mysql \
  --network <network_name> \
  -e MYSQL_ROOT_PASSWORD=<mysql-password> \
  -e MYSQL_DATABASE=<database_name> \
  -p 3306:3306 \
  mysql:8.0
```

> ✅ You can update the database name, user, and password as per your needs.

---

### 5. 🔧 Configure `config.py` in Flask App

Ensure `config.py` inside your cloned repo looks like:

```python
DB_HOST = 'mysql'  #mysql container name
DB_USER = 'root'
DB_PASSWORD = '<mysql-password>'
DB_NAME = '<database_name>'
```

---

### 6. 🛠️ Build Flask App Docker Image

```bash
sudo docker build -t docker-flask-login-app .
```

---

### 7. 🏃‍♂️ Run Flask App Container

```bash
 sudo docker run -d -p 5000:5000 --network <network_name> -e MYSQL_HOST=mysql -e MYSQL_USER=root -e MYSQL_PASSWORD=<mysql_password> -e MYSQL_DB=<database_name> docker-flask-login-app:latest
```

---

### 8. 🌐 Access the Application

Visit your browser at:

```
http://<your-ec2-public-ip>:5000
```

Replace `<your-ec2-public-ip>` with your actual EC2 instance public IP address.

---

## 🧹 Cleanup

To stop and remove containers and the network:

```bash
sudo docker stop <container_name or container_Id>
sudo docker rm <container_name or container_Id>
sudo docker network rm <network_name>
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
├── templates/
│   └── login.html
│   └── register.html
│   └── dashboard.html
└── static/
    └── style.css
```

---

## 🔐 Login Features

- ✅ Register new users  
- 🔐 Secure login with credentials  
- 🗃️ MySQL database integration for storing user data  
- 🔒 Passwords stored securely using encryption


