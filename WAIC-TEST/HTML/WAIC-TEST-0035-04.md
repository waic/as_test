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
[WAIC-CODE-0035-04](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0035-04.html)

# テストコードのソース (抜粋)
```CSS
li a {
    display: block;
}
li a:before {
    content: url(./img/WAIC-CODE-0035-04-01.png) ;
    vertical-align: middle;
    margin-right: .5em;
}
li a:after {
    content: url(./img/WAIC-CODE-0035-04-02.png);
    vertical-align: middle;
    margin-left: .5em;
}
```
```HTML
<ul>
    <li><a href="index.html">ホーム</a></li>
    <li><a href="company.html">会社概要</a></li>
    <li><a href="map.html">アクセスマップ</a></li>
</ul>
```
# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1.

1. 各リンク要素の内容の最初と最後に画像が表示されることを確認後、ユーザーエージェントでスタイルシートを無効にする。

## 期待される結果 1.

1. 各リンク要素の内容の最初と最後の画像いずれもが非表示となる。

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順と期待される結果 (音声閲覧環境)

## テスト手順

1. 各リンク要素の内容を確認する

## 期待される結果

1. 各リンク要素の内容の最初および最後に、画像に関する情報が含まれない

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし
