# テスト ID

WAIC-TEST-0022-01

# テストのタイトル

セレクトメニュー内のグループ化 (optgroup 要素)

# テストの目的

select 要素内の option 要素をグループ化するために optgroup 要素を使用した場合、各グループが表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)

1.3.1

# 関連する達成方法 (複数)

H85

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0022-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0022-01.html)

# テストコードのソース (抜粋)

```html
<div>
<form action="../../../../../jis2010-as-tests/201205/A/HTMLandXHTML/sample.cgi" method="post">
<label for="food">好きな食べ物は何ですか？</label>
<select id="food" name="food">
<optgroup label="フルーツ">
<option value="1">リンゴ</option>
<option value="2">バナナ</option>
<option value="3">桃</option>
<option value="4">みかん</option>
</optgroup>
<optgroup label="野菜">
<option value="5">にんじん</option>
<option value="6">キュウリ</option>
<option value="7">ピーマン</option>
</optgroup>
<optgroup label="焼き菓子">
<option value="8">アップルパイ</option>
<option value="9">チョコレートケーキ</option>
</optgroup>
</select>
</form>
</div>

```

# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テストファイルを読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)

次の 1. 〜 2. をすべて満たしている

1. optgroup 要素の label 属性値を知るための何らかの手段が提供されている
2. optgroup 要素の切り替わる位置 (グループの開始位置及び終了位置) を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

optgroup 要素 , option 要素
