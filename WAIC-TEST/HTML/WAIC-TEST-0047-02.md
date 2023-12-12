# テスト ID
WAIC-TEST-0047-02

# テストのタイトル
スライダーコントロールにラベルを付けるために aria-labelledby を使用する

# テストの目的
スライダーコントロールにラベルを提供するために aria-labelledby 属性が使用できることの確認

# テストの対象となる達成基準 
1.3.1、4.1.2

# 関連する達成方法 (複数)
ARIA16

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0047-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0047-02.html)

# テストコードのソース (抜粋)
```HTML
<p><span id="mysldr-lbl">旅行の日数</span>を選択してください。</p>
<div id="mysldr" role="slider" aria-labelledby="mysldr-lbl" tabindex="0" aria-valuenow="15">
<div id="mysldr-handle"></div>
</div>
```

```CSS
#mysldr {
　width: 200px;
　height: 10px;
　background-color: #ddd;
　position: relative;
　cursor: pointer;
　margin: 10px ;
　outline: none;
    }
#mysldr-handle {
　width: 20px;
　height: 20px;
　background-color: #3498db;
　border-radius: 50%;
　position: absolute;
　top: 50%;
　transform: translate(-50%, -50%);
    }
```

# テスト手順 (視覚閲覧環境)
テスト不要

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
スライダーコントロールにフォーカスを合わせ、読み上げ内容を確認

# 期待される結果 (音声閲覧環境)
「旅行の日数を選択　15」としてラベルが通知される

# テスト実施時の注意点 (音声閲覧環境)
なし

# 関連する要素や属性
aria-labelledby属性、id属性、role属性