

# テスト ID
WAIC-TEST-0003-01

# テストのタイトル
フォーカス移動順序を指定した複数のフォームコントロール (マークアップ順)

# テストの目的
複数のフォームコントロールにフォーカス順序を指定した場合、指定した順序でフォーカスが移動するかの確認

# テストの対象となる達成基準 (複数)
2.4.3

# 関連する達成方法 (複数)
H4

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0003-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0003-01.html)

# テストコードのソース (抜粋)
```html
<div>
<form action="#" method="post">
<table>
<caption>グリーティングカードのオーダーフォーム</caption>
<tr>
<th>入力内容</th>
<th>送り先1</th>
<th>送り先2</th>
</tr>
<tr>
<th>姓</th>
<td><input type="text" size="30" value="" name="dest1first" title="1番目の受取人の名字" tabindex="1"></td>
<td><input type="text" size="30" value="" name="dest2first" title="2番目の受取人の名字" tabindex="10"></td>
</tr>
<tr>
<th>名</th>
<td><input type="text" size="30" value="" name="dest2last" title="1番目の受取人の名前" tabindex="2"></td>
<td><input type="text" size="30" value="" name="dest2last" title="2番目の受取人の名前" tabindex="11"></td>
</tr>
<tr>
<th>住所</th>
<td><input type="text" size="30" value="" name="dest1add" title="1番目の受取人の住所" tabindex="3"></td>
<td><input type="text" size="30" value="" name="dest2add" title="2番目の受取人の住所" tabindex="12"></td>
</tr>
<tr>
<th>カードのデザイン</th>
<td><label><input type="radio" value="watermelon" name="dest1design" title="1番目の受取人へのカードデザイン：スイカ" tabindex="4">スイカ</label><br><label><input type="radio" value="fireworks" name="dest1design" title="1番目の受取人へのカードデザイン：花火" tabindex="5">花火</label></td>
<td><label><input type="radio" value="watermelon" name="dest2design" title="2番目の受取人へのカードデザイン：スイカ" tabindex="13">スイカ</label><br><label><input type="radio" value="fireworks" name="dest2design" title="2番目の受取人へのカードデザイン：花火" tabindex="14">花火</label></td>
</tr>
<tr>
<th>オプション</th>
<td><label><input type="checkbox" value="" name="dest1stamp" title="1番目の受取人へのオリジナルスタンプ" tabindex="6">オリジナルスタンプ</label><br><label><input type="checkbox" value="" name="dest1melody" title="1番目の受取人へのメロディカード" tabindex="7">メロディカード</label></td>
<td><label><input type="checkbox" value="" name="dest2stamp" title="2番目の受取人へのオリジナルスタンプ" tabindex="15">オリジナルスタンプ</label><br><label><input type="checkbox" value="" name="dest2melody" title="2番目の受取人へのメロディカード" tabindex="16">メロディカード</label></td>
</tr>
<tr>
<th>メッセージ</th>
<td><textarea name="dest1msg" cols="30" rows="5" tabindex="8" title="1番目の受取人へのメッセージ"></textarea></td>
<td><textarea name="dest2msg" cols="30" rows="5" tabindex="17" title="2番目の受取人へのメッセージ"></textarea></td>
</tr>
<tr>
<th>確認</th>
<td><button type="button" name="dest1conf" tabindex="9">1番目の受取人へのカードプレビュー</button></td>
<td><button type="button" name="dest2conf" tabindex="18">2番目の受取人へのカードプレビュー</button></td>
</tr>
</table>
<p><input type="submit" value="注文内容の確認" name="submit" title="注文内容の確認" tabindex="19"> &nbsp; <input type="reset" value="入力内容のリセット" name="reset" title="入力内容のリセット" tabindex="20"></p>
</form></div>

```
# テスト手順 (視覚閲覧環境)
キーボード操作 : Tab キーを押下し、フォーカスの移動順序を確認

# 期待される結果 (視覚閲覧環境)
次の順序でフォーカスが移動する :

- 送り先 1 の姓
- 送り先 1 の名
- 送り先 1 の住所
- スイカ
- 花火
- オリジナルスタンプ
- メロディカード
- 送り先 1 のメッセージ
- 1 番目の受取人へのカードプレビュー
- 送り先 2 の姓
- 送り先 2 の名
- 送り先 2 の住所
- スイカ
- 花火
- オリジナルスタンプ
- メロディカード
- 送り先 2 へのメッセージ
- 1 番目の受取人へのカードプレビュー
- 注文内容の確認
- 入力内容のリセット

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
キーボード操作 : Tab キーを押下し、フォーカスの移動順序を確認

# 期待される結果 (音声閲覧環境)
次の順序でフォーカスが移動する :

- 1 番目の受取人の名字
- 1 番目の受取人の名前
- 1 番目の受取人の住所
- スイカ
- 花火
- 1 番目の受取人へのオリジナルスタンプ
- 1 番目の受取人へメロディカード
- 1 番目の受取人へのメッセージ
- 1 番目の受取人へのカードプレビュー
- 2 番目の受取人の名字
- 2 番目の受取人の名前
- 2 番目の受取人の住所
- スイカ
- 花火
- 2 番目の受取人へのオリジナルスタンプ
- 2 番目の受取人へメロディカード
- 2 番目の受取人へのメッセージ
- 2 番目の受取人へのカードのプレビュー
- 注文内容の確認
- 入力内容のリセット

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性

- type="text" を持つ input 要素
- type="radio" を持つ input 要素
- type="checkbox" を持つ input 要素
- type="submit" を持つ input 要素
- type="reset" を持つ input 要素
- type="button" を持つ button 要素
- tabindex 属性

