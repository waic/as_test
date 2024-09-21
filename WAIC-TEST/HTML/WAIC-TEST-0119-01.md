# テスト ID

WAIC-TEST-0119-01

# テストのタイトル

キーボード及びマウスのイベントハンドラを両方とも使用する

# テストの目的

キーボードとマウスの両方のイベントハンドラを使用して、同等の処理を実行できることを確認する

# テストの対象となる達成基準

2.1.1

# 関連する達成方法 (複数)

SCR2

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0119-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0119-01.html)

# テストコードのソース (抜粋)

```javascript
function updateImage(imgId, isOver) {
  var theImage = document.getElementById(imgId);

  if (theImage != null) {
    if (isOver) {
      theImage.setAttribute('src', './img/WAIC-CODE-0119-01-02.png');
    } else {
      theImage.setAttribute('src', './img/WAIC-CODE-0119-01-01.png');
    }
  }
}
```

```html
<a
  href="#"
  onmouseover="updateImage('link1', true);"
  onfocus="updateImage('link1', true);"
  onmouseout="updateImage('link1', false);"
  onblur="updateImage('link1', false);"
>
  <img
    src="./img/WAIC-CODE-0119-01-01.png"
    alt=""
    id="link1"
    width="16"
    height="16"
  >
  リンク 1
</a>
<!-- 「リンク 2」も同様 -->
```

# テスト手順 (視覚閲覧環境)

1. ページを表示し、「リンク 1」内に×の画像が表示されていることを確認する
2. キーボードのTabキーを使用して「リンク 1」にフォーカスし、「リンク 1」内の画像を確認する（○の画像に変化する）
3. キーボードのTabキーを使用して「リンク 1」以外の要素にフォーカスし、「リンク 1」内の画像を確認する（×の画像に変化する）
4. マウスカーソルを「リンク 1」の中に移動し、「リンク 1」内の画像を確認する（○の画像に変化する）
5. マウスカーソルを「リンク 1」の外に移動し、「リンク 1」内の画像を確認する（×の画像に変化する）

# 期待される結果 (視覚閲覧環境)

- キーボード操作をしたとき、画像の変化が期待通りであること
- マウス操作をしたとき、画像の変化が期待通りであること

# テスト実施時の注意点 (視覚閲覧環境)

- ブラウザのJavaScriptが有効になっていることを確認すること

# テスト手順 (音声閲覧環境)

なし

# 期待される結果 (音声閲覧環境)

なし

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

script 要素, a・buttonなどのフォーカス可能な要素, イベントハンドラー属性
