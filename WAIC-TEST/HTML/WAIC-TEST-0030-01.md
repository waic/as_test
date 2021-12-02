# テスト ID 
WAIC-TEST-0030-01

# テストのタイトル 
aria-required プロパティによって必須項目を特定する(required プロパティが label 要素の後に置かれるアスタリスクによって示されている)

# テストの目的 


# テストの対象となる達成基準 (複数) :
1.3.1
3.3.3

# 関連する達成方法 (複数) :
今のところなし

# テストコード (テストファイルへのリンク) :
WAIC-CODE-0030-01

# テストコードのソース (抜粋)

<form action="#" method="post"  id="login1" onsubmit="return errorCheck1()">
  <p>Note: [*]denotes mandatory field</p>
  <p>
    <label for="usrname">Login name: </label>
    <input type="text" name="usrname" id="usrname" aria-required="true"/>[*]
  </p>
  <p>
    <label for="pwd">Password</label>
    <input type="password" name="pwd" id="pwd" size="12" aria-required="true" />[*]
  </p>
  <p>
    <input type="submit" value="Login" id="next_btn" name="next_btn"/>
  </p>

</form>

# テスト手順 (視覚閲覧環境) 
テスト不要

# 期待される結果 (視覚閲覧環境) 
なし

# テスト実施時の注意点 (視覚閲覧環境) 
なし

# テスト手順 (音声閲覧環境) 
テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境) 


# テスト実施時の注意点 (音声閲覧環境) 
なし

# 関連する要素や属性 :
form要素