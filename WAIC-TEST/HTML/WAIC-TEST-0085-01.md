# テスト ID

WAIC-TEST-0085-01

# テストのタイトル

autocomplete 属性による入力内容の関連付け

# テストの目的

input要素に設定されたautocomplete属性が機能することを確認する

# テストの対象となる達成基準 (複数)

1.3.5

# 関連する達成方法 (複数)

H98

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0085-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0085-01.html)

# テストコードのソース (抜粋)

```HTML

<form>
<div>
<label for="name">名前</label>
<input type="text" id="name" name="name" autocomplete="name">
</div>
<div>
<label for="email">メールアドレス</label>
<input type="email" id="email" name="email" autocomplete="email">
</div>
<div>
<label for="tel">電話番号</label>
<input type="tel" id="tel" name="tel" autocomplete="tel">
</div>
<div>
<label for="postal-code">郵便番号</label>
<input type="text" id="postal-code" name="postal-code" autocomplete="postal-code">
</div>
</form>

```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1

名前を入力するフィールドをクリックまたはタップする

## 期待される結果 1

過去に入力して記録された名前に関する情報が表示される

## テスト手順 2

メールアドレスをニュー力するフィールドをクリックまたはタップする

## 期待される結果 2

過去に入力して記録されたメールアドレスに関する情報が表示される

## テスト手順 3

電話番号をニュー力するフィールドをクリックまたはタップする

## 期待される結果 3

過去に入力して記録された電話番号に関する情報が表示される

## テスト手順 4

郵便番号をニュー力するフィールドをクリックまたはタップする

## 期待される結果 4

過去に入力して記録された郵便番号に関する情報が表示される

# テスト実施時の注意点 (視覚閲覧環境)

事前にブラウザでオートコンプリートを有効にする必要がある

# テスト手順と期待される結果 (音声閲覧環境)

テスト手順と期待される結果 (視覚閲覧環境)と同様の手順で行う

autocompleteによって記録された情報は、各入力項目を選択した状態で、以下のように確認する

キーボード操作: 下矢印キーを押す
タッチ操作: 入力項目に隣接する内容をタッチもしくはスワイプする

# テスト実施時の注意点 (音声閲覧環境)

事前にブラウザでオートコンプリートを有効にする必要がある

# 関連する要素や属性

input 要素,autocomplete 属性
