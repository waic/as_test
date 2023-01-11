# テスト ID
WAIC-TEST-0036-01

# テストのタイトル
CSSによる背景色の適用 (フォーカスされたリンク要素)

# テストの目的
フォーカスを受け取った要素の背景又はボーダーの色が変化することを確認し、その要素がフォーカスを失ったとき、背景又はボーダーの色の変更が除去されることを確認する。

# テストの対象となる達成基準 (複数)
1.4.1
2.4.7

# 関連する達成方法 (複数)
C15

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0036-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0036-01.html)

# テストコードのソース (抜粋)
```HTML
<ul id="mainnav">
  <li class="page_item">ホーム</li>
  <li class="page_item"><a href="/services">サービス内容</a></li>
  <li class="page_item"><a href="/projects">プロジェクト紹介</a></li>
  <li class="page_item"><a href="/demos">デモのご案内</a></li>
  <li class="page_item"><a href="/about-us">会社概要</a></li>
  <li class="page_item"><a href="/contact-us">お問い合わせ</a></li>
  <li class="page_item"><a href="/links">リンク集</a></li>
</ul>
```
```CSS
#mainnav a:hover, #mainnav a:active, #mainnav a:focus {
  background-color: #DCFFFF;
  color:#000066;
}
```

# テスト手順 (視覚閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (視覚閲覧環境)
マウス、またはキーボード操作でリンク部分の要素がフォーカスを受け取ったときに背景色が適用され、フォーカスが外れた際に、背景色の変更が除去される。

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
なし

# 期待される結果 (音声閲覧環境)
なし

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし
