# テスト ID

WAIC-TEST-0047-03

# テストのタイトル

複数のラベルを付けるために aria-labelledby を使用する

# テストの目的

複数のラベルを提供するために aria-labelledby 属性が使用できることの確認

# テストの対象となる達成基準

1.3.1
4.1.2

# 関連する達成方法 (複数)

ARIA9、ARIA16

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0047-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0047-03.html)

# テストコードのソース (抜粋)

```HTML
<label id="l1" for="f3">通知する</label>
<select name="amt" id="f3" aria-labelledby="f3 l2 l1">
  <option value="1">1</option>
  <option value="2">2</option>
</select>
<span id="l2" tabindex="-1">日前に</span>
```

# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

select要素にフォーカスを合わせ、読み上げ内容を確認

# 期待される結果 (音声閲覧環境)

「1日前に通知する」または「2日前に通知する」のどちらかでラベルが通知される

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

aria-labelledby属性、id属性、for属性
