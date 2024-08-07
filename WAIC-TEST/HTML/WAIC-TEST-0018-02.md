# テスト ID

WAIC-TEST-0018-02

# テストのタイトル

fieldset 要素及び legend 要素によるグループ化 (チェックボックス)

# テストの目的

fieldset 要素及び legend 要素によってチェックボックスをグループ化した場合、グループの説明が表示・読み上げされるかの確認

# テストの対象となる達成基準 (複数)

1.3.1, 3.3.2

# 関連する達成方法 (複数)

H71

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0018-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0018-02.html)

# テストコードのソース (抜粋)

```html
<div>
<p>文学に関するアンケートです。</p>
<fieldset>
<legend>好きな外国の作家は？</legend>
<input type="checkbox" id="shakesp" name="nobelist01" value="a">
<label for="shakesp">ウィリアム・シェイクスピア</label><br>
<input type="checkbox" id="kipling" name="nobelist02" value="b">
<label for="kipling">ラドヤード・キップリング</label><br>
<input type="checkbox" id="gbshaw" name="nobelist03" value="c">
<label for="gbshaw">ジョージ・バーナード・ショー</label><br>
<input type="checkbox" id="hem" name="nobelist04" value="d">
<label for="hem">アーネスト・ヘミングウェイ</label><br>
<input type="checkbox" id="dickens" name="nobelist05" value="e">
<label for="dickens">チャールズ・ディケンズ</label>
</fieldset>

<fieldset>
<legend>好きな日本の作家は？</legend>
<input type="checkbox" id="ryunosuke" name="nobelist06" value="a">
<label for="ryunosuke">芥川龍之介</label><br>
<input type="checkbox" id="soseki" name="nobelist07" value="b">
<label for="soseki">夏目漱石</label><br>
<input type="checkbox" id="ogai" name="nobelist08" value="c">
<label for="ogai">森鴎外</label><br>
</fieldset>

<p><input type="checkbox" id="yasunari" name="outOfFieldset" value="k"><label for="yasunari">川端康成</label></p>

<p>回答が終わりましたら「送信」ボタンをクリックしてください。</p>
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

次の 1. 〜 3. をすべて満たしている、あるいは 4. を満たしている

1. 1 番目の fieldset 要素内の各チェックボックスに差し掛かると、legend 要素の内容である “好きな外国の作家は?” が通知される
2. 2 番目の fieldset 要素内の各チェックボックスに差し掛かると、legend 要素の内容である “好きな日本の作家は?” が通知される
3. “川端康成” に差し掛かると、直前の fieldset 要素内のグループの一要素であると誤解されるような通知をされない
4. fieldset 要素の開始位置及び終了位置を知るための何らかの手段が提供されている

# テスト実施時の注意点 (音声閲覧環境)

テストコードをマークアップ順に順次読み上げるのではなく、Tab キー／コントロール間移動モード／直接タップなどの操作でチェックボックスに直接移動する

# 関連する要素や属性

fieldset 要素 , legend 要素 , type="checkbox" を持つ input 要素
