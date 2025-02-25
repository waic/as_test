# テスト ID

WAIC-TEST-0091-01

# テストのタイトル

CSS によるフォントサイズのキーワード指定

# テストの目的

strong 要素にキーワードでフォントサイズを指定した場合、親要素のフォントサイズに基づいて他のテキストより大きく表示されるかを確認

# テストの対象となる達成基準

1.4.4, 1.4.5（参考）, 1.4.8, 1.4.9（参考）

# 関連する達成方法 (複数)

C12, C13, C14

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0091-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0091-01.html)

# テストコードのソース (抜粋)

```HTML
<h1><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="WAICロゴマーク" width="50" height="50"><strong>ユーザー</strong>がテキストサイズを制御できるようにする</h1>
<p>どのサイズのテキストが自分に適しているかはユーザーのみが知ることができるので、
テキストサイズを設定できるようにすることが<strong>非常に</strong>重要です。</p>
```

```CSS
strong {
    font-size: larger;
}
```

# テスト手順 (視覚閲覧環境)

ズーム機能ではなく、ブラウザの文字サイズ変更機能を用いて、文字サイズのみを拡大する

# 期待される結果 (視覚閲覧環境)

h1 要素の行頭にある「ユーザー」と、p 要素の行末にある「非常に」が周囲のテキストよりも大きく表示されることを確認する。


# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順 (音声閲覧環境)

テスト不要

# 期待される結果 (音声閲覧環境)

なし

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

strong 要素
