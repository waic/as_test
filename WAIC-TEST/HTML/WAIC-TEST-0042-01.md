# テスト ID
WAIC-TEST-0042-01

# テストのタイトル
aria-labelledby による代替テキストの提供（img要素）

# テストの目的
aria-labelledby によって画像の代替テキストが提供されているかの確認

# テストの対象となる達成基準 
1.1.1

# 関連する達成方法 (複数)
ARIA10

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0042-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0042-01.html)

# テストコードのソース (抜粋)
```HTML
<div role="img" aria-labelledby="star_id">
<img src="./img/WAIC-CODE-0042-01.png" alt=""/>
<img src="./img/WAIC-CODE-0042-01.png" alt=""/>
<img src="./img/WAIC-CODE-0042-01.png" alt=""/>
<img src="./img/WAIC-CODE-0042-01.png" alt=""/>
<img src="./img/WAIC-CODE-0042-01-02.png" alt=""/>
</div>
<div id="star_id">五つ星中四つ星</div>
```
# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
はじめにaria-labelledby が設定された画像が、ラベル付けされた ID 属性を代替テキストとして読み上げ、最後にID 属性の内容も読み上げられるかを確認。

# 期待される結果 (音声閲覧環境)
「五つ星中四つ星」が画像の代替テキストと ID 属性の内容として2回読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)
本来、ラベル付けされた内容は代替テキストとして読み上げられるべきであり、ID 属性の内容が2回繰り返し読み上げられることは適切ではない。

# 関連する要素や属性
img要素、alt属性、role属性
