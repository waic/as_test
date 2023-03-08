# テスト ID
WAIC-TEST-0036-02

# テストのタイトル
CSSによる背景色の適用 (フォーカスされた入力フィールド)

# テストの目的
CSS の疑似要素でフォーカスを受け取った入力フィールドが強調表示される

# テストの対象となる達成基準 (複数)
1.4.1
2.4.7

# 関連する達成方法 (複数)
C15

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0036-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0036-02.html)

# テストコードのソース (抜粋)
```HTML
<form method="post" action="form.php">
      <p><label for="fname">名前: </label>
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
        color: #000;
      }
      input[type=checkbox]:focus + label, input[type=radio]:focus + label {
        background-color: #FF6; 
        color: #000; 
      }
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1.

1. 入力フィールドにフォーカスをあわせる。
2. 入力フィールドのフォーカスを外す。

## 期待される結果 1.

1. 入力フィールドの背景色が変化する。
2. 入力フィールドの背景色が、フォーカスを受け取る前の状態となる。

## テスト手順 2.

1. ラジオボタンにフォーカスを合わせる。
2. ラジオボタンのフォーカスを外す。

## 期待される結果 2.

1. ラジオボタンの背景色が変化する。
2. ラジオボタンの背景色が、フォーカスを受け取る前の状態となる。

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
なし

# 期待される結果 (音声閲覧環境)
なし

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし
