# テスト ID 
WAIC-TEST-0030-03

# テストのタイトル 
aria-required 属性による必須項目の特定（role=radioを指定したラジオボタン）

# テストの目的 

aria-required属性、role属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :
1.3.1
3.3.3

# 関連する達成方法 (複数) :
ARIA2

# テストコード (テストファイルへのリンク) :
[WAIC-CODE-0030-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0030-03.html)

# テストコードのソース (抜粋)

```html
<style type="text/css">
.aria-required=true {
  border: red thin solid;
}
.data-required=true:after {
  content: url('/iconStar.gif');
}
</style>

<form action="#" method="post" id="alerts1">
  <label for="acctnum" data-required="true">口座番号</label>
  <input size="12" type="text" id="acctnum" aria-required="true" name="acctnum" />
  <p id="radio_label" data-required="true">残高が$3,000を超えたらアラートを送信する</p>
  <ul  id="rg" role="radiogroup" aria-required="true" aria-labelledby="radio_label">
    <li id="rb1" role="radio">はい</li>
    <li id="rb2" role="radio">いいえ</li>
  </ul>
</form>
```

# テスト手順 (視覚閲覧環境) 
テスト不要

# 期待される結果 (視覚閲覧環境) 
なし

# テスト実施時の注意点 (視覚閲覧環境) 

なし

# テスト手順 (音声閲覧環境) 

テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境) 

aria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わる

# テスト実施時の注意点 (音声閲覧環境) 

なし

# 関連する要素や属性 :

aria-required 属性が指定されているinput 要素