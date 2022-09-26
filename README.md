# Github FlaskAPI

Simple flask API to interact with github API

## Description

Using this API, you can get a list of the user's public repositories on github and create an issue.

## Getting Started

### Installing

* SSH: 
git clone git@github.com:Vir2S/github_api.git
* HTTPS: 
git clone https://github.com/Vir2S/github_api.git
* Put your TOKEN in config.py 
* pip install -r requirements.txt

### Executing program

```
flask run 
```
OR RUN WITH DEBUG
```
flask --debug run
```
OR 
```
python3 app.py
```

## Sample requests

GET list repositories for github user
```c
curl -X GET http://"127.0.0.1:5000/<username>/repos"
```
Sample output
```json
{
  "repos": [
    "repo_1",
    "repo_2",
    ...
  ]
}
```
POST issue to repo
```c
curl -X POST http://127.0.0.1:5000/<GIT_USERNAME>/<GIT_REPONAME>/issue -H 'Content-Type:application/json' -d '{"title":"issue title","body":"test issue text"}'
```
Sample body for POST request from [GitHub Docs](https://docs.github.com/en/rest/issues/issues#create-an-issue)
```json
-d '{
    "title": "Found a bug",
    "body": "I'm having a problem with this.",
    "assignees": ["octocat"],
    "milestone": 1,
    "labels": ["bug"]
    }'
```
Sample output
```json
{
  "issue_created": true
}
```

## Enjoy
