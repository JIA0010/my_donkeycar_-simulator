# 📚 Donkey Car Simulator ドキュメント索引

**プロジェクト**: Donkey Car v5.0.0 シミュレーター学習環境  
**最終更新**: 2026年1月2日

PC上で Unity シミュレーターを使って自動運転AIを学習するプロジェクトのドキュメント索引です。目的や習熟度に合わせて参照してください。

---

## 🎯 はじめての方へ（5～30分で開始）

### ⚡ 最初に読むべき順序

| 順序 | ドキュメント | 所要時間 | 概要 |
| :---: | --- | :---: | --- |
| **1** | [QUICKSTART.md](QUICKSTART.md) | 5分 | 🚀 5ステップで自動運転テストまで実行 |
| **2** | [ABOUT_PROJECT.md](ABOUT_PROJECT.md) | 10分 | 🤖 プロジェクト全体の仕組みを理解 |
| **3** | [SETUP_DETAILS.md](SETUP_DETAILS.md) | 5分 | ✅ 環境セットアップ状況の確認 |
| **4** | [ABOUT_LIBRARY.md](ABOUT_LIBRARY.md) | 10分 | 📚 Donkey Car v5.0.0 について |

**推奨**: 忙しい方は **QUICKSTART.md** だけでも実行可能です！

---

## 🛠️ トラブル時（エラーが出たら）

| 緊急度 | ドキュメント | 対応 |
| --- | --- | --- |
| 🔥 **高** | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | よくあるエラーの即座の解決方法 |
| ⚠️ **中** | [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) | 技術的詳細・根本原因分析・バージョン互換性 |

**困ったら**: QUICK_REFERENCE.md → TECHNICAL_ISSUES.md の順で確認

---

## 🚀 スキルアップ・カスタマイズ

| 項目 | ドキュメント | 対象 | 内容 |
| --- | --- | :---: | --- |
| **コース作成** | [CUSTOM_COURSE.md](CUSTOM_COURSE.md) | 全員 | 環境切り替え・Unityでカスタムコース作成 |

---

## 📁 ディレクトリ構造

```
my_donkeycar_-simulator/
├── docs/                     # 📖 このドキュメント群
│   ├── INDEX.md              # ← あなたはここです
│   ├── QUICKSTART.md         # 5分クイックスタート
│   ├── ABOUT_PROJECT.md      # プロジェクト概要
│   ├── ABOUT_LIBRARY.md      # Donkey Car ライブラリ解説
│   ├── SETUP_DETAILS.md      # セットアップ確認
│   ├── QUICK_REFERENCE.md    # エラー解決集
│   ├── TECHNICAL_ISSUES.md   # 技術詳細＆トラブルシューティング
│   ├── CUSTOM_COURSE.md      # コース作成ガイド
│   └── unity_custom_course/  # Unityカスタムコース資料
│
├── scripts/                  # 🔧 実行用シェルスクリプト
│   ├── start_drive.sh        # 手動操縦を開始
│   ├── train_model.sh        # モデル学習を実行
│   ├── start_autopilot.sh    # 自動運転を実行
│   ├── switch_environment.sh # シミュレーター環境を切り替え
│   └── check_system.sh       # システム・バージョン確認
│
├── mycar/                    # 🚗 Donkey Car 実装本体
│   ├── manage.py             # ドライブ・学習・テスト実行
│   ├── config.py             # Donkey Car デフォルト設定
│   ├── myconfig.py           # 🔧 カスタム設定（編集用）
│   ├── train.py              # 学習スクリプト
│   ├── calibrate.py          # キャリブレーション
│   ├── data/                 # 📊 記録したトレーニングデータ
│   ├── logs/                 # 📈 学習ログ
│   └── models/               # 🤖 学習済みモデル格納先
│
├── env/                      # 🐍 Python 仮想環境
│   ├── bin/                  # python, pip, donkey コマンド等
│   └── lib/python3.11/site-packages/  # インストール済みパッケージ
│
├── unity_custom_course/      # 🎮 Unityカスタムコース（高度な活用）
│   ├── QUICKSTART.md
│   ├── setup_unity_project.md
│   ├── BUILD_AND_TEST.md
│   └── scripts/
│
├── requirements.txt          # 依存ライブラリリスト
└── README.md                 # プロジェクト README
```

---

## ⚙️ 環境情報

| 項目 | 値 |
| --- | --- |
| **Donkey Car** | v5.0.0 |
| **Python** | 3.11 |
| **TensorFlow** | 2.15 |
| **OS** | macOS (Apple Silicon 対応) |

---

## 💡 活用のアドバイス

### 🚀 今すぐ始めたい方
1. [QUICKSTART.md](QUICKSTART.md) で5ステップを実行
2. 手動運転 → 学習 → 自動運転テスト完了！

### ⚠️ エラーが出た方
1. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) で同じエラーを探す
2. コマンドをコピペして実行
3. 解決しなければ [TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md) で詳細を確認

### 🎯 性能を上げたい方
1. [CUSTOM_COURSE.md](CUSTOM_COURSE.md) で環境を変更
2. 複数環境で実験してスキルアップ

---

## 🔗 関連リソース

- **Donkey Car 公式ドキュメント**: https://docs.donkeycar.com/
- **GitHub**: https://github.com/autorope/donkeycar
- **Gym Donkey Car**: https://github.com/tawnkramer/gym-donkeycar

---

> **最終更新**: 2026年2月2日  
> **対応バージョン**: Donkey Car v5.0.0 / Python 3.11  
> **環境**: macOS (Apple Silicon)