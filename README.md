# Discord Q&A データベース化プロジェクト

## 概要
DiscordのQ&Aチャンネルの質問と回答をデータベース化する。

## フィールド構成
| フィールド | 説明 |
|-----------|------|
| id | 連番 |
| question | 質問本文 |
| answer | 回答本文 |
| category | カテゴリ（大分類） |
| tags | タグ（複数OK） |
| date | 投稿日 |

## ロードマップ

### Phase 0: 調査・準備
- [ ] DiscordChatExporterでチャンネルをJSONエクスポート

### Phase 1: データ取得・構造化
- [ ] JSONからQ&Aペアに構造化
- [ ] カテゴリ・タグ分類
- [ ] スプレッドシート + JSON に保存

### Phase 2: 検索・参照アプリ（人間用）
- [ ] GAS WebApp で検索UI作成

### Phase 3: AIナレッジ化（Bot用）
- [ ] RAG用データ整備
- [ ] チャットボット組み込み

## データ保存先
- `raw/` - DiscordChatExporterの生データ（JSONをここに置く）
- `structured/` - 構造化済みデータ
