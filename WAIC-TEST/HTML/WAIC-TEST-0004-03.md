

# テスト ID
WAIC-TEST-0004-03

# テストのタイトル
イメージマップ内の area 要素 (代替テキストあり)

# テストの目的
イメージマップ内の各 area 要素に代替テキストを指定した場合、代替テキストが表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
1.1.1, 2.4.4, 2.4.9

# 関連する達成方法 (複数)
H24

# テストコード (テストファイルへのリンク)
WAIC-CODE-0004-01

# テストコードのソース (抜粋)
```html
<div>
<p>各売り場への直通電話番号につきましては<a href="#">お問い合わせ先一覧</a>をご参照ください。</p>
<img src="img/WAIC-CODE-0004-01.gif" alt="デパートのフロアガイド。各階について詳しくお知りになりたい場合は各階をクリックしてください。" width="300" height="400" usemap="#Map">
<map name="Map" id="Map">
<area shape="poly" coords="0,  0,265,  0,300, 30,300,108,265,102,0,102" href="WAIC-CODE-0004-01-ref4.html" alt="4F雑貨 書籍">
<area shape="poly" coords="0,102,265,102,300,108,300,207,265,202,0,202" href="WAIC-CODE-0004-01-ref3.html" alt="3F衣料品">
<area shape="poly" coords="0,202,265,202,300,207,300,304,265,301,0,301" href="WAIC-CODE-0004-01-ref2.html" alt="2Fお菓子 その他食品">
<area shape="poly" coords="0,301,265,301,300,304,300,400,265,400,0,400" href="WAIC-CODE-0004-01-ref1.html" alt="1F生鮮食品">
</map>

<p>店舗へのアクセスにつきましては<a href="#">周辺地図</a>をご参照ください。</p>

</div>

```
# テスト手順 (視覚閲覧環境)
表示 : ブラウザの設定を変更して画像非表示にし、表示内容を確認

# 期待される結果 (視覚閲覧環境)
各 area 要素の alt 属性に指定した代替テキスト “4F 雑貨 書籍” “3F 衣料品” “2F お菓子 その他食品” “1F 生鮮食品” が表示される

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
各 area 要素を読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)
各 area 要素の alt 属性に指定した代替テキスト “4F 雑貨 書籍” “3F 衣料品” “2F お菓子 その他食品” “1F 生鮮食品” が読み上げられる

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
area 要素 , alt 属性

