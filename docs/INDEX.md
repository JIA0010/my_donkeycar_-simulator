# 📚 ドキュメント索引

Donkey Carシミュレーター環境の全ドキュメント一覧です。目的に応じて適切なドキュメントを参照してください。

---

## 🚀 初めての方向け

### 1. [README.md](../README.md)
**目的**: プロジェクト全体の概要とセットアップ手順

**こんな時に読む**:
- 最初に何をすべきか知りたい
- プロジェクトの全体像を把握したい

**所要時間**: 10分

---

### 2. [GETTING_STARTED.md](GETTING_STARTED.md)
**目的**: クイックスタートガイド

**こんな時に読む**:
- セットアップが完了してすぐに使い始めたい
- データ収集から自動運転までの流れを知りたい

**所要時間**: 5分

---

### 3. [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md)
**目的**: シミュレーターアプリの起動方法

**こんな時に読む**:
- シミュレーターのダウンロード先を知りたい
- 起動時の設定方法を知りたい

**所要時間**: 7分

---

## 🎯 カスタムコース・性能向上 ⭐ NEW!

### 4. [CUSTOM_COURSE.md](CUSTOM_COURSE.md) ⭐ **推奨**
**目的**: カスタムコース作成と性能向上の完全ガイド

**こんな時に読む**:
- 赤い壁と黒い道のコースを作りたい
- 環境を切り替えたい
- AIの性能を上げたい
- 3つの方法を比較したい

**所要時間**: 10分

**内容**:
- ✅ 方法1: 既存環境を使用（最速・推奨）
- ✅ 方法2: Unityでカスタムコース作成（30分）
- ✅ 方法3: 性能向上に集中（最も効果的）

---

### 5. [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)
**目的**: AIモデルの性能を最大化

**こんな時に読む**:
- モデルの精度を上げたい
- データ収集のテクニックを学びたい
- トレーニング設定を最適化したい

**所要時間**: 20分

**内容**:
- 高品質データ収集のコツ
- トレーニング設定の最適化
- 性能向上チェックリスト

---

## 🔧 トラブルシューティング

### 6. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) ⭐ **最優先**
**目的**: よくあるエラーと即座の解決方法

**こんな時に読む**:
- エラーが出てすぐに解決したい
- よくある問題の解決策を知りたい

**所要時間**: 1-5分

---

### 7. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md)
**目的**: 技術的問題の詳細な解説と根本原因

**こんな時に読む**:
- エラーの根本原因を理解したい
- 同じ問題を再発させたくない
- 技術的に深く理解したい

**所要時間**: 30-45分

---

## 🧹 環境管理

### 8. [CLEANUP_GUIDE.md](CLEANUP_GUIDE.md)
**目的**: システムを綺麗に保つためのガイド

**こんな時に読む**:
- 仮想環境の使い方を学びたい
- ベストプラクティスを知りたい
- システムをリセットしたい

**所要時間**: 15分

---

## 📖 参考資料

### 9. [REFERENCES.md](REFERENCES.md)
**目的**: 実装レポートと参考資料

**こんな時に読む**:
- 実装内容を確認したい
- 技術的背景を知りたい
- クリーンアップの詳細を確認したい

**所要時間**: 10-20分

---

## 🎓 学習・改善

### 10. [LESSONS_LEARNED.md](LESSONS_LEARNED.md)
**目的**: プロジェクトから得られた教訓

**こんな時に読む**:
- 同じミスを避けたい
- プロジェクトを改善したい
- ベストプラクティスを学びたい

**所要時間**: 20-30分

---

## 🔗 実行スクリプト

実行スクリプトは `scripts/` ディレクトリにあります：

- **`scripts/start_drive.sh`** - 手動運転モード起動
- **`scripts/train_model.sh`** - AIモデル学習
- **`scripts/start_autopilot.sh`** - 自動運転モード起動
- **`scripts/switch_environment.sh`** - 環境切り替え
- **`scripts/check_system.sh`** - システム状態確認

---

## 🗺️ シチュエーション別ガイド

### シナリオ1: 完全に初めての人
1. [README.md](../README.md) - 全体像を把握
2. [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md) - シミュレーターダウンロード
3. [GETTING_STARTED.md](GETTING_STARTED.md) - 実際に使う

**所要時間**: 25分

### シナリオ2: エラーが出た
1. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - 即座の解決
2. `./scripts/check_system.sh` - 自動診断
3. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) - 詳細確認

**所要時間**: 5-15分

