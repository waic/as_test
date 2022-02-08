## テスト手順や期待される結果に用いられる用語

### 読み上げさせる

スクリーンリーダーが提供しているコマンドをユーザーが実行することによって、結果が音声で伝えられること。

### 何らかの手段

ユーザーエージェント、または支援技術に搭載されている機能の内、下記の要件の全てに当てはまる機能。

1. 支援技術のベンダーより提供されているマニュアルに記載されている。
2. 他のユーザーインタフェースの操作を代行する機能ではない。例えば、マウスの右クリックを行う機能や、OCR を実行する機能は、この要件を満たさない。

### 差し掛かった時

スクリーンリーダーの利用中に、別の要素の位置から当該要素の位置へ読み上げカーソルが移動した時

### 通知される

読み上げカーソルが当該要素に差し掛かった時に、スクリーンリーダーが必要な情報を自動的に伝えること。
例： 見出しに差し掛かった時に、それが見出しであることや見出しレベルなどを自動的に伝える

### 読み飛ばす

ジャンプ機能を利用して、移動前の位置から移動後の位置の手前までに存在する全ての要素を読み上げすることなく、読み上げカーソルを移動する行為。

## スクリーンリーダーのモードや利用頻度の高いコマンドについて

### 読み上げカーソル

スクリーンリーダーが読み上げを行う要素を示すカーソル

PC-Talker「仮想カーソル」、NVDA「レビューカーソル」、JAWS「仮想 PC カーソル」

### テキストモード

ウェブサイトを閲覧するために用いる機能。矢印キーやジャンプ機能などを用いて、ウェブページを読み上げさせることができる。
このモードの利用中は、矢印キーや文字キーなどのキーボード操作が読み上げカーソルの移動のために用いられる。このため、一般的なユーザーエージェントが備えている機能のほとんど(例「矢印キーによるスクロール操作」、「フォームなどへの情報の入力」)が制限される。

PC-Talker/NetReader「行読みモード」「ナビゲーションキーモード」、NVDA「ブラウズモード」、JAWS「仮想 PC カーソルモード」

### フォームモード

ウェブサイトのフォームなどへ情報を入力するための機能。テキストモード利用中とは対照的に、利用者のキー操作がユーザーエージェントにバイパスされるので、入力欄への文字入力や、リストボックスからの項目選択などの操作が可能となる。

PC-Talker「エディットモード」、NVDA「フォーカスモード」、JAWS「フォームモード」

### ジャンプ機能

テキストモード利用中に、任意の位置にある要素を検索し、該当した要素の位置へ読み上げカーソルを移動する機能。

PC-Talker/NVDA「1 文字ナビゲーション」、NetReader「ダイレクトジャンプ」、JAWS「ナビゲーション クイック キー」