# 🤖 このプロジェクトについて

## 概要

**Donkey Car シミュレーター学習環境** です。

PC上で **Unity シミュレーター** を使って自動運転AIを学習するプロジェクトです。

---

## 何をするプロジェクト？

### 目的
自動運転車（自動操舵・速度制御）を **自分で学習させる** こと

### 流れ

```
1️⃣ 手動運転でコースを走行 → データ（画像+操作）を記録
2️⃣ そのデータをAIに学習させる → 学習済みモデル(.h5)を作成
3️⃣ そのモデルで自動運転テスト
```

---

## Donkey Car v5.0.0 は必須？

**はい。このプロジェクトはDonkey Car v5.0.0専用です。**
理由：Donkey Car v5.0.0がGym環境完全登録であり、このプロジェクトはGym環境で動かすものだから

### なぜ v5.0.0？

```
✅ Python 3.11 完全対応
✅ TensorFlow 2.15 完全対応  
✅ Gym 環境完全登録
✅ 最新の自動運転ライブラリ

❌ v4.x以下は古く、互換性エラー多発
❌ Python 3.12+は未サポート
```

---

## プロジェクト構成

```
my_donkeycar_-simulator/
│
├── 🚗 mycar/                    ← メインプロジェクト
│   ├── manage.py               # ドライブモード起動
│   ├── train.py                # 学習実行
│   ├── myconfig.py             # ✅ 設定ファイル（重要）
│   ├── data/                   # ✅ 走行データ保存先
│   │   ├── manifest.json
│   │   ├── images/             # 走行中の画像
│   │   └── catalog_*.catalog   # 操作記録
│   └── models/                 # ✅ 学習済みモデル保存先
│       ├── mypilot.h5          # Keras形式
│       └── mypilot.tflite      # 軽量版
│
├── 🐍 env/                      # ✅ Python仮想環境
│   ├── bin/python              # Python 3.11
│   ├── lib/python3.11/...      # パッケージ
│   └── ...
│
├── 📚 docs/                     # ドキュメント
│   ├── INDEX.md                # ナビゲーション
│   ├── QUICKSTART.md           # 5分で始める
│   ├── SETUP_DETAILS.md        # セットアップ確認
│   ├── QUICK_REFERENCE.md      # エラー即座解決
│   ├── CUSTOM_COURSE.md        # カスタムコース
│   └── TECHNICAL_ISSUES.md     # 技術詳細
│
├── 🛠️ scripts/                  # 実行スクリプト
│   ├── start_drive.sh          # 手動運転
│   ├── train_model.sh          # 学習
│   ├── start_autopilot.sh      # 自動運転
│   └── check_system.sh         # 診断
│
├── 🎮 unity_custom_course/      # Unityコース作成パッケージ
│   ├── QUICKSTART.md
│   ├── README.md
│   └── ...
│
└── 📖 README.md                 # ルートドキュメント
```

---

## 3ステップで実際に動かす

### ステップ1: セットアップ確認（5分）

```bash
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
source env/bin/activate
python -c "import donkeycar; print(donkeycar.__version__)"
# 出力: 5.0.0 ✅
```

👉 詳細: [docs/SETUP_DETAILS.md](docs/SETUP_DETAILS.md)

### ステップ2: シミュレーター + 手動走行（15分）

```bash
# シミュレーターアプリ起動
open /Applications/donkey_sim.app

# ドライブモード起動（新しいターミナル）
cd mycar
python manage.py drive

# ブラウザを開く
http://localhost:8887
```

👉 詳細: [docs/QUICKSTART.md](docs/QUICKSTART.md)

### ステップ3: 学習 → 自動運転（30分）

```bash
# 新しいターミナルで学習
cd mycar
donkey train --tub ./data --model ./models/mypilot.h5

# 学習完了後、ドライブモードで自動運転テスト
python manage.py drive --model ./models/mypilot.h5
# ブラウザで Mode を "Local Pilot" に変更
```

👉 詳細: [docs/QUICKSTART.md](docs/QUICKSTART.md)

---

## 何が特別？

### ✅ セットアップ済み
- Python仮想環境が完全に準備されている
- Donkey Car v5.0.0がインストール済み
- 必要な全パッケージが揃っている

### ✅ シミュレーター対応
- 実機なしでPC上だけで実験可能
- すぐにAIを学習させられる
- データ収集が簡単

### ✅ 学習環境最適化
- `MAX_EPOCHS = 150` で詳しい学習
- `EARLY_STOP_PATIENCE = 10` で効率的
- `LEARNING_RATE = 0.001` で安定学習

