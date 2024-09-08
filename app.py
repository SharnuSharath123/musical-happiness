# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
    # Process feedback (e.g., save to a database)
    return 'Thank you for your feedback!'

if __name__ == '__main__':
    app.run(debug=True)
