# テスト ID

WAIC-TEST-0143-01

# テストのタイトル

role属性による逐次的な更新の通知(role="log"の使用)

# テストの目的

role="log"を持つ要素の内容を更新した際に、更新内容だけが通知されることを確認する。

# テストの対象となる達成基準 (複数)

4.1.3

# 関連する達成方法 (複数)

ARIA23

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0143-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0143-01.html)

# テストコードのソース (抜粋)

```html
<h2 id="chatHeading">会話のログ</h2>
<div id="chatLog" role="log">
    <ul id="chatMessage"></ul>
</div>
```

```JavaScript
function makeChat () {
	var chatText = ["自動返信：こんにちわ！", "自動返信：5つカウントした後、返信を終了します", "自動返信：1", "自動返信：2", "自動返信：3", "自動返信：4", "自動返信：5", "自動返信：返信はこれで終了です"];
	var chatContent = document.getElementById("chatMessage");
	var list = document.createElement("li")
	var item = document.createTextNode(chatText[counter]);
	list.appendChild(item);
	chatContent.appendChild(list);
	counter++;
	if (counter > 7) {
		clearInterval(myVar);
	} 
}
```

# テスト手順と期待される結果 (視覚閲覧環境)

テスト不要

# テスト実施時の注意点 (視覚閲覧環境)

なし

# テスト手順と期待される結果 (音声閲覧環境)

## テスト手順 1

「メッセージを送る」ボタンを押下する

## 期待される結果 1

「あなた：こんにちわ」と通知される

## テスト手順 2

「メッセージを送る」ボタンのすぐ後に続く「ダミーコンテンツです」から始まるリンクへと移動する

## 期待される結果 2

リンク内容の通知の後、「自動返信」から始まるメッセージが通知される（リンク内容の通知は、自動返信の通知に遮られないこと）

# テスト実施時の注意点 (音声閲覧環境)

- ブラウザのJavaScriptが有効になっていることを確認すること
- 自動返信メッセージの通知中に次の自動返信が生じた場合、それまでの自動返信は中断される場合がある

# 関連する要素や属性

role属性
