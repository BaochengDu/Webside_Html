from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "fgF3kVYhDVpwzxaPOiTkdgNk"
SECRET_KEY = "yjd7eOMLPLOY0Qgy5BZnuIkbnAyUzHF3"

@app.route('/')
def home():
    return "✅ Baidu Voice Proxy Running"

@app.route('/baidu_token')
def get_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET_KEY
    }
    r = requests.post(url, params=params)
    resp = r.json()
    return jsonify(resp), 200, {"Access-Control-Allow-Origin": "*"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
