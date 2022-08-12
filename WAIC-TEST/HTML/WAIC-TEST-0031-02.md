

# テスト ID
WAIC-TEST-0031-02

# テストのタイトル
role 属性による役割の指定 (tree, treeitem, group)

# テストの目的
ul 要素および li 要素に role 属性を指定した場合、該当の role 属性が通知されるかの確認

# テストの対象となる達成基準 (複数)
4.1.2

# 関連する達成方法 (複数)
ARIA4

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0031-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0031-02.html)

# テストコードのソース (抜粋)
```html
<ul role="tree" tabindex="0">
  <li role="treeitem" tabindex="0">鳥</li>
  <li role="treeitem" tabindex="0">猫
    <ul role="group" tabindex="0">
      <li role="treeitem" tabindex="0">シャム</li>
      <li role="treeitem" tabindex="0">タビー</li>
    </ul>
  </li>
</ul>
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
下記の 3点が確認できること。
1. role="tree" をもつ ul 要素が、tree であることが通知される。
2. role="treeitem" をもつ li 要素が treeitem であることが通知される。
3. role="group" をもつ ul 要素が、group であることが通知される。

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
role="tree" をもつ ul 要素、role="treeitem" をもつ li 要素、role="group" をもつ ul 要素。


