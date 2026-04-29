---
marp: true
theme: default
size: 16:9
paginate: true
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap');

:root {
  --color-background: #ffffff;
  --color-foreground: #1f2937;
  --color-heading: #1e40af;
  --color-accent: #2563eb;
  --color-accent-2: #0f766e;
  --color-border: #d1d5db;
  --color-muted: #6b7280;
  --color-soft: #f8fafc;
  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
}

section {
  background-color: var(--color-background);
  color: var(--color-foreground);
  font-family: var(--font-default);
  font-size: 22px;
  line-height: 1.65;
  box-sizing: border-box;
  border-top: 8px solid var(--color-heading);
  padding: 56px;
}

h1, h2, h3 {
  color: var(--color-heading);
  font-weight: 800;
  margin: 0;
  letter-spacing: 0;
}

h1 {
  font-size: 52px;
  line-height: 1.28;
}

h2 {
  position: absolute;
  top: 40px;
  left: 56px;
  right: auto;
  width: 640px;
  max-width: calc(100% - 112px);
  font-size: 37px;
  padding-bottom: 14px;
  border-bottom: 3px solid var(--color-accent);
}

h2 + * {
  margin-top: 108px;
}

h3 {
  color: var(--color-accent-2);
  font-size: 25px;
  margin-top: 20px;
  margin-bottom: 10px;
}

p {
  margin: 0 0 16px;
}

ul, ol {
  padding-left: 32px;
  margin-top: 8px;
}

li {
  margin-bottom: 9px;
}

strong {
  color: var(--color-heading);
  font-weight: 800;
}

code {
  background-color: #eef2f7;
  color: #164e63;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.88em;
}

pre {
  background: #111827;
  color: #f9fafb;
  border-radius: 8px;
  padding: 18px 22px;
  font-size: 18px;
  line-height: 1.52;
  overflow: hidden;
}

pre code {
  background: transparent;
  color: #f8fafc !important;
  padding: 0;
  border-radius: 0;
  font-size: inherit;
}

pre code span {
  color: #f8fafc !important;
}

pre code .hljs-section,
pre code .hljs-title {
  color: #bfdbfe !important;
}

pre code .hljs-bullet,
pre code .hljs-string,
pre code .hljs-code {
  color: #f8fafc !important;
}

pre code .hljs-comment,
pre code .hljs-quote {
  color: #f8fafc !important;
  font-style: normal;
}

pre code .hljs-emphasis,
pre code .hljs-strong {
  color: #f8fafc !important;
  font-style: normal;
  font-weight: 400;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 18px 0;
  max-width: 780px;
  font-size: 20px;
}

th, td {
  border: 1px solid var(--color-border);
  padding: 12px 14px;
  text-align: left;
  vertical-align: top;
}

th {
  background-color: var(--color-heading);
  color: #ffffff;
  font-weight: 700;
}

tr:nth-child(even) {
  background-color: var(--color-soft);
}

footer {
  color: var(--color-muted);
  font-size: 15px;
}

