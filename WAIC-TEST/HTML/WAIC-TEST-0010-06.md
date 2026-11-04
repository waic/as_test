# テスト ID

WAIC-TEST-0010-06

# テストのタイトル

データセルと見出しセル (scope 属性あり : 行見出し)

# テストの目的

scope 属性を指定した場合、テーブルのデータセルと見出しセル (行見出し) が関連付いているかの確認

# テストの対象となる達成基準 (複数)

1.3.1

# 関連する達成方法 (複数)

H63

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0010-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0010-02.html)

# テストコードのソース (抜粋)

```html
<div>
<table>
<caption>Contact Information</caption>
<tr>
<td></td>
<td>First Name</td>
<th scope="col">Last Name</th>
<td>City</td>
</tr>
<tr>
<td>1.</td>
<td>Joel</td>
<td>Garner</td>
<td>Pittsburgh</td>
</tr>
<tr>
<td>2.</td>
<th scope="row">Clive</th>
<td>Lloyd
</td>
<td>Baltimore</td>
</tr>
<tr>
<td>3.</td>
<td>Gordon</td>
<td>Greenidge</td>
<td>Houston</td>
</tr>
</table>
</div>

```

# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順と期待される結果 (音声閲覧環境)

## テスト手順 1

“Clive” という内容のデータセルへ移動し、読み上げ内容を確認する

## 期待される結果 1

データセルの内容とともに、見出しセルの内容 “Clive” が読み上げられる

## テスト手順 2

セル “Greenidge” から同じ行のセル “Gordon” へ移動し、読み上げ内容を確認する

## 期待される結果 2

“Clive” は読み上げられない

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

値に "row" を持つ scope 属性, th 要素 , td 要素
