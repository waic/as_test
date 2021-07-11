

# テスト ID
WAIC-TEST-0028-02

# テストのタイトル
構造を示すマークアップに基づいてコンテンツを配置

# テストの目的
スタイルシートが適用されている状態でも、スタイルシート適用前の HTML 文書構造の意味のある順序を維持することが出来ているかの確認。

# テストの対象となる達成基準 (複数)
2.4.1
1.3.2
1.4.5
1.4.9

# 関連する達成方法 (複数)
C6

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0028-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0028-02.html)

# テストコードのソース (抜粋)
```html
<a href="#" class="box">
  <h2 class="title">製品</h2>
  <p class="date">2021年6月9日</p>
  <p class="description">製品情報についておしらせします。</p>
</a>
```

```css
.title {
	position: absolute;
	top: 1em;
}
.date {
	position: absolute;
	top: 0;
}
.description {
	position: absolute;
	top: 5em;
}
.box {
	display: block;
	position: relative;
	border: solid 1px #ccc;
	height: 150px;
}
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを開いて、その内容を確認。
ユーザエージェントでスタイルシートを無効にし、その内容を確認。

# 期待される結果 (音声閲覧環境)
ユーザエージェントによるスタイルシートの適用の有無にかかわらず、読み上げの順序が変化しない。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
a要素, h2要素, p要素
