# テスト ID

WAIC-TEST-0018-03

# テストのタイトル

fieldset 要素及び legend 要素によるグループ化 (テキスト入力フィールド)

# テストの目的

fieldset 要素及び legend 要素によってテキスト入力フィールドをグループ化した場合、グループの説明が表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)

1.3.1, 3.3.2

# 関連する達成方法 (複数)

H71

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0018-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0018-03.html)

# テストコードのソース (抜粋)

```html
<div>
<p>商品の配送先、及びご自宅住所を記入してください。</p>
<form action="http://example.com/adduser" method="post">
<fieldset>
<legend>ご自宅</legend>
<label for="raddress">住所: </label>
<input type="text" id="raddress" name="raddress">
<label for="rzip">郵便番号: </label>
<input type="text" id="rzip" name="rzip">
</fieldset>
<fieldset>
<legend>商品の送付先</legend>
<label for="paddress">住所: </label>
<input type="text" id="paddress" name="paddress">
<label for="pzip">郵便番号: </label>
<input type="text" id="pzip" name="pzip">
</fieldset>
<p><label for="mail">メールアドレス: </label><input type="text" id="mail" name="maddress"></p>
</form>
<p>記入が済みましたら「お支払い情報の選択」へお進みください。</p>
</div>

```

# テスト手順 (視覚閲覧環境)

一時保留

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テキスト入力フィールドのグループを読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)

次の 1. 〜 3. をすべて満たしている

1. それぞれのテキスト入力フィールドにフォーカスを移動すると、対応する legend 要素の内容 “ご自宅” または “商品の送付先” が通知される
2. “メールアドレス” に差し掛かると、直前の fieldset 要素内のグループの一要素であると誤解されるような通知をされない
3. fieldset 要素の開始位置及び終了位置を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

fieldset 要素 , legend 要素
