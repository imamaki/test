import urllib.request
import datetime
import requests
import os

#201812111100.zip～20181211145.zipのファイルは存在するのでそれで確認
dateS='201812111100'        #開始したい年月日時分を設定する。
dateE='201812111300'        #終了したい年月日時分を設定する。
interval=15                  #取得間隔を指定

dt1 = datetime.datetime.strptime(dateS, '%Y%m%d%H%M')
dt2 = datetime.datetime.strptime(dateE, '%Y%m%d%H%M')

i=1     #カウント用
#for count in  range(100):
#テスト用for文　テスト終了後While文のみ残すこと
while (dt1 <= dt2):
    #設定期間のファイルを指定した間隔でファイルをダウンロードする。

    date=dt1.strftime('%Y%m%d%H%M')
    # URLを指定
    url='https://www.wds.emis.go.jp/dmatshiryo/docs/sip/emis-sip_'+date+'.zip'
    # 保存したいファイルのパスを指定
    save_name = 'C:\\Users\\今牧真理子\\Google ドライブ\\test\\emis-sip_'+date+'.zip'

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('No.' + str(i)+':'+str(err))
    else:
        if os.path.exists(save_name):
            #ファイルがダウンロードされている場合（保存先にファイルが存在する場合）
            print('No.' + str(i)+':emis-sip_'+date+'.zipのファイルが存在します。')
        else:
            #保存先にファイルが存在しない場合
            print('No.' + str(i)+':'+str(url)+'のダウンロード開始します。')
            #ダウンロードの実行
            urllib.request.urlretrieve(url,save_name)

    i+=1
    dt1=dt1+datetime.timedelta(minutes=interval)