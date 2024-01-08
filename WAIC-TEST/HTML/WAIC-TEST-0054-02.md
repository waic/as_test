# テスト ID

WAIC-TEST-0054-02

# テストのタイトル

aria-label による不可視ラベルの提供 (複数の input 要素に分かれた入力欄)

# テストの目的

input 要素に対して aria-label を使用して名前 (name) を与えた場合に、名前 (name) が認識され、通知されるかどうかを確認する

# テストの対象となる達成基準 (複数)

4.1.2

# 関連する達成方法 (複数)

ARIA14

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0054-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0054-02.html)

# テストコードのソース (抜粋)

```HTML
<div role="group" aria-labelledby="groupLabel">
    <span id="groupLabel">勤務先電話番号</span>
    <input type="text" aria-label="市外局番">
    <input type="text" aria-label="市内局番">
    <input type="text" aria-label="加入者番号">
</div>
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順

テスト不要

## 期待される結果

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テストファイルを開き、3つの入力欄に順次フォーカスを移動して読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)

入力欄のグループに対して付けられた可視ラベル「勤務先電話番号」とは別に、それぞれの入力欄に対して「市外局番」「市内局番」「加入者番号」の名前が通知される

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

aria-label 属性、aria-labelledby 属性、role 属性
