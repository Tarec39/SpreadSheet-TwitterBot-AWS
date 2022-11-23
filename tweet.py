import json
from requests_oauthlib import OAuth1Session
import boto3


class Tweet: 
    # 初期処理
    def __init__(self):
        #パラメーターストア からトークンを取得
        ssm_client = boto3.client('ssm')
        response = ssm_client.get_parameter(
            Name='/credentials/twitter',
            WithDecryption=True
        )
        twitter_parameters = json.loads(response['Parameter']['Value'])

        #トークンの格納
        consumer_key = twitter_parameters['consumer_key']
        client_secret = twitter_parameters['client_secret']
        access_token = twitter_parameters['access_token']
        access_token_secret = twitter_parameters['access_token_secret']

        #TwitterAPIのOAuthを宣言
        self.oauth = OAuth1Session(
            consumer_key, 
            client_secret,
            access_token,
            access_token_secret
            )

    # ツイートする処理
    def tweet(self, text):
        print('[Start] Start Tweet')
        payload = {'text':text}
        response = self.oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )
        if response.status_code == 201:
            print("[Success] {} {}".format(response.status_code, response.text))
            return True
        else:
            raise Exception(
                "[Error] {} {}".format(response.status_code, response.text)
            )