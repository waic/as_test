

# テスト ID
WAIC-TEST-0024-02

# テストのタイトル
nav 要素への直接移動

# テストの目的
nav 要素を指定して関連したリンクをグループ化した場合、直前又は直後の nav 要素に直接移動できるかの確認

# テストの対象となる達成基準 (複数)
2.4.1

# 関連する達成方法 (複数)
なし

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0024-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0024-02.html)

# テストコードのソース (抜粋)
```html
<div>
<h1>ウェブアクセシビリティ基盤委員会</h1>
<nav>
<div><a href="organization.html">組織</a></div>
<div><a href="docs.html">JIS X 8341-3 関連ドキュメント</a></div>
<div><a href="event.html">イベント</a></div>
</nav>

<p>WAIC は、JIS X 8341-3 の普及・啓発・定着を通してウェブアクセシビリティの促進を目指して活動しています。</p>

<nav>
<div><a href="index.html">ホーム</a></div>
<div><a href="about.html">WAIC について</a></div>
<div><a href="inquiry.html">お問い合わせ</a></div>
</nav>

</div>

```
# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境)
直前または直後の nav 要素に直接移動するための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
nav 要素


