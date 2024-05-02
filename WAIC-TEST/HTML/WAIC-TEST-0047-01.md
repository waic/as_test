# テスト ID

WAIC-TEST-0047-01

# テストのタイトル

テキストフィールドにラベルを付けるために aria-labelledby を使用する

# テストの目的

フォームラベルを提供するために aria-labelledby 属性が使用できることの確認

# テストの対象となる達成基準

1.3.1, 4.1.2

# 関連する達成方法 (複数)

ARIA16

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0047-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0047-01.html)

# テストコードのソース (抜粋)

```HTML
<p id="sitesearch">サイト内検索</p>
<input name="searchtxt" type="text" aria-labelledby="sitesearch">
<input name="searchbtn" id="searchbtn" type="submit" value="検索">
```
# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テキストフィールドにフォーカスを合わせ、読み上げ内容を確認

# 期待される結果 (音声閲覧環境)

「サイト内検索」としてテキストフィールドのラベルが通知される

# テスト実施時の注意点 (音声閲覧環境)

ブラウズモードでの通知がなくても、フォーカスモードで通知があれば問題ない

# 関連する要素や属性

aria-labelledby属性、id属性、aria-labelledby 属性が指定された input 要素