### シナリオ3: 性能を上げたい
1. [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - 3つの方法を確認
2. [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) - テクニックを学ぶ
3. 実装・反復

**所要時間**: 30分+実装

### シナリオ4: Unityでカスタムコース作成
1. [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - 方法2を確認
2. [unity_custom_course/QUICKSTART.md](../unity_custom_course/QUICKSTART.md) - 30分で完成

**所要時間**: 30-60分

---

## 📊 ドキュメント比較表

| ドキュメント | 難易度 | 所要時間 | 優先度 | タイプ |
|------------|--------|---------|--------|--------|
| README.md | ★☆☆ | 10分 | 高 | 入門 |
| GETTING_STARTED.md | ★☆☆ | 5分 | 高 | 入門 |
| SIMULATOR_GUIDE.md | ★☆☆ | 7分 | 中 | 入門 |
| QUICK_REFERENCE.md | ★★☆ | 5分 | 最高 | 参考 |
| TECHNICAL_ISSUES.md | ★★★ | 45分 | 高 | 詳細 |
| CLEANUP_GUIDE.md | ★★☆ | 15分 | 中 | 管理 |
| CUSTOM_COURSE.md | ★★☆ | 10分 | 高 | 拡張 |
| PERFORMANCE_GUIDE.md | ★★☆ | 20分 | 中 | 拡張 |
| LESSONS_LEARNED.md | ★★★ | 30分 | 中 | 学習 |
| REFERENCES.md | ★★☆ | 20分 | 低 | 参考 |

**難易度**: ★☆☆（簡単） ～ ★★★（難しい）

---

## 🎯 クイックアクセス

### よくやることベスト5

1. **すぐにやってみたい**
   ```bash
   ./scripts/start_drive.sh
   ```
   参照: [GETTING_STARTED.md](GETTING_STARTED.md)

2. **モデルを訓練したい**
   ```bash
   ./scripts/train_model.sh
   ```
   参照: [CUSTOM_COURSE.md](CUSTOM_COURSE.md)

3. **自動走行をテストしたい**
   ```bash
   ./scripts/start_autopilot.sh
   ```
   参照: [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - 方法3

4. **環境を変更したい**
   ```bash
   ./scripts/switch_environment.sh
   ```
   参照: [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - 方法1

5. **Unityでコース作成したい**
   参照: [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - 方法2 → [unity_custom_course/QUICKSTART.md](../unity_custom_course/QUICKSTART.md)

---

## 🔍 キーワード検索

### 実行方法
- **データ収集** → GETTING_STARTED.md, CUSTOM_COURSE.md
- **AIの訓練** → CUSTOM_COURSE.md, PERFORMANCE_GUIDE.md
- **自動運転テスト** → CUSTOM_COURSE.md
- **環境切り替え** → CUSTOM_COURSE.md

### 環境管理
- **仮想環境** → CLEANUP_GUIDE.md, LESSONS_LEARNED.md
- **pip install** → CLEANUP_GUIDE.md, README.md
- **システム状態確認** → scripts/check_system.sh

### トラブル
- **エラーが出た** → QUICK_REFERENCE.md → TECHNICAL_ISSUES.md
- **実行できない** → TECHNICAL_ISSUES.md, CLEANUP_GUIDE.md

### 高度な使い方
- **性能最適化** → PERFORMANCE_GUIDE.md
- **カスタムコース** → CUSTOM_COURSE.md
- **Unity連携** → CUSTOM_COURSE.md - 方法2

---

## 📁 ディレクトリ構造

```
my_donkeycar_-simulator/
├── docs/                    ← このドキュメント群
│   ├── INDEX.md            # このファイル（ナビゲーション）
│   ├── README.md           # ルートREADME（別フォルダ）
│   ├── CUSTOM_COURSE.md    # カスタムコース完全ガイド ⭐
│   ├── PERFORMANCE_GUIDE.md # 性能向上テクニック
│   ├── QUICK_REFERENCE.md  # 緊急参考 ⭐
│   ├── TECHNICAL_ISSUES.md # 詳細な技術問題
│   ├── CLEANUP_GUIDE.md    # 環境管理
│   ├── LESSONS_LEARNED.md  # 教訓
│   ├── REFERENCES.md       # 参考資料
│   ├── GETTING_STARTED.md  # クイックスタート
│   └── SIMULATOR_GUIDE.md  # シミュレーター
├── scripts/                 # 実行スクリプト
│   ├── start_drive.sh       # 手動運転
│   ├── train_model.sh       # 訓練
│   ├── start_autopilot.sh   # 自動運転
│   ├── switch_environment.sh # 環境切り替え
│   └── check_system.sh      # 状態確認
├── mycar/                   # メイン実装
├── unity_custom_course/     # カスタムコースパッケージ
├── examples/                # サンプルコード
└── README.md               # ルートREADME
```

---

## 💡 使用のコツ

### ドキュメントの見つけ方

1. **目的で探す**: 上の「シチュエーション別ガイド」を使用
2. **キーワードで探す**: 「キーワード検索」セクション
3. **所要時間で探す**: 忙しい時は短いドキュメントを優先
4. **優先度で探す**: 「優先度: 高」から読む

### オフライン参照

印刷またはMarkdownビューワーで参照：

```bash
# すべてのドキュメントをダウンロード
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator/docs
ls *.md

# 特定のドキュメントを読む
cat QUICK_REFERENCE.md
```

---

## 🔄 更新ルール

このドキュメント群は生きたドキュメントです。更新時のルール：

1. **新しいエラー発見** → QUICK_REFERENCE.md と TECHNICAL_ISSUES.md に追加
2. **改善を実施** → LESSONS_LEARNED.md に記録
3. **使い方が変更** → 該当ドキュメントを更新
4. **このINDEX.md** → 新しいドキュメント追加時に更新

---

**📅 最終更新**: 2026年2月2日

**このドキュメント索引を起点に、あなたが必要なドキュメントを見つけてください！** 🚀
