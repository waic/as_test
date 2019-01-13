

# テスト ID
WAIC-TEST-0019-04

# テストのタイトル
リンクの目的の特定 (見出し)

# テストの目的
リンクテキストと先行する見出し要素とを組み合わせて、リンクの目的を特定することができるかの確認

# テストの対象となる達成基準 (複数)
2.4.4

# 関連する達成方法 (複数)
H80

# テストコード (テストファイルへのリンク)
WAIC-CODE-0019-04

# テストコードのソース (抜粋)
```html
<div>
<h2>ロイヤルパームホテル</h2>
<ul class="horizontal">
<li><a href="#">地図</a></li>
<li><a href="#">写真</a></li>
<li><a href="#">アクセス</a></li>
<li><a href="http://waic.jp/">お客様の声</a></li>
<li><a href="#">ご予約</a></li>
</ul>

<h2>ホテルスリーリバーズ</h2>
<ul class="horizontal">
<li><a href="#">地図</a></li>
<li><a href="#">写真</a></li>
<li><a href="#">アクセス</a></li>
<li><a href="#">お客様の声</a></li>
<li><a href="#">ご予約</a></li>
</ul>
</div>

```
# テスト手順 (視覚閲覧環境)
一時保留

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)
“ロイヤルパームホテル” に関する “お客様の声” のリンクからフォーカスを移動させずに、そのリンクの目的を表す見出しの内容 “ロイヤルパームホテル” を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
a 要素 , h 要素

