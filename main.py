from flask import Flask, request, render_template, redirect, session
from oauth import Oauth

app = Flask(__name__)


@app.route("/", methods=["get"])
def index():
    return redirect(Oauth.discord_login_url)


@app.route("/login", methods=["get"])
def login():
    code = request.args.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    username = "Welcome, "+user_json.get("username") + "#" + user_json.get("discriminator")
    return username


if __name__ == "__main__":
    app.run(debug=True)
