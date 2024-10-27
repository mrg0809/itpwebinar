from flask import Flask, render_template, request, redirect, url_for
from data import contacts, leads
from utils import process_registration

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts, leads=leads)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registrant = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
        }
        process_registration(registrant, contacts, leads)
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)