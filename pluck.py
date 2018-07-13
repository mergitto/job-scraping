import pandas as pd
import sys
from time import sleep
import mojimoji

df = pd.read_csv(sys.argv[1], header=None)

df = df[0]
df = df.dropna()

df = df.str.replace("\<.+?\>", "")
df = df.str.replace("\[.+?\]", "")
df = df.str.replace("\【.+?\】", "")
df = df.str.replace("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "")
df = df.str.replace("[#＃][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー]+", "")
df = df.str.replace("[@＠][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー_]+", "")
df = df.str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "")

df_text_list = []
for text in df:
    df_text_list.append(mojimoji.zen_to_han(text.lower(), kana=False, digit=False))

df = pd.DataFrame(df_text_list)

df.to_csv(sys.argv[2], index=None, header=None)

