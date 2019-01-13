

# テスト ID
WAIC-TEST-0012-04

# テストのタイトル
セレクトメニューとラベル (title 属性)

# テストの目的
title 属性に指定したラベルとセレクトメニューが関連付いているかの確認

# テストの対象となる達成基準 (複数)
1.1.1, 1.3.1, 3.3.2, 4.1.2

# 関連する達成方法 (複数)
H65

# テストコード (テストファイルへのリンク)
WAIC-CODE-0012-04

# テストコードのソース (抜粋)
```html
<div>
<label for="searchTerm">検索:</label><input id="searchTerm" type="text" size="30" value="" name="searchTerm">
<select title="検索範囲を選択" id="scope">
<option value="aaa">このサイト内</option>
<option value="aaa">このカテゴリ内</option>
<option value="aaa">インターネット全体</option>
</select>
</div>

```
# テスト手順 (視覚閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (視覚閲覧環境)
次の 1. 〜 2. をすべて満たしている
1. マウス操作 : セレクトメニューにマウスポインタを重ねると、title 属性の値 “検索範囲を選択” が通知される
2. キーボード操作 : セレクトメニューにフォーカスを移動させると、title 属性の値 “検索範囲を選択” が通知される

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境)
セレクトメニューにフォーカスを移動すると、title 属性値 “検索範囲を選択” が読み上げられる

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
select 要素 , title 属性

