

# テスト ID
WAIC-TEST-0028-01

# テストのタイトル
CSSによる表示順序の変更 (positionプロパティ : 左右に配置)

# テストの目的
スタイルシートが適用されている状態でも、スタイルシート適用前の HTML 文書構造の意味のある順序を維持することが出来ているかの確認。

# テストの対象となる達成基準 (複数)
1.3.2, 1.4.5, 1.4.9, 2.4.1

# 関連する達成方法 (複数)
C6

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0028-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0028-01.html)

# テストコードのソース (抜粋)
```html
<div class="box">
  <dl>
    <dt class="menu1">製品</dt>
    <dd class="item1">電話</dd>
    <dd class="item2">コンピュータ</dd>
    <dd class="item3">MP3プレーヤー</dd>
    <dt class="menu2">地域</dt>
    <dd class="item4">東京</dd>
    <dd class="item5">神奈川</dd>
  </dl>
</div>
```

```css
.item1 {
	left: 0;
	margin: 0;
	position: absolute;
	top: 7em;
}
.item2 {
	left: 0;
	margin: 0;
	position: absolute;
	top: 8em;
}
.item3 {
	left: 0;
	margin: 0;
	position: absolute;
	top: 9em;
}
.item4 {
	left: 14em;
	margin: 0;
	position: absolute;
	top: 7em;
}
.item5 {
	left: 14em;
	margin: 0;
	position: absolute;
	top: 8em;
}
.menu1 {
	background-color: #FFFFFF;
	color: #FF0000;
	font-family: sans-serif;
	font-size: 120%;
	left: 0;
	margin: 0;
	position: absolute;
	top: 3em;
}
.menu2 {
	background-color: #FFFFFF;
	color: #FF0000;
	font-family: sans-serif;
	font-size: 120%;
	left: 10em;
	margin: 0;
	position: absolute;
	top: 3em;
}
#box {
	left: 5em;
	position: absolute;
	top: 5em;
}
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
- テストファイルを開いて、その内容を確認。
- ユーザエージェントでスタイルシートを無効にし、その内容を確認。

# 期待される結果 (音声閲覧環境)
ユーザエージェントによるスタイルシートの適用の有無にかかわらず、読み上げの順序が変化しない。

# テスト実施時の注意点 (音声閲覧環境)
* dl, dt, dd 要素は、音声環境にて当該要素であることを確認できるかどうか。
  * スタイルシートの適用有無にかかわらず、当該要素の判別が難しい場合は別の要素を用いたサンプルにする必要があるではないか？

# 関連する要素や属性
dl要素, dt 要素, dd 要素
