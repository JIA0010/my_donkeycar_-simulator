# 📚 ドキュメント索引

Donkey Carシミュレーター環境の全ドキュメント一覧です。目的に応じて適切なドキュメントを参照してください。

---

## 🚀 初めての方向け

### 1. [README.md](README.md)
**目的**: プロジェクト全体の概要とセットアップ手順

**こんな時に読む**:
- 最初に何をすべきか知りたい
- プロジェクトの全体像を把握したい
- 基本的なセットアップ方法を知りたい

**所要時間**: 10分

---

### 2. [GETTING_STARTED.md](GETTING_STARTED.md)
**目的**: すぐに始めるためのクイックスタートガイド

**こんな時に読む**:
- セットアップが完了して、すぐに使い始めたい
- ブラウザでの操作方法を知りたい
- データ収集から自動運転までの流れを知りたい

**所要時間**: 5分

---

### 3. [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md)
**目的**: シミュレーターアプリの起動方法の詳細

**こんな時に読む**:
- シミュレーターのダウンロード先を知りたい
- 起動時の設定画面の操作方法を知りたい
- 「Play!」ボタンが見つからない時

**所要時間**: 7分

---

## 🎯 カスタムコース・性能向上 ⭐ NEW!

### 4. [QUICK_START_CUSTOM.md](QUICK_START_CUSTOM.md) ⭐ **推奨**
**目的**: カスタムコース作成と性能向上のクイックスタート

**こんな時に読む**:
- 赤い壁と黒い道のシンプルなコースを作りたい
- 既存の環境を切り替えたい
- AIの性能を上げたい
- データ収集のコツを知りたい

**所要時間**: 10分

**内容**:
- 4つのビルトイン環境の切り替え方法
- データ収集のベストプラクティス
- 性能向上の具体的なステップ
- トラブルシューティング

---

### 5. [CUSTOM_COURSE_COMPLETE.md](CUSTOM_COURSE_COMPLETE.md) 🆕 **完全版**
**目的**: Unityで赤い壁と黒い道のカスタムコースを実際に作成

**こんな時に読む**:
- 実際のコース環境を完全に再現したい
- Unityでカスタムシミュレーターを作りたい
- 30分でカスタムコースを完成させたい
- 完全な制御が必要

**所要時間**: 5分（概要）、30-60分（実装）

**内容**:
- 完全なカスタムコース作成パッケージ
- Unity C#スクリプト（自動トラック生成）
- マテリアル設定（黒い道、赤い壁）
- ビルドとテスト手順

**サブドキュメント**:
- 📖 `unity_custom_course/QUICKSTART.md` - 30分で完成
- 📖 `unity_custom_course/setup_unity_project.md` - 詳細セットアップ
- 📖 `unity_custom_course/BUILD_AND_TEST.md` - ビルドガイド

---

### 6. [CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md)
**目的**: カスタムコース作成の詳細ガイド

**こんな時に読む**:
- Unityで完全カスタムコースを作りたい
- 赤い壁と黒い道の実際のコース環境を作りたい
- シミュレーターのソースコードを触りたい

**所要時間**: 60分（実装含む）

**内容**:
- Unity環境のセットアップ
- カスタムシーンの作成手順
- マテリアル設定（黒い道、赤い壁）
- ビルドと使用方法

---

### 6. [CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md)
**目的**: カスタムコース作成の理論的ガイド（旧版）

**こんな時に読む**:
- カスタムコース作成の概要を知りたい
- 方法論を理解したい

**所要時間**: 20分

**注**: より実践的な方法は `CUSTOM_COURSE_COMPLETE.md` を参照してください

---

### 7. [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)
**目的**: AIモデルの性能を最大化する

**こんな時に読む**:
- モデルの精度を上げたい
- データ収集のテクニックを学びたい
- トレーニングパラメータを最適化したい
- うまく走らない原因を知りたい

**所要時間**: 20分

**内容**:
- 高品質データ収集のコツ
- トレーニング設定の最適化
- モデルアーキテクチャの選択
- データ拡張テクニック
- トラブルシューティング

---

## 🔧 トラブルシューティング

### 7. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) ⭐ **最優先**
**目的**: よくあるエラーと即座の解決方法

**こんな時に読む**:
- エラーが出てすぐに解決したい
- よくある問題の解決策を知りたい
- 診断コマンドを実行したい

**所要時間**: 問題解決まで1-5分

**対応エラー**:
- `ModuleNotFoundError: No module named 'pkg_resources'`
- `AttributeError: module 'collections' has no attribute 'MutableMapping'`
- `gym.error.NameNotFound: Environment doesn't exist`
- `SyntaxError: unterminated string literal`
- その他10種類以上のエラー

