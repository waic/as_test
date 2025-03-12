# テスト ID

WAIC-TEST-0037-01

# テストのタイトル

required 属性による必須項目の特定（input要素、select要素、textarea要素）

# テストの目的

required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数)

1.3.1, 3.3.3

# 関連する達成方法 (複数)

なし

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0037-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0037-01.html)

# テストコードのソース (抜粋)

```html
<h2>required属性が設定されている</h2>
<form action="#" method="post" id="login1" onsubmit="return errorCheck1()">
	<p>注：[*]は必須項目を示します。</p>
	<p>
		<label for="usrname1">ログインネーム[*]</label>
		<input type="text" name="usrname1" id="usrname1" required />
	</p>
	<p>
		<label for="pwd1">パスワード[*]</label>
		<input type="password" name="pwd1" id="pwd1" size="12" required />
	</p>
	<p>
		<label for="os_pc1">利用しているOS(PC)[*]</label>
		<select id="os_pc1" name="os_pc1" required>
		<option value="Windows">Windows</option>
		<option value="macOS">macOS</option>
		</select>
	</p>
	<p>
		<label for="os_mobile1">利用しているOS(モバイル)[*]</label>
		<select id="os_mobile1" name="os_mobile1" required>
		<option value="">選択してください</option>
		<option value="iOS">iOS</option>
		<option value="Android">Android</option>
		</select>
	</p>
	<fieldset>
		<legend>スクリーンリーダーの利用状況</legend>
		<input type="radio" id="yes1" name="sr1" value="1" required />
		<label for="yes1">利用している[*]</label>
		<input type="radio" id="no1" name="sr1" value="2" required />
		<label for="no1">利用していない[*]</label>
	</fieldset>
	<p>利用しているスクリーンリーダー</p>
		<div>
		<input type="checkbox" id="pctk1" name="pctk1" required />
		<label for="pctk1">PC-Talker[*]</label>
		</div>
		<div>
		<input type="checkbox" id="nvda1" name="nvda1" required />
		<label for="nvda1">NVDA[*]</label>
		</div>
		<p>
		<label for="other1">その他コメント[*]</label>
		<textarea id="other1" name="other1" required></textarea>
	</p>
	<p>
		<input type="submit" value="次へ" id="next_btn1" name="next_btn1" />
	</p>
</form>

<h2>required属性が設定されていない</h2>
<form action="#" method="post" id="login2" onsubmit="return errorCheck1()">
	<p>注：[*]は必須項目を示します。</p>
	<p>
		<label for="usrname2">ログインネーム[*]</label>
		<input type="text" name="usrname2" id="usrname2">
	</p>
	<p>
		<label for="pwd2">パスワード[*]</label>
		<input type="password" name="pwd2" id="pwd2" size="12">
	</p>
	<p>
		<label for="os_pc2">利用しているOS(PC)[*]</label>
		<select id="os_pc2" name="os_pc2">
		<option value="Windows">Windows</option>
		<option value="macOS">macOS</option>
		</select>
	</p>
	<p>
		<label for="os_mobile2">利用しているOS(モバイル)[*]</label>
		<select id="os_mobile2" name="os_mobile2">
		<option value="">選択してください</option>
		<option value="iOS">iOS</option>
		<option value="Android">Android</option>
		</select>
	</p>
	<fieldset>
		<legend>スクリーンリーダーの利用状況</legend>
		<input type="radio" id="yes2" name="sr2" value="1">
		<label for="yes2">利用している[*]</label>
		<input type="radio" id="no2" name="sr2" value="2">
		<label for="no2">利用していない[*]</label>
	</fieldset>
	<p>利用しているスクリーンリーダー</p>
		<div>
		<input type="checkbox" id="pctk2" name="pctk2">
		<label for="pctk2">PC-Talker[*]</label>
		</div>
		<div>
		<input type="checkbox" id="nvda2" name="nvda2">
		<label for="nvda2">NVDA[*]</label>
		</div>
	<p>
		<label for="other2">その他コメント[*]</label>
		<textarea id="other2" name="other2"></textarea>
	</p>
	<p>
		<input type="submit" value="次へ" id="next_btn2" name="next_btn2" />
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

テストファイルを操作し、結果を確認

# 期待される結果 (音声閲覧環境)

required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わる

# テスト実施時の注意点 (音声閲覧環境)

なし

# 関連する要素や属性

required 属性が指定されているinput 要素、select 要素、textarea 要素
