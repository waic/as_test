# テスト ID

WAIC-TEST-0029-04

# テストのタイトル

aria-describedby 属性による説明ラベルの提供 (input要素 : 隠された要素と関連付け)

# テストの目的

input 要素に隠された aria-describedby 属性で関連付けをおこなった場合、関連付けられた要素の内容が読み上げられるかの確認

# テストの対象となる達成基準 (複数)

1.3.1, 3.3.2

# 関連する達成方法 (複数)

ARIA1

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0029-04](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0029-04.html)

# テストコードのソース (抜粋)

```html
<label for="first">名前:</label>

<input type="text" id="first" name="first" size="20" aria-describedby="tp1" aria-required="false"/>

<div id="tp1" role="tooltip" aria-hidden="true">名前は任意です。</div>
```

# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

- input要素にフォーカスを合わせる。
- 隠された aria-describedby属性で関連付けられた文章が読み上げられることを確認する。

# 期待される結果 (音声閲覧環境)

input要素にフォーカスを合わせた際、aria-describedby属性で関連付けられた文章が読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

input要素、aria-describedby属性
