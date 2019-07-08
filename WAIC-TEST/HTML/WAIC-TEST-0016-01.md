

# テスト ID
WAIC-TEST-0016-01

# テストのタイトル
ページの言語

# テストの目的
html 要素の lang 属性に指定したページの言語で表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
3.1.1

# 関連する達成方法 (複数)
H57

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0016-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0016-01.html), [WAIC-CODE-0016-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0016-02.html)

# テストコードのソース (抜粋)
```html
<html lang="ja">
<head>
（中略）
</head>
<body>
<div>
<p>12345</p>
</div>

```
# テスト手順 (視覚閲覧環境)
一時保留

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
WAIC-CODE-0016-01.html 及び WAIC-CODE-0016-02.html を開いて読み上げ音声を確認

# 期待される結果 (音声閲覧環境)
WAIC-CODE-0016-01.html と WAIC-CODE-0016-02.html の読み上げ音声が異なる

# テスト実施時の注意点 (音声閲覧環境)
lang 属性による音声エンジンの自動切り替えが有効な設定になっているか、テスト実施前にスクリーンリーダーの設定内容を確認すること

# 関連する要素や属性
lang 属性が指定された html 要素