section.lead {
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: linear-gradient(135deg, #ffffff 0%, #eef6ff 62%, #f5fbf8 100%);
}

section.lead h1 {
  margin-bottom: 30px;
}

section.lead p {
  font-size: 25px;
  font-weight: 500;
}

.eyebrow {
  display: inline-block;
  color: var(--color-accent-2);
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 18px;
}

.section-label {
  display: inline-block;
  color: #ffffff;
  background: var(--color-accent-2);
  border-radius: 999px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 0.04em;
  padding: 4px 12px;
  margin-bottom: 12px;
}

.lead-text {
  color: var(--color-muted);
  font-size: 19px;
  font-weight: 500;
  margin-bottom: 14px;
}

.small {
  font-size: 17px;
}

.compact {
  font-size: 19px;
}

.note {
  color: var(--color-muted);
  font-size: 18px;
}

.accent {
  color: var(--color-accent-2);
  font-weight: 800;
}
</style>

<!-- _class: lead -->

![bg right:45% fit opacity:0.2](images/workflow-overview.png)

<p class="eyebrow">Chapter 01 / Minutes Workflow</p>

# 発言ログから<br>議事録を作成する

AI・コーディングエージェントを活用した<br>議事録作成とファイル変換

---

## 本章ゴール

<p class="lead-text"><span class="accent">発言ログを業務で使える議事録へ変換する</span>ための全体像を扱う。</p>

- 発言ログから重要情報を抽出する
- 議事録を実務で使える構造に整える
- Excel / Word / PDF への変換方針を理解する
- エージェントスキルで一連の作業を自動化する

---

## 全体ワーク

![bg right:45% fit](images/workflow-overview.png)

- 発言ログから議事録本文を作成する
- 確定した内容を共有用ファイルへ変換する
- 繰り返す処理はスキル化して再利用する

---

## AIへの指示

<p class="lead-text">品質を左右するのは、AIに渡す<span class="accent">判断基準</span>の明確さ。</p>

- 発言ログには雑談、言い直し、曖昧表現が混在する
- 単に「議事録を作成して」では判断がぶれやすい
- 記載対象、構成、詳しさを先に指定する
- 不明点は断定せず「要確認」として扱う

---

## フォーマット

議事録は「後で使う情報」ごとに分ける。

| 区分 | 主な内容 |
|---|---|
| 基本 | 会議名、日時、参加者、目的 |
| 議論 | アジェンダ、要約、主な発言 |
| 管理 | 決定事項、ToDo、保留事項 |
| 補足 | リスク、次回会議、抽出メモ |

---

## チャット型AI

![bg right:45% fit](images/chat-ai-minutes-flow.png)

- Gemini や ChatGPT の入力欄に条件を渡す
- 発言ログと出力形式を同じ依頼に含める
- 事前指示に登録すると入力の手間を減らせる

---

## プロンプト例

```markdown
# 指示内容
以下の文字起こしデータを分析し、
指定フォーマットで議事録を作成してください。

## 文字起こしデータ
【会議ログを貼り付け】

## 出力形式
【議事録フォーマットを貼り付け】
```

出力後は、決定事項・ToDo・不明項目を確認する。

---

## エージェント型

![bg right:45% fit](images/coding-agent-reference-structure.png)

- プロジェクト内のファイルを参照できる
- 長いフォーマット定義を毎回貼らずに済む
- `@ファイル名` 指定で材料を渡しやすい

---

## 参照構成

| ファイル | 役割 |
|---|---|
| `meeting_minutes_format.md` | 議事録フォーマット |
| `meeting_minutes_rules.md` | 記載ルール |
| `meeting_transcription_sample.md` | 発言ログ |
| `meeting_audio.mp3` | 必要に応じた音声 |

```markdown
@meeting_minutes_format.md と
@meeting_transcription_sample.md を参照して議事録を作成してください。
```

---

## 変換先

![bg right:45% fit](images/minutes-file-conversion-flow.png)

- 議事録本文を確定してから変換する
- 共有、編集、保管の目的に合わせて形式を選ぶ
- 変換後はレイアウトと記載漏れを確認する

---

## 形式選択

| 形式 | 向いている用途 |
|---|---|
| Word / docx | 文章中心のレビュー、社内文書 |
| Excel / xlsx | ToDo、決定事項、一覧管理 |
| PDF | 配布、保管、改変防止 |
| Docs / Sheets | 共同編集、継続運用 |

---

## 手動運用

<span class="section-label">Manual</span>

AIが出力した議事録をコピーし、指定ファイルへ貼り付ける。

- 最も始めやすい運用
- 特別な自動変換機能は不要
- 体裁調整と最終確認は手作業になる

---

## スキル活用

![bg right:45% fit](images/agent-skill-conversion-workflow.png)

- 議事録作成からファイル生成まで一連で依頼できる
- 転記漏れや整形の手間を減らせる
- 形式ごとの専門スキルへ処理を委譲する

---

## xlsxの役割

<span class="section-label">Excel出力</span>

`xlsx` スキルは、議事録データを Excel に反映するために使う。

- 新規 `.xlsx` ファイルを作成する
- 既存テンプレートへ追記・更新する
- 決定事項やToDoを表として管理する

---

## Excel導入

| ツール | 導入・配置の要点 |
|---|---|
| Claude Code | `document-skills` プラグイン |
| Antigravity | `.agents/skills/` |
| Cursor | `.cursor/skills/` または `.agents/skills/` |
| Codex | 任意配置と設定ファイルで参照 |
| Copilot | `.github/skills/` |

---

## 新規Excel出力

```markdown
/xlsx
以下の議事録データをもとに Excel を作成してください。

## 出力先
- minutes_YYYYMMDD.xlsx

## シート構成
- 基本情報・要約
- アジェンダ・議論内容
- 決定事項・ToDo
- 保留事項・リスク・次回会議
```

---

## 既存Excel反映

```markdown
/xlsx
既存の minutes_template.xlsx に内容を反映してください。

## 出力
- minutes_filled_YYYYMMDD.xlsx
- 元テンプレートは上書きしない

## 反映ルール
- 既存の見出しと書式を維持
- 表の列構成に合わせて追記
- 不明項目は「要確認」
```

---

## PDF出力演習

<span class="section-label">PDF出力</span>

- 作成済み議事録をPDF形式へ変換する
- 見出し、表、改ページ、余白を具体的に指定する
- 共有資料として読める体裁を目指す
- 生成後に崩れや不足を確認する

---

## PDF確認

| 観点 | チェック内容 |
|---|---|
| 見出し | 章構成が崩れていない |
| 表 | 列幅と改ページが自然 |
| 内容 | 決定事項、ToDo、保留事項が反映済み |
| 共有性 | そのまま配布できる見た目 |

---

## Skill-Creator

![bg right:45% fit](images/custom-skill-orchestration-flow.png)

- 毎回のプロンプト入力を減らす
- 議事録作成と変換手順を標準化する
- 一連の処理を独自スキルとして再利用する

---

## オーケストレーター

<span class="section-label">スキル作成</span>

独自スキルは司令塔として振る舞う。

- 発言ログから重要事項を抽出する
- 指定フォーマットで議事録本文を作成する
- 出力形式に応じて変換スキルを呼び出す
- 未インストールのスキルは処理前に通知する

---

## スキル連携

| 変換先 | 呼び出すスキル | 引き渡す内容 |
|---|---|---|
| Excel | `xlsx` | 議事録本文、シート構成 |
| Word | `docx` | 議事録本文、文書構成 |
| PDF | `pdf` | 議事録本文、体裁条件 |

---

## 処理フロー

<p class="lead-text">前工程の成果物を、次の専門スキルへ<span class="accent">明示的に渡す</span>設計にする。</p>

1. 入力された発言ログを確認する
2. 議事録に必要な情報を抽出する
3. 指定フォーマットで本文を生成する
4. ファイル形式ごとのスキルへ委譲する
5. 変換結果の確認事項を提示する

---

## テスト設計

| ケース | 確認したいこと |
|---|---|
| xlsx 出力 | シート構成と表が生成される |
| docx 出力 | 見出し構成が文書化される |
| PDF 出力 | 表と改ページが崩れない |
| 情報不足 | 必要な確認質問が出る |

---

## まとめ

- <span class="accent">議事録品質は指示設計で安定する</span>
- 決定事項、ToDo、保留事項を分ける
- 共有形式への変換は用途から選ぶ
- 繰り返す業務はスキル化して再利用する
