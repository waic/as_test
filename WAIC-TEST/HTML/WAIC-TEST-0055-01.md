# テスト ID

WAIC-TEST-0055-01

# テストのタイトル

CSS によるフォーカスされた要素のハイライト (a 要素)

# テストの目的

a 要素に対して :hover、:active、:focus 疑似クラスを使用してスタイルを変更することで視覚表現が変化するかどうかを確認する

# テストの対象となる達成基準 (複数)

2.4.7, 1.4.1 (参考)

# 関連する達成方法 (複数)

C15

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0055-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0055-01.html)

# テストコードのソース (抜粋)

```HTML
<ul id="mainnav">
  <li class="page_item">ホーム</li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref1.html">サービス</a></li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref2.html">プロジェクト</a></li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref3.html">デモ</a></li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref4.html">私たちについて</a></li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref5.html">お問い合わせ</a></li>
  <li class="page_item"><a href="WAIC-CODE-0055-01-ref6.html">リンク</a></li>
</ul>
```

```CSS
#mainnav a:hover, #mainnav a:active, #mainnav a:focus {
  background-color: #DCFFFF;
  color: #000066;
}
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1.

マウスなどのポインティングデバイスによって、リンクテキスト「サービス」の上にポインターをホバーさせる

### 期待される結果 1.

ホバーするとリンクテキスト「サービス」の背景色が変化する

## テスト手順 2.

マウスなどのポインティングデバイスによって、リンクテキスト「サービス」の上からポインターを外す

### 期待される結果 2.

ポインターが外れるとリンクテキスト「サービス」の背景色が元に戻る

## テスト手順 3.

Tab キーを押下し、リンクテキスト「サービス」にフォーカスを移動

### 期待される結果 3.

フォーカスが当たるとリンクテキスト「サービス」の背景色が変化する

## テスト手順 4.

Tab キーを押下し、リンクテキスト「サービス」から他の要素にフォーカスを移動

### 期待される結果 4.

フォーカスが外れるとリンクテキスト「サービス」の背景色が元の色に戻る

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テスト不要

# 期待される結果 (音声閲覧環境)

なし

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

a 要素、:hover 疑似クラス、:active 疑似クラス、:focus 疑似クラス
