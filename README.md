# job-scraping
就活系のテキストをtwitter api で取得するツール

### 開発環境構築の手順
python3が使える環境を用意

### モジュールの追加
```
pip install requests
pip install requests-oauthlib
```

### configの設定
```
cp config-sample.py config.py
```

### 取得したい文字列を含んだテキストの取得
config.pyのSEARCH_WORD_LIST内に単語を記述
```
vi config.py
```
検索単語を記述したらtweetの抽出処理実行
```
python getJob.py 好きなファイル名.csv
```
抽出したtweetのクレンジング処理
```
python pluck.py ↑で指定したファイル名.csv
```



