# テスト ID

WAIC-TEST-0048-01

# テストのタイトル

role 属性によるフォームのグループ化(role="group"の使用)

# テストの目的

role="group"を適用した要素が、支援技術にグループ化されたフォームコントロールとして認識されることを確認する

# テストの対象となる達成基準 (複数)

1.3.1、3.3.2

# 関連する達成方法 (複数)

ARIA17

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0048-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0048-01.html)

# テストコードのソース (抜粋)

```HTML
<div role="group" aria-labelledby="zip">
<p>前半3桁と後半4桁に分けて入力します</p>
<span id="zip">郵便番号</span> 
<span style="color: #D90D0D;"> * </span>
<input size="3" type="text" required title="前半3桁" />-
<input size="4" type="text" required title="後半4桁" />
</div>
```

# テスト手順 (視覚閲覧環境)

テスト不要

# 期待される結果 (視覚閲覧環境)

なし

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テストファイルを開き、矢印キーを使って移動し、どのように読み上げるかを確認する。

## テスト手順 1

テストファイルを開いた状態で矢印キーを押し、郵便番号を入力するテキストボックスへと移動する

### 期待される結果 1

郵便番号を入力するテキストボックスであることに加え、「郵便番号」というグループの内側であることが読み上げられる

## テスト手順 2

矢印キーを押し、「郵便番号を入力してください。」と読み上げられるまで移動する

### 期待される結果 2

「郵便番号を入力してください。」というテキストであることに加え、「郵便番号」というグループの外側であることが読み上げられる

# 期待される結果 (音声閲覧環境)

テスト手順1～2の結果をすべて満たしている。

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

role="group"が指定されたinput要素
