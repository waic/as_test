# テスト ID

WAIC-TEST-0093-01

# テストのタイトル

テキストを含むコンタクトフォームの拡大縮小


# テストの目的

コンタクトフォーム（h1 要素、p 要素、label 要素、type="text" および type="submit" の input 要素）に em でフォントサイズを指定し、ブラウザの文字サイズ変更機能を用いて文字サイズを拡大した場合、テキストがより大きく表示されるかを確認

# テストの対象となる達成基準 (複数)

1.4.4

# 関連する達成方法 (複数)


# テストコード (テストファイルへのリンク)

[WAIC-CODE-0093-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0093-01.html)

# テストコードのソース (抜粋)

```HTML
<h1><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="WAICロゴ" width="30" height="30">連絡先</h1>
<p><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15">必要事項をご記入の上、送信ボタンを押してださい。フォームの項目はすべて必須です。</p>
<label for="fname"><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15">姓:</label><input type="text" name="fname" id="fname"><br>
<label for="lname"><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15">名:</label><input type="text" name="lname" id="lname"><br>
<label for="phone"><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15">電話番号:</label><input type="text" name="phone" id="phone"><br>
<label for="email"><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15">メールアドレス:</label><input type="text" name="email" id="email"><br>
<img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="" width="15" height="15"><input type="submit" name="Submit" value="送信" id="Submit">
```

```CSS
h1 {
	font-size: 2em;
}
p, label, input {
	font-size: 1em;
}
```

# テスト手順 (視覚閲覧環境)

1. 入力フォームの「姓：」に任意のテキストを入力する
2. ズーム機能ではなく、ブラウザの文字サイズ変更機能を用いて、文字サイズのみを拡大する

# 期待される結果 (視覚閲覧環境)

h1 要素、p 要素、label 要素、type="text" および type="submit" の input 要素のテキストが、それぞれの行頭にある画像よりも大きく表示されることを確認する。

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テスト不要

# 期待される結果 (音声閲覧環境)

なし

# 関連する要素や属性

なし