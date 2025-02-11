from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json 
    
    response = requests.post('http://192.168.56.101:5002/receive_data', json=data)
    if response.status_code == 200:
        return jsonify({"message": "Data sent successfully!", "stored_data": response.json()})
    else:
        return jsonify({"error": "Failed to send data to VM2"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)