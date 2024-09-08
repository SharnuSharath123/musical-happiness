# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
    # For simplicity, we'll just print the feedback to the console.
    # In a real application, you might save this to a database or file.
    print(f"User Feedback: {user_feedback}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
