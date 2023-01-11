# テスト ID
WAIC-TEST-0035-04

# テストのタイトル
CSS による装飾画像の付加（content プロパティ）

# テストの目的
CSS の疑似要素で指定された装飾目的の画像が読み上げられない

# テストの対象となる達成基準 (複数)
1.1.1

# 関連する達成方法 (複数)
C9

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0035-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0035-04.html)

# テストコードのソース (抜粋)
```CSS
li a {
	display: block;
}
li a:before {
	content: '';
	display: inline-block;
	width: 16px;
	height: 18px;
	background: url(./img/WAIC-CODE-0035-04-01.png) no-repeat 50% 50% ;
    margin-right: .5em;
}
li a:after {
	content: '';
	display: inline-block;
	width: 16px;
	height: 13px;
	background: url(./img/WAIC-CODE-0035-04-02.png) no-repeat 50% 50% ;
    margin-left: .5em;
}
```
```HTML
<ul>
	<li><a href="#">リンクテキスト1</a></li>
	<li><a href="#">リンクテキスト2</a></li>
    <li><a href="#">リンクテキスト3</a></li>
</ul>
```
# テスト手順 (視覚閲覧環境)
なし

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認。

# 期待される結果 (音声閲覧環境)
画像として読み上げられない。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし
