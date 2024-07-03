# テスト ID

WAIC-TEST-0029-08

# テストのタイトル

aria-describedby 属性による説明ラベルの提供 (button要素 : 複数のaria-describedby属性値)

# テストの目的

button 要素に複数の aria-describedby 属性で関連付けをおこなった場合、関連付けられた要素の内容が読み上げられるかの確認

# テストの対象となる達成基準 (複数)

1.3.1, 3.3.2

# 関連する達成方法 (複数)

ARIA1

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0029-08](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0029-08.html)

# テストコードのソース (抜粋)

```html
<p><span id="fontDesc">このページで使用するフォントフェイスとサイズの選択</span>
    <span id="fontDesc2">ボタンを押下しフォントを選択してください</span>
    <button id="fontB" onclick="doAction('Fonts');" aria-describedby="fontDesc fontDesc2">フォント</button>
</p>
<p><span id="colorDesc">このページで使用する色を選択</span>
    <span id="colorDesc2">ボタンを押下し色を選択してください</span>
    <button id="colorB" onclick="doAction('Colors');" aria-describedby="colorDesc colorDesc2">色</button>
</p>
<p><span id="customDesc">このページで使われているレイアウトやスタイルをカスタマイズ</span>
    <span id="customDesc2">ボタンを押下しレイアウトやスタイルを選択してください</span>
    <button id="customB" onclick="doAction('Customize');" aria-describedby="customDesc customDesc2">カスタマイズ</button>
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
- aria-describedby属性で関連付けられた複数の文章が読み上げられることを確認する。

# 期待される結果 (音声閲覧環境)

button要素にフォーカスを合わせた際、aria-describedby属性で関連付けられた複数の文章が読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

button要素、aria-describedby属性
