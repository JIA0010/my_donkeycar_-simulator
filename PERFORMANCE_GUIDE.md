# シミュレーター性能向上ガイド

## 現在の設定

現在、倉庫環境（`donkey-warehouse-v0`）を使用しています。これはシンプルで制御しやすい環境です。

## 性能を上げるための具体的なステップ

### 1. 高品質なデータ収集（最重要！）

#### データ収集のベストプラクティス:
```bash
# シミュレーターを起動
cd /Users/yoshimurahiro/Desktop/my_donkeycar_-simulator
source env/bin/activate
python mycar/manage.py drive
```

**運転のコツ:**
- 🎯 **中央を走る**: できるだけトラックの中央を維持
- 🐌 **ゆっくり開始**: 最初は遅めのスピードで滑らかに
- 🔄 **一貫性**: 毎回同じラインを走る
- 📊 **データ量**: 最低2000-3000フレーム収集（3-5周）
- ⚠️ **避けるべき**: 急ハンドル、壁への衝突、ジグザグ運転

#### データ収集後の確認:
```bash
# データ数を確認
ls mycar/data/images/ | wc -l

# データが2000以上あることを確認
```

### 2. モデルトレーニングの最適化

#### 現在の最適化済み設定:
```python
# mycar/myconfig.py
MAX_EPOCHS = 150        # より長く学習
EARLY_STOP_PATIENCE = 10  # より多くの改善機会
BATCH_SIZE = 128        # バッチサイズ
LEARNING_RATE = 0.001   # 学習率
```

#### トレーニング実行:
```bash
cd mycar
python train.py --tub ./data --model ./models/mypilot.h5
```

#### 期待される結果:
- Training loss: < 20
- Validation loss: < 25
- 損失が徐々に減少すること

### 3. 異なる環境で試す

#### 環境切り替え方法:

`mycar/myconfig.py`を編集:

```python
# オプション1: 倉庫（シンプル）
DONKEY_GYM_ENV_NAME = "donkey-warehouse-v0"

# オプション2: 道路環境（中級）
DONKEY_GYM_ENV_NAME = "donkey-generated-roads-v0"

# オプション3: 自動生成トラック（上級）
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"

# オプション4: SparkFun AVCコース（実際のコースに近い）
DONKEY_GYM_ENV_NAME = "donkey-avc-sparkfun-v0"
```

### 4. モデルアーキテクチャの変更

#### 異なるモデルタイプを試す:

```python
# mycar/myconfig.py

# オプション1: 線形モデル（デフォルト、シンプル）
DEFAULT_MODEL_TYPE = 'linear'

# オプション2: カテゴリカルモデル（より複雑）
DEFAULT_MODEL_TYPE = 'categorical'

# オプション3: RNN（時系列を考慮）
DEFAULT_MODEL_TYPE = 'rnn'
```

### 5. データ拡張（Data Augmentation）

#### 拡張を有効化:

```python
# mycar/myconfig.py
AUGMENTATIONS = [
    'MULTIPLY',      # 明度調整
    'BLUR',          # ぼかし
    'CROP'           # クロッピング
]
```

### 6. テスト走行での調整

#### オートパイロットで走行:
```bash
cd mycar
python manage.py drive --model ./models/mypilot.h5
```

シミュレーターで:
1. 「Local Pilot」モードに切り替え
2. 車の動作を観察
3. 問題があれば追加データを収集

#### AI スロットル調整:

```python
# mycar/myconfig.py
AI_THROTTLE_MULT = 0.8  # スピードを落とす（0.5-1.5の範囲）
# または
AI_THROTTLE_MULT = 1.2  # スピードを上げる
```

## トラブルシューティング

### 問題: モデルがすぐに壁にぶつかる
**解決策:**
- より多くのデータを収集（特に問題のある箇所）
- スロットルを下げる（`AI_THROTTLE_MULT = 0.6`）
- 中央を走るデータを増やす

### 問題: カーブで外れる
**解決策:**
- カーブを滑らかに走るデータを多く収集
- 学習率を下げる（`LEARNING_RATE = 0.0005`）
- エポック数を増やす（`MAX_EPOCHS = 200`）

### 問題: ジグザグ運転
**解決策:**
- より滑らかな運転データを収集
- バッチサイズを増やす（`BATCH_SIZE = 256`）
- データをクリーンアップ（悪いフレームを削除）

### 問題: 訓練損失が下がらない
**解決策:**
```python
# 学習率を調整
LEARNING_RATE = 0.0001  # より小さく
# または
OPTIMIZER = "rmsprop"  # オプティマイザーを変更
```

## パフォーマンス測定

### 成功の指標:
1. ✅ 3周以上連続で完走できる
2. ✅ 壁にぶつからない
3. ✅ スムーズなライン取り
4. ✅ 一貫したスピード

### データ記録:
```bash
# 走行データを記録
# manage.py driveで走行中、自動的にdata/に保存される
```

## 次のステップ

1. **データ収集** → 3-5周、滑らかに運転
2. **トレーニング** → `python train.py`
3. **テスト** → オートパイロットで走行
4. **評価** → 性能を確認
5. **反復** → 問題箇所でさらにデータ収集

## 高度なテクニック

### カスタム損失関数
```python
# train.pyで高度なカスタマイズ可能
```

### アンサンブル学習
複数のモデルをトレーニングして組み合わせる

### 転移学習
事前トレーニング済みモデルから開始

## 参考リンク

- [Donkey Car Training Tips](https://docs.donkeycar.com/guide/train_autopilot/)
- [Model Types](https://docs.donkeycar.com/parts/keras/)
- [Data Augmentation](https://docs.donkeycar.com/guide/train_autopilot/#data-augmentation)

---

**重要**: 最も重要なのは**高品質なデータ**です。データの質が悪いと、どんなに良いモデルでも性能は上がりません！
