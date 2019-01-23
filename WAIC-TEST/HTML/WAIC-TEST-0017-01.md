

# テスト ID
WAIC-TEST-0017-01

# テストのタイトル
インラインフレームの説明 (title 属性)

# テストの目的
title 属性に指定したインラインフレームの説明及び代替コンテンツが表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
1.3.1, 4.1.2

# 関連する達成方法 (複数)
H64

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
テストファイルを読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)
次の 1. 〜 2. をすべて満たしている
1. 1 番目の iframe 要素の title 属性値 “ウェブアクセシビリティ基盤委員会” または代替コンテンツ “WAIC ウェブサイトへ” を知るための何らかの手段が提供されている
2. 2 番目の iframe 要素の title 属性値 “WCAG2.0 日本語訳” または代替コンテンツ “ウェブ・コンテンツ・アクセシビリティ・ガイドライン (WCAG) 2.0” を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
iframe 要素 , title 属性


