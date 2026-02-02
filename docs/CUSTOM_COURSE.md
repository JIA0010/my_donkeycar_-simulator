# 🎯 カスタムコース作成・性能向上ガイド

**最終更新**: 2026年1月2日

---

## 📝 あなたの要望への回答

**Q: 実際のコースの環境をシミュレートしたい。自分でコースを作れる？赤い壁があって、道は黒い。結構シンプル。ここでの成績を上げたい**

**A: はい、完全に対応可能です！** 以下の3つの方法があります。

---

## ✅ 方法1: 既存環境を使用（最も簡単・推奨）

### 概要
Donkeyシミュレーターには複数のビルトイン環境があります。

### 利用可能な環境

| 環境名 | 特徴 | 推奨度 |
|------|------|--------|
| **倉庫** (`donkey-warehouse-v0`) | シンプル、制御しやすい | ✅ **推奨** |
| **トラック** (`donkey-generated-track-v0`) | 壁付きの自動生成トラック | ⭐ 標準 |
| **道路** (`donkey-generated-roads-v0`) | 開けた道路 | 中級 |
| **AVCコース** (`donkey-avc-sparkfun-v0`) | 実際の競技会場を再現 | 上級 |

### 実施手順

#### ステップ1: 環境切り替え
```bash
./scripts/switch_environment.sh
```

#### ステップ2: 環境を選択
倉庫環境（推奨）またはお好みの環境を選択してください。

#### ステップ3: すぐに開始可能
`mycar/myconfig.py`は既に最適化済みです。

```bash
cd mycar
source ../env/bin/activate
python manage.py drive
```

### 利点
- ✅ 今すぐ使える（セットアップ不要）
- ✅ 複雑な環境では性能向上が容易
- ✅ Unity不要
- ✅ 複数環境で実験可能

---

## ✅ 方法2: Unityでカスタムコース作成（30-60分）

### 概要
赤い壁と黒い道の完全カスタムコースをUnityで作成します。

