import pandas as pd
import sys
from time import sleep
import gc

df = pd.read_csv(sys.argv[1])

df = df[df['id'] != 'id']
df = df['tweet']
df = df.dropna()

df = df.str.replace("\<.+?\>", "", regex=True)
df = df.str.replace("\[.+?\]", "", regex=True)
df = df.str.replace("\【.+?\】", "", regex=True)
df = df.str.replace("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "", regex=True)
df = df.str.replace("[#＃][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー]+", "", regex=True)
df = df.str.replace("[@＠][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー_]+", "", regex=True)
#df = df.str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "", regex=True)

df.to_csv(sys.argv[2], index=None)

