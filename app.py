from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Logika przetwarzania formularza
    print(f"Otrzymano wiadomość od {name} ({email}): {message}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
