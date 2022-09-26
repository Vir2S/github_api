import requests

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

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


@app.route("/<username>/<repo_name>/issue")
def post_issue(username, repo_name):
    if request.method == ["POST"]:
        r = requests.post(
            url=f"{config.URL}/{username}/{repo_name}/issues",
            json=(
                {
                    "title": "test issue title",
                    "body": "test issue text"
                }
            )
        )

        return jsonify(
            {
                "issue created": True
            }
        )


if __name__ == "__main__":
    app.run(debug=True)
