# webmcpt-trust-standards — AIエージェントが直接読める、実地検証済みOSSエンジニアリング標準カタログ

英語版（正本）は [README.md](README.md) を参照してください。

## これは何か

世界の本番実証済みOSS 130件超（Django・Kubernetes・curl・Linux・LLVM等）から、
コード品質・ライセンス・コントリビューションの統治規範を横断収集し、
**一次資料のみ**（LICENSE本文そのもの・プロジェクト自身のガバナンス文書・
採用企業自身の技術ブログ）で検証したカタログです。要約の要約は使いません。

全体を [Agent Skills](https://github.com/anthropics/skills) 形式
（SKILL.md＋トピック分割されたreferences）で構造化しているため、
AIコーディングエージェントが必要な深さだけを直接ロードできます。

## クイックスタート — 30秒で使う

**AIコーディングエージェント（Claude Code / Cursor / MCP・Skills対応エージェント）で使う場合：**

1. エージェントが読める場所にこのリポジトリを置く：
   ```bash
   git clone https://github.com/hummer-lab-001/webmcpt-trust-standards
   ```
2. エージェントにこのリポジトリを参照させ、普通の言葉で聞くだけ：
   > 「`skills/c4-selection-criteria/SKILL.md` を使って、**<リポジトリ名>** が
   > 再利用して安全か・本番実証済みかを6軸で採点して。判定前に必ずLICENSE本文を読み、
   > GitHubの表示ラベルは信用しないで。」

これで完結します。エージェントが6軸チェックリストをロードし、指定したリポジトリに適用し、
LICENSE本文に基づいた採点付きの判定を返します。

**手早くライセンス/模範判定だけ知りたい場合：** [`catalog/INDEX.md`](catalog/INDEX.md)
を開いてください。評価したいリポジトリが既に載っているかもしれません（ライセンスは
GitHubラベルではなくLICENSE本文から読んだもの・実証レベル付き）。見送ったリポジトリも、
それぞれ不適格となった具体的な条項とともに記載しています。

**自分でカタログを作りたい場合：** [`skills/c4-selection-criteria/`](skills/c4-selection-criteria/)
をそのままコピーしてください。MITライセンス・自己完結型で、6軸の手法はどんな領域にも応用できます。

## なぜ「WebMCPT」を名に冠するのか

WebMCPTは「AIモデルへの接続を、入口から一次情報で信頼評価し、悪意ある接続・
不透明な意図のMCP接続を排除する」信頼評価プロトコル体系です。
本リポジトリは、その規律——*一次情報で検証し、プラットフォームのラベルや
要約を鵜呑みにしない*——を、MCP接続ではなく「AIエージェントが従うべき
エンジニアリング規範の信頼性」に適用したものです。ライセンスはGitHubの
自動判定でなくLICENSE本文そのもので判定し、採用実績は採用企業自身の
公式発表のみを根拠とします。

WebMCPTはオープンな概念です。誰でも自由に採用・拡張・応用できるよう、
囲い込まずに世界へ差し出しています。目的は「所有すること」ではなく
「共有すること」。本リポジトリはその最初の公開実例であり、エコシステム全体が
許可なく使えるようMITライセンスで公開しています。

> **WebMCPT（Web Model Context Protocol Trust）**とは、
> AIモデルへの接続を入口から信頼評価し、悪意ある接続・
> 不透明な資本構造・意図の不純なMCP接続を排除することで
> AIモデルの文脈純粋性と健全性を守る、日本発の信頼評価プロトコル体系。
>
> 提唱者：HUMMER（ハマー）／NEWXUS DAO 創業者・2024年

## 収録内容（第一弾）

- `skills/c4-selection-criteria/` — リポジトリが「有名」ではなく「本番実証済みの模範」
  かを判定する6軸チェックリスト
- `catalog/license-strategy-patterns.md` — ライセンス戦略の実地分類
  （タイプA〜F・コピーレフト5段階・再ライセンスとフォーク対抗の系譜）
- `catalog/governance-patterns.md` — ガバナンス7系統と、独立に収斂した3つの安全装置
- `catalog/language-style-guide-patterns.md` — Googleの公開スタイルガイド18本
  （Python / C++ / Java / Go / TypeScript / Shell / JavaScript / JSON /
  HTML・CSS / Markdown / C# / Swift / Objective-C / R / Vim script / Common Lisp / XML / AngularJS）を原典で直接読み、各制限に対してガイド自身が
  述べている根拠を記録。逐語引用とパラフレーズを明確に区別し、「読んでいない
  セクション」も各節に明記する。複数ガイドをまたぐ仮説のうち、再現しなかった
  2件も否定的結果として記録している
- `catalog/combination-packs.md` — 上記スタイルガイドをレビュー即用の
  パック（3/6/9本）に組み合わせる。各パックは3層構造＝ガイドが「一致」する
  ルール（賛成ガイドを数える・沈黙は賛成ではない）／「割れる」ルール
  （両論＋推奨を明示）／理由が失効した「化石」（IE8・pre-module）。
  末尾にAIレビュアー用の貼り付けプロンプトブロック。**Web（3本）・Product（6本）・
  Enterprise+Mobile（9本）の3パックとも本体まで完成**。目玉＝GoとJavaのGoogle
  ガイドが頭字語で真っ向から矛盾（Goは`URL`保存/Javaは`Url`畳む）、行長が80陣営
  （JS/Python/C++）vs 100陣営（Java/C#/Swift/Objective-C）に割れる点
- `catalog/INDEX.md` — 厳選登録一覧（ライセンスは全件一次確認済み）

## 誠実性の原則

- 未確認の軸は◇と明記し、切り上げない
- 見送った候補も「検討の上見送り」として根拠条項付きで記録する
- このカタログはOSS世界を「読む」activityであり、調査対象プロジェクトへ
  AI生成コードを提出することはしません

## ライセンス

MIT（[LICENSE](LICENSE)）
