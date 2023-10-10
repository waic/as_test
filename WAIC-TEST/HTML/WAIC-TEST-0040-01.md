# テスト ID
WAIC-TEST-0040-01

# テストのタイトル
aria-labelledby 属性による複数のラベルの提供（input 要素 : 複数のaria-labelledby属性値）

# テストの目的
input 要素に複数の aria-labelledby 属性でラベルの提供をおこなった場合、指定された順番でラベルの提供が行われるかの確認

# テストの対象となる達成基準 (複数)
1.1.1
3.3.2

# 関連する達成方法 (複数)
ARIA9

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0040-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0040-01.html)

# テストコードのソース (抜粋)
```HTML
<form>
<p>
    <span id="timeout-label" tabindex="-1"><label for="timeout-duration">タイムアウトを延長する</label></span>
    <input type="text" size="3" id="timeout-duration" value="20" 
        aria-labelledby="timeout-duration timeout-unit timeout-label">
    <span id="timeout-unit" tabindex="-1">分</span>
</p>
</form>
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テキスト入力フィールドにフォーカスを合わせる。
読み上げる内容を確認する。

# 期待される結果 (音声閲覧環境)
テキスト入力フィールドのラベルとして「20分タイムアウトを延長する」と読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
type="text" を持つ input要素、aria-labellebdy属性