---

### 5. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md)
**目的**: 技術的問題の詳細な解説と根本原因

**こんな時に読む**:
- エラーの根本原因を理解したい
- なぜその解決策が有効なのか知りたい
- 同じ問題を再発させたくない
- 技術的に深く理解したい

**所要時間**: 30-45分（全部読む場合）

**内容**:
- 10個の主要な技術的問題
- 各問題の原因、解決方法、予防策
- バージョン互換性の詳細
- トラブルシューティングフローチャート

---

## 🧹 環境管理

### 6. [CLEANUP_GUIDE.md](CLEANUP_GUIDE.md)
**目的**: システムを綺麗に保つためのガイド

**こんな時に読む**:
- システムPythonが汚染された
- 仮想環境の使い方を学びたい
- pipの正しい使い方を知りたい
- ベストプラクティスを知りたい

**所要時間**: 15分

---

### 7. [CLEANUP_REPORT.md](CLEANUP_REPORT.md)
**目的**: 実施したクリーンアップの記録

**こんな時に読む**:
- 何がクリーンアップされたか確認したい
- 現在の環境状態を知りたい
- クリーンアップの手順を参考にしたい

**所要時間**: 10分

---

### 8. [check_system.sh](check_system.sh)
**目的**: システム状態を自動チェックするスクリプト

**こんな時に使う**:
- 環境が正しくセットアップされているか確認
- 問題がないか診断したい
- 次に何をすべきか知りたい

**使い方**:
```bash
./check_system.sh
```

---

## 🎓 学習・改善

### 9. [LESSONS_LEARNED.md](LESSONS_LEARNED.md)
**目的**: プロジェクトから得られた教訓と改善提案

**こんな時に読む**:
- 同じミスを避けたい
- プロジェクトを改善したい
- ベストプラクティスを学びたい
- 他のプロジェクトに応用したい

**所要時間**: 20-30分

**内容**:
- 技術的教訓（5項目）
- 改善提案（Docker化、テスト、CI/CD等）
- 再発防止策
- 今後の展望

---

## 🛠️ 実行スクリプト

### 10. [start_drive.sh](start_drive.sh)
**目的**: 手動運転モードを起動

**使い方**:
```bash
./start_drive.sh
```

---

### 11. [train_model.sh](train_model.sh)
**目的**: AIモデルの学習を実行

**使い方**:
```bash
./train_model.sh
```

---

### 12. [start_autopilot.sh](start_autopilot.sh)
**目的**: 自動運転モードを起動

**使い方**:
```bash
./start_autopilot.sh
```

---

## 📋 その他のファイル

### 13. [requirements.txt](requirements.txt)
**目的**: Python依存パッケージのリスト

**使い方**:
```bash
./env/bin/pip install -r requirements.txt
```

---

### 14. [.gitignore](.gitignore)
**目的**: Gitで無視するファイルの指定

---

### 15. mycar/myconfig.py
**目的**: Donkey Carの設定ファイル

**重要な設定**:
- `DONKEY_GYM = True` - シミュレーターモード
- `DONKEY_GYM_ENV_NAME` - コース選択
- `SIM_HOST` - 接続先

---

## 🗺️ ドキュメントマップ

```
初めての利用
    ↓
README.md (概要とセットアップ)
    ↓
SIMULATOR_GUIDE.md (シミュレーター起動)
    ↓
GETTING_STARTED.md (使い方)
    ↓
実行スクリプト (start_drive.sh等)

    ↓ (エラー発生時)
    
QUICK_REFERENCE.md (即座の解決)
    ↓ (詳細を知りたい)
TECHNICAL_ISSUES.md (詳細な解説)

    ↓ (環境管理)
    
CLEANUP_GUIDE.md (クリーンアップ方法)
check_system.sh (自動診断)

    ↓ (さらなる改善)
    
LESSONS_LEARNED.md (教訓と改善提案)
```

---

## 📊 ドキュメント比較表

| ドキュメント | 難易度 | 所要時間 | 優先度 | 対象者 |
|------------|--------|---------|--------|--------|
| README.md | ★☆☆ | 10分 | 高 | 全員 |
| GETTING_STARTED.md | ★☆☆ | 5分 | 高 | 初心者 |
| SIMULATOR_GUIDE.md | ★☆☆ | 7分 | 中 | 初心者 |
| QUICK_REFERENCE.md | ★★☆ | 5分 | 最高 | トラブル時 |
| TECHNICAL_ISSUES.md | ★★★ | 45分 | 中 | 技術者 |
| CLEANUP_GUIDE.md | ★★☆ | 15分 | 中 | 全員 |
| CLEANUP_REPORT.md | ★☆☆ | 10分 | 低 | 参考 |
| LESSONS_LEARNED.md | ★★★ | 30分 | 中 | 改善者 |
| check_system.sh | ★☆☆ | 1分 | 高 | 全員 |

