

# テスト ID
WAIC-TEST-0029-01

# テストのタイトル
ユーザインターフェース コントロールに対する説明ラベルを提供するために、aria-describedby プロパティを使用する

# テストの目的
button 要素に aria-describedby 属性で関連付けをおこなった場合、関連付けられた要素の内容が読み上げられるかの確認

# テストの対象となる達成基準 (複数)
1.3.1
3.3.2

# 関連する達成方法 (複数)
ARIA1

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0029-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0029-01.html)

# テストコードのソース (抜粋)
```html
<button aria-label="閉じる" aria-describedby="descriptionClose" onclick="myDialog.close()">X</button>

<div id="descriptionClose">このウィンドウを閉じると、入力された情報は破棄され、メインページに戻ります。</div>
```
# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
button要素にフォーカスを合わせる。
aria-describedby属性で関連付けられた文章が読み上げられることを確認する。

# 期待される結果 (音声閲覧環境)
button要素にフォーカスを合わせた際、aria-describedby属性で関連付けられた文章が読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
button要素、aria-describedby属性、aria-label属性


