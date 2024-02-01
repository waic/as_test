# テスト ID
WAIC-TEST-0051-01

# テストのタイトル
role 属性による領域の特定

# テストの目的
role="region"を適用した要素が、支援技術にページの領域として認識されることを確認する

# テストの対象となる達成基準 (複数)
1.3.1

# 関連する達成方法 (複数)
ARIA20

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0051-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0051-01.html)

# テストコードのソース (抜粋)
```HTML
<div role="region" aria-labelledby="pollhead">
<h3 id="pollhead">今週の質問</h3>
<form method="post" action="#">
<fieldset>
<legend>税制の見直しは必要だと思いますか?</legend>
<input type="radio" id="r1" name="poll" />
    <label for="r1">いいえ、現状のままで問題ありません。</label>
    <input type="radio" id="r2" name="poll" />
    <label for="r2">はい、富裕層はより多く支払う必要があります。</label>
    <input type="radio" id="r3" name="poll" />
    <label for="r3">はい、企業の税の抜け道をふさぐ必要があります。</label>
    <input type="radio" id="r4" name="poll" />
    <label for="r4">全面的な変更が必要です。</label>
  </fieldset>
</form>
</div>
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
テストファイルを開いた状態で矢印キーを押し、「今週の質問」と読み上げられるまで移動する

### 期待される結果
「今週の質問」という名前の領域に差し掛かったことを読み上げる

# 期待される結果 (音声閲覧環境)
期待される結果を満たしている。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
role="region"が指定されたdiv要素
