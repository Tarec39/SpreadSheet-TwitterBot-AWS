import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet:
    def __init__(self):
        scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        sheetName = "スプレッドシートの名称"  #ここに入れてください。
        self.sheet = client.open(sheetName).sheet1

    def findTargetCell(self) :
        sheet = self.sheet

        AllSheetData = sheet.get_all_values()
        
        FirstCell = AllSheetData[0][1]

        for i in range(len(AllSheetData)):
            #投稿回数がすべて同じのとき
            if(AllSheetData[i][0]==''):
                targetTweet = AllSheetData[0][0]
                targetCount = AllSheetData[0][1]
                targetRow = 0
                break
             #投稿回数の1番目 と 投稿回数のx番目を 比較
            if(FirstCell > AllSheetData[i][1]):
                targetTweet = AllSheetData[i][0]
                targetCount = AllSheetData[i][1]
                targetRow = i
                break

        
        return targetTweet, targetRow, targetCount 

        # if FirstCell > AllSheetData[i][1]:

        

    def updateCell(self, row, value):
        print('[Start] Update Cell')
        sheet = self.sheet
        self.row = row
        self.value = value

        updatedValue = str(int(self.value)+1)

        print('CELL    {}:2'.format(self.row+1))
        print('UPDATED {} → {}'.format(value, updatedValue))

        sheet.update_cell(self.row+1, 2, updatedValue)

        return True