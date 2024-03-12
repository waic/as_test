# テスト ID

WAIC-TEST-0052-01

# テストのタイトル

エラーフィールドを示すために aria-invalid を使用する

# テストの目的

フォーム入力フィールドに対して、JavaScript によって aria-invalid 属性が追加された際、スクリーンリーダーが認識し、通知するかどうかを確認する。

# テストの対象となる達成基準 (複数)

3.3.1

# 関連する達成方法 (複数)

ARIA21

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0052-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0052-01.html)

# テストコードのソース (抜粋)

```JavaScript
if(currentInput.value === ''){
  currentInput.setAttribute('aria-invalid', 'true');
  currentLabel.classList.add('failed');
  eFlag++;
} else {
  currentInput.removeAttribute('aria-invalid');
  currentLabel.classList.remove('failed');
}
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順

テスト不要

## 期待される結果

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

1. テストファイルを開き、入力フィールドに何も入力せずに送信ボタンを押す
2. 入力フィールドにフォーカスを移す

# 期待される結果 (音声閲覧環境)

入力フィールドにフォーカスを移した際、入力されているデータが適切でない旨がなんらかの手段によって通知される

# テスト実施時の注意点 (音声閲覧環境)

「無効なデータ」などと読み上げられる場合がある

# 関連する要素や属性

input要素、aria-invalid属性
