# テスト ID 
WAIC-TEST-0030-03

# テストのタイトル 
aria-required 属性による必須項目の特定（role属性）

# テストの目的 
aria-required属性、role属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :
1.3.1
3.3.3

# 関連する達成方法 (複数) :
ARIA2

# テストコード (テストファイルへのリンク) :
[WAIC-CODE-0030-03](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0030-03.html)

# テストコードのソース (抜粋)
```html
<h2>aria-required属性が設定されている</h2>

<!-- input[type="text"] -->
<p id="usrname">ログインネーム</p>
  <div role="textbox" aria-labelledby="usrname" aria-required="true" tabindex="0"></div>

<!-- select, option -->
<p id="os_pc">利用しているOS(PC)</p>
  <!-- select 閉じた状態 (select) -->
  <div role="combobox" aria-controls="combobox-target" aria-expanded="false" aria-required="true" tabindex="0">選択してください</div>

<!-- input[type="radio"] -->
<p id="sr">スクリーンリーダーの利用状況</p>
  <div role="radiogroup" aria-labelledby="sr" aria-required="true">
  <div role="radio" aria-checked="true" tabindex="0">利用している</div>
  <div role="radio" aria-checked="false" tabindex="0">利用していない</div>
  </div>

<!-- input[type="checkbox"] -->
<p id="sr_type">利用しているスクリーンリーダー</p>
  <div role="group" aria-labelledby="sr_type">
  <div role="checkbox" aria-checked="true" aria-required="true" tabindex="0">PC-Talker</div>
  <div role="checkbox" aria-checked="false" aria-required="true" tabindex="0">NVDA</div>
  </div>

<!-- textarea -->
<p id="other">その他コメント</p>
  <div role="textbox" aria-multiline="true" aria-labelledby="other" aria-required="true" tabindex="0"></div>


<h2>aria-required属性が設定されていない</h2>

<!-- input[type="text"] -->
<p id="usrname2">ログインネーム</p>
  <div role="textbox" aria-labelledby="usrname2" tabindex="0"></div>

<!-- select, option -->
<p id="os_pc2">利用しているOS(PC)</p>
  <!-- select 閉じた状態 (select) -->
  <div role="combobox" aria-controls="combobox-target2" aria-expanded="false" tabindex="0">選択してください</div>

<!-- input[type="radio"] -->
<p id="sr2">スクリーンリーダーの利用状況</p>
  <div role="radiogroup" aria-labelledby="sr2">
  <div role="radio" aria-checked="true" tabindex="0">利用している</div>
  <div role="radio" aria-checked="false" tabindex="0">利用していない</div>
  </div>

<!-- input[type="checkbox"] -->
<p id="sr_type2">利用しているスクリーンリーダー</p>
  <div role="group" aria-labelledby="sr_type2">
  <div role="checkbox" aria-checked="true" tabindex="0">PC-Talker</div>
  <div role="checkbox" aria-checked="false" tabindex="0">NVDA</div>
  </div>

<!-- textarea -->
<p id="other2">その他コメント</p>
  <div role="textbox" aria-multiline="true" aria-labelledby="other2" tabindex="0"></div>

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
aria-required 属性, role 属性値として "textbox" "combobox" "listbox" "radiogroup" "checkbox" のいずれかを持つ div要素