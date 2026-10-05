# テスト ID

WAIC-TEST-0057-02

# テストのタイトル

role="slider" へのステート、プロパティ指定

# テストの目的

sliderロールをもつウィジェットに、現在の値及び値の範囲を示すaria-valuemin、aria-valuemax、aria-valuenowが適切に指定され、スライダーの値を変更した際に aria-valuenow の値が現在の状態を反映するように更新されることを確認

# テストの対象となる達成基準

4.1.2

# 関連する達成方法 (複数)

G10
ARIA4
H91

# テストコード (テストファイルへのリンク)

[WAIC-CODE-0057-02](https://waic.github.io/as_test/WAIC-CODE/WAIC-CODE-0057-02.html)

# テストコードのソース (抜粋)

```HTML
<div
  class="slider"
  id="volume-slider"
>
  <div
    class="slider-thumb"
    id="volume-thumb"
    role="slider"
    tabindex="0"
    aria-labelledby="volume-label"
    aria-valuemin="0"
    aria-valuemax="100"
    aria-valuenow="50"
  ></div>
</div>
```

```CSS
    .slider {
      position: relative;
      width: 300px;
      height: 8px;
      margin: 30px 12px;
      background: #ccc;
      border-radius: 4px;
    }

    .slider-thumb {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 24px;
      height: 24px;
      background: #333;
      border-radius: 50%;
      transform: translate(-50%, -50%);
      cursor: pointer;
      touch-action: none;
    }

    .slider-thumb:focus-visible {
      outline: 3px solid #005fcc;
      outline-offset: 3px;
    }
```

```JS
  const slider = document.getElementById("volume-slider");
  const thumb = document.getElementById("volume-thumb");
  const output = document.getElementById("volume-value");

  const min = 0;
  const max = 100;
  const step = 1;

  let value = 50;

  function setValue(newValue) {
    value = Math.max(min, Math.min(max, newValue));
    thumb.setAttribute("aria-valuenow", value);
    output.textContent = value;
    const percent = ((value - min) / (max - min)) * 100;
    thumb.style.left = percent + "%";
  }

  function setValueFromPointer(clientX) {
    const rect = slider.getBoundingClientRect();
    let percent = (clientX - rect.left) / rect.width;
    percent = Math.max(0, Math.min(1, percent));
    const newValue =
      Math.round((min + percent * (max - min)) / step) * step;
    setValue(newValue);
  }

  thumb.addEventListener("keydown", function(event) {
    switch (event.key) {
      case "ArrowRight":
      case "ArrowUp":
        setValue(value + step);
        event.preventDefault();
        break;

      case "ArrowLeft":
      case "ArrowDown":
        setValue(value - step);
        event.preventDefault();
        break;

      case "Home":
        setValue(min);
        event.preventDefault();
        break;

      case "End":
        setValue(max);
        event.preventDefault();
        break;

      case "PageUp":
        setValue(value + step * 10);
        event.preventDefault();
        break;

      case "PageDown":
        setValue(value - step * 10);
        event.preventDefault();
        break;
    }
  });

  slider.addEventListener("pointerdown", function(event) {
    setValueFromPointer(event.clientX);
    thumb.focus();
    thumb.setPointerCapture(event.pointerId);
  });

  thumb.addEventListener("pointermove", function(event) {
    if (!thumb.hasPointerCapture(event.pointerId)) {
      return;
    }
    setValueFromPointer(event.clientX);
  });

  setValue(value);
```

# テスト手順 (視覚閲覧環境)

1. ロールに対して必須とされるステート及びプロパティが存在することを確認する。
2. 必須でなく、サポートもされず、継承もされない WAI-ARIA ステート又はプロパティが存在しないことを確認する。
3. ユーザインタフェースコンポーネントが状態を変更するときに、ステート及びプロパティの値が現在の状態を反映するように更新されていることを確認する。 

# 期待される結果 (視覚閲覧環境)

1. role="slider"にaria-valuenow（必須）があることが確認できる。
2. サポートされていないステート及びプロパティが存在しないことが確認できる。
3. スライダーを変更したときにaria-valuenowの値が変化していることが確認できる。

# テスト実施時の注意点 (視覚閲覧環境)

aria-valuenow の値が、画面上に表示される現在値及びスライダーのつまみの位置と一致していることを確認する。

# テスト手順 (音声閲覧環境)

1. role="slider" が指定されたスライダーにフォーカスを移動する。
2. スライダーのラベル、役割、現在値が読み上げられることを確認する。
3. 矢印キーを使用してスライダーの値を変更する。
4. 値の変更後、変更された現在値がスクリーンリーダーによって認識されることを確認する。

# 期待される結果 (音声閲覧環境)

1. スライダーにフォーカスが移動できる。
2. ラベル「音量」、スライダーであること、及び現在値「50」が認識できる。
3. 矢印キーでスライダーの値を変更できる。
4. スライダーの値を変更すると、変更後の現在値が認識できる。

# テスト実施時の注意点 (音声閲覧環境)

スクリーンリーダーによる具体的な読み上げ方は、使用するブラウザ及びスクリーンリーダーの組み合わせによって異なる場合があるため、読み上げ文言そのものではなく、スライダーの名前、役割及び現在値が認識できることを確認する。

# 関連する要素や属性

role="slider"
aria-labelledby
aria-valuemin
aria-valuemax
aria-valuenow
tabindex