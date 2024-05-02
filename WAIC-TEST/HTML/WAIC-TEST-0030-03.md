# テスト ID 
WAIC-TEST-0030-03

# テストのタイトル 
aria-required 属性による必須項目の特定（role属性）

# テストの目的 
aria-required属性、role属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :
1.3.1, 3.3.3

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
テストファイルを開き、タブキーを使いフォーカスをひとつづつ移動させ、どのように読み上げるかを確認する。このテストファイルは、それぞれの入力/選択項目について、aria-required属性が設定されているものと、設定されていないものが記載されているため、それぞれについて確認を行う。

## テスト手順 1.
テストファイルを開いた状態でタブキーを押し、ログインネームを入力するテキストボックスにフォーカスを移動する

### 期待される結果 1.
ログインネームを入力するテキストボックスにフォーカスが当たっていることと、入力必須であることが読み上げられる

## テスト手順 2.
タブキーを押し、利用しているOSを選択するセレクトボックスへフォーカスを移動させる

### 期待される結果 2.
利用しているOSを選択するセレクトボックスにフォーカスが当たっていることと、選択必須であることが読み上げられる

## テスト手順 3.
タブキーを押し、スクリーンリーダーの利用状況について選択するラジオボタンへフォーカスを移動させる

### 期待される結果 3.
スクリーンリーダーの利用状況について、「利用している」を選択するラジオボタンへとフォーカスが当たっていることと、選択必須であることが読み上げられる。もう一度タブキーを押し、「利用していない」を選択するラジオボタンへとフォーカスが当たっていることが読み上げられることも確認する。

## テスト手順 4.
タブキーを押し、利用しているスクリーンリーダーを選択するチェックボックスへフォーカスを移動させる

### 期待される結果4. 
利用しているスクリーンリーダーについて、「PC-Talker」を選択するチェックボックスにフォーカスが当たっていることと、選択必須であることが読み上げられる。もう一度タブキーを押し、「NVDA」を選択するチェックボックスにフォーカスが当たっていることと、選択必須であることが読み上げられることも確認する。

## テスト手順 5.
タブキーを押し、その他コメントを入力するテキストボックスへフォーカスを移動させる

### 期待される結果 5.
その他コメントを入力するテキストボックスへフォーカスが当たっていることと、入力必須であることが読み上げられる

## テスト手順 6.
タブキーを押し、ログインネームを入力するテキストボックスにフォーカスを移動させる

### 期待される結果 6.
ログインネームを入力するテキストボックスにフォーカスが当たっていることが読み上げられる。ただし、入力必須であることは読み上げられない。

## テスト手順 7.
タブキーを押し、利用しているOSを選択するセレクトボックスにフォーカスを移動させる

### 期待される結果 7.
利用しているOSを選択するセレクトボックスにフォーカスが当たっていることが読み上げられる。ただし、入力必須であることは読み上げられない。

## テスト手順8.
タブキーを押し、スクリーンリーダーの利用状況を選択するラジオボタンにフォーカスを移動させる

### 期待される結果 8.
スクリーンリーダーの利用状況について、「利用している」を選択するラジオボタンへとフォーカスが当たっていることが読み上げられる。もう一度タブキーを押すと、「利用していない」を選択するラジオボタンへとフォーカスが当たっていることが読み上げられる。いづれについても入力必須であることについては読み上げられない。

## テスト手順9.
タブキーを押し、利用しているスクリーンリーダーを選択するチェックボックスにフォーカスを移動させる

### 期待される結果9.
利用しているスクリーンリーダーについて、「PC-Talker」を選択するチェックボックスにフォーカスが当たっていることが読み上げられる。もう一度タブキーを押すと、「NVDA」を選択するチェックボックスにフォーカスが当たっていることが読み上げられる。いづれについても入力必須であることについては読み上げられない。

## テスト手順10.
タブキーを押し、その他コメントを入力するテキストボックスにフォーカスを移動させる

### 期待される結果 10.
その他コメントを入力するテキストボックスにフォーカスが当たっていることが読み上げられる。入力必須であることについては読み上げられない。

# 期待される結果 (音声閲覧環境) 
テスト手順1～10の結果をすべて満たしている。

# テスト実施時の注意点 (音声閲覧環境) 
矢印キーなどは使用せず、タブキーのみを使用してテストを行う

# 関連する要素や属性 :
aria-required 属性, role 属性値として "textbox" "combobox" "radiogroup" "checkbox" のいずれかを持つ div要素