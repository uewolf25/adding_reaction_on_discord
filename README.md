# 特定の人にあるリアクションをするBot
特定の人に予めセットしておいたリアクションを付与します。  
特定の人のidに反応してそのメッセにリアクションを付与。

## 環境
- 言語
  - Python:3.7.9
- Libraries
  - discord.py
  - dotenv(ローカルで使用する場合)
- heroku(サーバ)
  - pythonのversionは3.7.9

## 実行
Discordのbotの導入方法は各自探して下され。  
そしてトークンを取得から以下の動作を試してみてください。  

ローカルで動作させる場合は、
```
.env
apiKey.py
emoji_list_file.py
main.py
```
が最低限必要です。  

`.en-temp`に任意の環境変数を用意してください。  
`emoji_list_file.py`に付与したい絵文字をセットします。(ただし、１つのメッセージに付与できる最大数は20個までです。)  

`message.author.id`で対象の人と比較ができます。(型は**数値**で)

`python main.py`で待機状態になります。

## 注意等
- 環境変数はheroku側で設定できる。→[参考](https://qiita.com/opiyo_taku/items/a753623a4a565424dfec)  
- Pythonを使用する場合、サポートされているversionは決まってる。
  - 3.9.1
  - 3.8.7
  - 3.7.9
  - 3.6.12
  - 2.7.18  
これ以外をのversionを設定すると、Deploy時にBuildエラー。

