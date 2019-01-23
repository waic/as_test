

# テスト ID
WAIC-TEST-0017-02

# テストのタイトル
インラインフレームによるブロックスキップ

# テストの目的
ブロックスキップの目的で iframe 要素に指定したインラインフレームをスキップできるかの確認

# テストの対象となる達成基準 (複数)
2.4.1

# 関連する達成方法 (複数)
H64, H70

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0017-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0017-01.html)

# テストコードのソース (抜粋)
```html
<div>
<p>インラインフレームを用いてWAICサイトを表示しています。</p>
<iframe src="http://waic.jp/" id="testiframe1" name="testiframe1" title="ウェブアクセシビリティ基盤委員会" width="500" height="500"><a href="http://waic.jp/">WAIC ウェブサイトへ</a></iframe>
<p>また、WCAG2.0の日本語訳も表示しています。</p>
<iframe src="http://waic.jp/docs/WCAG20/Overview.html" id="testiframe2" name="testiframe2" title="WCAG2.0日本語訳" width="500" height="500"><a href="http://waic.jp/docs/WCAG20/Overview.html">ウェブ・コンテンツ・アクセシビリティ・ガイドライン（WCAG）2.0</a></iframe>
<p>詳細はウェブサイトをご確認ください。</p>
</div>

```
# テスト手順 (視覚閲覧環境)
一時保留

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境)
iframe 要素の末尾に直接移動するための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
iframe 要素


