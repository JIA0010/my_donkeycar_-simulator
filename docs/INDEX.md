# 📚 ドキュメント（ミニマル版）

## 🎯 3つのドキュメントだけ

| 何したい？ | ドキュメント |
|-----------|------------|
| **セットアップ確認** | [SETUP_DETAILS.md](SETUP_DETAILS.md) |
| **実際に走らせる** | [QUICKSTART.md](QUICKSTART.md) |
| **エラーを解決** | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |

---

## 詳しく知りたい場合

| タイプ | ドキュメント |
|--------|------------|
| カスタムコース・性能向上 | [CUSTOM_COURSE.md](CUSTOM_COURSE.md) |
| 技術的な詳細 | [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) |

---

� まずは [QUICKSTART.md](QUICKSTART.md) から始めよう！
- Donkey Car v5.0.0 インストール確認
- myconfig.py の設定
- mycar/data/ と mycar/models/ ディレクトリ管理

### 2️⃣ [GETTING_STARTED.md](GETTING_STARTED.md) - クイックスタート
- セットアップ後の最初のステップ
- 手動運転 → データ収集 → 学習 → 自動運転の流れ
- 基本的なトラブルシューティング

### 3️⃣ [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md) - シミュレーター操作マニュアル
- ブラウザUIの使い方
- 各操作モード（User / Local Angle / Local）
- キーボード操作
- データ記録の方法

### 4️⃣ [CUSTOM_COURSE.md](CUSTOM_COURSE.md) - カスタムコース作成
- 方法1: 既存環境を使用（推奨）
- 方法2: Unityでカスタムコース作成
- 利用可能な環境一覧
- パフォーマンス向上策

### 5️⃣ [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) - 性能向上ガイド
- データ品質の向上
- モデル学習の最適化
- トレーニングパラメータの調整
- デバッグとモニタリング

### 6️⃣ [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - エラーの即座の解決
- よくあるエラーと1行の解決方法
- 緊急度別に整理
- コマンドをコピペするだけで解決

### 7️⃣ [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) - 技術的な詳細解説
- エラーの深い原因分析
- バージョン互換性の詳細
- デバッグ方法
- 環境のリセット方法

---

## 🎯 あなたの状況に応じた読む順序

### ✅ セットアップを今からする
1. [README.md](../README.md)
2. [SETUP_DETAILS.md](SETUP_DETAILS.md)
3. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (エラーが出たら)

### ✅ セットアップは完了、さあ走らせる
1. [GETTING_STARTED.md](GETTING_STARTED.md)
2. [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md)

### ✅ パフォーマンスをもっと良くしたい
1. [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)
2. [CUSTOM_COURSE.md](CUSTOM_COURSE.md)

### ✅ エラーが出た
1. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) で即答を探す
2. 解決しなければ [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) で詳細を読む

---

## 📊 ドキュメント統計

- **総ファイル数**: 7個 (最小限)
- **総行数**: 約2,500行
- **総容量**: 約67KB (軽量)

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
