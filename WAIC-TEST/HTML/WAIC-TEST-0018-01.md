

# テスト ID
WAIC-TEST-0018-01

# テストのタイトル
fieldset 要素及び legend 要素によるグループ化 (ラジオボタン)

# テストの目的
fieldset 要素及び legend 要素によってラジオボタンをグループ化した場合、グループの説明が表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)
1.3.1, 3.3.2

# 関連する達成方法 (複数)
H71

# テストコード (テストファイルへのリンク)
[WAIC-CODE-0018-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0018-01.html)

# テストコードのソース (抜粋)
```html
<div>
<p>文学作品に関するクイズです。</p>
<fieldset>
<legend>ハムレットの作者は？</legend>
<input type="radio" id="shakesp" name="hamlet" checked value="a">
<label for="shakesp">ウィリアム・シェイクスピア</label><br>
<input type="radio" id="kipling" name="hamlet" value="b">
<label for="kipling">ラドヤード・キップリング</label><br>
<input type="radio" id="gbshaw" name="hamlet" value="c">
<label for="gbshaw">ジョージ・バーナード・ショー</label><br>
<input type="radio" id="hem" name="hamlet" value="d">
<label for="hem">アーネスト・ヘミングウェイ</label><br>
<input type="radio" id="dickens" name="hamlet" value="e">
<label for="dickens">チャールズ・ディケンズ</label>
</fieldset>

<fieldset>
<legend>坊っちゃんの作者は？</legend>
<input type="radio" id="ryunosuke" name="bocchan" checked value="a">
<label for="ryunosuke">芥川龍之介</label><br>
<input type="radio" id="soseki" name="bocchan" value="b">
<label for="soseki">夏目漱石</label><br>
<input type="radio" id="ogai" name="bocchan" value="c">
<label for="ogai">森鴎外</label><br>
</fieldset>

<p><input type="radio" id="yasunari" name="outOfFieldset" value="k"><label for="yasunari">川端康成</label></p>

<p>正解はウェブサイトをご確認ください。</p>
</div>

```
# テスト手順 (視覚閲覧環境)
一時保留

# 期待される結果 (視覚閲覧環境)
なし

# テスト実施時の注意点 (視覚閲覧環境)
なし

# テスト手順 (音声閲覧環境)
コントロール間を直接移動した際の読み上げ内容を確認

# 期待される結果 (音声閲覧環境)
次の 1. 〜 3. をすべて満たしている
1. “ウィリアム・シェイクスピア” に差し掛かると、legend 要素の内容である “ハムレットの作者は?” が通知される
2. “芥川龍之介” に差し掛かると、legend 要素の内容である “坊っちゃんの作者は?” が通知される
3. “川端康成” に差し掛かると、直前の fieldset 要素内のグループの一要素であると誤解されるような通知をされない

# テスト実施時の注意点 (音声閲覧環境)
テストコードをマークアップ順に順次読み上げるのではなく、Tab キー／コントロール間移動モード／直接タップなどの操作でラジオボタンに直接移動する

# 関連する要素や属性
fieldset 要素 , legend 要素 , type="radio" を持つ input 要素


