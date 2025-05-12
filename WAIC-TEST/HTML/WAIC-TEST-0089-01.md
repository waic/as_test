# テスト ID

WAIC-TEST-0089-01

# テストのタイトル

HTMLのdialog要素を使用してモーダルダイアログを作成する

# テストの目的

HTMLのdialog要素で作られたモーダルダイアログが機能するかどうかを確認する

# テストの対象となる達成基準 (複数)

2.4.3

# 関連する達成方法 (複数)

H102

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0089-01](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0089-01.html)

# テストコードのソース (抜粋)

```HTML
  <body>
    <main>
      <h1>ターボ・エンカビュレーター ニュース</h1>
      <button class="open-modal" type="button">メーリングリストに登録してください！</button>
    </main>
    <dialog aria-labelledby="dialog-heading" id="mailing-list-dialog">
      <h1 id="dialog-heading" tabindex="-1">メーリングリストに登録</h1>
      <form>
        <p class="req-note">すべての入力欄は必須です</p>
        <div>
          <label for="fname">名前(姓)</label>
          <input aria-required="true" autocomplete="given-name" id="fname" type="text">
        </div>
        <div>
          <label for="lname">名前(名)</label>
          <input aria-required="true" autocomplete="family-name" id="lname" type="text">
        </div>
        <div>
          <label for="email">メールアドレス</label>
          <input aria-required="true" autocomplete="email" id="email" type="text">
        </div>
        <button class="sign-up" type="submit">登録</button>
      </form>
     <form method="dialog">
        <button aria-label="閉じる" class="close-modal">&times;</button>
      </form>
    </dialog>
  </body>
```

# テスト手順と期待される結果 (視覚閲覧環境)

## テスト手順 1

キーボード操作で「メーリングリストに登録してください！」ボタンを押す

## 期待される結果 1

「メーリングリストに登録」というモーダルダイアログが開き、フォーカスがモーダルダイアログ内に移動する

## テスト手順 2

キーボード操作で、モーダルダイアログ上でフォーカスを移動する。それを繰り返す

## 期待される結果 2

フォーカスはモーダルダイアログ内の入力欄やボタンに移るが、モーダルダイアログの外には出ない (「メーリングリストに登録してください！」ボタンにフォーカスが移らない)

## テスト手順 3

キーボード操作で、モーダルダイアログ内の「閉じる」ボタン (見た目は「×」と表示されているボタン) を押す

## 期待される結果 3

ダイアログが閉じ、フォーカスが「メーリングリストに登録してください！」ボタンに移る

# テスト実施時の注意点 (視覚閲覧環境)

ダイアログ内のフォーム送信は機能せず、「登録」ボタンを押しても何も起こらないのが正しい (送信のテストは不要である)

# テスト手順と期待される結果 (音声閲覧環境)

## テスト手順 1

「メーリングリストに登録してください！」ボタンを押す

## 期待される結果 1

「メーリングリストに登録」というモーダルダイアログが開き、フォーカスがモーダルダイアログ内に移動する

## テスト手順 2

モーダルダイアログ上でフォーカスを移動する。それを繰り返す

## 期待される結果 2

フォーカスはモーダルダイアログ内の入力欄やボタンに移るが、モーダルダイアログの外には出ない (「メーリングリストに登録してください！」ボタンにフォーカスが移らない)

## テスト手順 3

モーダルダイアログ内の「閉じる」ボタンを押す

## 期待される結果 3

ダイアログが閉じ、フォーカスが「メーリングリストに登録してください！」ボタンに移る

# テスト実施時の注意点 (音声閲覧環境)

ダイアログ内のフォーム送信は機能せず、「登録」ボタンを押しても何も起こらないのが正しい (送信のテストは不要である)

# 関連する要素や属性

dialog要素、aria-describedby属性、aria-label属性
