from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {}

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  
    
    data_id = len(data_store) + 1
    data_store[data_id] = data
    print(f"Stored Data: {data_store}")
    
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)