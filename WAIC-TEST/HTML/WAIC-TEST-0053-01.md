# テスト ID
WAIC-TEST-0053-01

# テストのタイトル
アイコンフォントに意味を付与するために role="img" を使用

# テストの目的
role="img" が指定されたアイコンフォントは、フォントファミリーが上書きされても正しく表示されることの確認

# テストの対象となる達成基準 
1.3.1

# 関連する達成方法 (複数)
ARIA24

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0053-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0053-01.html)

# テストコードのソース (抜粋)
```HTML
<script>
    function fontFamilyToggle() {
    var element = document.getElementById("font-family-toggle");
    element.classList.toggle("font-family-toggle");
}
</script>    
<p><strong>アイコンフォントA</strong></p>
<p><span class="icon icon-star-bg"></span> </p>
<p><strong>アイコンフォントB</strong></p>
<p><span class="icon icon-star-bg" role="img" aria-label="Favorite"></span></p>
<button onclick="fontFamilyToggle()">フォントファミリーを変更</button>
```

```CSS
.icon {
    font-family: 'Material Icons Outlined';
}
.icon-star-bg::before {
    content: 'star';
}
.font-family-toggle *:not([role="img"]) {
    font-family: Verdana, sans-serif !important;
}
```
# テスト手順 (視覚閲覧環境)
「フォントファミリーを変更」ボタンをクリックして、フォントを切り替える

# 期待される結果 (視覚閲覧環境)
次の2点の両方を満たす
1.「アイコンフォントA」のアイコンフォントの表示が「スター」に切り替わる
2.「アイコンフォントB」のアイコンフォントの表示は変更されない

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを開き、タブキーや矢印キーを使いフォーカスをアイコンフォントに移動させ、どのように読み上げるかを確認

## テスト手順 1.
「アイコンフォントA」のアイコンフォントにフォーカスをあわせる

### 期待される結果 1.
「スター」というアイコンフォント名が通知される

## テスト手順 2.
「アイコンフォントB」のアイコンフォントにフォーカスをあわせる。

### 期待される結果 2.
「Favorite画像」という説明ラベルが通知される

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
role属性、aria-label属性