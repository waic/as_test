// 「関連する要素や属性」セクションの書式を検査するカスタムルール
// 各行を `- ` の箇条書きとし、CSS セレクタ風の記法（例: input[type="text"]）で記述する
// 該当なしの場合は `- なし` のみとする

const HEADING = "# 関連する要素や属性";
const COMPOUND = String.raw`[a-z0-9]*(?:\[[a-z-]+(?:="[^"]+")?\]|:[a-z-]+)*`;
const ITEM = /^- (\S(?:.*\S)?)$/;
const SELECTOR = new RegExp(`^${COMPOUND}(?: ${COMPOUND})*$`);

module.exports = {
  names: ["related-elements-format"],
  description: "「関連する要素や属性」セクションの書式",
  tags: ["waic"],
  parser: "none",
  function: ({ lines }, onError) => {
    const start = lines.findIndex((l) => l.trimEnd() === HEADING);
    if (start === -1) {
      return;
    }
    const items = [];
    for (let i = start + 1; i < lines.length && !lines[i].startsWith("# "); i++) {
      const line = lines[i].trimEnd();
      if (line === "") {
        continue;
      }
      const item = ITEM.exec(line)?.[1];
      if (item === undefined || (item !== "なし" && !SELECTOR.test(item))) {
        onError({
          lineNumber: i + 1,
          detail: '`- ` で始まる箇条書きにし、input[type="text"] や [alt] のようにセレクタ形式で記述してください',
          context: line,
        });
      } else {
        items.push(item);
      }
    }
    if (items.length === 0) {
      onError({ lineNumber: start + 1, detail: "項目がありません（該当なしの場合は `- なし` と記述してください）" });
    } else if (items.includes("なし") && items.length > 1) {
      onError({ lineNumber: start + 1, detail: "`- なし` は他の項目と併記できません" });
    }
  },
};
