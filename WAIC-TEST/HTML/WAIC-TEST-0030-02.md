

# テスト ID
WAIC-TEST-0030-02

# テストのタイトル
aria-required プロパティによって必須項目を特定する（required プロパティが label 要素の後に置かれる単語 "required" によって示されている）

# テストの目的


# テストの対象となる達成基準 (複数)
1.3.1
3.3.3

# 関連する達成方法 (複数)
今のところなし

# テストコード (テストファイルへのリンク)
WAIC-CODE-0030-02

# テストコードのソース (抜粋)
```html
<form action="#" method="post" id="step1" onsubmit="return errorCheck2()">
  <p>
    <label for="fname">First name: </label>
    <input type="text" id="fname" aria-required="true" />
    [required]
  </p>
  <p>
    <label for="mname">Middle name: </label>
    <input type="text" id="mname" />
  </p>
  <p>
    <label for="lname">Last name: </label>
    <input type="text" id="lname" aria-required="true" />
    [required]
  </p>
  <p>
    <label for="email">Email address: </label>
    <input type="text" id="email" aria-required="true" />
    [required]
  </p>
  <p>
    <label for="zip_post">Zip / Postal code: </label>
    <input type="text" id="zip_post" size="6" aria-required="true" />
    [required]
  </p>
  <p>
    <input type="submit" value="Next Step" id="step_btn" name="step_btn" />
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


# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性



