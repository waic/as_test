

# テスト ID
WAIC-TEST-0014-03

# テストのタイトル
説明リスト (dl 要素)

# テストの目的
dl 要素に指定した説明リストが表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
1.3.1

# 関連する達成方法 (複数)
H48

# テストコード (テストファイルへのリンク)
WAIC-CODE-0014-03

# テストコードのソース (抜粋)
```html
<div>
<p>重要な用語の意味を説明します。</p>
<dl>
<dt>略語 (abbreviation)</dt>
<dd>単語、語句、又は名称の短縮形で、その略語が言語の一部になっていないもの。</dd>
<dt>ASCII アート (ASCII art)</dt>
<dd>文字やグリフの空間的配置によって作られた図画 (典型的には、ASCIIで定義されている95の印字可能文字から作られる)。 </dd>
<dt>点滅 (blinking)</dt>
<dd>注意を引く意図で、二つの視覚的な状態を交互に切り替えること。 </dd>
<dd>似ている言葉として閃光がある。</dd>
</dl>
<p>詳細については文末の用語集をご参照ください。</p>
</div>

```
# テスト手順 (視覚閲覧環境)
一時保留

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
説明リストを読み上げ、内容を確認

# 期待される結果 (音声閲覧環境)
次の 1. 〜 4. をすべて満たしている
1. 説明リスト (dl) であること及びリスト項目 (dt) の数を知る何らかの手段が提供されている
2. 説明リスト (dl) の開始位置及び終了位置を知るための何らかの手段が提供されている
3. リスト項目 (dt) の開始位置及び終了位置を知るための何らかの手段が提供されている
4. dd 要素の開始位置及び終了位置を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)
例えば、“3項目の記述リスト リスト項目の開始 用語 略語 (abbreviation) 定義 単語、語句、又は名称の短縮形で、その略語が言語の一部になっていないもの。 リスト項目の終了…” と読み上げられる場合は OK と判断
3. については、次のリスト項目 (dt) に移動する機能を提供している場合も OK と判断
4. については、次の dd 要素に移動する機能を提供している場合も OK と判断
ただし、dt 要素をまたいで移動する場合は NG と判断

# 関連する要素や属性
dl 要素 , dt 要素 , dd 要素

