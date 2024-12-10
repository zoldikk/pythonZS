from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

def message_txt():
    url = 'https://pastebin.com/raw/6kSzRLST'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return 'error code'

def load_ids(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_id(filename, ids):
    with open(filename, 'w') as file:
        json.dump(ids, file)

@app.route('/add_uid', methods=['POST'])
def add_uid():
    uid = request.json.get('uid')  # استلام الـ UID من الطلب
    if not uid:
        return jsonify({"error": "UID is required"}), 400

    filename = 'ids.json'
    ids = load_ids(filename)

    if uid in ids:
        return jsonify({"message": "🚫 الـ UID موجود بالفعل."}), 400
    else:
        ids.append(uid)
        save_id(filename, ids)
        msg = message_txt()
        return jsonify({"message": f"✅ تم حفظ الـ UID بنجاح.", "info": msg}), 200

if __name__ == '__main__':
    app.run(debug=True)
