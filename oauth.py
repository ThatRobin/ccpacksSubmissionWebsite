import requests as requests


class Oauth(object):
    client_id = "843191707071938581"
    client_secret = "LolEc9hYS8f0AfnkII2chEAYVePBfjme"
    scope = "identify%20guilds"
    redirect_uri = "http://127.0.0.1:5000/login"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=843191707071938581&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Flogin&response_type=code&scope=identify"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api/"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id":Oauth.client_id,
            "client_secret":Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri":Oauth.redirect_uri,
            "scope":Oauth.scope
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        access_token = requests.post(url=Oauth.discord_token_url, data=payload, headers=headers)
        json = access_token.json()
        access_token.raise_for_status()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        user_object = requests.get(url, headers=headers)
        user_json = user_object.json()
        return user_json