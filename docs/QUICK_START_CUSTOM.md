# 🎯 カスタムコース・性能向上クイックガイド

## 📋 概要

このガイドでは、Donkey Carシミュレーターで**赤い壁と黒い道のシンプルなコース**を作成し、性能を向上させる方法を説明します。

## 🚀 クイックスタート

### 1️⃣ 環境の選択・切り替え

現在、4つのビルトイン環境が利用可能です:

```bash
# 簡単な方法: 切り替えスクリプトを使用
./switch_environment.sh
```

**利用可能な環境:**
- 🏭 **倉庫** (`donkey-warehouse-v0`) - シンプル、初心者向け ✅ **推奨**
- 🛣️ **道路** (`donkey-generated-roads-v0`) - 中級
- 🏁 **トラック** (`donkey-generated-track-v0`) - 上級
- 🎪 **AVCコース** (`donkey-avc-sparkfun-v0`) - 実際のコースに近い

### 2️⃣ データ収集（最重要！）

```bash
# シミュレーターを起動
./start_drive.sh

# またはブラウザで http://localhost:8887 にアクセス
```

**運転のコツ:**
- 🎯 トラックの中央を維持
- 🐌 ゆっくり滑らかに運転
- 🔄 同じラインを繰り返し走る
- 📊 最低2000-3000フレーム収集（3-5周）
- ❌ 急ハンドル、壁への衝突を避ける

### 3️⃣ モデルのトレーニング

```bash
# トレーニング実行
./train_model.sh

# または手動で
cd mycar
python train.py --tub ./data --model ./models/mypilot.h5
```

### 4️⃣ オートパイロットテスト

```bash
# オートパイロットで走行
./start_autopilot.sh

# ブラウザで http://localhost:8887 にアクセス
# "Local Pilot" モードに切り替え
```

## 🛠️ カスタムコース作成

### 方法1: 既存環境を使用（推奨）

最も簡単な方法は、既存の倉庫環境を使用することです。シンプルで制御しやすいです。

```bash
# mycar/myconfig.py を編集
DONKEY_GYM_ENV_NAME = "donkey-warehouse-v0"
```

### 方法2: Unityでカスタムコース作成

赤い壁と黒い道の完全カスタムコースを作成したい場合:

詳細は → **[CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md)** を参照

**必要なもの:**
- Unity Hub + Unity 2020.3 LTS以降
- Donkey Simulator ソースコード
- 基本的なUnityの知識

**手順の概要:**
1. Donkey Simulator ソースを clone
2. Unityでプロジェクトを開く
3. カスタムシーンを作成
4. 黒い道（Plane + 黒マテリアル）
5. 赤い壁（Cube + 赤マテリアル）
6. ビルドして使用

## 📈 性能向上のヒント

### 現在の最適化済み設定

```python
# mycar/myconfig.py
MAX_EPOCHS = 150              # より長く学習
EARLY_STOP_PATIENCE = 10      # より多くの改善機会
BATCH_SIZE = 128              # バッチサイズ
LEARNING_RATE = 0.001         # 学習率
```

### トラブルシューティング

| 問題 | 解決策 |
|------|--------|
| 壁にぶつかる | より多くのデータ収集、`AI_THROTTLE_MULT = 0.6` |
| カーブで外れる | カーブのデータを増やす、`LEARNING_RATE = 0.0005` |
| ジグザグ運転 | より滑らかなデータ、`BATCH_SIZE = 256` |
| 損失が下がらない | `LEARNING_RATE = 0.0001`、オプティマイザー変更 |

詳細は → **[PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)** を参照

## 📚 主要なドキュメント

| ファイル | 内容 |
|----------|------|
| **[CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md)** | カスタムコース作成の詳細手順 |
| **[PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)** | 性能向上の具体的なテクニック |
| **[SIMULATOR_GUIDE.md](SIMULATOR_GUIDE.md)** | シミュレーター使用方法 |
| **[GETTING_STARTED.md](GETTING_STARTED.md)** | 基本的な使い方 |

## 🎯 成功の指標

- ✅ 3周以上連続で完走
- ✅ 壁にぶつからない
- ✅ スムーズなライン取り
- ✅ 一貫したスピード

## 🔧 便利なスクリプト

```bash
./switch_environment.sh   # 環境切り替え
./start_drive.sh          # 手動運転開始
./start_autopilot.sh      # オートパイロット開始
./train_model.sh          # モデルトレーニング
./check_system.sh         # システムチェック
```

## 💡 重要なポイント

1. **データの質 > データの量**
   - 滑らかで一貫した運転データが最も重要
   
2. **段階的に改善**
   - まず簡単な環境（倉庫）で練習
   - 徐々に複雑な環境に移行
   
3. **反復的なプロセス**
   - データ収集 → トレーニング → テスト → 改善
   
4. **パラメータ調整**
   - 一度に1つのパラメータだけ変更
   - 変更の影響を確認してから次へ

## 🆘 サポート

問題が発生した場合:

1. **[TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md)** - 既知の問題と解決策
2. **[LESSONS_LEARNED.md](LESSONS_LEARNED.md)** - 学んだ教訓
3. システムチェック: `./check_system.sh`

## 📊 現在のプロジェクト状態

```bash
# データ数を確認
ls mycar/data/images/ | wc -l

# モデルを確認
ls -lh mycar/models/

# システムステータス
./check_system.sh
```

## 🎓 次のステップ

1. 倉庫環境でデータ収集（3-5周）
2. モデルをトレーニング
3. オートパイロットでテスト
4. 性能を評価
5. 必要に応じてデータ追加
6. より複雑な環境に挑戦

---

**Happy Racing! 🏎️💨**

質問があれば、各ドキュメントを参照するか、Donkey Car公式ドキュメントをチェックしてください。
