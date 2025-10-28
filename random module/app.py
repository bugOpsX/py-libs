from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    min_val = int(data['min'])
    max_val = int(data['max'])
    random_num = random.randint(min_val, max_val)
    return jsonify({'number': random_num})

if __name__ == '__main__':
    app.run(debug=True)
