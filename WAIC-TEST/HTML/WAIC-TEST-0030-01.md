# テスト ID 
WAIC-TEST-0030-01

# テストのタイトル 
aria-required 属性による必須項目の特定（input要素、select要素、textarea要素）

# テストの目的 

aria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わることを確認する

# テストの対象となる達成基準 (複数) :
1.3.1
3.3.3

# 関連する達成方法 (複数) :
ARIA2

# テストコード (テストファイルへのリンク) :
[WAIC-CODE-0030-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0030-01.html)

# テストコードのソース (抜粋)

```html
<h2>aria-required属性が設定されている</h2>
<form action="#" method="post"  id="login1" onsubmit="return errorCheck1()">
	<p>注：[*]は必須項目を示します。</p>
	<p>
		<label for="usrname">ログインネーム</label>
		<input type="text" name="usrname" id="usrname" aria-required="true"/>[*]
	</p>
	<p>
		<label for="pwd">パスワード</label>
		<input type="password" name="pwd" id="pwd" size="12" aria-required="true"/>[*]
	</p>
	<p>
		<label for="os_pc">利用しているOS(PC)</label>
		<select id="os_pc" name="os_pc" aria-required="true"/>[*]
		<option value="Windows">Windows</option>
		<option value="macOS">macOS</option>
		</select>
	</p>
	<p>
		<label for="os_mobile">利用しているOS(モバイル)</label>
		<select id="os_mobile" name="OS_mobile" aria-required="true"/>[*]
		<option value="">選択してください</option>
		<option value="iOS">iOS</option>
		<option value="Android">Android</option>
		</select>
	</p>
	<p>スクリーンリーダーの利用状況</p>
		<div>
		<input type="radio" id="yes" name="sr" value="1" aria-required="true"/>[*]
		<label for="yes">利用している</label>
		</div>
		<div>
		<input type="radio" id="no" name="sr" value="2" aria-required="true"/>[*]
		<label for="no">利用していない</label>
		</div>
	<p>利用しているスクリーンリーダー</p>
		<div>
		<input type="checkbox" id="pctk" name="pctk" aria-required="true"/>[*]
		<label for="pctk">PC-Talker</label>
		</div>
		<div>
		<input type="checkbox" id="nvda" name="nvda" aria-required="true"/>[*]
		<label for="nvda">NVDA</label>
		</div>
		<p>
		<label for="other">その他コメント[*]</label>
		<textarea id="other" name="other" aria-required="true"/></textarea>
	</p>
	<p>
		<input type="submit" value="次へ" id="next_btn" name="next_btn"/>
	</p>

</form>

<h2>aria-required属性が設定されていない</h2>
<form action="#" method="post"  id="login2" onsubmit="return errorCheck1()">
	<p>注：[*]は必須項目を示します。</p>
	<p>
		<label for="usrname1">ログインネーム</label>
		<input type="text" name="usrname1" id="usrname1">[*]
	</p>
	<p>
		<label for="pwd1">パスワード</label>
		<input type="password" name="pwd1" id="pwd1" size="12">[*]
	</p>
	<p>
		<label for="os_pc1">利用しているOS(PC)</label>
		<select id="os_pc1" name="os_pc1">[*]
		<option value="Windows">Windows</option>
		<option value="macOS">macOS</option>
	</select>
	</p>
	<p>
		<label for="os_mobile1">利用しているOS(モバイル)</label>
		<select id="os_mobile1" name="OS_mobile">[*]
		<option value="">選択してください</option>
		<option value="iOS">iOS</option>
		<option value="Android">Android</option>
		</select>
	</p>
	<p>スクリーンリーダーの利用状況</p>
		<div>
		<input type="radio" id="yes1" name="sr1" value="1">[*]
		<label for="yes1">利用している</label>
		</div>
		<div>
		<input type="radio" id="no1" name="sr1" value="2">[*]
		<label for="no1">利用していない</label>
		</div>
	<p>利用しているスクリーンリーダー</p>
		<div>
		<input type="checkbox" id="pctk1" name="pctk1">[*]
		<label for="pctk1">PC-Talker</label>
		</div>
		<div>
		<input type="checkbox" id="nvda1" name="nvda1">[*]
		<label for="nvda1">NVDA</label>
		</div>
	<p>
		<label for="other1">その他コメント[*]</label>
		<textarea id="other1" name="other1"></textarea>
	</p>
	<p>
		<input type="submit" value="次へ" id="next_btn" name="next_btn"/>
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

aria-required属性が設定された要素にフォーカスを移動した際、支援技術に必須であることが伝わる

# テスト実施時の注意点 (音声閲覧環境) 
なし

# 関連する要素や属性 :
aria-required 属性が指定されているinput 要素