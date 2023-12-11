# テスト ID

WAIC-TEST-0054-01

# テストのタイトル

aria-labelによるラベルの提供(可視ラベルが使用できないbutton要素)

# テストの目的

button 要素に対して aria-label を使用して名前 (name) を与えた場合に、名前 (name) が認識され、通知されるかどうかを確認する

# テストの対象となる達成基準 (複数)

4.1.2

# 関連する達成方法 (複数)

ARIA14

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0054-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0054-01.html)

# テストコードのソース (抜粋)

```HTML
<div id="box">
   これはポップアップボックスです。
   <button aria-label="閉じる" onclick="document.getElementById('box').style.display='none';" class="close-button">X</button>
</div>
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順

テスト不要

## 期待される結果

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

1. 「ポップアップボックスを表示する」リンクを押下
2. 表示されたポップアップボックス内を読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)

ボタンに対して「閉じる」という名前が通知される

# テスト実施時の注意点 (音声閲覧環境)

button要素の内容`X`は読み上げられないこと

# 関連する要素や属性

aria-label属性
