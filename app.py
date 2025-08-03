from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import config

app = Flask(__name__)
app.secret_key = 'secret123'

# MySQL configuration
app.config.from_object(config)
mysql = MySQL(app)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            flash("Passwords do not match!", "danger")
            return redirect('/register')

        hashed_password = generate_password_hash(password)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cur.close()
        flash("modal:Successfully registered!", "success")  # 'modal:' prefix to trigger JS modal
        return redirect('/register')  # You can also redirect to /login

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            flash("Invalid credentials!", "danger")
            return redirect('/login')
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