**難易度**: ★☆☆（簡単） ～ ★★★（難しい）

---

## 🎯 シチュエーション別ガイド

### シチュエーション1: 完全に初めての人
1. [README.md](README.md) - 全体像を把握
2. [SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md) - シミュレーターダウンロード
3. [GETTING_STARTED.md](GETTING_STARTED.md) - 実際に使ってみる

### シチュエーション2: エラーが出た
1. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - 即座の解決
2. `./check_system.sh` - 自動診断
3. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) - 詳細確認（必要なら）

### シチュエーション3: 環境が汚れた
1. [CLEANUP_GUIDE.md](CLEANUP_GUIDE.md) - クリーンアップ方法
2. `./check_system.sh` - 状態確認
3. [CLEANUP_REPORT.md](CLEANUP_REPORT.md) - 参考

### シチュエーション4: プロジェクトを改善したい
1. [LESSONS_LEARNED.md](LESSONS_LEARNED.md) - 教訓を学ぶ
2. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) - 問題を理解
3. 改善を実施

### シチュエーション5: 他のプロジェクトに応用したい
1. [LESSONS_LEARNED.md](LESSONS_LEARNED.md) - ベストプラクティス
2. [CLEANUP_GUIDE.md](CLEANUP_GUIDE.md) - 環境管理手法
3. [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) - 技術的知見

---

## 🔍 キーワード検索

### エラー関連
- **pkg_resources** → QUICK_REFERENCE.md, TECHNICAL_ISSUES.md
- **collections.MutableMapping** → QUICK_REFERENCE.md, TECHNICAL_ISSUES.md
- **SyntaxError** → QUICK_REFERENCE.md, TECHNICAL_ISSUES.md
- **ModuleNotFoundError** → QUICK_REFERENCE.md, TECHNICAL_ISSUES.md

### 環境管理
- **仮想環境** → CLEANUP_GUIDE.md, LESSONS_LEARNED.md
- **pip install** → CLEANUP_GUIDE.md, README.md
- **システム汚染** → CLEANUP_GUIDE.md, CLEANUP_REPORT.md

### セットアップ
- **シミュレーター** → SIMULATOR_GUIDE.md, README.md
- **データ収集** → GETTING_STARTED.md
- **学習** → GETTING_STARTED.md, README.md
- **自動運転** → GETTING_STARTED.md

### 改善
- **Docker** → LESSONS_LEARNED.md
- **テスト** → LESSONS_LEARNED.md
- **CI/CD** → LESSONS_LEARNED.md

---

## 💾 ドキュメントのダウンロード

すべてのドキュメントは `/Users/yoshimurahiro/mysim/` ディレクトリにあります。

```bash
# プロジェクトディレクトリに移動
cd /Users/yoshimurahiro/mysim

# すべてのドキュメントをリスト表示
ls *.md

# 特定のドキュメントを読む
cat README.md
less TECHNICAL_ISSUES.md
```

---

## 📱 印刷推奨ドキュメント

以下のドキュメントは印刷して手元に置いておくと便利です：

1. **QUICK_REFERENCE.md** - エラー発生時の即座の参照
2. **check_system.sh の出力** - 現在の環境状態の記録

```bash
# 印刷用にPDF化（Markdownビューワーから）
# または、ターミナルから
./check_system.sh > system_status.txt
```

---

## 🔄 ドキュメントの更新

このドキュメント群は生きたドキュメントです。新しい問題や改善が見つかり次第、更新してください。

**更新ルール**:
1. 新しいエラーを発見 → QUICK_REFERENCE.md と TECHNICAL_ISSUES.md に追加
2. 環境を変更 → CLEANUP_REPORT.md を更新
3. 改善を実施 → LESSONS_LEARNED.md に記録
4. 使い方が変更 → README.md や GETTING_STARTED.md を更新

---

## 📞 サポート

### ドキュメントで解決しない場合

1. すべての関連ドキュメントを確認済みか？
2. `./check_system.sh` を実行したか？
3. エラーメッセージ全体をコピーしたか？

**それでも解決しない場合**:
- Donkey Car公式フォーラム: [discord.gg/donkeycar](https://discord.gg/donkeycar)
- GitHub Issues: 各パッケージのリポジトリ

---

**📅 最終更新**: 2026年1月1日  
**📝 維持管理**: プロジェクト実施者

**このドキュメント索引を起点に、適切なドキュメントを見つけてください！**
