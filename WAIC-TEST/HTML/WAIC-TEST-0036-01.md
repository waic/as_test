# テスト ID
WAIC-TEST-0036-01

# テストのタイトル
CSSによる背景色の適用 (フォーカスされたリンク要素)

# テストの目的
フォーカスを受け取ったリンク要素の背景色が、CSS により変更される

# テストの対象となる達成基準 (複数)
1.4.1
2.4.7

# 関連する達成方法 (複数)
なし

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
#mainnav a {
  background-color: #000066;
  color:#DCFFFF;
}

#mainnav a:active, #mainnav a:focus {
  background-color: #DCFFFF;
  color:#000066;
}
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順

1. タブキーでリンク要素にフォーカスを移動する。
2. タブキーでリンク要素のフォーカスを外す。

## 期待される結果

1. フォーカスしたリンク要素の背景色が変化する。
2. フォーカスを外したリンク要素の背景色が、 “1.” で変化する前の状態に戻る。

# テスト実施時の注意点 (視覚閲覧環境)
ポインティングデバイスではアクティブ化してしまうのでキーボードによるテストを実施。

# テスト手順 (音声閲覧環境)
なし

# 期待される結果 (音声閲覧環境)
なし

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし
