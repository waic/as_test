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
      theImage.setAttribute('src', 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGxpbmUgeDE9IjgiIHkxPSI0IiB4Mj0iOCIgeTI9IjEyIiBzdHJva2U9IiNGRjc3MDAiIHN0cm9rZS13aWR0aD0iMSIvPjxsaW5lIHgxPSI0IiB5MT0iOCIgeDI9IjEyIiB5Mj0iOCIgc3Ryb2tlPSIjRkY3NzAwIiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4=');
    } else {
      theImage.setAttribute('src', 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGxpbmUgeDE9IjgiIHkxPSI0IiB4Mj0iOCIgeTI9IjEyIiBzdHJva2U9IiM2NjYiIHN0cm9rZS13aWR0aD0iMSIvPjxsaW5lIHgxPSI0IiB5MT0iOCIgeDI9IjEyIiB5Mj0iOCIgc3Ryb2tlPSIjNjY2IiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4=');
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
    src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGxpbmUgeDE9IjgiIHkxPSI0IiB4Mj0iOCIgeTI9IjEyIiBzdHJva2U9IiM2NjYiIHN0cm9rZS13aWR0aD0iMSIvPjxsaW5lIHgxPSI0IiB5MT0iOCIgeDI9IjEyIiB5Mj0iOCIgc3Ryb2tlPSIjNjY2IiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4="
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

1. ページを表示し、「リンク 1」内にグレー色の画像が表示されていることを確認する
2. キーボードのTabキーを使用して「リンク 1」にフォーカスし、「リンク 1」内の画像の色を確認する（黄色に変化する）
3. キーボードのTabキーを使用して「リンク 1」以外の要素にフォーカスし、「リンク 1」内の画像の色を確認する（グレー色に変化する）
4. マウスカーソルを「リンク 1」の中に移動し、「リンク 1」内の画像の色を確認する（黄色に変化する）
5. マウスカーソルを「リンク 1」の外に移動し、「リンク 1」内の画像の色を確認する（グレー色に変化する）

# 期待される結果 (視覚閲覧環境)

- キーボード操作をしたとき、画像の色の変化が期待通りであること
- マウス操作をしたとき、画像の色の変化が期待通りであること

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