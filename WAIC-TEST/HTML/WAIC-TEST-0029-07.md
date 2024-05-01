

# テスト ID
WAIC-TEST-0029-07

# テストのタイトル
aria-describedby 属性による説明ラベルの提供 (button要素 : aria-labelledby属性と併用)

# テストの目的
button 要素に aria-labelledby 属性と aria-describedby属性の両方で関連付けをおこなった場合、関連付けられた要素の内容が読み上げられるかの確認

# テストの対象となる達成基準 (複数)
1.3.1
3.3.2

# 関連する達成方法 (複数)
ARIA1

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0029-07](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0029-07.html)

# テストコードのソース (抜粋)
```html
<p><span id="fontLabel">フォントの選択</span>
    <span id="fontDesc">このページで使用するフォントフェイスとサイズの選択</span>
    <button id="fontB" onclick="doAction('Fonts');" aria-labelledby="fontLabel" aria-describedby="fontDesc">フォント</button>
</p>
<p><span id="colorLabel">色の選択</span>
    <span id="colorDesc">このページで使用する色を選択</span>
    <button id="colorB" onclick="doAction('Colors');" aria-labelledby="colorLabel" aria-describedby="colorDesc">色</button>
</p>
<p><span id="customLabel">その他のカスタマイズの選択</span>
    <span id="customDesc">このページで使われているレイアウトやスタイルをカスタマイズ</span>
    <button id="customB" onclick="doAction('Customize');" aria-labelledby="customLabel" aria-describedby="customDesc">カスタマイズ</button>
</p>
```
# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
- button要素にフォーカスを合わせる。
- aria-labelledby 属性と aria-describedby属性で関連付けられた文章が読み上げられることを確認する。

# 期待される結果 (音声閲覧環境)
button要素にフォーカスを合わせた際、aria-labelledby 属性と aria-describedby属性で関連付けられた文章が読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
button要素、aria-labelledby属性、aria-describedby属性


