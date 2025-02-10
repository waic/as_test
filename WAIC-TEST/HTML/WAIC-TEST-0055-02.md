# テスト ID

WAIC-TEST-0055-02

# テストのタイトル

CSS によるフォーカスされた要素のハイライト (input 要素)

# テストの目的

input 要素に対して :focus 疑似クラスを使用してスタイルを変更することで視覚表現が変化するかどうかを確認する

# テストの対象となる達成基準 (複数)

2.4.7, 1.4.1 (参考)

# 関連する達成方法 (複数)

C15

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0055-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0055-02.html)

# テストコードのソース (抜粋)

```HTML
<form method="post" action="form.php">
  <p><label for="fname">氏名: </label>
    <input class="text" type="text" name="fname" id="fname" />
  </p>
  <p>
    <input type="radio" name="sex" value="male" id="sm" /> <label for="sm">男性</label><br />
    <input type="radio" name="sex" value="female" id="sf" /> <label for="sf">女性</label>
  <p>
</form>
```

```CSS
input.text:focus {
  background-color: #7FFF00; 
  color: #000000;
}
input[type=radio]:focus + label {
  background-color: #FFFF66; 
  color: #000000; 
}
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1

Tab キーを押下し、「氏名」の入力欄にフォーカスを移動

### 期待される結果 1

フォーカスが当たると「氏名」の入力欄の背景色が変化する

## テスト手順 2

Tab キーを押下し、ラジオボタン「男性」にフォーカスを移動

### 期待される結果 2

- フォーカスが外れた「氏名」の入力欄の背景色が元に戻る
- フォーカスが当たるとラジオボタン「男性」のラベルの背景色が変化する

## テスト手順 3

下矢印キーを押下し、ラジオボタン「男性」から「女性」にフォーカスを移動

### 期待される結果 3

- フォーカスが外れたラジオボタン「男性」のラベルの背景色が元に戻る
- フォーカスが当たるとラジオボタン「女性」のラベルの背景色が変化する

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テスト不要

# 期待される結果 (音声閲覧環境)

なし

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

input 要素、:focus 疑似クラス
