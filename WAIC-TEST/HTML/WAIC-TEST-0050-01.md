# テスト ID

WAIC-TEST-0050-01

# テストのタイトル

エラーを特定するために ARIA role=alert を使用する

# テストの目的

DOM 内にすでに存在する role=alert をもつコンテナの中にエラーメッセージを注入することで、エラーを特定できることを確認する。

# テストの対象となる達成基準 (複数)

3.3.1
4.1.3

# 関連する達成方法 (複数)

ARIA19

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0050-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0050-01.html)

# テストコードのソース (抜粋)

```HTML
<script>
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('signup').addEventListener('submit', function (e) {
      e.preventDefault();
      document.getElementById('errors').innerHTML = '';
      if (document.getElementById('first').value === '') {
        document.getElementById('errors').innerHTML += '<p>ファーストネームを入力してください。</p>';
      }
      if (document.getElementById('last').value === '') {
        document.getElementById('errors').innerHTML += '<p>ラストネームを入力してください。</p>';
      }
      if (document.getElementById('email').value === '') {
        document.getElementById('errors').innerHTML += '<p>メールアドレスを入力してください。</p>';
      }
    });
  });
</script>

<form name="signup" id="signup" method="post" action="">
  <div id="errors" role="alert" aria-atomic="true"></div>
  <p>
    <label for="first">ファーストネーム (必須)</label><br>
    <input type="text" name="first" id="first">
  </p>
  <p>
    <label for="last">ラストネーム (必須)</label><br>
    <input type="text" name="last" id="last">
  </p>
  <p>
    <label for="email">メールアドレス (必須)</label><br>
    <input type="text" name="email" id="email">
  </p>
  <p>
    <button id="button">送信</button>
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

- フォームに何も入力をせずに、最後の送信ボタンのアクションを実行する（例えばフォーカスを合わせてEnterキーを押す）。
- 読み上げられる内容を確認する。

# 期待される結果 (音声閲覧環境)

「ファーストネームを入力してください。ラストネームを入力してください。メールアドレスを入力してください。」と読み上げられる。

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

role 属性, aria-atomic 属性
