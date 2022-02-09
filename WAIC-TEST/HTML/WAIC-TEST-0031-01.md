

# テスト ID
WAIC-TEST-0031-01

# テストのタイトル
ユーザインタフェース コンポーネントの役割 (role) を明示するために、WAI-ARIA ロールを使用する

# テストの目的
div 要素に role 属性を指定した場合、該当の role 属性が通知されるかの確認

# テストの対象となる達成基準 (複数)
4.1.2

# 関連する達成方法 (複数)
ARIA4

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0031-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0031-01.html)

# テストコードのソース (抜粋)
```html
<div role="toolbar">
    <button>Home</button>
    <button>Refresh</button>
    <button>Help</button>
</div>
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
次の 1. 〜 3. をすべて満たしている
1. 矢印キーなどで要素を順に移動し toolbar に差し掛かった場合、toolbar であることが通知される。
2. tab キーで移動し button 要素にフォーカスした場合、toolbar であることが通知される。
3. toolbar を通過した場合、toolbar を終了したことが通知される

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
role="toolbar" をもつ div 要素


