# テスト ID

WAIC-TEST-0044-01

# テストのタイトル

ページのリージョンを特定するために ARIA ランドマークを使用する

# テストの目的

ウェブページのセクションに対して、プログラムによるアクセスを提供する

# テストの対象となる達成基準 (複数)

1.3.1, 2.4.1

# 関連する達成方法 (複数)

H69, SCR28

# テストコード (テストファイルへのリンク)

[WAIC-CODE-00xx-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-00xx-01.html)

# テストコードのソース (抜粋)

```HTML
<div id="header" role="banner">
    <h1>世界への扉 旅行プランをご紹介</h1>
</div>
<div id="sitelookup" role="search">
    <form>
        <label for="search">サイト検索</label>
        <input type="text" id="search">
        <button type="submit">検索</button>
    </form>
</div>
<div id="nav" role="navigation">
    <ul>
        <li><a href="#">ホーム</a></li>
        <li><a href="#">サービス</a></li>
        <li><a href="#">会社概要</a></li>
        <li><a href="#">お問い合わせ</a></li>
    </ul>
</div>
<div id="content" role="main">
    <h2>オタワ</h2>
    ... オタワはカナダの首都 ...
</div>
<div id="rightsideadvert" role="complementary">
    .... ここに広告 ...
</div>
<div id="footer" role="contentinfo">
    (c)フリーダムカンパニー、123 フリーダムウェイ、ヘルプビル、USA
</div>
```

# テスト手順と期待される結果 (視覚閲覧環境)

テスト不要

## テスト手順

なし

## 期待される結果

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

ページを一番上から下に向かって読み上げて、ランドマークとその内容を確認する。

# 期待される結果 (音声閲覧環境)

以下の順番で、ランドマークとその内容の組み合わせが読み上げられる。

1. バナー(banner) : 「世界への扉 旅行プランをご紹介」見出し レベル1
2. 検索(search) : 最初のラベルは「サイト検索」
3. ナビゲーション(navigation) : 最初の要素は「ホーム」リンク
4. メイン(main) : 最初の要素は「オタワ」見出し レベル1
5. 補足情報(complementary) : 内容は「ここに広告」
6. コンテンツ情報(contentinfo) : 内容は「(c)フリーダムカンパニー（以下略）」

# テスト実施時の注意点 (音声閲覧環境)

期待されるもの以外のランドマークが確認されないこと。

# 関連する要素や属性

div要素, role属性