
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search_user():
    username = request.form.get('username')
    if not username:
        return jsonify({'error': 'No username provided.'}), 400

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(f"{username}.json", "w") as f:
            json.dump(data, f, indent=4)
        return jsonify(data), 200
    else:
        return jsonify({'error': f"GitHub API returned status code {response.status_code}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST -d "username=alina199826" http://127.0.0.1:5000/search
# для проверки