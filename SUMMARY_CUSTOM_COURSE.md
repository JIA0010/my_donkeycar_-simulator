# 🎯 カスタムコース作成・性能向上 まとめ

## 📝 質問への回答

**Q: 実際のコースの環境をシミュレートしたい。自分でコースを作れる？赤い壁があって、道は黒い。結構シンプル。ここでの成績を上げたい**

**A: はい、可能です！** 以下の3つの方法があります：

---

## ✅ 方法1: 既存環境を使用（最も簡単・推奨）

### 概要
Donkeyシミュレーターには4つのビルトイン環境があり、シンプルな環境もあります。

### 手順
1. **環境切り替えスクリプトを実行**
   ```bash
   ./switch_environment.sh
   ```

2. **利用可能な環境:**
   - 🏭 **倉庫** (`donkey-warehouse-v0`) - シンプル、制御しやすい ✅ **推奨**
   - 🛣️ **道路** (`donkey-generated-roads-v0`) - 中級
   - 🏁 **トラック** (`donkey-generated-track-v0`) - 上級
   - 🎪 **AVCコース** (`donkey-avc-sparkfun-v0`) - 実際のコース

3. **倉庫環境に既に切り替え済み**
   - `mycar/myconfig.py`で設定済み
   - シンプルで性能を上げやすい

### 詳細ドキュメント
📖 [QUICK_START_CUSTOM.md](QUICK_START_CUSTOM.md)

---

## ✅ 方法2: Unityで完全カスタムコース作成

### 概要
赤い壁と黒い道の完全カスタムコースを作成できます。

### 必要なもの
- Unity Hub + Unity 2020.3 LTS以降
- Donkey Simulator ソースコード
- 基本的なUnityの知識

### 手順概要
1. Donkey Simulatorのソースを取得
   ```bash
   git clone https://github.com/tawnkramer/sdsandbox
   ```

2. Unityでプロジェクトを開く

3. カスタムシーンを作成
   - **黒い道**: Plane + 黒マテリアル (RGB: 0, 0, 0)
   - **赤い壁**: Cube + 赤マテリアル (RGB: 255, 0, 0)
   - スケール・配置して道路を形成

4. ビルドして使用

### 詳細ドキュメント
📖 [CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md)

---

## ✅ 方法3: 性能向上に集中（推奨）

カスタムコースを作るよりも、**既存環境で性能を最大化**する方が効率的です。

### 性能を上げる具体的なステップ

#### 1️⃣ 高品質データ収集（最重要！）
```bash
./start_drive.sh
# ブラウザで http://localhost:8887 を開く
```

**運転のコツ:**
- 🎯 トラックの中央を維持
- 🐌 ゆっくり滑らかに運転
- 🔄 同じラインを繰り返す
- 📊 2000-3000フレーム以上収集
- ❌ 急ハンドル、壁への衝突を避ける

#### 2️⃣ 最適化済みトレーニング設定
すでに`mycar/myconfig.py`に設定済み:
```python
MAX_EPOCHS = 150              # より長く学習
EARLY_STOP_PATIENCE = 10      # より多くの改善機会
BATCH_SIZE = 128
LEARNING_RATE = 0.001
```

#### 3️⃣ トレーニング実行
```bash
./train_model.sh
```

#### 4️⃣ オートパイロットテスト
```bash
./start_autopilot.sh
# ブラウザで "Local Pilot" モードに切り替え
```

#### 5️⃣ 性能評価
- ✅ 3周以上連続で完走できる
- ✅ 壁にぶつからない
- ✅ スムーズなライン取り

### 詳細ドキュメント
📖 [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)

---

## 🎯 推奨アプローチ

### ステップ1: まず倉庫環境で基礎を固める
1. 倉庫環境（既に設定済み）でデータ収集
2. 滑らかで一貫した運転を習得
3. 2000フレーム以上のデータを収集

### ステップ2: モデルをトレーニング
```bash
./train_model.sh
```

### ステップ3: オートパイロットでテスト
```bash
./start_autopilot.sh
```

### ステップ4: 反復改善
- うまくいかない箇所でデータ追加
- パラメータ調整
- 再トレーニング

### ステップ5: より複雑な環境に挑戦
```bash
./switch_environment.sh
# より難しい環境を選択
```

### ステップ6: 必要に応じてカスタムコース作成
- Unityで実際のコース環境を再現

---

## 📊 作成されたファイル

### 新規作成したドキュメント
1. ✅ **QUICK_START_CUSTOM.md** - カスタムコース・性能向上のクイックスタート
2. ✅ **CUSTOM_COURSE_GUIDE.md** - カスタムコース作成の詳細ガイド
3. ✅ **PERFORMANCE_GUIDE.md** - AI性能向上の具体的テクニック
4. ✅ **switch_environment.sh** - 環境切り替えスクリプト

### 更新されたファイル
1. ✅ **mycar/myconfig.py** - 倉庫環境に設定、トレーニングパラメータ最適化
2. ✅ **README.md** - カスタムコースセクション追加
3. ✅ **INDEX.md** - 新しいドキュメントへのリンク追加

---

## 🚀 すぐに始める

### 現在の環境確認
```bash
cat mycar/myconfig.py | grep DONKEY_GYM_ENV_NAME
# 出力: DONKEY_GYM_ENV_NAME = "donkey-warehouse-v0"
```

### データ収集開始
```bash
./start_drive.sh
```

### 環境を変更したい場合
```bash
./switch_environment.sh
```

---

## 💡 重要なポイント

1. **データの質 > データの量**
   - 滑らかで一貫した運転が最も重要

2. **段階的改善**
   - 簡単な環境から始める
   - 徐々に複雑な環境に移行

3. **反復プロセス**
   - データ収集 → トレーニング → テスト → 改善

4. **カスタムコースは最後の手段**
   - まず既存環境で性能を最大化
   - 必要に応じてUnityでカスタム作成

---

## 📚 参考ドキュメント

| ドキュメント | 用途 |
|------------|------|
| [QUICK_START_CUSTOM.md](QUICK_START_CUSTOM.md) | 全体のクイックガイド |
| [CUSTOM_COURSE_GUIDE.md](CUSTOM_COURSE_GUIDE.md) | Unity カスタムコース作成 |
| [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) | 性能向上テクニック |
| [README.md](README.md) | プロジェクト概要 |
| [INDEX.md](INDEX.md) | 全ドキュメント一覧 |

---

## 🎓 次のステップ

1. ✅ **倉庫環境でデータ収集** - 今すぐ始められます
2. ⏳ **モデルトレーニング** - データ収集後
3. ⏳ **オートパイロットテスト** - トレーニング後
4. ⏳ **性能評価と改善** - テスト後
5. ⏳ **他の環境に挑戦** - 習熟後
6. ⏳ **カスタムコース作成** - 必要に応じて

---

**Happy Racing! 🏎️💨**

質問があれば、各ドキュメントを参照してください。すべてのステップが詳しく説明されています！
