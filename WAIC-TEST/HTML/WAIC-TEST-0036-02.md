# テスト ID
WAIC-TEST-0036-02

# テストのタイトル
ユーザインタフェースコンポーネントがフォーカスを受けとったときの提示を変更するために、CSS を使用する

# テストの目的
フォーカスを受け取った要素の背景又はボーダーの色が変化することを確認し、その要素がフォーカスを失ったとき、背景又はボーダーの色の変更が除去されることを確認する。

# テストの対象となる達成基準 (複数)
1.4.1
2.4.7

# 関連する達成方法 (複数)
なし

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

# テスト手順 (視覚閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (視覚閲覧環境)
マウス、またはキーボード操作で入力フィールドがフォーカスを受け取ったときに背景色が適用され、フォーカスが外れた際に、背景色の変更が除去される。

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