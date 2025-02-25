# テスト ID

WAIC-TEST-0090-01

# テストのタイトル

CSS によるフォントサイズのパーセント指定

# テストの目的

strong 要素にパーセントでフォントサイズを指定した場合、親要素のフォントサイズに基づいて他のテキストより大きく表示されるかを確認

# テストの対象となる達成基準

1.4.4, 1.4.5（参考）, 1.4.8, 1.4.9（参考）

# 関連する達成方法 (複数)

C12, C13, C14

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0090-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0090-01.html)

# テストコードのソース (抜粋)

```HTML
<h1><img src="https://waic.jp/wp-content/themes/waic/images/mark.png" alt="WAICロゴマーク" width="50" height="50"><strong>ユーザー</strong>がテキストサイズを制御できるようにする</h1>
<p>どのサイズのテキストが自分に適しているかはユーザーのみが知ることができるので、
テキストサイズを設定できるようにすることが<strong>非常に</strong>重要です。</p>
```

```CSS
strong {
        font-size: 120%;
}
```

# テスト手順 (視覚閲覧環境)

ズーム機能ではなく、ブラウザの文字サイズ変更機能を用いて、文字サイズのみを拡大する

# 期待される結果 (視覚閲覧環境)

フォントサイズがパーセントで指定された見出し要素内の strong 要素「ユーザー」と、段落要素内の strong 要素「非常に」が、周囲のテキストよりも大きく表示される

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
