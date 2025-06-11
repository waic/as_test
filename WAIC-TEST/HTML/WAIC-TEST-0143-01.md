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

# テストコードのソース (抜粋)

```html
<h2 id="chatHeading">会話のログ</h2>
<div id="chatLog" role="log" aria-labelledby="chatHeading">
    <ul id="chatMessage"></ul>
</div>
```

```JavaScript
function makeChat () {
	var chatText = ["自動返信：こんにちわ！", "自動返信：返信はこれで終了です"];
	var chatContent = document.getElementById("chatMessage");
	var list = document.createElement("li")
	var item = document.createTextNode(chatText[counter]);
	list.appendChild(item);
	chatContent.appendChild(list);
	counter++;
	if (counter > 1) {
		clearInterval(myVar);
	} 
}
```

# テスト手順 (視覚閲覧環境)

## テスト手順 1

「メッセージを送る」ボタンを押下する

## 期待される結果 1

「会話のログ」見出しの後に、「あなた：こんにちわ」と表示される

## テスト手順 2

「メッセージを送る」の押下後、何もしないまま6秒程度待つ

## 期待される結果 2

3秒後に「自動返信：こんにちわ！」と通知され、さらに3秒後に「自動返信：返信はこれで終了です」と表示される

# テスト実施時の注意点 (視覚閲覧環境)

- ブラウザのJavaScriptが有効になっていることを確認すること

# テスト手順 (音声閲覧環境)

## テスト手順 1

「メッセージを送る」ボタンを押下する

## 期待される結果 1

「あなた：こんにちわ」と通知される

## テスト手順 2

「メッセージを送る」の押下後、何もしないまま6秒程度待つ

## 期待される結果 2

3秒後に「自動返信：こんにちわ！」と通知され、さらに3秒後に「自動返信：返信はこれで終了です」と通知される

# テスト実施時の注意点 (音声閲覧環境)

- ブラウザのJavaScriptが有効になっていることを確認すること
- テストの通知を待つ間に他の通知が生じた場合、他の通知の完了後にテストによるメッセージが通知される。そのため、必ずしも3秒後にメッセージが通知されるとは限らない

# 関連する要素や属性

role属性、aria-labelledby属性
