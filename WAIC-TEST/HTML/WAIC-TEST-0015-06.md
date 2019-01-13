

# テスト ID
WAIC-TEST-0015-06

# テストのタイトル
下付き文字 (sub 要素)

# テストの目的
sub 要素を指定してセマンティックにマークアップした下付き文字が表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
1.3.1

# 関連する達成方法 (複数)
H49

# テストコード (テストファイルへのリンク)
WAIC-CODE-0015-06

# テストコードのソース (抜粋)
```html
<div>
<p>水の化学式は H<sub>2</sub>O です。</p>
</div>

```
# テスト手順 (視覚閲覧環境)
テストファイルを表示し、内容を確認

# 期待される結果 (視覚閲覧環境)
“H2O” の “2” が下付き表示される

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
段落を読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)
“H2O” の “2” に差し掛かかると、この部分が下付き文字であることを知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
行読みモードやブラウザモードなどで読み上げると、下付き文字であることが自動的に知らされない場合は NG と判断

# 関連する要素や属性
sub 要素