### 必要環境
- **Unity Hub**: [インストール](https://unity.com/download)
- **Unity 2020.3 LTS** 以降
- **Donkey Simulator ソースコード**
- ディスク容量: 10GB以上

### 作成されるもの

`unity_custom_course/` ディレクトリに完全なパッケージがあります：

```
unity_custom_course/
├── QUICKSTART.md              ← 30分クイックスタート ⭐
├── setup_unity_project.md     ← 詳細セットアップ
├── BUILD_AND_TEST.md          ← ビルドガイド
├── scripts/
│   ├── SimpleTrackGenerator.cs       # トラック自動生成
│   └── RedWallBlackRoadMaterials.cs  # マテリアル設定
└── materials/README.md        ← カスタマイズガイド
```

### クイック手順

#### 1. Donkey Simulatorを取得
```bash
cd ~/Desktop
git clone https://github.com/tawnkramer/sdsandbox
cd sdsandbox
```

#### 2. Unityで開く
- Unity Hubで新規追加 → sdsandboxフォルダを選択
- Unity 2020.3 LTSで開く

#### 3. カスタムスクリプトをコピー
```bash
cp unity_custom_course/scripts/*.cs sdsandbox/Assets/Scripts/
```

#### 4. Unityでシーン作成
- 新規シーンを作成
- `SimpleTrackGenerator` スクリプトをGameObjectに追加
- Playボタンで自動生成

#### 5. ビルド
- File → Build Settings
- Scenes in Buildにシーンを追加
- Build → 場所を選択

#### 6. Donkey Carで使用
```python
# mycar/myconfig.py
DONKEY_SIM_PATH = "/path/to/your/DonkeySimCustom.app"
```

### カスタマイズ可能なパラメータ

`SimpleTrackGenerator.cs`で編集：

```csharp
trackWidth = 4.0f;           // 道路幅
straightLength = 30.0f;      // 直線部分の長さ
curveRadius = 10.0f;         // カーブの半径
wallHeight = 2.0f;           // 壁の高さ
wallThickness = 0.2f;        // 壁の厚さ
roadColor = Color.black;     // 道路の色（黒）
wallColor = Color.red;       // 壁の色（赤）
createOvalTrack = true;      // 楕円形にするか
```

### 詳細ドキュメント
📖 [unity_custom_course/QUICKSTART.md](../unity_custom_course/QUICKSTART.md) - 30分で完成

---

## ✅ 方法3: 性能向上に集中（推奨・最も効果的）

カスタムコースを作るよりも、**既存環境で性能を最大化**する方が効率的です。

### 性能を上げる具体的なステップ

#### 1️⃣ 高品質データ収集（最重要！）

```bash
./scripts/start_drive.sh
```

ブラウザで `http://localhost:8887` を開き、手動走行します。

**運転のコツ:**
- 🎯 トラックの中央を維持
- 🐌 ゆっくり滑らかに運転
- 🔄 同じラインを繰り返す（一貫性が重要）
- 📊 2000-3000フレーム以上収集
- ❌ 急ハンドル、壁への衝突を避ける

**データの質 > 量です。中央を保ったスムーズな走行が最重要です。**

#### 2️⃣ 最適化済みトレーニング設定

既に`mycar/myconfig.py`に最適化済み：

```python
# トレーニングパラメータ（最適化済み）
BATCH_SIZE = 128
TRAIN_TEST_SPLIT = 0.8
MAX_EPOCHS = 150              # 十分な学習期間
EARLY_STOP_PATIENCE = 10      # 改善の余地を与える
MIN_DELTA = 0.0005
USE_EARLY_STOP = True
```

#### 3️⃣ トレーニング実行

```bash
./scripts/train_model.sh
```

または手動で：
```bash
cd mycar
source ../env/bin/activate
python train.py
```

#### 4️⃣ オートパイロットテスト

```bash
./scripts/start_autopilot.sh
```

ブラウザで `http://localhost:8887` を開き、自動走行を観察します。

#### 5️⃣ 反復改善

- 走行結果を観察
- 失敗パターンを追加収集
- 再度トレーニング
- テスト
- 繰り返し

### 性能向上チェックリスト

- [ ] 2000フレーム以上のデータを収集
- [ ] データは中央走行で一貫性がある
- [ ] 急ハンドルやジッターがない
- [ ] エポック数を150以上で学習
- [ ] 損失が安定している
- [ ] 自動走行テストで成功率が上がっている

### 詳細ガイド
📖 [docs/PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)

---

## 🎓 まとめ: 何から始めるか？

### シナリオ1: 今すぐ始めたい
→ **方法1: 既存環境を使用** + **方法3: 性能向上に集中**

```bash
./scripts/start_drive.sh        # データ収集
./scripts/train_model.sh        # 訓練
./scripts/start_autopilot.sh    # テスト
```

**所要時間**: 30分～1時間

### シナリオ2: Unityでオリジナルコースを作りたい
→ **方法2: Unityでカスタムコース作成**

**所要時間**: 30分～2時間

### シナリオ3: すべてをやってみたい
→ **方法1 → 方法3 → 方法2** の順序

---

## 📚 関連ドキュメント

- **クイックスタート**: [docs/GETTING_STARTED.md](GETTING_STARTED.md)
- **性能向上テクニック**: [docs/PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md)
- **Unityカスタムコース**: [unity_custom_course/](../unity_custom_course/)
- **トラブルシューティング**: [docs/TECHNICAL_ISSUES.md](TECHNICAL_ISSUES.md)

---

## 🎯 次のステップ

1. **最初の実行**: `./scripts/start_drive.sh`
2. **データ収集**: ブラウザでしばらく手動運転
3. **訓練**: `./scripts/train_model.sh`
4. **テスト**: `./scripts/start_autopilot.sh`
5. **改善**: データ品質を向上させて再実行

Happy autonomous driving! 🚗✨
