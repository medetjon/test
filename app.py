from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    numbers = data.get('numbers', [])
    return jsonify({'sum': sum(numbers)})

if __name__ == '__main__':
    app.run(debug=True)
