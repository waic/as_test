# テスト ID 

WAIC-TEST-0030-05

# テストのタイトル 

JavaScriptによって挿入されたaria-required 属性による必須項目の特定（input要素、select要素、textarea要素）

# テストの目的 

JavaScriptによって挿入されたaria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :

1.3.1
3.3.3

# 関連する達成方法 (複数) :

ARIA2

# テストコード (テストファイルへのリンク) :

[WAIC-CODE-0030-05](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0030-05.html)

# テストコードのソース (抜粋)

```html
<script type="text/javascript">
	//<![CDATA[
	// array or ids on the required fields on this page
	var requiredIds = new Array( "usrname", "pwd", "os_pc", "os_mobile", "yes", "no", "pctk", "nvda", "other");
	// function that is run after the page has loaded to set the aria-required property on each of the
	//elements in requiredIds array of id values
	function setRequired(){
	if (requiredIds){
		var field;
		for (var i = 0; i< requiredIds.length; i++){
			field = document.getElementById(requiredIds[i]);
			field.setAttribute("aria-required", "true");
		}
	}
	}
	window.onload=setRequired;
	//]]>
</script>
<p>以下のデータを入力してください。入力必須項目はプログラムによって特定されており、併せて[*]も記載されています。</p>
	<form action="#" method="post" onsubmit="return errorCheck1()">
	<p>
		<label for="usrname">ログインネーム *: </label>
		<input type="text" name="usrname" id="usrname">
	</p>
	<p>
		<label for="pwd">パスワード *: </label>
		<input type="password" name="pwd" id="pwd" size="12">
	</p>
	<p>
		<label for="os_pc">利用しているOS(PC) *: </label>
		<select id="os_pc" name="os_pc">
		<option value="Windows">Windows</option>
		<option value="macOS">macOS</option>
		</select>
	</p>
	<p>
		<label for="os_mobile">利用しているOS(モバイル) *: </label>
		<select id="os_mobile" name="OS_mobile">
		<option value="">選択してください</option>
		<option value="iOS">iOS</option>
		<option value="Android">Android</option>
		</select>
	</p>
	<p>スクリーンリーダーの利用状況</p>
		<div>
		<input type="radio" id="yes" name="sr" value="1"> *: 
		<label for="yes">利用している</label>
		</div>
		<div>
		<input type="radio" id="no" name="sr" value="2"> *: 
		<label for="no">利用していない</label>
		</div>
	<p>利用しているスクリーンリーダー</p>
		<div>
		<input type="checkbox" id="pctk" name="pctk"> *: 
		<label for="pctk">PC-Talker</label>
		</div>
		<div>
		<input type="checkbox" id="nvda" name="nvda"> *: 
		<label for="nvda">NVDA</label>
		</div>
	<p>
		<label for="other">その他コメント *: </label>
		<textarea id="other" name="other1"></textarea>
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

テストファイルを開き、タブキーや矢印キーを使いフォーカスをひとつづつ移動させ、どのように読み上げるかを確認する。

## テスト手順 1.

テストファイルを開いた状態でタブキーや矢印キーを押し、ログインネームを入力するテキストボックスにフォーカスを移動する

### 期待される結果 1.

ログインネームを入力するテキストボックスにフォーカスが当たっていることと、入力必須であることが読み上げられる

## テスト手順 2.

タブキーや矢印キーを押し、利用しているOSを選択するセレクトボックスへフォーカスを移動させる

### 期待される結果 2.

利用しているOSを選択するセレクトボックスにフォーカスが当たっていることと、選択必須であることが読み上げられる

## テスト手順 3.

タブキーや矢印キーを押し、スクリーンリーダーの利用状況について選択するラジオボタンへフォーカスを移動させる

### 期待される結果 3.

スクリーンリーダーの利用状況について、「利用している」を選択するラジオボタンへとフォーカスが当たっていることと、選択必須であることが読み上げられる。もう一度タブキーを押し、「利用していない」を選択するラジオボタンへとフォーカスが当たっていることが読み上げられることも確認する。

## テスト手順 4.

タブキーや矢印キーを押し、利用しているスクリーンリーダーを選択するチェックボックスへフォーカスを移動させる

### 期待される結果4.

利用しているスクリーンリーダーについて、「PC-Talker」を選択するチェックボックスにフォーカスが当たっていることと、選択必須であることが読み上げられる。もう一度タブキーを押し、「NVDA」を選択するチェックボックスにフォーカスが当たっていることと、選択必須であることが読み上げられることも確認する。

## テスト手順 5.

タブキーや矢印キーを押し、その他コメントを入力するテキストボックスへフォーカスを移動させる

### 期待される結果 5.

その他コメントを入力するテキストボックスへフォーカスが当たっていることと、入力必須であることが読み上げられる

# 期待される結果 (音声閲覧環境) 

テスト手順1～5の結果をすべて満たしている。

# テスト実施時の注意点 (音声閲覧環境) 

なし

# 関連する要素や属性 :

aria-required 属性が指定されているinput 要素、select 要素、textarea 要素