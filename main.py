import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def get_gpt_response():
    prompt = request.args.get('prompt')
    if prompt is None:
        return jsonify({"error": "No prompt provided"}), 400
    api_url = "https://joshweb.click/new/gpt-4_adv?prompt=" + prompt
    response = requests.get(api_url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
