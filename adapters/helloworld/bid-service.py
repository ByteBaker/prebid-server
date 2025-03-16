from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bid', methods=['POST'])
def bid():
    json_data = request.get_json(force=True)

    bid_response = {
        "id": f"dummy-response-{json_data['id']}",
        "original_request": json_data,
    }
    
    return jsonify(bid_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
