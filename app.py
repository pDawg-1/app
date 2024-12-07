from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "password":
            return "Login successful! Welcome, admin."
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

# Data Pull Page
@app.route('/data_pull', methods=['GET', 'POST'])
def data_pull():
    if request.method == 'POST':
        hshd_num = request.form.get('hshd_num')
        # Placeholder: Replace this with a real database query.
        data = {
            "Hshd_num": hshd_num,
            "Basket_num": "12345",
            "Date": "2023-12-01",
            "Product_num": "5678",
            "Department": "Dairy",
            "Commodity": "Milk",
        }
        return render_template('data_pull.html', data=data)
    return render_template('data_pull.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
