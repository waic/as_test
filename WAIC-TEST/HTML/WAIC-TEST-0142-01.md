# テスト ID

WAIC-TEST-0142-01

# テストのタイトル

検索結果にステータスメッセージを提供するために role="status" を使用する。

# テストの目的

role="status" を持つ要素の内容が更新された際に、変更が通知されることを確認する。

# テストの対象となる達成基準 (複数)

4.1.3

# 関連する達成方法 (複数)

ARIA22

# テストコードのソース (抜粋)

```html
<div role="main">
<div role="search">
<label for="mockinput">次の語と一致する単語を検索:
<input type="text" name="mockinput" id="mockinput" value="オレンジ">
</label>
<button id="btn" onclick="findOrange()">検索</button>
</div>
<h2>結果</h2>
<p role="status" aria-atomic="true" id="resultsmsg"></p>
</div>
```

```JavaScript
function findOrange () {
document.getElementById("resultsmsg").innerHTML = "0 件の結果が返されました"
}
```

# テスト手順 (視覚閲覧環境)

テストファイルを開き、検索フィールドに初期値「オレンジ」が入力されている状態で「検索」ボタンをクリックし表示内容を確認する。

# 期待される結果 (視覚閲覧環境)

「結果」の下に「0 件の結果が返されました」というテキストが表示される。

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テストファイルを開き、検索フィールドに初期値「オレンジ」が入力されている状態で「検索」ボタンをクリックし通知内容を確認する。

# 期待される結果 (音声閲覧環境)

「検索」ボタンを実行した後、フォーカス位置の変更に関わらず、「0 件の結果が返されました」と通知される。

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

role 属性
