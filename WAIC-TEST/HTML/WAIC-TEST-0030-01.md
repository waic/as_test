# テスト ID 
WAIC-TEST-0030-01

# テストのタイトル 
aria-required 属性によって必須項目を特定する(required 属性が label 要素の後に置かれるアスタリスクによって示されている)

# テストの目的 

aria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :
1.3.1
3.3.3

# 関連する達成方法 (複数) :
ARIA2

# テストコード (テストファイルへのリンク) :
[WAIC-CODE-0030-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0030-01.html)

# テストコードのソース (抜粋)

```html

<form action="#" method="post"  id="login1" onsubmit="return errorCheck1()">
  <p>注：[*]は必須項目を示します。</p>
  <p>
    <label for="usrname">ログインネーム</label>
    <input type="text" name="usrname" id="usrname" aria-required="true"/>[*]
  </p>
  <p>
    <label for="pwd">パスワード</label>
    <input type="password" name="pwd" id="pwd" size="12" aria-required="true" />[*]
  </p>
  <p>
    <input type="submit" value="ログイン" id="next_btn" name="next_btn"/>
  </p>

</form>

```

# テスト手順 (視覚閲覧環境) 
テスト不要

# 期待される結果 (視覚閲覧環境) 
なし

# テスト実施時の注意点 (視覚閲覧環境) 
なし

# テスト手順 (音声閲覧環境) 
テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境) 

aria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わる

# テスト実施時の注意点 (音声閲覧環境) 
なし

# 関連する要素や属性 :
aria-required 属性が指定されているinput 要素