# テスト ID
WAIC-TEST-0035-03

# テストのタイトル
装飾目的の画像を付加するために、CSS を使用する

# テストの目的
タブ要素の角丸画像が装飾目的としてCSSの背景画像として指定されているか確認する。

# テストの対象となる達成基準 
1.1.1

# 関連する達成方法 (複数)
C30
F3

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0035-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0035-03.html)

# テストコードのソース (抜粋)
```HTML
<div id="theComments">
    <div class="aComment">
      <blockquote>
        <p>こんにちは、ジョン。このテクニックはとても気に入っていて、自分のウェブサイトで使ってみようと思っています。</p>
      </blockquote>
      <div class="submitter">
        <cite><a href="http://example.com/">匿名の臆病者</a> エルボニアより</cite>
      </div>
    </div>
    <div class="aComment">
…
 </div>
</div>
```
```CSS
div#theComments { width:600px; }
    div.aComment { background: url('./img/WAIC-CODE-0035-03-01.png') repeat-y left top; 
    margin:0 0 30px 0; }
    div.aComment blockquote { background: url('./img/WAIC-CODE-0035-03-02.png') no-repeat left top; 
    margin:0; padding:8px 16px; }
    div.aComment div.submitter { background:#fff url('./img/WAIC-CODE-0035-03-03.png') no-repeat left top; 
    margin:0; padding-top:30px; }
```

# テスト手順 (視覚閲覧環境)
テストファイルを操作し、結果を確認。
ユーザエージェントでスタイルシート無効にし内容を確認。

# 期待される結果 (視覚閲覧環境)
スタイルシート無効により画像が非表示となる。

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを操作し、結果を確認。

# 期待される結果 (音声閲覧環境)
画像として読み上げられない。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
なし