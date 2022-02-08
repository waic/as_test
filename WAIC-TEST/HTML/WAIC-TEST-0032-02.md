# テスト ID
WAIC-TEST-0032-02

# テストのタイトル
リンクテキストの一部を非表示にするために、CSS を使用する

# テストの目的
非表示に配置されたa要素がリンクの目的を説明していることを確認する。

# テストの対象となる達成基準 (複数)
2.4.4
2.4.9

# 関連する達成方法 (複数)
G91
H33

# テストコード (テストファイルへのリンク)
WAIC-CODE-0032-02

# テストコードのソース (抜粋)
```html
<dl>
<dt>クマのプーさん </dt>
   <dd><a href="winnie_the_pooh.html">
      <span class="visually-hidden">クマのプーさん </span>HTML</a></dd>
   <dd><a href="winnie_the_pooh.pdf">
         <span class="visually-hidden">クマのプーさん </span>PDF</a></dd>
<dt>戦争と平和</dt>
    <dd><a href="war_and_peace.html">
      <span class="visually-hidden">戦争と平和 </span>HTML</a></dd> 
    <dd><a href="war_and_peace.pdf">
      <span class="visually-hidden">戦争と平和 </span>PDF</a></dd>
</dl>
```
# テスト手順 (視覚閲覧環境)
テストファイルを操作し、結果を確認。

# 期待される結果 (視覚閲覧環境)
リンクの目的を説明しているリンクテキストは表示されず、
電子書籍のリソースのリンクテキストのみが表示される

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認。

# 期待される結果 (音声閲覧環境)
非表示にされたa要素がリンクの目的の説明として読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
a要素、title属性