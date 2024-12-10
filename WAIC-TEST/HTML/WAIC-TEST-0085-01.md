# テスト ID

WAIC-TEST-0085-01

# テストのタイトル

autocomplete 属性による入力内容の関連付け

# テストの目的

input要素に適切なautocomplete属性を設定し、値の関連付けを行う

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
<label for="family-name">姓</label>
<input type="text" id="family-name" name="family-name" autocomplete="family-name">
</div>
<div>
<label for="given-name">名</label>
<input type="text" id="given-name" name="given-name" autocomplete="given-name">
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
# テスト実施時の注意点 (視覚閲覧環境)

事前にブラウザでオートコンプリートを有効にする必要がある

# テスト手順と期待される結果 (音声閲覧環境)

## テスト手順 1

Tabキーや矢印キーを押し、姓をニュー力するフィールドを選択し、下矢印キーを押す

## 期待される結果 1

過去に入力して記録された苗字に関する情報が表示される

## テスト手順 2

Tabキーや矢印キーを押し、名をニュー力するフィールドを選択し、下矢印キーを押す

## 期待される結果 2

過去に入力して記録された名前に関する情報が表示される

## テスト手順 3

Tabキーや矢印キーを押し、メールアドレスをニュー力するフィールドを選択し、下矢印キーを押す

## 期待される結果 3

過去に入力して記録されたメールアドレスに関する情報が表示される

## テスト手順 4

Tabキーや矢印キーを押し、電話番号をニュー力するフィールドを選択し、下矢印キーを押す

## 期待される結果 4

過去に入力して記録された電話番号に関する情報が表示される

## テスト手順 5

Tabキーや矢印キーを押し、郵便番号をニュー力するフィールドを選択し、下矢印キーを押す

## 期待される結果 5

過去に入力して記録されたメールアドレスに関する情報が表示される

# テスト実施時の注意点 (音声閲覧環境)

事前にブラウザでオートコンプリートを有効にする必要がある

# 関連する要素や属性

input 要素,autocomplete 属性
