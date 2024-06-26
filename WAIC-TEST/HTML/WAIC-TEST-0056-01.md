# テスト ID

WAIC-TEST-0056-01

# テストのタイトル

レイアウトデザインのためのスペーサー画像ではなく、CSS を使用する（マージンとパディング）

# テストの目的

スペーサー画像を使用することなく、CSS のマージンを使用して表組の外側にスペースが追加され、パディングを使用して表組のセルの内側にスペースが追加されるかの確認

# テストの対象となる達成基準

1.1.1

# 関連する達成方法 (複数)

C18

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0056-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0056-01.html)

# テストコードのソース (抜粋)

```HTML
<p>スタイルシートが適用された表組</p>
<table class="table">
  <caption>「Web 開発」カテゴリの書籍</caption>
    <thead>
      <tr>
        <th scope="col">タイトル</th>
        <th scope="col">著者</th>
        <th scope="col">発行日</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Web 標準について正しく考える方法</td>
        <td>アンドリュー・スタノビッチ</td>
        <td>2024年1月</td>
      </tr>
    </tbody>
</table>
    
<p>スタイルシートが無効な表組</p>
<table>
  <caption>「Web 開発」カテゴリの書籍</caption>
    <thead>
      <tr>
        <th scope="col">タイトル</th>
        <th scope="col">著者</th>
        <th scope="col">発行日</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Web 標準について正しく考える方法</td>
        <td>アンドリュー・スタノビッチ</td>
        <td>2024年1月</td>
      </tr>
    </tbody>
</table>
```

```CSS
.table {
            margin: 1em;
            border-collapse: collapse;
        }
        .table td, .table th {
            padding: 1em;
            border: 1px solid #000;
        }
```

# テスト手順 (視覚閲覧環境)

テストファイルを開き、「スタイルシートが適用された表組」と「スタイルシートが無効な表組」の表示を確認する

# 期待される結果

「スタイルシートが適用された表組」では、マージンとパディングが使用されて外側とセル内にスペースがあり、「スタイルシートが無効な表組」ではマージンとパディングの設定が適用されていないことが確認できる

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テスト不要

# 期待される結果

なし

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

なし
