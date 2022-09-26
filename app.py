import requests

from flask import Flask, request, jsonify
from flask_restful import Api

import config


app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "Hello! :-)"


@app.route("/<username>/repos", methods=["GET"])
def get_repos(username):
    if request.method == "GET":
        r = requests.get(f"{config.URL}/users/{username}/repos")
        result = []

        for item in r.json():
            result.append(item.get("name"))

        return jsonify(
            {
                "repos": result
            }
        ), 200

    return jsonify(
        {
            "result": "unknown error"
        }
    )

@app.route("/<username>/<repo_name>/issue", methods=["POST"])
def post_issue(username, repo_name):
    if request.method == ["POST"]:
        r = requests.post(
            url=f"{config.URL}/repos/{username}/{repo_name}/issues",
            json=(
                {
                    "title": "test issue title",
                    "body": "test issue text"
                }
            )
        )
        print("\nr.status_code = ", r.status_code)
        return jsonify(
            {
                "issue created": True
            }
        ), 201

    return jsonify(
        {
            "issue created": False,
            "reason": "unknown error"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