### ✅ ドキュメント完備
- シンプルなドキュメント（6個だけ）
- すぐに始められる
- 詳細な技術情報もある

---

## データの流れ（全体像）

```
🎮 シミュレーター起動
   ↓
👤 手動走行（ブラウザUIで操作）
   ↓
💾 走行データ自動保存（mycar/data/）
   ├── images/          ... 走行中の画像（160×120）
   └── catalog_*.catalog ... 操舵角・スロットル記録
   
   ↓

🤖 AIが学習開始
   ├── 入力: 画像（160×120）
   ├── 学習内容: 「この画像を見たら、こう操舵・スロットルする」
   └── 出力: モデル（mycar/models/mypilot.h5）
   
   ↓

✨ 自動運転テスト
   ├── モデルが画像を見ながら自動判断
   ├── 操舵角・スロットルを自動計算
   └── コースを走行
```

---

## 学習の仕組み（深掘り）

### 使用AI技術
- **フレームワーク**: TensorFlow 2.15 + Keras
- **ネットワーク**: Convolutional Neural Network (CNN)
- **学習方法**: 教師あり学習（Supervised Learning）

### データセット
```
必要データ数: 1,000～5,000枚の画像 (推奨)

各画像には:
- 画像（160×120 RGB）
- ステアリング角度（-1.0～1.0）
- スロットル値（-1.0～1.0）
```

### 学習パラメータ
```python
MAX_EPOCHS = 150           # 150回反復学習
BATCH_SIZE = 128           # 1度に128枚処理
LEARNING_RATE = 0.001      # 学習速度（小さい=安定）
EARLY_STOP_PATIENCE = 10   # 改善なければ10エポック後に停止
```

---

## 実際のディスク上の様子

### 手動走行後（mycar/data/）

```
data/
├── manifest.json           # メタデータ
├── catalog_0.catalog       # 第1回走行のデータ
├── catalog_1.catalog       # 第2回走行のデータ
└── images/
    ├── frame_000.jpg       # 画像1
    ├── frame_001.jpg       # 画像2
    └── ...（数千枚）
```

### 学習後（mycar/models/）

```
models/
├── mypilot.h5             # 学習済みモデル（Keras）
├── mypilot.tflite         # 軽量版（エッジ向け）
└── database.json          # メタデータ
```

---

## トラブルシューティング

### よくある質問

**Q: 「Donkey Car v5.0.0じゃないとダメ？」**

A: はい。このプロジェクトはv5.0.0専用です。古いバージョンは互換性エラーが多発します。
→ [詳細](docs/QUICK_REFERENCE.md)

**Q: 「シミュレーターの接続できない」**

A: よくあるエラー。以下の手順を確認してください：
1. シミュレーターアプリが起動しているか
2. ブラウザで `http://localhost:8887` にアクセスできるか
3. `mycar/myconfig.py` の `DONKEY_GYM = True` を確認
→ [詳細](docs/QUICK_REFERENCE.md)

**Q: 「学習が進まない」**

A: データ品質が重要です：
1. 最低1,000枚の画像を集める
2. スムーズに走行する（急ハンドル禁止）
3. 複数周走行する（データを増やす）
→ [詳細](docs/CUSTOM_COURSE.md)

---

## 次のステップ

### 初心者向け
👉 [docs/QUICKSTART.md](docs/QUICKSTART.md) - 5分で始める

### セットアップを理解したい
👉 [docs/SETUP_DETAILS.md](docs/SETUP_DETAILS.md) - セットアップ確認

### エラーが出た
👉 [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) - エラー即座解決

### 性能を上げたい
👉 [docs/CUSTOM_COURSE.md](docs/CUSTOM_COURSE.md) - カスタムコース・最適化

### 技術的に理解したい
👉 [docs/TECHNICAL_ISSUES.md](docs/TECHNICAL_ISSUES.md) - 詳細な技術説明

---

## 必要なもの

| 項目 | 用意されている？ | 詳細 |
|------|--------|--------|
| Python 3.11 | ✅ (`env/` に）| 仮想環境で独立 |
| Donkey Car v5.0.0 | ✅ | インストール済み |
| TensorFlow 2.15 | ✅ | 学習用 |
| Gym 環境 | ✅ | シミュレーター用 |
| Unityシミュレーター | ❌ | 別途ダウンロード必要 |
| 走行データ | ❌ | 自分で収集する |

---

## ライセンスと情報

- **Donkey Car**: オープンソース（MIT License）
- **TensorFlow**: オープンソース（Apache 2.0）
- **このプロジェクト**: 学習用のセットアップ済み環境

---

**楽しい自動運転ライフを！🚗💨**
