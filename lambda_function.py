from spreadsheet import SpreadSheet
from tweet import Tweet

def lambda_handler(event, context):
    spreadSheet = SpreadSheet()
    tweet = Tweet()
    TweetText, Row, Value = spreadSheet.findTargetCell()
    
    print("内容: {}, セル: {}-2, 元値: {}".format(TweetText, Row+1, Value))
    tweet.tweet(TweetText)

    
    try:
        spreadSheet.updateCell(Row, Value)
        print('[Success] Update is Done')
    except:
        print('[Fail] Update is Failed----')