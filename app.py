import requests

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "hello"


@app.route("/<username>/repos", methods=["GET"])
def get_repos(username):
    if request.method == "GET":
        r = requests.get(f"https://api.github.com/users/{username}/repos")
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
        print("issue created")


if __name__ == "__main__":
    app.run(debug=True)
