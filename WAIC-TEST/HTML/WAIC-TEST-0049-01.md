# テスト ID
WAIC-TEST-0049-01

# テストのタイトル
role 属性によるエラーの通知（alertdialog：aria-labelledby属性、aria-describedby属性と併用）

# テストの目的
role="alertdialog" を指定した div 要素に aria-labelledby 属性および aria-describedby 属性で関連付けを行った場合、alertdialog としての役割の通知とあわせて aria-labelledby 属性と aria-describedby 属性で関連付けられた要素の内容が読み上げられるかの確認。

# テストの対象となる達成基準 (複数)
3.3.1
3.3.3
4.1.3

# 関連する達成方法 (複数)
ARIA18

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0049-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0049-01.html)

# テストコードのソース (抜粋)
```HTML
<div id="alertDialog" role="alertdialog" aria-labelledby="alertHeading" aria-describedby="alertText" tabindex="0">
<div id="firstElement" tabindex="0"></div>
<h1 id="alertHeading">エラー</h1>
<div id="alertText">従業員の生年月日が入社日以降になっています。生年月日と入社日を確認してください。</div>
<button id="firstButton">戻る</button>
<button id="lastButton">保存する</button>
<div id="lastElement" tabindex="0"></div>
</div>
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
「エラーを表示」ボタンを押下後の通知内容を確認する。

# 期待される結果 (音声閲覧環境)
通知内容に次の 3点の全てが含まれることを確認する。

1. alertdialog であることが通知内容に含まれる。
2. aria-labelledby属性で関連付けた要素の内容となる「エラー」が通知内容に含まれる。
3. aria-describedby属性で関連付けた要素の内容となる「従業員の生年月日が入社日以降になっています。生年月日と入社日を確認してください。」が通知内容に含まれる。

# テスト実施時の注意点 (音声閲覧環境)
alertdialog は「ダイアログ」や「アラートダイアログ」のように通知されることがある。ダイアログであることが伝わるような何らかの通知があれば良い。

# 関連する要素や属性
role="alertdialog" をもつ div 要素、aria-labelledby属性、aria-describedby属性
